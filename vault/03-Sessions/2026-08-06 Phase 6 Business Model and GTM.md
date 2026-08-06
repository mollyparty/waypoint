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

With the gate closed, both remaining phases were completed rather than deferred.

**Phase 7 closed.** The dashboard now covers Phases 0 through 6 with every gate card and outcome, its HTML validates with no unclosed or mismatched tags, and the landing page links all three artifacts. The phase index records the standing rule this phase established: gate reviews happen on the dashboard, markdown stays the citable source of truth.

**Phase 8 drafted.** The example blueprint URL that timed out in the planning session fetched successfully on the retry, so the structure follows it: numbered sections, a hero with headline stat cards, a fixed navigator, and — the most valuable borrowing — a dedicated self-audit with known gaps, a 90-day validation sprint, and an explicit go / no-go. The bilingual EN/ES toggle was deliberately not adopted; the example serves a Dominican market and a half-built translation would read worse than none.

Deliverables: `blueprint/blueprint.md` as the citable master and `blueprint/index.html` as the investor-facing site, 17 sections each.

### The editorial call worth recording

The blueprint invents nothing and lets the confidence tags survive into investor-facing text rather than laundering them into false precision. Three findings a weaker document would bury are given emphasis instead: **H5 came back uncertain**, so the route wedge alone is a $5M to $30M business and the venture case is argued from four named expansion paths; **zero user interviews have been conducted**, stated in a callout directly under the hero; and **unit economics depend on distribution rather than pricing**. An investor finds all three in diligence anyway, and finding them there is much worse than reading them on page one.

The capital figure (~$350k to $400k pre-seed) is derived and labeled as such. No decision record covers a raise, so section 13 shows the arithmetic instead of asserting a number.

## Next steps for the next agent (any tool)

1. **Founder review of the blueprint**, then tag v0.4.0. Four open items are listed in `research/08-blueprint/_index.md`.
2. **Then the build begins.** The month-1 A3 safety-data buildability spike is the first task, and it is a go-to-market gate rather than only a technical one.

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] `research/00-PROGRESS.md` current and agreeing with START-HERE
- [x] Graph updated
- [x] Committed and pushed
