---
type: session
created: 2026-08-06
updated: 2026-08-06
tags: [session, research, phase-6, business-model, pricing, gtm, metrics]
---

# Session 2026-08-06 - Phase 6: business model and go-to-market

## Goal

With the Phase 5 gate closed, run Phase 6 end to end: revenue model, unit economics, metrics, go-to-market, and the integrating business model canvas. Then stage the gate for Claudio.

## What was done

- Four parallel research studies produced `revenue-model.md`, `unit-economics.md`, `metrics.md`, and `gtm-plan.md` in `research/06-business-model/`. Each was told explicitly not to run git commands, which avoided the coordination problem from the Phase 5 round-2 batch.
- Wrote `business-model-canvas.md` as the integrating document: all nine blocks, plus a reconciliation section covering where the four studies agree, where they conflict, and what the founder must decide as a result.
- Dashboard: new Phase 6 section with the money in four numbers, the revenue model, GTM, metrics, and six gate cards. Navigation, phase track, document counts, and the sources table all updated.
- Catalogs synced: `research/00-PROGRESS.md`, `research/06-business-model/_index.md`, [[00-START-HERE]], [[Business Model and GTM Key Findings (Phase 6)]], [[_Knowledge-Index]].

## The finding that governs the phase

**Unit economics are a function of distribution, not pricing.** Paid acquisition costs roughly $160 per subscriber against $86 to $107 of lifetime value, so it returns 53 to 70 cents on the dollar at every credible price. The model clears 3:1 only at roughly 84 percent organic acquisition at the recommended $99.99 price. The GTM plan independently rejects paid acquisition pre-funding for unrelated reasons (a bought install before month 10 has zero lifetime value and contaminates the retention signal), so the two agree, but the dependency is permanent.

## Reconciliation work worth remembering

- The economics headline of "90 percent organic" was calculated at a $7.99 mid price. At the recommended $99.99, lifetime value rises to $107 and the requirement falls to about 84 percent. Pricing and distribution are coupled, and the coupling is favorable.
- **Three conversion figures use three different denominators** (installs at paywall date, week-4-retained users, free active users) and must never be quoted side by side to an investor. Caught and documented in canvas section 10.2.
- The revenue model plans on ~30 percent first-year annual renewal against the economics model's 36 percent verified base, so the revenue side is the more conservative of the two. No fix needed, but worth knowing.

## Decisions made

The gate closed in the same session. Claudio answered all six cards; five followed the recommendation and one did not.

- [[DEC-011 Pricing and the permanent free tier]]: $99.99/yr, $12.99/mo, 21-day annual-only trial, Founding Runner $69.99/yr price-preserved. The generous free boundary approved and the escape hatch explicitly declined, so the coaching layer alone is paid and the free tier gets named publicly at launch.
- [[DEC-012 Measurement corrections analytics identity and re-based targets]]: cohort retention moves to a first-party Postgres event table on the existing account identifier; PRD G3 and G4 re-based to activated-cohort definitions; activation redefined as a completed recorded run.
- [[DEC-013 Home-metro beachhead and iOS-first public launch]]: home metro subject to the month-1 spike, and **the iOS date carries the public launch**.

### On the launch override

The go-to-market plan argued for Android as the public launch, and its reasoning was sound: mixed-platform run clubs, and four to eight quiet weeks of route-quality burn-in. Claudio chose iOS. Three things support that: the Apple featuring nomination is iOS-only and cannot be spent on an Android launch (which the plan underweighted), speed matters in a 12 to 18 month window the build already consumes ten months of, and iOS carries roughly 85 percent of category subscription revenue.

The honest cost is losing the burn-in, which was absorbing three real risks, so DEC-013 converts each into a commitment rather than leaving it implicit: the month-8 beta cohort target becomes a hard gate on the launch date, reviews are seeded from that cohort behind a 99.5 percent crash-free release gate, Android waitlist capture starts at launch, and the featuring nomination is filed at month 6 to 7. Recording the conditions was the point; an override without them would have quietly deleted the mitigations along with the recommendation.

## Corrections to Phase 5 that this phase surfaced, and applied

1. PRD goals G3 and G4 re-based; G4's 25 percent day-30 install-level retention sat far outside the category's top decile. Assumption A1 partly resolved.
2. `05-product/api-integration-map.md` named TelemetryDeck for analytics, and TelemetryDeck deliberately provides no stable per-user identifier, so it structurally cannot deliver cohort retention. Section 6.2 now carries the split. While in the file, the stale Supabase references left over from DEC-009 were also cleared: section 4.2, the master integration table, and the critical path.

## Open threads

- A1, the riskiest assumption in the program: whether the home metro clears the OpenStreetMap pedestrian-data floor. Now a go-to-market gate. #open-question
- The month-8 beta cohort is a hard gate on the launch date, a direct consequence of the override. #open
- The paid product rests entirely on one job, with no v1.x fallback if training-state-aware generation is not felt value. #risk
- Whether a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores. #open-question
- Organic cost per subscriber excludes founder time, which must be disclosed alongside any ratio shown to an investor. #open

## Phases 7 and 8, same session

Both remaining phases were completed in this same working session, but their record now lives in its own note so it can be found by filename: [[2026-08-06 Phase 7 Dashboard Closed and Phase 8 Blueprint Drafted]].

## Next steps for the next agent (any tool)

Superseded. The founding team was defined as three partners later the same day, which opened Phase 9 and put blueprint approval behind it. Current next steps live in [[2026-08-06 Phase 9 Financial Strategy and Founding Team]] and `research/00-PROGRESS.md`.

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] `research/00-PROGRESS.md` current and agreeing with START-HERE
- [x] Graph updated
- [x] Committed and pushed
