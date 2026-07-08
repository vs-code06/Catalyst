# Prediction Module — Intelligence Layer (L4)

## Responsibility

The Prediction module uses **Graph Neural Networks (GNNs)** to predict  
architectural metrics from the Software Genome. Unlike simulation (rule-based),  
prediction is **learned** — trained on real-world repositories and their  
measured outcomes.

## Prediction Targets

| Target | Description |
|---|---|
| `coupling_score` | Predicted afferent/efferent coupling after a change |
| `performance_risk` | Probability of latency regression |
| `change_impact` | Blast radius — how many nodes are affected |
| `maintainability_index` | Predicted maintainability score |

## Architecture

```
prediction/
├── features/      # Graph feature extraction for GNN input
├── datasets/      # PyTorch Geometric dataset classes
├── models/        # Base model interface
├── training/      # Training loop and checkpointing
├── evaluation/    # Metrics: MAE, RMSE, NDCG
├── inference/     # Production inference pipeline
└── gnn/           # GNN layers (GCN, GAT, GraphSAGE)
```

## Model Architecture

Uses **Graph Attention Networks (GAT)** as the default backbone:
- Node features: LOC, complexity, coupling degree, runtime metrics
- Edge features: dependency type, call frequency
- Output: per-node or per-graph regression/classification

## Dependencies

- **Upstream**: Graph module (graph structure), Telemetry module (runtime features), Simulation module (augmented training data)
- **Downstream**: API (inference results), Optimisation module
