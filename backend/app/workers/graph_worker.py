"""Graph Worker — Celery tasks for building dependency and call graphs."""

from __future__ import annotations

from app.workers.celery_app import app


@app.task(name="graph.build_dependency", queue="graph", bind=True)
def build_dependency_graph(self, repo_id: str) -> dict:
    """
    Build module-level dependency graph from extracted symbols and imports.
    Stores the resulting graph in Neo4j.
    """
    # TODO: implement dependency graph construction
    raise NotImplementedError


@app.task(name="graph.build_callgraph", queue="graph", bind=True)
def build_call_graph(self, repo_id: str) -> dict:
    """Build function-level call graph and store in Neo4j."""
    # TODO: implement call graph construction
    raise NotImplementedError


@app.task(name="graph.build_architecture", queue="graph", bind=True)
def build_architecture_model(self, repo_id: str) -> dict:
    """Infer high-level architectural model from dependency graph."""
    # TODO: implement architecture inference
    raise NotImplementedError
