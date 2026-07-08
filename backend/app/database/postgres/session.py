"""
PostgreSQL session factory for Catalyst.

Provides an async session context manager for use in FastAPI dependencies
and use-case classes.
"""

from __future__ import annotations

from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.database.postgres.engine import engine


def create_session_factory() -> async_sessionmaker[AsyncSession]:
    """Create an async session factory bound to the module-level engine."""
    if engine is None:
        raise RuntimeError("Database engine has not been initialised.")
    return async_sessionmaker(
        bind=engine,
        expire_on_commit=False,
        autoflush=False,
        autocommit=False,
    )


@asynccontextmanager
async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Async context manager that yields a database session."""
    session_factory = create_session_factory()
    async with session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
