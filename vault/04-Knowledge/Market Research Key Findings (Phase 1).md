---
type: knowledge
created: 2026-07-30
updated: 2026-07-30
tags: [knowledge, research, market, phase-1]
---

# Market Research Key Findings (Phase 1)

Distilled from `research/01-market/` (full citations live there). All four deliverables completed 2026-07-30.

## The opportunity signal

- **The route-generation whitespace is verifiable.** Training apps (Runna, TrainAsONE) prescribe workouts with no location intelligence; routing apps (Komoot, Strava routes) plan static routes with no training context. No incumbent generates the run itself, constraint-aware and on demand. The two assets that could fuse it (Runna, Komoot) were acquired by different companies in 2025 (Strava and Bending Spoons respectively).
- **The enabling stack is nearly free**: GraphHopper round-trip routing on OpenStreetMap, free SRTM elevation, WeatherKit free tier, Apple on-device foundation models. The moat must be personalization and execution, not routing algorithms (which are published research).
- **Participation is booming**, led by Gen Z and beginners: global runners 672M to 785M (2022 to 2025, GWI), record London Marathon ballot (1.13M), Strava clubs quadrupled. Caveat: the US "dedicated core" runner segment has softened, which pressures the committed-amateur hypothesis (test in Phase 3).

## The hard numbers (H5 verdict: UNCERTAIN)

- TAM: running app subscriptions roughly $1.3B to $2.9B (2025, low-credibility report mills), cross-checked against observable company revenue of $0.6B to $1.0B; fitness apps overall about $6B.
- SAM: about 14M committed amateur iOS runners (US, UK, EU, Canada, Australia); demonstrated willingness to pay supports roughly $150M to $300M per year.
- SOM (years 3 to 5): 70k to 300k paying subscribers, roughly $5M to $30M ARR, anchored on Runna reaching about 90k payers in 3 years before acquisition.
- Implication: the wedge alone is a strong business and a Runna-style strategic exit; venture scale needs an explicit expansion story (Android, geographies, broader coaching or outdoor navigation surface). This shapes the Phase 8 blueprint narrative.

## Strategic pressures

- **Platform squeeze**: Garmin Connect+ ($6.99/mo) and Apple Workout Buddy commoditize generic AI coaching chat; differentiation must be what they do not do (route generation). Apple's Workout Buddy is motivational only, not prescriptive.
- **Garmin API risk**: new Connect Developer Program applications are paused indefinitely; HealthKit remains fully open, validating iOS-first but making Garmin integration a launch risk.
- **Price umbrella**: between Garmin Connect+ ($70/yr) and Strava+Runna bundle ($150/yr). Health and fitness is the only app category where annual plans dominate (60.6% of revenue, RevenueCat 2026).

## Compliance guardrails (day-one architecture, not features)

- Precise location is the most sensitive surface: generated routes anchored at home reveal home address (Strava heatmap precedent). Privacy zones and private-by-default are mandatory from the MVP.
- Heart rate and training load are GDPR Article 9 special category data; FTC Health Breach Notification Rule and Washington MHMD apply to consumer fitness apps.
- EU AI Act Article 50 transparency (disclose users are talking to AI) applies from 2026-08-02.
- Full 15-item MVP compliance checklist: `research/01-market/regulatory-compliance.md`.

## Related

- [[Founder-Brief]] (hypotheses H2, H4, H5 touched by these findings)
- [[_Knowledge-Index]]
- `research/01-market/` (full documents with citations)
