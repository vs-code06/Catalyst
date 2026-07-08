"""Graph API routes — dependency, call, and architecture graphs."""

from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get(
    "/{repo_id}/dependency",
    summary="Get dependency graph for a repository",
)
async def get_dependency_graph(repo_id: str) -> dict:
    """
    Return the module-level dependency graph for the given repository
    as a JSON node-link structure compatible with React Flow / Cytoscape.
    """
    # TODO: query Neo4j for dependency graph
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Graph module not yet implemented.",
    )


@router.get(
    "/{repo_id}/callgraph",
    summary="Get call graph for a repository",
)
async def get_call_graph(repo_id: str) -> dict:
    """Return the function-level call graph for the given repository."""
    # TODO: query Neo4j for call graph
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Graph module not yet implemented.",
    )


@router.get(
    "/{repo_id}/architecture",
    summary="Get high-level architecture graph",
)
async def get_architecture_graph(repo_id: str) -> dict:
    """Return the inferred architectural view (layers, components, boundaries)."""
    # TODO: query Knowledge Layer graph
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Graph module not yet implemented.",
    )


@router.get(
    "/{repo_id}/metrics",
    summary="Get graph-level software metrics",
)
async def get_graph_metrics(repo_id: str) -> dict:
    """Return graph metrics: coupling, cohesion, centrality, clustering coefficient."""
    # TODO: compute NetworkX metrics from stored graph
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Graph module not yet implemented.",
    )
