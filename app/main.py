"""Main Module"""

from fastapi import FastAPI
from dotenv import load_dotenv
from .db.database import SessionLocal, Base, get_engine
from .routers import user

load_dotenv()

Base.metadata.create_all(bind=get_engine())

app = FastAPI()
app.include_router(user.router)
