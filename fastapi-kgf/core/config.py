from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseModel):
    url: str = "sqlite+aiosqlite:///database.db"
    echo: bool = False


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600


class Settings(BaseSettings):
    db: DatabaseConfig = DatabaseConfig()
    access_token: AccessToken = AccessToken()


settings = Settings()
