# Simulation Module — Intelligence Layer (L4)

## Responsibility

The Simulation module implements a **graph-based change propagation engine**.  
Given an architectural scenario (e.g., "extract this module as a microservice"),  
it simulates the structural and runtime impact across the dependency graph  
before any code is changed.

## Scenarios

| Scenario | Description |
|---|---|
| `extract_microservice` | Model the impact of decoupling a bounded context |
| `introduce_shared_lib` | Add a shared dependency and model coupling increase |
| `remove_dependency` | Remove an edge and model the blast radius |
| `merge_modules` | Merge two modules and predict cohesion changes |

## Architecture

```
simulation/
├── engine/        # Core simulation loop and graph mutation
├── scenarios/     # Scenario definitions (strategy pattern)
├── rules/         # Propagation rules (how changes spread)
├── propagation/   # Graph traversal for impact propagation
├── evaluators/    # Metric evaluation after propagation
└── metrics/       # Simulation output metrics
```

## Dependencies

- **Upstream**: Graph module (knowledge graph), Telemetry module (runtime baselines)
- **Downstream**: Prediction module (uses simulation results as features)
