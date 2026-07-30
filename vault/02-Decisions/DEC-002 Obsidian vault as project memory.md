---
type: decision
id: DEC-002
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, memory]
---

# DEC-002 Obsidian vault as project memory

## Context

AI agent sessions have no memory between conversations (amnesia). Waypoint needs a persistent, structured, human-and-agent-readable memory so every session starts with full project context without expensively re-reading everything.

## Decision

An Obsidian vault lives at `vault/` inside the repo, committed to git. `00-START-HERE.md` is the single always-current entry point, updated every session. Decisions, sessions, and knowledge each get their own folder with templates. Stable `.obsidian/` settings are committed; volatile workspace cache is gitignored.

## Rationale

- Plain markdown: readable by agents, humans, git diff, and Graphify extraction alike. No lock-in.
- Wikilinks and tags give Obsidian graph view for humans and rich edges for the knowledge graph.
- Living inside the repo means memory is versioned and travels with the project to any machine.
- One entry point (START-HERE) keeps session-start token cost near-constant regardless of project size.

## Alternatives considered

- **External notes app or wiki**: rejected; memory outside the repo is memory that gets stale and lost.
- **Single flat NOTES.md**: rejected; does not scale, and one giant file is expensive to read per session.

## Consequences

- The session-end update routine is mandatory; a stale START-HERE is worse than none.
- Note frontmatter (`updated:` field) serves as the Version-Timestamp for vault artifacts.

## Related

- [[_Decision-Log]]
- [[DEC-003 Graphify as queryable project brain]]
