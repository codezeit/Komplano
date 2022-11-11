"""User Class Module"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from ..db.database import Base


# pylint: disable=too-few-public-methods
class User(Base):
    """User Class"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    displayname = Column(String)
    created = Column(DateTime, default=datetime.utcnow())
    isactive = Column(Boolean)
    
