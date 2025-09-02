from flask import Flask, render_template, redirect, url_for, request, session, flash
from collections import Counter
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
from spotipy.cache_handler import FlaskSessionCacheHandler
from dotenv import load_dotenv
import os, random
from model import db, User
from user import user_blueprint
import secrets
from spotipy.exceptions import SpotifyException

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.register_blueprint(user_blueprint, url_prefix="")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
        db.create_all()

load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
REDIRECT_URI = os.environ.get("REDIRECT_URI")
SCOPE = 'user-top-read'

# Takes care of tokens
cache_handler = FlaskSessionCacheHandler(session)

oauth = SpotifyOAuth(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET, 
    redirect_uri=REDIRECT_URI, scope=SCOPE, 
    cache_handler=cache_handler,
)
sp = Spotify(oauth_manager=oauth)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/auth")
def auth():
    token = cache_handler.get_cached_token()
    print("DEBUG: token from cache_handler:", token)
    print("DEBUG: session keys:", session.keys())
    if not token or not oauth.validate_token(token):
        print("DEBUG: No valid token, redirecting to /auth")
        state = secrets.token_urlsafe(16)
        session["oauth_state"] = state
        return redirect(oauth.get_authorize_url(state=state))
    return redirect(url_for('get_stats'))

@app.route("/callback")
def callback():
   print("DEBUG: request.args:", request.args)
   if "error" in request.args:
       flash("Authorization failed!")
       return redirect(url_for('home'))

   state = request.args.get("state")
   print("DEBUG: received state:", state)
   print("DEBUG: session oauth_state:", session.get("oauth_state"))
   if not state or state != session.get("oauth_state"):
       print("DEBUG: Invalid state")
       return "Invalid state", 400

   token = oauth.get_access_token(request.args.get("code"))
   print("DEBUG: obtained token:", token)
   cache_handler.save_token_to_cache(token)
   return redirect(url_for('get_stats'))

@app.route("/get_stats")
def get_stats():
    token = cache_handler.get_cached_token()
    if not token or not oauth.validate_token(token):
        return redirect(url_for('auth'))
    
    sp = Spotify(auth=token['access_token'])
    
    if 'top_artists_names' in session and 'top_tracks_names' in session and 'genres_result' in session:
        top_artists_names = session['top_artists_names']
        top_tracks_names = session['top_tracks_names']
        genres_result = session['genres_result']

    else:
        try:
            top_artists = sp.current_user_top_artists(limit=30, time_range='short_term')["items"]
            top_tracks = sp.current_user_top_tracks(limit=30, time_range='short_term')["items"]
        except SpotifyException:
            return "This app is currently in development mode. Only authorized Spotify test users can use it."

        if len(top_artists) != 0 and len(top_tracks) != 0:
            top_artists_names = [top_artist["name"] for top_artist in top_artists]
            top_tracks_names = [top_track["name"] for top_track in top_tracks]

            genres_counter: dict[str, int] = {}
            for top_artist in top_artists:
                for genre in top_artist["genres"]:
                    genres_counter[genre] = genres_counter.get(genre, 0) + 1
            genres_counter = Counter(genres_counter)
            top_5_genres = genres_counter.most_common(5)
            genres_result = [genre for genre, count in top_5_genres]

            session['top_artists_names'] = top_artists_names
            session['top_tracks_names'] = top_tracks_names
            session['genres_result'] = genres_result

    return render_template("get_stats.html", top_artists=top_artists_names, top_tracks=top_tracks_names, top_genres=genres_result)

if __name__ == "__main__":
    app.run()
