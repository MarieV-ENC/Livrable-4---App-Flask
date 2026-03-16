from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

# initialisation de flask
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

app.config.from_object(Config)


# connection avec la bdd
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = Config().SQLALCHEMY_DATABASE_URI 


from .routes import generales 
from .routes import test