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
def create_chore(chore: chores_schemas.Chore,
                 db: Session = Depends(get_db)):
    """Creates a new Chore."""
    return crud.create_chore(db=db, chore=chore)
