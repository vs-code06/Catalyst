"""
Catalyst Backend — Application Entry Point

This module bootstraps the FastAPI application, registers all middleware,
mounts all API routers, and wires up the lifespan context manager for
startup/shutdown hooks.
"""

from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging, get_logger
from app.database.mongodb import client as mongodb_client


settings = get_settings()


@asynccontextmanager
async def lifespan(application: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan — handles startup and graceful shutdown."""
    configure_logging()
    logger = get_logger(__name__)

    logger.info("Starting up Catalyst application...")

    # Initialise MongoDB connection
    logger.info("Initialising MongoDB client...")
    mongodb_client.client = mongodb_client.create_client()
    try:
        # Verify MongoDB is reachable
        await mongodb_client.client.admin.command("ping")
        logger.info("MongoDB client connected successfully.")
    except Exception as e:
        logger.error("Failed to connect to MongoDB", error=str(e))
        raise

    # TODO: initialise Neo4j driver
    # TODO: initialise Redis client
    # TODO: configure OpenTelemetry

    yield

    logger.info("Shutting down Catalyst application...")
    if mongodb_client.client is not None:
        logger.info("Closing MongoDB client...")
        mongodb_client.client.close()
        logger.info("MongoDB client closed.")


def create_application() -> FastAPI:
    """Application factory — constructs and configures the FastAPI instance."""
    application = FastAPI(
        title="Catalyst API",
        description=(
            "Software Digital Twin & Predictive Architecture Intelligence Platform"
        ),
        version=settings.APP_VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )

    # ── CORS ──────────────────────────────────────────────────────────────────
    application.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # ── Routers ───────────────────────────────────────────────────────────────
    application.include_router(api_router, prefix=settings.API_PREFIX)

    return application


app = create_application()
