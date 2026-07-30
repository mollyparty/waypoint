# Graph Report - .  (2026-07-30)

## Corpus Check
- 80 files · ~122,994 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 138 nodes · 339 edges · 8 communities
- Extraction: 45% EXTRACTED · 8% INFERRED · 1% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.74)
- Token cost: 3,600 input · 950 output

## Community Hubs (Navigation)
- Product Wedge, Market Evidence, and Hypothesis Verdicts
- Agent Protocol and Memory Infrastructure
- Versioning and Project Identity
- Phase 2 Competitive Landscape and Threats
- Research Program, Constraints, and Open Decisions
- Phase 3 User Research and Personas
- Obsidian App Settings
- Community 7

## God Nodes (most connected - your core abstractions)
1. `START HERE (Home Note)` - 34 edges
2. `Session 2026-07-30 Foundation Setup` - 25 edges
3. `Waypoint Agent Protocol` - 23 edges
4. `README Overview` - 19 edges
5. `Versioning Strategy` - 19 edges
6. `DEC-001 Trunk-based versioning on main` - 14 edges
7. `Adaptive route generation (hero wedge)` - 14 edges
8. `Phase 2: Competitor analysis` - 13 edges
9. `Changelog` - 12 edges
10. `Nine-phase gated research program (Phase 0 to Phase 8)` - 12 edges

## Surprising Connections (you probably didn't know these)
- `Your AI Running Coach (Product Concept)` --conceptually_related_to--> `Knowledge Index`  [AMBIGUOUS]
  README.md → vault/04-Knowledge/_Knowledge-Index.md
- `Waypoint Agent Protocol` --references--> `Engineering Mantra (Security, Stability, Reliability, Compliance)`  [EXTRACTED]
  AGENTS.md → vault/01-Project/Charter.md
- `README Overview` --references--> `Decision Log`  [INFERRED]
  README.md → vault/02-Decisions/_Decision-Log.md
- `Your AI Running Coach (Product Concept)` --supersedes--> `Tagline: Know where to run (replaces Your AI Running Coach)`  [STATED]
  README.md → vault/02-Decisions/DEC-006 Concept lock route-first positioning.md
- `Adaptive route generation (hero wedge)` --supports--> `Unmet need: safety-aware routing (strongest evidence)`  [STATED]
  vault/01-Project/Founder-Brief.md → research/03-users/unmet-needs.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent Memory System (amnesia prevention)** — agents_protocol, start_here_home, dec002_vault_project_memory, dec003_graphify_knowledge_graph, agents_context_retrieval_order, agents_session_end_checklist [INFERRED 0.90]
- **Versioning and Traceability System** — docs_versioning_trunk_based_development, changelog_semantic_versioning, docs_versioning_conventional_commits, changelog_keep_a_changelog, docs_versioning_attribution_footer, changelog_changelog [EXTRACTED 1.00]
- **Decision Record Workflow** — template_decision_record, vault_02_decisions_decision_log_index, dec001_trunk_versioning, dec002_vault_memory, dec003_graphify_brain [EXTRACTED 1.00]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Product Wedge, Market Evidence, and Hypothesis Verdicts"
Cohesion: 0.09
Nodes (34): Business intent: venture-scale, freemium subscription, seed in 12 months, Engineering mantra: security, stability, reliability, compliance, AllTrails (Peak tier AI route adjustments, trail-locked), Komoot (Bending Spoons-owned, declining, bike/hike-first), Runna (Strava-owned, category-leading AI training app), Strava (platform: routes, heatmap, Runna owner), Adaptive route generation (hero wedge), Competitor feature matrix (+26 more)

### Community 1 - "Agent Protocol and Memory Infrastructure"
Cohesion: 0.09
Nodes (33): Constraint: data enclosure forces HealthKit-first and a proprietary context-data moat, DEC-005: Phased research program with gated approvals, DEC-006: Concept lock, route-first positioning, Know where to run, Concept definition (LOCKED at Phase 4 gate), Jobs-to-be-done (11 functional jobs, emotional and social jobs, persona job map), Runner pain points mined from communities, Personas: Marcus, Priya, Elena, Jake, Runner segmentation (five behavioral segments with sizing) (+25 more)

