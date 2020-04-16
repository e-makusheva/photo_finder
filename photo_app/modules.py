from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    roles = db.Column(db.String(64), index=True, unique=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Service_catalog(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return '<Service_catalog {}>'.format(self.service_name) 

class Pricelist(db.Model):
    price_id = db.Column(db.Integer, primary_key=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service_catalog.service_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Pricelist {}>'.format(self.price) 

class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    city = db.Column(db.String(64), nullable=False)
    about = db.Column(db.Text)
    Instagram = db.Column(db.Text, nullable=False)
    contacts = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Profile {}>'.format(self.profile_id) 

