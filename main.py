from flask import Flask, render_template, Blueprint, redirect, url_for, request, session, flash
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/auth")
def auth():
    return render_template("auth.html")

if __name__ == "__main__":
    app.run(debug=True)