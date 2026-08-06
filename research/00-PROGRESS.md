# Research Program Progress

> Version-Timestamp: 2026-08-06 12:45:00 UTC-4
>
> **This is the always-current phase catalog.** Any agent in any tool (Cursor, Claude Code, Codex, other) reads this after `vault/00-START-HERE.md` when continuing the research program. Do not invent status: update this file whenever a phase advances.

## Where we are right now (one paragraph)

Phases **0 to 5 are complete and gated**. The concept is **LOCKED** (DEC-006): route-first positioning, tagline **"Know where to run"**. Phase 5 closed on 2026-08-06 with all five gate decisions made: MVP scope approved, v1 launches entirely free, Watch is a fast-follow (DEC-008); the data layer **drops Supabase** for a split architecture of Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on the Hetzner private network for the geospatial moat, and auth decoupled into Waypoint's API layer via Better Auth (DEC-009, carrying an explicit revisit clause at Claudio's instruction); and the MVP ships **both platforms from one React Native codebase** with MapLibre maps, iOS at month 9 to 10 and Android 4 to 8 weeks later, ~29 to 31 person-months (DEC-010). Phase 6 deliverables are **all written** (canvas, revenue model, unit economics, metrics, GTM plan) and its gate is **open with six decisions** awaiting the founder on the dashboard. The governing finding: unit economics are a function of distribution, not pricing, since paid acquisition returns 53 to 70 cents on the dollar at every credible price and the model needs roughly 84 percent organic acquisition to clear 3:1. **Next agent action: nothing until Claudio answers the six Phase 6 gate cards**; then record the DECs and open Phase 7. Review surface: `dashboard/index.html` (also live on the protected Vercel preview). Latest tag: **v0.2.0**; v0.3.0 is due when Phase 6 is approved.

## Phase status board

| Phase | Name | Status | Gate | Folder / surface | Vault distillate | Decision(s) |
|------:|------|--------|------|------------------|------------------|---------------|
| 0 | Founder brief and infrastructure | **COMPLETE** | Passed | `vault/01-Project/`, `research/00-RESEARCH-PLAYBOOK.md` | [[Founder-Brief]], [[Charter]] | DEC-005 |
| 1 | Market and industry | **COMPLETE** | Passed | `research/01-market/` | [[Market Research Key Findings (Phase 1)]] | (gate in session) |
| 2 | Competitor analysis | **COMPLETE** | Passed | `research/02-competitors/` | [[Competitive Landscape Key Findings (Phase 2)]] | (gate in session) |
| 3 | User research | **COMPLETE** | Passed | `research/03-users/` | [[User Research Key Findings (Phase 3)]] | safety-free resolved in DEC-008 |
| 4 | Synthesis and concept lock | **COMPLETE** | Passed / concept LOCKED | `research/04-synthesis/` | [[Concept and Positioning (Phase 4)]] | DEC-006 |
| 5 | Product definition and MVP | **COMPLETE** | Passed (all 5 cards) | `research/05-product/` | [[Product Definition Key Findings (Phase 5)]] | DEC-008, DEC-009, DEC-010 |
| 6 | Business model and GTM | **DELIVERABLES COMPLETE** | **Open: 6 decisions on the dashboard** | `research/06-business-model/` | [[Business Model and GTM Key Findings (Phase 6)]] | pending |
| 7 | HTML research dashboard | **PARTIALLY DONE** (pulled forward) | Vercel polish still Phase 7 formal gate | `dashboard/index.html` (live on preview) | — | DEC-007 (publishing) |
| 8 | Business Blueprint | **NOT STARTED** | Blocked on Phases 5 to 7 | `blueprint/` (not created yet) | — | — |

## Phase 5 detail (closed 2026-08-06)

### Done and approved

- [x] `prd.md`, `rice-prioritization.md`, `mvp-scope.md`, `user-journeys.md`, `stack-recommendation.md`
- [x] `stack-validation.md` (round 1: no layer revised; Supabase and Hetzner with conditions)
- [x] MVP scope approved as drawn (~15 features, ~25 person-months, 8 to 10 months, iOS-native estimate)
- [x] Launch v1 entirely free; safety-aware routing free permanently
- [x] Apple Watch fast-follow at launch+30

### Round 2 studies, now decided

- [x] `database-deep-dive.md` (round 2): Supabase scored 3.45 vs Aiven 4.46 on the four pillars. Verdict: split architecture, Aiven (EU, ISO 27001 + SOC 2, 99.99% SLA) for personal data; self-managed PostGIS on Hetzner private net for the moat; Better Auth decoupled into the API layer. Runner-up: OVHcloud managed Postgres.
- [x] `dual-platform-strategy.md` (round 2): recommends Option D, staged cross-platform on React Native + MapLibre (~29-31 pm, iOS month 9-10, Android +4-8 weeks). Simultaneous dual-native (38-40 pm) endangers the competitive window. Runna (category leader) is the React Native existence proof.
- [x] `api-integration-map.md` (round 2): ~20 required integrations across 7 domains (30 cataloged incl. fallbacks); ~$80-130/mo at MVP, ~$350-500/mo at 10k MAU; only 6 gate the walking skeleton; top risks are Strava program terms, Android health/location review lead times, WeatherKit-on-Android goodwill, ODbL boundary.

