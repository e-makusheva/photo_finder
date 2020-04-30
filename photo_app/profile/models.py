from photo_app.db import db
from sqlalchemy.orm import relationship

class Profile(db.Model):
    profile_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), index=True)
    city = db.Column(db.String(64), nullable=False)
    about = db.Column(db.Text)
    Instagram = db.Column(db.Text, nullable=False)
    contacts = db.Column(db.Text, nullable=False)
    user = relationship('User', backref='profile')

    def __repr__(self):
        return '<Profile № {}>'.format(self.profile_id) 
