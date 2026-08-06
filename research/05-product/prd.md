# Waypoint Product Requirements Document (v1, iOS)

Version-Timestamp: 2026-07-30 15:55:00 UTC-4

Status: DRAFT for the Phase 5 gate. Governed by the locked concept (`research/04-synthesis/concept.md`, DEC-006). Changes to scope tiers or non-goals require a new decision record.

How to read this document: [verified] traces to a sourced claim in Phase 1 to 4 research (citation inline), [inferred] is a reasoned conclusion from verified inputs, [assumption] is unvalidated and listed again in Section 8. Requirement IDs (RG-x, TM-x, AC-x, EX-x, NF-x, C-x) exist for traceability into `mvp-scope.md`, `rice-prioritization.md`, and engineering tickets.

> **ANNOTATED 2026-08-06 by [[DEC-020 Features catalog is the source of truth for release phase]].** The P0, P1 and P2 tiers in section 4 are no longer the release plan. Release phase is canonical in `catalog/features.json`, adjustable at `catalog/index.html`, and every requirement ID in this document is cross-referenced there.
>
> The requirements themselves are untouched and remain authoritative. What changed is arithmetic rather than judgement: the P0 tier was written against an assumed 2.5 to 3.0 full-time-equivalent team, and Phase 9 established the real figure at three part-time founders delivering roughly 7.5 person-months a year. Priced at that capacity, the 19 features marked P0 plus the launch-gating obligations come to 43.1 native person-months and project to **month 47**, against a 12-to-18-month competitive window. The tiers are still the right description of what the product eventually is. They are not a description of what ships first.
>
> Where this document disagrees with `mvp-scope.md`, the catalog records both positions and a written recommendation: the Apple Watch companion (CF-1), the full ten-constraint set (CF-2), route explanations (CF-3), and whether the paid seam exists at launch (CF-4). In all four cases a later gate decision or decision record settled the question, and the catalog follows that rather than this document's tier.
>
> One thing this document under-specified rather than got wrong: the 15 compliance requirements in section 5.1 and the non-functional set in 5.2 to 5.5 are real engineering work, and the planning documents absorbed them into a single ~2 person-month overhead line. The catalog prices them individually at 4.35 native person-months, which is why full scope now reads 32 to 33 React Native person-months instead of 29 to 31.

---

## 1. Overview

### 1.1 Product summary

Waypoint is the running app that knows where you should run. Its hero capability is constraint-based adaptive route generation: from wherever the runner stands, it generates the right route for today, treating distance, elevation, weather, street crossings, surface, safety awareness, and the runner's training state as routing inputs rather than afterthoughts. A paid coaching layer connects what the runner's body needs to where the runner actually goes, which no product on the market does [verified] (`research/02-competitors/feature-matrix.md`: no competitor holds a Yes in both the training block and the route generation block; the weather, street crossing, and safety constraint rows are empty across the entire market).

v1 is native iOS, HealthKit-first (Garmin's developer program is paused to new applicants; Strava's API bans AI and ML use of its data) [verified] (`concept.md` Section 5, `adjacent-platforms.md`). Solo founder, with a 12 to 18 month window before Strava plausibly ships plan-linked route generation [verified] (`concept.md` Section 6). Speed is a business requirement: this PRD prioritizes ruthlessly.

### 1.2 Positioning statement (locked, DEC-006)

For committed amateur runners who never quite know where today's run should go, Waypoint is the running app that generates the right route for you, right now, from wherever you stand.

Tagline: "Know where to run."

### 1.3 Goals (measurable)

| # | Goal | Target | Measurement | Label |
|---|------|--------|-------------|-------|
| G1 | Ship v1 to the App Store inside the competitive window | Public release within 12 months of Phase 5 approval | App Store release date | [verified] window per `concept.md` Section 6 |
| G2 | Reach "thousands of active runners" (Founder Brief 12-month goal) | 3,000+ monthly active users within 6 months of launch | MAU, privacy-preserving analytics | Threshold of 3,000 is [assumption], the Founder Brief says "thousands" without a number |
| G3 | Prove activation on the hero feature | **Re-based by DEC-012:** 40 percent of new users **complete a generated route as a recorded run** within 7 days of install. Leading indicator "Ignition": share of first sessions reaching a route on screen, median under 180 seconds | Activation funnel (Section 6), definitions in `../06-business-model/metrics.md` | Re-based 2026-08-06. The prior "generate and start" definition counted mid-run abandonment as success, which is the bad-route signature the MVP most needs to see |
| G4 | Prove retention on the daily wedge (safety plus novelty, per the H1 reframe) | **Re-based by DEC-012:** 25 percent day-30 retention **of the activated cohort**, paired with a separate 8 to 12 percent install-level line kept for benchmark comparison only | Cohort retention, first-party Postgres event table (DEC-012) | Re-based 2026-08-06. At install level, 25 percent would sit far outside the top decile of the entire Health and Fitness category in month one |
| G5 | Prove the paid seam | Measurable paywall encounter-to-conversion by triggering feature; conversion target set in Phase 6 with pricing | Signal 8, Section 6 | [verified] method per `unmet-needs.md` Section d |
| G6 | Zero compliance regressions | All 15 checklist items (Section 5.1) verified before submission; no launch without them | Pre-submission compliance audit | [verified] checklist per `regulatory-compliance.md` Section 7 |

### 1.4 Non-goals (locked with the concept, `concept.md` Section 7)

| Non-goal | Rationale (one line) |
|----------|----------------------|
| No social network | Post TO Strava; never compete with the social graph |
| No route content library | Generate, do not curate |
| No multi-sport breadth in v1 | Running only; expansion path is post-traction |
| No hardware ambitions | Software on Apple's hardware |
| No "best training plan" brand war with Runna | Waypoint wins on the route seam, not plan quality claims |
| No charging for basic loop generation | The market gives simple loops away free; the free tier must too |

