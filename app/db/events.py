import asyncpg
from fastapi import FastAPI
from loguru import logger
from app.core.settings.app import AppSettings

async def connect_to_db(
    app:FastAPI, settings:AppSettings
) -> None:
    logger.info("Connecting to {0}", settings.database_url)

    app.state.pool = await asyncpg.create_pool(
        str(settings.database_url),
        min_size=settings.min_conn_count,
        max_size=settings.max_conn_count,
    )

    logger.info("Connection Established")

async def close_db_connection(app:FastAPI) -> None:
    logger.info("Closing connection to database")
    await app.state.pool.close()
    logger.info("Connection closed")