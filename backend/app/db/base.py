# backend/app/db/base.py

from sqlmodel import SQLModel

# Importar todos os modelos que você criar
# Exemplo:
from app.models.user import User
from app.models.item import Item

class Base(SQLModel):
    pass
