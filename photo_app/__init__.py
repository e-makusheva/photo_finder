from flask import Flask, render_template
from flask_login import LoginManager

from photo_app.forms import LoginForm
from photo_app.modules import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello photographer!'
    
    @app.route('/login')
    def login():
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title=title, form=login_form)
    
    return app