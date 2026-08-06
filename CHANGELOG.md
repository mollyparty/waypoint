# Changelog

> Version-Timestamp: 2026-08-06 15:00:00 UTC-4

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Staged for **v0.4.0**, which tags once the blueprint is signed off and the Phase 9 gate is closed. Neither has happened, so this is not yet a release.

### Added

- **Phase 9, financial strategy and founding team** (`research/09-financial-team/`): `legal-formation.md`, `operating-model.md`, `team-roadmap.md`, `capital-structure.md`, `fundraising-plan.md`. Opened outside the original program, which [DEC-005] ended at Phase 8, because the founding team was defined for the first time and the definition invalidated assumptions eight phases had rested on.
- Investor business blueprint (`blueprint/blueprint.md` and `blueprint/index.html`), 17 sections, drafted at Phase 8 and awaiting founder review.
- Phase 9 section on the research dashboard with six open gate cards.

### Changed

- **The financial model was rebuilt from the ground up.** The founding team is three part-time partners, two of them minors, building AI-assisted rather than hiring. Monthly burn is roughly $400 rather than $15,000; cash to public launch is $27,000 to $47,000 rather than $230,000; the ask is $50,000 on a post-money SAFE at a $1.5M cap rather than a $350,000 to $400,000 pre-seed. Three-year cash consumed all the way to break-even is roughly $40,000 to $53,000.
- **Break-even fell by an order of magnitude, to roughly 235 paying subscribers** from the ~3,000 quoted since Phase 6. The old figure divided a $15,000 monthly base that assumed a founder salary and a contractor retainer, neither of which exists.
- **Blueprint sections 12 and 13 rewritten**, the executive summary corrected, and four risks added covering founder capacity, the AI-leverage assumption, key-person concentration, and the minor-founder IP question.
- **DEC-010's iOS date is superseded pending the Phase 9 gate.** It assumed 2.5 to 3.0 full-time-equivalent people; the actual team has none. The recommendation is to ship the walking skeleton as the product, landing iOS at month 12 to 14.
- Charter now names the three founders and their roles, replacing "solo founder building from scratch".

### Fixed

- **A self-contradiction in the Phase 6 knowledge note**, which asserted both that the Android date was the public launch and that DEC-013 had overridden it to iOS. The graph carried the same error in a node label. An agent reading only the distillate, which is what the retrieval order instructs, could have acted on the wrong one.
- **Knowledge graph coverage: 86 of 86 project documents now have a node**, up from 75. Eleven were entirely absent and therefore invisible to every query: five competitor profiles, DEC-007, four session notes, and the Phase 6 distillate. Also removed six Obsidian settings nodes that the AST pass had extracted from configuration, and corrected three node labels still asserting "gate pending" or "not started" for closed work.
- **The graphify post-commit hook is now scoped to code paths.** Its rebuild runs without an LLM pass, so on a markdown-only tree it extracts headings as nodes and drops curated ones; one commit lost 9 nodes and 19 links before being restored. Note that `.git/hooks/` is untracked, so this fix does not travel to a fresh clone.
- Phases 7 and 8 were recorded inside the Phase 6 session note, where filename-based lookup could not find them. Split into their own dated note.
- Three cross-document cost conflicts reconciled with the reason stated: infrastructure at MVP ($135 to $255, not $80 to $130), the net revenue multiplier (0.8088, not 0.84), and the note that `unit-economics.md` is still priced against a $7.99/month case that DEC-011 replaced.
- Stale catalog claims in `vault/00-START-HERE.md` and `research/00-PROGRESS.md`; open questions in the Phase 3 and 4 distillates that DEC-008 and DEC-011 had already closed; the architecture index still calling the stack decision future work; DEC-007's missing alternatives section.

## [0.3.0] - 2026-08-06

Product definition and business model both locked. Waypoint now has an approved MVP scope, a decided technical stack, a price, a free/paid boundary, a measurement system, and a go-to-market plan.

### Added

