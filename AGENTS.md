# Waypoint Agent Protocol

> Version-Timestamp: 2026-07-30 12:25:00 UTC-4

You are working on Waypoint, a startup project built from scratch. This file is the always-loaded contract for every agent session in this repo. It exists to prevent amnesia and wasted tokens. Follow it in every session, without being asked.

## Session start (do this first, always)

1. Read `vault/00-START-HERE.md`. It is the latest approved snapshot of project state.
2. Read the newest note in `vault/03-Sessions/` for the freshest context and open threads.
3. Do NOT re-read the repo. For task-specific context, query the knowledge graph first.

## Context retrieval order (cheapest first)

1. This file (already loaded).
2. `vault/00-START-HERE.md` (one read).
3. Knowledge graph query: `graphify query "<question>" --budget 2000` against `graphify-out/graph.json` (see the graphify skill). Use for any question about project content, structure, decisions, or relationships.
4. Targeted vault notes (decisions, knowledge) via wikilink names.
5. Raw files: last resort only, and only the specific files needed.

## During work

- Record every meaningful decision immediately as a note in `vault/02-Decisions/` (copy `vault/_templates/Decision-Record.md`, next `DEC-NNN` number, add a row to `_Decision-Log.md`). Do not batch this to session end.
- New durable knowledge (research, domain facts, references) goes in `vault/04-Knowledge/` from the knowledge template, with sources cited.
- Every versioned artifact you create or update carries a visible `Version-Timestamp: YYYY-MM-DD HH:mm:ss TZ` (vault notes use the `updated:` frontmatter field instead).

## Session end (mandatory checklist, never skip)

1. Write or complete the session note in `vault/03-Sessions/` (from the session template).
2. Update `vault/00-START-HERE.md`: project state, done list, next steps, open threads, `updated:` date.
3. If docs or vault notes changed: rebuild the graph with the graphify `--update` flow. (Code changes rebuild automatically via the post-commit hook.)
4. Commit and push to `main` (or the work branch) on GitHub. Local-only history does not count as saved.

## Git and versioning rules

- `main` is always the latest approved version. Work on short-lived `feat/`, `fix/`, `docs/`, `chore/` branches; merge back fast. Full strategy: `docs/VERSIONING.md`.
- Conventional Commits: `type(scope): summary`.
- Every commit body ends with an attribution footer, values read from the real environment (`hostname`, tool version); write `unknown` rather than guess:

```
Agent-Attribution: computer=<hostname>; tool=Cursor; version=<version>; timestamp=<YYYY-MM-DD HH:mm:ss TZ>
```

- Approved milestones: semantic version tag (`v0.x.y`) plus a `CHANGELOG.md` entry written at tag time.
- Never commit secrets. `.env`, credentials, and keys are gitignored; keep it that way.

## Engineering standards

- Security, stability, reliability, compliance apply to everything shipped: validate input, handle errors on external calls, no silent failures, no hardcoded secrets, accessibility for anything user-facing.
- Lint and verify before claiming done. Report failures honestly.

## Self-check before ending any session

- Would a brand-new session, reading only START-HERE and the latest session note, know exactly where the project stands and what to do next? If no, the session-end checklist is not done.
