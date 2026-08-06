# Waypoint Features and Functionality Catalog

> Version-Timestamp: 2026-08-06 15:44:38 UTC-4
>
> **Generated file. Do not edit.** Source of truth is `catalog/features.json`;
> regenerate with `python catalog/build.py`. The interactive view, where release
> assignment can be changed and the timeline recomputed, is `catalog/index.html`.

Release phase assignment for every feature, compliance requirement and non-functional requirement.

## Read this first

**Counting compliance and non-functional work explicitly adds roughly 2.8 React Native person-months that the published totals absorbed into a single 2.0 'release overhead' line.** mvp-scope.md section 7 carries one ~2.0 person-month line for release overhead. Priced individually, the 15 compliance requirements need about 2.1 native person-months of engineering beyond what O-01 already covers, and the non-functional set needs about 2.25. That is 4.35 native, or roughly 5.2 React Native, against a 2.0 native placeholder. Full approved scope is therefore closer to 32 to 33 React Native person-months than DEC-010's 29 to 31. The recut v1 is unaffected, because team-roadmap.md already priced compliance and hardening as separate 2-to-3 line items.

**The walking skeleton is a thin slice through eight features, not a subset of whole ones.** Adding up the whole features named in mvp-scope.md section 6 gives 14.0 native person-months, twice the 6 to 7 the document quotes. The skeleton is reduced versions of those features: single-screen onboarding rather than the full flow, one candidate route rather than three, private-by-default storage rather than the privacy-zone interface. Each entry therefore carries a separate skeletonEffort field, and the sum of those is 6.8.

**The PRD's launch-critical list is close to four years of work at this team's capacity.** Selecting the 19 features that prd.md section 4 marks P0, plus the 34 obligations it also marks launch-gating, totals 43.10 native person-months, or 51.7 in React Native terms. At 1.8x leverage and 7.5 person-months a year that projects to month 47. The PRD was written against a 2.5-to-3.0 full-time-equivalent assumption that no longer holds, which is why its priority tiers cannot be read as a release plan. They are still the right specification of what the product eventually is.

## What each scenario costs

At 7.5 person-months a year of real capacity, a 1.8x AI leverage assumption, and a 1.2x React Native factor over the iOS-native estimates. Competitive window: 12 to 18 months.

| Scenario | Native pm | React Native pm | After leverage | Projected iOS launch | Verdict |
|---|---:|---:|---:|---:|---|
| Walking skeleton only | 6.8 | 8.16 | 4.53 | month 9 | inside the window with room |
| Recut v1 (recommended) | 11.15 | 13.38 | 7.43 | month 13 | inside, only just |
| Full MVP v1 (15 features) | 27.1 | 32.52 | 18.07 | month 30 | **past the 18-month window** |
| PRD P0 list | 43.1 | 51.72 | 28.73 | month 47 | **past the 18-month window** |

The recut is the standing Phase 9 recommendation. Its projection reproduces `research/09-financial-team/team-roadmap.md`'s published month 12 to 14 independently, which is the check that the model is not inventing numbers.

## Where the documents disagree

### CF-1: Apple Watch companion: launch-critical or fast-follow?

Affects: `X-02`

- `research/05-product/prd.md:283` &mdash; P0 for glanceable cues mirrored from the phone.
- `research/05-product/mvp-scope.md:50` &mdash; Fast-follow v1.x, firing by default at launch plus 30.

**Recommendation.** Fast-follow. GD-2 already decided this on the record, and the reasoning holds independently of team size: voice through headphones tests the execution hypothesis at 3.0 person-months, while the Watch adds 4.0 and watchOS risk without changing what the MVP proves. The PRD's P0 predates that gate decision. Its tripwire stands: a screener showing watch-dominant execution above 60 percent pulls it forward.

### CF-2: All ten routing constraints at launch, or a subset?

Affects: `H-03`, `H-04`, `H-06`

- `research/05-product/prd.md:87` &mdash; The RG engine enumerates all ten constraint inputs and section 4 marks the engine P0.
- `research/05-product/mvp-scope.md:52` &mdash; Surface, street-crossing and weather constraints are v1.x.

**Recommendation.** Subset. The PRD enumerates the constraint model, which is the right thing for an engine specification to do; it does not follow that every constraint ships at launch. Distance, elevation, novelty, safety and daylight make 'constraint-based' true. Surface, crossings and weather add 6.0 person-months for the least-evidenced needs in the set (N9 is rated weak to moderate). Note that street-crossing minimization is the one users asked for in their own words, so it has the strongest pull-forward case of the three.

### CF-3: Route explanations: at launch, or after?

Affects: `P-03`, `H-09`

- `research/05-product/prd.md:237` &mdash; AC3-F1 requires an explanation on every generated route and every plan adjustment, at P0.
- `research/05-product/mvp-scope.md:56` &mdash; P-03 explainable generation is v1.x.

**Recommendation.** Split, and the split is already written down. gtm-plan.md line 118 resolves it: honest degradation (H-09, 0.25 person-months) ships at launch because a safety-aware product that pretends is a liability, and the richer explanation layer (P-03, 2.0) follows in v1.x. Treat AC3-F1's minimum viable form as H-09 plus a one-line constraint summary, which the route card needs anyway to satisfy the AI Act disclosure in C-11.

### CF-4: Does the paid seam exist at launch?

Affects: `P-01`, `TS-08`

- `research/05-product/prd.md:170` &mdash; AC-1 workout-type-shaped generation is P0, because the seam must exist at launch to test the paid thesis.
- `research/05-product/mvp-scope.md:126` &mdash; GD-1 launches v1 entirely free with no active paywall; TS-08 and P-01 ship together in v1.x once week-4 retention clears the bar.

**Recommendation.** Free launch. GD-1 and then DEC-011 both settled this, and the reasoning is a measurement argument rather than a pricing one: a paywall before proof contaminates the retention signal the MVP exists to produce. DEC-011 additionally made the coaching layer the only paid product, so P-01 is the first paid feature by construction and cannot precede the paywall.

## Index

| ID | Feature | Module | Release | Native pm | RICE rank | Personas |
|---|---|---|---|---:|---:|---|
| `H-07` | Route novelty | Route Generation | **MVP v1** | 1.50 | #8 | Marcus, Elena, Jake |
| `H-08` | Travel mode framing | Route Generation | **MVP v1** | 0.50 | #9 | Priya, Marcus |
| `H-09` | Honest degradation messaging | Route Generation | **MVP v1** | 0.25 | #10 | Elena, Marcus, Priya |
| `H-01` | Core constraint route generation | Route Generation | **MVP v1** | 4.50 | #11 | Marcus, Priya, Elena, Jake |
| `H-02` | Elevation constraint | Route Generation | **MVP v1** | 1.00 | #14 | Marcus, Jake |
| `H-05` | Safety-aware routing v1 | Route Generation | **MVP v1** | 4.00 | #16 | Elena, Priya, Marcus |
| `H-03` | Surface constraint | Route Generation | v1.x | 1.00 | #18 | Marcus |
| `H-04` | Street-crossing minimization | Route Generation | v1.x | 3.00 | #20 | Marcus |
| `H-06` | Weather and heat route adjustment | Route Generation | v1.x | 2.00 | #22 | Marcus, Priya |
| `H-10` | Learning loop | Route Generation | v2+ | 3.00 | #23 | Marcus |
| `N-02` | Route content library | Route Generation | ~~never~~ | 0.00 | &mdash; | &mdash; |
| `N-03` | Multi-sport breadth in the v1 era | Route Generation | ~~never~~ | 0.00 | &mdash; | &mdash; |
| `TS-05` | Audio pace and distance cues | Run Execution | **MVP v1** | 0.50 | #12 | Marcus, Jake |
| `X-01` | Voice turn-by-turn navigation | Run Execution | **MVP v1** | 3.00 | #15 | Priya, Marcus, Elena |
| `X-02` | Apple Watch companion | Run Execution | v1.x | 4.00 | #17 | Priya, Marcus |
| `X-03` | Live location sharing | Run Execution | v2+ | 2.00 | #19 | Elena |
| `N-04` | Hardware | Run Execution | ~~never~~ | 0.00 | &mdash; | &mdash; |
| `TS-03` | HealthKit and Health Connect sync | Tracking and Data | **MVP v1** | 1.00 | #1 | Marcus, Priya, Jake |
| `TS-01` | GPS run tracking | Tracking and Data | **MVP v1** | 2.00 | #5 | Marcus, Priya, Elena, Jake |
| `TS-02` | Run history and basic stats | Tracking and Data | **MVP v1** | 1.00 | #7 | Marcus, Jake |
| `TS-06` | Route save and re-run | Tracking and Data | **MVP v1** | 0.50 | #13 | Marcus, Elena |
| `TS-10` | Offline route access | Tracking and Data | v1.x | 2.00 | #24 | Priya |
| `TS-09` | GPX export and import | Tracking and Data | v1.x | 0.50 | #29 | Marcus |
| `P-01` | Training-state-aware route generation | Coaching Layer | v1.x | 4.00 | #21 | Marcus, Priya |
| `P-03` | Explainable generation | Coaching Layer | v1.x | 2.00 | #25 | Elena, Marcus |
| `P-06` | Injury-calibrated progression | Coaching Layer | v2+ | 4.00 | #26 | Jake, Marcus |
| `P-02` | Adaptive routines | Coaching Layer | v2+ | 6.00 | #27 | Marcus, Jake, Priya |
| `P-04` | Readiness and fatigue input | Coaching Layer | v2+ | 2.00 | #28 | Marcus |
| `P-05` | Race-goal progression | Coaching Layer | v2+ | 3.00 | #30 | Marcus, Jake |
| `N-05` | A best-training-plan brand war with Runna | Coaching Layer | ~~never~~ | 0.00 | &mdash; | &mdash; |
| `O-01` | Privacy architecture | Trust and Privacy | **MVP v1** | 1.50 | #2 | Elena, Marcus, Priya, Jake |
| `C-1` | Privacy zones by default | Trust and Privacy | **MVP v1** | 0.00 | &mdash; | Elena |
| `C-10` | DPIA plus AI Act classification memo | Trust and Privacy | **MVP v1** | 0.20 | &mdash; | &mdash; |
| `C-11` | AI transparency | Trust and Privacy | **MVP v1** | 0.00 | &mdash; | &mdash; |
| `C-12` | Not-medical-advice framing | Trust and Privacy | **MVP v1** | 0.10 | &mdash; | Jake |
| `C-13` | Age gating | Trust and Privacy | **MVP v1** | 0.10 | &mdash; | &mdash; |
| `C-14` | Subscription hygiene | Trust and Privacy | **MVP v1** | 0.00 | &mdash; | Marcus |
| `C-15` | Security and breach readiness | Trust and Privacy | **MVP v1** | 0.30 | &mdash; | &mdash; |
| `C-2` | Private by default | Trust and Privacy | **MVP v1** | 0.00 | &mdash; | Elena, Marcus |
| `C-3` | Granular layered consent | Trust and Privacy | **MVP v1** | 0.00 | &mdash; | Elena |
| `C-4` | Standalone Consumer Health Data Privacy Policy | Trust and Privacy | **MVP v1** | 0.15 | &mdash; | &mdash; |
| `C-5` | Data minimization and retention schedule | Trust and Privacy | **MVP v1** | 0.20 | &mdash; | &mdash; |
| `C-6` | Full deletion pipeline | Trust and Privacy | **MVP v1** | 0.40 | &mdash; | &mdash; |
| `C-7` | Data subject rights tooling | Trust and Privacy | **MVP v1** | 0.40 | &mdash; | &mdash; |
| `C-8` | No ad tech, no data sales, no cross-app tracking | Trust and Privacy | **MVP v1** | 0.10 | &mdash; | Elena |
| `C-9` | DPAs and processor inventory | Trust and Privacy | **MVP v1** | 0.15 | &mdash; | &mdash; |
| `TS-08` | Subscription and paywall infrastructure | Distribution and Commerce | v1.x | 1.50 | #3 | Marcus |
| `TS-07` | Strava share | Distribution and Commerce | **MVP v1** | 0.50 | #4 | Marcus, Jake |
| `N-01` | Social network or feed | Distribution and Commerce | ~~never~~ | 0.00 | &mdash; | &mdash; |
| `N-06` | Charging for basic loop generation | Distribution and Commerce | ~~never~~ | 0.00 | &mdash; | &mdash; |
| `TS-04` | Onboarding and permissions flow | Onboarding and Activation | **MVP v1** | 1.00 | #6 | Marcus, Priya, Elena, Jake |
| `NF-A1` | Full VoiceOver support | Platform Quality | **MVP v1** | 0.40 | &mdash; | &mdash; |
| `NF-A2` | Respect OS accessibility settings | Platform Quality | **MVP v1** | 0.15 | &mdash; | &mdash; |
| `NF-A3` | Audio and haptic as accessibility equivalents | Platform Quality | **MVP v1** | 0.10 | &mdash; | &mdash; |
| `NF-A4` | One-handed operation in motion | Platform Quality | **MVP v1** | 0.15 | &mdash; | &mdash; |
| `NF-A5` | Glare legibility | Platform Quality | **MVP v1** | 0.10 | &mdash; | &mdash; |
| `NF-A6` | No information only in small text while moving | Platform Quality | **MVP v1** | 0.10 | &mdash; | &mdash; |
| `NF-L1` | No safety guarantees, ever | Platform Quality | **MVP v1** | 0.02 | &mdash; | &mdash; |
| `NF-L2` | Name the data basis and its limits | Platform Quality | **MVP v1** | 0.03 | &mdash; | &mdash; |
| `NF-L3` | Silence is a violation | Platform Quality | **MVP v1** | 0.02 | &mdash; | &mdash; |
| `NF-L4` | No fear-based marketing | Platform Quality | **MVP v1** | 0.01 | &mdash; | &mdash; |
| `NF-L5` | Substantiate every AI claim | Platform Quality | **MVP v1** | 0.02 | &mdash; | &mdash; |
| `NF-L6` | Banned-terms linter in CI | Platform Quality | **MVP v1** | 0.15 | &mdash; | &mdash; |
| `NF-O1` | Route and tiles cached at generation | Platform Quality | **MVP v1** | 0.30 | &mdash; | &mdash; |
| `NF-O2` | Offline recording with idempotent upload | Platform Quality | **MVP v1** | 0.25 | &mdash; | &mdash; |
| `NF-O3` | Honest offline state | Platform Quality | **MVP v1** | 0.05 | &mdash; | &mdash; |
| `NF-P1` | Route generation latency | Platform Quality | **MVP v1** | 0.15 | &mdash; | &mdash; |
| `NF-P2` | Cold open to running | Platform Quality | **MVP v1** | 0.10 | &mdash; | &mdash; |
| `NF-P3` | Watch cue latency | Platform Quality | **MVP v1** | 0.05 | &mdash; | &mdash; |
| `NF-P4` | Battery | Platform Quality | **MVP v1** | 0.10 | &mdash; | &mdash; |

