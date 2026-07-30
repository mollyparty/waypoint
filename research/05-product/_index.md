# Phase 5: Product definition and MVP scope

> Version-Timestamp: 2026-07-30 21:05:00 UTC-4

**Status: IN PROGRESS.** Deliverables drafted. Gate **partially passed** (DEC-008). Stack and platform decisions still open. Distilled in vault: `vault/04-Knowledge/Product Definition Key Findings (Phase 5).md`. Program catalog: `../00-PROGRESS.md`.

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
| `database-deep-dive.md` | Round 2: security-first DB alternatives beyond Supabase | **MISSING** (agent failed: API limit; relaunch) |
| `dual-platform-strategy.md` | Round 2: iOS + Android MVP options and cost to the window | **MISSING** (agent failed: API limit; relaunch) |
| `api-integration-map.md` | Round 2: every external API for launch features (both platforms) | **MISSING** (agent failed: API limit; relaunch) |

## Gate status (DEC-008)

| Decision | Outcome |
|----------|---------|
| MVP scope as drawn | **Approved** |
| Free/paid line | **Launch v1 entirely free**; safety routing free permanently |
| Apple Watch | **Fast-follow** at launch+30 |
| Stack | **Held** for validation; round 1 done; round 2 required before approval |
| Platform | **New requirement:** MVP on both iOS and Android (pending strategy doc + founder DEC) |

## Do not start Phase 6 until

1. Round 2 files exist and are reviewed on the dashboard.
2. Claudio approves stack (with or without revisions).
3. Claudio chooses a dual-platform option; if it changes effort or client stack, record a new DEC and update MVP scope numbers.
