---
type: home
created: 2026-07-30
updated: 2026-07-30T13:50
tags: [home]
---

# START HERE

This is the single always-current entry point to the Waypoint project. Every session (human or agent) begins by reading this note. It is updated at the end of every session and represents the latest approved snapshot of project state.

## Project state

- **Phase:** Phases 0 to 4 complete, concept LOCKED (DEC-006). Phase 5 gate mostly passed ([[DEC-008 Phase 5 gate MVP approved stack in validation]]): MVP scope approved, launch free, Watch fast-follow. **Open: the stack verdict**, pending the deep validation study (`research/05-product/stack-validation.md`). Phase 6 starts after the stack verdict.
- **Publishing:** every push auto-deploys to the protected Vercel preview (DEC-007). Live surfaces: landing (`index.html`), dashboard (`/dashboard/`), interactive graph explorer (`/graph/`).
- **Product:** **Know where to run.** Waypoint is the running app that knows where you should run: constraint-based adaptive route generation as the hero (free-tier anchor), adaptive coaching as the paid layer, voice navigation as the execution surface, privacy as day-one architecture. Locked concept: `research/04-synthesis/concept.md`. See [[Charter]].
- **Review surface:** Claudio reviews via `dashboard/index.html` (dashboard-first gate reviews, per the amended playbook), not raw markdown.
- **Latest version:** v0.2.0 (research milestone: Phases 1 to 4, concept locked).

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
- [x] Phase 4 synthesis complete and **concept LOCKED** (DEC-006): route-first positioning, "Know where to run" tagline, H1 reframe accepted; key findings in [[Concept and Positioning (Phase 4)]]
- [x] HTML research dashboard built (`dashboard/index.html`, pulled forward from Phase 7); playbook amended to dashboard-first gate reviews

- [x] Phase 5 product definition complete in `research/05-product/` (5 documents); key findings in [[Product Definition Key Findings (Phase 5)]] (15-feature MVP, ~25 pm, GraphHopper stack)

## What unlocks next

1. **Phase 5 gate**: Claudio approves MVP scope, free/paid line, Watch timing, and stack (dashboard cards 5 to 8). The recommendation on the free/paid line (launch fully free, safety routing free permanently) would also resolve the deferred safety-free-tier question.
2. **Phase 6: business model** (Business Model Canvas, unit economics, metrics, GTM) once the gate passes.
3. The real-user interview backlog runs alongside build (`research/03-users/unmet-needs.md`).
4. Operational, already sanctioned: month-1 safety-data buildability spike; week-1 GraphHopper crossing-penalty spike; 2-day voice-guidance spike.
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
