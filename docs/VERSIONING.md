# Versioning Strategy

> Version-Timestamp: 2026-07-30 12:15:00 UTC-4

This document defines how Waypoint tracks versions. The goal: full history of everything, while `main` always shows the latest approved version.

## Model: trunk-based development

```
main  ─●───────●───────●──────●──▶   (always the latest APPROVED version)
        \     /  \    /      /
         feat/x   docs/y  fix/z      (short-lived work branches)

tags:  v0.1.0          v0.2.0        (approved milestones)
```

### Rules

1. **`main` is sacred.** It always represents the latest approved state of the project. Anyone (human or agent) opening the repo at `main` sees the current truth.
2. **Work happens on short-lived branches.** Prefix by intent: `feat/`, `fix/`, `docs/`, `chore/`. Branch from `main`, merge back to `main` quickly (hours to days, not weeks).
3. **Approved milestones get semantic version tags.** `vMAJOR.MINOR.PATCH`:
   - MAJOR: breaking or directional change (product pivot, architecture replacement).
   - MINOR: new capability, phase, or significant content addition.
   - PATCH: fixes and small corrections.
   - Pre-1.0 (`v0.x.y`) signals the project is still forming.
4. **Every tag gets a `CHANGELOG.md` entry** in Keep a Changelog format, written when the tag is created, not after.
5. **Push continuously, not just at session end.** Every meaningful unit of work (a completed todo, a coherent group of file changes, a milestone) gets committed and pushed to `origin/main` before moving on. Local-only history does not exist as far as this project is concerned. A human collaborator may pull `main` at any time and must see current work.

## Commit convention

Commits follow [Conventional Commits](https://www.conventionalcommits.org/): `type(scope): summary`.

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`.

Every commit carries an attribution footer so history is traceable across machines and tools:

```
Agent-Attribution: computer=<hostname>; tool=<tool>; version=<tool version>; timestamp=<YYYY-MM-DD HH:mm:ss TZ>
```

Values are read from the real environment. If a value cannot be determined, it is written as `unknown`, never omitted.

## Versioned artifacts

Every versioned artifact (docs, decks, scripts, configs, reports) carries a visible `Version-Timestamp: YYYY-MM-DD HH:mm:ss TZ` in a header or metadata block. Vault notes use an `updated:` field in YAML frontmatter instead, which serves the same purpose.

## "Latest approved version" in practice

- **Code and docs:** whatever is on `main`.
- **Releases:** the highest semver tag; see `CHANGELOG.md` for what it contains.
- **Project memory:** `vault/00-START-HERE.md` on `main` is the latest approved snapshot of project state.
