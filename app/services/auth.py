"""Authentication Service layer"""
from datetime import datetime, timedelta
from passlib.context import CryptContext
from jose import jwt
from ..config import get_settings


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()


def verify_password(plain_password, hashed_password):
    """Verify a password against a hashed password"""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Hash a password"""
    return pwd_context.hash(password)


def create_access_token(data: dict):
    """Create an access token with JWT"""
    to_encode = data.copy()
    if settings.access_token_expire_minutes:
        expire = datetime.utcnow() + \
            timedelta(minutes=settings.access_token_expire_minutes)
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.secret_key,
        algorithm=settings.algorithm)
    return encoded_jwt
