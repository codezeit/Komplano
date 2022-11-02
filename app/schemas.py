# Pydantic models

from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str
    name: str
    
class User(UserBase):
    id: int
    name: str
    
    class Config:
        orm_mode = True