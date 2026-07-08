"""
Celery Application — Catalyst Task Queue.

This module defines the central Celery app instance and configures all queues.
Workers import tasks from their respective module worker files.
"""

from __future__ import annotations

from celery import Celery

from app.core.settings import get_settings

settings = get_settings()

app = Celery(
    "catalyst",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND,
)

app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_track_started=True,
    task_acks_late=True,
    worker_prefetch_multiplier=1,
    result_expires=3600,
    task_routes={
        "app.workers.parser_worker.*": {"queue": "parser"},
        "app.workers.graph_worker.*": {"queue": "graph"},
        "app.workers.simulation_worker.*": {"queue": "simulation"},
        "app.workers.prediction_worker.*": {"queue": "prediction"},
        "app.workers.telemetry_worker.*": {"queue": "telemetry"},
    },
)

# Auto-discover tasks from all worker modules
app.autodiscover_tasks(
    [
        "app.workers.parser_worker",
        "app.workers.graph_worker",
        "app.workers.simulation_worker",
        "app.workers.prediction_worker",
        "app.workers.telemetry_worker",
    ]
)
