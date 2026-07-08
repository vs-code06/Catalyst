"""Prediction Worker — Celery tasks for GNN-based architectural predictions."""

from __future__ import annotations

from app.workers.celery_app import app


@app.task(name="prediction.run_inference", queue="prediction", bind=True)
def run_prediction_inference(
    self, repo_id: str, target: str, horizon: int = 1
) -> dict:
    """
    Run a GNN inference pass on the repository graph to predict
    the requested target metric.
    """
    # TODO: implement GNN inference pipeline
    raise NotImplementedError
