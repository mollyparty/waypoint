# Phase 5: Product definition and MVP scope

> Version-Timestamp: 2026-08-06 11:40:00 UTC-4

**Status: COMPLETE. Gate passed.** All deliverables written including the three round-2 studies; all five gate decisions closed (DEC-008 on 2026-07-30; DEC-009 and DEC-010 on 2026-08-06). Distilled in vault: `vault/04-Knowledge/Product Definition Key Findings (Phase 5).md`. Program catalog: `../00-PROGRESS.md`.

Governed by the locked concept (`../04-synthesis/concept.md`, DEC-006), whose client stack is amended by DEC-010 (React Native + MapLibre, dual-platform).

## Deliverables

| File | Contents | Status |
|------|----------|--------|
| `prd.md` | Product requirements, constraints, compliance as requirements | complete |
| `rice-prioritization.md` | RICE scoring of ~30 candidate features | complete |
| `mvp-scope.md` | 15-feature MVP line, effort, walking skeleton, gate cards | complete (scope approved; effort may change with Android) |
| `user-journeys.md` | Five journeys, ten design principles | complete |
| `stack-recommendation.md` | Initial stack (GraphHopper, Supabase, SwiftUI, etc.) | complete |
| `stack-validation.md` | Round 1 second opinion: no layer revised; conditions named | complete |
| `database-deep-dive.md` | Round 2: 12-candidate DB scoring; verdict: replace Supabase with Aiven (EU) + self-managed PostGIS + decoupled auth (Better Auth) | complete |
| `dual-platform-strategy.md` | Round 2: four options costed; recommends Option D, staged React Native (iOS month 9-10, Android +4-8 weeks, ~29-31 pm) | complete |
| `api-integration-map.md` | Round 2: ~20 required integrations across 7 domains (30 cataloged); ~$80-130/mo at MVP; 6 gate the walking skeleton | complete |

## Gate status (DEC-008)

| Decision | Outcome |
|----------|---------|
| MVP scope as drawn | **Approved** |
| Free/paid line | **Launch v1 entirely free**; safety routing free permanently |
| Apple Watch | **Fast-follow** at launch+30 |
| Stack | **Approved as revised** (DEC-009): Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on Hetzner for the moat, auth decoupled via Better Auth. Supabase dropped. Carries an explicit revisit clause |
| Platform | **Option D approved** (DEC-010): one React Native codebase, MapLibre both platforms, iOS month 9-10, Android 4-8 weeks later, ~29-31 person-months |

## Amendments this gate produced

- `mvp-scope.md` section 7: effort ~25 → **~29 to 31 person-months**; calendar now iOS month 9-10, Android month 10-12; Android long-lead paperwork added at month 1.
- Charter: client stack is React Native + MapLibre, dual-platform; Android removed from the expansion narrative.
- `api-integration-map.md` section 4 predates DEC-009 and still names Supabase Auth; read it as "the auth layer" (Better Auth).

## Phase 6 is now unblocked

Business model, unit economics, metrics, and GTM proceed in `../06-business-model/`, using the DEC-009 cost lines and the DEC-010 launch calendar.
