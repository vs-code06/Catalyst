"""
MongoDB async client configuration for Catalyst.

Uses motor.motor_asyncio for async operations.
"""

from __future__ import annotations

from motor.motor_asyncio import AsyncIOMotorClient
from app.core.settings import get_settings


def create_client() -> AsyncIOMotorClient:
    """Create and return the Motor async MongoDB client."""
    settings = get_settings()
    return AsyncIOMotorClient(
        settings.MONGO_URI,
        uuidRepresentation="standard"
    )


# Module-level client instance (initialised at startup)
client: AsyncIOMotorClient | None = None
