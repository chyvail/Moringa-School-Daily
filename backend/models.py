from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime


db=SQLAlchemy()

class User(db.Model,SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    email = db.Column(db.String(50), unique= True)
    password = db.Column(db.String(50))
    role = db.Column(db.String(50))


class Content(db.Model,SerializerMixin):
    __tablename__ = 'contents'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(350))
    content_type = db.Column(db.String(50))
    published_date = db.Column(db.DateTime, default=datetime.utcnow) 
    content_url = db.Column(db.String(250))
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    flagged = db.Column(db.Boolean, default = False)
    status = db.Column(db.Boolean, default = True)