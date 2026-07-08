# Development Roadmap — Catalyst

This document outlines the development milestones for Catalyst over the next 6-12 months.

---

## 📅 Milestones Overview

### Milestone 1: Core Parsing & Graph Storage (Months 1–3)
- Ingest GitHub repositories
- Run Tree-sitter parsers on Python & TypeScript codebases
- Map symbols to PostgreSQL and build dependency relationships in Neo4j

### Milestone 2: Telemetry Ingestion & Correlation (Months 4–6)
- Build OpenTelemetry receivers
- Pull Prometheus metrics and Jaeger traces
- Corelate runtime metrics to graph nodes

### Milestone 3: Simulation & Impact Engines (Months 7–9)
- Implement rule-based impact propagation algorithms
- Establish baseline scenarios (e.g., microservice extraction)

### Milestone 4: GNN-based Predictions & Recommendations (Months 10–12)
- Train Graph Attention Networks on structural + runtime genomes
- Surface actionable recommendations with explanations
