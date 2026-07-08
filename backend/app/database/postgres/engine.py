"""
PostgreSQL async engine configuration.

Uses SQLAlchemy 2.x with asyncpg driver.
"""

from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from app.core.settings import get_settings


class Base(DeclarativeBase):
    """Declarative base for all SQLAlchemy ORM models."""


def create_engine() -> AsyncEngine:
    """Create and return the SQLAlchemy async engine."""
    settings = get_settings()
    return create_async_engine(
        settings.DATABASE_URL,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_MAX_OVERFLOW,
        pool_timeout=settings.DB_POOL_TIMEOUT,
        echo=settings.DEBUG,
        future=True,
    )


# Module-level engine instance (initialised at startup)
engine: AsyncEngine | None = None
