# Claude Code Instructions

> Version-Timestamp: 2026-07-30 21:05:00 UTC-4

This file exists because Claude Code looks for `CLAUDE.md` by convention.

## Do this first (every session)

1. Read [AGENTS.md](AGENTS.md) in full. It is the canonical protocol for every AI tool in this repo.
2. Read [vault/00-START-HERE.md](vault/00-START-HERE.md). Current project snapshot.
3. Read the newest note in [vault/03-Sessions/](vault/03-Sessions/).
4. Read [research/00-PROGRESS.md](research/00-PROGRESS.md). Phase-by-phase status board. Do not invent phase status.

Then query the knowledge graph before browsing the repo: `graphify query "<question>" --budget 2000`. Interactive view: `graph/index.html` (also on the protected Vercel preview).

## Same rules as every other tool

Nothing special about Claude Code beyond this pointer file. Same vault, same graph, same research playbook (`research/00-RESEARCH-PLAYBOOK.md`), same dashboard-first gate reviews (`dashboard/index.html`), same continuous push to `main`, same attribution footer on commits. If you change project state, update START-HERE and `research/00-PROGRESS.md` together so the next tool does not inherit a lie.
