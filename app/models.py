# SQLAlchemy models

from .database import Base
from sqlalchemy import Column, ForeignKey, Boolean, Integer, String
# from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    # is_active = Column(Boolean)
    name = Column(String)
    
# class Group(Base):
#     __tablename__ = 'groups'
    
#     id = Column(Integer, primary_key=True, index=True)
#     # is_active = Column(Boolean)
#     name = Column(String, unique=True)
    
#     creator_id = Column(Integer, ForeignKey('users.id'))
    
#     # add relationship?

