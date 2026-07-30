# Research Program Progress

> Version-Timestamp: 2026-07-30 22:30:00 UTC-4
>
> **This is the always-current phase catalog.** Any agent in any tool (Cursor, Claude Code, Codex, other) reads this after `vault/00-START-HERE.md` when continuing the research program. Do not invent status: update this file whenever a phase advances.

## Where we are right now (one paragraph)

Phases **0 to 4 are complete and gated**. The concept is **LOCKED** (DEC-006): route-first positioning, tagline **"Know where to run"**. Phase 5 product deliverables are ALL written, including the three round-2 studies (`database-deep-dive.md`, `dual-platform-strategy.md`, `api-integration-map.md`). Claudio approved MVP scope, free launch, and Watch as fast-follow (DEC-008). **Round 2 revised the stack recommendation:** replace Supabase with a split architecture (Aiven for PostgreSQL in the EU for personal data; self-managed PostGIS on the Hetzner private network for the geospatial moat; auth decoupled into the API layer via Better Auth), and, if dual-platform is confirmed, rebase the client on React Native + MapLibre (staged: iOS month 9-10, Android 4 to 8 weeks later, ~29-31 person-months). **Next agent action: nothing until Claudio decides** dashboard cards 8 (revised stack) and 9 (platform strategy); each decision then gets a new DEC and downstream doc updates. Phase 6 is blocked until both close. Review surface: `dashboard/index.html` (also live on the protected Vercel preview). Latest tag: **v0.2.0**.

## Phase status board

| Phase | Name | Status | Gate | Folder / surface | Vault distillate | Decision(s) |
|------:|------|--------|------|------------------|------------------|---------------|
| 0 | Founder brief and infrastructure | **COMPLETE** | Passed | `vault/01-Project/`, `research/00-RESEARCH-PLAYBOOK.md` | [[Founder-Brief]], [[Charter]] | DEC-005 |
| 1 | Market and industry | **COMPLETE** | Passed | `research/01-market/` | [[Market Research Key Findings (Phase 1)]] | (gate in session) |
| 2 | Competitor analysis | **COMPLETE** | Passed | `research/02-competitors/` | [[Competitive Landscape Key Findings (Phase 2)]] | (gate in session) |
| 3 | User research | **COMPLETE** | Passed | `research/03-users/` | [[User Research Key Findings (Phase 3)]] | safety-free resolved in DEC-008 |
| 4 | Synthesis and concept lock | **COMPLETE** | Passed / concept LOCKED | `research/04-synthesis/` | [[Concept and Positioning (Phase 4)]] | DEC-006 |
| 5 | Product definition and MVP | **IN PROGRESS** (all deliverables written incl. round 2; awaiting stack + platform decisions) | Partial: DEC-008; cards 8 and 9 open | `research/05-product/` | [[Product Definition Key Findings (Phase 5)]] | DEC-008; stack + platform DECs pending |
| 6 | Business model and GTM | **NOT STARTED** | Blocked on Phase 5 stack + platform | `research/06-business-model/` | — | — |
| 7 | HTML research dashboard | **PARTIALLY DONE** (pulled forward) | Vercel polish still Phase 7 formal gate | `dashboard/index.html` (live on preview) | — | DEC-007 (publishing) |
| 8 | Business Blueprint | **NOT STARTED** | Blocked on Phases 5 to 7 | `blueprint/` (not created yet) | — | — |

## Phase 5 detail (current workstream)

### Done and approved

- [x] `prd.md`, `rice-prioritization.md`, `mvp-scope.md`, `user-journeys.md`, `stack-recommendation.md`
- [x] `stack-validation.md` (round 1: no layer revised; Supabase and Hetzner with conditions)
- [x] MVP scope approved as drawn (~15 features, ~25 person-months, 8 to 10 months, iOS-native estimate)
- [x] Launch v1 entirely free; safety-aware routing free permanently
- [x] Apple Watch fast-follow at launch+30

### Done, awaiting founder decision

- [x] `database-deep-dive.md` (round 2): Supabase scored 3.45 vs Aiven 4.46 on the four pillars. Verdict: split architecture, Aiven (EU, ISO 27001 + SOC 2, 99.99% SLA) for personal data; self-managed PostGIS on Hetzner private net for the moat; Better Auth decoupled into the API layer. Runner-up: OVHcloud managed Postgres.
- [x] `dual-platform-strategy.md` (round 2): recommends Option D, staged cross-platform on React Native + MapLibre (~29-31 pm, iOS month 9-10, Android +4-8 weeks). Simultaneous dual-native (38-40 pm) endangers the competitive window. Runna (category leader) is the React Native existence proof.
- [x] `api-integration-map.md` (round 2): ~20 required integrations across 7 domains (30 cataloged incl. fallbacks); ~$80-130/mo at MVP, ~$350-500/mo at 10k MAU; only 6 gate the walking skeleton; top risks are Strava program terms, Android health/location review lead times, WeatherKit-on-Android goodwill, ODbL boundary.

### Open (blocks Phase 6)

- [ ] Stack final approval: revised recommendation on dashboard card 8 (Aiven split architecture, decoupled auth)
- [ ] Platform decision: dashboard card 9 (Option D recommended; amends DEC-006 client stack SwiftUI/MapKit to React Native/MapLibre and MVP effort to ~29-31 pm)
- [ ] Record the two new DECs once decided; update `mvp-scope.md` numbers and Charter if Option C or D chosen
- [ ] Verify Garmin Connect writes into Health Connect before committing Android (H6 was HealthKit-only)

## Decisions that govern the product (do not contradict without a new DEC)

| ID | Summary |
|----|---------|
| DEC-006 | Concept locked: route-first; tagline "Know where to run"; H1 reframe (travel activates, safety + novelty retain) |
| DEC-007 | GitHub → Vercel auto-publish; real content on protected `main` preview only; production branch is placeholder |
| DEC-008 | MVP scope / free launch / Watch fast-follow approved; stack held for validation; graph explorer required |

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
