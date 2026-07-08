"""Telemetry API routes — runtime metrics and trace ingestion."""

from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/{repo_id}/metrics", summary="Get runtime metrics for a repository")
async def get_runtime_metrics(repo_id: str) -> dict:
    """Return aggregated Prometheus metrics associated with this repository."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Telemetry module not yet implemented.",
    )


@router.get("/{repo_id}/traces", summary="Get distributed traces")
async def get_traces(repo_id: str) -> dict:
    """Return sampled Jaeger traces linked to the given repository."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Telemetry module not yet implemented.",
    )