## Coverage by persona

| Persona | Role | Features serving them | Of those, in the MVP |
|---|---|---:|---:|
| **Marcus** | The committed amateur racer | 30 | 17 |
| **Priya** | The traveling professional | 14 | 9 |
| **Elena** | The safety-first city runner | 15 | 13 |
| **Jake** | The ambitious beginner | 14 | 11 |

## Coverage by unmet need

| Need | Evidence | Features | In the MVP |
|---|---|---:|---:|
| **N1** Safety-aware routing | Strong | 9 | 7 |
| **N2** Route novelty and personalization at home | Strong | 7 | 5 |
| **N3** Training-state-to-route connection | Strong on the gap, inferred on demand | 4 | 1 |
| **N4** Travel: where do I run, right now, from here | Moderate to strong | 3 | 2 |
| **N5** Injury-calibrated coaching that runners trust | Moderate | 5 | 0 |
| **N6** Mid-run navigation execution | Moderate | 4 | 2 |
| **N7** Plan flexibility when life disrupts training | Moderate | 2 | 0 |
| **N8** Urban doorstep running as a design center | Moderate | 10 | 8 |
| **N9** Weather and heat adaptation applied to the route | Weak to moderate | 1 | 0 |
| **N10** Trustworthy subscription mechanics | Moderate as pattern, weak as need | 1 | 0 |
| **N11** Quiet routes for self-conscious beginners | Weak | 0 | 0 |

A need with strong evidence and nothing in the MVP is a gap worth arguing about. N11 is intentionally unserved: it is on the do-not-chase list.

## Full detail

### Route Generation

*The engine. The single reason the product exists.* &mdash; 12 items, 20.75 native person-months.

#### `H-07` Route novelty

**Roads you have not run. History-aware generation, and the daily retention engine at home.**

A 'new ground' preference that prefers unrun segments using Waypoint's own run history for this user, held on device first. The posture is 'never the same loop twice unless asked', with a repeat-a-favorite escape hatch. This is the second-strongest-evidenced need and the reason a runner opens the app on an ordinary Tuesday from their own front door, which is what separates a retention product from a travel utility. A brand-new user has no history, so novelty is silently inapplicable and the engine notes it is still learning.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Route Generation |
| **Effort, iOS-native** | 1.50 pm |
| **Effort, React Native** | 1.80 pm |
| **RICE** | rank #8, score 6,400 (reach 6,000, impact 2, confidence 80%, effort 1.5) |
| **Personas** | Marcus (primary), Elena (primary), Jake (secondary) |
| **Needs** | N2 Route novelty and personalization at home, N8 Urban doorstep running as a design center |
| **Jobs** | FJ3 Get novelty and variety from my own front door |
| **Emotional jobs** | Novelty and exploration joy |
| **Depends on** | `H-01` Core constraint route generation, `TS-01` GPS run tracking |
| **Blocks** | `H-10` |
| **Requirement IDs** | `RG-F6` |

**What it actually does**

- Unrun-segment preference weighting from personal run history
- History held on device first, synced rather than server-first
- Never-the-same-loop-twice default posture
- Repeat-a-favorite escape hatch
- Graceful inapplicability for accounts with no history yet
- GraphHopper round_trip seed variation to diversify candidates

**Done means**

- A user with ten or more recorded runs receives measurably higher unrun-segment share than a fresh account for the same request
- A fresh account generates normally with novelty noted as still learning, never as applied

**Integrations** &mdash; GraphHopper round_trip.seed; First-party run history store

**Risks**

- Novelty depends on accumulated history, so its value is lowest exactly when a new user is deciding whether to stay

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:37`, `research/05-product/mvp-scope.md:34`, `research/05-product/prd.md:97`

#### `H-08` Travel mode framing

**Instant orientation in an unfamiliar city. The activation moment and the demo story, at near-zero marginal cost.**

Technically the same engine, because start-anywhere is already a core capability. Travel mode is the packaging: detecting a start point far from the user's home area, offering one-tap 'run here' with saved defaults applied, defaulting safety awareness on in unfamiliar areas, and caching aggressively. The H1 reframe accepted in DEC-006 is precise about its role: travel is how users arrive and how the product demos, while safety and home novelty are why they stay. Half a person-month for the sharpest test of the engine's promise.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Route Generation |
| **Effort, iOS-native** | 0.50 pm |
| **Effort, React Native** | 0.60 pm |
| **RICE** | rank #9, score 6,000 (reach 2,000, impact 2, confidence 75%, effort 0.5) |
| **Personas** | Priya (primary), Marcus (secondary) |
| **Needs** | N4 Travel: where do I run, right now, from here |
| **Jobs** | FJ1 Find a trustworthy route in an unfamiliar place |
| **Emotional jobs** | Confidence in unfamiliar places |
| **Depends on** | `H-01` Core constraint route generation |
| **Requirement IDs** | `TM-F1`, `TM-F2`, `TM-F3`, `TM-F4` |

**What it actually does**

- Far-from-home detection offering one-tap generation with saved defaults
- Zero-configuration first route in an unfamiliar city
- Safety awareness defaulted on in unfamiliar areas
- Generation-to-started-run in under 30 seconds
- Aggressive on-device caching of the generated route and its corridor

**Done means**

- A first-time-in-city user reaches a started, navigable run within 30 seconds of app open, measured at p75
- The home-area definition used for far-from-home detection is privacy-safe and consistent with privacy zones

**Integrations** &mdash; Platform geocoders

**Risks**

- Defaulting safety awareness on in unfamiliar areas interacts with the free-tier boundary; DEC-011 resolved it by making all routing constraints free permanently

**Still open**

- What distance from home triggers travel framing, and is the home-area definition privacy-safe

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:38`, `research/05-product/mvp-scope.md:36`, `research/05-product/prd.md:150`

#### `H-09` Honest degradation messaging

**When no good route exists, say so and name the blockers. The cheapest trust feature in the catalog.**

Engine-wide behavior rather than a screen: when any data source is unavailable the interface states which constraint could not be honored, and when nothing satisfies the active constraints it says 'no good route meets your constraints right now' with the specific blockers and offers relaxation choices. It never ships a pretender route. At 0.25 person-months this is the highest trust-per-unit-effort item in the entire catalog, and for a product making safety-adjacent claims it is closer to a liability control than a feature.

> **Documents disagree (CF-3).** Route explanations: at launch, or after? Recommendation: Split, and the split is already written down. gtm-plan.md line 118 resolves it: honest degradation (H-09, 0.25 person-months) ships at launch because a safety-aware product that pretends is a liability, and the richer explanation layer (P-03, 2.0) follows in v1.x. Treat AC3-F1's minimum viable form as H-09 plus a one-line constraint summary, which the route card needs anyway to satisfy the AI Act disclosure in C-11.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Route Generation |
| **Effort, iOS-native** | 0.25 pm |
| **Effort, React Native** | 0.30 pm |
| **RICE** | rank #10, score 5,600 (reach 2,000, impact 1, confidence 70%, effort 0.25) |
| **Personas** | Elena (primary), Marcus (secondary), Priya (secondary) |
| **Needs** | N1 Safety-aware routing |
| **Jobs** | FJ2 Find a route that is safe at this hour |
| **Emotional jobs** | Feel safe, not brave |
| **Depends on** | `H-01` Core constraint route generation |
| **Blocks** | `P-03` |
| **Requirement IDs** | `RG-F10` |

**What it actually does**

- Per-constraint unavailability reporting on every route card
- No-route-found state naming the specific blocking constraints
- Relaxation choices offered rather than a dead end
- Never presenting a non-conforming route as conforming
- Copy governed by the safety-claim language rules

**Done means**

- Constraints no local route can satisfy show the message naming unmet constraints and offer relaxation, with no unlabeled non-conforming route returned
- Every degradation string is VoiceOver-accessible

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: explicitly NOT cut.

Sources: `research/05-product/rice-prioritization.md:39`, `research/05-product/mvp-scope.md:37`, `research/05-product/prd.md:115`

#### `H-01` Core constraint route generation

**Generate a loop or out-and-back from any start point that satisfies a target distance, the product's entire reason for existing.**

The hero primitive. Given a start point (current GPS location or a dropped pin) and a free-form target distance, return one to three candidate routes that close the loop within tolerance, each with a map preview, distance, elevation profile and a summary of which constraints shaped it. Free-form distance rather than presets is a deliberate differentiator: Strava's preset-only distances are a documented weakness. Start-anywhere is what makes travel mode possible without a second engine.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Route Generation |
| **Effort, iOS-native** | 4.50 pm |
| **Effort, React Native** | 5.40 pm |
| **Walking-skeleton slice** | 2.30 pm &mdash; Current location start, target distance, one round-trip route on screen with map preview, distance and elevation profile. No multi-candidate ranking, no regenerate, no other constraints. |
| **RICE** | rank #11, score 4,800 (reach 9,000, impact 3, confidence 80%, effort 4.5) |
| **Personas** | Marcus (primary), Priya (primary), Elena (primary), Jake (secondary) |
| **Needs** | N2 Route novelty and personalization at home, N4 Travel: where do I run, right now, from here, N8 Urban doorstep running as a design center |
| **Jobs** | FJ1 Find a trustworthy route in an unfamiliar place, FJ3 Get novelty and variety from my own front door, FJ9 Fit the run into the time I actually have |
| **Blocks** | `H-02`, `H-03`, `H-04`, `H-05`, `H-06`, `H-07`, `H-08`, `H-09`, `P-01`, `P-03`, `TS-06`, `TS-10`, `X-01` |
| **Requirement IDs** | `RG-F1`, `RG-F2`, `RG-F3`, `RG-F5`, `RG-F7`, `RG-F9`, `RG-F11` |

**What it actually does**

- Round-trip loop generation from a single start point at a target distance
- Out-and-back generation where a loop is not achievable
- Free-form distance input in the user's unit preference, not presets
- One to three candidate routes per request, ranked
- Regenerate without re-entering constraints, never repeating a route already offered in the session
- Constraint conflict resolution by stated priority order, with the relaxed constraint named
- Start point treated as sensitive end to end, obfuscated before it leaves the device
- Works over cellular with payloads sized for hotel and roaming conditions

**Done means**

- A 10 km target from a mapped urban start point returns 1 to 3 routes each within 9.5 to 10.5 km, p95 under 15 seconds on cellular
- Constraints no local route can satisfy produce the honest-degradation message naming the unmet constraints, never an unlabeled non-conforming route
- With location permission denied, pin-drop generation works and everything functions except current-location start

**Integrations** &mdash; Self-hosted GraphHopper on Hetzner (round_trip algorithm); Geofabrik OSM extracts plus daily diffs; AWS Terrain Tiles / Copernicus GLO-30 elevation; Platform geocoders

**Risks**

- GraphHopper custom models are officially beta, and node-level crossing penalties likely need Java-level work

**Still open**

- The plus or minus 5 percent distance tolerance and the three-candidate count are placeholders to tune in beta

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:40`, `research/05-product/mvp-scope.md:32`, `research/05-product/prd.md:106`

#### `H-02` Elevation constraint

**Target or avoid climb, the cheapest real constraint beyond distance.**

A preference (flat, rolling, hilly) with an optional total-gain cap, applied as a weighting on the generation request. This is what makes the phrase 'constraint-based' true rather than marketing, at one person-month. When a digital elevation model tile is missing for the area, the engine says elevation data is unavailable here, generates by distance alone, and flags the route as elevation-unverified rather than silently ignoring the preference.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Route Generation |
| **Effort, iOS-native** | 1.00 pm |
| **Effort, React Native** | 1.20 pm |
| **RICE** | rank #14, score 3,750 (reach 5,000, impact 1, confidence 75%, effort 1.0) |
| **Personas** | Marcus (primary), Jake (secondary) |
| **Needs** | N2 Route novelty and personalization at home, N8 Urban doorstep running as a design center |
| **Jobs** | FJ3 Get novelty and variety from my own front door, FJ4 Match the route to today's workout |
| **Depends on** | `H-01` Core constraint route generation |
| **Requirement IDs** | `RG-F1` |

**What it actually does**

- Flat, rolling and hilly preference presets
- Optional total elevation gain cap
- Elevation profile rendered on every route card
- Explicit elevation-unverified flag where DEM coverage is missing

**Done means**

- Selecting flat versus hilly for the same start and distance measurably changes total gain
- A start point with no DEM coverage generates successfully with the unavailability stated and the route flagged

**Integrations** &mdash; AWS Terrain Tiles plus Copernicus GLO-30; OSM way tags

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:43`, `research/05-product/mvp-scope.md:33`, `research/05-product/prd.md:91`

