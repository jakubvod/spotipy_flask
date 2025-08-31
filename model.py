from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    _id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column("name", db.String(100))
    album = db.Column("album", db.String(100))

    def __init__(self, name, album):
        self.name = name
        self.album = album