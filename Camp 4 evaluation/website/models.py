from . import db
from flask_login import UserMixin

class Users(db.Model):
    userId=db.Column(db.Integer, primary_key=True) #primary key
    userName=db.Column(db.String(10))
    userEmail=db.Column(db.String(20))
    #userPassword=db.Column(db.String(20))

    comment=db.relationship('comments')
    blogs=db.relationship('blogPosts')

class BlogPosts(db.Model):
    blogId=db.Column(db.Integer, primary_key=True) #primary key
    blogTitle=db.Column(db.String(20))
    descSmall=db.Column(db.String(500))
    descBig=db.Column(db.String(5000))
    blogDate=db.Column(db.Date)
    userId = db.Column(db.Integer, db.ForeignKey('users.userid')) #foreign key

    comment=db.relationship('comments')

class Comments(db.Model):
    commentId=db.Column(db.Integer, primary_key=True) #primary key
    userComments=db.Column(db.String(100))
    userId = db.Column(db.Integer, db.ForeignKey('users.userid')) #foreign key
    blogId = db.Column(db.Integer, db.ForeignKey('blogposts.blogid')) #foreign key