---

## 2. Users

Full personas: `research/03-users/personas.md`. These are desk personas awaiting interview validation; the interview backlog runs alongside Phase 5 and can adjust calibration without unlocking the concept (DEC-006).

| Persona | Role in v1 | Essence | Critical flows |
|---------|-----------|---------|----------------|
| Marcus, committed amateur racer | Primary target, the proven payer [verified] (`segmentation.md` via `concept.md`) | 3 to 5 runs per week, self-coached, races, bored of his three loops | Daily generate-from-home with novelty; workout-shaped route (paid); post-run Strava share; clean billing |
| Jake, ambitious beginner | Secondary, growth pipeline | Run-club Gen Z, first half marathon, one aggressive plan from injury | Free-tier generate and explore; gentle calibration in the paid plan; shareable results |
| Priya, traveling professional | Activation-critical, sharpest demo | Hotel lobby at 6 a.m., 10 miles to do, unfamiliar city | Travel mode: trustworthy route from the hotel door in under 30 seconds; watch-guided hands-free execution; offline resilience |
| Elena, safety-first city runner | Activation-critical, strongest-evidence need [verified] (`unmet-needs.md` need 1) | The route IS the safety decision; 92 percent of women runners report safety concerns [verified] | Safety-aware generation with time-of-day awareness; the WHY explanation; honest degradation; privacy zones and no location leakage |

Reading: v1 flows are designed around Marcus's week and stress-tested against Priya's trip and Elena's 6 a.m. run. Jake inherits the free tier plus gentler defaults; he gets no dedicated surface in v1.

---

## 3. Feature requirements

Organized by the three tiers from the locked concept. Priorities: P0 ships in v1 or v1 does not ship; P1 ships in v1 if the window allows, first fast-follow otherwise; P2 is post-v1, documented to prevent scope creep. The exact free-vs-paid boundary is a Phase 6 decision (DEC-006 deferral); tier labels here reflect the concept's anchoring (hero free, adaptive paid).

### TIER 1: The free anchor, constraint-based route generation

#### 3.1 Feature RG: Route generation engine (the hero, deepest treatment)

Description: on-demand generation of a runnable loop or out-and-back from any start point, satisfying user constraints and ambient context. Built on OpenStreetMap data with GraphHopper-class round-trip routing plus custom constraint scoring; the moat is the constraint data and personalization, not the router [verified] (`concept.md` Section 5, `industry-trends.md`).

Priority: P0. This is the product.

User stories:

- As Marcus, I want a route matching my target distance from my front door that I have not run before, so the daily decision is effortless.
- As Elena, I want lighting, foot traffic, and time of day treated as routing inputs, so I can widen my running world beyond my two proven loops.
- As Priya, I want a trustworthy route from the hotel door in under 30 seconds, so the run happens instead of the treadmill surrender.
- As Jake, I want new-runner distances to feel like exploration, not laps of the same park.

##### 3.1.1 Constraint inputs: full enumeration

Every constraint row states its data source and its failure mode. The engine-wide failure principle (RG-F10 below): degrade honestly, never fake confidence. When a data source is unavailable, the engine says which constraint it could not honor and generates without it, or declines to generate. It never silently pretends the constraint was applied.

