from flask import Flask
from photo_app.modules import db

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def hello():
        return 'Hello photographer!'
    
    return app

