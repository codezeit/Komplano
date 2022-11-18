"""
This is the CRUD-Controler for all database operations
"""
from sqlalchemy.orm import Session
from ..models.user import User
from ..models.chores import Chore
from ..schemas import user_schemas, chores_schemas
from ..services import auth


# User related CRUDs

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
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=auth.get_password_hash(user.password)
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Chores related CRUDs

def get_chores(db: Session, skip: int = 0, limit: int = 100):
    """Get all chores"""
    return db.query(Chore).offset(skip).limit(limit).all()


def create_chore(db: Session, chore: chores_schemas.Chore):
    """Create chore"""
    db_chore = Chore(
        title=chore.title,
        description=chore.description,
        room=chore.room,
        cycle_days=chore.cycle_days,
        flat_id=chore.flat_id
        )
    db.add(db_chore)
    db.commit()
    db.refresh(db_chore)
    return db_chore


# def edit_chore(db: Session):
#     pass
