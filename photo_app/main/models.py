from datetime import datetime

from photo_app.db import db


class News(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        url = db.Column(db.String, unique=True, nullable=False)
        text = db.Column(db.Text, nullable=True)
    
        def __repr__(self):
            return '<News {} {}>'.format(self.title, self.url)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    news_id = db.Column(
        db.Integer,
        db.ForeignKey('news.id', ondelete='CASCADE'),
        index=True
    )
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )

    def __repr__(self):
        return '<Comment {}>'.format(self.id)