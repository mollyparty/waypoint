> Version-Timestamp: 2026-08-06 11:55:00 UTC-4

# Metrics: North Star, Metric Tree, and Instrumentation

Status: DRAFT for the Phase 6 gate. Governed by the locked concept (`research/04-synthesis/concept.md`, DEC-006), the approved MVP scope (DEC-008), and the staged cross-platform plan (DEC-010). Builds on, and does not replace, the analytics section of `research/05-product/prd.md` (Section 6); where this document changes a PRD target, the change is called out explicitly in Section 7.2.

**Executive summary.** The North Star is **Weekly Routed Runners (WRR)**: the count of distinct runners who complete two or more Waypoint-generated routes in a rolling seven days. It is the sharpest available proxy for the one hypothesis the MVP exists to test (committed amateurs will adopt and return for constraint-based route generation), because it cannot rise unless people generate, trust, run, and come back inside a single week. Raw MAU, total routes generated, and total distance run are rejected below, each with its failure mode; the second of those is disqualified because it rises when the product's core risk (bad routes) materializes. Activation is defined as **first Waypoint-generated route completed as a recorded run within seven days of install**, with the onboarding journey's "first route on screen inside three minutes" demoted to a daily-readable leading indicator called Ignition. The section that matters most is route quality (Section 5): because runners will rarely rate anything, quality is read from regeneration, silent abandonment at the reveal, mid-run abandonment, deviation, and repeat, combined into one weekly number, the **Good Route Rate**. Guardrails protect safety weighting, privacy architecture, generation latency, and segment mix from a naive push on the North Star. Targets are set for four stages and are honest about which are sourced and which are judgment. The instrumentation plan fits roughly fifteen event types, computes every location-derived and health-derived quantity on device, and emits only scalars. Five genuine tensions with the privacy architecture are named and resolved in Section 9, the sharpest being that cohort retention needs a stable per-user identifier that the recommended no-PII analytics vendor deliberately does not provide.

**How to read this document.** [verified] traces to a sourced external claim or to a sourced finding in a prior Waypoint research document, with the citation inline. [inferred] is a reasoned conclusion from verified inputs. [assumption] is an unvalidated working belief, collected in Section 12. Every metric is labeled **actionable** (a number that names a next move) or **diagnostic** (a number that only explains another number). External benchmark sources are listed in full in Section 14, all accessed 2026-08-06.

---

## 1. What is being measured, and why

### 1.1 The one thing

`research/05-product/mvp-scope.md` states the MVP's purpose in one line: prove that committed amateur runners will adopt and return for constraint-based route generation. It also states the risk: "the real MVP risk is bad routes, not missing features" [verified, `mvp-scope.md` Section 6]. Those two sentences define the job of this document. A metric plan that reports growth but cannot detect route quality collapse is a failed metric plan, so route quality is treated here as a first-class measurement design problem rather than a satisfaction survey.

Three facts about the first year shape everything below.

1. **v1 launches entirely free** and the paid layer arrives in v1.x at month 10 to 12 [verified, DEC-008 decision 2]. Revenue is therefore not the scoreboard in year one. Retention and route quality are.
2. **Two platforms ship on a stagger**: iOS at month 9 to 10, Android at month 10 to 12 [verified, DEC-010]. Every cohort metric must be locked to (platform, install week) or the Android cohort will drag the iOS retention read downward for reasons that have nothing to do with the product.
3. **Privacy is architecture, not a feature.** Health data never leaves the device, location is treated as sensitive end to end, and no ad or tracking SDK enters the binary [verified, `prd.md` C-1, C-5, C-8]. Instrumentation is designed inside that constraint, not around it.

### 1.2 Relationship to the PRD and to the Phase 3 telemetry signals

`prd.md` Section 6 already maps eight telemetry signals from `research/03-users/unmet-needs.md` Section d onto features. This document keeps all eight, gives them precise definitions and owners, and sequences them, because instrumenting all eight at launch would produce a dashboard the founder does not read.

| Phase 3 signal | Where it lives here | Launch priority |
|---|---|---|
| 1. Travel-mode share (generations far from home) | Section 4 acquisition, Section 9 tension 2 | v1 launch, as an on-device boolean only |
| 2. Novelty versus loop loyalty (repeat versus new) | Section 5, route quality (repeat is a positive quality signal, not only a novelty signal) | Walking skeleton |
| 3. Safety-constraint usage by hour bucket | Section 6, safety guardrail | v1 launch |
| 4. Workout-route attach rate | Section 4 revenue, Section 7 paid-layer gate | v1.x with the paid layer |
| 5. Post-disruption plan behavior | Deferred | v2, with adaptive routines |
| 6. Execution and form factor (watch versus phone, deviation, completion) | Section 5, route quality proxies | Walking skeleton (deviation and completion), v1.x (watch split) |
| 7. Weather-adaptation acceptance | Deferred | v1.x with H-06 |
| 8. Revealed willingness to pay (paywall encounter to conversion) | Section 4 revenue, Section 7 stage 4 | v1.x with the paywall |

Signals 5 and 7 attach to features that do not exist in v1 (`mvp-scope.md` Sections 3 and 4), so instrumenting them at launch would measure nothing. They are named here so they are not lost.

---

## 2. The North Star metric

### 2.1 Definition

**Weekly Routed Runners (WRR): the number of distinct runners who completed two or more Waypoint-generated routes within a rolling seven-day window.**

Implementable definition, term by term:

| Term | Precise meaning |
|---|---|
| Runner | A distinct installed profile with an account (Sign in with Apple or email/passkey, `api-integration-map.md` 4.2). Multi-device users collapse to one account. |
| Waypoint-generated route | A route produced by the generation engine, including a previously saved Waypoint route being re-run. Freeform runs (start tracking, no route) never count. |
| Completed | The recorded run reached at least 80 percent of the generated route's planned distance AND ended through the normal finish flow rather than being discarded. Both quantities are computed on device. |
| Two or more | The habit threshold. It is what makes WRR a return metric rather than a usage metric. |
| Rolling seven days | Reported for ISO weeks; the window matches the target segment's stated cadence of 3 to 5 runs per week (`research/03-users/personas.md`, Marcus) [verified]. |

**Reading form.** WRR is a count, which is what a North Star should be at scale. Below roughly 500 activated users it is statistically useless as a count, so during the walking skeleton and the first launch weeks the same metric is read in its rate form: **WRR rate = WRR divided by activated users who installed at least 14 days ago**. The count is the business number; the rate is the product number, and the rate is what gets read weekly for the whole of year one.

**Staggered-launch rule.** WRR is reported as one total (business view) and always also split by platform-launch cohort (product view). No retention or activation rate is ever quoted across a blended iOS plus Android population. See Section 7.4.

### 2.2 Why this metric

Waypoint's value moment is not the route on the screen. It is the run that happened because of the route on the screen, repeated. WRR is the only formulation found that requires all four links of the hypothesis chain inside one window: the runner generated (adoption), trusted the output enough to go outside (acceptance), finished what was generated (quality), and did it again within days (return). Amplitude's own test for a good North Star is that it starts from the customer's value moment, expresses it as a measurable behavior, is time-bound, and is a leading rather than lagging indicator [verified] (Amplitude, "What Makes a Good vs Bad North Star Metric", https://amplitude.com/blog/good-bad-north-star-metric, accessed 2026-08-06). WRR satisfies all four.

Two deliberate inclusions are worth defending.

- **Re-runs of saved routes count.** Excluding them would push the product toward novelty at all costs, and re-running a route the engine produced is one of the strongest unprompted quality endorsements available (Section 5.3). The fresh-versus-repeat split is preserved as an input metric, not as a filter on the North Star.
- **The 80 percent completion floor is inside the North Star, not in a separate quality dashboard.** This is the single most important design choice in this document. It means the North Star mechanically cannot be inflated by shipping more routes that people abandon.

