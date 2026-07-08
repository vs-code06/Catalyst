"""Telemetry Worker — Celery tasks for runtime telemetry collection."""

from __future__ import annotations

from app.workers.celery_app import app


@app.task(name="telemetry.collect_metrics", queue="telemetry", bind=True)
def collect_runtime_metrics(self, repo_id: str, time_window_minutes: int = 60) -> dict:
    """
    Collect Prometheus metrics and OpenTelemetry traces for the given
    repository within the specified time window.
    """
    # TODO: implement telemetry collection
    raise NotImplementedError
