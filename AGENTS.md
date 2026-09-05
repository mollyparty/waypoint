# Waypoint Agent Protocol

> Version-Timestamp: 2026-07-30 21:05:00 UTC-4

You are working on Waypoint, a startup project built from scratch. This file is the always-loaded contract for every agent session in this repo, in any tool: Cursor, Codex CLI, Claude Code (via `CLAUDE.md`, which points here), Gemini CLI, or any other. It exists to prevent amnesia and wasted tokens. Follow it in every session, without being asked, regardless of which tool loaded it.

## Session start (do this first, always)

Memory workflow update (Version-Timestamp: 2026-09-05 18:00:00 UTC-4): read `vault/01-Project/CURRENT-WORK.json` after START-HERE. Follow `docs/MEMORY-WORKFLOW.md` for checkpoints, delegation, installation and verified publishing. Run `python tools/memory.py check` at session start. The tracked hooks replace automatic graph rebuilding with checks; graph source baselines detect drift but do not certify semantic truth. Update CURRENT-WORK throughout meaningful work and before context handoffs. Use `python tools/memory.py publish --message "type(scope): summary"` after explicit staging. Report any remaining errors or unpushed commits.

1. Read `vault/00-START-HERE.md`. Latest approved snapshot of project state.
2. Read the newest note in `vault/03-Sessions/` for freshest context and open threads.
3. Read `research/00-PROGRESS.md`. Phase-by-phase status board. Do not invent phase status.
4. Do NOT re-read the repo. For task-specific context, query the knowledge graph first.

## Context retrieval order (cheapest first)

1. This file (already loaded).
2. `vault/00-START-HERE.md` (one read).
3. `research/00-PROGRESS.md` (phase catalog; one read when doing research or product work).
4. Knowledge graph query: `graphify query "<question>" --budget 2000` against `graphify-out/graph.json` (interactive UI: `graph/index.html`). Use for any question about project content, structure, decisions, or relationships.
5. Targeted vault notes (decisions, knowledge) via wikilink names.
6. Raw files: last resort only, and only the specific files needed.

## During work

- Record every meaningful decision immediately as a note in `vault/02-Decisions/` (copy `vault/_templates/Decision-Record.md`, next `DEC-NNN` number, add a row to `_Decision-Log.md`). Do not batch this to session end.
- New durable knowledge (research, domain facts, references) goes in `vault/04-Knowledge/` from the knowledge template, with sources cited.
- Every versioned artifact you create or update carries a visible `Version-Timestamp: YYYY-MM-DD HH:mm:ss TZ` (vault notes use the `updated:` frontmatter field instead).

## Push cadence (continuous, not just session end)

Commit and push after every meaningful unit of work, not only at session end: after each todo completes, after each file group that forms a coherent change, and always before ending a turn. A human collaborator (partner) may pull `main` at any moment and expects it current. See `vault/02-Decisions/DEC-004 Continuous push and cross-IDE agent files.md`.

## Session end (mandatory checklist, never skip)

1. Write or complete the session note in `vault/03-Sessions/` (from the session template).
2. Update `vault/00-START-HERE.md`: project state, done list, next steps, open threads, `updated:` date. If any research phase moved, update `research/00-PROGRESS.md` to match (never leave the two disagreeing).
3. If docs or vault notes changed: rebuild the graph with the graphify `--update` flow. (Code changes rebuild automatically via the post-commit hook.) After any commit, check `git status` for hook-triggered `graphify-out/` changes — the hook's automatic rebuild has no LLM pass and can pollute the graph with junk nodes from markdown headings when it runs on doc-heavy commits. If node count looks inflated or labels look like headings/section names, redo the `--update` flow properly rather than trusting the hook's output.
4. Final commit and push to `main` (or the work branch) on GitHub, confirming the working tree is clean. Local-only history does not count as saved.

## Git and versioning rules

- `main` is always the latest approved version. Work on short-lived `feat/`, `fix/`, `docs/`, `chore/` branches; merge back fast. Full strategy: `docs/VERSIONING.md`.
- Conventional Commits: `type(scope): summary`.
- Every commit body ends with an attribution footer, values read from the real environment (`hostname`, the actual tool you are running as, its version); write `unknown` rather than guess:

```
Agent-Attribution: computer=<hostname>; tool=<Cursor|Codex CLI|Claude Code|other>; version=<version>; timestamp=<YYYY-MM-DD HH:mm:ss TZ>
```

- Approved milestones: semantic version tag (`v0.x.y`) plus a `CHANGELOG.md` entry written at tag time.
- Never commit secrets. `.env`, credentials, and keys are gitignored; keep it that way.

## Engineering standards

- Security, stability, reliability, compliance apply to everything shipped: validate input, handle errors on external calls, no silent failures, no hardcoded secrets, accessibility for anything user-facing.
- Lint and verify before claiming done. Report failures honestly.

## Self-check before ending any session

- Would a brand-new session, reading only START-HERE and the latest session note, know exactly where the project stands and what to do next? If no, the session-end checklist is not done.
