# Pydantic Settings & Configuration
# Install Pydantic Settings
# python -m pip install pydantic-settings

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    debug: bool
    database_url: str
    secret_key: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


settings = Settings()

#
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "FastAPI Application"
    debug: bool = False
    database_url: str
    secret_key: str
    api_version: str = "v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()

    #                 ┌──────────────┐
    #                 │    .env      │
    #                 └──────┬───────┘
    #                        ↓
    #             ┌────────────────────┐
    #             │ Pydantic Settings  │
    #             └─────────┬──────────┘
    #                       ↓
    #                 ┌───────────┐
    #                 │ settings  │
    #                 └─────┬─────┘
    #                       ↓
    #       ┌───────────────┼────────────────┐
    #       ↓               ↓                ↓
    #  Database          Security         Application
    #    config            config           config

# Q: Why use Pydantic Settings instead of os.getenv() everywhere?

# A good interview answer:

# Pydantic Settings centralizes application configuration and 
# validates environment variables based on declared types. 
# It also supports .env files and provides a clean, 
# maintainable way to manage configuration across development, 
# testing, and production environments.