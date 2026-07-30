# Graph Report - .  (2026-07-30)

## Corpus Check
- Corpus is ~25,656 words - fits in a single context window. You may not need a graph.

## Summary
- 83 nodes · 240 edges · 12 communities (11 shown, 1 thin omitted)
- Extraction: 63% EXTRACTED · 11% INFERRED · 1% AMBIGUOUS · INFERRED: 27 edges (avg confidence: 0.74)
- Token cost: 5,200 input · 1,300 output

## Community Hubs (Navigation)
- Vault Memory and Decision Infrastructure
- Research Program and Hypotheses
- Versioning and Attribution
- Phase 1 Market Research
- Changelog and Repo Docs
- Product Concept and Founder Vision
- Cross-IDE and Continuous Push
- Project Identity and Foundation
- Obsidian App Settings
- Research Playbook and Standards
- Agent Protocol
- MVP Scope and Integration Risks

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
- `Versioning Strategy` --references--> `Keep a Changelog Format`  [EXTRACTED]
  docs/VERSIONING.md → CHANGELOG.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Agent Memory System (amnesia prevention)** — agents_protocol, start_here_home, dec002_vault_project_memory, dec003_graphify_knowledge_graph, agents_context_retrieval_order, agents_session_end_checklist [INFERRED 0.90]
- **Versioning and Traceability System** — docs_versioning_trunk_based_development, changelog_semantic_versioning, docs_versioning_conventional_commits, changelog_keep_a_changelog, docs_versioning_attribution_footer, changelog_changelog [EXTRACTED 1.00]
- **Decision Record Workflow** — template_decision_record, vault_02_decisions_decision_log_index, dec001_trunk_versioning, dec002_vault_memory, dec003_graphify_brain [EXTRACTED 1.00]

## Communities (12 total, 1 thin omitted)

### Community 0 - "Vault Memory and Decision Infrastructure"
Cohesion: 0.38
Nodes (11): Context Retrieval Order, DEC-002 Obsidian vault as project memory, DEC-003 Graphify as queryable project brain, Graphify Knowledge Graph, Decision Log index, START HERE (Home Note), Decision Record Template, Knowledge Note Template (+3 more)

### Community 1 - "Research Program and Hypotheses"
Cohesion: 0.25
Nodes (11): Business intent: venture-scale, freemium subscription, seed in 12 months, Finding: H5 venture-scale verdict UNCERTAIN, Testable hypotheses H1 to H7, Phase 2: Competitor analysis, Phase 3: User research, Phase 4: Synthesis and concept lock, Phase 6: Business model and go-to-market, Phase 7: HTML research dashboard on Vercel (deployment protection required) (+3 more)

### Community 2 - "Versioning and Attribution"
Cohesion: 0.39
Nodes (9): Semantic Versioning, DEC-001 Trunk-based versioning on main, Agent Attribution Footer, Conventional Commits, Versioning Strategy, Version-Timestamp Convention, Agent-Attribution commit footer, Conventional Commits convention (+1 more)

### Community 3 - "Phase 1 Market Research"
Cohesion: 0.39
Nodes (8): Industry trends research (wearables, AI coaching, subscriptions, routing tech, running culture), Market landscape research (running, fitness, AI coaching markets), Market sizing: TAM $1.3B to $2.9B, SAM 14M runners, SOM $5M to $30M ARR, Regulatory and compliance research (location, health data, AI Act, accessibility, subscriptions), Finding: platform giants commoditize generic AI coaching, Finding: route-generation whitespace is real and unowned, Market Research Key Findings (Phase 1) vault note, Phase 1: Market and industry research

### Community 4 - "Changelog and Repo Docs"
Cohesion: 0.38
Nodes (7): Changelog, Keep a Changelog Format, Obsidian Vault as Project Memory, Token Cost Telemetry, Trunk-Based Development, README Overview, Trunk-based development model

