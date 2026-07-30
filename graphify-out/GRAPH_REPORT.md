# Graph Report - .  (2026-07-30)

## Corpus Check
- Corpus is ~8,720 words - fits in a single context window. You may not need a graph.

## Summary
- 73 nodes · 216 edges · 9 communities
- Extraction: 70% EXTRACTED · 12% INFERRED · 1% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.74)
- Token cost: 7,400 input · 1,650 output

## Community Hubs (Navigation)
- Research Program and Phase Gates
- Versioning Strategy
- Product Concept and Founder Vision
- Vault Structure and Entry Point
- Cross-IDE and Continuous Push
- Obsidian App Settings
- Graphify Operations and Sessions
- Memory and Knowledge Graph
- Agent Protocol and Traceability

## God Nodes (most connected - your core abstractions)
1. `START HERE (Home Note)` - 34 edges
2. `Session 2026-07-30 Foundation Setup` - 25 edges
3. `Waypoint Agent Protocol` - 23 edges
4. `README Overview` - 19 edges
5. `Versioning Strategy` - 19 edges
6. `DEC-001 Trunk-based versioning on main` - 14 edges
7. `Changelog` - 12 edges
8. `Graphify Knowledge Graph` - 11 edges
9. `CONTRIBUTING.md (collaborator onboarding doc)` - 11 edges
10. `DEC-004: Continuous push and cross-IDE agent files` - 11 edges

## Surprising Connections (you probably didn't know these)
- `Your AI Running Coach (Product Concept)` --conceptually_related_to--> `Knowledge Index`  [AMBIGUOUS]
  README.md → vault/04-Knowledge/_Knowledge-Index.md
- `Waypoint Agent Protocol` --references--> `Engineering Mantra (Security, Stability, Reliability, Compliance)`  [EXTRACTED]
  AGENTS.md → vault/01-Project/Charter.md
- `README Overview` --implements--> `Version-Timestamp Convention`  [INFERRED]
  README.md → docs/VERSIONING.md
- `README Overview` --references--> `Decision Log`  [INFERRED]
  README.md → vault/02-Decisions/_Decision-Log.md
- `START HERE (Home Note)` --conceptually_related_to--> `Context Retrieval Order`  [INFERRED]
  vault/00-START-HERE.md → AGENTS.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent Memory System (amnesia prevention)** — agents_protocol, start_here_home, dec002_vault_project_memory, dec003_graphify_knowledge_graph, agents_context_retrieval_order, agents_session_end_checklist [INFERRED 0.90]
- **Versioning and Traceability System** — docs_versioning_trunk_based_development, changelog_semantic_versioning, docs_versioning_conventional_commits, changelog_keep_a_changelog, docs_versioning_attribution_footer, changelog_changelog [EXTRACTED 1.00]
- **Decision Record Workflow** — template_decision_record, vault_02_decisions_decision_log_index, dec001_trunk_versioning, dec002_vault_memory, dec003_graphify_brain [EXTRACTED 1.00]

## Communities (9 total, 0 thin omitted)

### Community 0 - "Research Program and Phase Gates"
Cohesion: 0.18
Nodes (15): DEC-005: Phased research program with gated approvals, Testable hypotheses H1 to H7, Phase 1: Market and industry research, Phase 2: Competitor analysis, Phase 3: User research, Phase 4: Synthesis and concept lock, Phase 5: Product definition and MVP scope, Phase 6: Business model and go-to-market (+7 more)

### Community 1 - "Versioning Strategy"
Cohesion: 0.35
Nodes (12): Changelog, Keep a Changelog Format, Semantic Versioning, DEC-001 Trunk-based versioning on main, Conventional Commits, Versioning Strategy, Trunk-Based Development, README Overview (+4 more)

