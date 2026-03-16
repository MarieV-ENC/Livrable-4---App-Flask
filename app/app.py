from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .routes.test import test_bp

# initialisation de flask
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config.from_object(Config)


# connection avec la bdd
db = SQLAlchemy(app)

# Enregistrement du blueprint
app.register_blueprint(test_bp)

from .routes import generales 
from .routes import test