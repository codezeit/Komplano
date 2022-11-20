"""Flats Router."""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import crud
from ..db.database import get_db
from ..models.flat import Flat
from ..models.user import User
from ..schemas import flat_schemas
from ..services import auth

router = APIRouter(
    prefix="/flats",
    tags=["Flats"],
)


@router.post("/", response_model=flat_schemas.Flat)
def create_flat(
        flat: flat_schemas.FlatCreate,
        db: Session = Depends(get_db)
        ):
    """"Creates a new Flat."""
    db_flat = crud.get_flat_by_name(db, name=flat.name)
    if db_flat:
        raise HTTPException(status_code=400, detail="Flat already registered")
    return crud.create_flat(db=db, flat=flat)


@router.get("/", response_model=list[flat_schemas.Flat])
def get_flats(
        db: Session = Depends(get_db)
        ):
    """"Returns a list of flats."""
    flats = crud.get_flats(db)
    return flats
