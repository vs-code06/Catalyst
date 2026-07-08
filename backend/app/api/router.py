"""
Top-level API router — aggregates all module routers.
"""

from fastapi import APIRouter

from app.api.routes import health, parser, graph, telemetry, simulation, prediction

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(parser.router, prefix="/parser", tags=["Parser"])
api_router.include_router(graph.router, prefix="/graph", tags=["Graph"])
api_router.include_router(telemetry.router, prefix="/telemetry", tags=["Telemetry"])
api_router.include_router(simulation.router, prefix="/simulation", tags=["Simulation"])
api_router.include_router(prediction.router, prefix="/prediction", tags=["Prediction"])
