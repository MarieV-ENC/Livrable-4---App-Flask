from flask import Flask, render_template
from flask_login import LoginManager, UserMixin
from ..models.users import login_manager, User
from ..app import app
from ..models import users

@app.route('/')
def test_db():
    return "Connexion réussie!"

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def map_page():
    return render_template("map.html")


@app.route("/search")
def search():
    return render_template("search.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/bird")
def bird_detail():
    return render_template("bird_detail.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/methodology")
def methodology():
    return render_template("methodology.html")


@app.route("/dataviz")
def dataviz():
    return render_template("dataviz.html")


@app.route("/birds")
def birds():
    return render_template("birds.html")


@app.route("/legal")
def legal():
    return render_template("legal.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404