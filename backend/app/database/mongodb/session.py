"""
MongoDB database connection and dependency injection helpers for Catalyst.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from motor.motor_asyncio import AsyncIOMotorDatabase

from app.core.settings import get_settings
from app.database.mongodb import client as mongodb_client


def get_database() -> AsyncIOMotorDatabase:
    """Retrieve the database instance from the module-level client."""
    if mongodb_client.client is None:
        raise RuntimeError("MongoDB client has not been initialised.")
    settings = get_settings()
    return mongodb_client.client[settings.MONGO_DB]


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncIOMotorDatabase, None]:
    """Async context manager yielding the database instance."""
    db = get_database()
    yield db


async def get_db() -> AsyncGenerator[AsyncIOMotorDatabase, None]:
    """FastAPI dependency that yields the MongoDB database instance."""
    db = get_database()
    yield db
