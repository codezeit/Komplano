"""All ORM associations are defined here."""
from sqlalchemy import Column, Integer, ForeignKey, Table
from ..db.database import Base


# Users are living in Flats they can live in multiple Flats
flat_user_association = Table(
    'flat_user_association',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('flat_id', Integer, ForeignKey('flats.id'))
)
