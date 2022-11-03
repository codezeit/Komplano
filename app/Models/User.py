from ..DB import database
from sqlalchemy import Column, ForeignKey, Boolean, Integer, String
from sqlalchemy.orm import relationship

class User(database.Base):
    __tablename__   = 'users'
    
    id              = Column(Integer, primary_key=True, index=True)
    hashed_password = Column(String)
    email           = Column(String, unique=True, index=True)
    name            = Column(String)