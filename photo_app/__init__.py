from flask import Flask, flash, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required

from photo_app.db import db
from photo_app.admin.views import blueprint as admin_blueprint
from photo_app.main.views import blueprint as main_blueprint
from photo_app.user.models import User
from photo_app.user.views import blueprint as user_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app