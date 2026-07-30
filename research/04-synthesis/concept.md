# Waypoint Concept Definition

Version-Timestamp: 2026-07-30 16:30:00 UTC-4

Status: PROPOSED FOR LOCK. This document synthesizes Phases 0 to 3 into the concept Claudio locks at the Phase 4 gate. Decisions requiring his explicit choice are marked "GATE DECISION". Once locked, this document governs Phase 5 (product definition) and beyond; changes after the lock require a decision record.

## 1. The concept

Waypoint is the running app that knows where you should run. Its hero capability is **constraint-based adaptive route generation**: from wherever the runner stands, it generates the right route for today, treating distance, elevation, weather and humidity, street crossings, surface, safety, and the runner's training state as routing inputs rather than afterthoughts. A personalized coaching layer sits on top of the route engine, connecting what the runner's body needs to where the runner actually goes, which no product on the market does (`research/02-competitors/gap-analysis.md`, H2 verdict in `hypotheses-review.md`).

Elevator version: every training app prescribes workouts without knowing where you are standing; every route app draws static lines without knowing what your body needs today. Waypoint answers the question both halves ignore: "where should I run, right now, from here, for me."

## 2. The users

- **Primary: the committed amateur** (Marcus). Runs 3 to 5 times per week, races a few times a year, self-coached via apps, will not pay a human coach. The only segment with proven willingness to pay in this category (`research/03-users/segmentation.md`). [verified]
- **Secondary: the ambitious beginner** (Jake). The Gen Z-weighted growth pipeline; served in the same product with gentler calibration, not a separate SKU (`research/03-users/segmentation.md`). [verified]
- **Within the primary, two activation-critical profiles**: the traveling professional (Priya; the sharpest demo of the hero feature) and the safety-first runner (Elena; for whom the route IS the safety decision, and whose needs are the strongest-evidence unmet need in the entire research program) (`research/03-users/personas.md`, `unmet-needs.md`). [verified]
- **Anti-users (explicitly not designed for)**: serious racers with human coaches, casual run-trackers content with free apps, trail-first ultrarunners (AllTrails territory), multi-sport athletes (`research/03-users/segmentation.md`, `research/02-competitors/gap-analysis.md` section d).

## 3. The user needs (ranked by evidence strength)

1. **Safety-aware routing** (strong): 54 percent of women runners changed routes over safety; zero of 15+ products accept safety as a routing input (`research/03-users/unmet-needs.md`). [verified]
2. **Route novelty and personalization at home** (strong): "roads not yet run" is a proven paying desire (CityStrides, 90k+ users); incumbents rank by popularity, the opposite (`unmet-needs.md`). [verified]
3. **The training-state-to-route connection** (strong gap, inferred demand): total market absence; demand confirmation is interview priority 1 (`unmet-needs.md`). [inferred]
4. **"Where do I run" in unfamiliar places** (frequent, episodic): the founding insight; constant in communities, usually worked around, therefore the activation moment and demo story rather than the daily driver (`pain-points.md`, H1 verdict). [verified]
5. **Plans that survive real life** (moderate): disruption guilt, adaptation distrust, the Runna-too-hard vs TrainAsONE-too-soft calibration gap (`pain-points.md`, `gap-analysis.md`). [verified]
6. **Navigation without friction** (moderate, narrower): voice-guided execution so the phone stays in the pocket; RunGo proves willingness to pay for this alone (`pain-points.md`). [verified]

## 4. The features

**The hero (free tier anchors here, exact boundary set in Phase 6):**
- On-demand route generation from any start point with constraint inputs: target distance, elevation preference, surface, street-crossing minimization, lighting and populated-area awareness (framed as "safety-aware", never "safe": see liability note), weather and heat adjustment (shade, exposure).
- Route novelty: personal history awareness, "roads you have not run", never the same loop twice unless asked.
- Travel mode: instant orientation in an unfamiliar city (the demo story and activation moment).

**The adaptive layer (paid tier):**
- Training-state-aware generation: today's workout type, fatigue and readiness (HealthKit), progression toward a race goal shape the route that gets generated.
- Adaptive routines: plans that reshape when life happens (missed runs, travel, weather), calibrated between Runna-too-aggressive and TrainAsONE-too-conservative (`gap-analysis.md` unmet need 4).
- The coach explains its reasoning (trust is the adoption barrier for AI training advice; transparency is the counter).

**The execution surface:**
- Voice-guided turn-by-turn navigation so the phone stays pocketed; Apple Watch companion for glanceable cues.
- Post-run: share to Strava (never compete with the social graph: `gap-analysis.md` section d).

