.PHONY: help dev stop build test test-backend test-frontend lint format migrate worker logs clean

DOCKER_COMPOSE = docker-compose
BACKEND_SERVICE = backend
WORKER_SERVICE  = worker

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ─── Development ──────────────────────────────────────────────────────────────

dev: ## Start all services in development mode
	$(DOCKER_COMPOSE) up --build

dev-detach: ## Start all services in background
	$(DOCKER_COMPOSE) up --build -d

stop: ## Stop all services
	$(DOCKER_COMPOSE) down

rebuild: ## Rebuild all Docker images without cache
	$(DOCKER_COMPOSE) build --no-cache

logs: ## Tail logs for all services
	$(DOCKER_COMPOSE) logs -f

logs-backend: ## Tail backend logs
	$(DOCKER_COMPOSE) logs -f $(BACKEND_SERVICE)

logs-worker: ## Tail worker logs
	$(DOCKER_COMPOSE) logs -f $(WORKER_SERVICE)

# ─── Testing ──────────────────────────────────────────────────────────────────

test: ## Run all tests
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) pytest backend/tests/ -v
	cd frontend && npm run test

test-backend: ## Run backend tests only
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) pytest backend/tests/ -v --tb=short

test-frontend: ## Run frontend tests only
	cd frontend && npm run test

test-coverage: ## Run backend tests with coverage
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) pytest backend/tests/ --cov=backend/app --cov-report=html

# ─── Code Quality ─────────────────────────────────────────────────────────────

lint: ## Run all linters
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) ruff check backend/
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) mypy backend/app
	cd frontend && npm run lint

format: ## Auto-format code
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) ruff format backend/
	cd frontend && npm run format

typecheck: ## Run mypy type-checking
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) mypy backend/app --strict

# ─── Database ─────────────────────────────────────────────────────────────────

db-create-indexes: ## Create indexes in MongoDB collections
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) python -m app.database.mongodb.client

# ─── Workers ─────────────────────────────────────────────────────────────────

worker: ## Start Celery worker (local)
	cd backend && celery -A app.workers.celery_app worker --loglevel=info

flower: ## Open Flower (Celery monitoring UI)
	open http://localhost:5555

# ─── Utilities ────────────────────────────────────────────────────────────────

install-backend: ## Install Python dependencies
	cd backend && pip install -r requirements.txt -r requirements-dev.txt

install-frontend: ## Install Node dependencies
	cd frontend && npm install

install: install-backend install-frontend ## Install all dependencies

clean: ## Remove all generated artifacts and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name htmlcov -exec rm -rf {} + 2>/dev/null || true
	find . -name "*.pyc" -delete 2>/dev/null || true
	rm -rf frontend/dist frontend/node_modules/.cache 2>/dev/null || true
	@echo "Clean complete."

shell-backend: ## Open a shell in the backend container
	$(DOCKER_COMPOSE) exec $(BACKEND_SERVICE) bash

shell-db: ## Open a MongoDB shell
	$(DOCKER_COMPOSE) exec mongodb mongosh -u catalyst -p catalyst_dev_password --authSource admin catalyst

# ─── Monitoring ───────────────────────────────────────────────────────────────

grafana: ## Open Grafana
	open http://localhost:3001

prometheus: ## Open Prometheus
	open http://localhost:9090

jaeger: ## Open Jaeger UI
	open http://localhost:16686
