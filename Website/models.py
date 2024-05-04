from . import db   
from flask_login import UserMixin
from sqlalchemy.sql import func  #for fetching the current timestamp for posting 


#creating a Post Schema model for database

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userId=db.Column(db.Integer, db.ForeignKey('user.id'))
    title=db.Column(db.String(1000))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone=True), default=func.now())






#creating a User Schema model for database 

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    firstName=db.Column(db.String(150))
    lastName=db.Column(db.String(150))
    emailAddress=db.Column(db.String(254),unique=True)
    password=db.Column(db.String(150))
    posts=db.relationship('Post')