#### `H-05` Safety-aware routing v1

**Lighting, populated areas and time of day as first-class routing constraints. The strongest-evidenced need in the entire program.**

The constraint no competitor offers. Lighting from OSM lit tags, population proxy from point-of-interest and business density with open-hours data, and an on-device solar calculation for daylight, combined into a routing weight that rises automatically after civil dusk without the user configuring anything. Explicitly not crime data in v1, because of unresolved redlining exposure. Framing is 'safety-aware' and never 'safe' at every scope level, which is a liability rule rather than a copy preference. Where coverage falls below a usable threshold the toggle reports that it cannot be honored here; an unscored route is never presented as safety-checked.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Route Generation |
| **Effort, iOS-native** | 4.00 pm |
| **Effort, React Native** | 4.80 pm |
| **RICE** | rank #16, score 2,625 (reach 5,000, impact 3, confidence 70%, effort 4.0) |
| **Personas** | Elena (primary), Priya (primary), Marcus (secondary) |
| **Needs** | N1 Safety-aware routing, N8 Urban doorstep running as a design center |
| **Jobs** | FJ2 Find a route that is safe at this hour, FJ1 Find a trustworthy route in an unfamiliar place |
| **Emotional jobs** | Feel safe, not brave |
| **Depends on** | `H-01` Core constraint route generation |
| **Requirement IDs** | `RG-F8`, `RG-F10` |

**What it actually does**

- OSM lit-tag weighting for street lighting
- Population proxy from POI and business density with open-hours awareness
- On-device sunrise and sunset calculation, no network required
- Automatic time-of-day weighting after civil dusk with no user configuration
- Coverage-threshold detection with an explicit limited-coverage notice
- Per-area availability reporting when the constraint cannot be honored

**Done means**

- Dusk at the start point measurably weights lit and populated ways versus the same request at noon, verifiable in engine telemetry
- Lighting coverage below threshold displays the limited-coverage notice, and no route is presented as safety-scored
- No user-facing surface anywhere uses the banned safety-guarantee vocabulary

**Integrations** &mdash; OSM lit tags; POI and business-hours data; On-device solar calculation

**Risks**

- Scope is gated by GD-3: if the month-1 spike fails, launch with time-of-day and daylight heuristics plus honest degradation and move the full data layer to v1.x
- Redlining and fairness exposure: safety scoring can systematically steer users away from certain neighborhoods even without crime data. Needs counsel plus a fairness design review before launch
- Data licensing for safety-critical use is unaudited

**Still open**

- Which metros get constraint coverage at launch, and what is the coverage-threshold number that flips a constraint to unavailable

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: explicitly NOT cut.

Sources: `research/05-product/rice-prioritization.md:45`, `research/05-product/mvp-scope.md:35`, `research/05-product/prd.md:94`

#### `H-03` Surface constraint

**Prefer paved, unpaved or mixed surfaces, or avoid trails entirely.**

A preference applied against OpenStreetMap surface and highway tags. The honest-degradation obligation bites hard here, because OSM surface tagging is sparse and uneven: where coverage is partial the engine states so, prefers tagged ways, and never presents an untagged way as confirmed surface. Cheap to build, but serving a need with weaker evidence than the constraints ahead of it.

> **Documents disagree (CF-2).** All ten routing constraints at launch, or a subset? Recommendation: Subset. The PRD enumerates the constraint model, which is the right thing for an engine specification to do; it does not follow that every constraint ships at launch. Distance, elevation, novelty, safety and daylight make 'constraint-based' true. Surface, crossings and weather add 6.0 person-months for the least-evidenced needs in the set (N9 is rated weak to moderate). Note that street-crossing minimization is the one users asked for in their own words, so it has the strongest pull-forward case of the three.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Route Generation |
| **Effort, iOS-native** | 1.00 pm |
| **Effort, React Native** | 1.20 pm |
| **RICE** | rank #18, score 1,050 (reach 3,000, impact 0.5, confidence 70%, effort 1.0) |
| **Personas** | Marcus (primary) |
| **Needs** | N2 Route novelty and personalization at home |
| **Jobs** | FJ4 Match the route to today's workout |
| **Depends on** | `H-01` Core constraint route generation |
| **Requirement IDs** | `RG-F1` |

**What it actually does**

- Paved, unpaved, mixed and avoid-trails preferences
- Surface breakdown shown per candidate route
- Partial-coverage notice where OSM tagging is sparse

**Done means**

- Avoid-trails returns routes with measurably lower unpaved share in an area with mixed tagging
- An area with sparse surface tagging shows the partial-coverage notice and makes no confirmed-surface claim

**Integrations** &mdash; OSM surface and highway tags

**What pulls it forward.** Beta users request it organically. Cheap enough that moderate demand suffices.

**Risks**

- OSM surface tagging density varies enormously between metros, so the feature's usefulness is geography-dependent

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:47`, `research/05-product/mvp-scope.md:54`, `research/05-product/prd.md:92`

#### `H-04` Street-crossing minimization

**Uninterrupted stretches for tempo and interval work, built on a proprietary crossing graph.**

A toggle, plus automatic weighting from workout context, that penalizes intersections and signalized crossings. This is the constraint runners articulated in their own words, and the only one in the set backed by a verbatim community complaint. It also requires the most novel data work: a crossing graph derived from OSM intersections, road class and signal tags, which is assumption A3 and the riskiest technical unknown in the plan. Where the graph is not built for a region the toggle is greyed out with 'not yet available here' rather than producing a fake score.

> **Documents disagree (CF-2).** All ten routing constraints at launch, or a subset? Recommendation: Subset. The PRD enumerates the constraint model, which is the right thing for an engine specification to do; it does not follow that every constraint ships at launch. Distance, elevation, novelty, safety and daylight make 'constraint-based' true. Surface, crossings and weather add 6.0 person-months for the least-evidenced needs in the set (N9 is rated weak to moderate). Note that street-crossing minimization is the one users asked for in their own words, so it has the strongest pull-forward case of the three.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Route Generation |
| **Effort, iOS-native** | 3.00 pm |
| **Effort, React Native** | 3.60 pm |
| **RICE** | rank #20, score 800 (reach 4,000, impact 1, confidence 60%, effort 3.0) |
| **Personas** | Marcus (primary) |
| **Needs** | N3 Training-state-to-route connection, N8 Urban doorstep running as a design center |
| **Jobs** | FJ10 Avoid interruptions and street crossings, FJ4 Match the route to today's workout |
| **Depends on** | `H-01` Core constraint route generation |
| **Requirement IDs** | `RG-F1` |

**What it actually does**

- Crossing-count penalty as a generation weight
- Automatic activation for tempo and interval workout types
- Crossing count displayed per candidate route
- Region-level availability gating with an explicit unavailable state

**Done means**

- Enabling the constraint measurably reduces crossing count for the same start and distance
- A region with no crossing graph shows the toggle disabled with the reason, and never reports a crossing score

**Integrations** &mdash; Proprietary crossing graph derived from OSM; GraphHopper custom model with ch.disable

**What pulls it forward.** The month-1 A3 spike proves crossing graphs cheap to build; or beta feedback names interrupted runs a top-three complaint.

**Risks**

- Node-level crossing penalties likely require Java-level work inside GraphHopper rather than configuration
- The crossing graph is per-region build work, so coverage does not generalize for free

**Still open**

- Buildability at this team's scale is assumption A3, answered by the month-1 spike

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:49`, `research/05-product/mvp-scope.md:52`, `research/05-product/prd.md:93`

#### `H-06` Weather and heat route adjustment

**Shade preference, exposure avoidance and cut-short options in heat, rather than a temperature readout.**

Automatic adjustment with user override, driven by temperature, humidity, UV and wind from the weather API plus an OSM tree-cover and land-use shade proxy. The distinction that matters: every competitor shows the weather, none routes around it. When the weather API is down the engine generates without adjustment and says so; when the shade proxy is unavailable it omits the shade claim from the explanation rather than hedging it.

> **Documents disagree (CF-2).** All ten routing constraints at launch, or a subset? Recommendation: Subset. The PRD enumerates the constraint model, which is the right thing for an engine specification to do; it does not follow that every constraint ships at launch. Distance, elevation, novelty, safety and daylight make 'constraint-based' true. Surface, crossings and weather add 6.0 person-months for the least-evidenced needs in the set (N9 is rated weak to moderate). Note that street-crossing minimization is the one users asked for in their own words, so it has the strongest pull-forward case of the three.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Route Generation |
| **Effort, iOS-native** | 2.00 pm |
| **Effort, React Native** | 2.40 pm |
| **RICE** | rank #22, score 750 (reach 3,000, impact 1, confidence 50%, effort 2.0) |
| **Personas** | Marcus (primary), Priya (secondary) |
| **Needs** | N9 Weather and heat adaptation applied to the route |
| **Jobs** | FJ6 Adjust the route for heat and weather |
| **Depends on** | `H-01` Core constraint route generation |
| **Requirement IDs** | `RG-F1` |

**What it actually does**

- Temperature, humidity, UV and wind inputs to generation weights
- Shade preference from OSM tree cover and land use
- Exposure avoidance in high-UV conditions
- Cut-short route options offered in dangerous heat
- User override of every automatic adjustment

**Done means**

- A high-heat forecast measurably increases shaded-way share versus the same request in mild conditions
- Weather API unavailability generates a route with the missing adjustment stated

**Integrations** &mdash; Apple WeatherKit REST (both platforms); Open-Meteo commercial fallback; OSM tree cover and land use

**What pulls it forward.** The launch summer cohort shows heat-hour generation spikes; or an acceptance-rate test slot opens.

**Risks**

- WeatherKit on Android runs on Apple's goodwill rather than a contractual guarantee

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:52`, `research/05-product/mvp-scope.md:53`, `research/05-product/prd.md:95`

#### `H-10` Learning loop

**A preference model trained on which generated routes actually got run and completed.**

The compounding advantage, and the reason the data posture matters from day one. Completed runs, accepted versus rejected candidates, and deviation behavior feed a per-user preference model that improves generation over time. Deferred not on value but on prerequisite: before there is repeat-generation volume the model has nothing to learn from. On-device first, with segment-level aggregation only later.

| | |
|---|---|
| **Release** | v2+ |
| **Module** | Route Generation |
| **Effort, iOS-native** | 3.00 pm |
| **Effort, React Native** | 3.60 pm |
| **RICE** | rank #23, score 667 (reach 4,000, impact 1, confidence 50%, effort 3.0) |
| **Personas** | Marcus (primary) |
| **Needs** | N2 Route novelty and personalization at home |
| **Jobs** | FJ3 Get novelty and variety from my own front door |
| **Depends on** | `H-07` Route novelty, `TS-01` GPS run tracking |

**What it actually does**

- Accept and reject signals per generated candidate
- Completion and deviation behavior as implicit feedback
- Per-user preference weights that shift generation over time
- On-device model first, aggregation deferred
- Explainable influence, so learned preferences appear in the route explanation

**Done means**

- A user with sustained generation history receives candidates measurably closer to their historical acceptance pattern than a fresh account
- Learned influence is disclosed in the route explanation rather than applied invisibly

**What pulls it forward.** Repeat-generation volume creates the training data. Before scale it has nothing to learn from.

**Risks**

- A preference model that learns from a thin history can entrench a bad early impression

**What each document says.** `mvp-scope.md`: v2. `prd.md`: unlisted. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:53`, `research/05-product/mvp-scope.md:67`

#### `N-02` Route content library

**Generate, do not curate. RunGo's territory.**

A curated library is a content operation with editorial cost that scales linearly with geography. Generation scales with code. Choosing curation would be choosing a different company.

> **Locked.** Ruled out by DEC-006's NOT list. Reopening it needs a superseding decision record, not a scenario toggle.

| | |
|---|---|
| **Release** | ~~never~~ |
| **Module** | Route Generation |
| **Effort, iOS-native** | 0.00 pm |
| **Effort, React Native** | 0.00 pm |

**What each document says.** `mvp-scope.md`: never. `prd.md`: explicit non-goal. `team-roadmap.md`: not in scope at any horizon.

Sources: `research/05-product/mvp-scope.md:76`, `research/04-synthesis/concept.md`

#### `N-03` Multi-sport breadth in the v1 era

**Focus is the moat. Expansion is a later business decision, not a feature.**

Cycling, hiking and walking are the same engine with different constraint weights, which makes them tempting and cheap-looking. They are still a distraction from proving one hypothesis with one segment in one metro.

> **Locked.** Ruled out by DEC-006's NOT list. Reopening it needs a superseding decision record, not a scenario toggle.

| | |
|---|---|
| **Release** | ~~never~~ |
| **Module** | Route Generation |
| **Effort, iOS-native** | 0.00 pm |
| **Effort, React Native** | 0.00 pm |

**What each document says.** `mvp-scope.md`: never. `prd.md`: explicit non-goal. `team-roadmap.md`: not in scope at any horizon.

Sources: `research/05-product/mvp-scope.md:76`, `research/04-synthesis/concept.md`

### Run Execution

*Turning a generated route into a run that actually happens.* &mdash; 5 items, 9.50 native person-months.

#### `TS-05` Audio pace and distance cues

**Spoken splits and progress, expected by every headphone runner and trivial on top of tracking.**

Periodic spoken announcements of distance, pace and elapsed time at a configurable interval, sharing the audio session and ducking behavior with turn-by-turn navigation. Half a person-month because the hard parts, audio session management and ducking, are already paid for by voice navigation.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Run Execution |
| **Effort, iOS-native** | 0.50 pm |
| **Effort, React Native** | 0.60 pm |
| **Walking-skeleton slice** | 0.30 pm &mdash; Basic pace and distance announcements at a fixed interval. |
| **RICE** | rank #12, score 4,800 (reach 6,000, impact 0.5, confidence 80%, effort 0.5) |
| **Personas** | Marcus (primary), Jake (secondary) |
| **Needs** | N6 Mid-run navigation execution |
| **Jobs** | FJ11 Track and log my running life |
| **Depends on** | `TS-01` GPS run tracking |
| **Requirement IDs** | `EX1-F1` |

