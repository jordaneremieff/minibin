from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class Paste(db.Model):

    __tablename__ = 'pastes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    password = db.Column(db.String(255))

    def __init__(self, title, content, password):
        self.title = title
        self.content = content
        self.password = password
        _date = datetime.utcnow()
        _date = _date.replace(microsecond=0)
        self.date_created = _date

    def __repr__(self):
        return '<Paste %s %s>' % (self.id, self.date_created)

    def __str__(self):
        return self.id