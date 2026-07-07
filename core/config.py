from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DATABASE_URL: str

    SECRET_KEY: str

    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES: int

    REFRESH_TOKEN_EXPIRE_DAYS: int

    APP_NAME: str

    APP_VERSION: str

    DEBUG: bool

    class Config:
        env_file = ".env"


settings = Settings()