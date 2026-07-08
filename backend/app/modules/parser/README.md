# Parser Module — Repository Layer (L1)

## Responsibility

The Parser module is the **entry point** for all source code ingestion.  
It is responsible for cloning repositories, walking their file systems,  
and building language-agnostic **Abstract Syntax Trees (ASTs)** with full  
symbol extraction.

No other module feeds this one. Every other module depends on its output.

## Capabilities

| Capability | Description |
|---|---|
| Repository cloning | Clone public/private GitHub repos via GitPython + GitHub API |
| Language detection | Detect language by file extension + heuristics |
| Tree-sitter parsing | Build ASTs using Tree-sitter grammars for 5 languages |
| Symbol extraction | Extract functions, classes, imports, exports, decorators |
| Visitor pattern | Pluggable AST visitors for language-specific analysis |

## Supported Languages

- Python 3.x
- TypeScript / JavaScript
- Java 8+
- C/C++

## Internal Structure

```
parser/
├── github/              # GitHub API client (repo metadata, auth)
├── repository_loader/   # Git clone + filesystem walker
├── languages/           # Per-language parser implementations
├── tree_sitter/         # Tree-sitter engine + grammar management
├── ast/                 # AST node types and builder
├── symbols/             # Symbol extraction and symbol domain model
├── visitors/            # Base visitor + per-language visitors
└── queries/             # Tree-sitter query definitions per language
```

## Output

Produces `ParsedRepository` domain objects stored in PostgreSQL.  
Enqueues `graph_worker.build_dependency` after completion.

## Dependencies

- **Upstream**: GitHub API, local filesystem
- **Downstream**: Graph module (consumes parsed symbols)

## Development Notes

- All Tree-sitter grammars are compiled at container build time
- Symbol extraction is idempotent — re-parsing the same commit is a no-op
- Large repos (> 500 MB) are rejected at the API layer