### Community 2 - "Versioning and Project Identity"
Cohesion: 0.14
Nodes (19): Condition: Hetzner with off-provider backups, IaC, restore drill, OVH fallback runbook, Condition: Supabase with EU region, on-device health line, auth containment, off-platform backups, HTML research dashboard (dashboard/index.html), DEC-008: Phase 5 gate, MVP approved, launch free, Watch fast-follow, stack held for validation, Stack choice: self-hosted GraphHopper routing (moat data cannot run hosted), Stack choice: on-device Apple Foundation Models for coaching, Decision: safety-aware routing free permanently (with v1 launching entirely free), Phase 5 gate pending: MVP scope, free/paid line, Watch timing, stack approval (+11 more)

### Community 3 - "Phase 2 Competitive Landscape and Threats"
Cohesion: 0.33
Nodes (17): Context Retrieval Order, Session-End Checklist, DEC-002 Obsidian vault as project memory, Obsidian Vault as Project Memory, Token Cost Telemetry, DEC-003 Graphify as queryable project brain, Graphify Knowledge Graph, Post-Commit Graph Rebuild Hook (+9 more)

### Community 4 - "Research Program, Constraints, and Open Decisions"
Cohesion: 0.28
Nodes (15): Changelog, Keep a Changelog Format, Semantic Versioning, DEC-001 Trunk-based versioning on main, Agent Attribution Footer, Conventional Commits, Versioning Strategy, Trunk-Based Development (+7 more)

### Community 5 - "Phase 3 User Research and Personas"
Cohesion: 0.71
Nodes (8): Waypoint Agent Protocol, CLAUDE.md (Claude Code pointer file), Cross-IDE / cross-tool compatibility (Cursor, Codex CLI, Claude Code, Gemini CLI, others), .gitattributes line-ending normalization (eol=lf), CONTRIBUTING.md (collaborator onboarding doc), DEC-004: Continuous push and cross-IDE agent files, Continuous push policy (commit and push after every meaningful unit of work), Session 2026-07-30 - Continuous Push and Cross-IDE Setup

### Community 6 - "Obsidian App Settings"
Cohesion: 0.47
Nodes (6): Charter (Waypoint product charter stub), Knowledge Index, Your AI Running Coach (Product Concept), Waypoint (Startup Project), Charter, Engineering Mantra (Security, Stability, Reliability, Compliance)

### Community 7 - "Community 7"
Cohesion: 0.33
Nodes (5): alwaysUpdateLinks, attachmentFolderPath, newLinkFormat, showUnsupportedFiles, useMarkdownLinks

## Ambiguous Edges - Review These
- `Your AI Running Coach (Product Concept)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to
- `Charter (Waypoint product charter stub)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to

## Knowledge Gaps
- **26 isolated node(s):** `alwaysUpdateLinks`, `newLinkFormat`, `useMarkdownLinks`, `attachmentFolderPath`, `showUnsupportedFiles` (+21 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Your AI Running Coach (Product Concept)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Charter (Waypoint product charter stub)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `START HERE (Home Note)` connect `Phase 2 Competitive Landscape and Threats` to `Agent Protocol and Memory Infrastructure`, `Research Program, Constraints, and Open Decisions`, `Phase 3 User Research and Personas`, `Obsidian App Settings`?**
  _High betweenness centrality (0.354) - this node is a cross-community bridge._
- **Why does `Nine-phase gated research program (Phase 0 to Phase 8)` connect `Agent Protocol and Memory Infrastructure` to `Product Wedge, Market Evidence, and Hypothesis Verdicts`, `Phase 2 Competitive Landscape and Threats`?**
  _High betweenness centrality (0.236) - this node is a cross-community bridge._
- **Why does `Session 2026-07-30 - Research Program Kickoff and Founder Brief` connect `Agent Protocol and Memory Infrastructure` to `Product Wedge, Market Evidence, and Hypothesis Verdicts`, `Versioning and Project Identity`?**
  _High betweenness centrality (0.181) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `START HERE (Home Note)` (e.g. with `Context Retrieval Order` and `Session Note Template`) actually correct?**
  _`START HERE (Home Note)` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Session 2026-07-30 Foundation Setup` (e.g. with `DEC-001 Trunk-based versioning on main` and `DEC-002 Obsidian vault as project memory`) actually correct?**
  _`Session 2026-07-30 Foundation Setup` has 7 INFERRED edges - model-reasoned connections that need verification._