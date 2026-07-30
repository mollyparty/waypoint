# Waypoint

> Know where to run

> Version-Timestamp: 2026-07-30 17:10:00 UTC-4

Waypoint is the running app that knows where you should run: it generates the right route for you, right now, from wherever you stand, with adaptive coaching layered on top (concept locked 2026-07-30, DEC-006). This repository is its single source of truth: research, product definition, decisions, knowledge, architecture, and (eventually) code all live here, versioned and pushed to GitHub.

## What is in this repository

| Path | Purpose |
|------|---------|
| `vault/` | Obsidian vault: the persistent project memory (decisions, sessions, knowledge). Open this folder as a vault in Obsidian. |
| `vault/00-START-HERE.md` | The always-current entry point. Read this first, every session. |
| `research/` | The research program: market, competitors, users, synthesis. Start with `00-RESEARCH-PLAYBOOK.md`. |
| `dashboard/index.html` | The readable HTML dashboard summarizing all research. Open in any browser. |
| `graphify-out/` | Graphify knowledge graph: queryable project brain plus token cost telemetry. |
| `docs/VERSIONING.md` | The versioning strategy for this repository. |
| `AGENTS.md` | The memory and working protocol for AI agents working in this repo, in any tool. |
| `CLAUDE.md` | Thin pointer to `AGENTS.md` for Claude Code (which looks for this filename by convention). |
| `CONTRIBUTING.md` | How to pick this project up from any machine, in any AI coding tool. |
| `CHANGELOG.md` | Human-readable history of approved versions. |

## Working from any IDE

This project is not tied to one tool. Cursor, Codex CLI, Claude Code, or any other AI coding assistant can pick this up and have full context, because that context lives in the repo itself, not in any tool's chat history. See [CONTRIBUTING.md](CONTRIBUTING.md) for setup steps if you are a collaborator (including a partner) joining from a different machine or tool.

## Versioning at a glance

- `main` is always the latest approved version.
- Work happens on short-lived branches (`feat/`, `fix/`, `docs/`) merged into `main`.
- Approved milestones are tagged with semantic versions (`v0.1.0`, `v0.2.0`, ...) and recorded in `CHANGELOG.md`.

Full details: [docs/VERSIONING.md](docs/VERSIONING.md).

## Getting oriented

1. Read [vault/00-START-HERE.md](vault/00-START-HERE.md) for the current project state.
2. Browse `vault/02-Decisions/` for why things are the way they are.
3. Open `graphify-out/graph.html` in a browser for a visual map of the project.
