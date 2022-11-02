from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQALCHEMY_DATABASE_URL = 'postgresql://username:password@localhost:5432/default_database'

engine = create_engine(
    SQALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()