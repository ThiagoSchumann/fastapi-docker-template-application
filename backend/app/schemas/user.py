from sqlmodel import SQLModel
from typing import Optional

class UserCreate(SQLModel):
    name: str
    email: str

class UserRead(SQLModel):
    id: int
    name: str
    email: str
    is_active: bool

class UserUpdate(SQLModel):
    name: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None
