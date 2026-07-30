# Phase 5: Product definition and MVP scope

> Version-Timestamp: 2026-07-30 22:30:00 UTC-4

**Status: IN PROGRESS.** All deliverables written, including the three round-2 studies. Gate **partially passed** (DEC-008). **Awaiting founder decisions on the revised stack and the platform strategy** (evidence on the dashboard, cards 8 and 9). Distilled in vault: `vault/04-Knowledge/Product Definition Key Findings (Phase 5).md`. Program catalog: `../00-PROGRESS.md`.

Governed by the locked concept (`../04-synthesis/concept.md`, DEC-006), subject to amendment if dual-platform MVP is adopted.

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
| Stack | **Held**; round 2 complete and it revises the recommendation (Aiven split architecture replaces Supabase; auth decoupled). Awaiting founder approval (dashboard card 8) |
| Platform | Round 2 strategy complete; recommends staged React Native (Option D), which amends the DEC-006 client stack. Awaiting founder choice (dashboard card 9) |

## Do not start Phase 6 until

1. ~~Round 2 files exist and are reviewed on the dashboard.~~ Done: all three written and digested on the dashboard.
2. Claudio approves the revised stack (dashboard card 8).
3. Claudio chooses a platform option (dashboard card 9); the choice needs a new DEC and, under Option C or D, updated MVP effort numbers.
