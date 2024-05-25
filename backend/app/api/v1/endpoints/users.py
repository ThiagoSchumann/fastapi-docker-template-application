from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ....models.user import User
from ....schemas.user import UserCreate, UserRead, UserUpdate
from ....services.user import create_user, get_users, get_user, update_user, delete_user
from ....db.session import get_session

router = APIRouter()

@router.post("/users", response_model=UserRead, tags=["Users"])
async def create_new_user(user_in: UserCreate, db: AsyncSession = Depends(get_session)):
    user = await create_user(db=db, user_in=user_in)
    if not user:
        raise HTTPException(status_code=400, detail="User could not be created")
    return user

@router.get("/users", response_model=List[UserRead], tags=["Users"])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session)):
    users = await get_users(db=db, skip=skip, limit=limit)
    return users

@router.get("/users/{user_id}", response_model=UserRead, tags=["Users"])
async def read_user(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/users/{user_id}", response_model=UserRead, tags=["Users"])
async def update_existing_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_session)):
    user = await update_user(db=db, user_id=user_id, user_in=user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/users/{user_id}", response_model=UserRead, tags=["Users"])
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_session)):
    user = await delete_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
