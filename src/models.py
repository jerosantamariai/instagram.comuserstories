import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followings = Column(String(250), nullable=False)
    follower_id = Column(Integer, ForeignKey('follower.id'))
    following_id = Column(Integer, ForeignKey('following.id'))

    def serialize(self): # cambiar el objeto python a JSON
        # son los datos q devuelve de la tabla
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email,
            "followings": self.followings,
            "follower_id": self.follower_id,
            "following_id": self.following_id
        }

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id
        }


class Following(Base):
    __tablename__ = 'following'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id
        }

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    photo_id = Column(Integer, ForeignKey('photo.id')) # tabla imaginaria
    photo = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    location = Column(String(250), nullable=False)

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "photo_id": self.photo_id,
            "photo": self.photo,
            "description": self.description,
            "location": self.location
        }

class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    photo_id = Column(Integer, ForeignKey('photo.id'))# tabla no existe
    photo = Column(String(250), nullable=False)
    text = Column(String(250), nullable=False)
    icon = Column(String(250), nullable=False)
    like = Column(Integer, nullable=False)

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "post_id": self.post_id,
            "photo_id": self.photo_id,
            "photo": self.photo,
            "text": self.text,
            "icon": self.icon,
            "like": self.like,
        }


class Direct(Base):
    __tablename__ = 'direct'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    messege_id = Column(Integer, ForeignKey('messege.id'))# tabla no existe
    userOtro_id = Column(Integer, ForeignKey('userOtro.id'))# tabla no existe
    photo_id = Column(Integer, ForeignKey('photo.id'))# tabla no existe
    text = Column(String(250), nullable=False)
    icon = Column(String(250), nullable=False)

    def serialize(self): 
        return {
            "id": self.id,
            "user_id": self.user_id,
            "messege_id": self.messege_id,
            "userOtro_id": self.userOtro_id,
            "photo_id": self.photo_id,
            "text": self.text,
            "icon": self.icon
        }


## Draw from SQLAlchemy base
render_er(Base, 'diagramUML.png')