### Gate outcome (2026-08-06)

- [x] **Stack: approved as revised** (DEC-009). Aiven (EU) for personal data + self-managed PostGIS on Hetzner + Better Auth in Waypoint's API layer. Supabase dropped. **The revisit clause is deliberate**, at Claudio's instruction: re-open before the walking skeleton, when architecture design starts, at Aiven contract time, or if the two-database plus self-owned-auth ops burden proves real. Infrastructure detail must not block product definition.
- [x] **Platform: Option D approved** (DEC-010). One React Native codebase, MapLibre on both platforms, iOS month 9-10, Android month 10-12, ~29-31 pm. Amends DEC-006 client stack and DEC-008 effort.
- [x] Amendments propagated: `mvp-scope.md` section 7 and milestone table, Charter constraints and success criteria, dashboard cards 8 and 9.

## Phase 6 detail (current workstream)

### Written 2026-08-06

- [x] `business-model-canvas.md` — nine blocks plus the cross-document reconciliation. **The document to read first.**
- [x] `revenue-model.md` — $99.99/yr list, $12.99/mo, 21-day annual-only trial, Founding Runner $69.99/yr price-preserved. Lifetime tier and data monetization rejected on the record.
- [x] `unit-economics.md` — break-even ~3,000 paying subscribers; free active user costs under $1/year; paid acquisition returns 53 to 70 cents on the dollar at every credible price.
- [x] `metrics.md` — North Star Weekly Routed Runners (80 percent completion floor inside the definition); activation = first generated route completed as a recorded run; Good Route Rate; ten guardrails.
- [x] `gtm-plan.md` — one metro, one segment; run clubs, then Reddit, then store optimization; SEO and paid acquisition argued against; Android date is the real public launch.

### Open (blocks Phase 7 close and Phase 8)

- [ ] Six gate decisions, listed in `research/06-business-model/_index.md` and staged on the dashboard: price, free/paid boundary breadth, the analytics identity fix, re-basing PRD G3/G4, the beachhead metro, and which date is the real launch.

### Corrections to Phase 5 surfaced by Phase 6

- [ ] PRD goals G3 and G4 need re-basing to activated-cohort definitions (gate card 4)
- [ ] `05-product/api-integration-map.md` names TelemetryDeck, which structurally cannot deliver cohort retention (gate card 3)
- [ ] Treat the month-1 safety-data buildability spike as a **go-to-market gate**, not only a technical one

### Carried into the build phase (not blockers)

- [ ] Verify Garmin Connect writes into Health Connect before Android work begins (H6 was verified for HealthKit only)
- [ ] `api-integration-map.md` section 4 still names Supabase Auth; superseded by DEC-009, correct it when architecture notes are written
- [ ] Android long-lead paperwork (Play org account, Health Connect + fine-location declarations) starts month 1 of the build

## Decisions that govern the product (do not contradict without a new DEC)

| ID | Summary |
|----|---------|
| DEC-006 | Concept locked: route-first; tagline "Know where to run"; H1 reframe (travel activates, safety + novelty retain) |
| DEC-007 | GitHub → Vercel auto-publish; real content on protected `main` preview only; production branch is placeholder |
| DEC-008 | MVP scope / free launch / Watch fast-follow approved; stack held for validation; graph explorer required |
| DEC-009 | Data layer: Aiven for PostgreSQL (EU) for personal data + self-managed PostGIS on Hetzner for the moat + Better Auth decoupled into the API layer. Supabase dropped. Revisitable at four named checkpoints |
| DEC-010 | Staged cross-platform MVP: one React Native codebase, MapLibre both platforms, iOS month 9-10, Android +4-8 weeks, ~29-31 person-months. Amends DEC-006 client stack and DEC-008 effort |

## Surfaces every agent must know

| Surface | Path | Purpose |
|---------|------|---------|
| Project state | `vault/00-START-HERE.md` | Latest approved snapshot |
| This catalog | `research/00-PROGRESS.md` | Phase-by-phase status |
| Playbook | `research/00-RESEARCH-PLAYBOOK.md` | Standards, citation, gate definition of done |
| Readable review | `dashboard/index.html` | Claudio's review surface (dashboard-first) |
| Knowledge graph UI | `graph/index.html` | Interactive explorer over `graphify-out/graph.json` |
| Landing (Vercel) | `index.html` | Links dashboard + graph |
| Agent protocol | `AGENTS.md` (Claude Code via `CLAUDE.md`) | Memory, git, engineering rules |
| Collaborator setup | `CONTRIBUTING.md` | Clone and tool onboarding |

## Vercel access (confidential)

- Real content (login required): https://waypoint-git-main-mollypartys-projects.vercel.app
- Public production domains serve only a placeholder (DEC-007). Do not publish confidential research to unprotected production.

## Version plan

| Tag | When |
|-----|------|
| v0.1.0 | Foundation (done) |
| v0.2.0 | Phases 1 to 4, concept locked (done) |
| v0.3.0 | Phases 5 to 6 approved |
| v0.4.0 | Phases 7 to 8 approved |

## How to update this file

When a phase advances: change the status board row, tick or add Phase 5 detail items, update the one-paragraph "Where we are" block, bump the Version-Timestamp, then update `vault/00-START-HERE.md` to match. Never leave START-HERE and this file disagreeing.
