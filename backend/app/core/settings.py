"""
Core Settings — Pydantic BaseSettings for Catalyst.

All configuration is read from environment variables (or a .env file).
Settings are cached as a singleton via lru_cache.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Literal

from pydantic import Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Application ───────────────────────────────────────────────────────────
    APP_NAME: str = "catalyst"
    APP_VERSION: str = "0.1.0"
    APP_ENV: Literal["development", "test", "staging", "production"] = "development"
    DEBUG: bool = False
    SECRET_KEY: str = Field(..., min_length=32)
    API_PREFIX: str = "/api/v1"
    ALLOWED_ORIGINS: list[str] = ["http://localhost:3000"]

    # ── MongoDB ───────────────────────────────────────────────────────────────
    MONGO_URI: str = Field(
        "mongodb://catalyst:catalyst_dev_password@localhost:27017/catalyst?authSource=admin"
    )
    MONGO_DB: str = "catalyst"

    # ── Neo4j ─────────────────────────────────────────────────────────────────
    NEO4J_URI: str = "bolt://localhost:7687"
    NEO4J_USER: str = "neo4j"
    NEO4J_PASSWORD: str = Field(..., min_length=8)

    # ── Redis ─────────────────────────────────────────────────────────────────
    REDIS_URL: str = "redis://localhost:6379/0"

    # ── Celery ────────────────────────────────────────────────────────────────
    CELERY_BROKER_URL: str = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379/1"

    # ── GitHub ────────────────────────────────────────────────────────────────
    GITHUB_TOKEN: str = ""
    GITHUB_API_URL: str = "https://api.github.com"

    # ── Observability ─────────────────────────────────────────────────────────
    OTEL_SERVICE_NAME: str = "catalyst-backend"
    OTEL_EXPORTER_OTLP_ENDPOINT: str = "http://localhost:4317"
    OTEL_SDK_DISABLED: bool = False
    METRICS_ENABLED: bool = True
    LOG_LEVEL: str = "INFO"

    # ── ML ────────────────────────────────────────────────────────────────────
    TORCH_DEVICE: str = "cpu"
    MODEL_REGISTRY_PATH: str = "./models"
    MAX_GRAPH_NODES: int = 50_000

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def parse_allowed_origins(cls, v: str | list[str]) -> list[str]:
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",")]
        return v

    @property
    def is_development(self) -> bool:
        return self.APP_ENV == "development"

    @property
    def is_production(self) -> bool:
        return self.APP_ENV == "production"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached application settings singleton."""
    return Settings()  # type: ignore[call-arg]
