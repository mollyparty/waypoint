# MVP Scope: The Line Through the Ranking

Version-Timestamp: 2026-07-30 16:20:00 UTC-4

**Executive summary.** The MVP exists to prove one hypothesis: committed amateur runners will adopt and return for constraint-based route generation. Everything in MVP v1 either proves that hypothesis, is a table-stakes prerequisite for testing it, or is a day-one legal and trust obligation. Fifteen items make the cut at roughly 23 person-months of scored effort (about 25 with release overhead), which a founder plus two contractors can ship in 8 to 10 calendar months: walking skeleton on TestFlight by month 3 to 4, App Store launch by month 9. The entire paid coaching layer, the Apple Watch app, and every remaining constraint wait for v1.x or v2, each with a named pull-forward trigger. The concept's NOT list (DEC-006) stays never. Four gate decisions close the document, each with a recommendation.

**The ONE core job** (from `research/03-users/jobs-to-be-done.md` via `concept.md`): the right route, right now, from here, for me. Travel is the demo; safety plus home novelty are the daily muscles [verified: DEC-006 point 4].

## 1. The MVP line at a glance

| Tier | What | Items | Scored effort (pm) |
|---|---|---|---|
| MVP v1 (ships first) | Generate a constrained route, run it with voice guidance, save it, trust it | 15 | 22.75 |
| Fast-follow v1.x (30 to 120 days post-launch) | Monetization, Watch, remaining constraints, depth | 8 | ~17 |
| Deferred v2+ | Full coaching layer, expansion surface | 6 | ~20 |
| Never (DEC-006 NOT list) | Social network, route library, multi-sport, hardware, plan-brand war, paid basic loops | n/a | 0 |

## 2. MVP v1: what ships and why

Every feature carries its RICE rank (`rice-prioritization.md`) and a one-line reason it makes the cut.

| RICE rank | ID | Feature | Effort pm | Why it makes the cut |
|---|---|---|---|---|
| 6 | TS-04 | Onboarding and permissions flow | 1.0 | No permissions, no product; the activation gate for everything below. |
| 5 | TS-01 | GPS run tracking | 2.0 | Table stakes; a running app that cannot record a run is not a running app [verified: all 10 competitors]. |
| 12 | TS-05 | Audio pace and distance cues | 0.5 | Expected by every headphone runner; trivial on top of tracking. |
| 7 | TS-02 | Run history and basic stats | 1.0 | The return visit needs something to return to. |
| 1 | TS-03 | HealthKit sync | 1.0 | The locked data posture (HealthKit-first) starts accruing the moat from day one [verified: `concept.md` S5]. |
| 13 | TS-06 | Route save and re-run | 0.5 | A good generated route the user cannot keep is a broken promise. |
| 4 | TS-07 | Strava share | 0.5 | Post TO Strava, never compete with it; free distribution and credibility [verified: DEC-006 NOT list]. |
| 2 | O-01 | Privacy zones, private-by-default, consent, AI disclosure | 1.5 | Legal obligation (EU AI Act, 2026-08-02) and the trust floor Elena stands on; not optional at any scope. |
| 11 | H-01 | Core constraint route generation (distance, start-anywhere, round-trip) | 4.5 | The hypothesis itself; the single reason the product exists. |
| 14 | H-02 | Elevation constraint | 1.0 | Cheapest real constraint beyond distance; makes "constraint-based" true, not marketing. |
| 8 | H-07 | Route novelty (history-aware, "roads you have not run") | 1.5 | Evidence rank 2 need and the daily retention driver at home; the return-visit engine [verified]. |
| 16 | H-05 | Safety-aware routing v1 (lighting, populated areas, time of day) | 4.0 | Evidence rank 1 need, scoped as a launch capability per the Phase 3 mandate, not a later mode [verified: `unmet-needs.md` implication 2]. Scope gated by GD-3. |
| 9 | H-08 | Travel mode framing | 0.5 | The activation moment and demo story at near-zero marginal cost (same engine, different framing) [verified: DEC-006 point 4]. |
| 10 | H-09 | Honest degradation messaging | 0.25 | Cheapest trust feature in the table; a safety-aware product that pretends is a liability. |
| 15 | X-01 | Voice turn-by-turn navigation | 3.0 | Generation without execution strands the value; a generated route the runner cannot follow hands-free fails Priya and Marcus both [verified: need 6]. |

