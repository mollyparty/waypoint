---
type: decision
id: DEC-007
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, infrastructure, vercel, security]
---

# DEC-007 Vercel publishing pipeline with protected previews

## Context

Claudio wants every HTML artifact (knowledge graph, research dashboard, blueprint site) published automatically to Vercel as it is created, with the GitHub repo (`mollyparty/waypoint`) as the single source of truth and Vercel connected directly to it. The repo contains confidential pre-launch research, so nothing may be publicly readable. The account is on the free Hobby plan, which cannot put Vercel Authentication on the production domain.

## Decision

1. **Git-connected Vercel project.** Project `waypoint` (team `mollypartys-projects`, id `prj_1lbIwFOqmPQ878r2BpFuYmivQllT`) is connected to the GitHub repo. No build step; the repo root is served as a static site. Every push publishes automatically.
2. **Protected previews carry the real content.** Standard Protection (Vercel Authentication) is enabled for all previews and production deployment URLs. The production branch is pointed at `vercel-production-locked`, an orphan branch containing only a harmless placeholder page. Pushes to `main` therefore produce protected preview deployments only.
3. **Stable access URL.** The team views the real content at `https://waypoint-git-main-mollypartys-projects.vercel.app` after logging into Vercel. The public production domains (`waypoint-khaki.vercel.app`, `waypoint-mollypartys-projects.vercel.app`) serve only the placeholder.
4. **Landing page.** A root `index.html` on `main` acts as the front door, linking the knowledge graph now and the Phase 7 dashboard and Phase 8 blueprint when they exist.

## Rationale

- Chosen by Claudio over (a) a curated public production site via `.vercelignore` and (b) upgrading to Vercel Pro. This option is free, fully confidential, and still auto-publishes on every push.
- During setup Vercel auto-deployed `main` to production before the branch switch, briefly exposing the repo on the production domain. The placeholder was promoted over it and the confidential deployment was deleted. Verified afterwards: production serves the placeholder (HTTP 200), `main` previews redirect to Vercel login (HTTP 302).

## Consequences

- Viewing any real artifact requires a Vercel login (owner or invited team member). Investor-facing material in Phase 8 should ship as a separate public Vercel project, not this one.
- `vercel-production-locked` is a permanent orphan branch; do not delete it and do not merge it with `main`.
- `.vercel/` and `.env*` stay gitignored (CLI credentials and OIDC tokens).
- If the account ever upgrades to Pro, production can be re-pointed to `main` with full Vercel Authentication instead.

## Related

- [[_Decision-Log]]
- [[DEC-005 Phased research program with gated approvals]]
