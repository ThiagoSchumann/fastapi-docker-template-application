# src/app/api/v1/endpoints/items.py

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.models.item import Item
from app.schemas import ItemCreate, ItemRead, ItemUpdate
from app.services import create_item, get_items, get_item, update_item, delete_item,  get_user_from_token
from app.db.session import get_session

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/items", response_model=ItemRead, tags=["Items"])
async def create_new_item(item_in: ItemCreate, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    user = await get_user_from_token(db=db, token=token)
    item = await create_item(db, item_in, user)
    if not item:
        raise HTTPException(
            status_code=400, detail="Item could not be created")
    return item


@router.get("/items", response_model=List[ItemRead], tags=["Items"])
async def read_items(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    items = await get_items(db=db, skip=skip, limit=limit)
    return items


@router.get("/items/{item_id}", response_model=ItemRead, tags=["Items"])
async def read_item(item_id: int, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    item = await get_item(db=db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{item_id}", response_model=ItemRead, tags=["Items"])
async def update_existing_item(item_id: int, item_in: ItemUpdate, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    item = await update_item(db=db, item_id=item_id, item_in=item_in)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.delete("/items/{item_id}", response_model=ItemRead, tags=["Items"])
async def delete_existing_item(item_id: int, db: AsyncSession = Depends(get_session), token: str = Depends(oauth2_scheme)):
    item = await delete_item(db=db, item_id=item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item
