from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    user_city = Column(String, nullable=True)
    birthday = Column(String, nullable=True)
    password = Column(String)
    reg_date = Column(DateTime, default=datetime.now())
    post_fk = relationship("UserPost", back_populates="user_fk")

class UserPost(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    main_text = Column(String, nullable=True)
    hashtags = Column(String, ForeignKey("hashtags.hashtag_name"))
    reg_date = Column(String)
    user_fk = relationship("User", lazy="subquery", back_populates="post_fk",
                           cascade="all, delete", passive_deletes=True)
    hashtag_fk = relationship("Hashtags", lazy="subquery")

class Hashtags(Base):
    __tablename__ = "hashtags"
    id = Column(Integer, primary_key=True, autoincrement=True)
    hashtag_name = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

class PostPhoto(Base):
    __tablename__ = "photos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    photo_path = Column(String, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())

    post_fk = relationship("UserPost", lazy="subquery")

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("post.id"))
    comment = Column(String, nullable=False)

    user_fk = relationship("User", lazy="subquery")
    post_fk = relationship("UserPost", lazy="subquery")


