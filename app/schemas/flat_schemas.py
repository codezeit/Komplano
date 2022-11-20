"""Schemas for Flats"""
from typing import List, Optional
from pydantic import BaseModel

from .user_schemas import User


class FlatBase(BaseModel):
    """Pydantic Base Class for Flat"""
    name: str


class FlatCreate(FlatBase):
    """Pydantic Class for Flat Creation"""
    name: str


class Flat(FlatBase):
    """Pydantic Class for Flat"""
    id: int
    name: str
    users: List[User] = []

    class Config:
        """Pydantic Config Class for Flat"""
        orm_mode = True


class FlatUpdate(FlatBase):
    """Pydantic Class for Flat Update"""
    name: Optional[str] = None
