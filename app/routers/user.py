"""User Router."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import crud
from ..db.database import get_db
from ..schemas import user_schemas


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("/", response_model=user_schemas.User)
def create_user(
        user: user_schemas.UserCreate, 
        db: Session = Depends(get_db)
        ):
    """"Creates a new User."""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@router.get("/", response_model=list[user_schemas.User])
def read_users(
        skip: int = 0, 
        limit: int = 100, 
        db: Session = Depends(get_db)
        ):
    """"Returns a list of users."""
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=user_schemas.User)
def read_user(
        user_id: int,
        db: Session = Depends(get_db)
        ):
    """"Returns a single user."""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
