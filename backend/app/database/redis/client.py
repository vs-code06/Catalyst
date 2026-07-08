"""
Redis client for Catalyst — caching and pub/sub.
"""

from __future__ import annotations

import redis.asyncio as aioredis

from app.core.settings import get_settings

_client: aioredis.Redis | None = None  # type: ignore[type-arg]


async def get_redis_client() -> aioredis.Redis:  # type: ignore[type-arg]
    """Return the module-level async Redis client."""
    global _client
    if _client is None:
        settings = get_settings()
        _client = aioredis.from_url(
            settings.REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
        )
    return _client


async def close_redis_client() -> None:
    """Close the Redis connection on application shutdown."""
    global _client
    if _client is not None:
        await _client.aclose()
        _client = None
