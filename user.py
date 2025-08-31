from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from model import db, User


user_blueprint = Blueprint("user", __name__, static_folder="static", template_folder="templates")

@user_blueprint.route("/login")
def login():
    return render_template("login.html")