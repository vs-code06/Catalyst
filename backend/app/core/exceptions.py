"""
Domain Exception Hierarchy for Catalyst.

All application exceptions inherit from CatalystError.
HTTP mapping is done at the API layer, not here.
"""

from __future__ import annotations


class CatalystError(Exception):
    """Base class for all Catalyst application errors."""

    def __init__(self, message: str, *, code: str | None = None) -> None:
        self.message = message
        self.code = code or self.__class__.__name__
        super().__init__(message)


# ─── Not Found ────────────────────────────────────────────────────────────────

class NotFoundError(CatalystError):
    """Raised when a requested resource does not exist."""


class RepositoryNotFoundError(NotFoundError):
    """Raised when a repository cannot be located."""


class GraphNotFoundError(NotFoundError):
    """Raised when a graph for a repository does not exist."""


# ─── Validation ───────────────────────────────────────────────────────────────

class ValidationError(CatalystError):
    """Raised when input data fails domain validation."""


class UnsupportedLanguageError(ValidationError):
    """Raised when an unsupported programming language is requested."""


# ─── Parsing ──────────────────────────────────────────────────────────────────

class ParseError(CatalystError):
    """Raised when source code cannot be parsed."""


class RepositoryTooLargeError(ParseError):
    """Raised when a repository exceeds the configured size limit."""


# ─── Graph ────────────────────────────────────────────────────────────────────

class GraphBuildError(CatalystError):
    """Raised when graph construction fails."""


class GraphQueryError(CatalystError):
    """Raised when a graph query returns an unexpected result."""


# ─── Simulation ───────────────────────────────────────────────────────────────

class SimulationError(CatalystError):
    """Raised when a simulation fails to execute."""


class ScenarioNotFoundError(SimulationError):
    """Raised when a simulation scenario cannot be found."""


# ─── Prediction ───────────────────────────────────────────────────────────────

class PredictionError(CatalystError):
    """Raised when a prediction model fails."""


class ModelNotLoadedError(PredictionError):
    """Raised when a required ML model is not available."""


# ─── Infrastructure ───────────────────────────────────────────────────────────

class DatabaseError(CatalystError):
    """Raised when a database operation fails."""


class ExternalServiceError(CatalystError):
    """Raised when an external API (GitHub, etc.) returns an error."""
