"""
This is the CRUD-Controler for all database operations
"""
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas import user_schemas


def get_user(db: Session, user_id: int):
    """Get user by id"""
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """Get all users"""
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db: Session, email: str):
    """Get user by email"""
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: user_schemas.UserCreate):
    """Create user"""
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = User(
        email=user.email,
        hashed_password=fake_hashed_password,
        name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