**What it actually does**

- Configurable announcement interval by distance or time
- Distance, pace and elapsed-time announcements
- Shared audio session and ducking with turn cues
- Independently silenceable from turn cues

**Done means**

- Announcements fire at the configured interval and duck rather than stop the user's audio
- Silencing pace cues leaves turn cues audible and vice versa

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:41`, `research/05-product/mvp-scope.md:26`

#### `X-01` Voice turn-by-turn navigation

**Hands-free execution of a generated route. Generation without execution strands the value.**

Spoken turn cues with configurable verbosity that duck rather than pause the user's music or podcast, off-route detection with calm rerouting, screen-locked operation, and haptic cues as a non-audio alternative. The competitive insight is specific: turn-by-turn audio for runners is a solved problem at indie scale, but nobody has paired it with generation. The complaint Waypoint must not reproduce is Garmin's unsilenceable prompts, which is why verbosity is configurable and rerouting prompts exactly once rather than scolding.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Run Execution |
| **Effort, iOS-native** | 3.00 pm |
| **Effort, React Native** | 3.60 pm |
| **Walking-skeleton slice** | 1.50 pm &mdash; Turn cues through headphones plus rejoin guidance. No verbosity configuration, no reroute-to-distance, no haptic alternative. |
| **RICE** | rank #15, score 3,267 (reach 7,000, impact 2, confidence 70%, effort 3.0) |
| **Personas** | Priya (primary), Marcus (primary), Elena (secondary) |
| **Needs** | N6 Mid-run navigation execution |
| **Jobs** | FJ7 Execute an unfamiliar route hands-free |
| **Emotional jobs** | Confidence in unfamiliar places |
| **Depends on** | `H-01` Core constraint route generation, `TS-01` GPS run tracking |
| **Blocks** | `TS-10`, `X-02`, `X-03` |
| **Requirement IDs** | `EX1-F1`, `EX1-F2`, `EX1-F3`, `EX1-F4`, `EX1-F5` |

**What it actually does**

- Spoken turn cues with all-cues, turns-only and off verbosity settings
- Audio ducking rather than pausing for music and podcasts
- Off-route detection with a single calm reroute prompt cycle
- Reroute back to path or recalculated to target distance
- Full operation with the screen locked, over any connected audio device
- Haptic turn cues as an accessibility and quiet-running alternative

**Done means**

- A scripted 5 km route delivers every turn cue between 80 and 30 metres before the turn with zero missed turns
- Going off-route triggers exactly one reroute prompt cycle and guidance resumes on the new path
- Music ducking verified against Apple Music, Spotify and a podcast app

**Integrations** &mdash; Ferrostar or equivalent voice-guidance engine; iOS background location mode; Android foreground service with location type

**Risks**

- Voice-guidance engine now has to answer for two platforms rather than one, per DEC-010

**Still open**

- Reroute-to-distance versus reroute-to-original-path as the default

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:44`, `research/05-product/mvp-scope.md:38`, `research/05-product/prd.md:267`

#### `X-02` Apple Watch companion

**Glanceable distance, pace and next-turn cues on the wrist, with haptics, mirroring the phone session.**

The wrist is where a runner actually looks, and for Priya it is what keeps the phone in her pocket in a strange city. Scoped as mirroring rather than a standalone watch engine: the phone holds the session and the watch renders it, with wrist haptics for turns. Standalone watch-only execution is a separate and much larger effort held at P2. GD-2 deferred this to fast-follow with development starting during beta, and set an explicit tripwire that pulls it into v1.

> **Documents disagree (CF-1).** Apple Watch companion: launch-critical or fast-follow? Recommendation: Fast-follow. GD-2 already decided this on the record, and the reasoning holds independently of team size: voice through headphones tests the execution hypothesis at 3.0 person-months, while the Watch adds 4.0 and watchOS risk without changing what the MVP proves. The PRD's P0 predates that gate decision. Its tripwire stands: a screener showing watch-dominant execution above 60 percent pulls it forward.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Run Execution |
| **Effort, iOS-native** | 4.00 pm |
| **Effort, React Native** | 4.80 pm |
| **RICE** | rank #17, score 1,788 (reach 5,500, impact 2, confidence 65%, effort 4.0) |
| **Personas** | Priya (primary), Marcus (primary) |
| **Needs** | N6 Mid-run navigation execution |
| **Jobs** | FJ7 Execute an unfamiliar route hands-free |
| **Depends on** | `X-01` Voice turn-by-turn navigation |
| **Requirement IDs** | `EX2-F1`, `EX2-F2` |

**What it actually does**

- Elapsed distance, pace and next-turn cue mirrored from the phone session
- Wrist haptics for turn cues
- Direct-sunlight legibility with no mid-run interaction beyond raise-to-look
- Session survival across phone screen lock and backgrounding

**Done means**

- Turn haptic fires on the wrist within one second of the phone cue
- The watch session survives phone screen lock and backgrounding for a full run

**Integrations** &mdash; HealthKit plus WorkoutKit; watchOS session mirroring

**What pulls it forward.** Fires by default at launch plus 30, with the build starting during beta. Pulls into v1 only if the screener survey shows watch-dominant execution above roughly 60 percent, which pushes launch out by a month.

**Risks**

- Adds watchOS risk to the critical path without changing what the MVP proves
- Wear OS is a separate post-traction effort, so this does not deliver parity across platforms

**Still open**

- watchOS mirroring versus a native watch workout session is a stack decision

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:46`, `research/05-product/mvp-scope.md:50`, `research/05-product/prd.md:283`

#### `X-03` Live location sharing

**Beacon-style live run sharing to one trusted contact, opt-in per run and auto-expiring.**

One of Elena's named jobs: let someone I trust follow my run live. Also the catalog's sharpest privacy tension, because the same mechanism that reassures a trusted contact is a deanonymization and stalking vector, and Strava's Flyby history is the cautionary precedent. Held at v2 with an unusually explicit condition: build it only if safety interviews show Strava Beacon and Find My leave a real gap, and otherwise never, because rebuilding trusted incumbents is not a good use of this team.

| | |
|---|---|
| **Release** | v2+ |
| **Module** | Run Execution |
| **Effort, iOS-native** | 2.00 pm |
| **Effort, React Native** | 2.40 pm |
| **RICE** | rank #19, score 825 (reach 3,000, impact 1, confidence 55%, effort 2.0) |
| **Personas** | Elena (primary) |
| **Needs** | N1 Safety-aware routing |
| **Jobs** | FJ2 Find a route that is safe at this hour |
| **Emotional jobs** | Feel safe, not brave |
| **Depends on** | `X-01` Voice turn-by-turn navigation, `O-01` Privacy architecture |
| **Requirement IDs** | `EX2-F3` |

**What it actually does**

- Opt-in per run, never default-on
- Single trusted contact rather than a broadcast surface
- Automatic expiry at run end
- Privacy-zone obfuscation applied to the shared view

**Done means**

- Sharing requires explicit per-run opt-in and expires automatically at run end with no lingering link
- A shared view never reveals a true in-zone start point

**What pulls it forward.** Safety interviews show Strava Beacon and Find My leave a real gap. Otherwise never.

**Risks**

- Creates a deanonymization and stalking vector that may outweigh its safety value; needs a privacy design review before any commitment
- Interacts directly with private-by-default and privacy zones

**Still open**

- Does live sharing's safety value survive the privacy design review

**What each document says.** `mvp-scope.md`: v2. `prd.md`: P1 pending privacy review. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:48`, `research/05-product/mvp-scope.md:68`, `research/05-product/prd.md:296`

#### `N-04` Hardware

**Capital and competence mismatch.**

Stated plainly in the locked concept. Nothing about this team's composition or capital position makes hardware sane.

> **Locked.** Ruled out by DEC-006's NOT list. Reopening it needs a superseding decision record, not a scenario toggle.

| | |
|---|---|
| **Release** | ~~never~~ |
| **Module** | Run Execution |
| **Effort, iOS-native** | 0.00 pm |
| **Effort, React Native** | 0.00 pm |

**What each document says.** `mvp-scope.md`: never. `prd.md`: explicit non-goal. `team-roadmap.md`: not in scope at any horizon.

Sources: `research/05-product/mvp-scope.md:76`, `research/04-synthesis/concept.md`

### Tracking and Data

*Recording the run and owning the history the engine learns from.* &mdash; 6 items, 7.00 native person-months.

#### `TS-03` HealthKit and Health Connect sync

**Write runs to the platform health store and read activity back. The locked data posture, accruing the moat from day one.**

The device health store is Waypoint's system of record, which is a deliberate strategic choice rather than a convenience: Strava's API bans AI and machine-learning use of its data, and Garmin's developer program is paused, so platform health is the only durable intake. Highest RICE score in the catalog at rank 1. Reading activity history also seeds novelty for users who ran before installing Waypoint. Health data is GDPR Article 9 special category, so explicit separate consent is required before any read.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Tracking and Data |
| **Effort, iOS-native** | 1.00 pm |
| **Effort, React Native** | 1.20 pm |
| **Walking-skeleton slice** | 0.40 pm &mdash; Write the workout to HealthKit on finish. No read, no readiness signals. |
| **RICE** | rank #1, score 14,450 (reach 8,500, impact 2, confidence 85%, effort 1.0) |
| **Personas** | Marcus (primary), Priya (secondary), Jake (secondary) |
| **Needs** | N3 Training-state-to-route connection, N8 Urban doorstep running as a design center |
| **Jobs** | FJ11 Track and log my running life |
| **Depends on** | `TS-01` GPS run tracking |
| **Blocks** | `P-01`, `P-04` |
| **Requirement IDs** | `EX3-F4`, `AC1-F2` |

**What it actually does**

- Write completed runs as workouts to HealthKit and Health Connect
- Read activity history to seed novelty and context
- Explicit granular consent before any health read, separately withdrawable
- Degraded mode on consent withdrawal that never breaks route generation

**Done means**

- A completed run appears in the platform health store with correct distance, duration and route
- Revoking health access degrades dependent features with the correct notice, with no crash and no stale claims

**Integrations** &mdash; HealthKit plus WorkoutKit (iOS entitlement); Health Connect (Android granular permissions plus Play declaration)

**Risks**

- Garmin Connect writing into Health Connect is unverified; H6 was verified for HealthKit only, and this must be checked before Android work begins

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:32`, `research/05-product/mvp-scope.md:28`

#### `TS-01` GPS run tracking

**Record pace, distance, time and the GPS trace. A running app that cannot record a run is not a running app.**

Table stakes verified across all ten competitors, and a prerequisite rather than a differentiator. It matters here for a second reason: the recorded run is what feeds novelty history and eventually the learning loop, so the tracking surface is also the data-moat intake. Recording is fully offline, with upload queued and retried idempotently.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Tracking and Data |
| **Effort, iOS-native** | 2.00 pm |
| **Effort, React Native** | 2.40 pm |
| **Walking-skeleton slice** | 1.20 pm &mdash; Start run, GPS tracking, run summary. No advanced stats, no history views beyond a simple list. |
| **RICE** | rank #5, score 9,000 (reach 10,000, impact 2, confidence 90%, effort 2.0) |
| **Personas** | Marcus (primary), Priya (primary), Elena (primary), Jake (primary) |
| **Needs** | N8 Urban doorstep running as a design center |
| **Jobs** | FJ11 Track and log my running life |
| **Blocks** | `H-07`, `H-10`, `TS-02`, `TS-03`, `TS-05`, `TS-07`, `TS-09`, `X-01` |
| **Requirement IDs** | `EX1-F3` |

**What it actually does**

- GPS trace capture with pace, distance and elapsed time
- Background recording with the screen off during an active run
- Fully offline recording with idempotent queued upload
- Workout session compatible with the platform health store
- Recorded runs feed novelty history

**Done means**

- A full run records accurately with the screen locked and the app backgrounded
- Recording continues with no connectivity and uploads once without duplication when connectivity returns

**Integrations** &mdash; iOS background location mode; Android foreground service with location type and fine-location declaration

**Risks**

- Play Store fine-location declaration review is a long-lead item that must start in month 1 of the build

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:34`, `research/05-product/mvp-scope.md:25`, `research/05-product/prd.md:269`

#### `TS-02` Run history and basic stats

**Somewhere for the return visit to land.**

A list of recorded runs with per-run detail and simple aggregate statistics. Modest on its own, but the return visit needs something to return to, and history is also the visible face of the novelty engine: seeing which roads you have covered is what makes 'roads you have not run' legible as a promise rather than a claim.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Tracking and Data |
| **Effort, iOS-native** | 1.00 pm |
| **Effort, React Native** | 1.20 pm |
| **RICE** | rank #7, score 7,200 (reach 8,000, impact 1, confidence 90%, effort 1.0) |
| **Personas** | Marcus (primary), Jake (secondary) |
| **Needs** | N2 Route novelty and personalization at home |
| **Jobs** | FJ11 Track and log my running life |
| **Emotional jobs** | Feel like a real runner |
| **Depends on** | `TS-01` GPS run tracking |

**What it actually does**

- Chronological run list with per-run detail
- Aggregate distance, time and pace statistics
- Route replay on a map
- Coverage view of roads run, feeding the novelty story

**Done means**

