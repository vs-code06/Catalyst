"""
Shared Enums — Job and resource status.
"""

from enum import StrEnum


class JobStatus(StrEnum):
    """Asynchronous job lifecycle states."""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"
    RETRY = "retry"


class RepositoryStatus(StrEnum):
    """Repository ingestion states."""
    QUEUED = "queued"
    CLONING = "cloning"
    PARSING = "parsing"
    GRAPH_BUILDING = "graph_building"
    READY = "ready"
    ERROR = "error"
