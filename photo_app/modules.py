from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    roles = db.Column(db.String(64), index=True, unique=True)

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
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Pricelist {}>'.format(self.price) 

class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    city = db.Column(db.String(64), nullable=False)
    about = db.Column(db.Text)
    Instagram = db.Column(db.Text, nullable=False)
    contacts = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Profile {}>'.format(self.profile_id) 