- Every recorded run appears in history with correct distance, time and pace
- History renders from local storage with no network connection

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:36`, `research/05-product/mvp-scope.md:27`

#### `TS-06` Route save and re-run

**A good generated route the user cannot keep is a broken promise.**

Save a generated route, name it, and re-run it later with navigation intact. Also the escape hatch for the novelty engine's never-the-same-loop-twice default: some routes earn repetition, and refusing to allow it would be a worse product than the boredom it set out to solve.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Tracking and Data |
| **Effort, iOS-native** | 0.50 pm |
| **Effort, React Native** | 0.60 pm |
| **Walking-skeleton slice** | 0.20 pm &mdash; Save the run locally on finish. No naming, no saved-route management. |
| **RICE** | rank #13, score 4,000 (reach 5,000, impact 0.5, confidence 80%, effort 0.5) |
| **Personas** | Marcus (primary), Elena (primary) |
| **Needs** | N2 Route novelty and personalization at home |
| **Jobs** | FJ3 Get novelty and variety from my own front door |
| **Depends on** | `H-01` Core constraint route generation |

**What it actually does**

- Save a generated route with an optional name
- Saved-route list with re-run action
- Re-run with full navigation and cue generation
- Repeat-a-favorite override of the novelty preference

**Done means**

- A saved route re-runs later with identical geometry and working turn cues
- Saved routes are readable offline

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:42`, `research/05-product/mvp-scope.md:29`

#### `TS-10` Offline route access

**Maps and route cached on device, because Priya's connectivity is a hotel and a foreign SIM.**

Map tiles for a sensible corridor, the route geometry and all navigation cues cached at generation time, so mid-run connectivity loss never interrupts guidance. Note the split: caching a generated route is in scope, while generating a route offline is a P2 investigation, and the offline state says so plainly rather than spinning. Partially satisfied by travel mode's caching requirement, which is why the two should ship close together.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Tracking and Data |
| **Effort, iOS-native** | 2.00 pm |
| **Effort, React Native** | 2.40 pm |
| **RICE** | rank #24, score 600 (reach 2,000, impact 1, confidence 60%, effort 2.0) |
| **Personas** | Priya (primary) |
| **Needs** | N4 Travel: where do I run, right now, from here, N6 Mid-run navigation execution |
| **Jobs** | FJ1 Find a trustworthy route in an unfamiliar place, FJ7 Execute an unfamiliar route hands-free |
| **Depends on** | `H-01` Core constraint route generation, `X-01` Voice turn-by-turn navigation |
| **Requirement IDs** | `NF-O1`, `NF-O2`, `NF-O3`, `TM-F3` |

**What it actually does**

- Map tile caching for the route corridor at generation time
- Route geometry and cue set cached on device
- Guidance continues through full connectivity loss
- Explicit offline state offering cached previous routes rather than an undiagnosed spinner

**Done means**

- Airplane-moded mid-run, voice guidance continues to route completion
- With no connectivity at app open, cached routes are offered and the inability to generate is stated plainly

**Integrations** &mdash; Self-hosted Protomaps PMTiles; MapLibre

**What pulls it forward.** Travel-mode telemetry shows a meaningful far-from-home generation share, or Priya-profile interviews validate it.

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: P0 via NF-O1. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:57`, `research/05-product/mvp-scope.md:55`, `research/05-product/prd.md:379`

#### `TS-09` GPX export and import

**Near-free goodwill for the runners who ask for it.**

Export a generated route or recorded run as GPX, and import a GPX to run it with navigation. Lowest RICE score among the table-stakes set, but DEC-011 made it free permanently as part of the commitment that everything except the coaching layer stays free, which turns a minor utility into a small trust signal.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Tracking and Data |
| **Effort, iOS-native** | 0.50 pm |
| **Effort, React Native** | 0.60 pm |
| **RICE** | rank #29, score 350 (reach 1,000, impact 0.25, confidence 70%, effort 0.5) |
| **Personas** | Marcus (secondary) |
| **Needs** | N8 Urban doorstep running as a design center |
| **Jobs** | FJ11 Track and log my running life |
| **Depends on** | `TS-01` GPS run tracking, `O-01` Privacy architecture |

**What it actually does**

- Export a generated route as GPX
- Export a recorded run as GPX with privacy-zone obfuscation applied
- Import a GPX and navigate it
- Free permanently per DEC-011

**Done means**

- An exported GPX opens correctly in a third-party tool and never contains a true in-zone start point
- An imported GPX generates working turn cues

**What pulls it forward.** First sustained user requests.

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: unlisted. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:59`, `research/05-product/mvp-scope.md:57`

### Coaching Layer

*The only paid product. The defensible seam.* &mdash; 7 items, 21.00 native person-months.

#### `P-01` Training-state-aware route generation

**The workout shapes the route. The first paid feature, and the seam no competitor can copy without becoming the other kind of product.**

Today's workout type maps automatically to constraint weights: tempo gets a flat, crossing-minimized loop, easy gets soft surface, intervals get uninterrupted stretches, and poor readiness gets a shorter, gentler option with the reason stated. This is the defensible seam identified in Phase 4 and the entire basis of the paid tier under DEC-011. Its confidence score of 50 percent is honest about why: the market gap is verified, but demand is inferred from total absence rather than expressed need, which is exactly the risk DEC-011 accepted when it made the coaching layer the only paid product.

> **Documents disagree (CF-4).** Does the paid seam exist at launch? Recommendation: Free launch. GD-1 and then DEC-011 both settled this, and the reasoning is a measurement argument rather than a pricing one: a paywall before proof contaminates the retention signal the MVP exists to produce. DEC-011 additionally made the coaching layer the only paid product, so P-01 is the first paid feature by construction and cannot precede the paywall.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 4.00 pm |
| **Effort, React Native** | 4.80 pm |
| **RICE** | rank #21, score 750 (reach 2,000, impact 3, confidence 50%, effort 4.0) |
| **Personas** | Marcus (primary), Priya (secondary) |
| **Needs** | N3 Training-state-to-route connection |
| **Jobs** | FJ4 Match the route to today's workout |
| **Depends on** | `H-01` Core constraint route generation, `TS-03` HealthKit and Health Connect sync, `TS-08` Subscription and paywall infrastructure |
| **Blocks** | `P-02`, `P-04` |
| **Requirement IDs** | `AC1-F1`, `AC1-F2`, `AC1-F3`, `AC1-F4` |

**What it actually does**

- Workout type (easy, long, tempo, intervals, race pace) mapped to constraint weights automatically
- Readiness signals from platform health modulating distance and intensity envelope
- Degraded generation from workout type alone when readiness data is absent or consent withdrawn
- Plain-language explanation of every adjustment

**Done means**

- Selecting tempo measurably reduces crossing count and elevation variance versus easy for the same start and distance
- Revoking health access flips generation to workout-type-only with the correct notice, no crash and no stale readiness claims

**Integrations** &mdash; HealthKit readiness signals; Health Connect

**What pulls it forward.** Ships with TS-08 once week-4 retention of route generators clears roughly 20 percent.

**Risks**

- The entire paid product rests on this one job being felt value. If training-state-aware generation is not felt value, there is no fallback paid thing at v1.x

**Still open**

- Does workout-route matching resonate as a felt need once demonstrated
- Which readiness signals are defensible science rather than wellness theater

**What each document says.** `mvp-scope.md`: v1.x with TS-08. `prd.md`: P0 for workout-type, P1 for readiness. `team-roadmap.md`: months 16 to 20.

Sources: `research/05-product/rice-prioritization.md:51`, `research/05-product/mvp-scope.md:51`, `research/05-product/prd.md:181`

#### `P-03` Explainable generation

**Why this route, in one to three sentences that name the constraints and data that shaped it.**

Trust is the adoption barrier for AI training advice, and transparency is the counter. Every generated route and every plan adjustment carries a plain-language explanation that names its data basis and states its limitations honestly, because an explanation that overstates confidence is a defect rather than a style choice. Template-based is explicitly acceptable in v1: honesty and specificity outrank prose quality. Note the split with H-09, which ships the minimum honest-degradation form at launch while the richer explanation layer follows here.

> **Documents disagree (CF-3).** Route explanations: at launch, or after? Recommendation: Split, and the split is already written down. gtm-plan.md line 118 resolves it: honest degradation (H-09, 0.25 person-months) ships at launch because a safety-aware product that pretends is a liability, and the richer explanation layer (P-03, 2.0) follows in v1.x. Treat AC3-F1's minimum viable form as H-09 plus a one-line constraint summary, which the route card needs anyway to satisfy the AI Act disclosure in C-11.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 2.00 pm |
| **Effort, React Native** | 2.40 pm |
| **RICE** | rank #25, score 600 (reach 2,000, impact 1, confidence 60%, effort 2.0) |
| **Personas** | Elena (primary), Marcus (primary) |
| **Needs** | N1 Safety-aware routing, N5 Injury-calibrated coaching that runners trust |
| **Jobs** | FJ2 Find a route that is safe at this hour |
| **Emotional jobs** | Feel safe, not brave |
| **Depends on** | `H-01` Core constraint route generation, `H-09` Honest degradation messaging |
| **Requirement IDs** | `AC3-F1`, `AC3-F2`, `AC3-F3`, `AC3-F4`, `AC3-F5`, `RG-F4` |

**What it actually does**

- One-to-three sentence explanation on every route and adjustment
- Named data basis and stated limitations per explanation
- AI-generated labeling on all advice surfaces
- No safety guarantees and no medical claims, enforced by the language rules
- Template-based generation acceptable in v1

**Done means**

- Every route card and plan adjustment displays an explanation, and zero explanations contain banned terms
- Explanation copy passes the language-rule linter in continuous integration
- Explanations are VoiceOver-accessible

**Integrations** &mdash; On-device foundation models where feasible

**What pulls it forward.** Safety trust interviews confirm that explanation earns trust; then ship alongside the safety layer's first upgrade.

**Risks**

- A wrong answer on what explanation earns women runners' trust for safety-adjacent claims is a product-killing liability

**Still open**

- What explanation evidence actually earns trust for safety-adjacent claims

**What each document says.** `mvp-scope.md`: v1.x. `prd.md`: P0 for structured explanations, P2 for chat. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:58`, `research/05-product/mvp-scope.md:56`, `research/05-product/prd.md:237`

#### `P-06` Injury-calibrated progression

**The Runna-too-aggressive and TrainAsONE-too-conservative middle, claimed carefully.**

Load progression calibrated to protect beginners from their own ambition, which is Jake's central job and the clearest documented competitor failure: Runna's complaint record includes stress fractures and shin splints attributed to aggressive defaults, while the conservative alternative caps ambition with ten-minute runs. The opportunity is real and so is the liability, which is why this must stay advisory and non-diagnostic with no injury triage, and why the calibration methodology needs a defensible source before any claim is made.

| | |
|---|---|
| **Release** | v2+ |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 4.00 pm |
| **Effort, React Native** | 4.80 pm |
| **RICE** | rank #26, score 413 (reach 1,500, impact 2, confidence 55%, effort 4.0) |
| **Personas** | Jake (primary), Marcus (secondary) |
| **Needs** | N5 Injury-calibrated coaching that runners trust |
| **Jobs** | FJ8 Get training calibration that will not injure me |
| **Emotional jobs** | Feel like a real runner |
| **Depends on** | `P-02` Adaptive routines |
| **Requirement IDs** | `AC2-F4`, `AC2-F5` |

**What it actually does**

- Conservative load progression defaults for beginners
- Progression rate bounded by published load-management principles
- Advisory framing with no diagnosis and no injury triage
- Explanation of why a week was held back

**Done means**

- Beginner plans respect a bounded week-over-week load increase
- No surface makes a diagnostic or injury-prediction claim

**What pulls it forward.** P-02 exists, since calibration needs a plan to calibrate, plus interview evidence that the middle is worth claiming with liability care.

**Risks**

- Injury-adjacent claims carry the highest liability exposure in the catalog and need counsel before any marketing language

**Still open**

- Calibration methodology source gates both credibility and FTC substantiation

**What each document says.** `mvp-scope.md`: v2. `prd.md`: unlisted. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:55`, `research/05-product/mvp-scope.md:64`

#### `P-02` Adaptive routines

**Training plans that reshape when life happens, without guilt and without stacking missed load.**

Race-goal plan generation, then forward reshaping when runs are missed to travel, illness or family, calibrated deliberately between Runna-too-aggressive and TrainAsONE-too-conservative. Over half of marathoners miss seven or more consecutive days in a build, which is the evidence this exists for. Every plan day must be generatable as a route, and the specification is unusually blunt that a plan day without a route button is a defect: the seam is the product. Advisory and non-diagnostic only, which keeps Waypoint out of medical-device and AI-Act high-risk territory. The largest single item in the catalog at 6.0 person-months.

| | |
|---|---|
| **Release** | v2+ |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 6.00 pm |
| **Effort, React Native** | 7.20 pm |
| **RICE** | rank #27, score 400 (reach 2,000, impact 2, confidence 60%, effort 6.0) |
| **Personas** | Marcus (primary), Jake (primary), Priya (secondary) |
| **Needs** | N5 Injury-calibrated coaching that runners trust, N7 Plan flexibility when life disrupts training |
| **Jobs** | FJ5 Keep my training plan intact when life disrupts it, FJ8 Get training calibration that will not injure me |
| **Emotional jobs** | Guilt-free flexibility |
| **Depends on** | `P-01` Training-state-aware route generation |
| **Blocks** | `P-05`, `P-06` |
| **Requirement IDs** | `AC2-F1`, `AC2-F2`, `AC2-F3`, `AC2-F4`, `AC2-F5` |

**What it actually does**

- Race-goal plan generation from distance, date and current fitness
- Missed-run reshaping forward, never stacking load, with no guilt framing
- Every plan day generatable as a route with pre-filled constraint weights
- Conservative calibration defaults for beginners
- Advisory and non-diagnostic only, with no injury triage or health-risk scoring

**Done means**

