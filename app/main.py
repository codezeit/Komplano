"""Main Module"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from .db.database import Base, get_engine
from .routers import user, auth
from .config import get_settings

load_dotenv()

Base.metadata.create_all(bind=get_engine())

app = FastAPI(
    title="Komplano API",
    description="The API for the Komplano Chore Management App",
    version="0.1.0",
)

origins = [
    "http://localhost",
    "http://localhost:4200",
    "http://localhost:8000",
]

if get_settings().environment != "test":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(user.router)
app.include_router(auth.router)
