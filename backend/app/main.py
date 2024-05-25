# backend/app/main.py

from fastapi import FastAPI
from .db.session import init_db
from .api.v1.endpoints import users, items

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
)


app.include_router(users.router)
app.include_router(items.router)


@app.on_event("startup")
async def on_startup():
    await init_db()
