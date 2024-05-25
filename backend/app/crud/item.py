from sqlmodel import SQLModel, Session, select
from typing import List, Optional
from app.models.item import Item

class CRUDItem:
    def __init__(self, session: Session):
        self.session = session

    def create(self, item: Item) -> Item:
        self.session.add(item)
        self.session.commit()
        self.session.refresh(item)
        return item

    def read(self, item_id: int) -> Optional[Item]:
        return self.session.get(Item, item_id)

    def read_all(self) -> List[Item]:
        return self.session.exec(select(Item)).all()

    def update(self, item_id: int, item_data: Item) -> Optional[Item]:
        item = self.session.get(Item, item_id)
        if not item:
            return None
        item_data.id = item.id
        self.session.merge(item_data)
        self.session.commit()
        self.session.refresh(item_data)
        return item_data

    def delete(self, item_id: int) -> bool:
        item = self.session.get(Item, item_id)
        if not item:
            return False
        self.session.delete(item)
        self.session.commit()
        return True
