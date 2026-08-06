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

None. Six are staged for Claudio on the dashboard: price, free/paid boundary breadth, the analytics identity fix, re-basing PRD G3/G4, the beachhead metro, and which date is the real public launch.

## Corrections to Phase 5 that this phase surfaced

1. PRD goals G3 and G4 need re-basing; G4's 25 percent day-30 install-level retention sits far outside the category's top decile.
2. `05-product/api-integration-map.md` names TelemetryDeck for analytics, and TelemetryDeck deliberately provides no stable per-user identifier, so it structurally cannot deliver the cohort retention the PRD's own goals require.
3. The month-1 safety-data buildability spike should be treated as a **go-to-market gate**, not merely a technical one, because the beachhead metro choice depends on its result.

## Open threads

- Six Phase 6 gate decisions. #open
- A1, the riskiest assumption in the program: whether the beachhead metro clears the OpenStreetMap pedestrian-data floor. #open-question
- Whether a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores. A 30-minute check that prevents a launch-week surprise. #open-question
- Organic cost per subscriber excludes founder time, which must be disclosed alongside any ratio shown to an investor. #open

## Next steps for the next agent (any tool)

1. If Claudio has answered the six cards: record the DECs (DEC-011 onward), apply the two Phase 5 corrections above, update the PRD and API integration map, then tag v0.3.0 with a CHANGELOG entry.
2. Then Phase 7 formal close (dashboard and Vercel packaging polish), then Phase 8 (the investor blueprint).

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] `research/00-PROGRESS.md` current and agreeing with START-HERE
- [x] Graph updated
- [x] Committed and pushed
