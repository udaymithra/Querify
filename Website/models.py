from . import db   
from flask_login import UserMixin
from sqlalchemy.sql import func  #for fetching the current timestamp for posting 
from flask_login import current_user

#creating a Post Schema model for database

class Post(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userId=db.Column(db.Integer, db.ForeignKey('user.id'))
    title=db.Column(db.String(1000))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone='Asia/Kolkata'), default=func.date(func.now()))
    






#creating a User Schema model for database 

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    firstName=db.Column(db.String(150))
    lastName=db.Column(db.String(150))
    emailAddress=db.Column(db.String(254),unique=True)
    password=db.Column(db.String(150))
    posts=db.relationship('Post')




def get_user_id():
    return current_user.id if current_user.is_authenticated else None

class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postId = db.Column(db.Integer, db.ForeignKey('post.id'))
    userId = db.Column(db.Integer, default=get_user_id)
 

class Comments(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    postId=db.Column(db.Integer, db.ForeignKey('post.id'))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone='Asia/Kolkata'), default=func.date(func.now()))

class Reply(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    commentId=db.Column(db.Integer, db.ForeignKey('comments.id'))
    content=db.Column(db.Text)
    date=db.Column(db.DateTime(timezone='Asia/Kolkata'), default=func.date(func.now()))
    repliedBy=db.Column(db.Text)
    repliedTo=db.Column(db.Text)
    postId=db.Column(db.Integer)
    userId=db.Column(db.Integer)

class CommentsLike(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    commentId=db.Column(db.Integer, db.ForeignKey('comments.id'))
    userId=db.Column(db.Integer)
    
    


    