- A simulated seven-day gap mid-plan produces a reshaped forward plan with reduced next-week load versus the pre-gap trajectory, plus an explanation
- Every plan day renders a generate-today's-route action that pre-fills the workout weights

**What pulls it forward.** Workout-route attach rate proves the seam is felt value, and paid conversion on P-01 funds the six person-month build.

**Risks**

- Calibration methodology is unsourced, which gates both credibility and FTC substantiation

**Still open**

- Published training-load science versus licensed methodology versus an advisor
- Does plan-disruption guilt actually connect to route intelligence in behavior

**What each document says.** `mvp-scope.md`: v2. `prd.md`: P1. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:56`, `research/05-product/mvp-scope.md:63`, `research/05-product/prd.md:209`

#### `P-04` Readiness and fatigue input

**Heart-rate variability and sleep feeding the day's route, once the signals are proven to mean something.**

Platform health readiness signals modulating the distance and intensity envelope of a generated route. Held at v2 for a reason worth stating plainly: the line between defensible sleep-and-HRV science and wellness theater is thin, and the explainable coach must not overstate it. When readiness data is missing or consent is withdrawn, generation falls back to stated workout type and says the signal is missing rather than inventing a score.

| | |
|---|---|
| **Release** | v2+ |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 2.00 pm |
| **Effort, React Native** | 2.40 pm |
| **RICE** | rank #28, score 375 (reach 1,500, impact 1, confidence 50%, effort 2.0) |
| **Personas** | Marcus (primary) |
| **Needs** | N3 Training-state-to-route connection, N5 Injury-calibrated coaching that runners trust |
| **Jobs** | FJ4 Match the route to today's workout, FJ8 Get training calibration that will not injure me |
| **Depends on** | `P-01` Training-state-aware route generation, `TS-03` HealthKit and Health Connect sync |
| **Requirement IDs** | `AC1-F2`, `AC1-F3` |

**What it actually does**

- Sleep, heart-rate variability and resting heart rate as generation inputs
- Distance and intensity envelope modulation
- Explicit consent before any readiness read
- Missing-signal state that never invents a readiness score

**Done means**

- Poor readiness measurably shortens or softens the generated option, with the reason stated
- Withdrawn consent falls back to workout type alone with the missing signal named

**Integrations** &mdash; HealthKit readiness signals; Health Connect

**What pulls it forward.** P-01 attach rate proven, plus readiness signal quality validated on real cohorts.

**Risks**

- Overstating what readiness signals mean is an FTC substantiation exposure, not just a credibility one

**Still open**

- Which readiness signals are defensible science rather than wellness theater

**What each document says.** `mvp-scope.md`: v2. `prd.md`: P1. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:58`, `research/05-product/mvp-scope.md:66`, `research/05-product/prd.md:182`

#### `P-05` Race-goal progression

**A plan that builds toward a specific race on a specific date.**

Progression modeling toward a committed race, which is the organizing structure most committed amateurs already think in and the motivation Gen Z cites most. Depends on adaptive routines existing first, because there must be a plan before there is a progression to shape.

| | |
|---|---|
| **Release** | v2+ |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 3.00 pm |
| **Effort, React Native** | 3.60 pm |
| **RICE** | rank #30, score 300 (reach 1,500, impact 1, confidence 60%, effort 3.0) |
| **Personas** | Marcus (primary), Jake (secondary) |
| **Needs** | N5 Injury-calibrated coaching that runners trust, N7 Plan flexibility when life disrupts training |
| **Jobs** | FJ5 Keep my training plan intact when life disrupts it, FJ8 Get training calibration that will not injure me |
| **Emotional jobs** | Feel like a real runner |
| **Depends on** | `P-02` Adaptive routines |
| **Requirement IDs** | `AC2-F1` |

**What it actually does**

- Race date and distance as the plan's organizing target
- Periodized build with taper
- Progression re-derivation when the plan is disrupted
- Race-week guidance

**Done means**

- A committed race date produces a periodized build ending in a taper
- A mid-build disruption re-derives the progression without stacking missed load

**What pulls it forward.** P-02 exists, and race-committed cohort share is visible in telemetry.

**What each document says.** `mvp-scope.md`: v2. `prd.md`: unlisted. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:61`, `research/05-product/mvp-scope.md:65`

#### `N-05` A best-training-plan brand war with Runna

**Unwinnable on brand. Waypoint wins on the seam, not the plan.**

Runna has the category brand and now Strava's distribution behind it. Competing plan-to-plan means fighting on their strongest ground. The seam between training state and route is where they are absent.

> **Locked.** Ruled out by DEC-006's NOT list. Reopening it needs a superseding decision record, not a scenario toggle.

| | |
|---|---|
| **Release** | ~~never~~ |
| **Module** | Coaching Layer |
| **Effort, iOS-native** | 0.00 pm |
| **Effort, React Native** | 0.00 pm |

**What each document says.** `mvp-scope.md`: never. `prd.md`: explicit non-goal. `team-roadmap.md`: not in scope at any horizon.

Sources: `research/05-product/mvp-scope.md:76`, `research/04-synthesis/concept.md`

### Trust and Privacy

*Legal obligation and the floor Elena stands on. Never optional.* &mdash; 16 items, 3.60 native person-months.

#### `O-01` Privacy architecture

**Privacy zones, private by default, layered consent and AI disclosure. Legal obligation and the floor Elena stands on.**

The engineering behind the compliance package, and second-highest RICE score in the catalog. Auto-generated obfuscation zones around home and frequent start points, applied before data leaves the device rather than as a display mask; everything private by default with no public heatmaps or proximity features; separate withdrawable consents for location, health and sharing, recorded with statement, timestamp and policy version; and AI disclosure at first interaction. The Strava heatmap precedent is the reason this is not deferrable: routes anchored at home reveal home addresses, and this product deliberately generates from the front door.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 1.50 pm |
| **Effort, React Native** | 1.80 pm |
| **Walking-skeleton slice** | 0.50 pm &mdash; Private-by-default storage and home-area coordinates never leaving the device unblurred. No privacy-zone interface, no consent management screens. |
| **RICE** | rank #2, score 12,000 (reach 10,000, impact 2, confidence 90%, effort 1.5) |
| **Personas** | Elena (primary), Marcus (secondary), Priya (secondary), Jake (secondary) |
| **Needs** | N1 Safety-aware routing |
| **Jobs** | FJ2 Find a route that is safe at this hour |
| **Emotional jobs** | Feel safe, not brave |
| **Blocks** | `TS-07`, `TS-09`, `X-03` |
| **Satisfies** | `C-1`, `C-2`, `C-3`, `C-11` |
| **Requirement IDs** | `C-1`, `C-2`, `C-3`, `C-11`, `RG-F9` |

**What it actually does**

- Auto-generated privacy zones around home and frequent start points
- Obfuscation applied before data leaves the device, on export, upload and log paths
- Private by default with no public heatmaps, flybys or proximity features
- Granular layered consent, separately withdrawable, never bundled into terms
- Consent ledger recording statement, timestamp and policy version, replayable
- AI disclosure at first interaction and on every AI surface

**Done means**

- No exported, uploaded or server-logged artifact contains a true in-zone start point, verified by automated test on export and upload paths
- A fresh-install audit shows zero data visible to any other party without an explicit share action
- Withdrawing health consent degrades dependent features without breaking route generation

**Risks**

- Obfuscation implemented as a display mask rather than end to end is the classic failure mode, and it is exactly what the Strava precedent punished

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: explicitly NOT cut.

Sources: `research/05-product/rice-prioritization.md:30`, `research/05-product/mvp-scope.md:31`, `research/05-product/prd.md:350`

#### `C-1` Privacy zones by default

**An obfuscation zone around home and frequent start points, applied before data leaves the device.**

Auto-generated rather than user-configured, because a privacy feature that depends on the user knowing to enable it protects the wrong people. Critically this is not a display-layer mask: the start point is treated as sensitive data end to end, so obfuscation happens before any export, upload or server log. The Strava heatmap incident is the precedent, and a product that generates routes from the front door is more exposed to it than one that does not.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.00 pm &mdash; Engineered as part of O-01; counted there, not here, to avoid double counting. |
| **Effort, React Native** | 0.00 pm |
| **Personas** | Elena (primary) |
| **Needs** | N1 Safety-aware routing |
| **Engineered by** | `O-01` |
| **Requirement IDs** | `C-1` |

**Done means**

- No exported, uploaded or server-logged artifact contains a true in-zone start point, verified by automated test on the export and upload paths.

**Risks**

- Implementing this as a display mask rather than end to end is the classic failure, and it is what the Strava precedent punished

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-10` DPIA plus AI Act classification memo

**A data protection impact assessment and an AI Act classification memo before EU launch.**

Large-scale processing of special category data triggers a mandatory DPIA. The AI Act memo documents why Waypoint sits outside the high-risk category, which is the reasoning that keeps the coaching layer advisory and non-diagnostic. EU and UK representatives are needed if there is no local establishment.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.20 pm |
| **Effort, React Native** | 0.24 pm |
| **Requirement IDs** | `C-10` |

**Done means**

- Both documents exist and are counsel-reviewed before EU availability.

**Risks**

- Mostly counsel work rather than engineering, and it is on the critical path for EU launch

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-11` AI transparency

**Disclose at first interaction that coaching is AI-generated, and label AI-generated routes and plans.**

EU AI Act Article 50(1) applies from 2 August 2026, which is before any plausible launch date, so this ships from the first build rather than being retrofitted for an EU release.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.00 pm &mdash; Engineered as part of O-01; counted there, not here, to avoid double counting. |
| **Effort, React Native** | 0.00 pm |
| **Engineered by** | `O-01` |
| **Requirement IDs** | `C-11` |

**Done means**

- The disclosure is shown at onboarding and on AI surfaces, with screenshot evidence retained.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-12` Not-medical-advice framing

**A prominent disclaimer, a physician-consultation prompt with red-flag symptoms, and risk acknowledgment at onboarding.**

This is what keeps Waypoint inside the FDA general wellness lane and out of medical device territory. It binds App Store copy as well as in-app text, so marketing language is in scope. No disease diagnosis or treatment claims anywhere.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Personas** | Jake (primary) |
| **Requirement IDs** | `C-12` |

**Done means**

- The onboarding flow contains the disclaimer, the physician prompt and the risk acknowledgment, and App Store copy is audited against the general wellness lane.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-13` Age gating

**A 16-plus minimum age gate at signup, with no knowing collection of children's data.**

The floor is set at 16 rather than 13 to stay clear of the additional children's-data regimes, and the assumption is inherited from the compliance research rather than decided. There is a note worth carrying: two of the three founders are minors themselves, which does not change the legal analysis but is a detail worth being ready for if anyone asks.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Requirement IDs** | `C-13` |

**Done means**

- The age gate blocks under-16 signup, and no child-directed content or marketing exists.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-14` Subscription hygiene

**Apple IAP and Play Billing only, full pre-purchase disclosure, and cancellation no harder than signup.**

Price, term and trial conversion disclosed before purchase, plus renewal reminders. The stakes here are strategic as much as legal: the category has documented billing rage, and Marcus is category-burned, so this is a trust surface rather than a checkbox.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.00 pm &mdash; Engineered as part of TS-08; counted there, not here, to avoid double counting. |
| **Effort, React Native** | 0.00 pm |
| **Personas** | Marcus (primary) |
| **Engineered by** | `TS-08` |
| **Requirement IDs** | `C-14` |

**Done means**

- The purchase flow shows full terms pre-purchase, and cancellation takes no more steps than signup.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-15` Security and breach readiness

**Encryption at rest and in transit, least-privilege access, and a drill-tested incident response plan.**

The response plan has to map to three different clocks: 60 days under the FTC Health Breach Notification Rule, 72 hours to authorities under GDPR, and whatever the applicable state breach laws require. Writing the plan after an incident is not a plan.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.30 pm |
| **Effort, React Native** | 0.36 pm |
| **Requirement IDs** | `C-15` |

**Done means**

- The incident response plan exists and is drill-tested before launch, and encryption is verified in architecture review.

**Risks**

- Self-managed PostGIS on Hetzner under DEC-009 means Waypoint owns more of the security surface than a fully managed stack would

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-2` Private by default

**Routes, activities and statistics visible only to the user unless explicitly shared.**

No public heatmaps, no proximity or flyby features in v1. This is both a compliance position and a competitive one: the deanonymization incidents that damaged competitors came from exactly these surfaces, and DEC-006's NOT list already forbids the social features that would need them.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.00 pm &mdash; Engineered as part of O-01; counted there, not here, to avoid double counting. |
| **Effort, React Native** | 0.00 pm |
| **Personas** | Elena (primary), Marcus (primary) |
| **Needs** | N1 Safety-aware routing |
| **Engineered by** | `O-01` |
| **Requirement IDs** | `C-2` |

**Done means**

- A fresh-install audit shows zero data visible to any other party without an explicit share action.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-3` Granular layered consent

**Separate withdrawable opt-ins for precise location, health data and sharing, never bundled into terms acceptance.**

Health and fitness data is GDPR Article 9 special category and needs explicit consent in its own right. Each consent is recorded with its statement, timestamp and policy version in a ledger that can be replayed, because the ability to prove what a user agreed to and when is the actual compliance artifact. Withdrawal must degrade the dependent feature without breaking route generation.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.00 pm &mdash; Engineered as part of O-01; counted there, not here, to avoid double counting. |
| **Effort, React Native** | 0.00 pm |
| **Personas** | Elena (primary) |
| **Needs** | N1 Safety-aware routing |
| **Engineered by** | `O-01` |
| **Requirement IDs** | `C-3` |

**Done means**

- The consent ledger exists and replays; withdrawing health consent flips training-state generation to its degraded mode without breaking route generation.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-4` Standalone Consumer Health Data Privacy Policy

