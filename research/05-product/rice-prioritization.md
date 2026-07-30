# RICE Prioritization: Waypoint Candidate Feature Set

Version-Timestamp: 2026-07-30 16:15:00 UTC-4

**Executive summary.** Thirty candidate features, drawn from the locked concept (`research/04-synthesis/concept.md`, DEC-006) plus the table-stakes capabilities the category demands (`research/02-competitors/feature-matrix.md`), are scored with RICE. The top of the ranking is dominated by cheap, high-reach enablers (HealthKit sync, privacy architecture, GPS tracking, Strava share) and by low-effort hero surfaces (route novelty, travel mode, honest degradation). The hero engine itself (core constraint generation) ranks eleventh on raw RICE because its effort is the largest single line item, which is a property of the formula, not a verdict: without it, nothing above it matters. The paid coaching layer scores in the bottom third across the board, driven by inferred (not expressed) demand and heavy effort, which is exactly why it belongs after the free-tier hypothesis is proven. Eight scores carry explicit sensitivity flags tied to the open interview backlog (`research/03-users/unmet-needs.md`, Section c).

## 1. Method

- **Formula**: RICE = (Reach x Impact x Confidence) / Effort.
- **Reach**: users per quarter affected, against a reference base of 10,000 quarterly active users (QAU). [assumption] The base is a working normalization consistent with the 12-month goal of "thousands of active runners" (`concept.md`, Section 6); absolute reach numbers will scale with actual adoption, relative rankings will not.
- **Impact** per user reached, on the core hypothesis (runners adopt and return for constraint-based route generation): 3 = massive, 2 = high, 1 = medium, 0.5 = low, 0.25 = minimal.
- **Confidence**: percent, mapped from the Phase 3 evidence-strength rubric (`unmet-needs.md`, Section a): strong desk evidence 80 to 90 percent, moderate 60 to 75 percent, inferred demand or weak evidence 50 to 55 percent. No score exceeds 90 percent because zero user interviews have been conducted. [verified: desk research disclaimer, `unmet-needs.md`]
- **Effort**: person-months for a small team (solo founder plus contractors), including design, build, and test for that item, excluding shared release overhead (counted once in `mvp-scope.md`).
- **Sensitivity flags** (column S) mark scores that move materially if an open assumption breaks. Legend in Section 4.

## 2. Candidate inventory and sources

| Group | Items | Source |
|---|---|---|
| Table stakes and enablers (TS) | GPS tracking, run history, HealthKit sync, onboarding, audio cues, route save, Strava share, subscription infrastructure, GPX export, offline routes | `feature-matrix.md` (what every credible category product has), `concept.md` Section 5 (data posture) |
| Hero: free-tier route engine (H) | Core constraint generation, elevation, surface, street crossings, safety-aware routing, weather adjustment, route novelty, travel mode, honest degradation, learning loop | `concept.md` Section 4 (the hero) and Section 5 (functionality) |
| Paid: adaptive layer (P) | Training-state-aware generation, adaptive routines, explainable coach, readiness input, race progression, injury calibration | `concept.md` Section 4 (the adaptive layer) |
| Execution surface (X) | Voice turn-by-turn, Apple Watch companion, live location sharing | `concept.md` Section 4 (execution surface), `unmet-needs.md` need 6, `personas.md` (Elena) |
| Day-one obligations (O) | Privacy zones, private-by-default, granular consent, EU AI Act Article 50 disclosure (scored as one architecture item) | `concept.md` Section 4 (day-one architecture), `regulatory-compliance.md` |

## 3. Scoring table, ranked by RICE

Reading the math: RICE = (R x I x C) / E, shown per row. Reach in users per quarter of the 10,000 QAU base.

