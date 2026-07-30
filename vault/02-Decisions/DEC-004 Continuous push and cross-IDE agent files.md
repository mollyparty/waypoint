---
type: decision
id: DEC-004
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, versioning, memory]
---

# DEC-004 Continuous push and cross-IDE agent files

## Context

Two new requirements surfaced once a second collaborator (Claudio's partner) entered the picture: (1) GitHub must always reflect current work, not just work committed at the end of a session, so a partner can pull at any moment and see the latest; (2) the project must be fully usable from any AI coding tool (Cursor, Codex CLI/ChatGPT, Claude Code, or others), on any machine, not only inside this Cursor workspace.

## Decision

1. **Continuous push.** Amends the cadence set in [[DEC-001 Trunk-based versioning on main]]: commit and push after every meaningful unit of work (a completed todo, a coherent file group), not only at session end. `main` should be current at essentially any point in time, not just when a session wraps up.
2. **Cross-IDE agent files.** `AGENTS.md` remains the single canonical protocol, genericized so it applies to any tool. `CLAUDE.md` is added as a short, non-duplicated pointer to `AGENTS.md`, because Claude Code looks for that filename by convention. `CONTRIBUTING.md` is added as the human-facing onboarding doc for a collaborator joining from any machine or tool.
3. **Cross-platform repo hygiene.** `.gitattributes` normalizes line endings (`eol=lf`) so the repo is byte-identical on Windows, macOS, and Linux, avoiding spurious diffs between collaborators on different operating systems.

## Rationale

- A symlink from `CLAUDE.md` to `AGENTS.md` was considered but rejected: `core.symlinks` is disabled on this machine (common on Windows without developer mode), so a symlink would be stored as an unusable plain-text path reference instead of a working link. A real short pointer file works identically everywhere, at the cost of one file to keep in sync (low risk since it is intentionally almost empty).
- Duplicating agent instructions per tool was rejected: it guarantees drift. One canonical file plus thin pointers is the maintainable version of the "reference, don't embed" principle.
- Continuous push has an overhead cost (more, smaller commits) but directly serves the stated goal: a partner must never be blocked on waiting for a session to "finish."

## Alternatives considered

- **Keep push cadence at session-end only**: rejected, does not meet the collaborator's need for near-real-time visibility.
- **Separate, tool-specific instruction files with full content in each**: rejected, drift risk.
- **Symlink CLAUDE.md -> AGENTS.md**: rejected on this machine due to `core.symlinks=false`; revisit if a collaborator's environment supports it, but the thin-file approach works everywhere regardless.

## Consequences

- More frequent, smaller commits appear in history; this is intentional, not noise.
- `CLAUDE.md` must be checked whenever `AGENTS.md`'s scope changes, to confirm the pointer framing still holds (it rarely needs edits itself).
- `.gitattributes` renormalization was a one-time repo-wide line-ending pass; already applied.

## Related

- [[_Decision-Log]]
- [[DEC-001 Trunk-based versioning on main]]