One deliberate exclusion: WRR ignores the runner who does exactly one generated run per week. That is a real segment (Elena's dark-hours cadence can be twice a week, Priya's travel cadence is monthly) and dropping it entirely would be blind. The companion breadth metric **Weekly Routed Runners (1+)** is tracked alongside, as diagnostic. If the ratio WRR / WRR(1+) falls persistently below roughly 0.45, the product is acquiring people it does not convert into a habit [assumption on the ratio, re-baseline after twelve launch weeks].

### 2.3 Alternatives considered and rejected

| Rejected candidate | Superficial appeal | Failure mode |
|---|---|---|
| **Monthly active users (MAU)**, including the PRD's G2 target of 3,000 MAU | Simple, investor-legible, already in the PRD | It counts opens, not value. A user who opens the app, looks at a map, and leaves is indistinguishable from Marcus. It is inflatable by launch press and by the Android launch, and its monthly window hides a collapsing weekly cadence for up to four weeks in a product used 3 to 5 times per week. MAU is retained as a business reporting number for G2 and the seed conversation, and is explicitly demoted from steering (Section 10). |
| **Total routes generated** | It is the hero feature, so counting it feels right | Disqualifying: it counts the act of asking, not the act of being satisfied, and **it rises when routes are bad**, because rejection produces regeneration. A team optimizing it would ship a product that generates more and delivers less. Any metric that moves in the same direction as the project's number-one risk cannot be the North Star. It survives only as the denominator of the route-quality ratios in Section 5. |
| **Total distance run, or total runs tracked** | Big, healthy-sounding, easy to instrument | It measures whether people run, not whether Waypoint's hero feature is why. A cohort using Waypoint purely as a GPS tracker on their own known loops would score perfectly while refuting the hypothesis, and would push the product toward the tracker category that DEC-006 explicitly rules out (`concept.md` Section 7) [verified]. |
| **Day-30 or week-4 retention rate** | It is the actual bar in gate decision GD-1 | Wrong shape for a North Star: it is a rate rather than an output, it can only be read 28 days late, and it counts a user who opened the app identically to a user who ran a generated route. It is the single most important **input** metric (Section 3) and the gate for the paid layer (Section 7.4), not the summit. |

---

## 3. The metric tree

The North Star is an output nobody can move directly. Below it sit five inputs, each of which a founder-plus-two-contractors team can actually push, and each of which has a named response when it moves. Amplitude's guidance is 3 to 5 inputs following a breadth, depth, frequency, efficiency pattern [verified] (Amplitude, "Every Product Needs a North Star Metric", https://amplitude.com/blog/product-north-star-metric, accessed 2026-08-06). Five are used here because route quality splits into two structurally different gates (accept, then complete).

```
                        WEEKLY ROUTED RUNNERS (WRR)
     distinct runners completing 2+ generated routes in a rolling 7 days
                                    |
   +-------------+-------------+----+--------+-------------+-------------+
   |             |             |             |             |             |
 [I1]          [I2]          [I3]          [I4]          [I5]
ACTIVATED     GENERATION    ACCEPTANCE    COMPLETION    RETENTION
  BASE        FREQUENCY      (quality      (quality     (durability)
 (breadth)     (depth)        gate 1)       gate 2)
   |             |             |             |             |
   |- installs   |- gens per   |- first-     |- route      |- wk-4 retention
   |  (qualified)|  active     |  route      |  completion |  of activated
   |- activation |  runner/wk  |  acceptance |  rate       |  cohort
   |  rate (7d)  |- novelty    |- regens per |- mid-run    |- wk-12 retention
   |- reactivation  supply     |  accepted   |  abandon    |- dormancy
   |  of dormant |  (unrun     |  route      |  rate       |  return rate
   |             |  street %)  |- reveal     |- on-route   |
   |             |- constraint |  abandon    |  adherence  |
   |             |  breadth    |  rate       |             |
```

| # | Input | Definition | Type | If it moves, do this |
|---|---|---|---|---|
| I1 | **Activated base** | Distinct runners who have ever activated (Section 4.2) and are not dormant beyond 60 days | Actionable | Down: the problem is onboarding or recruitment, not the engine. Fix the first-session funnel before touching routing. Up with WRR flat: you are acquiring the wrong people (see the segment-mix guardrail, Section 6). |
| I2 | **Generation frequency** | Generation sessions per activated runner per week (a session is one constraint set, however many regenerations it contains) | Actionable | Falling with acceptance and completion healthy means the runner is not thinking of Waypoint on run day: it is a trigger and habit problem (widget, plan-day prompt, pre-generation on travel arrival), not a routing problem. |
| I3 | **Acceptance** | Share of generation sessions that end in a started run, and the number of regenerations required to get there | Actionable | The primary route-quality alarm. Falling acceptance means the first route is not credible. Response is engine and constraint-data work, cut by metro (Section 5). |
| I4 | **Completion** | Share of started routed runs that finish at 80 percent or more of planned distance through the normal finish flow | Actionable | Falling completion with healthy acceptance means routes look good and run badly: navigation, surface, crossings, or map accuracy on the ground. Response is field-testing the failing routes, not the reveal screen. |
| I5 | **Retention** | Week-4 retention of the activated cohort, measured as completing at least one routed run in days 22 to 28 after activation | Actionable, slow | The paid-layer gate (GD-1). Falling while I3 and I4 hold means the product works but does not earn a place in the week: look at novelty supply exhaustion and trigger design. |

Multiplicatively, WRR is approximately: activated base times the share generating in a week times acceptance times completion, filtered by the two-runs-per-week habit threshold. That identity is the debugging path: when WRR stalls, walk left to right and the first input that broke is the one to fix.

---

## 4. Lifecycle metrics

Five stages, deliberately thin. Each stage carries at most three numbers, because a solo founder cannot act on more.

### 4.1 Acquisition

| Metric | Definition | Type | Notes |
|---|---|---|---|
| Qualified installs | Installs from a store listing, split by platform and by source where the store console provides it | Diagnostic | Store console only (App Store Connect, Play Console). No attribution SDK exists in the binary and none will be added (`prd.md` C-8) [verified]. |
| Listing conversion rate | Product page views to installs, per platform | Actionable | The only acquisition lever that is free to pull pre-spend: screenshots and the first three lines of copy. |
| Travel-generation share | Share of activated runners with at least one far-from-home generation in the trailing 30 days (Phase 3 signal 1) | Diagnostic | Settles the H1 reframe with behavior rather than recall (`hypotheses-review.md` H1) [verified]. Computed as an on-device boolean, see Section 9. |

Acquisition is deliberately the least instrumented stage of the five. Until retention clears the bar in Section 7, spending attention on the top of the funnel is a way of avoiding the question the MVP exists to answer.

### 4.2 Activation (the highest-leverage definition in the product)

**Definition: a new user is Activated when they complete their first Waypoint-generated route as a recorded run, within seven days of install.** Reported as the seven-day activation rate on weekly install cohorts, split by platform.

The argument, since this definition sets what the whole team optimizes:

