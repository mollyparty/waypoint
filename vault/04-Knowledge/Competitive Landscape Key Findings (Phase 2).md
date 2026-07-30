---
type: knowledge
created: 2026-07-30
updated: 2026-07-30
tags: [knowledge, research, competitors, phase-2]
---

# Competitive Landscape Key Findings (Phase 2)

Distilled from `research/02-competitors/` (14 documents, full citations there). Completed 2026-07-30.

## Hypothesis verdicts from this phase

- **H2 (no incumbent solves constraint-based adaptive route generation): SUPPORTED.** Across 15+ products examined, zero accept weather, crossings, or safety as routing constraints; zero connect routes to training state. Coaching apps (Runna, TrainAsONE, AI Endurance, Coopah, Joggo) have no route capability at all; route apps (Komoot, AllTrails, Footpath, RunGo) have no training context; Strava generates from popularity, not from the runner.
- **H3 (route wedge beats plan wedge): SUPPORTED with a monetization caveat.** The plan market is crowded, branded (Runna), and floored at free by Garmin and Apple. The route wedge is open and demand-validated (free web generators, RunGo at $59.99/yr for navigation alone, Strava gating routes behind $79.99/yr). But basic generation is anchored at zero, so revenue lives in the adaptive layer: route wedge for acquisition, coaching layer for revenue, exactly the Founder Brief layering.

## Threat model

1. **Strava + Runna convergence is the kill shot**: one owner holds the only shipping route generator, the biggest heatmap, and the leading plan engine. Likelihood of a plan-linked v1 within 18 months: 50 to 60 percent; full constraint depth: 20 to 30 percent. **Working window: 12 to 18 months.** Early-warning signals: Runna beta strings about routes, Strava routing-engineer postings, bundle marketing shifting to "route creation for your workout".
2. **Runna owns the target user's trust ladder** (4.8 ratings, race partnerships, Strava funnel). Openings: injury discourse (paces too aggressive), bundle billing friction, sync complaints.
3. **AllTrails** could extend Peak's AI (currently only 4 adjustments on existing trail routes, cannot generate from scratch) toward runners; blind spot is urban doorstep running and training context.
4. **Data enclosure**: Strava API bans AI/ML use of its data; Garmin developer program paused. Build HealthKit-first; moat must be proprietary context data (crossing graphs, safety scoring, micro-weather), not incumbent data.

## Unmet needs to carry into Phase 3 (user research)

1. "Where should I run, right now, from here, for me" is unanswered anywhere.
2. Safety-aware routing (Strava's documented dangerous routes: interstates, no-shoulder roads; users ask for time-of-day awareness).
3. Weather/heat adaptation applied to the route, not just the pace (Runna Adapt for Heat and TrainAsONE prove pace-side demand).
4. Injury-calibrated coaching runners trust (Runna too aggressive, TrainAsONE too conservative; the middle is unclaimed).
5. Urban doorstep running is nobody's design center (Komoot is bike/hike-first, AllTrails is trail-locked).
6. Personalization beyond popularity (no "roads you have not run", no preference learning anywhere).
7. Trustworthy subscription mechanics (billing complaints are a category-wide pattern: differentiation opportunity).
8. Generation plus voice-guided execution in one product.

## Do not compete on

Community/social graph (post TO Strava), trail content libraries, coaching brand marketing, hardware/watch-native stack, price-zero basics, multi-sport breadth.

## Pricing intelligence

Price umbrella: Garmin Connect+ at $70/yr (low anchor) to Strava+Runna bundle at $150/yr (high anchor). Health and fitness is the only category where annual plans dominate. Freemium boundary pattern: incumbents gate routes and adaptivity behind paid; free tiers are trackers.

## Related

- [[Market Research Key Findings (Phase 1)]]
- [[Founder-Brief]] (H2 and H3 now supported; verdicts formalize in Phase 4)
- [[_Knowledge-Index]]
- `research/02-competitors/` (full documents with citations)
