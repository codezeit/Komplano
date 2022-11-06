"""Main Module"""
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from dotenv import load_dotenv
from .crud import crud
from .schemas import user_schemas
from .db.database import Base, engine, SessionLocal


Base.metadata.create_all(bind=engine)

load_dotenv()

app = FastAPI()


def get_db():
    """Creates a new database Session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=user_schemas.User)
def create_user(user: user_schemas.UserCreate, db: Session = Depends(get_db)):
    """"Creates a new User."""
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[user_schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """"Returns a list of users."""
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=user_schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """"Returns a single user."""
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