### Community 2 - "Product Concept and Founder Vision"
Cohesion: 0.25
Nodes (11): Business intent: venture-scale, freemium subscription, seed in 12 months, Charter (Waypoint product charter stub), Engineering mantra: security, stability, reliability, compliance, Adaptive route generation (hero wedge), Decision Log index, Founder Brief (Claudio's vision, 2026-07-30 interview), Knowledge Index, Phase 8: Business Blueprint (investor deliverable) (+3 more)

### Community 3 - "Vault Structure and Entry Point"
Cohesion: 0.36
Nodes (9): GitHub Repo (mollyparty/waypoint), START HERE (Home Note), Decision Record Template, Knowledge Note Template, Charter, Engineering Mantra (Security, Stability, Reliability, Compliance), Decision Log, Knowledge Index (+1 more)

### Community 4 - "Cross-IDE and Continuous Push"
Cohesion: 0.67
Nodes (7): CLAUDE.md (Claude Code pointer file), Cross-IDE / cross-tool compatibility (Cursor, Codex CLI, Claude Code, Gemini CLI, others), .gitattributes line-ending normalization (eol=lf), CONTRIBUTING.md (collaborator onboarding doc), DEC-004: Continuous push and cross-IDE agent files, Continuous push policy (commit and push after every meaningful unit of work), Session 2026-07-30 - Continuous Push and Cross-IDE Setup

### Community 5 - "Obsidian App Settings"
Cohesion: 0.33
Nodes (5): alwaysUpdateLinks, attachmentFolderPath, newLinkFormat, showUnsupportedFiles, useMarkdownLinks

### Community 6 - "Graphify Operations and Sessions"
Cohesion: 0.80
Nodes (5): Session-End Checklist, Token Cost Telemetry, DEC-003 Graphify as queryable project brain, Post-Commit Graph Rebuild Hook, Session 2026-07-30 Foundation Setup

### Community 7 - "Memory and Knowledge Graph"
Cohesion: 0.67
Nodes (4): Context Retrieval Order, DEC-002 Obsidian vault as project memory, Obsidian Vault as Project Memory, Graphify Knowledge Graph

### Community 8 - "Agent Protocol and Traceability"
Cohesion: 0.83
Nodes (4): Waypoint Agent Protocol, Agent Attribution Footer, Version-Timestamp Convention, Session Note Template

## Ambiguous Edges - Review These
- `Your AI Running Coach (Product Concept)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to
- `Charter (Waypoint product charter stub)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to

## Knowledge Gaps
- **12 isolated node(s):** `alwaysUpdateLinks`, `newLinkFormat`, `useMarkdownLinks`, `attachmentFolderPath`, `showUnsupportedFiles` (+7 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Your AI Running Coach (Product Concept)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Charter (Waypoint product charter stub)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `START HERE (Home Note)` connect `Vault Structure and Entry Point` to `Research Program and Phase Gates`, `Versioning Strategy`, `Product Concept and Founder Vision`, `Cross-IDE and Continuous Push`, `Graphify Operations and Sessions`, `Memory and Knowledge Graph`, `Agent Protocol and Traceability`?**
  _High betweenness centrality (0.451) - this node is a cross-community bridge._
- **Why does `Nine-phase gated research program (Phase 0 to Phase 8)` connect `Research Program and Phase Gates` to `Product Concept and Founder Vision`, `Vault Structure and Entry Point`?**
  _High betweenness centrality (0.235) - this node is a cross-community bridge._
- **Why does `Founder Brief (Claudio's vision, 2026-07-30 interview)` connect `Product Concept and Founder Vision` to `Research Program and Phase Gates`, `Vault Structure and Entry Point`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `START HERE (Home Note)` (e.g. with `Context Retrieval Order` and `Session Note Template`) actually correct?**
  _`START HERE (Home Note)` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Session 2026-07-30 Foundation Setup` (e.g. with `DEC-001 Trunk-based versioning on main` and `DEC-002 Obsidian vault as project memory`) actually correct?**
  _`Session 2026-07-30 Foundation Setup` has 7 INFERRED edges - model-reasoned connections that need verification._