- **Why not account creation?** v1 defers authentication until first save (`user-journeys.md` Journey 1, stage 1) [verified], so account creation is neither early nor meaningful. It measures a wall, not a value moment.
- **Why not first route generated?** This is the tempting choice, because the onboarding journey's contract is "install to first generated route in under 3 minutes" [verified, `user-journeys.md` Journey 1]. But a generated route is a request fulfilled, not value received. It counts the user who looks at a bad loop and closes the app, which is precisely the population the MVP most needs to see. Calling that user activated would make the number rise as route quality falls, the same defect that disqualifies "total routes generated" as a North Star.
- **Why not first route started?** Closer, and it is the PRD's current G3 ("generate a route and start a run within 7 days") [verified, `prd.md` G3]. It still stops one step short of the truth: starting and abandoning is the exact signature of a bad route (Section 5.2). An activation definition that treats abandonment as success blinds the one measurement the founder cannot afford to lose.
- **Why completion, and why seven days?** Completion is the first moment the promise has been kept on the ground rather than on a screen. Seven days is chosen because installs frequently happen away from a run occasion (evening discovery, App Store browsing, a friend's recommendation over dinner), and the target segment runs 3 to 5 times per week, so a seven-day window contains at least one natural run occasion for essentially every target user [inferred from segment cadence, `personas.md`]. A 24-hour window would measure timing luck; a 30-day window would be unreadable during the beta.

**The cost of this definition, and the fix.** Activation now takes up to seven days to read, which is too slow to steer a build week. The fix is a named, daily-readable leading indicator:

> **Ignition (diagnostic): the share of first sessions that reach a generated route on screen, and the median seconds from first open to that route.** Target: 70 percent or more of first sessions reach a route, median under 180 seconds, matching the journey's three-minute budget [verified as the design budget, `user-journeys.md` Journey 1].

Ignition is the onboarding team's number. Activation is the product's number. The gap between them (routes seen but never run) is itself the most useful single diagnostic in the first launch month, because it isolates "we cannot get people to a route" from "our routes do not get run".

**Validate the definition rather than assume it.** With the walking-skeleton cohort of 20 to 50 TestFlight runners, run the comparison directly: for each candidate step (route seen, route started, route completed, two routes completed), measure week-4 retention of the users who reached it. Adopt whichever step best separates retained from churned users. This is cheap at n=40 (it can be done by hand) and it converts the definition from a judgment into a finding. If "first route started" turns out to predict retention as well as "first route completed", switch, and record it as a decision.

**Supporting activation metrics (both actionable):** location permission grant rate at the pre-permission screen (the journey's named moment of truth 1), and first-session route acceptance rate (the same quality gate as I3, restricted to first sessions, since one bad first route confirms the skeptic's prior, `user-journeys.md` Journey 1 moment of truth 2) [verified].

### 4.3 Retention

| Metric | Definition | Type |
|---|---|---|
| **Week-4 retention of activated cohort** | Share of activated users who complete at least one routed run in days 22 to 28 after activation | Actionable (the paid-layer gate) |
| Week-12 retention of activated cohort | Same, days 78 to 84 | Diagnostic (the durability read) |
| Install-level D30 | Share of installs with any app open on days 29 to 31 | Diagnostic (the only figure comparable to public benchmarks) |
| Retention curve flatness | Whether the activated cohort curve flattens rather than decaying toward zero between weeks 4 and 12 | Diagnostic, and the truest product-market-fit read available pre-revenue [verified as the standard interpretation] (Amplitude, North Star and retention material, https://amplitude.com/blog/product-north-star-metric, accessed 2026-08-06) |

Two definitional insistences. First, retention is measured on **routed runs, not app opens**. An open-based retention curve for this product would flatter it substantially and teach nothing. Second, retention is measured on the **activated cohort**, not on installs, everywhere except the single benchmark-comparable line. Section 7.2 explains why the PRD's current 25 percent day-30 target needs re-basing onto the activated cohort to be achievable at all.

### 4.4 Referral

Waypoint has no social graph by design (`concept.md` Section 7) [verified], so referral is measured in exactly two places and nowhere else.

| Metric | Definition | Type |
|---|---|---|
| Strava share rate | Share of completed routed runs posted to Strava, per user per month | Diagnostic |
| Organic install share | Installs attributable to App Store or Play search and browse rather than any owned channel, from the store consoles | Diagnostic |

Neither is actionable at v1 scale, and neither should be optimized. They are read monthly at most. A rising share rate with flat organic installs simply means Waypoint fits the runner's existing identity loop, which is the strategic intent (`gap-analysis.md` via `concept.md`, feed Strava, never compete with it) [verified].

### 4.5 Revenue

Nothing here is measured until v1.x. The stage exists in this document so the instrumentation is designed for it, not bolted on.

| Metric | Definition | Benchmark anchor |
|---|---|---|
| Paywall encounter to conversion, by triggering feature | Phase 3 signal 8 | Health and Fitness median download-to-paid is 2.9 percent, top quartile above 6.2 percent; freemium apps specifically convert at a 2.1 percent median by day 35 against 10.7 percent for hard paywalls [verified] (RevenueCat, State of Subscription Apps 2026, https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/, accessed 2026-08-06) |
| Trial start rate and trial-to-paid | Share of paywall viewers starting a trial; share of trials converting | Health and Fitness medians: 7.2 percent trial start, 37.7 percent trial-to-paid [verified as reported] (The-Diff subscription benchmark calculator, presenting RevenueCat State of Subscription Apps 2026 data, https://tools.the-diff.com/health/, accessed 2026-08-06) |
| Workout-route attach rate | Phase 3 signal 4: share of generated routes linked to a planned workout, and the completion delta of linked versus unlinked runs | No external benchmark exists; this is the H7 seam test (`hypotheses-review.md` H7) [verified] |
| First renewal | Share of subscriptions surviving the first renewal | Health and Fitness medians: 57.0 percent monthly, 36.0 percent annual [verified as reported] (The-Diff calculator, same source and date) |

Note for Phase 6 pricing work: RevenueCat's 2026 data shows freemium's conversion disadvantage against hard paywalls (2.1 percent versus 10.7 percent at day 35) largely disappears in year-one subscriber retention (28 percent versus 27 percent) [verified] (RevenueCat, same source and date). That materially supports the GD-1 decision to launch free, and it belongs in `revenue-model.md`, not here.

---

## 5. Route quality: the section that matters most

### 5.1 The measurement problem

Runners will not rate routes. Any design that depends on explicit feedback will produce a tiny, self-selected sample dominated by people angry enough to tap. So route quality has to be inferred from what runners do anyway. Fortunately, running a generated route is an unusually informative behavior: it costs 30 to 90 minutes of physical effort, which means every observed acceptance, completion, and repeat is an expensive vote, and every abandonment is an expensive complaint.

The signals below are ordered by information value per unit of instrumentation cost. All are computed on device from data the app already holds.

### 5.2 What a runner does when a route is bad

| # | Behavior | Metric | Type | Interpretation and caution |
|---|---|---|---|---|
| B1 | Taps "try another" | **Regeneration rate**: share of generation sessions requiring two or more generations before a start or an abandon. Companion: **generations per accepted route** (mean) | Actionable | The cheapest and fastest quality signal in the product, available from the walking skeleton. Caution: a small amount of regeneration is healthy browsing, not rejection; the shape of the distribution matters more than the mean (see thresholds). |
| B2 | Looks at the route and leaves | **Reveal abandon rate**: share of generation sessions with no start and no regeneration within 30 minutes | Actionable | The quietest and possibly most damning signal. A user who regenerates is still engaged; a user who closes the app after one reveal has silently concluded the product does not work. Emitted on device after the timeout, not at the moment of closing. |
| B3 | Starts, then quits early | **Early abandon rate**: share of started routed runs ending before 25 percent of planned distance | Actionable | Distinguish from life interruptions by checking whether a new run started within two hours. Persistent early abandonment concentrated in one metro is a routing-data problem, not a user problem. |
| B4 | Leaves the line | **Off-route share**: share of route distance run outside a 40 meter corridor, after discarding GPS-gap segments. Companion: **manual reroute taps per run** | Diagnostic | Genuinely ambiguous: it can mean a bad route, a missed turn, a closed path, or personal preference. Never read alone. Read as a pair with B3 (deviation plus abandonment equals bad route; deviation plus completion equals a route the runner improved, which is a preference-learning opportunity, `concept.md` Section 5 learning loop) [verified]. |
| B5 | Never comes back | **First-route churn**: week-4 retention of activated users whose first generated route carried a bad signature (B1 to B4), against those whose did not | Diagnostic, slow, decisive | The most important number in the whole document and the slowest to read. It is the direct measurement of the claim in `user-journeys.md` that one bad first route confirms the skeptic's prior [verified]. |
| B6 | Says so | **Flag rate**: pre-run "avoid this street" flags, mid-run safety flags, post-run one-tap negative | Diagnostic | Sparse but high-information, and load-bearing for Elena's journey. Do not build a rating funnel to raise the sample size; the volume is the point, in that a rising flag rate is always worth reading by hand. |

### 5.3 What a runner does when a route is good

| # | Behavior | Metric | Type |
|---|---|---|---|
| G1 | Runs the whole thing | **Route completion rate** (the 80 percent floor, as in the North Star) | Actionable |
| G2 | Keeps it | **Save rate**: share of completed routed runs saved for re-run | Actionable |
| G3 | **Runs it again** | **Repeat rate**: share of generated routes re-run at least once within 30 days | Actionable, and the strongest single positive proxy available |
| G4 | Posts it | Strava share rate on routed runs | Diagnostic (confounded by habitual sharers) |
| G5 | Comes back for another | **Return-to-generate**: share of completed routed runs followed by a new generation within seven days | Actionable |

G3 deserves the emphasis. Re-running costs the runner nothing to skip, carries no social performance, and cannot be prompted without contaminating it. If runners re-run generated routes, the engine produced something worth keeping. It is also the cleanest counterweight to a novelty-obsessed reading of the product, which is why the North Star counts re-runs.

### 5.4 The one number: Good Route Rate

Six bad signals and five good ones are too many to read weekly. They collapse into one:

> **Good Route Rate (GRR): the share of generation sessions that end in a completed run on a route accepted within the first two generations.**

GRR is the single number that answers "are the routes good enough". It falls when routes are rejected (B1, B2), when they are abandoned (B3), and when they are never started, and it is insensitive to how many people are using the app, which makes it readable from the walking skeleton onward. Everything in 5.2 and 5.3 is its diagnostic decomposition: when GRR falls, the sub-metrics say whether the failure is at the reveal or on the road.

**Segment GRR by area before reading it in aggregate.** Route quality will not fail uniformly. It will fail where OpenStreetMap tagging is sparse, where the elevation model is thin, and where lighting data does not exist, which is exactly the risk flagged in gate decision GD-3 and assumption A3 (`mvp-scope.md` GD-3) [verified]. A healthy portfolio GRR can hide a metro where the product is broken. The privacy-safe way to cut it is in Section 9.

### 5.5 Thresholds: what should worry the founder

These are judgment calls, not benchmarks. No public benchmark exists for route regeneration rates, because no competitor ships constraint-based generation (`gap-analysis.md` H2 verdict) [verified]. They are set at the level where the founder should stop feature work and investigate, and every one of them should be re-baselined after twelve weeks of real cohort data [assumption].

| Metric | Healthy | Investigate | Stop feature work |
|---|---|---|---|
| First-route acceptance rate | 70 percent or above | Below 60 percent | Below 50 percent |
| Generations per accepted route (mean) | Below 1.4 | 1.4 to 1.8 | Above 1.8 |
| Sessions reaching 3 or more generations | Below 10 percent | 10 to 15 percent | Above 15 percent |
| Reveal abandon rate | Below 20 percent | 20 to 30 percent | Above 30 percent |
| Route completion rate | 85 percent or above | 75 to 85 percent | Below 75 percent |
| Early abandon rate (under 25 percent of distance) | Below 5 percent | 5 to 10 percent | Above 10 percent |
| **Good Route Rate** | **65 percent or above** | **50 to 65 percent** | **Below 50 percent** |
| Any single metro's GRR versus portfolio median | Within 10 points | 10 to 15 points below | More than 15 points below |
| First-route churn gap (B5) | Under 10 points | 10 to 20 points | Above 20 points |

The bottom two rows are the ones that change strategy rather than the backlog. A metro more than 15 points below the median says the constraint-data build has failed for that metro, which is the GD-3 fallback trigger (ship time-of-day heuristics with honest degradation and rebuild the data layer) rather than an engine problem. A first-route churn gap above 20 points says the first route is deciding retention on its own, which would justify spending engineering time on first-route conservatism (prefer a boring, certain route for a new account over a clever one).

---

## 6. Counter-metrics and guardrails

Every North Star can be gamed, including by an honest team under pressure. These are the numbers that must not move in the wrong direction while WRR moves in the right one. Each has a threshold that triggers a stop, not a discussion.

| # | Guardrail | What it protects against | Threshold and action |
|---|---|---|---|
| **GR1 (safety)** | **Honest-refusal rate holds steady at constant data coverage.** Share of generation sessions ending in "no route meets your constraints" (RG-F10) | The most likely way to raise acceptance and GRR is to quietly relax constraints when the engine struggles. That converts an honest refusal into a pretender route, which is the exact behavior `personas.md` says would destroy Elena's trust [verified] | If the refusal rate falls more than 30 percent without a matching improvement in data coverage, treat it as a regression and audit the constraint-relaxation path. Never set a target of zero refusals. |
| **GR2 (safety)** | **Dark-hours safety weighting share does not fall.** Share of generations in the local dark bucket with safety weighting active (Phase 3 signal 3) | A UI redesign that raises speed by burying the safety control would show up as faster generation and higher acceptance, and would silently disable the strongest-evidence user need | Any month-over-month fall above 10 points blocks the release that caused it. |
| **GR3 (safety)** | **Mid-run safety flags per 1,000 dark-hours kilometers, trending down per area** | Route scoring that degrades quietly as OSM data ages | Any upward trend over three consecutive weeks in a metro triggers a data-freshness review. Individual flags are read by hand, always. |
| **GR4 (privacy)** | **Zero location or health egress regressions.** Automated release-blocking test asserting no true in-privacy-zone start point appears in any exported, uploaded, or server-logged artifact (C-1), plus a count of third-party SDKs with location or health access, which must remain zero (C-8) | The single unrecoverable failure for this brand (`user-journeys.md` Journey 4, moment of truth 3) [verified] | Binary. A non-zero result blocks the release. This is a metric in the sense that it is reported weekly with a number that is always zero. |
| **GR5 (privacy)** | **Analytics payload audit: zero free-text and zero high-cardinality fields in the shipped event schema** | Instrumentation drift, where a well-meaning debug property starts carrying coordinates or place names | Reviewed at every release. Any new event property requires the privacy classification in Section 8.2 before it ships. |
| GR6 (speed) | Generation latency p95 under 15 seconds, p50 under 5 seconds (NF-P1) | Buying route quality with search time, which breaks the 30-second hotel-lobby promise that is the activation moment | A quality change that pushes p95 above 15 seconds is reverted regardless of its GRR gain. |
| GR7 (trust) | Upsell dismissal rate and notification opt-out rate (v1.x) | Raising trial starts by nagging, in a category with documented billing distrust (`gap-analysis.md` unmet need 7) [verified] | If trial starts rise while dismissal or opt-out rises faster, the upsell is a tax, not an offer. Remove it. |
| GR8 (segment) | Share of new activated users who reach 3 or more runs per week by week 4 | Growth that inflates the funnel with people outside the target segment and then reports a retention collapse as a product failure | If the share falls below roughly 40 percent while installs rise, the acquisition channel is wrong, not the product [assumption on the level]. |
| GR9 (novelty versus quality) | Unrun-street share and completion rate, read together | Pushing novelty into roads that should not be run, which is the documented incumbent failure ("12 miles of very unsafe roads", `gap-analysis.md` via `personas.md`) [verified] | Rising novelty share with falling completion is a stop condition for the novelty weighting. |
| GR10 (Android reliability) | Share of runs with a GPS gap longer than 60 seconds, per platform | The known Android background-location survival problem against OEM battery killers (DEC-010) [verified] | Above 2 percent on Android blocks the Android launch. Tracked from the first Android internal build. |

GR1 is the most important guardrail in the document, and the least obvious. A product whose honest refusals quietly disappear looks like a product that got better.

---

## 7. Targets by stage

Targets are labeled **sourced** (traceable to an external benchmark) or **judgment** (set by reasoning, to be re-baselined). Most are judgment, because no competitor ships this feature and therefore no benchmark exists for the metrics that matter most.

### 7.1 Stage 1: Walking skeleton, month 3 to 4, 20 to 50 TestFlight runners

At n=40, a percentage carries roughly plus or minus 15 points of noise, so **rates are not the instrument at this stage: counts and hand-reading are** [inferred]. The single highest-information activity of this stage is the founder personally reading ten generation sessions per week end to end, including the resulting GPS trace. That is a metric practice, not a vibe.

| Metric | Target | Basis |
|---|---|---|
| Testers completing a generated route in week 1 | 25 of 40 or better | Judgment |
| Median time to first generated route | Under 180 seconds | Design budget, `user-journeys.md` Journey 1 [verified as the budget] |
| Good Route Rate | 50 percent or above | Judgment; below this, the skeleton has not yet answered its question |
| Generations per accepted route | Below 2.0 | Judgment, loosened from the launch threshold because early engines are rough |
| Hard safety failures | Zero routes routed onto limited-access roads, or across a motorway junction, in the whole beta | Binary, non-negotiable; this is the incumbent's documented failure and one instance in a 40-person beta predicts many at scale [verified for the failure mode] |
| Runs with a GPS gap over 60 seconds | Under 2 percent (iOS) | Judgment, becomes GR10 for Android |
| Hand-read sessions | 10 per week | Practice, not a target |

The skeleton's job per `mvp-scope.md` Section 6 is to smoke out the routing-quality risk [verified]. If GRR cannot reach 50 percent with 40 friendly testers in two or three launch metros, the scope conversation changes before feature-complete beta, which is exactly what the month 3 to 4 checkpoint exists for.

### 7.2 Stage 2: iOS launch, month 9 to 10

| Metric | Target | Basis |
|---|---|---|
| 7-day activation rate (completed first routed run) | 35 percent of installs | Judgment. The PRD's G3 sets 40 percent for the weaker "generate and start" definition; a completion-based definition is strictly harder, so 35 percent is the equivalent bar, not a reduction in ambition |
| Ignition (first session reaches a route) | 70 percent, median under 180 seconds | Judgment on the level, design budget on the time |
| Good Route Rate | 65 percent | Judgment |
| Week-4 retention of activated cohort | 30 percent | Judgment, set above the GD-1 paid-layer bar of roughly 20 percent so that the gate is cleared with margin rather than exactly |
| Install-level D30 (benchmark-comparable) | 8 to 12 percent | Sourced band, see the conflict note below |
| WRR rate (habitual share of the mature activated base) | 25 percent | Judgment |
| MAU (business reporting only) | On track for the PRD's G2 of 3,000 within 6 months of launch | Inherited from `prd.md` G2 [verified as the stated goal, target value is an assumption in that document] |

**Benchmark conflict, resolved explicitly** (the playbook requires both sides when sources disagree). Published 2026 compilations put Health and Fitness day-30 retention at roughly 3.5 to 4 percent of installs, with one AppsFlyer-derived figure as low as 2.78 percent [verified as reported] (Snoopr, Mobile App Retention Benchmarks 2026, https://www.snoopr.co/blog/mobile-app-retention-benchmarks-2026-what-good-looks-like-for-fitness-ecommerce-gaming-and-more, accessed 2026-08-06; vmobify, App Retention Benchmarks by Industry 2026, giving a directional band of 3 to 7 percent, https://vmobify.com/blog/app-retention-benchmarks, accessed 2026-08-06). A separate compilation reports subscription-model apps at roughly 14 percent day-30 against a 5.4 percent cross-category mean, and Health and Fitness subscription apps specifically at 12.1 percent [verified as reported] (Digital Applied, Mobile App Marketing Statistics 2026, https://www.digitalapplied.com/blog/mobile-app-marketing-statistics-2026-install-data, accessed 2026-08-06). All of these are secondary compilations of Adjust and AppsFlyer data rather than primary reports, and they define "active" differently, so they are neighborhoods rather than addresses.

We weight the subscription-app band, adjusted downward, and land on 8 to 12 percent. Reasoning: Waypoint launches free, so it does not get the paywall's self-selection benefit that drives the 12 to 14 percent figures, but it also does not carry the category's January-resolution install profile, since its audience is committed runners recruited on a specific job rather than a New Year intention [inferred].

**Two PRD targets need re-basing, and this is the recommendation to the founder.** `prd.md` G4 sets 25 percent day-30 retention, labeled there as an assumption pending Phase 6 benchmarks [verified as labeled]. Against every published Health and Fitness benchmark found, 25 percent at the install level would put Waypoint far outside the top decile of the entire category in its first month, which is not a plan. The recommendation is to redefine G4 as **25 percent day-30 retention of the activated cohort** (a bar this document considers reachable and sets at 30 percent for week 4) and to add **8 to 12 percent install-level D30** as the separate benchmark-comparable line. Similarly, G3's activation definition should move from "generate and start" to "complete", per Section 4.2. Both changes are Phase 6 gate items.

### 7.3 Stage 3: Android launch, month 10 to 12

Android's targets are mostly parity targets, because the product question was already answered on iOS and the new question is whether the cross-platform codebase delivers the same experience (DEC-010) [verified].

| Metric | Target | Basis |
|---|---|---|
| Android 7-day activation rate | Within 5 points of the iOS cohort at the equivalent cohort age | Judgment |
| Android Good Route Rate | Within 3 points of iOS | Judgment; the engine is shared, so a larger gap means a client or map-rendering defect, not a routing defect |
| Runs with a GPS gap over 60 seconds (Android) | Under 2 percent (GR10) | Judgment, and a launch blocker |
| Crash-free session rate, both platforms | 99.5 percent or above | Judgment, standard practice |
| iOS mature-cohort metrics | Unchanged by the Android launch | Method, not target: see below |

**The cohort-pollution rule.** Every aggregate rate metric will dip when Android launches, because a large new cohort enters at the top of its decay curve. That dip is an artifact. Three defences, all cheap: (1) every retention and activation number is reported by (platform, install week) cohort, never blended; (2) a "mature cohort" view restricted to users who installed 8 or more weeks ago is the default weekly read; (3) the WRR count is reported blended (it is a business number and the growth is real), while the WRR rate is reported per platform. Write these three rules into the weekly report template before Android ships, not after the first confusing week.

### 7.4 Stage 4: the paid-layer moment, month 10 to 12

Gate first, then targets. GD-1 says the paywall ships only once week-4 retention of route generators clears the healthy-cohort bar, directionally 20 percent or better [verified, `mvp-scope.md` GD-1 and assumption]. This document sharpens that bar into three conditions, all of which must hold for four consecutive weeks:

1. Week-4 retention of the activated cohort at 25 percent or above (iOS mature cohorts).
2. Good Route Rate at 65 percent or above, with no launch metro more than 15 points below the median.
3. Workout-route attach rate measurable at all, meaning the AC-1 seam exists and is being used, since it is the first paid feature and the H7 test.

Post-paywall targets, all benchmarked:

| Metric | Target | Basis |
|---|---|---|
| Download-to-paid conversion, 6 months after paywall | 3 percent or above | Sourced: above the 2.1 percent freemium median, below the 2.9 percent all-models Health and Fitness median [verified] (RevenueCat SOSA 2026, accessed 2026-08-06) |
| Trial start rate | 7 percent or above | Sourced: Health and Fitness median 7.2 percent [verified as reported] (The-Diff calculator presenting RevenueCat SOSA 2026, accessed 2026-08-06) |
| Trial-to-paid | 35 percent or above | Sourced: median 37.7 percent, same source |
| Annual first renewal | 36 percent or above | Sourced: category median, same source |
| Free-tier health after the paywall | WRR rate does not fall | Judgment, and the real risk: the paywall must not degrade the free wedge (`user-journeys.md` cross-journey principle 8) [verified] |

---

## 8. Instrumentation plan

### 8.1 Where things live

| Layer | What it computes or stores | Why there |
|---|---|---|
| **On device** | Every location-derived and health-derived quantity: route adherence, completion ratio, off-route share, far-from-home boolean, dark-hours bucket, metro label, readiness-modulation flags. Emits only scalars and enumerations | The privacy architecture requires it (C-1, C-5), and it is also cheaper than shipping traces |
| **Server (Waypoint orchestration API and Postgres)** | Generation requests already transit the server for GraphHopper, so generation, latency, degradation flags, and candidate counts are logged there, truncated with short TTL per the stack posture. First-party event table for cohort-critical events (activation, retention, route session outcomes) | Cohort analysis needs a stable pseudonymous identifier that stays inside our own trust boundary (Section 9, tension 3) |
| **Third-party analytics (TelemetryDeck)** | Coarse aggregate counters: onboarding funnel, permission grants, feature usage counts | Already the recommended vendor: privacy-first, German-hosted, no personal data, no consent banner, no ATT prompt [verified, `api-integration-map.md` 6.2] |
| **Crash and error (Sentry)** | Crash-free session rate, error volume, with IP collection disabled and coordinates scrubbed from breadcrumbs [verified, `api-integration-map.md` 6.1] | Stability guardrails |
| **Store consoles** | Installs, product page conversion, uninstalls (Play), ratings, subscription revenue | Only source for pre-install funnel data; no attribution SDK exists |
| **RevenueCat (v1.x only)** | Trial starts, conversions, renewals, churn | Already the approved subscription vendor [verified, `api-integration-map.md` 5.1] |

**Vendor flags.** Three vendors touch metrics: TelemetryDeck (analytics, MVP), Sentry (crashes, walking skeleton), RevenueCat (subscriptions, v1.x). All three are already chosen and costed in `api-integration-map.md` sections 6.1, 6.2, and 5.1, and none of them receives location or health data under this plan. No new vendor is proposed. If cohort funnel analysis outgrows the first-party table, the pre-approved upgrade path is PostHog EU (Frankfurt), which requires a DPA and a consent story that TelemetryDeck avoids [verified, `api-integration-map.md` 6.2].

**A budget constraint worth designing around.** TelemetryDeck's free tier is 50,000 signals per month for accounts created after 1 July 2026 [verified, `api-integration-map.md` 6.2]. At roughly 15 emitted events per active runner per week, 1,000 monthly active runners produce on the order of 60,000 signals per month, which exceeds the free tier. Two consequences: keep the shipped schema at roughly fifteen event types (below), and budget the paid tier from launch rather than discovering the cap mid-month. Cohort-critical events go to the first-party table anyway, which keeps the vendor volume down.

### 8.2 Event schema

Privacy classes follow `api-integration-map.md`: P0 (no personal data), P1 (pseudonymous or coarse), P2 (personal data), P3 (sensitive: precise location or health). **No event in this schema is P3.** That is a design rule, not a coincidence: anything P3 is reduced on device to a P1 scalar before emission.

| Event | Fires when | Properties | Computed | Stored | Class |
|---|---|---|---|---|---|
| `app_first_open` | First launch after install | platform, app_version, country, install_week | Device | TelemetryDeck | P1 |
| `onboarding_step` | Each onboarding stage completes or is skipped | step, outcome, elapsed_ms | Device | TelemetryDeck | P1 |
| `permission_result` | Any permission dialog resolves | type (location, health, notification), granted, ask_context | Device | TelemetryDeck | P1 |
| `route_generated` | Engine returns candidates | session_id, generation_index, distance_bucket, elevation_pref, safety_weight, novelty_on, latency_ms, candidate_count, degradation_flags, coverage_class, metro_label | Server plus device | First-party table | P1 |
| `route_regenerated` | User taps try another | session_id, generation_index, seconds_viewed | Device | First-party table | P1 |
| `route_session_abandoned` | 30 minutes after a reveal with no start | session_id, last_generation_index | Device | First-party table | P1 |
| `route_accepted` | User starts or saves the route | session_id, accepted_generation_index, action (start, save) | Device | First-party table | P1 |
| `run_started` | Run recording begins | run_id, source (generated, saved, freeform), nav_mode | Device | First-party table | P1 |
| `run_completed` | Run ends through the finish flow | run_id, distance_ratio_bucket, adherence_bucket, reroute_count, offroute_events, max_gps_gap_s, battery_pct_per_hour_bucket | Device | First-party table | P1 |
| `run_abandoned` | Run ends before the finish flow or under 25 percent of distance | run_id, fraction_bucket, offroute_before_abandon | Device | First-party table | P1 |
| `route_saved` / `route_repeated` | Save, or a saved route re-run | local_route_hash, days_since_generated | Device | First-party table | P1 |
| `honest_refusal_shown` | Engine declines to return a route (RG-F10) | reason, active_constraints, coverage_class, metro_label | Server | First-party table | P1 |
| `safety_flag_raised` | Pre-run, mid-run, or post-run flag | context, reason_chip, hour_bucket, metro_label | Device | First-party table | P2, privacy review required |
| `share_completed` | Strava or system share succeeds | target, zone_trimmed | Device | TelemetryDeck | P1 |
| `upsell_shown` / `paywall_view` / `trial_start` (v1.x) | Paid-layer surfaces | trigger_feature, action | Device | RevenueCat plus first-party | P2 |

Rules that keep this schema honest, enforced by GR5: no free-text properties, ever; no coordinates, ever; every numeric that could be identifying (distance, duration, battery) is emitted as a bucket rather than a value; `metro_label` is a coarse label from a fixed list of launch metros, resolved on device, and is suppressed as `unknown` when fewer than twenty users in that metro emitted the event that week.

### 8.3 Metric to event mapping

| Metric | Events required |
|---|---|
| WRR and WRR rate | `run_completed` with source in (generated, saved), joined to accounts |
| Activation, Ignition | `app_first_open`, `route_generated`, `run_completed` |
| Acceptance, regeneration, reveal abandon | `route_generated`, `route_regenerated`, `route_accepted`, `route_session_abandoned` |
| Completion, early abandon, off-route | `run_started`, `run_completed`, `run_abandoned` |
| Good Route Rate | The four above, joined by `session_id` |
| Retention | `run_completed` by account and cohort week |
| GR1 honest refusals | `honest_refusal_shown` against `route_generated` |
| GR2, GR3 safety | `route_generated` (safety_weight, hour bucket), `safety_flag_raised` |
| GR10 Android GPS | `run_completed.max_gps_gap_s` |

---

## 9. Privacy: what is cheap, what is in tension, and how each tension resolves

### 9.1 Cheap to collect privately

Counts of generations, regenerations, acceptances, refusals, completions, abandonments, latencies, degradation flags, permission outcomes, and crash rates are all scalars with no personal content. Adherence, completion ratio, and off-route share are derived from data the device already holds for navigation and are emitted as buckets. Cohort membership uses the account identifier Waypoint already holds for sync, with no advertising identifier, no cross-app identifier, and therefore no ATT prompt. All store-console metrics are aggregate by construction. This covers the North Star, the entire metric tree, activation, retention, and the whole of Section 5 except the geographic cut.

### 9.2 Genuine tensions, and the resolution for each

**Tension 1: route quality is only actionable when cut by geography, and geography is the sensitive part.** A portfolio Good Route Rate hides the metro where the product is broken, so the cut is not optional. Resolution: resolve a coarse `metro_label` on device from a fixed list of launch metros (cardinality in single digits at launch), never coordinates and never a cell fine enough to imply a neighborhood; suppress the label when fewer than twenty distinct users in that metro emitted the event in that week; and store metro labels as counters rather than as properties on a user timeline, because a per-user sequence of metro labels with timestamps is a travel diary regardless of how coarse each entry is. Routing requests themselves do need the true start point at the server to produce a route at all, but those requests are transient and logged truncated with a short TTL under the existing stack posture, and the analytics pipeline never reads them.

**Tension 2: the travel signal (Phase 3 signal 1) is inherently a statement that this person is away from home.** Resolution: compute `is_far_from_home` on device and emit only the boolean plus a coarse distance band, never both endpoints; and aggregate it per user per month into a single count ("3 travel generations this month") rather than emitting a timestamped event stream, so the analytics store never holds a trip itinerary. This makes the metric slightly less precise and completely defensible. If the founder later wants trip-level analysis, that requires a DPIA update, not a schema tweak.

**Tension 3, the sharpest: proper cohort retention needs a stable per-user identifier over time, and the recommended analytics vendor deliberately does not provide one.** TelemetryDeck's privacy model (hashed identifiers, differential privacy, no personal data) is exactly why it needs no consent banner, and it is also why it cannot answer "what share of the users who activated in week 12 were still running routes in week 16" [verified as the product's design, `api-integration-map.md` 6.2]. This is a real gap between the PRD's promise of privacy-preserving analytics and the metric plan the PRD's own goals require. Resolution: keep cohort retention in the first-party Postgres event table keyed to the account identifier Waypoint already holds for sync, inside the existing trust boundary and the existing DPA set, and use TelemetryDeck only for coarse counters. This adds no vendor, no SDK, and no new consent basis, at the cost of the founder building three or four SQL views by hand. The alternative (PostHog EU) adds a processor, a DPA, and pseudonymous event-level data leaving the boundary, and should be a deliberate v1.x decision rather than a default. **This needs a founder decision at the Phase 6 gate.**

**Tension 4: the temptation to mine GPS traces for segment-level route quality.** Learning which specific street segments runners avoid would make the engine much better, and it would also rebuild something with heatmap-shaped deanonymization risk, which C-2 forbids and which the Strava and NRK incidents make concrete [verified, `prd.md` C-2 and Section 7]. Resolution: defer segment-level aggregation entirely to v1.x behind a DPIA; at v1, learn preferences on device only (the concept's learning loop is described as on-device-first anyway) and accept that the aggregate scoring layer improves more slowly. If it ships later, the minimum design is: segments outside every user's privacy zones, a minimum count threshold per segment, no user association, and no export.

**Tension 5: paid-layer metrics that touch health data.** Readiness-modulated generation (AC-1) is the first paid feature, and its obvious metric is "acceptance rate of readiness-modulated routes versus workout-type-only routes". Health values may never leave the device [verified, `api-integration-map.md` 3.1]. Resolution: emit a boolean (`readiness_applied`) and nothing else; never a readiness score, never an input value, never a bucket of one. The comparison is still computable because the boolean plus the existing acceptance events are sufficient.

**One thing that is not a tension, and should be said plainly:** none of the metrics in this document require an advertising identifier, a device fingerprint, an attribution SDK, or any third-party SDK with location or health access. The plan is implementable inside the existing architecture without a single new data flow off the device beyond the counters described in Section 8.

---

## 10. Reporting cadence for one person

The test applied to every item below: if this number moved, would the founder do something different this week? If not, it does not appear on the daily or weekly list.

### Daily, 2 minutes, and only during beta and the two weeks after each launch

A single health check, glanced at with coffee, not a dashboard session.

- Crash-free session rate, both platforms (Sentry).
- Generation success rate and p95 latency (GR6).
- Honest-refusal spikes (GR1), which usually mean a data pipeline broke rather than that the world changed.
- New safety flags (GR3), read individually, always.

Plus, during the walking skeleton only: read ten generation sessions end to end per week, including the resulting trace. This is the highest-information activity in the entire plan at that stage, and no dashboard replaces it.

### Weekly, 30 minutes, Monday

One page, seven numbers, one decision.

1. WRR (count) and WRR rate (mature cohort, per platform).
2. Good Route Rate, with the worst metro named.
3. First-route acceptance rate and generations per accepted route.
4. Route completion rate.
5. Activation rate of the install cohort that matured last week, plus Ignition.
6. Guardrail exceptions: only the ones that breached, listed by name (GR1 to GR10).
7. One sentence: what changed, and what will be done about it.

The rule is one decision per week. A weekly review that produces a list of six things to look into is a review that produced nothing.

### Monthly, 60 to 90 minutes

- Cohort retention curves by install month and platform, including the flatness read.
- Week-4 and week-12 retention of the cohorts that matured this month.
- Route quality by metro, with the constraint-coverage story attached (which constraints were degraded, where).
- Novelty supply: share of users approaching street exhaustion within 5 km of home, which is a leading indicator of a specific, predictable churn cause.
- Segment mix (GR8), and MAU for the G2 business goal.
- Re-baseline check: are the judgment thresholds in Sections 5.5 and 7 still the right ones now that real distributions exist?

### Stage-gated, not scheduled

- Paid-layer readiness (Section 7.4), evaluated only when the three gate conditions are plausibly close.
- Unit economics inputs, handed to `unit-economics.md`.
- Benchmark refresh, annually or when a new State of Subscription Apps lands.

### Deliberately ignored until it matters

| Ignored | Until |
|---|---|
| MAU as a steering metric | The seed conversation or the G2 six-month checkpoint; it stays on the business page, off the product page |
| DAU, and DAU/MAU ratio | Never. It is the wrong shape for a product used 3 to 5 times per week; the weekly window is the natural one |
| All revenue metrics | The v1.x paywall ships |
| Watch versus phone split (signal 6) | The Watch app ships at launch plus 30 |
| Weather acceptance (signal 7) and plan-disruption behavior (signal 5) | Their features exist (v1.x and v2) |
| NPS and satisfaction surveys | After the retention curve flattens; before that they measure enthusiasm for a promise, not for a product |
| Channel and attribution analysis | There is paid acquisition to attribute, which is not v1 |
| Strava share rate | Monthly at most, and never as a target |

---

## 11. Metric summary card

The whole plan on one screen, for the weekly page.

| Layer | Metric | Type | Launch target |
|---|---|---|---|
| North Star | Weekly Routed Runners (2+ completed generated routes in 7 days) | Actionable | 25 percent of the mature activated base |
| Input I1 | Activated base | Actionable | Growing |
| Input I2 | Generations per activated runner per week | Actionable | 2.5 or above (judgment) |
| Input I3 | First-route acceptance rate | Actionable | 70 percent |
| Input I4 | Route completion rate | Actionable | 85 percent |
| Input I5 | Week-4 retention of activated cohort | Actionable | 30 percent |
| Activation | Completed first routed run within 7 days of install | Actionable | 35 percent |
| Activation leading | Ignition (first session reaches a route, median under 180 s) | Diagnostic | 70 percent |
| Route quality | Good Route Rate | Actionable | 65 percent |
| Route quality | Generations per accepted route | Actionable | Below 1.4 |
| Route quality | Repeat rate within 30 days | Actionable | No target at launch, baseline first |
| Guardrail | GR1 honest-refusal stability | Binary | Stable |
| Guardrail | GR4 location and health egress | Binary | Zero |
| Business | MAU, install-level D30 | Diagnostic | 3,000 in 6 months; 8 to 12 percent |

---

## 12. Assumptions register

- **A1.** The two-runs-per-week habit threshold in the North Star matches the target segment's real cadence. It is derived from the segment definition of 3 to 5 runs per week, not from observed Waypoint behavior. If beta shows committed amateurs generating routes for only some of their runs (using known loops for the rest), the threshold may need to fall to one per week, which would change what WRR means. [assumption]
- **A2.** The 80 percent completion floor is the right cut between "ran the route" and "abandoned it". Runners legitimately cut runs short for reasons unrelated to route quality. [assumption]
- **A3.** Every route-quality threshold in Section 5.5 is judgment, because no competitor ships constraint-based generation and therefore no external benchmark exists. All of them should be re-baselined after twelve weeks of launch data. [assumption]
- **A4.** Activation at seven days is the right window, and completion is the right step. Section 4.2 specifies the beta-cohort test that would confirm or replace it. [assumption]
- **A5.** External retention benchmarks used in Section 7.2 are secondary compilations of Adjust and AppsFlyer data with inconsistent definitions of "active"; the 8 to 12 percent install-level D30 target is an inference over conflicting bands, not a sourced number. [assumption]
- **A6.** Subscription benchmarks (conversion, trial, renewal) come from RevenueCat's 2026 dataset and its derived calculator, and describe apps that were paid from launch. Waypoint's first paying cohort will have used a free product for months, which plausibly raises trial-to-paid and lowers trial start rate relative to the medians. [assumption]
- **A7.** Twenty distinct users per metro per week is a sufficient k-anonymity threshold for the `metro_label` suppression rule. A privacy review should confirm or raise it. [assumption]
- **A8.** The event volume estimate of roughly 15 signals per active runner per week (Section 8.1) is a planning figure; the real number will be known from the first beta week and determines the TelemetryDeck tier. [assumption]
- **A9.** GR8's 40 percent segment-mix floor and GR2's 10-point safety-share tolerance are set by judgment with no external anchor. [assumption]
- **A10.** Cohort retention in a first-party Postgres table is operationally sustainable for a solo founder (three or four SQL views, refreshed weekly). If it is not, the PostHog EU decision arrives sooner than v1.x. [assumption]

---

## 13. Open questions for the founder

1. **Approve or reject the North Star as defined**, including the two-runs-per-week threshold and the inclusion of saved-route re-runs. This is the single choice that shapes every other number here.
2. **Ratify the activation definition** (completed first routed run within seven days), and accept the corresponding re-basing of PRD goals G3 and G4 (Section 7.2). Both changes deserve a decision record.
3. **Decide the cohort-retention data path now** (Section 9, tension 3): first-party Postgres event table, or PostHog EU with its DPA and consent implications. Deciding this at the Phase 6 gate is much cheaper than discovering it during the first retention read.
4. **Confirm the k-anonymity threshold and the metro-label design** with the compliance checklist review, since the geographic cut of route quality is the one metric family that genuinely touches the privacy architecture.
5. **Accept the walking-skeleton practice of hand-reading ten sessions per week.** It is the only route-quality instrument that works at n=40, and it costs real founder hours.
6. **Are the launch metros decided?** Route quality cannot be segmented before the metro list exists, and the list is already an open question in `mvp-scope.md` (open question 3).
7. **Does the paid-layer gate (Section 7.4, three conditions for four consecutive weeks) match the founder's risk appetite**, or is a two-week read acceptable given the competitive window?

---

## 14. Sources

External, all accessed 2026-08-06:

- RevenueCat, State of Subscription Apps 2026, https://www.revenuecat.com/state-of-subscription-apps and the Health and Fitness cut, https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/ (Health and Fitness download-to-paid median 2.9 percent and top quartile above 6.2 percent; hard paywall 10.7 percent versus freemium 2.1 percent day-35 download-to-paid; year-one subscriber retention 27 percent hard paywall versus 28 percent freemium; Health and Fitness day-14 revenue per install $0.48 median).
- The-Diff subscription benchmark calculator, presenting RevenueCat State of Subscription Apps 2026 data, https://tools.the-diff.com/health/ (Health and Fitness trial start rate 7.2 percent, trial-to-paid 37.7 percent, monthly first renewal 57.0 percent, annual first renewal 36.0 percent, 12-month retention 34.2 percent). Secondary presentation of the RevenueCat dataset.
- Snoopr, Mobile App Retention Benchmarks 2026, https://www.snoopr.co/blog/mobile-app-retention-benchmarks-2026-what-good-looks-like-for-fitness-ecommerce-gaming-and-more (Health and Fitness day-1 20 percent, day-7 7 to 8.5 percent, day-30 3.5 to 4 percent; an AppsFlyer-derived day-30 figure of 2.78 percent). Secondary compilation of Adjust, AppsFlyer, and Statista data.
- vmobify, App Retention Benchmarks by Industry 2026, https://vmobify.com/blog/app-retention-benchmarks (Health and Fitness directional day-30 band of 3 to 7 percent, with an explicit caution to treat published bands as neighborhoods). Secondary compilation.
- Digital Applied, Mobile App Marketing Statistics 2026, https://www.digitalapplied.com/blog/mobile-app-marketing-statistics-2026-install-data (cross-category day-30 5.4 percent; subscription apps near 14 percent; Health and Fitness subscription cohort 12.1 percent). Secondary compilation.
- Amplitude, Every Product Needs a North Star Metric, https://amplitude.com/blog/product-north-star-metric, and What Makes a Good vs Bad North Star Metric, https://amplitude.com/blog/good-bad-north-star-metric (North Star Framework: 3 to 5 inputs, the breadth, depth, frequency, efficiency heuristic, and the test that a North Star starts at the customer value moment and leads rather than lags).

Internal (all read 2026-08-06): `research/00-RESEARCH-PLAYBOOK.md`, `research/04-synthesis/concept.md`, `research/04-synthesis/hypotheses-review.md`, `research/05-product/mvp-scope.md`, `research/05-product/prd.md`, `research/05-product/user-journeys.md`, `research/05-product/api-integration-map.md`, `research/03-users/personas.md`, `research/03-users/jobs-to-be-done.md`, `research/03-users/unmet-needs.md`, `vault/02-Decisions/DEC-008 Phase 5 gate MVP approved stack in validation.md`, `vault/02-Decisions/DEC-010 Staged cross-platform MVP on React Native.md`.

## Related

- `research/06-business-model/revenue-model.md` (pricing; consumes the conversion benchmarks above)
- `research/06-business-model/unit-economics.md` (consumes activation, retention, and conversion targets)
- `research/06-business-model/gtm-plan.md` (consumes acquisition metrics and the segment-mix guardrail)
- `research/05-product/prd.md` Section 6 (the analytics section this document extends and, in two places, re-bases)
- `research/03-users/unmet-needs.md` Section d (the eight telemetry signals mapped in Section 1.2)
