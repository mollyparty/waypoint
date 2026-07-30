# Research Program Progress

> Version-Timestamp: 2026-07-30 21:05:00 UTC-4
>
> **This is the always-current phase catalog.** Any agent in any tool (Cursor, Claude Code, Codex, other) reads this after `vault/00-START-HERE.md` when continuing the research program. Do not invent status: update this file whenever a phase advances.

## Where we are right now (one paragraph)

Phases **0 to 4 are complete and gated**. The concept is **LOCKED** (DEC-006): route-first positioning, tagline **"Know where to run"**. Phase 5 product deliverables are written; Claudio approved MVP scope, free launch, and Watch as fast-follow (DEC-008). **Still open:** the stack decision. Round 1 validation (`stack-validation.md`) confirmed the original stack with conditions; Claudio asked for **round 2**: a deeper database study, a **dual-platform (iOS + Android) MVP strategy** (this amends the iOS-first assumption), and a full API integration map. Those three files are expected in `research/05-product/` and were in flight at last update. Phase 6 is blocked until the stack and platform decisions close. Review surface: `dashboard/index.html` (also live on the protected Vercel preview). Latest tag: **v0.2.0**.

## Phase status board

| Phase | Name | Status | Gate | Folder / surface | Vault distillate | Decision(s) |
|------:|------|--------|------|------------------|------------------|---------------|
| 0 | Founder brief and infrastructure | **COMPLETE** | Passed | `vault/01-Project/`, `research/00-RESEARCH-PLAYBOOK.md` | [[Founder-Brief]], [[Charter]] | DEC-005 |
| 1 | Market and industry | **COMPLETE** | Passed | `research/01-market/` | [[Market Research Key Findings (Phase 1)]] | (gate in session) |
| 2 | Competitor analysis | **COMPLETE** | Passed | `research/02-competitors/` | [[Competitive Landscape Key Findings (Phase 2)]] | (gate in session) |
| 3 | User research | **COMPLETE** | Passed | `research/03-users/` | [[User Research Key Findings (Phase 3)]] | safety-free resolved in DEC-008 |
| 4 | Synthesis and concept lock | **COMPLETE** | Passed / concept LOCKED | `research/04-synthesis/` | [[Concept and Positioning (Phase 4)]] | DEC-006 |
| 5 | Product definition and MVP | **IN PROGRESS** (deliverables drafted; stack gate open) | Partial: DEC-008; stack reopened for round 2 | `research/05-product/` | [[Product Definition Key Findings (Phase 5)]] | DEC-008; stack DEC pending |
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

### Open (blocks Phase 6)

- [ ] Stack final approval after round 2 research
- [ ] Platform decision: simultaneous iOS + Android vs staged (amends DEC-006 / DEC-008 iOS-first)
- [ ] Expected round 2 files (create if missing; do not invent status):
  - `research/05-product/database-deep-dive.md`
  - `research/05-product/dual-platform-strategy.md`
  - `research/05-product/api-integration-map.md`

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
