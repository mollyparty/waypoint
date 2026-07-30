---
type: decision
id: DEC-003
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, memory, tokens]
---

# DEC-003 Graphify as queryable project brain

## Context

Reading raw files to answer project questions burns tokens (credits) and gets slower as the project grows. Waypoint needs cheap, accurate, on-demand context retrieval plus telemetry on what context costs.

## Decision

Graphify (the installed `/graphify` skill, pip package `graphifyy`) maintains a persistent knowledge graph in `graphify-out/`. The git post-commit hook rebuilds the graph from code changes for free (AST, no LLM). Doc changes get incremental `--update` runs at session end. Questions are answered via `graphify query` with token budgets. `graph.json`, `GRAPH_REPORT.md`, and `cost.json` are committed so the graph survives across machines; transient working files are gitignored.

## Rationale

- Persistent graph survives sessions: relationships extracted once are queryable forever.
- Token economics: budgeted BFS traversal of the graph is far cheaper than re-reading folders.
- Telemetry: `cost.json` accumulates per-run token counts, making memory costs visible.
- Honest audit trail: every edge tagged EXTRACTED, INFERRED, or AMBIGUOUS.

## Alternatives considered

- **Vector store / embeddings RAG**: rejected for now; extra infrastructure, opaque retrieval, no audit trail.
- **No index, read files on demand**: rejected; exactly the amnesia and token burn this project wants to avoid.

## Consequences

- Graph must be rebuilt when docs change or it silently goes stale; the session-end protocol owns this.
- The hook only covers code; doc updates are a manual (protocol-enforced) step.

## Related

- [[_Decision-Log]]
- [[DEC-002 Obsidian vault as project memory]]
