# Waypoint

> Know where to run

> Version-Timestamp: 2026-07-30 21:05:00 UTC-4

Waypoint is the running app that knows where you should run: it generates the right route for you, right now, from wherever you stand, with adaptive coaching layered on top (concept locked 2026-07-30, DEC-006). This repository is its single source of truth: research, product definition, decisions, knowledge, architecture, and (eventually) code all live here, versioned and pushed to GitHub.

## What is in this repository

| Path | Purpose |
|------|---------|
| `vault/` | Obsidian vault: persistent project memory (decisions, sessions, knowledge). |
| `vault/00-START-HERE.md` | Always-current entry point. Read this first, every session. |
| `research/00-PROGRESS.md` | Phase-by-phase progress catalog (what is done, what is open). |
| `research/00-RESEARCH-PLAYBOOK.md` | Research standards and phase specs. |
| `research/01-market/` … `08-blueprint/` | Per-phase folders; each has `_index.md` with status. |
| `dashboard/index.html` | Readable HTML research dashboard (Claudio's review surface). |
| `graph/index.html` | Interactive knowledge graph explorer. |
| `graphify-out/` | Graphify data (`graph.json`) plus reports and cost telemetry. |
| `docs/VERSIONING.md` | Versioning strategy. |
| `AGENTS.md` | Agent memory and working protocol (every AI tool). |
| `CLAUDE.md` | Pointer for Claude Code → `AGENTS.md` + START-HERE + PROGRESS. |
| `CONTRIBUTING.md` | Collaborator onboarding from any machine or tool. |
| `CHANGELOG.md` | Approved version history. |

## Working from any IDE

This project is not tied to one tool. Cursor, Codex CLI, Claude Code, or any other AI coding assistant can pick this up and have full context, because that context lives in the repo itself, not in any tool's chat history. See [CONTRIBUTING.md](CONTRIBUTING.md) for setup steps if you are a collaborator (including a partner) joining from a different machine or tool.

## Versioning at a glance

- `main` is always the latest approved version.
- Work happens on short-lived branches (`feat/`, `fix/`, `docs/`) merged into `main`.
- Approved milestones are tagged with semantic versions (`v0.1.0`, `v0.2.0`, ...) and recorded in `CHANGELOG.md`.

Full details: [docs/VERSIONING.md](docs/VERSIONING.md).

## Getting oriented

1. Read [vault/00-START-HERE.md](vault/00-START-HERE.md) for the current project state.
2. Read [research/00-PROGRESS.md](research/00-PROGRESS.md) for the phase status board.
3. Browse `vault/02-Decisions/` for why things are the way they are.
4. Open `dashboard/index.html` and `graph/index.html` (or the protected Vercel preview) for visual review.
