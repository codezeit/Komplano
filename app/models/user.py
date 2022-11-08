"""User Class Module"""
from sqlalchemy import Column, Integer, String

from ..db.database import Base


class User(Base):
    """User Class"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    name = Column(String)