**A separate health-data policy for Washington MHMD, plus accurate Apple privacy nutrition labels.**

Washington's My Health My Data Act requires a distinct consumer health data privacy policy rather than a section inside the general one, linked prominently. Nutrition labels must match actual data flows, which is a pre-submission audit rather than a drafting exercise.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.15 pm |
| **Effort, React Native** | 0.18 pm |
| **Requirement IDs** | `C-4` |

**Done means**

- Policies are live before App Store submission and nutrition labels match actual data flows in a pre-submission audit.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-5` Data minimization and retention schedule

**Collect only what generation and coaching need, with retention defined per data type.**

Maryland's MODPA applies a necessity standard rather than a consent standard, which means user permission does not license collection that is not necessary. Raw GPS is processed on device where feasible. The deliverable is a written data inventory with per-type retention, and no collection without a mapped purpose.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.20 pm |
| **Effort, React Native** | 0.24 pm |
| **Requirement IDs** | `C-5` |

**Done means**

- A written data inventory exists with per-type retention, and no data category is collected without a mapped purpose.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-6` Full deletion pipeline

**In-app account deletion cascading to backups and processors within statutory windows.**

Apple requires in-app account deletion for any app that supports account creation, so this is a store-review gate as well as a legal one. The hard part is the cascade: deletion has to empty the primary store, the analytics path and every processor system, which is why it needs verifying end to end in staging rather than asserting.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.40 pm |
| **Effort, React Native** | 0.48 pm |
| **Requirement IDs** | `C-6` |

**Done means**

- A deletion request empties user data from the primary store, analytics and processor systems, verified end to end in staging.

**Risks**

- The split data architecture under DEC-009 means deletion must fan out across two databases plus the auth layer

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-7` Data subject rights tooling

**Access and export, correction, and Global Privacy Control recognition.**

Portability means a complete machine-readable archive rather than a summary. GPC is an automated browser and device signal that some US states require honoring, so it is a technical integration rather than a policy statement.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.40 pm |
| **Effort, React Native** | 0.48 pm |
| **Requirement IDs** | `C-7` |

**Done means**

- Export produces a complete machine-readable archive, and the GPC signal is honored where applicable.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-8` No ad tech, no data sales, no cross-app tracking

**Health and location data walled off from every third-party SDK, contractually and technically.**

An SDK audit before each integration, with an inventory and an audit record. The upside of holding this line is concrete: with no tracking there is no App Tracking Transparency prompt to show, which removes a conversion-killing dialog from onboarding. Apple 5.1.3, FTC consent orders and Maryland's sale ban all point the same way.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Personas** | Elena (primary) |
| **Needs** | N1 Safety-aware routing |
| **Requirement IDs** | `C-8` |

**Done means**

- An SDK inventory with audit records exists, zero advertising or tracking SDKs are in the binary, and no ATT prompt is needed because no tracking exists.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

#### `C-9` DPAs and processor inventory

**Article 28 data processing agreements with every processor, plus a transfer mechanism for EU-to-US flows.**

Cloud, maps, analytics and AI providers each need a signed DPA before they touch production data, and EU-to-US transfers need standard contractual clauses or an adequacy mechanism. MHMD adds its own processor contract requirements.

> **Locked.** A launch-gating legal obligation under PRD goal G6. It cannot be moved out of the MVP; it can only be resourced.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Trust and Privacy |
| **Effort, iOS-native** | 0.15 pm |
| **Effort, React Native** | 0.18 pm |
| **Requirement IDs** | `C-9` |

**Done means**

- A signed DPA is on file for every processor before it touches production data.

**What each document says.** `mvp-scope.md`: mvp (O-01 umbrella). `prd.md`: P0, launch-gating. `team-roadmap.md`: compliance minimum, 2 to 3 pm.

Sources: `research/05-product/prd.md:350`, `research/01-market/regulatory-compliance.md section 7`

### Distribution and Commerce

*Getting the run out and the subscription in.* &mdash; 4 items, 2.00 native person-months.

#### `TS-08` Subscription and paywall infrastructure

**Clean billing. Deliberately deferred despite ranking third on RICE.**

Store billing through RevenueCat over StoreKit 2 and Play Billing, the paywall surface, trial handling, and the subscription hygiene the category has taught users to distrust. The instructive part is that a rank-3 RICE score did not earn a launch slot: GD-1 deferred it because a paywall before retention proof contaminates the signal the MVP exists to produce, and its high score reflects enabler efficiency rather than launch urgency. DEC-011 then set the terms it must implement: $99.99 a year, $12.99 a month, a 21-day annual-only trial, and a price-preserved Founding Runner rate at $69.99 for the free-era cohort.

> **Documents disagree (CF-4).** Does the paid seam exist at launch? Recommendation: Free launch. GD-1 and then DEC-011 both settled this, and the reasoning is a measurement argument rather than a pricing one: a paywall before proof contaminates the retention signal the MVP exists to produce. DEC-011 additionally made the coaching layer the only paid product, so P-01 is the first paid feature by construction and cannot precede the paywall.

| | |
|---|---|
| **Release** | v1.x |
| **Module** | Distribution and Commerce |
| **Effort, iOS-native** | 1.50 pm |
| **Effort, React Native** | 1.80 pm |
| **RICE** | rank #3, score 11,333 (reach 10,000, impact 2, confidence 85%, effort 1.5) |
| **Personas** | Marcus (primary) |
| **Needs** | N10 Trustworthy subscription mechanics |
| **Depends on** | `TS-04` Onboarding and permissions flow |
| **Blocks** | `P-01` |
| **Requirement IDs** | `C-14` |

**What it actually does**

- Store billing via RevenueCat over StoreKit 2 and Play Billing
- Annual and monthly products at the DEC-011 prices
- 21-day annual-only trial with pre-purchase disclosure of price, term and conversion
- Founding Runner price-preserved grandfathering for the free-era cohort
- Cancellation no harder than signup, plus renewal reminders
- Apple Small Business Program and Play 15 percent tier enrollment before the first transaction

**Done means**

- The purchase flow shows full terms before purchase, and trial conversion is disclosed
- Cancellation takes no more steps than signup
- Free-era accounts receive the preserved Founding Runner rate on conversion

**Integrations** &mdash; RevenueCat; StoreKit 2; Play Billing; Apple Small Business Program; Play 15 percent tier

**What pulls it forward.** Week-4 retention of route generators clears the healthy-cohort bar, directionally above 20 percent. Ships together with P-01, never alone, because a paywall in front of nothing is not a product.

**Risks**

- Enrol in the Apple Small Business Program before the first paid transaction, not after; the commission cliff is retroactive within the year
- The category has documented billing rage, so trust stakes here are strategic as well as legal

**Still open**

- Verify a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores

**What each document says.** `mvp-scope.md`: v1.x by GD-1. `prd.md`: P0 via C-14. `team-roadmap.md`: months 16 to 20.

Sources: `research/05-product/rice-prioritization.md:31`, `research/05-product/mvp-scope.md:42`, `research/05-product/prd.md:363`

#### `TS-07` Strava share

**Post to Strava, never compete with it. Free distribution and category credibility for half a person-month.**

One-way activity upload to a connected Strava account via the official upload API, with optional auto-share. Strictly write-only, for two reasons: Strava's API terms ban AI and machine-learning use of its data, and DEC-006's NOT list forbids competing with the social graph. Privacy-zone obfuscation is applied before upload rather than relying on Strava's own zones, so an exported trace never carries a true home start point. For Marcus, a run that is not in Strava did not really happen, which makes this an identity requirement as much as a distribution channel.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Distribution and Commerce |
| **Effort, iOS-native** | 0.50 pm |
| **Effort, React Native** | 0.60 pm |
| **RICE** | rank #4, score 9,600 (reach 6,000, impact 1, confidence 80%, effort 0.5) |
| **Personas** | Marcus (primary), Jake (primary) |
| **Needs** | N8 Urban doorstep running as a design center |
| **Jobs** | FJ11 Track and log my running life |
| **Emotional jobs** | Feel like a real runner |
| **Depends on** | `TS-01` GPS run tracking, `O-01` Privacy architecture |
| **Requirement IDs** | `EX3-F1`, `EX3-F2`, `EX3-F3` |

**What it actually does**

- OAuth connection with activity:write scope only
- Activity upload with trace and statistics
- Optional per-user auto-share
- Privacy-zone obfuscation applied before upload
- No read-back of Strava data into generation or coaching
- Token removal and upload stop on disconnect

**Done means**

- An uploaded activity appears in Strava with correct distance and time, and an obfuscated start when the run began inside a privacy zone
- Disconnecting removes stored tokens and stops uploads immediately

**Integrations** &mdash; Strava Upload API with activity:write only, OAuth 2.0

**Risks**

- Strava's program terms are a named top risk; confirm at build time that write-only upload from an AI-generation app is permitted

**Still open**

- Re-read the Strava upload API terms at build time

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: post-launch iteration.

Sources: `research/05-product/rice-prioritization.md:33`, `research/05-product/mvp-scope.md:30`, `research/05-product/prd.md:318`

#### `N-01` Social network or feed

**Post to Strava, never compete with the graph.**

The social graph is Strava's moat and it is not contestable by a three-person team. Waypoint writes to it and takes the distribution. This is locked by DEC-006 and it is also why the Strava integration is deliberately write-only.

> **Locked.** Ruled out by DEC-006's NOT list. Reopening it needs a superseding decision record, not a scenario toggle.

| | |
|---|---|
| **Release** | ~~never~~ |
| **Module** | Distribution and Commerce |
| **Effort, iOS-native** | 0.00 pm |
| **Effort, React Native** | 0.00 pm |

**What each document says.** `mvp-scope.md`: never. `prd.md`: explicit non-goal. `team-roadmap.md`: not in scope at any horizon.

Sources: `research/05-product/mvp-scope.md:76`, `research/04-synthesis/concept.md`

#### `N-06` Charging for basic loop generation

**Free web tools and Strava already commoditized it. The free tier anchors here.**

Confirmed and hardened by DEC-011, which made every routing constraint free permanently and left the coaching layer as the only paid product. Charging for basic generation would price against free substitutes while also charging women for safety, which the persona research flagged as the ethics line.

> **Locked.** Ruled out by DEC-006's NOT list. Reopening it needs a superseding decision record, not a scenario toggle.

| | |
|---|---|
| **Release** | ~~never~~ |
| **Module** | Distribution and Commerce |
| **Effort, iOS-native** | 0.00 pm |
| **Effort, React Native** | 0.00 pm |

**What each document says.** `mvp-scope.md`: never. `prd.md`: explicit non-goal. `team-roadmap.md`: not in scope at any horizon.

Sources: `research/05-product/mvp-scope.md:76`, `research/04-synthesis/concept.md`

### Onboarding and Activation

*No permissions, no product.* &mdash; 1 items, 1.00 native person-months.

#### `TS-04` Onboarding and permissions flow

**No permissions, no product. The activation gate for everything else in the catalog.**

Account creation via Sign in with Apple plus email or passkey, the location permission ask with a purpose string that names the feature, the health permission ask as a separate granular consent, the AI disclosure required by the EU AI Act from August 2026, the not-medical-advice framing with its physician prompt, and the age gate. Several launch-gating compliance requirements are satisfied here rather than anywhere else, which is why a flow this unglamorous is on the critical path.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Onboarding and Activation |
| **Effort, iOS-native** | 1.00 pm |
| **Effort, React Native** | 1.20 pm |
| **Walking-skeleton slice** | 0.40 pm &mdash; Single-screen onboarding: location permission, health write permission, AI disclosure line. No preference setup, no notification permission. |
| **RICE** | rank #6, score 8,500 (reach 10,000, impact 1, confidence 85%, effort 1.0) |
| **Personas** | Marcus (primary), Priya (primary), Elena (primary), Jake (primary) |
| **Needs** | N8 Urban doorstep running as a design center |
| **Blocks** | `TS-08` |
| **Requirement IDs** | `C-3`, `C-11`, `C-12`, `C-13` |

**What it actually does**

- Sign in with Apple plus email and passkey via Better Auth
- Location permission with a feature-naming purpose string, When In Use only
- Separate granular health-data consent, never bundled into terms
- AI disclosure at first interaction
- Not-medical-advice framing with physician prompt and risk acknowledgment
- Age gate at the 16-plus floor
- Unit and default preferences

**Done means**

- A first-time user reaches a first generated route in under three minutes
- Declining any single permission leaves the app functional in its degraded mode with the limitation stated
- Onboarding contains the AI disclosure, the medical framing and the age gate, evidenced by screenshot

**Integrations** &mdash; Sign in with Apple; Better Auth email and passkey (DEC-009)

**Risks**

- Each additional permission ask costs activation, and this flow carries four

**Still open**

- The 16-plus versus 18-plus age floor still needs its own decision record

**What each document says.** `mvp-scope.md`: mvp. `prd.md`: P0. `team-roadmap.md`: recut v1 core.

Sources: `research/05-product/rice-prioritization.md:35`, `research/05-product/mvp-scope.md:24`, `research/05-product/user-journeys.md:18`

### Platform Quality

*Performance, offline behavior, accessibility and the language rules. Obligations, not features.* &mdash; 19 items, 2.25 native person-months.

#### `NF-A1` Full VoiceOver support

**Every flow VoiceOver-navigable; account, purchase and subscription flows meet EN 301 549 without exception.**

The European Accessibility Act has been in force since June 2025 and puts purchase and account flows squarely in scope, which makes this the legally exposed surface rather than a nice-to-have. US ADA litigation references WCAG as the de facto benchmark, so the same work answers both.

> **Locked.** An accessibility obligation under the European Accessibility Act and WCAG 2.2 AA.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.40 pm |
| **Effort, React Native** | 0.48 pm |
| **Requirement IDs** | `NF-A1` |

**Done means**

