# Working on Waypoint

> Version-Timestamp: 2026-07-30 13:20:00 UTC-4

This project is designed to be picked up from any machine, by any collaborator, using any AI coding tool. This is how.

## 1. Clone the repo

```bash
git clone https://github.com/mollyparty/waypoint.git
cd waypoint
```

Set your own git identity if you have not already (each collaborator uses their own name/email, not a shared one):

```bash
git config user.name "Your Name"
git config user.email "you@example.com"
```

## 2. Pick any AI coding tool - they all read the same instructions

| Tool | What it reads |
|------|----------------|
| Cursor | `AGENTS.md` + `.cursor/rules/memory-protocol.mdc` |
| Codex CLI / ChatGPT | `AGENTS.md` |
| Claude Code | `CLAUDE.md` (a short pointer to `AGENTS.md`) |
| Anything else | `AGENTS.md` - it is plain markdown, tool-agnostic |

**Always read [AGENTS.md](AGENTS.md) first, in full**, before doing any work. It is the single source of truth for how this project maintains memory, versioning, and quality across sessions and tools.

## 3. Open the Obsidian vault (optional but recommended)

The `vault/` folder is a full Obsidian vault: decisions, sessions, knowledge, and project state. Open Obsidian, choose "Open folder as vault," and select `vault/` inside this repo. Read `vault/00-START-HERE.md` first - it always reflects the current state of the project.

You do not need Obsidian to read or edit vault notes; they are plain markdown and readable in any editor. Obsidian just adds graph view, backlinks, and templates.

## 4. Graphify (the project's knowledge graph)

Graphify turns the whole repo into a queryable knowledge graph so nobody has to re-read everything to get context.

```bash
pip install graphifyy
```

Query it instead of re-reading files: `graphify query "<question>" --budget 2000`. Outputs live in `graphify-out/` (`graph.json`, `GRAPH_REPORT.md`, `graph.html` - open the HTML file in a browser for a visual map). A git post-commit hook keeps the graph current automatically for code changes; see `AGENTS.md` for the doc-update step.

## 5. How to contribute

1. Branch from `main`: `feat/`, `fix/`, `docs/`, or `chore/` prefix.
2. Make focused changes; commit with [Conventional Commits](https://www.conventionalcommits.org/) messages and the attribution footer described in [docs/VERSIONING.md](docs/VERSIONING.md).
3. Push continuously, not just when "done" - `main` should always be current for whoever else is working on this.
4. Merge back to `main` quickly. Full strategy: [docs/VERSIONING.md](docs/VERSIONING.md).

## 6. Where things live

- `vault/00-START-HERE.md` - current project state, read this first.
- `vault/02-Decisions/` - why things are the way they are.
- `AGENTS.md` / `CLAUDE.md` - the agent protocol (memory, versioning, engineering standards).
- `docs/VERSIONING.md` - the full versioning strategy.
- `graphify-out/` - the knowledge graph and its outputs.
