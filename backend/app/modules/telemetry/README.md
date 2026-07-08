# Telemetry Module — Runtime Layer (L3)

## Responsibility

The Telemetry module bridges **static structural analysis** (graph) with  
**dynamic runtime behaviour**. It collects, normalises, and correlates:

- Prometheus metrics (latency, error rates, throughput)
- Jaeger distributed traces (spans, dependencies)
- OpenTelemetry signals (logs, metrics, traces)

Runtime signals are correlated with graph nodes to enrich the Software Genome  
with behavioural data — enabling more accurate simulation and prediction.

## Internal Structure

```
telemetry/
├── collectors/
│   ├── prometheus/   # PromQL query execution, metric scraping
│   ├── jaeger/       # Trace fetching and span analysis
│   └── otel/         # OTLP receiver for push-based telemetry
└── profilers/        # CPU/memory profiling hooks
```

## Key Concepts

- **Service-to-Graph Mapping**: Traces are mapped to graph nodes using service name → module path correlation
- **Metric Enrichment**: Graph nodes gain runtime attributes (p99 latency, error_rate)
- **Anomaly Baseline**: Historical metrics establish performance baselines for simulation

## Dependencies

- **Upstream**: External: Prometheus, Jaeger, OTLP sources
- **Downstream**: Simulation module, Prediction module
