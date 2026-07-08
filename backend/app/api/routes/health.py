"""Health check routes."""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    version: str
    environment: str


@router.get("", response_model=HealthResponse, summary="Liveness probe")
async def health_check() -> HealthResponse:
    """Returns 200 OK if the API is alive."""
    from app.core.settings import get_settings
    settings = get_settings()
    return HealthResponse(
        status="healthy",
        version=settings.APP_VERSION,
        environment=settings.APP_ENV,
    )


@router.get("/ready", summary="Readiness probe")
async def readiness_check() -> dict[str, str]:
    """Returns 200 OK when all downstream services are reachable."""
    # TODO: ping Postgres, Neo4j, Redis
    return {"status": "ready"}
