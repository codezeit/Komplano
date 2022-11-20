"""
This is the CRUD-Controler for all database operations
"""
from sqlalchemy.orm import Session
from ..models.user import User
from ..models.flat import Flat
from ..models.chores import Chore, ChoreLog
from ..schemas import user_schemas, chores_schemas
from ..schemas import flat_schemas
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


def chore_done(db: Session, chore_id: int, finished: bool, user_id: int):
    """Marks chore as done"""
    db_done = ChoreLog(
        chore_id=chore_id, user_id=user_id, finished=True
    )
    db.add(db_done)
    db.commit()
    db.refresh(db_done)
    response_dict = {
        "chore_id": db_done.chore_id,
        "date": db_done.date,
        "finished": db_done.finished
    }
    return response_dict


# def edit_chore(db: Session):
#     pass


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
