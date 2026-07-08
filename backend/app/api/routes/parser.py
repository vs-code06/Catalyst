"""Parser API routes — repository ingestion and parsing jobs."""

from fastapi import APIRouter, BackgroundTasks, HTTPException, status
from pydantic import BaseModel, HttpUrl

router = APIRouter()


class ParseRepositoryRequest(BaseModel):
    repo_url: HttpUrl
    branch: str = "main"
    language_hints: list[str] = []


class ParseJobResponse(BaseModel):
    job_id: str
    status: str
    repo_url: str


@router.post(
    "/repositories",
    response_model=ParseJobResponse,
    status_code=status.HTTP_202_ACCEPTED,
    summary="Submit a repository for parsing",
)
async def submit_repository(
    request: ParseRepositoryRequest,
    background_tasks: BackgroundTasks,
) -> ParseJobResponse:
    """
    Enqueue a repository for cloning, parsing, and AST + symbol extraction.

    Returns a job ID that can be used to poll status.
    """
    # TODO: validate repo URL
    # TODO: enqueue Celery parser task
    # TODO: return real job ID from task
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Parser module not yet implemented.",
    )


@router.get(
    "/repositories/{job_id}/status",
    response_model=ParseJobResponse,
    summary="Get parse job status",
)
async def get_parse_status(job_id: str) -> ParseJobResponse:
    """Poll the status of a parse job by its ID."""
    # TODO: query Celery task result
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Parser module not yet implemented.",
    )


@router.get(
    "/repositories/{repo_id}/symbols",
    summary="Get extracted symbols for a repository",
)
async def get_symbols(repo_id: str) -> dict:
    """Return all extracted symbols (classes, functions, modules) for a repository."""
    # TODO: query symbol repository
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Parser module not yet implemented.",
    )
