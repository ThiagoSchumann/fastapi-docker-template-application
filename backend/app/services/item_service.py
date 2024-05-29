# backend/app/services/item_service.py

from sqlmodel import Session, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Item
from app.schemas import ItemCreate
from typing import List

from app.db.session import get_session


async def get_item(item_id: int, db: AsyncSession) -> Item:
    result = await db.execute(select(Item).where(Item.id == item_id))
    return result.scalar_one_or_none()


async def get_items(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[Item]:
    result = await db.execute(select(Item).offset(skip).limit(limit))
    return result.scalars().all()


async def create_item(db: AsyncSession, item_in: ItemCreate, owner_id: int) -> Item:
    item = Item(**item_in.dict(), owner_id=owner_id)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


async def update_item(item_id: int, item_data: dict, db: AsyncSession) -> Item:
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    if item:
        for key, value in item_data.items():
            setattr(item, key, value)
        db.add(item)
        await db.commit()
        await db.refresh(item)
        return item
    return None


async def delete_item(item_id: int, db: AsyncSession) -> bool:
    result = await db.execute(select(Item).where(Item.id == item_id))
    item = result.scalar_one_or_none()
    if item:
        await db.delete(item)
        await db.commit()
        return True
    return False
