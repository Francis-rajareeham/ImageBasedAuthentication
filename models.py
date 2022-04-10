from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    first_name = db.Column(db.String(150))
    imgname = db.Column(db.Text, nullable=False)
    notes = db.relationship('Note')
    userinterest = db.relationship('userinterests')

class random_obj(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imgnum = db.Column(db.Text, nullable=False)
    name = db.Column(db.Text, nullable=False)

class interestsimg(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imgnum = db.Column(db.Text, nullable=False)
    interestname = db.Column(db.Text, nullable=False)
    imgcategory = db.Column(db.Text, nullable=False)

class userinterests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    interestname = db.Column(db.Text, nullable=False)
