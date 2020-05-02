from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

from photo_app.db import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    roles = db.Column(db.String(64), index=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.roles == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    fullname = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), nullable=False)
    about = db.Column(db.Text)
    Instagram = db.Column(db.Text, nullable=False)
    contacts = db.Column(db.Text, nullable=False)
    user = relationship('User', backref='profile')

    def __repr__(self):
        return '<Profile № {}>'.format(self.fullname) 