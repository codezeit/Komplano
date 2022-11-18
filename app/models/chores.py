"""User Class Module"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean

from ..db.database import Base


# pylint: disable=too-few-public-methods
class Chore(Base):
    """Chores Class"""
    __tablename__ = "chores"

    id = Column(Integer, primary_key=True, index=True)
    # TODO: make sure there are no duplicate title/room pairs
    title = Column(String)
    description = Column(String)
    created_by = Column(Integer)
    created_on = Column(DateTime, default=datetime.utcnow())
    room = Column(String)
    is_active = Column(Boolean, default=True)
    flat_id = Column(Integer)
    cycle_days = Column(Integer)  # has to be done every {cycle_days} days


class ChoreLog(Base):
    """Chore logging Class"""
    __tablename__ = "chorelog"

    id = Column(Integer, primary_key=True, index=True)
    chore_id = Column(Integer)  # flat id, room should be obvious from chore id
    user_id = Column(Integer)

# class User(Base):
#     """User Class"""
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String, nullable=False)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     displayname = Column(String)
#     created = Column(DateTime, default=datetime.utcnow())
#     isactive = Column(Boolean)
