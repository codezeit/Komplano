"""
Database Connector
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config import get_settings

Base = declarative_base()
settings = get_settings()


def get_db_url():
    """Returns the database url."""
    sqlalchemy_database_url = 'postgresql://{}:{}@{}:{}/{}'.format(
        settings.postgres_user,
        settings.postgres_password,
        settings.postgres_host,
        settings.postgres_port,
        settings.postgres_db
    )
    return sqlalchemy_database_url


def get_test_db_url():
    """Returns the database url."""
    sqlalchemy_database_url = 'sqlite:///./test.db'
    return sqlalchemy_database_url


def get_engine():
    """Creates a new database Session."""
    engine = create_engine(
        get_test_db_url() if settings.environment=="test" else get_db_url(),
        connect_args={"check_same_thread": False} if settings.environment=="test" else {}
    )

    return engine


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=get_engine()
    )


def get_db():
    """Creates a new database Session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
