"""
Neo4j driver initialisation for Catalyst.
"""

from __future__ import annotations

from neo4j import AsyncDriver, AsyncGraphDatabase

from app.core.settings import get_settings

_driver: AsyncDriver | None = None


async def get_driver() -> AsyncDriver:
    """Return the module-level Neo4j async driver, initialising if needed."""
    global _driver
    if _driver is None:
        settings = get_settings()
        _driver = AsyncGraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD),
        )
    return _driver


async def close_driver() -> None:
    """Close the Neo4j driver on application shutdown."""
    global _driver
    if _driver is not None:
        await _driver.close()
        _driver = None
