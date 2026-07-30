# Waypoint Research Playbook

Version-Timestamp: 2026-07-30 13:30:00 UTC-4

This is the operating manual for the Waypoint research-to-blueprint program. Any agent (Cursor, Codex CLI, Claude Code, other) or human picking up a research phase follows this playbook exactly. It exists so that no phase cuts corners, no claim goes unsourced, and no context is lost between sessions or tools.

## Program overview

The program runs in nine phases. Each phase builds on the outputs of the previous one. A phase is not started until the previous phase has passed its gate (Claudio's explicit approval).

| Phase | Name | Output folder | Gate |
|-------|------|---------------|------|
| 0 | Founder brief and infrastructure | `vault/01-Project/` + this folder | Approved plan |
| 1 | Market and industry research | `research/01-market/` | Claudio reviews deliverables |
| 2 | Competitor analysis | `research/02-competitors/` | Claudio reviews deliverables |
| 3 | User research | `research/03-users/` | Claudio reviews deliverables |
| 4 | Synthesis and concept definition | `research/04-synthesis/` | Claudio locks the concept (heaviest gate) |
| 5 | Product definition and MVP scope | `research/05-product/` | Claudio approves PRD and MVP scope |
| 6 | Business model and go-to-market | `research/06-business-model/` | Claudio approves model |
| 7 | HTML research dashboard | `dashboard/` | Claudio approves before Vercel deploy |
| 8 | Business Blueprint | `blueprint/` | Claudio approves investor deliverable |

Version tags: `v0.2.0` after Phases 1 to 4, `v0.3.0` after Phases 5 to 6, `v0.4.0` after Phases 7 to 8.

## Non-negotiable standards (apply to every phase)

### Citation standard

- Every factual claim carries a source: publisher or author, title or page, URL, and the date accessed.
- Market size numbers additionally state the methodology (who measured it, what year, what geography, what definition of the market).
- If two sources conflict, present both and say which one we weight and why.
- No source, no claim. If a number cannot be sourced, it is labeled an assumption.

### Confidence labeling

Every finding is tagged with exactly one of:

- `[verified]` - directly sourced from a credible primary or strong secondary source.
- `[inferred]` - a reasonable conclusion we drew from verified facts; the reasoning is written out.
- `[assumption]` - unverified; must be validated later. All assumptions are also listed in the phase's `ASSUMPTIONS.md` section or block so they are never silently absorbed into conclusions.

### Definition of done (gate checklist for every phase)

A phase is done only when all of the following are true:

1. Every deliverable listed in the phase folder's `_index.md` exists and is complete (no TODO stubs unless explicitly deferred with Claudio's sign-off).
2. Every claim is cited and confidence-labeled per the standards above.
3. Open questions and assumptions are collected in a clearly marked section, not buried.
4. Key findings are distilled into vault knowledge notes (`vault/04-Knowledge/`) with wikilinks, so the graph and future sessions can find them.
5. Any locked choices are recorded as decision records (`vault/02-Decisions/`).
6. A session note exists in `vault/03-Sessions/` for the working session(s).
7. `vault/00-START-HERE.md` reflects the new state (phase status, next unlock).
8. Graphify graph updated, everything committed with attribution footer and pushed.
9. Claudio has reviewed and approved the phase at the gate.

### Dashboard-first review (added 2026-07-30 at Claudio's request)

Claudio reviews phases in the HTML dashboard (`dashboard/index.html`), not in raw markdown. Every phase must update the dashboard with its digest (key findings, tables, any new gate decisions) before its gate review. The markdown documents remain the citable source of truth; the dashboard is the readable window into them. Keep it a single self-contained file (no build step) until Phase 7 deploys it to Vercel with deployment protection.

### Memory protocol

Follow `AGENTS.md` at the repo root. In short: start by reading `vault/00-START-HERE.md` and the newest session note; query the graph before re-reading the repo; record decisions as they happen; push continuously.

### Writing standard

No em dashes or en dashes anywhere in deliverables. Use periods, commas, colons, or parentheses. Use "to" for ranges.

## Phase specifications

### Phase 1: Market and industry research

Deliverables in `research/01-market/`:

- `market-landscape.md` - the running app, fitness coaching, and AI coaching markets: definitions, size, growth, structure, value chain.
- `market-sizing.md` - TAM, SAM, SOM with sourced numbers, stated methodology, and a bottom-up sanity check alongside any top-down figures.
- `industry-trends.md` - wearables integration, AI coaching adoption, subscription fitness economics, relevant technology shifts.
- `regulatory-compliance.md` - health and fitness data privacy (GDPR, CCPA, HIPAA adjacency), App Store and Play Store health app rules, accessibility obligations, AI-specific regulation relevant to coaching advice.

