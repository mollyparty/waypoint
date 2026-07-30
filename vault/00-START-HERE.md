---
type: home
created: 2026-07-30
updated: 2026-07-30T13:50
tags: [home]
---

# START HERE

This is the single always-current entry point to the Waypoint project. Every session (human or agent) begins by reading this note. It is updated at the end of every session and represents the latest approved snapshot of project state.

## Project state

- **Phase:** Research program, Phases 0 to 3 complete. Phase 4 (synthesis and concept lock, the heaviest gate) is next, gated on Claudio's review.
- **Product:** An AI running coach whose hero wedge is **adaptive route generation**: "where should I run, right now, from here, for me," with routes adapting to distance, elevation, weather, street crossings, and other constraints; coaching and routines layer on top. See [[Founder-Brief]] and [[Charter]].
- **Latest version:** v0.1.0 (foundation); v0.2.0 lands when research Phases 1 to 4 are approved.

## What is done

- [x] Git repository connected to [mollyparty/waypoint](https://github.com/mollyparty/waypoint), trunk-based versioning in place ([[DEC-001 Trunk-based versioning on main]])
- [x] Obsidian vault built as persistent project memory ([[DEC-002 Obsidian vault as project memory]])
- [x] Graphify knowledge graph integrated with git hook and cost telemetry ([[DEC-003 Graphify as queryable project brain]])
- [x] Agent memory protocol codified in `AGENTS.md` and Cursor rule
- [x] Cross-IDE support: `CLAUDE.md`, `CONTRIBUTING.md`, genericized `AGENTS.md`, continuous push cadence ([[DEC-004 Continuous push and cross-IDE agent files]])
- [x] Research program scaffolded: `research/00-RESEARCH-PLAYBOOK.md` plus per-phase folders; nine gated phases to the Business Blueprint ([[DEC-005 Phased research program with gated approvals]])
- [x] Founder discovery interview captured as [[Founder-Brief]] with testable hypotheses H1 to H7; [[Charter]] upgraded from stub to draft
- [x] Phase 1 market and industry research complete in `research/01-market/`; key findings in [[Market Research Key Findings (Phase 1)]] (route-generation whitespace real, H5 venture-scale verdict UNCERTAIN, location privacy is day-one architecture)
- [x] Phase 2 competitor analysis complete in `research/02-competitors/` (14 documents); key findings in [[Competitive Landscape Key Findings (Phase 2)]] (H2 and H3 SUPPORTED; Strava+Runna convergence is the kill-shot threat, 12 to 18 month window; HealthKit-first with proprietary context-data moat)
- [x] Phase 3 user research complete in `research/03-users/` (5 documents); key findings in [[User Research Key Findings (Phase 3)]] (H1 PARTIALLY SUPPORTED: travel is activation, safety plus home novelty is daily retention; 4 personas; interview backlog is the validation plan)

## What unlocks next

1. **Phase 4: synthesis and concept lock** (`research/04-synthesis/`), the heaviest gate: Claudio locks the concept. Key open input: the travel-vs-daily-wedge reframe from Phase 3.
2. The open founder decision on whether safety-critical routing must be free (needs a DEC before Phase 6 pricing). #open-question
2. **Concept lock at the Phase 4 gate**: the heaviest decision point of the program.
3. Capture the research pipeline as a reusable venture-discovery skill after Phase 4 if it performs well.

## Open threads

- Claudio's blueprint example (premiumcuts-blueprint.vercel.app) is unreachable; retry at Phase 8 or get the section list from him. #open-question
- Research dashboard must deploy to Vercel with deployment protection (confidential pre-launch research). #open-question
- No CI/CD yet; add when code exists. #open-question
- Partner has not yet cloned the repo or confirmed which tool they will use; `CONTRIBUTING.md` is ready for whenever they do. #open-question

## Map of the vault

- [[Charter]] - what Waypoint is (draft; locks at the Phase 4 gate)
- [[Founder-Brief]] - Claudio's vision and the hypotheses research must confirm or kill
- [[_Decision-Log]] - index of all decisions and their status
- `03-Sessions/` - one note per working session, newest is the freshest context
- `04-Knowledge/` - domain knowledge and research
- `05-Architecture/` - technical design (empty until the product exists)
- `_templates/` - templates for session, decision, and knowledge notes

## How memory works here

1. Session start: read this note, then the most recent session note.
2. Task-specific context: query the knowledge graph (`graphify query "..."`), do not re-read the repo.
3. During work: record decisions in `02-Decisions/` as they happen.
4. Session end: update this note, write the session note, rebuild the graph if docs changed, commit and push.
