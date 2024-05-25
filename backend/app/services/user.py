from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from typing import List

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

async def create_user(db: AsyncSession, user_in: UserCreate) -> User:
    user = User(**user_in.dict())
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_users(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[User]:
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

async def get_user(db: AsyncSession, user_id: int) -> User:
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def update_user(db: AsyncSession, user_id: int, user_in: UserUpdate) -> User:
    user = await get_user(db, user_id)
    if user:
        for key, value in user_in.dict(exclude_unset=True).items():
            setattr(user, key, value)
        db.add(user)
        await db.commit()
        await db.refresh(user)
    return user

async def delete_user(db: AsyncSession, user_id: int) -> User:
    user = await get_user(db, user_id)
    if user:
        await db.delete(user)
        await db.commit()
    return user
