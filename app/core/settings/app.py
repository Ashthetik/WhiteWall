import logging, sys
from typing import Any, Dict, List, Tuple
from loguru import logger
from pydantic import PostgresDsn, SecretStr
from app.core.logging import InterceptHandler
from app.core.settings.base import BaseAppSettings

class AppSettings(BaseAppSettings):
    debug: bool = True
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title: str = "Title goes Here"
    version: str = "0.0.1"

    database_url: PostgresDsn
    max_conn_count: int = 10
    min_conn_count: int = 10

    secret_key: SecretStr

    api_prefix: str = "/api"
    jwt_token_prefix = "Token"
    jwt_algorithm = "HS256"

    allowed_hosts: List[str] = ["*"]

    logging_level: int = logging.DEBUG
    loggers: Tuple[str, str] = ("uvicorn.asgi", "uvicorn.access")

    class Config:
        validate_assignment = True
    
    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
            "version": self.version,   
        }

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [InterceptHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [InterceptHandler(
                level=self.logging_level
            )]
        logger.configure(
            handlers=[{
                "sink": sys.stderr,
                "level": self.logging_level
            }]
        )