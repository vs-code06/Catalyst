"""
Generic async repository base class.

Provides a consistent interface for all data access objects.
Concrete repositories inherit from this and inject their specific
session/driver type.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")
ID = TypeVar("ID")


class AbstractRepository(ABC, Generic[T, ID]):
    """Abstract base for all domain repositories."""

    @abstractmethod
    async def get_by_id(self, entity_id: ID) -> T | None:
        """Retrieve an entity by its primary identifier."""
        ...

    @abstractmethod
    async def save(self, entity: T) -> T:
        """Persist a new or updated entity and return the saved version."""
        ...

    @abstractmethod
    async def delete(self, entity_id: ID) -> bool:
        """Delete an entity by ID. Returns True if deleted, False if not found."""
        ...

    @abstractmethod
    async def list(self, limit: int = 20, offset: int = 0) -> list[T]:
        """Return a paginated list of entities."""
        ...
