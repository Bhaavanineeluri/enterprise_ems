import os

from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)


BASE_DIR = Path(__file__).resolve().parent.parent


ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "dev"
)


ENV_FILE = BASE_DIR / f".env.{ENVIRONMENT}"


class Settings(BaseSettings):

    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REFRESH_TOKEN_EXPIRE_DAYS: int

    APP_NAME: str

    APP_VERSION: str

    DEBUG: bool

    REDIS_HOST: str = "localhost"

    REDIS_PORT: int = 6379


    ENVIRONMENT: str = ENVIRONMENT


    model_config = SettingsConfigDict(

        env_file=ENV_FILE,

        extra="ignore"

    )
    print("Loading config:", ENV_FILE)


settings = Settings()