**Day-one architecture (not features, obligations):**
- Privacy zones and private-by-default routes; granular consent; the 15-item compliance checklist from `research/01-market/regulatory-compliance.md`.
- EU AI Act Article 50 transparency (disclose the AI, effective 2026-08-02).

## 5. The functionality (how it works, concept level)

1. **Inputs**: location, stated constraints (distance, elevation, surface preferences), ambient context (weather, humidity, daylight, via free-tier APIs), personal context (running history, training plan state, HealthKit readiness signals), and the proprietary context layer (street-crossing graphs, lighting and populated-area scoring built from open data).
2. **Route engine**: constraint-solving generation on OpenStreetMap data (GraphHopper-class round-trip routing plus custom constraint scoring). The routing algorithms are published research; the moat is the constraint data and personalization, not the router (`research/01-market/industry-trends.md`). [verified]
3. **Coaching layer**: plan generation and daily adaptation informed by training load and readiness; on-device AI where feasible (Apple foundation models) for privacy and cost.
4. **Learning loop**: every completed run teaches preferences (hills avoided, turns missed, routes re-run); personalization compounds into switching cost.
5. **Data posture**: HealthKit-first (Garmin developer program is paused; Strava's API bans AI use of its data: `adjacent-platforms.md`). The moat is data Waypoint builds, not data it borrows. [verified]

## 6. The business needs

- **Model**: freemium subscription (H4 partially supported; category payment proven, tier boundary set in Phase 6 with the safety-free-tier decision as its gating input).
- **Price umbrella**: between Garmin Connect+ ($70/yr) and the Strava+Runna bundle ($150/yr) (`pricing-matrix.md`). [verified]
- **The investor story must carry the expansion path** (H5 uncertain): the wedge alone benchmarks to $5M to $30M ARR by year 5; venture scale requires the stated sequence: iOS English-first, then Android, more geographies, and the broader "context-aware outdoor coaching" surface (walking, cycling, hiking are the same route engine with different constraint weights) (`market-sizing.md`, `opportunity.md`). [inferred]
- **Execution window**: 12 to 18 months before Strava plausibly ships plan-linked route generation v1; Strava's Instant Workouts (January 2026) already attaches heatmap routes to suggested workouts, so the window consumes from now and the differentiation rests on constraint depth and personalization (`positioning.md`). Speed is a business requirement, not a preference. [verified]
- **Trust as brand strategy**: clean billing (a category-wide complaint: `gap-analysis.md` unmet need 7), transparent AI, never marketing "safe routes" as a guarantee (liability: `unmet-needs.md`).
- **12-month goal** (unchanged from the Founder Brief): MVP live, thousands of active runners, seed closed or in motion.

## 7. What Waypoint is NOT (locked with the concept)

No social network (post TO Strava). No route content library (generate, do not curate). No multi-sport breadth in v1. No hardware ambitions. No "best training plan" brand war with Runna. No charging for what the market gives away free (basic loop generation). (`gap-analysis.md` section d.)

## 8. GATE DECISIONS for Claudio

1. **Lock the concept as defined above** (sections 1 to 7), or amend.
2. **Positioning statement**: recommended Candidate A (route-first) from `positioning.md`: "For committed amateur runners who never quite know where today's run should go, Waypoint is the running app that generates the right route for you, right now, from wherever you stand."
3. **Tagline**: `positioning.md` recommends retiring "Your AI Running Coach" (it prices Waypoint against free Garmin/Apple and brands it against Runna) in favor of route-led options ("Know where to run", "The app that knows where you should run", "Never wonder where to run", or the bridge option "The coach that knows the way").
4. **The H1 reframe**: accept travel as activation and safety plus novelty as daily retention (recommended, evidence-backed), or keep travel as the headline wedge.
5. **Deferred by design**: the safety-free-tier decision lands in Phase 6 with pricing; the interview backlog runs alongside Phase 5 and can adjust calibration without unlocking the concept.

## Assumptions

- A1: Runners experience the route situations (travel, safety, boredom, workout fit) as one job an app can own; the bundling test is interview priority 1. [assumption]
- A2: The expansion path (multi-activity context-aware coaching) is credible to investors without traction proof. [assumption]
- A3: Proprietary context data (crossing graphs, lighting scoring) is buildable from open data at solo-founder scale; Phase 5 must validate technically. [assumption]

## Open questions

- Interview program results (willingness to pay, safety trust, bundling) may recalibrate tier boundaries and messaging; they do not block Phase 5.
- Strava Instant Workouts capability depth needs monitoring (added to the Phase 2 early-warning list). #open-question

## Related

- `hypotheses-review.md`, `opportunity.md`, `positioning.md` (this folder)
- `vault/01-Project/Founder-Brief.md` (the vision this concept refines)
- `vault/04-Knowledge/` (Phase 1 to 3 key findings notes)
