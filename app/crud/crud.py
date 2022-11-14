"""
This is the CRUD-Controler for all database operations
"""
from sqlalchemy.orm import Session
from ..models.user import User
from ..models.flat import Flat
from ..schemas import user_schemas
from ..schemas import flat_schemas
from ..services import auth


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


def get_flat_by_name(db: Session, name: str):
    """Get flat by name"""
    return db.query(Flat).filter(Flat.name == name).first()


def get_flats(db: Session):
    """Get all flats"""
    return db.query(Flat).all()


def create_flat(db: Session, flat: flat_schemas.FlatCreate):
    """Create flat"""
    db_flat = Flat(
        name=flat.name,
        address=flat.address,
        description=flat.description
        )
    db.add(db_flat)
    db.commit()
    db.refresh(db_flat)
    return db_flat
