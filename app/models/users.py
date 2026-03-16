from flask_login import LoginManager, UserMixin
from ..app import app

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, id):
        self.id = id