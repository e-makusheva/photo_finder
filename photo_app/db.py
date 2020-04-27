from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

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
