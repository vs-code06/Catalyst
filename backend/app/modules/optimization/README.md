# Optimization Module — Intelligence Layer (L4)

## Responsibility

The Optimization module ranks and recommends **architectural improvements**  
based on predicted impact scores. It operates as a recommendation engine  
on top of simulation and prediction outputs.

## Approach

1. Generate candidate scenarios via simulation
2. Score each scenario using prediction models
3. Rank candidates by multi-objective function (coupling ↓, maintainability ↑, risk ↓)
4. Surface top-N recommendations with explanations

## Architecture

```
optimization/
├── strategies/     # Candidate generation strategies
├── objectives/     # Optimisation objective definitions
├── constraints/    # Constraints (e.g., "do not break public API")
└── recommender/    # Ranking and explanation engine
```

## Dependencies

- **Upstream**: Simulation module, Prediction module
- **Downstream**: API (recommendations endpoint), Dashboard
