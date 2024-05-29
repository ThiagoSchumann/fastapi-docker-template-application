# backend/app/services/user_service.py

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.models.user import User
from app.schemas.user_schema import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password, create_access_token
from app.core.config import settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(name=user_in.name, email=user_in.email,
                hashed_password=hashed_password)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


async def get_user(db: AsyncSession, user_id: int) -> Optional[User]:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()


async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    result = await db.execute(select(User).where(User.email == email))
    return result.scalar_one_or_none()


async def update_user(db: AsyncSession, user_id: int, user_in: UserUpdate) -> Optional[User]:
    user = await get_user(db, user_id)
    if not user:
        return None
    if user_in.password:
        user_in.password = get_password_hash(user_in.password)
    user_data = user_in.dict(exclude_unset=True, exclude={"password"})
    for key, value in user_data.items():
        setattr(user, key, value)
    if user_in.password:
        user.hashed_password = user_in.password
    await db.commit()
    await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user_id: int) -> Optional[User]:
    user = await get_user(db, user_id)
    if not user:
        return None
    await db.delete(user)
    await db.commit()
    return user


async def authenticate_user(db: AsyncSession, email: str, password: str) -> Optional[User]:
    user = await get_user_by_email(db, email)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user


async def get_current_user_email(token: str = Depends(oauth2_scheme)) -> str:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY,
                             algorithms=[settings.ALGORITHM])
        user_email: str = payload.get("sub")
        if user_email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return user_email


async def get_user_from_token(db: AsyncSession, token: str = Depends(oauth2_scheme)) -> Optional[User]:
    user_email = await get_current_user_email(token)
    user = await get_user_by_email(db, user_email)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
