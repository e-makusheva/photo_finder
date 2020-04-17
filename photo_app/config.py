import os

basedir = os.path.abspath(os.path.dirname(__file__))

INSTAGRAM_API_KEY='КЛЮЧ'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'photo_app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "warsdfhdhdghdzfhzdfhfdh47w%7w68"