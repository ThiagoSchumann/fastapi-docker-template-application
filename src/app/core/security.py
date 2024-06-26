# src/app/core/security.py

from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import Optional

from .config import settings
from passlib.context import CryptContext
from sqlmodel import SQLModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Token(SQLModel, table=False):
    access_token: str
    token_type: str


class TokenData(SQLModel, table=False):
    username: Optional[str] = None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)
