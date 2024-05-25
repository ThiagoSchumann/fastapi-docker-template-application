# backend/app/crud/crud_user.py

from sqlmodel import SQLModel, Session, select
from typing import List, Optional
from app.models.user import User

class CRUDUser:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def read(self, user_id: int) -> Optional[User]:
        return self.session.get(User, user_id)

    def read_all(self) -> List[User]:
        return self.session.exec(select(User)).all()

    def update(self, user_id: int, user_data: User) -> Optional[User]:
        user = self.session.get(User, user_id)
        if not user:
            return None
        user_data.id = user.id
        self.session.merge(user_data)
        self.session.commit()
        self.session.refresh(user_data)
        return user_data

    def delete(self, user_id: int) -> bool:
        user = self.session.get(User, user_id)
        if not user:
            return False
        self.session.delete(user)
        self.session.commit()
        return True
