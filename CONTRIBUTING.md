# Working on Waypoint

> Version-Timestamp: 2026-07-30 21:05:00 UTC-4

This project is designed to be picked up from any machine, by any collaborator, using any AI coding tool. This is how.

## 1. Clone the repo

```bash
git clone https://github.com/mollyparty/waypoint.git
cd waypoint
git pull
```

Set your own git identity if you have not already (each collaborator uses their own name/email):

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

## 2. Pick any AI coding tool (they all read the same instructions)

| Tool | What it reads |
|------|----------------|
| Cursor | `AGENTS.md` + `.cursor/rules/memory-protocol.mdc` |
| Codex CLI / ChatGPT | `AGENTS.md` |
| Claude Code | `CLAUDE.md` (pointer) → `AGENTS.md` |
| Anything else | `AGENTS.md` |

**Always read [AGENTS.md](AGENTS.md) first**, then [vault/00-START-HERE.md](vault/00-START-HERE.md), then [research/00-PROGRESS.md](research/00-PROGRESS.md).

## 3. Orient in under five minutes

| Read | Why |
|------|-----|
| `vault/00-START-HERE.md` | Latest approved project state |
| Newest file in `vault/03-Sessions/` | Freshest open threads |
| `research/00-PROGRESS.md` | Phase catalog: what is done, what is open |
| `dashboard/index.html` | Readable research + gate decisions |
| `vault/02-Decisions/_Decision-Log.md` | Locked choices (do not contradict without a new DEC) |

Optional: open `vault/` as an Obsidian vault. Notes are plain markdown either way.

## 4. Graphify (knowledge graph)

```bash
pip install graphifyy
graphify query "<question>" --budget 2000
```

Outputs: `graphify-out/` (`graph.json`, `GRAPH_REPORT.md`). Prefer the interactive explorer `graph/index.html` over the raw Graphify HTML. A post-commit hook may rewrite the graph on doc-heavy commits; if labels look like junk headings, restore and run the proper `--update` flow (see `AGENTS.md`).

## 5. Protected Vercel preview (team review)

Every push to `main` publishes automatically (DEC-007).

- Real content (Vercel login): https://waypoint-git-main-mollypartys-projects.vercel.app
- Public production domains serve a placeholder only. Do not put confidential research on unprotected production.
- Landing page links the dashboard and graph explorer.

## 6. Where things live

| Path | Purpose |
|------|---------|
| `vault/00-START-HERE.md` | Current state |
| `research/00-PROGRESS.md` | Phase progress catalog |
| `research/00-RESEARCH-PLAYBOOK.md` | Research standards and phase specs |
| `research/01-market/` … `08-blueprint/` | Phase folders (each has `_index.md`) |
| `dashboard/` | HTML research dashboard |
| `graph/` | Interactive knowledge graph UI |
| `vault/02-Decisions/` | Decision records |
| `AGENTS.md` / `CLAUDE.md` | Agent protocol |
| `docs/VERSIONING.md` | Versioning strategy |

## 7. How to contribute

1. Prefer short-lived branches (`feat/`, `fix/`, `docs/`, `chore/`) when the change is large; small continuous pushes to `main` are the norm for this early stage (DEC-004).
2. Conventional Commits + attribution footer (see [docs/VERSIONING.md](docs/VERSIONING.md)).
3. After meaningful work: update START-HERE and `research/00-PROGRESS.md` if status moved, then commit and push so partners and other tools always see current `main`.
4. Claudio reviews research via the dashboard, not raw markdown walls.