Skills: `strategy-frameworks` for industry structure. Use parallel research subagents for independent workstreams where possible.

### Phase 2: Competitor analysis

Deliverables in `research/02-competitors/`:

- One profile per direct competitor (`profile-<name>.md`): product, features, pricing, positioning, strengths, weaknesses, review sentiment summary, funding and traction if public.
- Direct set (starting list, expand as research warrants): Runna, TrainAsONE, AI Endurance, Coopah, Joggo.
- Adjacent set (lighter profiles): Strava, Garmin Coach, Nike Run Club, WHOOP, Apple Fitness+.
- `feature-matrix.md` - features across all competitors in one table.
- `pricing-matrix.md` - pricing tiers, trials, annual vs monthly.
- `positioning-map.md` - how each player positions, and the visible whitespace.
- `gap-analysis.md` - unmet needs and underserved segments visible from the competitive set.

Note: collect competitor app store reviews and community complaints during this phase; they are primary input for Phase 3.

### Phase 3: User research

Deliverables in `research/03-users/`:

- `segmentation.md` - runner segments with sizing where sourceable.
- `personas.md` - 3 to 5 evidence-based personas. Every persona trait traces to evidence; no invented biography details presented as fact.
- `jobs-to-be-done.md` - functional, emotional, and social jobs.
- `pain-points.md` - inventory mined from competitor reviews, Reddit, running forums; each pain point cites where it was observed and how often.
- `unmet-needs.md` - ranked by evidence strength, with explicit notes on which findings require real user interviews to validate. Desk research is labeled as desk research, never passed off as validated primary research.

### Phase 4: Synthesis and concept definition

Deliverables in `research/04-synthesis/`:

- `opportunity.md` - the opportunity definition: where market gap, user need, and feasibility intersect.
- `positioning.md` - positioning statement and rationale against the competitive map.
- `concept.md` - the locked concept document covering: the concept, the users, the features, the functionality, the user needs, the business needs.
- `hypotheses-review.md` - verdict on every hypothesis from the Founder Brief: confirmed, refuted, or still open.

Skills: `brainstorming` for divergence, then `strategy-frameworks` for convergence. This phase's gate locks the concept; locked choices become DEC records.

### Phase 5: Product definition and MVP scope

Deliverables in `research/05-product/`:

- `prd.md` - product requirements document.
- `prioritization.md` - RICE scoring of the feature set.
- `mvp-scope.md` - must have, should have, later; the ONE core job stated explicitly.
- `user-journeys.md` - complete experience maps including loading, error, empty, and success states.
- `stack-recommendation.md` - recommended architecture and stack with justification and alternatives considered.

Skill: `zero-to-launch`.

### Phase 6: Business model and go-to-market

Deliverables in `research/06-business-model/`:

- `business-model-canvas.md` - all nine blocks.
- `revenue-model.md` - pricing strategy and revenue streams.
- `unit-economics.md` - directional CAC, LTV, margin assumptions, all labeled directional.
- `metrics.md` - North Star metric and supporting metric tree.
- `gtm-plan.md` - launch strategy, channels, early traction plan.

Skills: `business-model-designer`, `metrics-frameworks`, `strategy-frameworks`.

### Phase 7: HTML research dashboard

- Static HTML, CSS, and JS in `dashboard/` (no build step, opens in any browser, portable across IDEs).
- Presents all research: navigation by phase, key findings, matrices, personas, charts.
- Deployed to Vercel with deployment protection enabled. This research is confidential pre-launch material; an unprotected URL is a data handling violation. Do not deploy unprotected without Claudio's explicit instruction.

### Phase 8: Business Blueprint

- Markdown master blueprint in `blueprint/` synthesizing all prior phases.
- Structure matched to Claudio's example (premiumcuts-blueprint.vercel.app) if fetchable; otherwise: problem, market, users, solution, product, competition, business model, GTM, financials, roadmap, the ask.
- Polished investor-facing HTML site deployed to Vercel as a separate deployment.
- Skills: `brand-blueprint-builder` for narrative and positioning sections, `human-voice` for copy.

## How to run a phase (any agent, any IDE)

1. Read `vault/00-START-HERE.md`, the newest session note, and this playbook.
2. Read the phase folder's `_index.md` and all prior phases' deliverables (or query the graph for their key findings).
3. Read the Founder Brief (`vault/01-Project/Founder-Brief.md`); research exists to confirm or kill its hypotheses, not to ignore them.
4. Produce the deliverables to the standards above. Push work continuously, not just at the end.
5. Walk the definition-of-done checklist. Fix anything that fails before declaring the phase complete.
6. Present the deliverables to Claudio at the gate. Do not start the next phase without approval.