Total scored: 22.75 person-months. What "return" means for the hypothesis: week-4 retention of users who generated at least one route, plus the repeat-generation rate (telemetry signals 1 to 3, `unmet-needs.md` Section d). [inferred]

Explicitly NOT in MVP v1 despite high RICE rank: TS-08 subscription infrastructure (rank 3) is deferred to v1.x by gate decision GD-1 below; its high score reflects enabler efficiency, not launch urgency.

## 3. Fast-follow v1.x (30 to 120 days post-launch)

Each deferral names the evidence or milestone that pulls it forward.

| ID | Feature | Effort pm | Pull-forward trigger |
|---|---|---|---|
| X-02 | Apple Watch companion | 4.0 | Fires by default at launch+30 (build starts during beta); pulls into v1 only if the screener survey shows watch-dominant execution above ~60 percent (S5). |
| TS-08 + P-01 | Paywall plus training-state-aware generation (first paid feature, shipped together) | 5.5 | Week-4 retention of route generators clears the healthy-cohort bar (directionally 20 percent+, RevenueCat-class benchmarks); paywall without proven return burns the trust budget. |
| H-04 | Street-crossing minimization | 3.0 | A3 spike (GD-3) proves crossing graphs cheap; or beta feedback names interrupted runs a top-3 complaint. |
| H-06 | Weather and heat route adjustment | 2.0 | Launch summer cohort telemetry shows heat-hour generation spikes; or acceptance-rate test slot opens (signal 7). |
| H-03 | Surface constraint | 1.0 | Beta users request it organically; cheap enough that moderate demand suffices. |
| TS-10 | Offline route access | 2.0 | Travel-mode telemetry (signal 1) shows meaningful far-from-home generation share; Priya validation in interviews. |
| P-03 | Explainable generation ("why this route") | 2.0 | Safety trust interviews (priority 2) confirm explanation earns trust; then ship alongside the safety layer's first upgrade. |
| TS-09 | GPX export | 0.5 | First sustained user requests; near-free goodwill. |

## 4. Deferred to v2+

| ID | Feature | What would pull it forward |
|---|---|---|
| P-02 | Adaptive routines (plans that reshape) | Workout-route attach rate (signal 4) proves the seam is felt value, and paid conversion on P-01 funds the 6 pm build. |
| P-06 | Injury-calibrated progression | P-02 exists (calibration needs a plan to calibrate); interview evidence that the Runna/TAO middle is worth claiming with liability care. |
| P-05 | Race-goal progression | P-02 exists; race-committed cohort share visible in telemetry. |
| P-04 | Readiness and fatigue input | P-01 attach rate proven, plus HealthKit readiness signal quality validated on real cohorts. |
| H-10 | Learning loop (preference model) | Repeat-generation volume creates the training data; before scale it has nothing to learn from. |
| X-03 | Live location sharing | Safety interviews show Strava Beacon and Find My leave a real gap; otherwise never (do not rebuild trusted incumbents). |

Android, additional geographies, and the multi-activity expansion surface are v2+ business decisions per the concept's stated sequence (`concept.md` Section 6), not feature deferrals. [verified]

## 5. Never (locked by DEC-006)

| Item | Why never |
|---|---|
| Social network or feed | Post TO Strava; never compete with the graph. |
| Route content library | Generate, do not curate; RunGo's territory. |
| Multi-sport breadth in v1 era | Focus is the moat; expansion is a later business decision, not a feature. |
| Hardware | Capital and competence mismatch for a solo founder. |
| "Best training plan" brand war with Runna | Unwinnable on brand; Waypoint wins on the seam, not the plan. |
| Charging for basic loop generation | Free web tools and Strava commoditized it; the free tier anchors here [verified: `pricing-matrix.md`]. |