| Rank | ID | Feature | Reach (why) | Impact (why) | Conf. (why) | Effort pm (why) | RICE math | RICE | S |
|---|---|---|---|---|---|---|---|---|---|
| 1 | TS-03 | HealthKit sync (read activity, write runs) | 8,500: near-all iOS runners grant Health access [inferred] | 2: HealthKit-first is the locked data posture, Garmin paused, Strava API closed [verified, `concept.md` S5] | 85%: platform capability certain, grant rate assumed | 1.0: standard HealthKit read/write | 8500x2x0.85/1.0 | 14,450 | |
| 2 | O-01 | Privacy zones, private-by-default, consent, AI disclosure | 10,000: architecture touches every user | 2: day-one obligation, Elena's trust hinges on it, EU AI Act effective 2026-08-02 [verified] | 90%: compliance requirement, not a demand bet | 1.5: geofenced blurring, consent flows, disclosure copy | 10000x2x0.90/1.5 | 12,000 | |
| 3 | TS-08 | Subscription and paywall infrastructure (clean billing) | 10,000: every user eventually meets the tier boundary | 2: business requirement, and trust-as-brand vs category billing complaints [verified, `pricing-matrix.md`] | 85%: mechanics proven, conversion untested | 1.5: StoreKit 2 plus receipt handling or RevenueCat-class service | 10000x2x0.85/1.5 | 11,333 | S6 |
| 4 | TS-07 | Strava share (post run to Strava) | 6,000: Strava penetration among committed amateurs [inferred from `personas.md` Marcus] | 1: credibility and distribution, never compete with the graph [verified, `concept.md` S7] | 80%: upload API is standard; AI-use ban does not block posting | 0.5: OAuth plus activity upload | 6000x1x0.80/0.5 | 9,600 | |
| 5 | TS-01 | GPS run tracking (pace, distance, time, map) | 10,000: every run by every user | 2: absence kills the product, presence does not differentiate [verified: all 10 competitors have it] | 90%: fully understood problem | 2.0: CoreLocation recording, battery tuning, GPS smoothing | 10000x2x0.90/2.0 | 9,000 | |
| 6 | TS-04 | Onboarding and permissions flow | 10,000: every install | 1: activation gate, not a value driver itself | 85%: known patterns; consent-rate risk noted | 1.0: location, Health, notification permission choreography | 10000x1x0.85/1.0 | 8,500 | |
| 7 | TS-02 | Run history and basic stats | 8,000: everyone who runs twice | 1: table stakes retention surface | 90%: universal category expectation | 1.0: list, detail, weekly aggregates | 8000x1x0.90/1.0 | 7,200 | |
| 8 | H-07 | Route novelty ("roads you have not run", history-aware) | 6,000: home runners, the daily use case [verified: need 2, strong] | 2: evidence rank 2, proven paying desire (CityStrides 90k) [verified] | 80%: strong desk evidence; loop-loyalist share unknown | 1.5: history overlap scoring on the generator | 6000x2x0.80/1.5 | 6,400 | S3 |
| 9 | H-08 | Travel mode (instant orientation, unfamiliar city) | 2,000: episodic, traveler subset [verified: H1 reframe] | 2: the activation moment and demo story [verified: DEC-006 point 4] | 75%: frequency verified, willingness-to-pay absent in threads | 0.5: framing and UX on the same engine, not new routing | 2000x2x0.75/0.5 | 6,000 | S1 |
| 10 | H-09 | Honest degradation ("no good route meets your constraints") | 2,000: constraint-edge encounters | 1: trust prerequisite for safety claims [inferred, `unmet-needs.md` implication 2] | 70%: design judgment, liability-driven | 0.25: messaging states on the generator | 2000x1x0.70/0.25 | 5,600 | S2 |
| 11 | H-01 | Core constraint route generation (distance, start-anywhere, round-trip) | 9,000: the product's reason to exist; near-all actives generate | 3: the hero; the core hypothesis IS this feature | 80%: gap verified across 15+ products; bundled demand inferred | 4.5: GraphHopper-class round-trip routing plus custom constraint scoring service and route quality tuning | 9000x3x0.80/4.5 | 4,800 | S1 |
| 12 | TS-05 | Audio pace and distance cues | 6,000: headphone runners | 0.5: expected, minimal differentiation | 80%: standard capability | 0.5: interval announcements over the tracking engine | 6000x0.5x0.80/0.5 | 4,800 | |
| 13 | TS-06 | Route save and re-run | 5,000: keepers of good routes | 0.5: convenience, mild retention | 80%: standard pattern | 0.5: persistence plus load-into-navigation | 5000x0.5x0.80/0.5 | 4,000 | |
| 14 | H-02 | Elevation constraint (target or avoid climb) | 5,000: hill avoiders and seekers | 1: expected of a serious generator; Strava only offers coarse presets [verified] | 75%: verified competitor gap, moderate expressed demand | 1.0: elevation data is in OSM/DEM, scoring is straightforward | 5000x1x0.75/1.0 | 3,750 | |
| 15 | X-01 | Voice turn-by-turn navigation | 7,000: most runs on generated (unfamiliar) routes need guidance | 2: the bridge from generation to execution; mandatory per concept [verified: need 6, RunGo pays alone] | 70%: moderate evidence, narrower population | 3.0: turn detection, audio timing, rerouting, background audio | 7000x2x0.70/3.0 | 3,267 | S5 |
| 16 | H-05 | Safety-aware routing v1 (lighting, populated areas, time of day) | 5,000: women ~50% of base with 92% concern rate, plus dawn/dark runners of all genders [verified] | 3: evidence rank 1, strongest need in the research program [verified] | 70%: evidence strong, but algorithmic trust unvalidated (interview priority 2) | 4.0: open-data lighting and population scoring layer plus constraint integration (A3 risk) | 5000x3x0.70/4.0 | 2,625 | S2, S7 |
| 17 | X-02 | Apple Watch companion (glanceable cues, watch recording) | 5,500: Apple Watch is Strava's top device [verified] | 2: Priya's execution surface; pocket-phone promise | 65%: H6 supported, watch/phone split survey open | 4.0: watchOS app, sync, complications, battery | 5500x2x0.65/4.0 | 1,788 | S5 |
| 18 | H-03 | Surface constraint (road, trail, soft surface) | 3,000: surface-sensitive runners | 0.5: nice on top of the hero, rarely decisive alone | 70%: verified gap, thin expressed demand | 1.0: OSM surface tags into scoring | 3000x0.5x0.70/1.0 | 1,050 | |
| 19 | X-03 | Live location sharing (beacon-style) | 3,000: safety-conscious users | 1: Elena job, but Strava Beacon and Find My already serve it [verified] | 55%: duplication of trusted incumbents | 2.0: live session infra, share links, privacy review | 3000x1x0.55/2.0 | 825 | S2 |
| 20 | H-04 | Street-crossing minimization | 4,000: urban uninterrupted-run seekers | 1: differentiating constraint, zero competitor entries [verified] | 60%: no direct demand evidence; product logic | 3.0: crossing graph derivation from OSM at scale (A3 risk) | 4000x1x0.60/3.0 | 800 | S7 |
| 21 | P-01 | Training-state-aware generation (workout shapes the route) | 2,000: paid-tier and trial subset | 3: the defensible seam, paid centerpiece [verified gap, inferred demand: need 3] | 50%: demand is product logic, interview priority 1 | 4.0: plan-state model plus constraint mapping per workout type | 2000x3x0.50/4.0 | 750 | S1, S6 |
| 22 | H-06 | Weather and heat route adjustment (shade, exposure) | 3,000: seasonal, hot-climate skew | 1: differentiator; pace-side analogs ship (Runna heat) [verified] | 50%: need 9 weak to moderate; route-side demand not found | 2.0: weather API plus shade/exposure scoring | 3000x1x0.50/2.0 | 750 | S3 |
| 23 | H-10 | Learning loop (preference learning from completed runs) | 4,000: repeat generators | 1: compounds into switching cost over time [inferred] | 50%: mechanism unvalidated, effect long-horizon | 3.0: feedback capture, preference model, re-ranking | 4000x1x0.50/3.0 | 667 | S3 |
| 24 | TS-10 | Offline route access (maps and route offline) | 2,000: travelers, spotty coverage | 1: Priya stress case; Komoot gates this as paid [verified] | 60%: need present, frequency unknown | 2.0: tile caching, offline nav states | 2000x1x0.60/2.0 | 600 | S5 |
| 25 | P-03 | Explainable coach (reasoning transparency) | 2,000: paid-tier subset | 1: trust counter to AI skepticism [inferred, `concept.md`] | 60%: transparency-trust link is category folklore plus surveys | 2.0: explanation generation over coach decisions | 2000x1x0.60/2.0 | 600 | S1 |
| 26 | P-06 | Injury-calibrated progression (the Runna/TAO middle) | 1,500: plan followers in the paid tier | 2: unclaimed calibration middle [verified sentiment both ends] | 55%: sentiment verified, calibration target unproven | 4.0: load modeling, conservative-aggressive tuning, liability care | 1500x2x0.55/4.0 | 413 | S4 |
| 27 | P-02 | Adaptive routines (plans that reshape when life happens) | 2,000: plan followers | 2: H7 retention deepener, directionally supported [verified caveat: guilt and schedule, not routes] | 60%: over 50% of marathoners miss 7+ days [verified]; route connection inferred | 6.0: plan engine, adaptation logic, calendar integration; largest single build | 2000x2x0.60/6.0 | 400 | S4 |
| 28 | P-04 | Readiness and fatigue input (HRV, sleep into generation) | 1,500: wearable-rich paid subset | 1: sharpens the seam, does not create it | 50%: signal quality and user trust both unproven | 2.0: HealthKit readiness ingestion plus weighting | 1500x1x0.50/2.0 | 375 | S4 |
| 29 | TS-09 | GPX export and import | 1,000: power users, watch ecosystems | 0.25: escape hatch, goodwill | 70%: trivial, known demand niche | 0.5: file generation and parsing | 1000x0.25x0.70/0.5 | 350 | |
| 30 | P-05 | Race-goal progression (plan toward a race date) | 1,500: race-committed paid subset | 1: expected of a coaching tier eventually | 60%: category standard, not a wedge driver | 3.0: goal modeling, phased plan structure | 1500x1x0.60/3.0 | 300 | S4 |

