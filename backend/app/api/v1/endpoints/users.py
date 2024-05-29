# backend/app/api/v1/endpoints/users.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.models import User
from app.schemas import UserCreate, UserRead, UserUpdate, UserLogin, Token
from app.services import (create_user, get_users,
                          get_user, update_user, delete_user, authenticate_user)
from app.core.security import create_access_token
from app.db.session import get_session

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/users", response_model=UserRead, tags=["Users"])
async def create_new_user(user_in: UserCreate, db: AsyncSession = Depends(get_session)):
    user = await create_user(db=db, user_in=user_in)
    if not user:
        raise HTTPException(
            status_code=400, detail="User could not be created")
    return user


@router.post("/token", response_model=Token, tags=["Users"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=401, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users", response_model=List[UserRead], tags=["Users"])
async def read_users(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    users = await get_users(db=db, skip=skip, limit=limit)
    return users


@router.get("/users/{user_id}", response_model=UserRead, tags=["Users"])
async def read_user(user_id: int, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user = await get_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=UserRead, tags=["Users"])
async def update_existing_user(user_id: int, user_in: UserUpdate, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user = await update_user(db=db, user_id=user_id, user_in=user_in)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/users/{user_id}", response_model=UserRead, tags=["Users"])
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user = await delete_user(db=db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
