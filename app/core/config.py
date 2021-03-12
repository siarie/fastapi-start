import secrets
from typing import Any, List, Dict, Optional, Union
from pydantic import BaseSettings, AnyHttpUrl


class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    SQLALCHEMY_DATABASE_URI: str

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