### Community 5 - "Product Concept and Founder Vision"
Cohesion: 0.43
Nodes (7): Charter (Waypoint product charter stub), Engineering mantra: security, stability, reliability, compliance, Adaptive route generation (hero wedge), Founder Brief (Claudio's vision, 2026-07-30 interview), Guardrail: location privacy is day-one architecture (privacy zones, private-by-default), Knowledge Index, Problem: where to run in unfamiliar situations

### Community 6 - "Cross-IDE and Continuous Push"
Cohesion: 0.67
Nodes (7): CLAUDE.md (Claude Code pointer file), Cross-IDE / cross-tool compatibility (Cursor, Codex CLI, Claude Code, Gemini CLI, others), .gitattributes line-ending normalization (eol=lf), CONTRIBUTING.md (collaborator onboarding doc), DEC-004: Continuous push and cross-IDE agent files, Continuous push policy (commit and push after every meaningful unit of work), Session 2026-07-30 - Continuous Push and Cross-IDE Setup

### Community 7 - "Project Identity and Foundation"
Cohesion: 0.60
Nodes (6): Your AI Running Coach (Product Concept), Waypoint (Startup Project), Session 2026-07-30 Foundation Setup, GitHub Repo (mollyparty/waypoint), Charter, Engineering Mantra (Security, Stability, Reliability, Compliance)

### Community 8 - "Obsidian App Settings"
Cohesion: 0.33
Nodes (5): alwaysUpdateLinks, attachmentFolderPath, newLinkFormat, showUnsupportedFiles, useMarkdownLinks

### Community 9 - "Research Playbook and Standards"
Cohesion: 0.40
Nodes (5): DEC-005: Phased research program with gated approvals, Research Playbook (research/00-RESEARCH-PLAYBOOK.md), Session 2026-07-30 - Research Program Kickoff and Founder Brief, Citation and confidence-labeling standard ([verified]/[inferred]/[assumption]), Phase definition-of-done gate checklist

### Community 10 - "Agent Protocol"
Cohesion: 0.83
Nodes (4): Waypoint Agent Protocol, Session-End Checklist, Post-Commit Graph Rebuild Hook, Session Note Template

## Ambiguous Edges - Review These
- `Your AI Running Coach (Product Concept)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to
- `Charter (Waypoint product charter stub)` → `Knowledge Index`  [AMBIGUOUS]
  vault/04-Knowledge/_Knowledge-Index.md · relation: conceptually_related_to

## Knowledge Gaps
- **10 isolated node(s):** `alwaysUpdateLinks`, `newLinkFormat`, `useMarkdownLinks`, `attachmentFolderPath`, `showUnsupportedFiles` (+5 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Your AI Running Coach (Product Concept)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Charter (Waypoint product charter stub)` and `Knowledge Index`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `START HERE (Home Note)` connect `Vault Memory and Decision Infrastructure` to `Research Program and Hypotheses`, `Versioning and Attribution`, `Changelog and Repo Docs`, `Product Concept and Founder Vision`, `Cross-IDE and Continuous Push`, `Project Identity and Foundation`, `Agent Protocol`?**
  _High betweenness centrality (0.450) - this node is a cross-community bridge._
- **Why does `Nine-phase gated research program (Phase 0 to Phase 8)` connect `Research Program and Hypotheses` to `Vault Memory and Decision Infrastructure`, `Research Playbook and Standards`, `Phase 1 Market Research`, `MVP Scope and Integration Risks`?**
  _High betweenness centrality (0.234) - this node is a cross-community bridge._
- **Why does `Founder Brief (Claudio's vision, 2026-07-30 interview)` connect `Product Concept and Founder Vision` to `Vault Memory and Decision Infrastructure`, `Research Playbook and Standards`, `Phase 1 Market Research`, `Research Program and Hypotheses`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `START HERE (Home Note)` (e.g. with `Context Retrieval Order` and `Session Note Template`) actually correct?**
  _`START HERE (Home Note)` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 7 inferred relationships involving `Session 2026-07-30 Foundation Setup` (e.g. with `DEC-001 Trunk-based versioning on main` and `DEC-002 Obsidian vault as project memory`) actually correct?**
  _`Session 2026-07-30 Foundation Setup` has 7 INFERRED edges - model-reasoned connections that need verification._