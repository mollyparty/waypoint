---
type: session
created: 2026-07-30
tags: [session, infrastructure, vercel]
---

# 2026-07-30 Vercel Publishing Pipeline

## What happened

- Created Vercel project `waypoint` under team `mollypartys-projects` and connected it directly to `mollyparty/waypoint` on GitHub. Every push now publishes automatically; GitHub remains the single source of truth.
- Enabled Standard Protection (Vercel Authentication) on all previews and production deployment URLs. The Hobby plan cannot protect the production domain, so Claudio chose the protected-previews approach (see [[DEC-007 Vercel publishing pipeline with protected previews]]).
- Created orphan branch `vercel-production-locked` with a placeholder page and pointed the production branch at it. Public production domains serve only the placeholder.
- Added a root `index.html` landing page on `main` linking the knowledge graph, with cards reserved for the Phase 7 dashboard and Phase 8 blueprint.
- Incident handled: Vercel auto-deployed `main` to production the moment git was connected, before the branch switch, briefly exposing the repo publicly. Promoted the placeholder over it and deleted the confidential deployment. Verified: production 200 placeholder, main preview 302 to login.

## Access

- Real content (login required): https://waypoint-git-main-mollypartys-projects.vercel.app
- Public placeholder: https://waypoint-khaki.vercel.app

## Notes for future sessions

- Knowledge graph update for DEC-007 deferred to the next scheduled graph run to avoid colliding with the main research session's pipeline.
- Phase 8 investor-facing blueprint should be a separate public Vercel project; this project stays private.
