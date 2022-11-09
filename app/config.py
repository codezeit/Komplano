"""Module with configuration classes and functions."""

import os
from functools import lru_cache
from pydantic import BaseSettings
from dotenv import load_dotenv
print(os.getcwd())
load_dotenv()


class Settings(BaseSettings):
    """Class with settings from .env file."""
    app_name: str = "Awesome API"
    admin_email: str = "test@test.de"
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: int
    postgres_db: str
    environment: str

    class Config:
        """Define name and path of .env file."""
        env_file = ".env"
        env_file_encoding = "utf-8"


# TODO - decide where to put this
@lru_cache()
def get_settings():
    """Function with decorator to cache settings from .env file."""
    return Settings()