- All flows are VoiceOver-navigable, and account and purchase flows pass an EN 301 549 audit.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:387`

#### `NF-A2` Respect OS accessibility settings

**Dynamic Type, contrast and reduced-motion settings respected throughout.**

Baseline WCAG 2.2 AA from the first sprint rather than a pre-launch retrofit, because layout that assumes a fixed text size is expensive to unpick later.

> **Locked.** An accessibility obligation under the European Accessibility Act and WCAG 2.2 AA.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.15 pm |
| **Effort, React Native** | 0.18 pm |
| **Requirement IDs** | `NF-A2` |

**Done means**

- Text scales with Dynamic Type without truncation or overlap, and reduced motion suppresses non-essential animation.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:387`

#### `NF-A3` Audio and haptic as accessibility equivalents

**Audio turn cues double as an accessibility feature for blind and low-vision runners; haptics serve deaf and hard-of-hearing runners.**

A pleasing convergence: the cue system built for hands-free running is also the accessibility path, so one implementation serves both. It does mean neither can be dropped as an optimization.

> **Locked.** An accessibility obligation under the European Accessibility Act and WCAG 2.2 AA.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Requirement IDs** | `NF-A3` |

**Done means**

- Every navigation cue is available in both audio and haptic form.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:387`

#### `NF-A4` One-handed operation in motion

**All mid-run actions reachable in the bottom half of the screen, touch targets at or above 44 points, operable with sweaty fingers.**

Running-specific and not covered by any general standard. No mid-run action may require two hands or a precise gesture.

> **Locked.** An accessibility obligation under the European Accessibility Act and WCAG 2.2 AA.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.15 pm |
| **Effort, React Native** | 0.18 pm |
| **Requirement IDs** | `NF-A4` |

**Done means**

- Every mid-run action is reachable one-handed in the lower half of the screen with a target of at least 44 points.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:387`

#### `NF-A5` Glare legibility

**Mid-run and watch screens meet a high-contrast outdoor legibility standard, field-tested in direct sunlight.**

Running-specific. A contrast ratio at or above 7:1 for mid-run essentials, with the exact ratio an assumption to validate outdoors rather than in a simulator.

> **Locked.** An accessibility obligation under the European Accessibility Act and WCAG 2.2 AA.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Requirement IDs** | `NF-A5` |

**Done means**

- Mid-run essentials remain legible in direct sunlight in field testing.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:387`

#### `NF-A6` No information only in small text while moving

**Anything a runner must know mid-run is available as audio or haptic.**

Running-specific, and the rule that keeps the interface honest about its context: reading small text while moving at pace is not a thing people can do safely.

> **Locked.** An accessibility obligation under the European Accessibility Act and WCAG 2.2 AA.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Requirement IDs** | `NF-A6` |

**Done means**

- No mid-run-essential information is delivered exclusively as small on-screen text.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:387`

#### `NF-L1` No safety guarantees, ever

**Never 'safe route', 'safest route', 'keeps you safe', or any wording implying a safety guarantee.**

Approved framing is 'safety-aware', 'prefers lit and populated streets', 'designed around your preferences'. This binds product copy, marketing and App Store metadata equally. Disclaimers do not eliminate negligence liability, so the language itself is the control.

> **Locked.** A liability control on product, marketing and store copy alike.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.02 pm |
| **Effort, React Native** | 0.02 pm |
| **Requirement IDs** | `NF-L1` |

**Done means**

- No user-facing or marketing surface contains a banned safety-guarantee term.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:400`

#### `NF-L2` Name the data basis and its limits

**Every safety-adjacent surface states what data it used and how incomplete that data can be.**

For example: based on street lighting and business-hours data, which can be incomplete. Specificity is what makes the claim defensible.

> **Locked.** A liability control on product, marketing and store copy alike.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.03 pm |
| **Effort, React Native** | 0.04 pm |
| **Requirement IDs** | `NF-L2` |

**Done means**

- Every safety-adjacent surface names its data basis and states its limits.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:400`

#### `NF-L3` Silence is a violation

**When safety data is unavailable, the interface says so.**

Honest degradation as a language rule rather than only an engine behavior. Saying nothing reads as confirmation, which is the failure mode this rule exists to prevent.

> **Locked.** A liability control on product, marketing and store copy alike.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.02 pm |
| **Effort, React Native** | 0.02 pm |
| **Requirement IDs** | `NF-L3` |

**Done means**

- Unavailable safety data produces an explicit statement rather than an absent indicator.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:400`

#### `NF-L4` No fear-based marketing

**Adopted as the default brand position, pending founder ratification.**

Selling a safety product by amplifying fear works and is corrosive, particularly to the persona it targets. Flagged in the persona research for founder decision and adopted here as the default until ratified.

> **Locked.** A liability control on product, marketing and store copy alike.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.01 pm |
| **Effort, React Native** | 0.01 pm |
| **Requirement IDs** | `NF-L4` |

**Done means**

- No marketing asset uses fear-based framing.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:400`

#### `NF-L5` Substantiate every AI claim

**Every explicit or implicit claim about what the AI does must be evidenced before it is made.**

The FTC's Operation AI Comply is the reason this is a hard rule rather than a style guideline.

> **Locked.** A liability control on product, marketing and store copy alike.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.02 pm |
| **Effort, React Native** | 0.02 pm |
| **Requirement IDs** | `NF-L5` |

**Done means**

- Every AI capability claim has documented substantiation before publication.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:400`

#### `NF-L6` Banned-terms linter in CI

**A banned-terms and required-disclosure lint list applied to interface copy and store metadata in continuous integration.**

The implementation that makes the other five language rules enforceable rather than aspirational. Without it, compliance depends on everyone remembering, which is not a control.

> **Locked.** A liability control on product, marketing and store copy alike.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.15 pm |
| **Effort, React Native** | 0.18 pm |
| **Requirement IDs** | `NF-L6` |

**Done means**

- The linter runs in CI and fails the build on a banned term or a missing required disclosure.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:400`

#### `NF-O1` Route and tiles cached at generation

**The route, its map tiles for a sensible corridor, and all navigation cues cached on device at generation time.**

Mid-run connectivity loss must never interrupt guidance. This is the requirement behind offline route access and travel mode's caching promise, and it is why the corridor rather than the whole city is the cache unit.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.30 pm |
| **Effort, React Native** | 0.36 pm |
| **Requirement IDs** | `NF-O1` |

**Done means**

- Airplane-moded mid-run, voice guidance continues to route completion.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:377`

#### `NF-O2` Offline recording with idempotent upload

**Run recording is fully offline; upload queues and retries idempotently.**

Idempotency is the load-bearing word. A retry that creates a duplicate activity in Strava is a visible bug in someone else's product, which is worse than a failed upload.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.25 pm |
| **Effort, React Native** | 0.30 pm |
| **Requirement IDs** | `NF-O2` |

**Done means**

- A run recorded with no connectivity uploads exactly once when connectivity returns, with no duplicate activity.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:377`

#### `NF-O3` Honest offline state

**Generation requires connectivity in v1; the offline state says so plainly and offers cached routes.**

Never a spinner without a diagnosis. On-device generation is a P2 investigation, and pretending otherwise in the interface would be the same dishonesty the engine's degradation rules forbid.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.05 pm |
| **Effort, React Native** | 0.06 pm |
| **Requirement IDs** | `NF-O3` |

**Done means**

- With no connectivity, the app states that generation is unavailable and offers cached previous routes.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:377`

#### `NF-P1` Route generation latency

**p50 at or under 5 seconds and p95 at or under 15 seconds from request to first route card, on cellular.**

Derived from Priya's 30-second total budget rather than chosen abstractly: if generation eats 15 seconds, everything else has to fit in the remaining 15. Targets are working numbers to validate in beta.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.15 pm |
| **Effort, React Native** | 0.18 pm |
| **Requirement IDs** | `NF-P1` |

**Done means**

- A 10 km urban request returns its first route card within the stated p50 and p95 on a cellular connection.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:368`

#### `NF-P2` Cold open to running

**Under 30 seconds from cold app open to a started, navigable run, including constraint confirmation.**

The hotel-lobby promise, and the one performance number that is a verified persona requirement rather than an engineering guess. It is also the demo: if this budget is missed, the activation story stops being true.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Requirement IDs** | `NF-P2` |

**Done means**

- A first-time-in-city user reaches a started navigable run within 30 seconds of app open, measured at p75.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:368`

#### `NF-P3` Watch cue latency

**Turn haptic on the wrist within one second of the phone cue.**

A cue that arrives late is worse than no cue, because the runner has already passed the turn.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.05 pm |
| **Effort, React Native** | 0.06 pm |
| **Requirement IDs** | `NF-P3` |

**Done means**

- The wrist haptic fires within one second of the corresponding phone cue.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:368`

#### `NF-P4` Battery

**A two-hour guided run consumes no more battery than category norms for GPS navigation apps.**

Benchmarked in field tests against RunGo and Footpath rather than against an absolute target, because the comparison is what a user actually notices.

> **Locked.** A quality floor that defines whether the feature works in its actual context, not an optional enhancement.

| | |
|---|---|
| **Release** | **MVP v1** |
| **Module** | Platform Quality |
| **Effort, iOS-native** | 0.10 pm |
| **Effort, React Native** | 0.12 pm |
| **Requirement IDs** | `NF-P4` |

**Done means**

- A two-hour guided run's battery consumption is within the measured band of comparable navigation apps.

**What each document says.** `mvp-scope.md`: absorbed into the ~2 pm release overhead line. `prd.md`: P0 for the accessibility and language groups. `team-roadmap.md`: public-launch hardening, 2 to 3 pm.

Sources: `research/05-product/prd.md:368`

## Taxonomies

### Personas

- **Marcus**, The committed amateur racer (Primary target segment). Runs four times a week around a job and family, races a spring half and a fall marathon, coaches himself with apps, and is bored to death of his own three routes. Top jobs: FJ4, FJ3, FJ8. Source: `research/03-users/personas.md:18`
- **Priya**, The traveling professional (Activation-critical profile inside the primary segment). A consultant in a different city every week, mid marathon block, standing in a hotel lobby at 6 a.m. with 10 miles to do and no idea where to run them. Top jobs: FJ1, FJ5, FJ7. Source: `research/03-users/personas.md:30`
- **Elena**, The safety-first city runner (Activation-critical profile inside the primary segment). An urban runner who plans every run around daylight, lighting and escape routes before she ever thinks about pace, because for her the route IS the safety decision. Top jobs: FJ2, FJ3. Source: `research/03-users/personas.md:42`
- **Jake**, The ambitious beginner (Secondary target segment). Nine months into running via a run club and a couch-to-5K app, signed up for his first half marathon on a dare, motivated, overconfident, and one aggressive training plan away from a shin splint. Top jobs: FJ8, FJ3. Source: `research/03-users/personas.md:55`

### Unmet needs

- **N1 Safety-aware routing** (evidence: Strong). Lighting, population and time of day as first-class routing constraints. 92 percent of women runners report safety concerns; no product among fifteen examined accepts safety as a routing input.
- **N2 Route novelty and personalization at home** (evidence: Strong). Roads not yet run, from the same front door, three to five times a week.
- **N3 Training-state-to-route connection** (evidence: Strong on the gap, inferred on demand). The day's prescribed workout shapes the route generated. No product connects the two.
- **N4 Travel: where do I run, right now, from here** (evidence: Moderate to strong). Arriving in an unfamiliar city mid-training-block with no local knowledge.
- **N5 Injury-calibrated coaching that runners trust** (evidence: Moderate). Between Runna-too-aggressive and TrainAsONE-too-conservative.
- **N6 Mid-run navigation execution** (evidence: Moderate). Hands-free guidance that is timely and shuts up between turns.
- **N7 Plan flexibility when life disrupts training** (evidence: Moderate). Over half of marathoners miss seven or more consecutive days in a build.
- **N8 Urban doorstep running as a design center** (evidence: Moderate). Not trailheads, not destinations. The run starts at the door.
- **N9 Weather and heat adaptation applied to the route** (evidence: Weak to moderate). Shade preference and exposure avoidance rather than a temperature readout.
- **N10 Trustworthy subscription mechanics** (evidence: Moderate as pattern, weak as need). The category has documented billing rage. Marcus is category-burned.
- **N11 Quiet routes for self-conscious beginners** (evidence: Weak). Explicitly on the do-not-chase list.

### Jobs to be done

- **FJ1** Find a trustworthy route in an unfamiliar place (wedge)
- **FJ2** Find a route that is safe at this hour (wedge)
- **FJ3** Get novelty and variety from my own front door (wedge)
- **FJ4** Match the route to today's workout (coaching)
- **FJ5** Keep my training plan intact when life disrupts it (coaching)
- **FJ6** Adjust the route for heat and weather (wedge)
- **FJ7** Execute an unfamiliar route hands-free (execution)
- **FJ8** Get training calibration that will not injure me (coaching)
- **FJ9** Fit the run into the time I actually have (wedge)
- **FJ10** Avoid interruptions and street crossings (wedge)
- **FJ11** Track and log my running life (table stakes)

### Emotional jobs

- **EJ1** Feel safe, not brave (Elena)
- **EJ2** Feel like a real runner (Jake)
- **EJ3** Guilt-free flexibility (Marcus)
- **EJ4** Confidence in unfamiliar places (Priya)
- **EJ5** Novelty and exploration joy (Marcus)

## Source documents

- `research/05-product/rice-prioritization.md`
- `research/05-product/mvp-scope.md`
- `research/05-product/prd.md`
- `research/05-product/user-journeys.md`
- `research/05-product/api-integration-map.md`
- `research/09-financial-team/team-roadmap.md`
- `research/03-users/personas.md`
- `research/03-users/unmet-needs.md`
- `research/03-users/jobs-to-be-done.md`

