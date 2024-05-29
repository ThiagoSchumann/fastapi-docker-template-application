# src/app/core/config.py

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = os.getenv("APP_NAME")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY", "f496b7d1bc6a5037f9482e3201c09d16699f01625ffd5aad1e1537e3b9feb11b")
    ALGORITHM = os.getenv("ALGORITHM", 'HS256')
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))


settings = Settings()
