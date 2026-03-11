from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    url: str = "sqlite+aiosqlite:///database.db"
    echo: bool = False


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    model_settings = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    db: DatabaseConfig = DatabaseConfig()
    access_token: AccessToken


settings = Settings()
