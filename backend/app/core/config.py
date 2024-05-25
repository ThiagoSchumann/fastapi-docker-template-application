# backend/app/core/config.py

import os

class Settings:
    APP_NAME = os.getenv("APP_NAME", "My FastAPI Application")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL", "admin@example.com")
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

settings = Settings()
