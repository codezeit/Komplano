"""Schemas for Chores"""
from datetime import datetime
from pydantic import BaseModel


class ChoreBase(BaseModel):
    """Pydantic Base Class for Chore"""
    title: str


class ChoreCreate(ChoreBase):
    """Pydantic Class for Chore creation"""
    title: str  # title has to be given and must be str
    description: str


class Chore(ChoreBase):
    """Pydantic Chore model"""
    id: int
    title: str
    description: str
    # created_by: int
    # created_on: datetime
    # room: str
    # is_active: bool
    # flat_id: int
    # cycle_days: int

    class Config:
        """Pydantic Config Class for Chore"""
        orm_mode = True
