# Changelog

> Version-Timestamp: 2026-07-30 17:20:00 UTC-4

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
