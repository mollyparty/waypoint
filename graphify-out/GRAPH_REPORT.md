# Graph Report - .  (2026-07-30)

## Corpus Check
- Corpus is ~3,150 words - fits in a single context window. You may not need a graph.

## Summary
- 38 nodes · 124 edges · 7 communities
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 20 edges (avg confidence: 0.75)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Obsidian App Settings
- Agent Protocol and Traceability
- Versioning Strategy
- Entry Point and Knowledge Base
- Product and Project Identity
- Memory and Knowledge Graph
- Decision Records

## God Nodes (most connected - your core abstractions)
1. `START HERE (Home Note)` - 24 edges
2. `Session 2026-07-30 Foundation Setup` - 24 edges
3. `Waypoint Agent Protocol` - 16 edges
4. `README Overview` - 14 edges
5. `Changelog` - 12 edges
6. `Versioning Strategy` - 12 edges
7. `Graphify Knowledge Graph` - 10 edges
8. `DEC-001 Trunk-based versioning on main` - 9 edges
9. `Decision Log` - 9 edges
10. `DEC-003 Graphify as queryable project brain` - 8 edges

## Surprising Connections (you probably didn't know these)
- `README Overview` --implements--> `Version-Timestamp Convention`  [INFERRED]
  README.md → docs/VERSIONING.md
- `README Overview` --references--> `Decision Log`  [INFERRED]
  README.md → vault/02-Decisions/_Decision-Log.md
- `START HERE (Home Note)` --conceptually_related_to--> `Session-End Checklist`  [INFERRED]
  vault/00-START-HERE.md → AGENTS.md
- `DEC-003 Graphify as queryable project brain` --references--> `Session-End Checklist`  [INFERRED]
  vault/02-Decisions/DEC-003 Graphify as queryable project brain.md → AGENTS.md
- `Waypoint Agent Protocol` --references--> `Changelog`  [EXTRACTED]
  AGENTS.md → CHANGELOG.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent Memory System (amnesia prevention)** — agents_protocol, start_here_home, dec002_vault_project_memory, dec003_graphify_knowledge_graph, agents_context_retrieval_order, agents_session_end_checklist [INFERRED 0.90]
- **Versioning and Traceability System** — docs_versioning_trunk_based_development, changelog_semantic_versioning, docs_versioning_conventional_commits, changelog_keep_a_changelog, docs_versioning_attribution_footer, changelog_changelog [EXTRACTED 1.00]
- **Decision Record Workflow** — template_decision_record, vault_02_decisions_decision_log_index, dec001_trunk_versioning, dec002_vault_memory, dec003_graphify_brain [EXTRACTED 1.00]

## Communities (7 total, 0 thin omitted)

### Community 2 - "Obsidian App Settings"
Cohesion: 0.33
Nodes (5): alwaysUpdateLinks, newLinkFormat, useMarkdownLinks, attachmentFolderPath, showUnsupportedFiles

### Community 1 - "Agent Protocol and Traceability"
Cohesion: 0.48
Nodes (7): Waypoint Agent Protocol, Session Note Template, Agent Attribution Footer, Version-Timestamp Convention, Post-Commit Graph Rebuild Hook, Session-End Checklist, Engineering Mantra (Security, Stability, Reliability, Compliance)

### Community 0 - "Versioning Strategy"
Cohesion: 0.50
Nodes (9): Changelog, README Overview, Versioning Strategy, DEC-001 Trunk-based versioning on main, Trunk-Based Development, Semantic Versioning, Keep a Changelog Format, Conventional Commits (+1 more)

### Community 4 - "Entry Point and Knowledge Base"
Cohesion: 0.67
Nodes (4): START HERE (Home Note), Knowledge Index, Knowledge Note Template, Context Retrieval Order

### Community 3 - "Product and Project Identity"
Cohesion: 0.80
Nodes (5): Charter, Waypoint (Startup Project), GitHub Repo (mollyparty/waypoint), Session 2026-07-30 Foundation Setup, Your AI Running Coach (Product Concept)

### Community 5 - "Memory and Knowledge Graph"
Cohesion: 0.83
Nodes (4): DEC-002 Obsidian vault as project memory, DEC-003 Graphify as queryable project brain, Obsidian Vault as Project Memory, Graphify Knowledge Graph

### Community 6 - "Decision Records"
Cohesion: 0.67
Nodes (3): Decision Log, Architecture Index, Decision Record Template

## Knowledge Gaps
- **5 isolated node(s):** `alwaysUpdateLinks`, `newLinkFormat`, `useMarkdownLinks`, `attachmentFolderPath`, `showUnsupportedFiles`
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `START HERE (Home Note)` connect `Entry Point and Knowledge Base` to `Versioning Strategy`, `Agent Protocol and Traceability`, `Product and Project Identity`, `Memory and Knowledge Graph`, `Decision Records`?**
  _High betweenness centrality (0.190) - this node is a cross-community bridge._
- **Why does `Session 2026-07-30 Foundation Setup` connect `Product and Project Identity` to `Versioning Strategy`, `Agent Protocol and Traceability`, `Entry Point and Knowledge Base`, `Memory and Knowledge Graph`, `Decision Records`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Why does `Waypoint Agent Protocol` connect `Agent Protocol and Traceability` to `Versioning Strategy`, `Product and Project Identity`, `Entry Point and Knowledge Base`, `Memory and Knowledge Graph`, `Decision Records`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `START HERE (Home Note)` (e.g. with `Context Retrieval Order` and `Session Note Template`) actually correct?**
  _`START HERE (Home Note)` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `Session 2026-07-30 Foundation Setup` (e.g. with `Decision Record Template` and `Knowledge Note Template`) actually correct?**
  _`Session 2026-07-30 Foundation Setup` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `README Overview` (e.g. with `Trunk-Based Development` and `Version-Timestamp Convention`) actually correct?**
  _`README Overview` has 3 INFERRED edges - model-reasoned connections that need verification._
- **What connects `alwaysUpdateLinks`, `newLinkFormat`, `useMarkdownLinks` to the rest of the system?**
  _5 weakly-connected nodes found - possible documentation gaps or missing edges._