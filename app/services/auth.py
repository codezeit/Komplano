"""Authentication Service layer"""
from datetime import datetime, timedelta

from ..config import get_settings
from passlib.context import CryptContext
from jose import JWTError, jwt


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(data: dict):
    to_encode = data.copy()
    if settings.access_token_expire_minutes:
        expire = datetime.utcnow() + timedelta(minutes=settings.access_token_expire_minutes)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)
    return encoded_jwt
