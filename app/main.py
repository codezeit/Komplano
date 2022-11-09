"""Main Module"""

from fastapi import FastAPI
from dotenv import load_dotenv
from .db.database import Base, get_engine
from .routers import user, auth

load_dotenv()

Base.metadata.create_all(bind=get_engine())

app = FastAPI(
    title="Komplano API",
    description="The API for the Komplano Chore Management App",
    version="0.1.0",
)
app.include_router(user.router)
app.include_router(auth.router)
