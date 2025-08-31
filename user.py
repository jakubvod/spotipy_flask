from flask import Flask, render_template, redirect, url_for, request, session, flash, Blueprint
from model import db, User


user_blueprint = Blueprint("user", __name__, static_folder="static", template_folder="templates")

@user_blueprint.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        
        if len(user) < 3:
            flash("Invalid length! (at least 3 characters)")
            return redirect(url_for("user.login"))

        session["user"] = user
        found = User.query.filter_by(name=user).first()

        if not found:
            usr = User(user, "")
            db.session.add(usr)
            db.session.commit()
        return redirect(url_for("user.user"))

    elif "user" in session:
        flash("Already logged in!")
        return redirect(url_for("user.user"))
    return render_template("login.html")

@user_blueprint.route("/user", methods=["POST", "GET"])
def user():
    if "user" not in session:
        return redirect(url_for("user.login"))
    
    found_user = User.query.filter_by(name=session["user"]).first()

    if request.method == "POST":
        if request.form.get("action") == "Change":
            album = request.form["album"]
            found_user.album = album
            db.session.commit()
            flash("Favourite album changed!")
        elif request.form.get("action") == "Delete":
            found_user.album = ""
            db.session.commit()
            flash("Favourite album removed!")
        else: # Delete account
            db.session.delete(found_user)
            db.session.commit()
            session.pop("user", None)
            flash("User account deleted!")
            return redirect(url_for("user.login"))
    return render_template("user.html", user=found_user)

@user_blueprint.route("/logout")
def logout():
    if "user" not in session:
        flash("Already logged out!")
    else:
        session.pop("user", None)
        flash("Logged out succesfully!")
    return render_template("logout.html")

@user_blueprint.route("/users")
def users():
    return render_template("users.html", user_list=User.query.all())