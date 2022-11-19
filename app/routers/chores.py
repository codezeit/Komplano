"""Chores Router."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import crud
from ..db.database import get_db
from ..schemas import chores_schemas
from ..models.user import User
from ..services import auth


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
def create_chore(chore: chores_schemas.Chore,
                 db: Session = Depends(get_db)):
    """Creates a new Chore."""
    return crud.create_chore(db=db, chore=chore)


@router.post("/{chore_id}",
             response_model=chores_schemas.ChoreDoneReturn)
            #  current_user: User = Depends())
def chore_done(chore_id: int,
               message: chores_schemas.ChoreDoneBase,
               current_user: User = Depends(auth.get_current_user),
               db: Session = Depends(get_db)):
    """Marks chore as done by specific user"""
    user_id = current_user.id
    finished = message.finished
    return crud.chore_done(db=db, chore_id=chore_id,
                           user_id=user_id, finished=finished)
