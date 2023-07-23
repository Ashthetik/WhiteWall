import logging
from pydantic import PostgresDsn, SecretStr
from app.core.settings.app import AppSettings

class TestAppSettings(AppSettings):
    debug: bool = True
    title: str = "title goes here"
    secret_key: SecretStr = SecretStr("test_secret")
    database_url: PostgresDsn
    max_conn_count: int = 5
    min_conn_count: int = 5

    logging_level: int = logging.DEBUG