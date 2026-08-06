# Research Program Progress

> Version-Timestamp: 2026-08-06 15:45:00 UTC-4
>
> **This is the always-current phase catalog.** Any agent in any tool (Cursor, Claude Code, Codex, other) reads this after `vault/00-START-HERE.md` when continuing the research program. Do not invent status: update this file whenever a phase advances.

## Where we are right now (one paragraph)

Phases **0 through 8 are complete**, with Phase 8's blueprint awaiting founder review and **Phase 9 (financial strategy and founding team) now the active workstream**. The concept is **LOCKED** (DEC-006): route-first positioning, tagline **"Know where to run"**. Phase 5 closed on 2026-08-06 with all five gate decisions made: MVP scope approved, v1 launches entirely free, Watch is a fast-follow (DEC-008); the data layer **drops Supabase** for a split architecture of Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on the Hetzner private network for the geospatial moat, and auth decoupled into Waypoint's API layer via Better Auth (DEC-009, carrying an explicit revisit clause at Claudio's instruction); and the MVP ships **both platforms from one React Native codebase** with MapLibre maps, iOS at month 9 to 10 and Android 4 to 8 weeks later, ~29 to 31 person-months (DEC-010). **Phase 6 is COMPLETE and its gate is CLOSED** (2026-08-06, DEC-011 / DEC-012 / DEC-013). The governing finding: unit economics are a function of distribution, not pricing, since paid acquisition returns 53 to 70 cents on the dollar at every credible price and the model needs roughly 84 percent organic acquisition to clear 3:1. Price is $99.99/yr with the coaching layer as the only paid product; the beachhead is the founder's home metro; **the iOS date at month 9 to 10 carries the public launch**, overriding the plan's Android recommendation.

**Phase 7 is CLOSED** and **Phase 8's blueprint draft is COMPLETE**: `blueprint/blueprint.md` (master markdown) and `blueprint/index.html` (investor-facing site, 17 sections), with sections 12 and 13 rewritten by Phase 9.

**Phase 9 deliverables are COMPLETE and its gate is OPEN with six cards.** It was opened on 2026-08-06 when the founding team was defined for the first time as three part-time partners, two of them minors, building AI-assisted rather than hiring. That invalidated three figures that eight phases of research had rested on: the ~$230k cash build, the ~$15k/month operating base, and the ~$350k to $400k pre-seed, which was their sum. Real burn is ~$400/month, break-even is ~235 paying subscribers rather than ~3,000, and the recommended ask is $50k on a post-money SAFE at a $1.5M cap. **The governing finding: the binding constraint is calendar time, not money** — 29 to 31 person-months of approved scope against roughly 7.5 person-months a year of capacity does not fit a 12 to 18 month window, so gate card 1 recommends shipping the walking skeleton as the product, landing iOS at month 12 to 14 and superseding DEC-010's dates.

**The features catalog now holds release-phase authority** (2026-08-06, DEC-020). `catalog/features.json` carries 70 entries — 30 features, 15 compliance requirements, 19 non-functional requirements and the 6 items DEC-006 ruled out — each with its persona, need and job linkage, capabilities breakout, acceptance criteria, RICE values and dependencies. `catalog/index.html` is the working surface: filter by any of those dimensions, move a feature between MVP, v1.x, v2 and cut, and read the recomputed effort and projected iOS launch month against the competitive window. `mvp-scope.md`, `prd.md` and `rice-prioritization.md` are annotated: their analysis stands, their phase columns do not. **It corrected full scope from 29-31 to roughly 32-33 React Native person-months**, because pricing the 34 obligations individually costs 4.35 native person-months against the single ~2.0 "release overhead" line the planning documents carried. The recut v1 is unaffected and validated: the model reproduces the published walking skeleton, compliance minimum, hardening line, v1 total and month-13 launch independently. See [[Features Catalog and Scope Arithmetic]].

**Next agent action: answer the six Phase 9 gate cards** on `dashboard/index.html` and record DEC-014 onward. **Card 1 should be settled in `catalog/index.html`**, which loads the recommended recut by default with the three alternatives one click away; then update `features.json` to match and rerun `python catalog/build.py`. Blueprint approval and the v0.4.0 tag follow. Review surfaces: `dashboard/index.html` for research, `catalog/index.html` for scope, `blueprint/index.html` for the investor document, all on the protected Vercel preview. Latest tag: **v0.3.0**.

## Phase status board

| Phase | Name | Status | Gate | Folder / surface | Vault distillate | Decision(s) |
|------:|------|--------|------|------------------|------------------|---------------|
| 0 | Founder brief and infrastructure | **COMPLETE** | Passed | `vault/01-Project/`, `research/00-RESEARCH-PLAYBOOK.md` | [[Founder-Brief]], [[Charter]] | DEC-005 |
| 1 | Market and industry | **COMPLETE** | Passed | `research/01-market/` | [[Market Research Key Findings (Phase 1)]] | (gate in session) |
| 2 | Competitor analysis | **COMPLETE** | Passed | `research/02-competitors/` | [[Competitive Landscape Key Findings (Phase 2)]] | (gate in session) |
| 3 | User research | **COMPLETE** | Passed | `research/03-users/` | [[User Research Key Findings (Phase 3)]] | safety-free resolved in DEC-008 |
| 4 | Synthesis and concept lock | **COMPLETE** | Passed / concept LOCKED | `research/04-synthesis/` | [[Concept and Positioning (Phase 4)]] | DEC-006 |
| 5 | Product definition and MVP | **COMPLETE** | Passed (all 5 cards) | `research/05-product/` | [[Product Definition Key Findings (Phase 5)]] | DEC-008, DEC-009, DEC-010 |
| 6 | Business model and GTM | **COMPLETE** | **CLOSED** 2026-08-06 (DEC-011, DEC-012, DEC-013) | `research/06-business-model/` | [[Business Model and GTM Key Findings (Phase 6)]] | done |
| 7 | HTML research dashboard | **COMPLETE** | Closed 2026-08-06; covers Phases 0-6, HTML validated | `dashboard/index.html`, `graph/index.html` (live on preview) | — | DEC-007 (publishing) |
| 8 | Business Blueprint | **DRAFT COMPLETE** | **Open: founder review**, 4 items in `08-blueprint/_index.md`. Sections 12 and 13 rewritten by Phase 9 | `blueprint/blueprint.md`, `blueprint/index.html` | — | pending v0.4.0 |
| 9 | Financial strategy and founding team | **DELIVERABLES COMPLETE** | **Open: 6 cards** in `09-financial-team/_index.md` | `research/09-financial-team/` | [[Financial Strategy and Founding Team (Phase 9)]] | pending |

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

## Phase 6 detail (closed 2026-08-06)

### Written 2026-08-06

- [x] `business-model-canvas.md` — nine blocks plus the cross-document reconciliation. **The document to read first.**
- [x] `revenue-model.md` — $99.99/yr list, $12.99/mo, 21-day annual-only trial, Founding Runner $69.99/yr price-preserved. Lifetime tier and data monetization rejected on the record.
- [x] `unit-economics.md` — free active user costs under $1/year; paid acquisition returns 53 to 70 cents on the dollar at every credible price. **Its break-even figure of ~3,000 subscribers is superseded by Phase 9 (~235), and its tables are still priced at a $7.99/mo mid case that DEC-011 replaced.**
- [x] `metrics.md` — North Star Weekly Routed Runners (80 percent completion floor inside the definition); activation = first generated route completed as a recorded run; Good Route Rate; ten guardrails.
- [x] `gtm-plan.md` — one metro, one segment; run clubs, then Reddit, then store optimization; SEO and paid acquisition argued against. Its recommendation that the Android date carry the public launch was **overridden** at the gate.

### Gate outcome (2026-08-06): all six closed

- [x] **Price** approved as recommended: $99.99/yr, $12.99/mo, 21-day annual-only trial, Founding Runner $69.99/yr price-preserved (DEC-011)
- [x] **Free/paid boundary** approved as recommended and the escape hatch declined: all routing constraints, Watch and GPX free forever, coaching layer alone is paid, free tier named publicly at launch (DEC-011)
- [x] **Analytics identity** fixed: first-party Postgres cohort table on the existing account identifier; TelemetryDeck keeps aggregate signals; PostHog EU deferred to v1.x (DEC-012)
- [x] **PRD G3 and G4 re-based** to activated-cohort definitions with a separate install-level benchmark line; activation redefined as a completed recorded run (DEC-012)
- [x] **Beachhead:** the founder's home metro, subject to the month-1 pedestrian-data spike (DEC-013)
- [x] **Launch shape: OVERRIDDEN.** The iOS date at month 9 to 10 carries the public launch, not the Android date (DEC-013). Reasons: the Apple featuring nomination is iOS-only, speed matters in a 12 to 18 month window, and iOS carries ~85 percent of category subscription revenue

### Amendments this gate produced (all applied)

- [x] `05-product/prd.md` goals G3 and G4 re-based; assumption A1 partly resolved
- [x] `05-product/api-integration-map.md` section 6.2 amended for the analytics split, section 4.2 amended for Better Auth, and the Supabase rows in the master table and critical path replaced per DEC-009
- [x] `06-business-model/gtm-plan.md` section 5.1 annotated as overridden, with the compensating conditions listed
- [x] `06-business-model/business-model-canvas.md` section 11 records the outcome and the override reasoning

### Conditions the launch override created (carry into build planning)

- [ ] The beta cohort's month-8 target of 150 to 300 active testers is now a **hard gate on the launch date**, not a milestone
- [ ] Seed reviews from the beta cohort at launch; crash-free sessions above 99.5 percent is a release gate
- [ ] Android waitlist capture at every in-person event from launch onward
- [ ] File the Apple featuring nomination at month 6 to 7 (roughly three-month lead)
- [ ] Treat the month-1 safety-data buildability spike as a **go-to-market gate**, not only a technical one

### Carried into the build phase (not blockers)

- [ ] Verify Garmin Connect writes into Health Connect before Android work begins (H6 was verified for HealthKit only)
- [x] ~~`api-integration-map.md` section 4 still names Supabase Auth~~ **Resolved 2026-08-06:** section 4.2 now carries a DEC-009 amendment banner, and the Supabase rows in the master integration table and the critical path were replaced
- [ ] Android long-lead paperwork (Play org account, Health Connect + fine-location declarations) starts month 1 of the build

## Phase 9 detail (deliverables complete, gate OPEN)

### Written

- [x] `legal-formation.md` — Delaware C-corp sequence; UTMA custodial shares for the two minor founders; the voidable-IP cure path (guardian co-signature plus re-execution at 18); 83(b) inside 30 days with no extensions; Daniel as Apple Account Holder (legal age of majority plus authority to bind; D-U-N-S up to 14 business days); formation at $3,300 to $9,000 including the minor-founder premium.
- [x] `operating-model.md` — burn of ~$260 pre-formation, ~$400 build, ~$900 beta, ~$1,050 post-launch; AI tooling at $160/mo plus a $50 overage allowance; cash to launch ~$12k to $18k excluding privacy counsel; 36-month projection totaling ~$40k to $53k; **and the reconciliation of three cross-document cost conflicts.**
- [x] `team-roadmap.md` — roles per founder; ~7.5 person-months a year of real capacity against 29 to 31 of scope; the AI-multiplier sensitivity table; the recut v1 at 12 to 15 person-months; the re-derived schedule; school seasonality; hiring triggers; the month-6 checkpoint.
- [x] `capital-structure.md` — 40/30/30 recommended with 34/33/33 and 50/25/25 argued rather than dismissed; four-year vesting with a one-year cliff plus a college-transition review with three named outcomes; a 10 percent pool; the dilution waterfall (founders ~56 percent combined after a seed).
- [x] `fundraising-plan.md` — $50k on a post-money SAFE at a $1.5M cap; why a SAFE and not a note or priced equity; milestones that make a pre-seed raisable; how investors will read a part-time team with two minors; the diligence-readiness checklist.

### Cross-document corrections this phase made (use these, not the originals)

- [x] **Infrastructure at MVP: $135 to $255/month** (`unit-economics.md` 1.1), not the $80 to $130 in `api-integration-map.md` 8.2, which was summed before DEC-009 replaced Supabase. The integration map's per-service table is still correct; only its 8.2 total is stale.
- [x] **Net revenue multiplier: 0.8088** (`unit-economics.md` 1.3), not 0.84 (`revenue-model.md` 6.2). The former includes the refund allowance.
- [x] **Break-even: ~235 paying subscribers**, not ~3,000. The old figure divided a $15,000 monthly base that assumed salaries and contractors.
- [ ] **Not yet done: re-run the `unit-economics.md` tables at the locked $99.99/yr price.** They are still built on a $7.99/mo mid case. Every correction runs in Waypoint's favor (LTV ~$107 to $115 rather than $86), so nothing is hidden, but the published figures understate the business and must not be quoted to an investor as they stand.

### Gate: six cards OPEN on `dashboard/index.html`

| # | Decision | Recommendation |
|---|---|---|
| 1 | Scope and timeline | Ship the walking skeleton as the product. iOS month 12 to 14. **Supersedes DEC-010's dates.** Settle it in `catalog/index.html`, where this is the default preset and the alternatives are one click away |
| 2 | Founder equity split | Daniel 40, Claudio 30, Asher 30 |
| 3 | Vesting | Four years, one-year cliff, all three, plus a college-transition review |
| 4 | Option pool | 10 percent at formation |
| 5 | Formation timing | Incorporate before the round |
| 6 | Round size and terms | $50k post-money SAFE at a $1.5M cap |

### Carried forward

- [ ] The 1.8x AI leverage multiplier is unmeasured and underwrites the schedule, the scope cut and the round size. The month-6 checkpoint replaces it with evidence; below 1.2x the plan is rebuilt.
- [ ] Decide explicitly whether the goal is venture scale or profitable independence. Break-even at ~235 subscribers makes the second genuinely available, and it fits the uncertain H5 verdict.
- [ ] Map Daniel's other business's seasonality against this schedule before finalizing it.

## Features catalog (built 2026-08-06, DEC-020)

Not a research phase. A standing surface, and the source of truth for release phase.

### Files

- `catalog/features.json` — 70 entries. **Edit this, then run `python catalog/build.py`.**
- `catalog/index.html` — the interactive surface. Filter, reassign, recompute.
- `catalog/FEATURES.md` — generated mirror, 2,500-plus lines. Read this if you have no browser. Never edit it.
- `catalog/build.py` — validator plus generator. `--check` validates without writing.

### What it contains

| Kind | Count | Notes |
|---|---:|---|
| Features | 30 | H-01 to H-10, X-01 to X-03, TS-01 to TS-10, P-01 to P-06, O-01. Capabilities, acceptance criteria, persona / need / job linkage, RICE, dependencies, integrations, pull-forward triggers, risks, sources |
| Compliance requirements | 15 | C-1 to C-15, locked into the MVP. C-1, C-2, C-3 and C-11 are engineered by O-01 and carry zero effort with a `satisfiedBy` pointer; C-14 points at TS-08. That is how double counting is avoided |
| Non-functional requirements | 19 | NF-P1-4, NF-O1-3, NF-A1-6, NF-L1-6, locked. These answer `team-roadmap.md` open question 4, which flagged launch hardening as its least-specified line |
| Ruled out | 6 | N-01 to N-06, the DEC-006 NOT list, zero effort and locked out, so nobody re-proposes a social feed |

### The effort model, and what it validated

`calendarMonths = (nativeEffort x 1.20 / aiMultiplier) / 7.5 x 12 + 1.5`

| Scenario | React Native pm | Projected iOS launch | Published figure |
|---|---:|---:|---|
| Walking skeleton only | 8.16 | month 9 | 8 to 9 pm ✓ |
| **Recut v1 (default)** | **13.38** | **month 13** | 12 to 15 pm, month 12 to 14 ✓ |
| Full MVP v1 | 32.52 | month 30 | **29 to 31 pm — corrected upward** |
| PRD P0 list | 51.72 | month 47 | never costed before |

Four published figures reproduce from one set of constants, which is the check that the model is not inventing numbers. The correction: pricing the 34 obligations individually costs 4.35 native person-months against the single ~2.0 "release overhead" line the planning documents carried, so full scope is ~32-33 rather than 29-31. The recut is unaffected because `team-roadmap.md` had already broken those lines out.

### Documents annotated (analysis kept, phase authority moved)

- [x] `research/05-product/mvp-scope.md` — plus the finding that its section 6 walking skeleton is a thin slice through eight features, not a subset of whole ones; read as a feature list it over-estimates by 2x.
- [x] `research/05-product/prd.md` — plus the arithmetic showing its P0 tier projects to month 47 at real capacity.
- [x] `research/05-product/rice-prioritization.md` — plus the warning that its effort column is in iOS-native units and must not be mixed with React Native figures.

### The four conflicts, each with a written recommendation

| ID | Question | Resolution |
|---|---|---|
| CF-1 | Apple Watch: P0 or v1.x? | v1.x, per GD-2 |
| CF-2 | All ten constraints at launch? | Subset; the deferred three cost 6.0 pm for the weakest-evidenced needs |
| CF-3 | Route explanations at launch? | Split: H-09 at launch, P-03 after |
| CF-4 | Paid seam at launch? | Free launch, per GD-1 and DEC-011 |

### Carried forward

- [ ] The 1.20x platform multiplier is a reconciliation of two published conversions, not a measurement. The walking-skeleton build is the first chance to check it.
- [ ] Scenario state in the browser is `localStorage` only. A scope decision made in the UI must be exported and written back into `features.json` or it exists in one browser.
- [ ] `build.py` is not wired into a hook. Editing the JSON without running it leaves `FEATURES.md` stale, which is the exact drift this catalog was built to end. Consider `--check` in pre-commit.

## Decisions that govern the product (do not contradict without a new DEC)

| ID | Summary |
|----|---------|
| DEC-006 | Concept locked: route-first; tagline "Know where to run"; H1 reframe (travel activates, safety + novelty retain) |
| DEC-007 | GitHub → Vercel auto-publish; real content on protected `main` preview only; production branch is placeholder |
| DEC-008 | MVP scope / free launch / Watch fast-follow approved; stack held for validation; graph explorer required |
| DEC-009 | Data layer: Aiven for PostgreSQL (EU) for personal data + self-managed PostGIS on Hetzner for the moat + Better Auth decoupled into the API layer. Supabase dropped. Revisitable at four named checkpoints |
| DEC-010 | Staged cross-platform MVP: one React Native codebase, MapLibre both platforms, ~29-31 person-months. Amends DEC-006 client stack and DEC-008 effort. **Its month 9-10 iOS date assumed 2.5 to 3.0 FTE and is superseded pending Phase 9 gate card 1** |
| DEC-011 | Pricing and the permanent free tier: $99.99/yr, $12.99/mo, 21-day annual-only trial, Founding Runner $69.99/yr price-preserved. Coaching layer is the only paid product; everything else free forever and named publicly at launch. Lifetime tier and data monetization rejected |
| DEC-012 | Measurement corrections: cohort retention moves to a first-party Postgres event table (TelemetryDeck cannot provide a stable identifier); PRD G3 and G4 re-based to activated-cohort definitions; activation redefined as a completed recorded run |
| DEC-013 | Beachhead is the founder's home metro subject to the month-1 data spike; **the iOS date carries the public launch**, overriding the GTM plan's Android recommendation, with four compensating conditions |
| DEC-020 | **`catalog/features.json` is the source of truth for release phase.** 70 entries; `mvp-scope.md`, `prd.md` and `rice-prioritization.md` keep their analysis and lose their phase columns. Compliance and non-functional entries are locked into the MVP with their effort counted; the DEC-006 NOT list is locked out. Refines DEC-010's total to ~32-33 person-months. DEC-014 to DEC-019 stay reserved for the open Phase 9 gate |

## Surfaces every agent must know

| Surface | Path | Purpose |
|---------|------|---------|
| Project state | `vault/00-START-HERE.md` | Latest approved snapshot |
| This catalog | `research/00-PROGRESS.md` | Phase-by-phase status |
| Playbook | `research/00-RESEARCH-PLAYBOOK.md` | Standards, citation, gate definition of done |
| Readable review | `dashboard/index.html` | Claudio's review surface (dashboard-first) |
| **Scope source of truth** | `catalog/features.json` | **Canonical release phase for all 70 entries (DEC-020). Regenerate the mirror with `python catalog/build.py` after any edit** |
| Scope working surface | `catalog/index.html` | Filter by persona, need, job, module or release; reassign features and watch the launch month recompute |
| Scope mirror for agents | `catalog/FEATURES.md` | Generated. Read it instead of the JSON; never edit it |
| Knowledge graph UI | `graph/index.html` | Interactive explorer over `graphify-out/graph.json` |
| Landing (Vercel) | `index.html` | Links dashboard, catalog, graph and blueprint |
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
| v0.4.0 | Phases 7 to 9 approved (blueprint signed off and the Phase 9 gate closed). Entry already staged under Unreleased in `CHANGELOG.md` |

## How to update this file

When a phase advances: change the status board row, tick or add items in that phase's detail section, update the one-paragraph "Where we are" block, bump the Version-Timestamp, then update `vault/00-START-HERE.md` to match. Never leave START-HERE and this file disagreeing.

**Graph state.** 227 nodes, 542 edges, 15 communities as of 2026-08-06, with coverage measured at 104 of 104 corpus documents (rule: every `.md` file except `vault/_templates/` and `GRAPH_REPORT.md` itself), zero dangling links, zero isolated nodes. The catalog merge added 20 nodes and 46 edges, so a question about what ships when resolves to `catalog/features.json` rather than to one of the three documents that disagree.

**A note on the graph.** The graphify post-commit hook has been scoped to code file extensions, because its rebuild runs without an LLM pass and on a markdown-only tree it extracts headings as nodes while dropping curated ones. Documentation commits no longer trigger it; update the graph deliberately instead. **That fix lives in `.git/hooks/post-commit`, which git does not track**, so a fresh clone on another machine will not have it. Watch for the graph losing nodes after a doc commit and reapply it if so.
