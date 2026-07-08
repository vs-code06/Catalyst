"""
Application-wide constants for Catalyst.
"""

from __future__ import annotations

# ─── API ──────────────────────────────────────────────────────────────────────
API_VERSION = "v1"
DEFAULT_PAGE_SIZE = 20
MAX_PAGE_SIZE = 100

# ─── Parsing ──────────────────────────────────────────────────────────────────
SUPPORTED_LANGUAGES = frozenset(
    ["python", "typescript", "javascript", "java", "cpp"]
)
MAX_FILE_SIZE_BYTES = 10 * 1024 * 1024  # 10 MB
MAX_REPO_SIZE_MB = 500

# ─── Graph ────────────────────────────────────────────────────────────────────
MAX_GRAPH_DEPTH = 10
DEPENDENCY_EDGE_TYPE = "DEPENDS_ON"
CALL_EDGE_TYPE = "CALLS"
IMPORT_EDGE_TYPE = "IMPORTS"

# ─── Celery Queues ────────────────────────────────────────────────────────────
QUEUE_PARSER = "parser"
QUEUE_GRAPH = "graph"
QUEUE_SIMULATION = "simulation"
QUEUE_PREDICTION = "prediction"
QUEUE_TELEMETRY = "telemetry"

# ─── Cache TTL (seconds) ──────────────────────────────────────────────────────
CACHE_TTL_SHORT = 60          # 1 minute
CACHE_TTL_MEDIUM = 60 * 15   # 15 minutes
CACHE_TTL_LONG = 60 * 60     # 1 hour
CACHE_TTL_DAY = 60 * 60 * 24 # 24 hours

# ─── Telemetry ────────────────────────────────────────────────────────────────
OTEL_SPAN_ATTRIBUTE_REPO = "catalyst.repository"
OTEL_SPAN_ATTRIBUTE_MODULE = "catalyst.module"
OTEL_SPAN_ATTRIBUTE_LANGUAGE = "catalyst.language"
