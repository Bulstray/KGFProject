from pydantic import BaseModel
from pydantic_settings import BaseSettings


class DatabaseConfig(BaseModel):
    url: str = "sqlite+aiosqlite:///database.db"
    echo: bool = False


class Settings(BaseSettings):
    database: DatabaseConfig = DatabaseConfig()


settings = Settings()