## 4. Sensitivity flags (scores that move if assumptions break)

The interview backlog is still open (`unmet-needs.md`, Section c). These flags mark which scores are hostage to which unvalidated assumption.

| Flag | Assumption at risk | Validation instrument | Features affected | Direction if it breaks |
|---|---|---|---|---|
| S1 | Runners experience the route situations as one bundled job (A1); training-state demand is felt, not just logical | Interview priority 1 (8 to 12 committed amateurs) | H-01, H-08, P-01, P-03 | H-01 Confidence drops toward 60%, P-01 toward 35%; the concept itself is re-examined per DEC-006 |
| S2 | Safety-conscious runners will trust an algorithmic route at all | Interview priority 2 (4 to 6 women runners, specialist moderator) | H-05, H-09, X-03 | H-05 Impact could fall to 1 (feature becomes a display layer) or rise (trust earned = category-defining); this is the widest swing in the table |
| S3 | Novelty demand beats loop loyalty; weather and preference learning are felt value | MVP telemetry signals 2, 7 (`unmet-needs.md` Section d) | H-07, H-06, H-10 | H-07 Reach halves if loop loyalists dominate |
| S4 | Plan disruption connects to route intelligence (H7 inference) | MVP telemetry signals 4, 5; interview priority 1 | P-02, P-04, P-05, P-06 | Entire paid-plan block loses a further 10 to 20 points of Confidence; paid tier re-centers on P-01 alone |
| S5 | Watch/phone execution split supports phone-first voice MVP | Parallel screener survey (n 100+); telemetry signal 6 | X-01, X-02, TS-10 | If watch-dominant, X-02 moves up and X-01 phone investment partially strands |
| S6 | Freemium converts at category rates (H4) | Telemetry signal 8 (paywall encounter conversion); Phase 6 pricing work | TS-08, P-01 | Reach of every P-row falls with conversion; tier boundary moves |
| S7 | Constraint data (crossings, lighting) is buildable from open data at solo-founder scale (A3) | Month-1 technical spike (see `mvp-scope.md`, gate GD-3) | H-05, H-04 | Effort doubles or scope shrinks to time-of-day heuristics; H-05 RICE falls below 1,500 |

