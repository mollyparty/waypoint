---
type: session
created: 2026-07-30
updated: 2026-08-06
tags: [session, infrastructure, vercel]
---

# Session 2026-07-30 - Vercel Publishing Pipeline

> Retrofitted to the session template on 2026-08-06. Content is unchanged; it was originally written with ad-hoc headings and no `updated:` field.

## Goal

Publish every HTML artifact automatically to Vercel from the GitHub repo, so the partner always has a current URL, without ever exposing confidential pre-launch research publicly.

## What was done

- Created Vercel project `waypoint` under team `mollypartys-projects` and connected it directly to `mollyparty/waypoint` on GitHub. Every push now publishes automatically; GitHub remains the single source of truth.
- Enabled Standard Protection (Vercel Authentication) on all previews and production deployment URLs. The Hobby plan cannot protect the production domain, so Claudio chose the protected-previews approach (see [[DEC-007 Vercel publishing pipeline with protected previews]]).
- Created orphan branch `vercel-production-locked` with a placeholder page and pointed the production branch at it. Public production domains serve only the placeholder.
- Added a root `index.html` landing page on `main` linking the knowledge graph, with cards reserved for the Phase 7 dashboard and Phase 8 blueprint.
- Incident handled: Vercel auto-deployed `main` to production the moment git was connected, before the branch switch, briefly exposing the repo publicly. Promoted the placeholder over it and deleted the confidential deployment. Verified: production 200 placeholder, main preview 302 to login.

## Decisions made

- [[DEC-007 Vercel publishing pipeline with protected previews]]

## Access

- Real content (login required): https://waypoint-git-main-mollypartys-projects.vercel.app
- Public placeholder: https://waypoint-khaki.vercel.app

## Open threads

- Phase 8 investor-facing blueprint should be a separate public Vercel project; this one stays private. **Still open** as of 2026-08-06: the blueprint shipped into this protected project, and the separate public deployment is an open item in `research/08-blueprint/_index.md`. #open-question

## Next steps

1. ~~Add DEC-007 to the knowledge graph on the next scheduled run~~ deferred at the time to avoid colliding with the research session's pipeline, then forgotten. **Done 2026-08-06** during the memory audit remediation.

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] Graph updated if docs changed (DEC-007 node added 2026-08-06, later than it should have been)
- [x] Committed with attribution footer and pushed to GitHub
