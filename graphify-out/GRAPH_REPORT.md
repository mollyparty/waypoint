# Graph Report - .  (2026-07-30)

## Corpus Check
- Corpus is ~4,889 words - fits in a single context window. You may not need a graph.

## Summary
- 53 nodes · 181 edges · 9 communities
- Extraction: 84% EXTRACTED · 15% INFERRED · 1% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.74)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Cross-IDE and Continuous Push
- Product and Project Identity
- Versioning Strategy
- Changelog and Milestones
- Entry Point and Vault Structure
- Obsidian App Settings
- Memory and Knowledge Graph
- Graphify Operations
- Trunk-Based Development

## God Nodes (most connected - your core abstractions)
1. `START HERE (Home Note)` - 32 edges
2. `Session 2026-07-30 Foundation Setup` - 25 edges
3. `Waypoint Agent Protocol` - 23 edges
4. `README Overview` - 19 edges
5. `Versioning Strategy` - 19 edges
6. `DEC-001 Trunk-based versioning on main` - 14 edges
7. `Changelog` - 12 edges
8. `Graphify Knowledge Graph` - 11 edges
9. `CONTRIBUTING.md (collaborator onboarding doc)` - 11 edges
10. `Session 2026-07-30 - Continuous Push and Cross-IDE Setup` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Your AI Running Coach (Product Concept)` --conceptually_related_to--> `Knowledge Index`  [AMBIGUOUS]
  README.md → vault/04-Knowledge/_Knowledge-Index.md
- `Waypoint Agent Protocol` --references--> `Engineering Mantra (Security, Stability, Reliability, Compliance)`  [EXTRACTED]
  AGENTS.md → vault/01-Project/Charter.md
- `README Overview` --references--> `Decision Log`  [INFERRED]
  README.md → vault/02-Decisions/_Decision-Log.md
- `Versioning Strategy` --references--> `Keep a Changelog Format`  [EXTRACTED]
  docs/VERSIONING.md → CHANGELOG.md
- `START HERE (Home Note)` --conceptually_related_to--> `Context Retrieval Order`  [INFERRED]
  vault/00-START-HERE.md → AGENTS.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent Memory System (amnesia prevention)** — agents_protocol, start_here_home, dec002_vault_project_memory, dec003_graphify_knowledge_graph, agents_context_retrieval_order, agents_session_end_checklist [INFERRED 0.90]
- **Versioning and Traceability System** — docs_versioning_trunk_based_development, changelog_semantic_versioning, docs_versioning_conventional_commits, changelog_keep_a_changelog, docs_versioning_attribution_footer, changelog_changelog [EXTRACTED 1.00]
- **Decision Record Workflow** — template_decision_record, vault_02_decisions_decision_log_index, dec001_trunk_versioning, dec002_vault_memory, dec003_graphify_brain [EXTRACTED 1.00]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Cross-IDE and Continuous Push"
Cohesion: 0.71
Nodes (8): Waypoint Agent Protocol, CLAUDE.md (Claude Code pointer file), Cross-IDE / cross-tool compatibility (Cursor, Codex CLI, Claude Code, Gemini CLI, others), .gitattributes line-ending normalization (eol=lf), CONTRIBUTING.md (collaborator onboarding doc), DEC-004: Continuous push and cross-IDE agent files, Continuous push policy (commit and push after every meaningful unit of work), Session 2026-07-30 - Continuous Push and Cross-IDE Setup

### Community 1 - "Product and Project Identity"
Cohesion: 0.38
Nodes (7): Charter (Waypoint product charter stub), Engineering mantra: security, stability, reliability, compliance, Knowledge Index, Your AI Running Coach (Product Concept), Waypoint (Startup Project), Charter, Engineering Mantra (Security, Stability, Reliability, Compliance)

### Community 2 - "Versioning Strategy"
Cohesion: 0.48
Nodes (7): Agent Attribution Footer, Versioning Strategy, Trunk-Based Development, Version-Timestamp Convention, README Overview, Trunk-based development model, Version-Timestamp versioned-artifact header

### Community 3 - "Changelog and Milestones"
Cohesion: 0.47
Nodes (6): Changelog, Keep a Changelog Format, Semantic Versioning, Conventional Commits, Session 2026-07-30 Foundation Setup, GitHub Repo (mollyparty/waypoint)

### Community 4 - "Entry Point and Vault Structure"
Cohesion: 0.53
Nodes (6): START HERE (Home Note), Decision Record Template, Knowledge Note Template, Decision Log, Knowledge Index, Architecture Index

### Community 5 - "Obsidian App Settings"
Cohesion: 0.33
Nodes (5): alwaysUpdateLinks, attachmentFolderPath, newLinkFormat, showUnsupportedFiles, useMarkdownLinks

### Community 6 - "Memory and Knowledge Graph"
Cohesion: 0.50
Nodes (5): Context Retrieval Order, DEC-002 Obsidian vault as project memory, Obsidian Vault as Project Memory, Graphify Knowledge Graph, Session Note Template

### Community 7 - "Graphify Operations"
Cohesion: 0.50
Nodes (5): Session-End Checklist, Token Cost Telemetry, DEC-003 Graphify as queryable project brain, Post-Commit Graph Rebuild Hook, Decision Log index

### Community 8 - "Trunk-Based Development"
Cohesion: 0.67
Nodes (3): DEC-001 Trunk-based versioning on main, Agent-Attribution commit footer, Conventional Commits convention

## Ambiguous Edges - Review These
- `Your AI Running Coach (Product Concept)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to
- `Charter (Waypoint product charter stub)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to

## Knowledge Gaps
- **7 isolated node(s):** `alwaysUpdateLinks`, `newLinkFormat`, `useMarkdownLinks`, `attachmentFolderPath`, `showUnsupportedFiles` (+2 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Your AI Running Coach (Product Concept)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Charter (Waypoint product charter stub)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `START HERE (Home Note)` connect `Entry Point and Vault Structure` to `Cross-IDE and Continuous Push`, `Product and Project Identity`, `Versioning Strategy`, `Changelog and Milestones`, `Memory and Knowledge Graph`, `Graphify Operations`, `Trunk-Based Development`?**
  _High betweenness centrality (0.258) - this node is a cross-community bridge._
- **Why does `Versioning Strategy` connect `Versioning Strategy` to `Cross-IDE and Continuous Push`, `Trunk-Based Development`, `Changelog and Milestones`, `Entry Point and Vault Structure`?**
  _High betweenness centrality (0.109) - this node is a cross-community bridge._
- **Why does `Session 2026-07-30 Foundation Setup` connect `Changelog and Milestones` to `Cross-IDE and Continuous Push`, `Product and Project Identity`, `Versioning Strategy`, `Entry Point and Vault Structure`, `Memory and Knowledge Graph`, `Graphify Operations`, `Trunk-Based Development`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `START HERE (Home Note)` (e.g. with `Context Retrieval Order` and `Session Note Template`) actually correct?**
  _`START HERE (Home Note)` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Session 2026-07-30 Foundation Setup` (e.g. with `DEC-001 Trunk-based versioning on main` and `DEC-002 Obsidian vault as project memory`) actually correct?**
  _`Session 2026-07-30 Foundation Setup` has 7 INFERRED edges - model-reasoned connections that need verification._