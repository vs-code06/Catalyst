# 🧬 Catalyst

> **Software Digital Twin & Predictive Architecture Intelligence Platform**

Catalyst is not an AI chatbot. It is a **Software Digital Twin** — a living, structured representation of your codebase capable of understanding source code at a semantic level, simulating architectural changes, and predicting their downstream impact before a single line is written.

---

## What Catalyst Does

| Capability | Description |
|---|---|
| **Repository Parsing** | Clones and parses GitHub repositories using Tree-sitter across 5+ languages |
| **AST Construction** | Builds language-agnostic Abstract Syntax Trees with symbol extraction |
| **Dependency Graph** | Constructs module/package dependency graphs stored in Neo4j |
| **Call Graph** | Builds function-level call graphs across the entire codebase |
| **Software Genome** | Encodes the structural DNA of a software system as a graph embedding |
| **Runtime Telemetry** | Collects live Prometheus / OpenTelemetry / Jaeger traces |
| **Architecture Simulation** | Simulates "what if" architectural changes and propagates impact |
| **Impact Prediction** | GNN-based models predict performance, coupling, and risk scores |
| **Architecture Recommendations** | Surfaces optimisation opportunities ranked by predicted impact |

---

## Architecture

Catalyst is organised in **5 layered tiers** where each layer builds on the one below:

```
┌─────────────────────────────────────────────────────┐
│  Presentation Layer  │  API · Dashboard · Reports    │
├─────────────────────────────────────────────────────┤
│  Intelligence Layer  │  Simulation · Prediction      │
│                      │  Optimisation                 │
├─────────────────────────────────────────────────────┤
│  Runtime Layer       │  Telemetry · Metrics          │
├─────────────────────────────────────────────────────┤
│  Knowledge Layer     │  Graph · Architecture Model   │
│                      │  Software Model               │
├─────────────────────────────────────────────────────┤
│  Repository Layer    │  Parser · Symbol Extraction   │
└─────────────────────────────────────────────────────┘
```

---

## Tech Stack

**Backend**: Python 3.12 · FastAPI · Pydantic · SQLAlchemy · Alembic · Celery · Redis · PostgreSQL · Neo4j · Tree-sitter · NetworkX · PyTorch · PyTorch Geometric · OpenTelemetry · Prometheus · Jaeger

**Frontend**: React 18 · TypeScript · Vite · TailwindCSS · React Flow · Cytoscape.js · Zustand · React Query · D3.js

**Infrastructure**: Docker · Docker Compose · GitHub Actions · Kubernetes (future) · Terraform (future)

---

## Getting Started

### Prerequisites
- Docker ≥ 24
- Docker Compose ≥ 2.20
- Python 3.12 (for local development)
- Node.js ≥ 20 (for frontend development)

### Quick Start

```bash
# Clone the repository
git clone https://github.com/your-org/catalyst.git
cd catalyst

# Copy environment config
cp .env.example .env

# Start all services
make dev

# OR using docker-compose directly
docker-compose up --build
```

### Service URLs (local dev)

| Service | URL |
|---|---|
| Backend API | http://localhost:8000 |
| API Docs (Swagger) | http://localhost:8000/docs |
| API Docs (ReDoc) | http://localhost:8000/redoc |
| Frontend | http://localhost:3000 |
| Flower (Celery) | http://localhost:5555 |
| Grafana | http://localhost:3001 |
| Prometheus | http://localhost:9090 |
| Jaeger | http://localhost:16686 |

---

## Project Structure

```
catalyst/
├── backend/          # Python FastAPI backend
├── frontend/         # React TypeScript frontend
├── docs/             # Architecture docs, decisions, roadmap
├── research/         # Research papers, notes, ideas
├── datasets/         # Training and evaluation datasets
├── examples/         # Example repositories for demos
├── infrastructure/   # Docker, Kubernetes, Terraform, monitoring
├── scripts/          # Dev, CI, and database utility scripts
├── tests/            # Top-level integration and e2e tests
├── benchmarks/       # Module performance benchmarks
├── experiments/      # ML experiments (GNN, graph, simulation)
├── tools/            # Developer tools and generators
└── .github/          # GitHub Actions, templates
```

---

## Documentation

- [Product Vision](docs/vision/product-vision.md)
- [System Architecture](docs/architecture/system-overview.md)
- [Layered Module Design](docs/architecture/layered-module-design.md)
- [Development Roadmap](docs/milestones/roadmap.md)
- [API Guide](docs/api/openapi-guide.md)
- [ADR-001: Layered Architecture](docs/decisions/ADR-001-layered-architecture.md)

---

## Development

```bash
make lint          # Run ruff + mypy + eslint
make test          # Run all tests
make test-backend  # Backend tests only
make test-frontend # Frontend tests only
make migrate       # Run Alembic migrations
make worker        # Start Celery workers
```

---

## License

Proprietary. All rights reserved.
