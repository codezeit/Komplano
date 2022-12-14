"""Schemas for Chores"""
from datetime import datetime
from pydantic import BaseModel


# class ChoreBase(BaseModel):
#     """Pydantic Base Class for Chore"""
#     title: str


# class ChoreCreate(ChoreBase):
#     """Pydantic Class for Chore creation"""
#     title: str  # title has to be given and must be str
#     description: str


class Chore(BaseModel):
    """Pydantic Chore model"""
    # id: int
    title: str
    description: str
    created_by: int | None = None
    created_on: datetime | None = None
    room: str | None = None
    is_active: bool | None = None
    flat_id: int | None = None
    cycle_days: int | None = None

    class Config:
        """Pydantic Config Class for Chore"""
        orm_mode = True


class ChoreDoneBase(BaseModel):
    """Pydantic base model for entries in chore done table"""
    finished: bool


class ChoreDoneReturn(ChoreDoneBase):
    """Chore done model for returning when setting chore done"""
    chore_id: int
    # user_id: int
    finished: bool
    date: datetime
