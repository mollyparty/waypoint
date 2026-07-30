---
type: decision
id: DEC-001
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision]
---

# DEC-001 Trunk-based versioning on main

## Context

Waypoint needs full version history of everything produced, while always displaying the latest approved version. Multiple tools and machines may touch the repo, so the model must be simple and unambiguous.

## Decision

Trunk-based development: `main` is always the latest approved version. Work happens on short-lived `feat/`, `fix/`, `docs/` branches merged into `main`. Approved milestones get semantic version tags (`v0.x.y`) plus a `CHANGELOG.md` entry. Conventional Commits with an attribution footer on every commit. Push at every milestone and session end.

## Rationale

- One branch to trust: anyone opening `main` sees the current truth, which directly satisfies the "latest approved version" requirement.
- Lower overhead than GitFlow for a solo founder; no long-lived develop branch to drift.
- Tags plus changelog give named, auditable milestones without ceremony.

## Alternatives considered

- **GitFlow**: rejected; develop/release branch overhead adds friction with no benefit at this scale.
- **Main-only, commit direct**: rejected; branches give a cheap review point before something becomes "approved".

## Consequences

- Branches must stay short-lived (hours to days) or they defeat the model.
- Full strategy documented in `docs/VERSIONING.md`.

## Amendment (2026-07-30)

Push cadence amended by [[DEC-004 Continuous push and cross-IDE agent files]]: push continuously (after every meaningful unit of work), not only at session end. Everything else in this decision stands.

## Related

- [[_Decision-Log]]
- [[DEC-004 Continuous push and cross-IDE agent files]]
