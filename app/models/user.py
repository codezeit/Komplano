"""User Class"""
from sqlalchemy import Column, Integer, String

from ..db import database


class User(database.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    email = Column(String, unique=True, index=True)
    name = Column(String)