## 5. Reading notes (how to use this ranking honestly)

1. RICE measures efficiency, not necessity. The hero engine (H-01) ranks eleventh only because it carries the largest effort denominator; every TS row above it is worthless without it. The MVP line in `mvp-scope.md` is drawn with RICE plus the dependency graph plus the core hypothesis, not RICE alone. [inferred]
2. Cheap enablers and obligations cluster at the top by construction (full reach, low effort). Their high scores mean "do these without debate", not "these are the product". [inferred]
3. The paid layer's uniformly low scores are an artifact of honest Confidence (inferred demand) and honest Effort (plan engines are big). This is the quantitative case for wedge-first sequencing: prove the free hero, then buy Confidence with telemetry and interviews before spending 15+ person-months on coaching. [inferred]
4. Every score in this table is desk-research-calibrated. Interview priorities 1 and 2 can move any flagged row by a tier; the table should be re-scored once (not continuously) when the interview program lands. [assumption]

## Assumptions

- [assumption] 10,000 QAU reference base; rankings are robust to the base, absolute RICE values are not.
- [assumption] Reach shares (for example 60 percent Strava penetration, 55 percent Apple Watch, 50 percent women users) are directional composites from `personas.md` and `segmentation.md`, not measured cohorts.
- [assumption] Effort figures assume a competent iOS contractor and a backend contractor available on demand; solo-founder-only effort would run 30 to 50 percent higher in calendar terms.
- [assumption] Impact is scored against the core hypothesis (adopt and return for constraint-based generation), not against revenue; a revenue-weighted re-score in Phase 6 will lift the P block.
- [assumption] No competitor shipment between 2026-07-30 sources and this scoring (same day).

## Open questions

1. Do interview priorities 1 and 2 confirm the Confidence tiers, especially H-01 at 80 percent and H-05 at 70 percent?
2. Does the A3 technical spike (GD-3 in `mvp-scope.md`) validate the safety data layer effort at 4.0 person-months, or force a re-score?
3. Where exactly the free/paid boundary lands (Phase 6) changes Reach for every P row; re-score after the pricing decision.

## Related

- `research/05-product/mvp-scope.md` (the line drawn through this ranking)
- `research/04-synthesis/concept.md` (DEC-006, candidate feature source)
- `research/03-users/unmet-needs.md` (evidence strength and interview backlog)
- `research/02-competitors/feature-matrix.md`, `pricing-matrix.md` (table stakes and tier patterns)
