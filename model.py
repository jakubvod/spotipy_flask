from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    album = db.Column("album", db.String(100))

    def __init__(self, name, album):
        self.name = name
        self.album = album

class SpotifyUser(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    spotify_id = db.Column(db.String(100), unique=True, nullable=False)
    access_token = db.Column(db.String(500), nullable=False)
    refresh_token = db.Column(db.String(500), nullable=False)
    expires_at = db.Column(db.Integer, nullable=False)