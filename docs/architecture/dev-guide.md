# Catalyst Developer & Workflow Guide

Welcome to the development team of **Catalyst**. This document serves as your learning path and step-by-step engineering playbook for building the Software Digital Twin platform.

---

## 📚 What to Learn (Prerequisites)

Because Catalyst combines static analysis, graph theory, telemetry, and machine learning, you should focus on these five domains:

### 1. ASTs & Tree-sitter (Repository Layer)
- **Goal**: Understand how code is compiled into syntax trees.
- **What to study**:
  - Abstract Syntax Trees (ASTs) vs. Concrete Syntax Trees (CSTs).
  - [Tree-sitter Documentation](https://tree-sitter.github.io/tree-sitter/): How to load language grammars, walk nodes, and run **Pattern Queries** (S-expressions) to extract symbols without writing complex manual traversals.

### 2. Neo4j & Cypher (Knowledge Layer)
- **Goal**: Model structural code relationships as a graph.
- **What to study**:
  - Graph Database modeling (Nodes, Labels, Relationships, Properties).
  - **Cypher Query Language**: MATCH, MERGE, APOC procedures, and pathfinding (e.g., Shortest Path).
  - Graph metrics: Coupling (Afferent/Efferent), Centrality, and Cohesion (using NetworkX).

### 3. OpenTelemetry & Distributed Tracing (Runtime Layer)
- **Goal**: Correlate dynamic production telemetry to static code entities.
- **What to study**:
  - Distributed tracing standards: Spans, Trace Context, Parent/Child span relationships.
  - OpenTelemetry SDKs (specifically how auto-instrumentation generates span tags).
  - PromQL (Prometheus Query Language) for querying error rates and p99 metrics.

### 4. Graph Neural Networks (Intelligence Layer)
- **Goal**: Train models to predict architectural regressions.
- **What to study**:
  - [PyTorch Geometric (PyG)](https://pytorch-geometric.readthedocs.io/): Loading custom graph structures as PyG `Data` objects.
  - Message-passing architectures: Graph Convolutional Networks (GCN) and Graph Attention Networks (GAT).

---

## 🏗️ Step-by-Step Implementation Workflow

We strongly recommend building Catalyst **vertically, layer-by-layer**. Start with static parsing, visualize it on the frontend, and add ML/dynamic logic later.

```
┌────────────────────────────────────────────────────────┐
│ Phase 5: GNN Predictions & Intelligence                │
└───────────────────▲────────────────────────────────────┘
                    │
┌───────────────────┴────────────────────────────────────┐
│ Phase 4: OpenTelemetry & Runtime Enrichment            │
└───────────────────▲────────────────────────────────────┘
                    │
┌───────────────────┴────────────────────────────────────┐
│ Phase 3: REST API & React Flow Visualization           │
└───────────────────▲────────────────────────────────────┘
                    │
┌───────────────────┴────────────────────────────────────┐
│ Phase 2: Neo4j Graph Builders & Cypher                │
└───────────────────▲────────────────────────────────────┘
                    │
┌───────────────────┴────────────────────────────────────┐
│ Phase 1: Repository Parser & Symbol Ingestion          │
└────────────────────────────────────────────────────────┘
```

---

### 🚀 Phase 1: Repository Parser & Symbol Ingestion (L1)
**Objective**: Successfully clone and parse a single Python source file.
1. Implement the Git cloner under `parser/repository_loader`.
2. Load the Python grammar in `parser/tree_sitter`.
3. Write a simple Tree-sitter query to extract classes, functions, and import statements in a file.
4. Save the result to MongoDB as `ParsedRepository` and `Symbol` collections.

### 🔗 Phase 2: Neo4j Graph Builders (L2)
**Objective**: Build your first dependency graph.
1. Take the symbols from Phase 1.
2. Resolve import targets: If `module_a.py` imports `helper` from `shared.utils`, create a `DEPENDS_ON` relationship in Neo4j between `module_a` and `shared.utils`.
3. Create a call graph parser: Detect function declarations and trace where those functions are invoked within other functions. Write a `CALLS` edge in Neo4j.

### 🎨 Phase 3: REST API & React Flow (L5)
**Objective**: Get a visual end-to-end flow.
1. Create a FastAPI endpoint `/api/v1/graph/{repo_id}/dependency` that pulls nodes and relationships from Neo4j.
2. Format the response into a JSON structure matching React Flow's node/edge properties.
3. In the React frontend, load this data and render it inside the `DependencyGraph` component using `React Flow` to visualize your system modules.

### ⚡ Phase 4: Runtime Correlation (L3)
**Objective**: overlay real CPU/latency data on the code graph.
1. Run a sample application instrumented with OpenTelemetry.
2. In Catalyst, query Jaeger traces and match Span names to function symbols in your graph.
3. Decorate the Neo4j nodes with runtime attributes (e.g. `FunctionNode { name: "execute", p99_latency: "250ms" }`).

### 🧠 Phase 5: GNN Predictions & Simulation (L4)
**Objective**: The digital twin predicts impact.
1. Write simulation logic to propagate change rules (e.g., if class X changes, find all transitive callers up to depth 3).
2. Model node and edge features as tensors for PyTorch Geometric.
3. Train a basic GAT model to predict whether changing module A will lead to latency spikes in module B.
