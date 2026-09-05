---
type: session
created: 2026-09-05
updated: 2026-09-05
tags: [session, memory, audit, codex]
---

# Codex Memory and Sync Audit

## Goal

Verify whether Waypoint changes automatically reach GitHub and become Obsidian memory after moving from Cursor to Codex. Assess improvements for Astra orchestration.

## Verified findings

- Origin is https://github.com/mollyparty/waypoint.git. At audit start, local HEAD and live remote main both resolved to `6cd0d0c041a613ec579a6a5d37c8d5ea018b3e65`. `git push --dry-run origin main` succeeded. This verifies access and current committed history, not continuous automatic pushes.
- The Obsidian application registry points to this project's `vault/`. Its core `sync` plugin is enabled in `vault/.obsidian/core-plugins.json`. No Obsidian process was found. Remote Obsidian Sync account pairing and transfer health were not established by these settings.
- No community plugin directory or Obsidian Git plugin configuration was found in this vault. No Waypoint/Obsidian/Graphify named Windows scheduled task or Codex automation directory was found. These scoped checks cannot rule out arbitrarily named third-party automation.
- The Git hooks contain Graphify rebuilding, not Git pushing or semantic session-note generation. The memory protocol in AGENTS.md requires agents to write notes and commit/push; it is a behavioral workflow rather than a background sync service.
- `post-commit` skips docs and catalog/scripts/tools. `post-checkout` still runs a full code rebuild on branch switches without that scope filter. Both hooks are local and untracked, so their setup does not travel with a clone.
- Actual graph: 236 nodes, 570 links, 14 distinct community values. The older 227/542/15 handoff claim is stale. Node count does not prove document coverage or semantic accuracy. Stale labels include `gate_phase6_open`, `capital_requirement_derived`, and `product_ai_running_coach`.
- `python catalog/build.py --check` passes for 70 entries. Inspection shows that it returns before rendering/comparing generated outputs, so passing it does not establish that FEATURES.md or blueprint section 05 matches the catalog.
- The last recorded session was August 30. The September 5 orientation response had no durable session note. This audit captures the migration findings now.
- Two pre-existing modified files are outside this audit: `vault/.obsidian/graph.json` and `vault/04-Knowledge/Competitive Landscape Key Findings (Phase 2).md`. They are not included in this audit commit.

## Recommended foundation, pending implementation

1. Add a repository-owned memory-health check: detect missing checkpoints, stale source hashes, invalid links, unresolved contradictions, stale generated outputs, and local commits not on the remote. Expose distinct saved-local, committed, pushed, and indexed states.
2. Replace machine-only hook assumptions with versioned scripts and an explicit installer. Prevent both commit and checkout hooks from discarding curated semantic graph data. Keep application AST indexing separate from document memory.
3. Give Astra a durable current-work checkpoint containing objective, approved scope, active task, changed files, evidence/check results, blockers, and exact next action. Update after meaningful units and before handoff or context compaction. Retain concise session history separately.
4. For delegated work, use bounded context and structured completion records containing sources, changes, tests, proposed decisions, and unresolved issues. Astra reviews and integrates them into canonical memory. Delegated suggestions do not become founder approvals.
5. Maintain source/version/status metadata for graph facts, explicitly mark superseded facts, and validate source freshness before relying on retrieval. Incremental re-extraction should follow changed source hashes. Recheck targeted contradictions before declaring memory healthy.
6. Implement a scoped checkpoint-and-push command with explicit file selection, attribution, validation, push failure reporting, and live remote verification. Avoid indiscriminate save-triggered staging of confidential or unfinished material.
7. Add a compact HTML memory-health view to the existing dashboard: last checkpoint, last verified push, graph freshness, open decisions, current objective, and next action. Retain the vault and repository as the durable store across models and IDEs.

## Decisions and current project state

No new business decisions or phase approvals. Phase 9's six founder decisions remain open; blueprint approval and v0.4.0 remain pending. Recommendations above are an implementation backlog, not installed automation. A stronger orchestrator does not itself provide durable storage or guarantee zero forgetting.

## Follow-up

First implement the memory-health check and portable safe hooks, then repair semantic graph drift and introduce checked checkpoints. Graph semantic refresh remains pending for this audit too; do not describe the graph as current until reconciled. Read this note directly from START-HERE in the interim.

## Evidence

Local inspection: `.git/hooks/post-commit`, `.git/hooks/post-checkout`, `vault/.obsidian/`, `graphify-out/graph.json`, `catalog/build.py`, Windows process/task listings, live `git ls-remote`, and push dry-run. No Obsidian Sync remote UI or end-to-end automatic-sync test was performed.

Related: [[00-START-HERE]], [[DEC-002 Obsidian vault as project memory]], [[2026-08-30 Features Catalog Inside the Blueprint]].
