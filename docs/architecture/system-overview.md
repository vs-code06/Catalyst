# System Overview — Catalyst Architecture

This document describes the high-level system architecture of the Catalyst Software Digital Twin platform.

---

## 🏗️ High-Level Component Topology

```mermaid
graph TD
    subgraph Client
        FE[React Frontend / TypeScript / React Flow]
    end

    subgraph API Gateway
        BE[FastAPI Web Server / Motor / Uvicorn]
    end

    subgraph Message Broker
        RD[(Redis)]
        Celery[Celery Task Queue]
    end

    subgraph Data Stores
        MG[(MongoDB)]
        Neo4j[(Neo4j Graph Database)]
    end

    subgraph Worker Tasks
        Parser[Parser Worker / Tree-sitter]
        GraphW[Graph Worker / NetworkX]
        Sim[Simulation Worker]
        Pred[Prediction Worker / PyTorch]
        Telem[Telemetry Worker]
    end

    %% Flow
    FE <-->|REST / WebSockets| BE
    BE -->|Enqueue Task| RD
    RD <--> Celery
    Celery <--> Parser
    Celery <--> GraphW
    Celery <--> Sim
    Celery <--> Pred
    Celery <--> Telem

    Parser -->|Write Symbols| MG
    GraphW -->|Write Graph Relationships| Neo4j
    Sim -->|Read/Write Simulation Runs| MG
    Pred -->|Read Embeddings & Infer| Neo4j
    Telem -->|Query Telemetry| PM[Prometheus / Jaeger]
```

---

## 🏛️ Layered Design

Catalyst organizes its capabilities into a clean, unidirectional stack:

1. **Repository Layer** (`parser`): Ingests raw repository source code, parses files using Tree-sitter, and extracts structural symbols.
2. **Knowledge Layer** (`graph`): Constructs the Software Genome (dependency graphs, call graphs) and saves node relationships to Neo4j.
3. **Runtime Layer** (`telemetry`): Queries dynamic performance data (Prometheus / Jaeger metrics) and links them to graph nodes.
4. **Intelligence Layer** (`simulation`, `prediction`, `optimization`): Executes rule-based simulations and runs GNN predictions to score future changes.
5. **Presentation Layer** (`api`, `frontend`): Provides standard REST endpoints, WebSockets updates, and interactive visualizations.
