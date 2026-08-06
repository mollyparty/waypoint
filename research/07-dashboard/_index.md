# Phase 7: HTML research dashboard

> Version-Timestamp: 2026-08-06 13:45:00 UTC-4

**Status: COMPLETE.** Built early at Claudio's request during Phases 4 and 5, and closed out on 2026-08-06 once the Phase 6 section landed. Program catalog: `../00-PROGRESS.md`.

## Deliverables

- [x] `dashboard/index.html` - single-file research dashboard covering Phases 0 through 6, with every gate card and its outcome
- [x] `graph/index.html` - interactive knowledge graph explorer (search, clusters, node detail)
- [x] Root `index.html` - landing page linking the live artifacts
- [x] GitHub to Vercel auto-publish with protected previews ([[DEC-007 Vercel publishing pipeline with protected previews]])
- [x] Phase 6 section wired in with the six gate decisions and their outcomes
- [x] HTML structure validated (no unclosed or mismatched tags)

## Access

- Protected preview: https://waypoint-git-main-mollypartys-projects.vercel.app (Vercel login required)
- Local: open `dashboard/index.html` directly, or serve the repo root over HTTP

## What this phase established

Markdown remains the citable source of truth; the dashboard is the readable window into it. That split is now a standing rule in `../00-RESEARCH-PLAYBOOK.md`: gate reviews happen on the dashboard, not on walls of markdown. Every phase gate from 4 onward was actually decided this way, which is the evidence the surface works.

## Note

The playbook originally placed this phase after the business model. Claudio required a readable HTML surface earlier, so it was pulled forward and grown incrementally with each phase. Phase 8's investor blueprint is a separate, externally-facing artifact with a different audience and a different standard of polish.
