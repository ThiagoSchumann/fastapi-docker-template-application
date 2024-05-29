# backend/app/main.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db import init_db
from app.api.v1.endpoints import users, items

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa antes da aplicação começar a receber requisições
    await init_db()
    yield
    # Executa após a aplicação parar de receber requisições (se necessário, adicione lógica de limpeza aqui)

# Cria a aplicação FastAPI e passa a função lifespan
app = FastAPI(
    title="Template Criação de APIs",
    description="Esta é a descrição da minha API.",
    version="1.0.0",
    contact={
        "name": "Thiago Artur Schumann",
        "url": "https://github.com/ThiagoSchumann",
        "email": "thiagoarturschumann@gmail.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
    lifespan=lifespan  # Configura o lifespan para gerenciar o ciclo de vida
)

# Inclui os roteadores dos endpoints
app.include_router(users.router)
app.include_router(items.router)