| # | Constraint | User-facing control | Data source(s) | Failure mode (when data is missing or stale) |
|---|-----------|--------------------|----------------|---------------------------------------------|
| 1 | Start point | Current GPS location or dropped pin | Core Location | No GPS fix: prompt for a pin or address; never guess a start point |
| 2 | Target distance | Free-form value (not presets; Strava's presets are a documented weakness [verified], `feature-matrix.md` footnote 16) | User input | Engine cannot hit target within tolerance (plus or minus 5 percent [assumption, tune in beta]): return nearest achievable distance, labeled, with the delta stated |
| 3 | Elevation | Preference (flat, rolling, hilly) and optional gain cap | OSM plus digital elevation model tiles | DEM tile missing: state "elevation data unavailable here", generate by distance only, flag the route as elevation-unverified |
| 4 | Surface | Preference (paved, unpaved, mixed, avoid trails) | OSM surface and highway tags | Sparse OSM tagging in the area: state coverage is partial, prefer tagged ways, never present untagged ways as confirmed surface |
| 5 | Street-crossing minimization | Toggle plus workout context (tempo and intervals want uninterrupted stretches) | Proprietary crossing graph derived from OSM intersections, road class, and signal tags [assumption A3 in `concept.md`: buildable from open data at solo-founder scale; Phase 5 stack work must validate] | Crossing graph not built for region: constraint greyed out with "not yet available here"; never a fake score |
| 6 | Safety awareness (lighting, populated areas) | Toggle plus automatic time-of-day weighting; framed as "safety-aware", never "safe" (Section 5.4) | OSM lit tags, POI and business density, open-hours data, ambient daylight calculation; explicitly NOT crime data in v1 (redlining exposure, see open questions) | Any input unavailable: banner "lighting data is limited in this area, route preference applied where known"; if coverage falls below a usable threshold, the toggle reports it cannot be honored here. NEVER present an unscored route as safety-checked |
| 7 | Weather and heat | Automatic adjustment (shade preference, exposure avoidance, cut-short options in heat) with override | Free-tier weather API (temperature, humidity, UV, wind), OSM tree cover and land use for shade proxy | Weather API down: generate without weather adjustment and say so; shade proxy unavailable: omit the shade claim from the route explanation |
| 8 | Daylight | Automatic (sunrise and sunset at the start point) | On-device solar calculation, no network needed | Effectively cannot fail; if the clock or location is wrong the user sees the assumed local time in the explanation |
| 9 | Route novelty | "New ground" preference; "roads you have not run" | Waypoint's own run history for this user (on-device first) | No history yet (new user): novelty silently inapplicable, engine notes it is learning; history sync unavailable: use local cache |
| 10 | Training state (paid, feeds from Tier 2) | Today's workout type, readiness | Waypoint plan state plus HealthKit readiness signals | HealthKit permission denied or data absent: generate from stated workout type alone and say the readiness signal is missing; never invent a readiness score |

Data posture note: HealthKit-first; no Strava data ingestion for generation or coaching (Strava's API terms ban AI and ML use [verified], `adjacent-platforms.md`); Garmin is an uncertain later unlock [verified].

##### 3.1.2 Functional requirements

| ID | Requirement |
|----|-------------|
| RG-F1 | Generate a loop or out-and-back from any start point (current location or pin) satisfying the active constraints in 3.1.1 |
| RG-F2 | Accept free-form target distance in the user's unit preference (km or mi); result within plus or minus 5 percent or labeled with the actual delta |
| RG-F3 | Return at least 1 and up to 3 candidate routes per generation, each with distance, elevation profile, surface breakdown, crossing count, and constraint-satisfaction summary |
| RG-F4 | Every generated route carries a plain-language explanation of why it was chosen and which constraints shaped it (the trust and transparency requirement; also serves EU AI Act Article 50 disclosure, C-11) |
| RG-F5 | Regenerate ("try another") without re-entering constraints; regeneration must not return a route already offered in the session |
| RG-F6 | Novelty: when history exists, prefer unrun segments; "never the same loop twice unless asked" as the default posture, with a "repeat a favorite" escape hatch |
| RG-F7 | Constraint conflicts (for example, flat plus hilly area plus exact distance) resolve by stated priority order, and the result explains which constraint was relaxed |
| RG-F8 | Time-of-day awareness is automatic: generating after civil dusk weights lighting and populated areas up without the user asking (Elena's flows must not require configuration) |
| RG-F9 | The start point is treated as sensitive data end to end: obfuscated before leaving the device for any shared or logged surface (C-1) |
| RG-F10 | Honest degradation, engine-wide: when any data source in 3.1.1 is unavailable, the UI states which constraint was not honored; when no route meets active constraints, the engine says "no good route meets your constraints right now" with the specific blockers, rather than shipping a pretender route [verified requirement origin: `unmet-needs.md` Section b implication 2, `personas.md` Elena] |
| RG-F11 | All generation requests work over cellular; payload sized for hotel and roaming conditions [inferred from Priya's flows] |

##### 3.1.3 Acceptance criteria

- AC-RG-1: Given a start point in a mapped urban area, a 10 km target generates 1 to 3 routes each within 9.5 to 10.5 km, in p95 under 15 seconds (NF-P1).
- AC-RG-2: Given safety awareness on and lighting data coverage below threshold for the area, the route card displays the limited-coverage notice, and no route is presented as safety-scored.
- AC-RG-3: Given dusk at the start point, generated routes measurably weight lit and populated ways versus the same request at noon (verifiable in engine telemetry).
- AC-RG-4: Given constraints no local route can satisfy, the app shows the honest-degradation message naming the unmet constraints and offers relaxation choices; it never returns an unlabeled non-conforming route.
- AC-RG-5: Every route card shows the WHY explanation and the AI disclosure; both are VoiceOver-accessible.
- AC-RG-6: A user with 10+ recorded runs receives routes with measurably higher unrun-segment share than a fresh account for the same request (novelty proof).
- AC-RG-7: With location permission denied, the app offers pin-drop generation and functions fully except current-location start.

Open questions (RG):

- OQ-RG-1: Crossing graph and lighting scoring buildability at solo-founder scale (concept assumption A3) needs a technical spike before the stack recommendation locks. Which regions get constraint coverage at launch, and what is the coverage-threshold number that flips a constraint to "unavailable here"?
- OQ-RG-2: Does any candidate lighting or weather data license restrict safety-critical use? [carried from `regulatory-compliance.md` open questions]
- OQ-RG-3: Does safety-aware scoring create redlining or discrimination exposure by systematically steering users away from certain neighborhoods? Needs counsel plus a fairness design review before launch; v1 excludes crime data partly for this reason. [carried from `regulatory-compliance.md`]
- OQ-RG-4: The plus or minus 5 percent distance tolerance and the 3-candidate count are [assumption]; beta telemetry should tune both.

#### 3.2 Feature TM: Travel mode (activation moment and demo story)

Description: instant orientation in an unfamiliar city. Technically the same engine (start-anywhere is RG-F1); travel mode is the packaging: zero-configuration first route, aggressive defaults, offline resilience. Travel is the activation moment, safety plus home novelty are the daily retention wedge [verified] (H1 reframe, DEC-006).

Priority: P0 (it is the demo story and the sharpest test of the engine's promise).

User stories:

- As Priya, I want to open the app in a hotel lobby and have a route sized to today's workout in under 30 seconds, so I never think the night before.
- As Marcus on a race trip, I want a shakeout route from the hotel without learning a new workflow.

Functional requirements:

| ID | Requirement |
|----|-------------|
| TM-F1 | Detecting a start point far from the user's home area offers one-tap "run here" with the user's saved defaults applied |
| TM-F2 | Generation-to-start-run flow completes in under 30 seconds including constraint confirmation (NF-P2) |
| TM-F3 | Once generated, the route and its navigation are fully cached on device (NF-O1); mid-run connectivity loss never breaks guidance |
| TM-F4 | Safety awareness defaults ON in unfamiliar areas [inferred from Priya's 6 a.m. flows; interacts with the Phase 6 free-tier boundary decision] |

Acceptance criteria:

- AC-TM-1: A first-time-in-city user reaches a started, navigable run within 30 seconds of app open (measured p75 [assumption on percentile]).
- AC-TM-2: Airplane-moded mid-run, voice guidance and on-watch cues continue to route completion.

Open questions: OQ-TM-1: what distance from home triggers travel framing, and is the home area definition privacy-safe (interacts with privacy zones, C-1)?

### TIER 2: The paid adaptive layer

The defensible seam: what neither a route app nor a coaching app can copy without becoming the other [verified] (`unmet-needs.md` Section b implication 3). Demand for the training-state-to-route connection is [inferred] (total market absence, no expressed community demand); paywall telemetry (Signal 8) and Priority 1 interviews arbitrate.

#### 3.3 Feature AC-1: Training-state-aware route generation

Description: today's workout type, fatigue and readiness (HealthKit), and progression toward a race goal shape the route that gets generated. Tempo day gets a flat uninterrupted loop; easy day gets soft surface; readiness-poor days get shorter, gentler options.

Priority: P0 for workout-type-shaped generation (the seam must exist at launch to test the paid thesis); P1 for HealthKit readiness modulation.

User stories:

- As Marcus, I want tempo day to produce a flat, crossing-minimized route, so the workout is executable, not just prescribed.
- As Marcus, when my readiness is poor, I want the route to reflect a gentler day and tell me why.

Functional requirements:

| ID | Requirement |
|----|-------------|
| AC1-F1 | Workout type (easy, long, tempo, intervals, race pace) maps to constraint weights (surface, crossings, elevation, loop shape) automatically |
| AC1-F2 | HealthKit readiness signals (sleep, HRV, resting HR [exact signal set is a stack-recommendation decision]) modulate the day's distance and intensity envelope; explicit consent per C-3 before any HealthKit read |
| AC1-F3 | Readiness data missing or consent withdrawn: generate from workout type alone, state the missing signal (RG failure principle); coaching features degrade, route generation never breaks (GDPR withdrawal degraded-mode requirement [verified], `regulatory-compliance.md` Section 2) |
| AC1-F4 | Every adjustment is explained in plain language (feeds Feature AC-3) |

Acceptance criteria:

- AC-AC1-1: Selecting "tempo" measurably reduces crossing count and elevation variance versus "easy" for the same start and distance.
- AC-AC1-2: Revoking HealthKit access flips generation to workout-type-only with the correct notice, no crash, no stale readiness claims.

Open questions: OQ-AC1-1: does workout-route matching resonate as felt need once demonstrated (Priority 1 interview question, `unmet-needs.md`)? OQ-AC1-2: which readiness signals are defensible science versus wellness theater; the explainable coach must not overstate them (FTC substantiation, C-12 adjacent).

#### 3.4 Feature AC-2: Adaptive routines (plans that survive real life)

Description: training plans that reshape when life happens (missed runs, travel, weather), calibrated between Runna-too-aggressive and TrainAsONE-too-conservative [verified gap] (`gap-analysis.md` need 4 via `unmet-needs.md` need 5). Over 50 percent of marathoners miss 7+ consecutive days in a build [verified].

Priority: P1. The wedge acquires; the coaching layer monetizes but can fast-follow the route seam. A v1 without plans still monetizes AC-1 plus AC-3 [inferred; final call in `mvp-scope.md`].

User stories:

- As Marcus, when I miss a week to family life, I want the plan to reshape without guilt, not demand three makeup runs.
- As Jake, I want a plan that protects me from my own ambition and gets me to the start line uninjured.
- As Priya, I want the plan to bend around a travel week and hand each day to the route engine.

Functional requirements:

| ID | Requirement |
|----|-------------|
| AC2-F1 | Race-goal plan generation (distance, date, current fitness self-report plus history when available) |
| AC2-F2 | Missed-run and disruption handling: reshape forward, never stack missed load; no guilt framing in copy |
| AC2-F3 | Each plan day is generatable as a route via AC-1 (the seam is the product; a plan day without a route button is a defect) |
| AC2-F4 | Calibration defaults conservative for beginners (Jake's injury evidence [verified as sentiment], `profile-runna.md` via `personas.md`) |
| AC2-F5 | Advisory and non-diagnostic only; no injury triage, no health-risk scoring (keeps Waypoint out of medical device and AI Act high-risk territory [verified], `regulatory-compliance.md` Section 4) |

Acceptance criteria:

- AC-AC2-1: Simulated 7-day gap mid-plan produces a reshaped forward plan with reduced next-week load versus pre-gap trajectory, plus an explanation.
- AC-AC2-2: Every plan day renders a "generate today's route" action that pre-fills AC1-F1 weights.

Open questions: OQ-AC2-1: calibration model source (published training-load science versus licensed methodology versus advisor); this gates credibility and FTC substantiation. OQ-AC2-2: does the community's plan-disruption guilt actually connect to route intelligence in behavior (Signal 5 telemetry arbitrates, `unmet-needs.md` Section d).

#### 3.5 Feature AC-3: The explainable coach

Description: the coach explains its reasoning in plain language: why this route, why this workout, why the plan changed. Trust is the adoption barrier for AI training advice; transparency is the counter [verified as the concept's position] (`concept.md` Section 4). On-device AI where feasible (Apple foundation models) for privacy and cost [verified intent] (`concept.md` Section 5).

Priority: P0 for route and adjustment explanations (they are load-bearing for Elena's trust and for AI Act disclosure); P2 for free-form conversational chat.

User stories:

- As Elena, I want to know WHY a route was chosen (lit streets, open businesses, populated path), so I can judge it myself instead of trusting a black box.
- As Marcus, when the plan changes, I want the reason in one sentence, not a shrug.

Functional requirements:

| ID | Requirement |
|----|-------------|
| AC3-F1 | Every generated route and every plan adjustment carries a one-to-three sentence explanation naming the constraints and data that shaped it |
| AC3-F2 | Explanations state data limitations honestly (ties to RG-F10); an explanation that overstates confidence is a defect, not a style choice |
| AC3-F3 | All AI-generated advice surfaces are labeled as AI-generated (C-11, EU AI Act Article 50(1), applies 2026-08-02 [verified]) |
| AC3-F4 | No explanation makes safety guarantees or medical claims (Section 5.4 language rules) |
| AC3-F5 | v1 explanations may be template-based rather than LLM-generated; honesty and specificity outrank prose quality [inferred scope control] |

Acceptance criteria:

- AC-AC3-1: 100 percent of route cards and plan adjustments display an explanation; zero explanations contain the banned terms in Section 5.4.
- AC-AC3-2: Explanation copy passes the language-rule linter (Section 5.4 implementation note) in CI.

Open questions: OQ-AC3-1: what explanation evidence earns women runners' trust for safety-adjacent claims (Priority 2 interview study; a wrong answer is a product-killing liability [verified framing], `unmet-needs.md` Section c).

### TIER 3: The execution surface

Turn-by-turn audio for runners is a solved problem at indie scale (Footpath, RunGo) but never paired with generation; Waypoint attaches execution to an intelligent generator rather than inventing it [verified] (`feature-matrix.md` finding 5).

#### 3.6 Feature EX-1: Voice-guided turn-by-turn navigation

Priority: P0. The bridge between generation and reality; generation without execution is a demo, not a product [inferred] (`unmet-needs.md` need 6: execution layer, wedge-adjacent and mandatory).

User stories:

- As Priya, I want to run an unfamiliar city with the phone pocketed, never stopping to check a screen.
- As Marcus on a new route, I want prompts that are timely and shut up between turns (Garmin's unsilenceable prompts are a documented complaint [verified], `pain-points.md` Section 6 via `unmet-needs.md`).

Functional requirements:

| ID | Requirement |
|----|-------------|
| EX1-F1 | Spoken turn cues with configurable verbosity (all cues, turns only, off); duck rather than pause the user's music or podcast audio |
| EX1-F2 | Off-route detection with calm rerouting back to the route or recalculated to target distance; no scolding repetition |
| EX1-F3 | Full run tracking (GPS trace, distance, pace, time) recorded via HealthKit-compatible workout session; the recorded run feeds novelty history and the learning loop |
| EX1-F4 | Works with screen locked; audio cues via any connected audio device |
| EX1-F5 | Haptic turn cues as a non-audio alternative (accessibility and quiet running, NF-A group) |

Acceptance criteria:

- AC-EX1-1: A scripted 5 km route walk-through delivers every turn cue between 80 m and 30 m before the turn [assumption on distances, tune in field testing] with zero missed turns in test runs.
- AC-EX1-2: Going off-route triggers exactly one reroute prompt cycle, and guidance resumes on the new path.
- AC-EX1-3: Music ducking verified against Apple Music, Spotify, and a podcast app.

Open questions: OQ-EX1-1: reroute-to-distance versus reroute-to-original-path default; Signal 6 telemetry (deviation behavior) decides.

#### 3.7 Feature EX-2: Apple Watch companion

Priority: P0 for glanceable cues mirrored from the phone session (distance, pace, next turn, haptics); P2 for standalone watch-only execution (no phone on the run).

User stories:

- As Priya, I want the next turn on my wrist so the phone never leaves my pocket in a strange city.
- As Elena, I want my live run shareable to a trusted contact (P1, see EX2-F3).

Functional requirements:

| ID | Requirement |
|----|-------------|
| EX2-F1 | Watch shows elapsed distance, pace, and next-turn cue with wrist haptics, mirroring the phone session |
| EX2-F2 | Watch face legible in direct sunlight at a glance (NF-A5); no interaction required mid-run beyond raise-to-look |
| EX2-F3 | (P1) Live location sharing to one trusted contact, opt-in per run, never default-on, auto-expiring at run end (Elena's job "let someone I trust follow my run live"; privacy interactions with C-1 and C-2 must be resolved in design) |

Acceptance criteria:

- AC-EX2-1: Turn haptic fires on the wrist within 1 second of the phone cue.
- AC-EX2-2: Watch session survives phone screen lock and backgrounding for a full run.

Open questions: OQ-EX2-1: watchOS mirroring versus native watch workout session architecture (stack decision); OQ-EX2-2: does EX2-F3 live sharing create a deanonymization or stalking vector that outweighs its safety value; needs a privacy design review before P1 commitment [inferred from the Flyby lesson, `regulatory-compliance.md` Section 1].

#### 3.8 Feature EX-3: Post-run share to Strava

Priority: P0. Strava is where the social graph lives; Waypoint posts to it and never competes with it (non-goal 1).

User stories:

- As Marcus, I want the run in my Strava feed automatically, or I did not really run it.
- As Jake, I want shareable moments for the run club.

Functional requirements:

| ID | Requirement |
|----|-------------|
| EX3-F1 | One-way activity upload (GPX trace plus stats) to a connected Strava account via the official upload API; optional auto-share per user setting |
| EX3-F2 | Privacy zone obfuscation applied BEFORE upload (the exported trace never contains the true start point when it is home, C-1); Strava's own privacy zones are not relied on |
| EX3-F3 | No Strava data is read back into Waypoint for generation or coaching (API AI/ML ban [verified], `adjacent-platforms.md`); the integration is write-only |
| EX3-F4 | Also writes the workout to HealthKit (system of record on device) |

Acceptance criteria:

- AC-EX3-1: An uploaded activity appears in Strava with correct distance, time, and an obfuscated start when the run began inside a privacy zone.
- AC-EX3-2: Strava disconnect removes stored tokens and stops uploads immediately.

Open questions: OQ-EX3-1: confirm the current Strava upload API terms permit write-only integration from an app whose generation is AI-based; needs a terms re-read at build time [inferred caution].

---

## 4. Feature priority summary

| Priority | Features |
|----------|----------|
| P0 | RG route generation engine (all 10 constraint inputs, honest degradation), TM travel mode, AC-1 workout-type-shaped generation, AC-3 route and adjustment explanations, EX-1 voice turn-by-turn plus run tracking, EX-2 watch companion (glanceable cues), EX-3 Strava share, all Section 5.1 compliance requirements |
| P1 | AC-1 HealthKit readiness modulation, AC-2 adaptive routines, EX2-F3 live location sharing (pending privacy review) |
| P2 | Standalone watch-only execution, free-form conversational coach chat, Android and additional geographies (Section 7) |

---

## 5. Non-functional requirements

### 5.1 Privacy and compliance (the 15-item checklist as requirements)

Source: `research/01-market/regulatory-compliance.md` Section 7 [verified checklist; per-item labels inherited from that document]. Each item is a launch-gating requirement (G6). Not legal advice; counsel confirms per market before launch.

| ID | Requirement | Acceptance criterion |
|----|-------------|----------------------|
| C-1 | Privacy zones by default: auto-generated obfuscation zone around home and frequent start points; obfuscation applied before data leaves the device or reaches any shared surface (not a display-layer mask); the start point is sensitive data end to end | No exported, uploaded, or server-logged artifact contains a true in-zone start point; verified by automated test on the export and upload paths |
| C-2 | Private by default: routes, activities, stats visible only to the user unless explicitly shared; no public heatmaps, no proximity or flyby features in v1 | Fresh-install audit shows zero data visible to any other party without an explicit share action |
| C-3 | Granular layered consent: separate withdrawable opt-ins for (a) precise location, (b) health and fitness data (GDPR Article 9 explicit consent), (c) any sharing; never bundled into terms acceptance; each consent recorded with statement, timestamp, and policy version | Consent ledger exists and replays; withdrawing (b) flips AC-1 to its degraded mode (AC1-F3) without breaking route generation |
| C-4 | Standalone Consumer Health Data Privacy Policy (Washington MHMD) linked prominently, plus main privacy policy and accurate Apple privacy nutrition labels | Policies live before App Store submission; nutrition labels match actual data flows in a pre-submission audit |
| C-5 | Data minimization and retention schedule: collect only what generation and coaching need; retention defined per data type; raw GPS processed on-device where feasible (Maryland MODPA necessity standard) | Written data inventory with per-type retention; no collection without a mapped purpose |
| C-6 | Full deletion pipeline: in-app account deletion (Apple requirement) cascading to backups and processors within statutory windows | Deletion request empties user data from primary store, analytics, and processor systems; verified end to end in staging |
| C-7 | Data subject rights tooling: access and export (portability), correction, Global Privacy Control recognition for the GPC states | Export produces a complete machine-readable archive; GPC signal honored where applicable |
| C-8 | No ad tech, no data sales, no cross-app tracking; health and location data contractually and technically walled off from every third-party SDK; SDK audit before each integration (Apple 5.1.3, FTC orders, Maryland sale ban) | SDK inventory with audit record; zero ad or tracking SDKs in the binary; no ATT prompt needed because no tracking exists |
| C-9 | DPAs and processor inventory: Article 28 DPAs with cloud, maps, analytics, AI providers; SCCs or adequacy mechanism for EU-to-US transfers; MHMD processor contracts | Signed DPA on file for every processor before it touches production data |
| C-10 | DPIA plus AI Act classification memo before EU launch; EU and UK representatives appointed if no local establishment | Documents exist and are counsel-reviewed before EU availability |
| C-11 | AI transparency: disclose at first interaction that coaching is AI-generated (EU AI Act Article 50(1), applies 2026-08-02); label AI-generated plans and routes in the UI | Disclosure shown at onboarding and on AI surfaces (RG-F4, AC3-F3); screenshot evidence retained |
| C-12 | Not-medical-advice framing: prominent disclaimer, physician-consultation prompt with red-flag symptom list, assumption-of-risk acknowledgment at onboarding; no disease diagnosis or treatment claims anywhere including App Store copy | Onboarding flow contains all three elements; App Store copy audited against the FDA general wellness lane |
| C-13 | Age gating: 16+ minimum age gate at signup [assumption A2 in the source doc: 16 vs 18 needs a decision record]; no knowing collection of children's data | Age gate blocks under-16 signup; no child-directed content or marketing |
| C-14 | Subscription hygiene: sell via Apple IAP only in v1; disclose price, term, and trial conversion before purchase; cancellation no harder than signup; renewal reminders | Purchase flow shows full terms pre-purchase; category-trust stakes are strategic as well as legal [verified] (`unmet-needs.md` need 10, Marcus is category-burned) |
| C-15 | Security and breach readiness: encryption at rest and in transit, least-privilege access, written incident response plan mapped to FTC HBNR (60-day notice), GDPR (72-hour authority notice), and state breach laws | IR plan exists and is drill-tested before launch; encryption verified in architecture review |

### 5.2 Performance

| ID | Requirement | Label |
|----|-------------|-------|
| NF-P1 | Route generation latency: p50 at or under 5 seconds, p95 at or under 15 seconds from request to first route card, on cellular | [assumption] targets; derived from Priya's 30-second total budget, validated in beta |
| NF-P2 | Cold app open to started, navigable run: under 30 seconds including constraint confirmation (the hotel-lobby promise) | [verified] as the persona requirement (`personas.md` Priya); the engineering budget behind it is [inferred] |
| NF-P3 | Watch cue latency: turn haptic within 1 second of phone cue | [assumption] |
| NF-P4 | Battery: a 2-hour guided run consumes no more battery than category norms for GPS navigation apps; measured against RunGo and Footpath in field tests | [inferred] benchmark approach |

### 5.3 Offline behavior

| ID | Requirement |
|----|-------------|
| NF-O1 | A generated route, its map tiles for a sensible corridor, and all navigation cues are cached on device at generation time; mid-run connectivity loss never interrupts guidance (TM-F3) |
| NF-O2 | Run recording is fully offline; upload (Strava, backend sync) queues and retries when connectivity returns, idempotently (no duplicate activities) |
| NF-O3 | Route generation itself requires connectivity in v1; the offline state says so plainly and offers cached previous routes, never a spinner without diagnosis [inferred scope control; on-device generation is a P2 investigation] |

### 5.4 Accessibility

Baseline: WCAG 2.2 AA plus EN 301 549 Chapter 11 from the first sprint [verified obligation and recommendation] (`regulatory-compliance.md` Section 5: EAA in force since June 2025, purchase and account flows squarely in scope; US ADA litigation references WCAG as the de facto benchmark).

| ID | Requirement |
|----|-------------|
| NF-A1 | Full VoiceOver support on all flows; account, purchase, and subscription management flows meet EN 301 549 without exception (the legally exposed surface) |
| NF-A2 | Respect OS text size (Dynamic Type), contrast, and reduced-motion settings throughout |
| NF-A3 | Audio turn cues double as an accessibility feature (blind and low-vision runners) and a safety feature; haptic alternatives for deaf and hard-of-hearing runners (EX1-F5) |
| NF-A4 | Running-specific, one-handed use: all mid-run actions reachable in the bottom half of the screen, touch targets at or above 44 pt, operable with sweaty fingers and in motion; no mid-run action requires two hands or precise gestures |
| NF-A5 | Running-specific, glare: mid-run and watch screens meet a high-contrast outdoor-legibility standard (contrast ratio at or above 7:1 for mid-run essentials [assumption on the exact ratio]; field-tested in direct sunlight) |
| NF-A6 | Running-specific, motion: no information delivered only via small text while moving; anything a runner must know mid-run is available as audio or haptic; animations respect reduced motion and nothing essential is animation-gated |

### 5.5 Safety-claim language rules (binding on product, marketing, and App Store copy)

The liability stakes are documented [verified] (`unmet-needs.md`: never marketing "safe routes" as a guarantee; `regulatory-compliance.md`: FTC substantiation, disclaimers do not eliminate negligence liability).

| ID | Rule |
|----|------|
| NF-L1 | Never "safe route", "safest route", "keeps you safe", or any wording that states or implies a safety guarantee. Approved framing: "safety-aware", "prefers lit and populated streets", "designed around your preferences" |
| NF-L2 | Every safety-adjacent surface names its data basis and its limits ("based on street lighting and business-hours data, which can be incomplete") |
| NF-L3 | Honest degradation is a language rule too: when safety data is unavailable, the UI says so; silence is a violation (RG-F10, AC3-F2) |
| NF-L4 | No fear-based marketing framing [assumption on brand ethics, flagged in `personas.md` Elena for founder decision; adopted here as the default pending that decision] |
| NF-L5 | Every explicit or implicit claim about what the AI does must be substantiated with evidence before it is made (FTC Operation AI Comply [verified]) |
| NF-L6 | Implementation note: maintain a banned-terms and required-disclosure lint list applied to UI copy and App Store metadata in CI (AC-AC3-2) |

---

## 6. Analytics and success metrics

All instrumentation is privacy-preserving by design: no third-party ad or tracking SDKs (C-8), location aggregated and obfuscated before any metric leaves the device, and a privacy review before shipping any location-derived metric [verified requirement framing] (`unmet-needs.md` Section d). The eight MVP telemetry signals from `unmet-needs.md` Section d are mapped to features below.

| Feature | Activation metric | Retention proxy | Research signal it resolves |
|---------|-------------------|-----------------|------------------------------|
| RG engine | Percent of new users generating a first route within 24 hours; generate-to-run-start rate | Weekly generations per active user; repeat-route rate versus new-route requests (Signal 2, novelty versus loop loyalty) | Is generation the habit loop? |
| Safety awareness | Share of generations with safety or time-of-day constraints active, by local hour bucket (dawn, day, dusk, dark) (Signal 3; coarse buckets only, privacy review required) | Retention of safety-constraint users versus others | Daily driver or occasional mode? |
| Travel mode | Share of generations starting far from home area, per user per month (Signal 1) | Repeat travel-mode use across trips | The activation thesis and the missing travel-x-running cross-tabulation |
| AC-1 training-state generation | Workout-route attach rate: share of generated routes linked to a planned workout (Signal 4) | Completion rate of linked runs versus unlinked runs | The H7 seam: felt value or product-logic fantasy? |
| AC-2 adaptive routines | Plan-start rate among paid users | Post-missed-run behavior: reschedule in-app, generate shorter time-boxed route, or go silent (Signal 5); week-over-week plan adherence | Does plan disruption connect to route intelligence in behavior? |
| AC-3 explainable coach | Explanation open or expand rate | Constraint-trust proxy: safety-constraint reuse after a degraded-data notice [inferred metric design] | Does honesty retain rather than repel? |
| EX-1 and EX-2 execution | Runs started with navigation; watch versus phone execution split (Signal 6) | Mid-run completion rate; route-deviation rate; audio setting distribution | H6 form factor hardening |
| EX-3 Strava share | Connect rate; share rate per run | Ongoing share rate (proxy for Waypoint fitting the runner's existing identity loop) | Does post-to-Strava suffice versus social pull? |
| Weather adaptation | Weather-adjusted route offer acceptance versus override (Signal 7) | Seasonal retention stability | Need 9: felt value once surfaced? |
| Monetization | Paywall encounter-to-conversion by triggering feature (Signal 8) | Renewal rate (post-v1 horizon) | Revealed willingness to pay; feeds Phase 6 pricing |
| Product-level | G3 (re-based, DEC-012): 40 percent complete a generated route as a recorded run within 7 days; Ignition as the daily leading indicator | G4 (re-based, DEC-012): 25 percent day-30 retention of the activated cohort, plus an 8 to 12 percent install-level benchmark line; D1, D7, D30 cohort curves | Overall thesis. North Star and the full metric tree live in `../06-business-model/metrics.md` |

What telemetry cannot resolve, interviews stay mandatory [verified] (`unmet-needs.md` Section d): trust formation for safety claims (a user who never installs never appears in telemetry), pre-adoption workarounds and switching triggers, price framing before launch.

---

## 7. Explicitly out of scope for v1

| Item | One-line reason |
|------|-----------------|
| Android app | iOS-first is locked (DEC-006); Android is the first expansion step post-traction |
| Social feed, community, clubs | Non-goal: post TO Strava, never compete with the social graph |
| Route content library or curation | Non-goal: generate, do not curate |
| Multi-sport (cycling, hiking, walking) | Expansion surface for later; same engine, different constraint weights, post-traction |
| Garmin (and Coros, Polar, Suunto) integrations | Garmin's developer program is paused [verified]; HealthKit-first is the locked data posture |
| Strava data ingestion (reading activities, heatmaps, segments) | Strava's API bans AI and ML use of its data [verified]; the moat is data Waypoint builds |
| Crime-data-based safety scoring | Unresolved redlining and fairness exposure (OQ-RG-3); lighting and population signals only in v1 |
| Public heatmaps, flybys, proximity features | Documented deanonymization vectors (Strava and NRK incidents [verified]); contradicts C-2 |
| Standalone watch-only execution (no phone) | P2: mirroring ships first; a native watch engine is a separate effort |
| Free-form conversational coach chat | P2: explainability ships as structured explanations first; chat is cost and moderation surface |
| On-device offline route generation | P2 investigation; v1 caches generated routes instead (NF-O3) |
| Web app or web checkout | Apple IAP delegates subscription mechanics (C-14); a web funnel reopens EU withdrawal-button and state ARL duties [verified] |
| Human coach marketplace | Non-goal adjacent: Waypoint's coach is the product; marketplaces are a different business |
| EHR or EHDS interoperability claims | Regulatory monitor-only until at least 2029 [verified] (`regulatory-compliance.md` Section 2) |
| Localization beyond English | iOS English-first is the locked sequence (DEC-006 via `concept.md` Section 6) |

---

## 8. Assumptions (collected)

- A1: **Partly resolved.** G3 and G4 were re-based against category benchmarks by DEC-012 (see section 1.3); the definitions are now settled and the numbers are benchmarked. G2's 3,000 MAU and NF-P1's latency figures remain unbenchmarked working numbers to be re-baselined at beta. [assumption]
- A2: The crossing graph and lighting scoring are buildable from open data at solo-founder scale (concept assumption A3); the stack recommendation must validate with a technical spike before this PRD's constraint table is credible. [assumption]
- A3: Tier labels (free anchor, paid adaptive) anticipate the Phase 6 boundary decision; the safety-free-tier question (Elena ethics flag) can move features across the paywall without changing their requirements. [assumption]
- A4: Distance tolerance (5 percent), candidate count (3), cue distances (80 to 30 m), and contrast ratio (7:1) are engineering placeholders to be tuned in beta. [assumption]
- A5: Workout-type-shaped generation (AC-1 at P0) is enough paid-seam surface to test monetization without full adaptive plans (AC-2 at P1); `mvp-scope.md` and RICE scoring pressure-test this. [assumption]
- A6: The 16+ age floor (C-13) follows the compliance document's assumption A2 and still needs its own decision record. [assumption]

## 9. Open questions for the founder (consolidated)

1. Free-tier boundary for safety-aware routing: charging women a safety premium is an ethics and brand decision, deferred to Phase 6 by DEC-006 but shaping tier architecture now; the defensible default is safety in the free tier (`personas.md` Elena). Needs a decision record.
2. Age floor 16+ versus 18+ (C-13, liability versus reach). Needs a decision record.
3. Redlining and fairness exposure of safety scoring (OQ-RG-3): commission counsel review plus a fairness design review before launch; v1 excludes crime data, but lighting and population signals still steer.
4. Technical spike on the proprietary constraint data (A2 above): which launch regions get crossing and lighting coverage, and what does the build cost at solo-founder scale?
5. Live location sharing (EX2-F3): safety value versus deanonymization vector; privacy design review decides P1 inclusion.
6. Calibration methodology source for AC-2 (OQ-AC2-1): published science, licensed methodology, or advisor; gates coach credibility and FTC substantiation.
7. Strava upload terms re-read at build time (OQ-EX3-1): confirm write-only upload from an AI-generation app is clean.
8. Data licensing for safety-critical use (OQ-RG-2): audit lighting and weather licenses before integration.
9. Fear-free marketing rule (NF-L4): adopted as default here; founder should ratify it as brand policy.
10. Interview program (Priorities 1 and 2, `unmet-needs.md` Section c) runs alongside Phase 5: H1 base rate, bundling, safety trust. Results recalibrate tiers and copy, not the concept.

## Related

- `research/04-synthesis/concept.md` (governs this document), `research/03-users/personas.md`, `research/03-users/unmet-needs.md`, `research/02-competitors/feature-matrix.md`, `research/01-market/regulatory-compliance.md`
- Companions in this folder: `rice-prioritization.md`, `mvp-scope.md`, `user-journeys.md`, `stack-recommendation.md`