## 6. Walking skeleton (thinnest end-to-end slice, TestFlight target: month 3 to 4)

One flow, fully working, nothing else: **generate a route, run it with voice guidance, save the run.**

| Step | Included (minimum) | Explicitly excluded from the skeleton |
|---|---|---|
| 1. Open app | Single-screen onboarding: location permission, Health write permission, AI disclosure line | Accounts beyond Sign in with Apple, notification permission, preference setup |
| 2. Generate | Start from current location, target distance input, one round-trip route on screen (map preview, distance, elevation profile) | All other constraints (elevation preference, safety, novelty), regenerate options, travel framing |
| 3. Run it | Start run, GPS tracking, voice turn cues through headphones, basic pace/distance announcements | Watch, offline, rerouting beyond rejoin guidance, audio settings |
| 4. Finish | Run summary, save locally, write workout to HealthKit | Strava share, history views beyond a simple list, stats |
| 5. Trust | Private-by-default storage, home-area coordinates never leave the device unblurred | Full privacy-zone UI, consent management screens |

Skeleton effort: roughly 6 to 7 person-months of the 22.75 total, reachable by month 3 to 4 with the team below. [inferred] Its job is to make the core hypothesis testable with 20 to 50 TestFlight runners while interviews run in parallel (GD-4), and to smoke out the routing-quality risk (the real MVP risk is bad routes, not missing features). [inferred]

## 7. Effort and calendar

> **AMENDED 2026-08-06 by [[DEC-010 Staged cross-platform MVP on React Native]].** The figures below were the iOS-native estimate. Under the approved staged cross-platform plan (one React Native codebase, MapLibre on both platforms), total effort is **~29 to 31 person-months**, iOS ships **month 9 to 10**, Android **month 10 to 12**, full dual-platform launch **month 11 to 13**, with no added headcount. The 15-feature scope itself is unchanged. The contractor mix shifts from "senior iOS" to "senior React Native with native-module experience". Every other row below still holds. See `dual-platform-strategy.md` section 4 for the option-by-option costing.

| Line | Value (original iOS-native estimate) |
|---|---|
| MVP v1 scored effort | 22.75 person-months |
| Release overhead (App Store review cycles, beta management, QA hardening, crash triage) | ~2 person-months [assumption] |
| Total | ~25 person-months (**amended: ~29 to 31** under DEC-010) |
| Team | Founder full time (product, client, routing) plus 2 contractors: senior client engineer (0.75 to 1.0 FTE) and backend/routing plus data (0.5 to 1.0 FTE) [assumption] |
| Effective capacity | 2.5 to 3.0 FTE |
| Calendar | 8 to 10 months to App Store launch (**amended: iOS month 9 to 10, Android 4 to 8 weeks later**) |

| Milestone | Month |
|---|---|
| Android long-lead paperwork begins (Play org account, Health Connect + fine-location declarations, DEC-010) | 1 |
| A3 technical spike verdict (GD-3), now answering for both platforms | 1 |
| Walking skeleton on TestFlight | 3 to 4 |
| Interview priorities 1 and 2 complete, scope checkpoint | 3 to 4 |
| Feature-complete beta (all 15 items) | 7 |
| App Store launch | 8 to 9 (10 with slippage buffer) |
| v1.x paid layer (TS-08 + P-01) | 10 to 12 |

This fits the 12-month goal (MVP live, thousands of runners, seed in motion) and consumes at most 10 of the 12 to 18 month Strava window before launch, leaving the paid layer inside the window. [inferred] Slippage rule: if launch slips past month 10, cut safety data depth (fall back to time-of-day heuristics) or novelty scope; never cut the walking skeleton flow, and never add scope to "catch up". [inferred]

## 8. Gate decisions for the founder

