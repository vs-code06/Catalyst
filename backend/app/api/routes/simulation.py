"""Simulation API routes — architectural change simulation."""

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()


class SimulationRequest(BaseModel):
    repo_id: str
    scenario: str
    parameters: dict = {}


class SimulationResponse(BaseModel):
    simulation_id: str
    status: str
    scenario: str


@router.post(
    "/run",
    response_model=SimulationResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Run an architectural simulation",
)
async def run_simulation(request: SimulationRequest) -> SimulationResponse:
    """
    Submit a simulation scenario for execution.

    Scenarios describe architectural changes (e.g., extract microservice,
    introduce shared library) and the engine propagates their impact.
    """
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Simulation module not yet implemented.",
    )


@router.get("/{simulation_id}", summary="Get simulation result")
async def get_simulation_result(simulation_id: str) -> dict:
    """Return the result of a previously submitted simulation."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Simulation module not yet implemented.",
    )


@router.get("/scenarios", summary="List available simulation scenarios")
async def list_scenarios() -> dict:
    """List all available simulation scenario types."""
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Simulation module not yet implemented.",
    )
