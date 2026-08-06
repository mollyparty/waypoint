---
type: index
created: 2026-07-30
updated: 2026-08-06
tags: [architecture, index]
---

# Architecture Index

Technical design notes: system architecture, data models, stack choices, integration diagrams.

**Nothing here yet, and that is expected.** No application code exists. This folder fills once the build starts, beginning with the walking skeleton.

## The stack is already decided

Do not re-litigate these here. They are decisions, and changing them requires a superseding decision record.

- [[DEC-009 Revised data layer Aiven split architecture with decoupled auth]] - Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on Hetzner for the geospatial moat, Better Auth decoupled into Waypoint's own API layer. Supabase dropped. **Carries a deliberate revisit clause** at four named checkpoints, the first of which is "before the walking skeleton", so the first architecture note written here should open by re-testing it.
- [[DEC-010 Staged cross-platform MVP on React Native]] - one React Native codebase, MapLibre on both platforms.

Supporting research: `research/05-product/stack-recommendation.md`, `stack-validation.md`, `database-deep-dive.md`, `dual-platform-strategy.md`, and `api-integration-map.md` for the roughly twenty external integrations.

## What belongs here when the build starts

- System architecture and service boundaries
- Data model and the personal-data / geospatial split, including what crosses between the two databases
- The routing pipeline (GraphHopper, OpenStreetMap ingestion, crossing penalties)
- Integration diagrams and failure modes for the external APIs
- Any superseding stack decision that comes out of the DEC-009 revisit
