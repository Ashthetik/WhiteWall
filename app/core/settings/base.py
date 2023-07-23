from enum import Enum
from pydantic import BaseSettings

class AppEnvTypes(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "canary"

class BaseAppSettings(BaseSettings):
    app_env: AppEnvTypes = AppEnvTypes.dev

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"