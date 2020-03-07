# coding: utf-8
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from App.ext import db



class Article(db.Model):
    __tablename__ = 'article'

    aid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.String(10000))
    create_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    cid = db.Column(db.ForeignKey('category.cid', ondelete='CASCADE'), index=True)
    hits = db.Column(db.Integer, server_default=db.FetchedValue())
    comments = db.Column(db.Integer, server_default=db.FetchedValue())
    picture = db.Column(db.String(300))
    category = db.relationship('Category', primaryjoin='Article.cid == Category.cid', backref='articles')
    tid = db.Column(db.Integer)


class Category(db.Model):
    __tablename__ = 'category'

    cid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    num = db.Column(db.Integer, server_default=db.FetchedValue())



class Mark(db.Model):
    __tablename__ = 'mark'

    mid = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000))
    creat_time = db.Column(db.DateTime, server_default=db.FetchedValue())
    uid = db.Column(db.ForeignKey('user.uid'), index=True)

    user = db.relationship('User', primaryjoin='Mark.uid == User.uid', backref='marks')



class Tag(db.Model):
    __tablename__ = 'tag'

    tid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    aid = db.Column(db.ForeignKey('article.aid'), index=True)

    article = db.relationship('Article', primaryjoin='Tag.aid == Article.aid', backref='tags')



class User(db.Model):
    __tablename__ = 'user'

    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    phone = db.Column(db.String(11))
    email = db.Column(db.String(200))
    portrait = db.Column(db.String(300))
    regtime = db.Column(db.DateTime)
    isforbid = db.Column(db.Integer, server_default=db.FetchedValue())