| # | Decision | Recommendation | Reasoning |
|---|---|---|---|
| GD-1 | Where does the free/paid line sit in v1? | Launch v1 entirely free with no active paywall; ship TS-08 plus P-01 together in v1.x once week-4 retention clears the bar. Safety-aware routing stays free permanently (final pricing framing in Phase 6). | The MVP's only job is proving adopt-and-return; a paywall before proof contaminates the retention signal and burns the trust budget in a category with documented billing rage [verified: `pricing-matrix.md`]. Charging women a safety premium is the ethics line already flagged in `personas.md` (Elena); free basic generation is forced anyway by the commoditized floor. Risk accepted: 2 to 3 months of revenue delay against a cleaner hypothesis test and Phase 6 pricing informed by real telemetry (signal 8). |
| GD-2 | Apple Watch app: MVP or fast-follow? | Fast-follow v1.x, development starting during beta (month 6 to 7), shipping launch+30. MVP executes phone-first with voice through headphones. | Voice navigation with a pocketed phone tests the execution hypothesis at 3.0 pm; the Watch app adds 4.0 pm and watchOS risk to the critical path without changing what the MVP proves. The screener survey (S5) is the tripwire: watch-dominant results above ~60 percent pull it into v1 and push launch one month. |
| GD-3 | Safety-aware routing: full data layer in MVP or reduced scope? | Run a month-1 technical spike on A3 (lighting and population scoring from open data in 2 to 3 launch metros). Spike passes: ship H-05 as scoped (4.0 pm). Spike fails: launch with time-of-day and daylight heuristics plus honest degradation, move the full data layer to v1.x, and re-score H-05. | Safety is the strongest-evidenced need and the Phase 3 mandate says launch capability, but A3 (open-data buildability at solo scale) is the single riskiest technical assumption in the plan. A spike converts the biggest unknown into a scoped decision in 4 weeks instead of discovering it in month 5. Framing stays "safety-aware", never "safe", at every scope level (liability) [verified: `unmet-needs.md`]. |
| GD-4 | Do interviews gate the build start? | No. Build starts now; interview priorities 1 and 2 (12 to 18 conversations) run in parallel during months 1 to 3, landing at the walking-skeleton checkpoint. | The concept is locked (DEC-006) and the interview backlog was explicitly designed to recalibrate, not unlock. Waiting 2 to 3 months for interviews spends 15 to 25 percent of the competitive window to de-risk decisions the walking skeleton will also test with real behavior. The month 3 to 4 checkpoint is the built-in moment to act on interview findings before feature-complete beta locks scope. |

## Assumptions

- [assumption] Contractor availability and quality at the stated FTE levels; a hiring miss adds 1 to 2 calendar months.
- [assumption] Week-4 retention bar for GD-1 (directionally 20 percent+) borrows category subscription-cohort benchmarks; the exact bar should be set with RevenueCat-class data in Phase 6.
- [assumption] Walking skeleton effort (6 to 7 pm) and release overhead (~2 pm) are planning estimates, not quotes; the month-1 spike and skeleton build are the calibration instruments.
- [assumption] The 12 to 18 month Strava window (from `positioning.md`) holds; Strava shipping plan-linked generation early compresses everything and would justify cutting v1.x scope to accelerate the paid seam.
- [assumption] TestFlight recruitment of 20 to 50 target-segment runners by month 4 is achievable through run clubs and the founder's network.

## Open questions

1. Does the A3 spike pass, and at what per-metro data cost? (Gates GD-3 and the safety effort line.)
2. What do interview priorities 1 and 2 say at the month 3 to 4 checkpoint, and does anything they say move the v1.x order?
3. Which 2 to 3 launch metros? (Constrains the safety data build and beta recruitment; decide with the spike.)
4. Does the screener survey trip the GD-2 watch tripwire?

## Related

- `research/05-product/rice-prioritization.md` (the ranked input to this line)
- `research/04-synthesis/concept.md` (DEC-006, the locked concept and NOT list)
- `research/03-users/unmet-needs.md` (evidence ranking, interview backlog, telemetry signals)
- `research/02-competitors/pricing-matrix.md` (free-tier floor and tier patterns behind GD-1)
