"""Chores Router."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import crud
from ..db.database import get_db
from ..schemas import chores_schemas


router = APIRouter(
    prefix="/chores",
    tags=["Chores"],
)


@router.get("/", response_model=list[chores_schemas.Chore])
def read_chores(skip=0, limit=100,
                db: Session = Depends(get_db)):
    """Returns a list of chores."""
    return crud.get_chores(db, skip=skip, limit=limit)


@router.post("/", response_model=chores_schemas.Chore)
def create_chore(chore: chores_schemas.ChoreCreate,
                 db: Session = Depends(get_db)):
    """Creates a new Chore."""
    return crud.create_chore(db=db, chore=chore)

# @router.post("/", response_model=user_schemas.User)
# def create_user(
#         user: user_schemas.UserCreate,
#         db: Session = Depends(get_db)
#         ):
#     """"Creates a new User."""
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @router.get("/", response_model=list[user_schemas.User])
# def read_users(
#         skip: int = 0,
#         limit: int = 100,
#         db: Session = Depends(get_db)
#         ):
#     """"Returns a list of users."""
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @router.get("/{user_id}", response_model=user_schemas.User)
# def read_user(
#         user_id: int,
#         db: Session = Depends(get_db)
#         ):
#     """"Returns a user."""
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user
