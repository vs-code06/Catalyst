"""Parser Worker — Celery tasks for repository cloning, parsing, and AST building."""

from __future__ import annotations

from app.workers.celery_app import app


@app.task(name="parser.clone_and_parse", queue="parser", bind=True, max_retries=3)
def clone_and_parse_repository(self, repo_url: str, branch: str = "main") -> dict:
    """
    Clone a repository from GitHub and trigger the full parse pipeline:
    1. Clone repository via GitPython
    2. Walk filesystem and filter source files by language
    3. Run Tree-sitter parsing on each file
    4. Extract symbols (functions, classes, imports)
    5. Store results to PostgreSQL
    6. Enqueue graph_worker.build_graphs task
    """
    # TODO: implement parse pipeline
    raise NotImplementedError


@app.task(name="parser.extract_symbols", queue="parser", bind=True)
def extract_symbols(self, repo_id: str, file_path: str) -> dict:
    """Extract symbols from a single source file."""
    # TODO: implement symbol extraction
    raise NotImplementedError
