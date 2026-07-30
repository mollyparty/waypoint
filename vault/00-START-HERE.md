---
type: home
created: 2026-07-30
updated: 2026-07-30T13:30
tags: [home]
---

# START HERE

This is the single always-current entry point to the Waypoint project. Every session (human or agent) begins by reading this note. It is updated at the end of every session and represents the latest approved snapshot of project state.

## Project state

- **Phase:** Foundation (workspace, versioning, memory infrastructure)
- **Product:** An AI running coach (working tagline from the repo: "Your AI Running Coach"). Full product discovery is the next major phase.
- **Latest version:** v0.1.0 (foundation)

## What is done

- [x] Git repository connected to [mollyparty/waypoint](https://github.com/mollyparty/waypoint), trunk-based versioning in place ([[DEC-001 Trunk-based versioning on main]])
- [x] Obsidian vault built as persistent project memory ([[DEC-002 Obsidian vault as project memory]])
- [x] Graphify knowledge graph integrated with git hook and cost telemetry ([[DEC-003 Graphify as queryable project brain]])
- [x] Agent memory protocol codified in `AGENTS.md` and Cursor rule
- [x] Cross-IDE support: `CLAUDE.md`, `CONTRIBUTING.md`, genericized `AGENTS.md`, continuous push cadence ([[DEC-004 Continuous push and cross-IDE agent files]])

## What unlocks next

1. **Product discovery session**: define what Waypoint is; capture into [[Charter]] and `01-Project/`.
2. **Stack and architecture decision**: record as decision notes in `02-Decisions/`.
3. Capture the session-end memory routine as a reusable skill once it has run twice.

## Open threads

- Product definition beyond the "AI Running Coach" tagline is open. #open-question
- No CI/CD yet; add when code exists. #open-question
- Partner has not yet cloned the repo or confirmed which tool they will use; `CONTRIBUTING.md` is ready for whenever they do. #open-question

## Map of the vault

- [[Charter]] - what Waypoint is (stub until product discovery)
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
