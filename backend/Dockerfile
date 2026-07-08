# ─── Build Stage ──────────────────────────────────────────────────────────────
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONFAULTHANDLER=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System dependencies (tree-sitter native compilation, git for repo cloning)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# ─── Dependencies Stage ───────────────────────────────────────────────────────
FROM base AS dependencies

COPY requirements.txt requirements-dev.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# ─── Development Stage ────────────────────────────────────────────────────────
FROM dependencies AS development

RUN pip install -r requirements-dev.txt

COPY . .

EXPOSE 8000 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

# ─── Production Stage ─────────────────────────────────────────────────────────
FROM dependencies AS production

COPY . .

# Create non-root user
RUN addgroup --system catalyst && adduser --system --group catalyst
RUN chown -R catalyst:catalyst /app
USER catalyst

EXPOSE 8000 8001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
