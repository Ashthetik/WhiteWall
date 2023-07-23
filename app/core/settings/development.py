import logging 
from app.core.settings.app import AppSettings

class DevAppSettings(AppSettings):
    debug: bool = True
    title: str = "Title goes Here"
    logging_level: int = logging.CRITICAL

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"