- Phase 5 round-2 studies (`research/05-product/`): `database-deep-dive.md`, `dual-platform-strategy.md`, and `api-integration-map.md`, the last cataloging roughly 20 required integrations across 7 domains at $80 to $130 per month at MVP scale.
- Phase 6 business model (`research/06-business-model/`): `business-model-canvas.md` as the integrating document, plus `revenue-model.md`, `unit-economics.md`, `metrics.md`, and `gtm-plan.md`.
- Interactive knowledge graph explorer (`graph/index.html`) and a root landing page for the published artifact set.
- `research/00-PROGRESS.md`, the always-current phase catalog that makes cross-tool handoff possible without re-reading the repository.

### Changed

- **Data layer (DEC-009)**: Supabase dropped for a split architecture of Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on the Hetzner private network for the geospatial moat, and Better Auth decoupled into Waypoint's own API layer. Carries an explicit revisit clause at four named checkpoints.
- **Platform (DEC-010)**: the MVP ships both iOS and Android from one React Native codebase with MapLibre maps, iOS at month 9 to 10 and Android 4 to 8 weeks later, revising effort to roughly 29 to 31 person-months.
- **Pricing (DEC-011)**: $99.99 per year list, $12.99 per month, 21-day annual-only trial, and a price-preserved Founding Runner rate at $69.99 per year for the free-era cohort. The coaching layer is the only paid product; every routing constraint, the Watch app, and GPX export are free permanently and named publicly at launch. Lifetime tier and data monetization rejected on the record.
- **Measurement (DEC-012)**: cohort retention moves to a first-party Postgres event table on the existing account identifier, because TelemetryDeck deliberately provides no stable per-user identifier and therefore cannot produce it. PRD goals G3 and G4 re-based to activated-cohort definitions, and activation redefined as a completed recorded run rather than a started one.
- **Go-to-market (DEC-013)**: one segment in the founder's home metro, subject to a month-1 pedestrian-data spike that is now treated as a go-to-market gate. The iOS date at month 9 to 10 carries the public launch, overriding the plan's Android recommendation, with four compensating conditions attached.

### Fixed

- Stale Supabase references in `api-integration-map.md` (sign-in section, master integration table, and critical path) corrected to match DEC-009.

## [0.2.0] - 2026-07-30

### Added

- Research program infrastructure: `research/00-RESEARCH-PLAYBOOK.md` (nine gated phases, citation and confidence standards, definition-of-done checklists), amended to dashboard-first gate reviews.
- Founder Brief (`vault/01-Project/Founder-Brief.md`) with seven testable hypotheses from the founder discovery interview.
- Phase 1 market research (`research/01-market/`): landscape, TAM-SAM-SOM sizing, industry trends, regulatory compliance with a 15-item MVP checklist.
- Phase 2 competitor analysis (`research/02-competitors/`): ten profiles, adjacent platforms, feature and pricing matrices, positioning maps, gap analysis.
- Phase 3 user research (`research/03-users/`): pain points, segmentation, four personas, jobs-to-be-done, ranked unmet needs with the interview backlog.
- Phase 4 synthesis (`research/04-synthesis/`): opportunity definition, positioning, hypothesis verdicts, and the concept document.
- HTML research dashboard (`dashboard/index.html`): single-file readable summary of the research corpus and gate decisions.

### Changed

- **Concept locked (DEC-006)**: route-first positioning ("the running app that generates the right route for you, right now, from wherever you stand"); tagline changed from "Your AI Running Coach" to **"Know where to run"**; travel reframed as activation moment with safety plus home novelty as the daily retention wedge. README and Charter updated accordingly.

## [0.1.0] - 2026-07-30

### Added

- Repository foundation: README, versioning strategy (`docs/VERSIONING.md`), changelog, gitignore.
- Obsidian vault (`vault/`) as persistent project memory: START-HERE entry point, Project, Decisions, Sessions, Knowledge, Architecture folders, and note templates.
- Graphify knowledge graph integration (`graphify-out/`) with git post-commit hook and token cost telemetry.
- Agent memory protocol (`AGENTS.md` and Cursor rule) codifying session start and session end routines.

[Unreleased]: https://github.com/mollyparty/waypoint/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/mollyparty/waypoint/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/mollyparty/waypoint/releases/tag/v0.1.0
