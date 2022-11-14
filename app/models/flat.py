"""Flat Class Module"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import relationship

from .connections import flat_user_association
from ..db.database import Base


class Flat(Base):
    """Flat Class"""
    __tablename__ = 'flats'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created = Column(DateTime, default=datetime.utcnow())
    isactive = Column(Boolean)
    users = relationship(
        "User",
        secondary=flat_user_association,
        back_populates="flats"
    )
