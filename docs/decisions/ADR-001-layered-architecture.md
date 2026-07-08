# ADR 001: Layered Architecture

## Status
Approved

## Context
Catalyst is a platform requiring high modularity. We need to avoid circular dependencies and ensure that static repository parsing is decoupled from dynamic runtime collection and predictive machine learning models.

## Decision
We adopt a strictly layered dependency architecture:
1. **Repository Layer** (parser)
2. **Knowledge Layer** (graph)
3. **Runtime Layer** (telemetry)
4. **Intelligence Layer** (simulation, prediction, optimization)
5. **Presentation Layer** (API, frontend)

Dependencies flow strictly downwards. For example, the Intelligence Layer can query the Knowledge Layer, but the Knowledge Layer cannot import or call anything in the Intelligence Layer.

## Consequences
- Modular code separation.
- Clear development domains for different teams (Parser team, ML/Intelligence team, Platform team).
- Simplifies testing and mock injection.
