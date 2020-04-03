from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username) 

class Service_catalog(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return '<Service_catalog {}>'.format(self.service_name) 