# Graph Module — Knowledge Layer (L2)

## Responsibility

The Graph module transforms parsed symbols into **structural knowledge graphs**  
stored in Neo4j. It constructs three complementary graph views of a codebase:

1. **Dependency Graph** — module/package-level import relationships
2. **Call Graph** — function-level invocation relationships  
3. **Architecture Graph** — inferred high-level component boundaries

These graphs form the **Software Genome** — the structural DNA that downstream  
Intelligence Layer modules consume.

## Internal Structure

```
graph/
├── builders/
│   ├── dependency/    # Constructs module dependency graph
│   ├── callgraph/     # Constructs function call graph
│   ├── architecture/  # Infers architectural boundaries
│   └── knowledge/     # Merges all views into unified knowledge graph
├── queries/           # Cypher query templates for Neo4j
├── algorithms/        # NetworkX: centrality, clustering, pathfinding
└── visualization/     # Graph export (JSON, GraphML, DOT)
```

## Graph Schema (Neo4j)

| Node Label | Properties |
|---|---|
| `Repository` | id, url, language, last_parsed_at |
| `Module` | id, path, language, loc |
| `Function` | id, name, signature, complexity |
| `Class` | id, name, methods_count |

| Relationship | Meaning |
|---|---|
| `DEPENDS_ON` | Module A imports Module B |
| `CALLS` | Function A calls Function B |
| `CONTAINS` | Module contains Class/Function |
| `PART_OF` | Component belongs to Architectural Layer |

## Dependencies

- **Upstream**: Parser module (symbols, AST)
- **Downstream**: Simulation module, Prediction module
