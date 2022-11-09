"""Schemas for User"""
from pydantic import BaseModel


class UserBase(BaseModel):
    """Pydantic Base Class for User"""
    email: str


class UserCreate(UserBase):
    """Pydantic Class for User Creation"""
    password: str
    name: str


class User(UserBase):
    """Pydantic Class for User"""
    id: int
    name: str

    class Config:
        """Pydantic Config Class for User"""
        orm_mode = True
