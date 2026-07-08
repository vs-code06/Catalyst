"""Prediction API routes — GNN-based architectural impact prediction."""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()


class PredictionRequest(BaseModel):
    repo_id: str
    target: str   # e.g., "coupling_score", "performance_risk", "change_impact"
    horizon: int = 1  # number of hops in graph to consider


@router.post(
    "/predict",
    status_code=status.HTTP_202_ACCEPTED,
    summary="Run a GNN prediction on a repository graph",
)
async def run_prediction(request: PredictionRequest) -> dict:
    """
    Submit a prediction job using the Graph Neural Network models.

    Supported targets:
    - coupling_score: predicted coupling metric after a change
    - performance_risk: risk score for latency degradation
    - change_impact: blast radius of a proposed change
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction module not yet implemented.",
    )


@router.get("/{prediction_id}", summary="Get prediction result")
async def get_prediction_result(prediction_id: str) -> dict:
    """Return results of a previously submitted prediction job."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction module not yet implemented.",
    )


@router.get("/models", summary="List available prediction models")
async def list_models() -> dict:
    """Return metadata for all loaded prediction models."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Prediction module not yet implemented.",
    )
