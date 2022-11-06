"""
Database Connector
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import get_settings

settings = get_settings()

SQALCHEMY_DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(
    settings.postgres_user,
    settings.postgres_password,
    settings.postgres_host,
    settings.postgres_port,
    settings.postgres_db
)


engine = create_engine(
    SQALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
