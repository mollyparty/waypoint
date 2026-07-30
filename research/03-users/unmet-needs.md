# Unmet Needs: Phase 3 Capstone Ranking and Validation Plan

Version-Timestamp: 2026-07-30 15:45:00 UTC-4

**Executive summary.** This capstone merges the six community-mined pain themes (`pain-points.md`) with the eight competitor-visible unmet needs (`gap-analysis.md`) into eleven consolidated needs, ranked by evidence strength. The top three by evidence are safety-aware routing (quantified surveys, a peer-reviewed study, and a verified competitor failure producing dangerous routes), route novelty and personalization at home (organic emotional testimony plus a 90,000-user paying movement), and the training-state-to-route connection (a total, verified absence across fifteen-plus products, though demand for it is inferred rather than expressed). Travel route friction, the founder's original H1 framing, ranks fourth: frequency is overwhelming but workarounds mostly succeed, so it is repositioned as the activation moment and demo story while safety plus home novelty carry daily retention. H7 (personalized routine building as a retention deepener) is directionally supported through the plan-disruption and calibration evidence, with the honest caveat that the community expresses plan pain as guilt and schedule, not as routes. The document closes with the consolidated interview backlog (five prioritized studies, roughly 20 to 30 conversations total) and the list of uncertainty areas the MVP can resolve with telemetry instead of interviews.

**Desk research disclaimer.** This synthesis rests entirely on desk research: community mining, published surveys, competitor profiles, and platform data, all accessed 2026-07-30 and documented in `pain-points.md`, `segmentation.md`, `personas.md`, and `research/02-competitors/gap-analysis.md`. No Waypoint user interviews have been conducted. Evidence-strength ratings grade the quality of desk evidence, not validated market truth; a "strong" rating here still requires interview confirmation before it drives irreversible product decisions. [verified] marks claims traced to sourced evidence in the source documents; [inferred] marks reasoned conclusions; [assumption] marks unsupported working belief.

## (a) Ranked unmet needs

Rating rubric [inferred, judgment layer]: **strong** requires at least two independent evidence classes (for example quantified survey plus community testimony plus competitor failure); **moderate** requires verified evidence in one class with corroboration gaps; **weak** means the need is inferred from expert advice, product logic, or thin community signal.

| # | Need | Evidence strength (why) | Personas feeling it | Competitors failing at it | Wedge-native? |
|---|---|---|---|---|---|
| 1 | Safety-aware routing (lighting, population, time of day as first-class constraints) | **Strong.** Quantified surveys (54 percent of women changed routes; 42 percent routine dictated by safety; 82 to 92 percent hold safety concerns), a peer-reviewed British Journal of Criminology study, raw community testimony, and a verified competitor failure (Strava routes on interstates and unsafe roads, no flagging mechanism) (`pain-points.md` Section 3; `gap-analysis.md` need 2; `personas.md` Elena) | Elena primarily; Priya at 6 a.m. in unfamiliar cities; cross-cutting for women within every persona | All fifteen-plus products examined: zero accept safety, lighting, or traffic as routing input; Strava Night Heatmap is display only | Yes, hero constraint |
| 2 | Route novelty and personalization at home ("roads not yet run") | **Strong.** Organic emotional testimony ("reduced me to tears", "dreading"), a 90,000-user paying movement (CityStrides) built on exactly this desire, and a verified incumbent mismatch (Strava ranks by popularity, steering everyone onto the most-run streets) (`pain-points.md` Section 2; `gap-analysis.md` need 6) | Marcus centrally; Jake (exploration, not laps); Elena (widen her world safely) | Strava (popularity ranking is the opposite), all hobby generators (impersonal), CityStrides (adjacent but no generation, no training context) | Yes |
| 3 | Training-state-to-route connection (the day's workout shapes the route) | **Strong on the gap, inferred on demand.** Verified total absence: every coaching product has zero route capability, every route product has zero training context, "two different runners at the same corner get the same routes" (`gap-analysis.md` need 1). But no community post asks for it in these words; demand is product logic [inferred] | Marcus (tempo needs flat and uninterrupted); Priya (workout sized to the trip) | All ten profiled products plus the hobby long tail; the empty top-right quadrant of the Phase 2 positioning map | The seam: wedge provides the surface, coaching layer provides the intelligence |
| 4 | Travel "where should I run, right now, from here" | **Moderate to strong.** Overwhelming frequency evidence (decades of LetsRun threads, r/running FAQ infrastructure, Great Runs existing solely for this); intensity capped because the heatmap-plus-hotel-desk workaround usually succeeds in 15 to 20 minutes and the treadmill is an accepted fallback (`pain-points.md` Sections 1 and 9) | Priya acutely and frequently; Marcus episodically (race trips, work travel) | Nothing purpose-built: Strava heatmap approximates, Great Runs covers major cities only, community answers take days | Yes, sharpest demo |
| 5 | Injury-calibrated coaching that runners trust | **Moderate.** Verified sentiment at both market ends: Runna injury discourse (stress fractures, "even a easy day was a grind") versus TrainAsONE over-conservatism capping ambition; the calibrated middle is unclaimed (`gap-analysis.md` need 4; `personas.md` Jake) | Jake most acutely; Marcus (protect the build); returners by temperament | Runna (too aggressive), TrainAsONE (too conservative), Coopah (warm but rigid) | No, coaching layer |
| 6 | Mid-run navigation execution (hands-free, non-infuriating guidance) | **Moderate.** Multi-year, multi-device verified complaints with emotional language on Garmin forums, plus a willingness-to-pay signal (RunGo at $59.99 per year); affected population narrower (course-followers) (`pain-points.md` Section 6; `gap-analysis.md` need 8) | Priya (never stop to check a phone in a strange city); Marcus on new routes | Garmin (prompts cannot be silenced sanely), web generators (no mobile execution), RunGo and Footpath (execute but do not generate) | Execution layer, wedge-adjacent and mandatory |
| 7 | Plan flexibility when life disrupts training (without guilt) | **Moderate.** One strong statistic (over 50 percent of marathoners miss 7+ consecutive days) and a large coaching-content genre built on the guilt spiral; but the community frames it as schedule and emotion, not routes; the route connection is Waypoint's inference (`pain-points.md` Section 4) | Marcus (family, work); Priya (travel chaos); Jake (life happens) | Runna (adapts poorly per complaint record), all static plans; nobody adapts the where | Coaching layer, with wedge assist (FJ9 time-boxing) |
| 8 | Urban doorstep running as a design center | **Moderate.** Verified structural absence: Komoot is cyclist-first, AllTrails is trail-locked, RunGo's library is race courses and city tours; the runner starting at a front door, hotel, or office is nobody's design center (`gap-analysis.md` need 5) | All four personas; this is where the target segment actually runs | Komoot, AllTrails, RunGo, Footpath | Yes, by definition of the wedge |
| 9 | Weather and heat adaptation applied to the route | **Weak to moderate.** Consistent expert advice (shade, water, cut-short loops) and a shipping pace-side analog (Runna Adapt for Heat) validate the lever, but organic first-person demand for route-level tooling was not found (`pain-points.md` Section 5; `gap-analysis.md` need 3) | Marcus (summer long runs); Priya (climate whiplash between cities) | Runna and TrainAsONE (pace only), Komoot and AllTrails (display weather, do not route by it) | Yes, differentiating constraint |
| 10 | Trustworthy subscription mechanics | **Moderate as pattern, weak as need.** Verified complaint records (Joggo renewal traps, Runna double-charging and support silence, Komoot paywall exits); this is category hygiene rather than a job runners hire for (`gap-analysis.md` need 7) | All paying personas, Marcus most (category-burned) | Joggo, Runna, Komoot | No, table stakes conduct |
| 11 | Quiet routes for self-conscious beginners | **Weak.** Verified testimony exists (C25K forums: running at dark hours to avoid being seen) but the pre-committed beginner sits below the target segment; parked for a future persona (`pain-points.md` Section 7) | Jake-adjacent (below Jake's commitment level) | Nobody; unserved and unclaimed | Technically yes; deliberately deferred |

Reading note: needs 1 through 4 are the wedge's load-bearing wall. Needs 5 and 7 carry the coaching layer and H7. Need 6 is the bridge between generation and reality. Needs 9 to 11 are differentiators or deferrals, not foundations [inferred].

**Merge trace.** How the six pain themes (`pain-points.md`) and eight competitor gaps (`gap-analysis.md`) collapse into the eleven needs above:

- Need 1 = pain theme 3 (women's safety route constraints) + gap need 2 (safety-aware routing).
- Need 2 = pain theme 2 (route boredom at home) + gap need 6 (personalization beyond popularity).
- Need 3 = gap need 1 (training state to route choice); no matching community-expressed pain theme exists, which is why demand is tagged inferred.
- Need 4 = pain theme 1 (travel "where should I run").
- Need 5 = gap need 4 (injury-calibrated adaptive coaching).
- Need 6 = pain theme 6 (mid-run navigation friction) + gap need 8 (generation plus navigation in one product).
- Need 7 = pain theme 4 (plan disruption and guilt) + the adaptation half of gap need 4.
- Need 8 = gap need 5 (urban doorstep running); corroborated indirectly by the doorstep framing throughout pain theme 1.
- Need 9 = pain theme 5 (heat-driven route adjustment) + gap need 3 (weather adaptation on the route side).
- Need 10 = gap need 7 (trustworthy subscription mechanics); no pain-theme counterpart, it surfaced from competitor complaint records.
- Need 11 = pain theme 7 (the beginner self-consciousness bonus theme); no gap counterpart, nobody serves or claims it.

## (b) Hypothesis verdicts and implications for Phase 4

**H1 ("where do I run" friction, especially when traveling, drives adoption): PARTIALLY SUPPORTED, reframed.** Full reasoning in `pain-points.md`, Section 9; the nuance matters enough to restate plainly here.

- What holds: the travel question is asked constantly across decades of forum threads, is monetized by a cottage industry (Great Runs, running tours, hotel route maps), and is painful enough to change hotel-booking behavior [verified].
- What does not hold: the workaround stack (heatmap, Street View, hotel desk) usually succeeds in 15 to 20 minutes, the treadmill is an accepted fallback, travel is episodic for the core committed amateur, and nobody in the mined threads expressed willingness to pay for generated routes [verified as absence].
- The honest formulation: travel friction is a strong **activation moment and demo story** (the 30-second hotel-lobby route is the most vivid possible demonstration of the engine), while **safety-aware routing plus home novelty are the daily retention wedge**, because they recur 3 to 5 times per week for the exact target segment and are the two strongest-evidenced needs in the table above [inferred].
- Net: H1 as literally framed is UNCERTAIN. H1 reframed as "the where-should-I-run question, of which travel is the sharpest episode, is frequent and underserved" is SUPPORTED by desk evidence and awaits interview arbitration [inferred].

**H7 (personalized routine building deepens retention after the wedge acquires): DIRECTIONALLY SUPPORTED, unproven on the connection.**

- The supporting chain: plan disruption is near-universal among plan followers (over 50 percent of marathoners miss 7+ consecutive days in a build) [verified]; adaptation quality, not plan quality, is where trust breaks in the incumbent (Runna's complaint record) [verified]; and the calibration middle ground between aggressive and conservative is unclaimed [verified] (`pain-points.md` Section 4; `gap-analysis.md` need 4).
- The caveat that keeps this from full support: the community experiences plan pain as guilt and schedule, and the leap from "my plan broke" to "give me a personalized routine with routes" is Waypoint's inference, not the users' words [inferred].
- H7's retention mechanics (does routine depth actually reduce churn) are unmeasurable until a product exists; signals 4 and 5 in Section d are the designated instruments.

**Implications for the Phase 4 concept definition** [inferred throughout]:

1. The concept leads with the umbrella job from `jobs-to-be-done.md` Section a: the right route, right now, from here, for me. Travel is the marketing hero; safety and novelty are the product's daily muscles.
2. Safety-aware routing should be scoped as a launch capability, not a later mode: it is the strongest-evidenced need, the loudest verified competitor failure, and Elena's existential requirement. It also carries the highest liability and trust burden, so the Phase 4 concept must include the honest-degradation behavior ("no good route meets your constraints right now") and the free-tier ethics decision flagged in `personas.md` (Elena, willingness-to-pay note).
3. The training-state-to-route connection (need 3) is the defensible seam: it is what neither a route app nor a coaching app can copy without becoming the other, and it is the single most important gap per `gap-analysis.md`. The concept should treat it as the paid-tier centerpiece, consistent with the H3 monetization caveat (wedge acquires, coaching layer monetizes).
4. Phase 4 should carry forward the 12 to 18 month Strava window (`gap-analysis.md`, Section c) as the pacing constraint: the concept must be shippable as a focused wedge inside that window, not a five-constraint cathedral.

## (c) Interview backlog: the validation plan

Consolidated from the interview-needed flags across `pain-points.md` (Section 10), `segmentation.md` (open questions), and `personas.md` (open questions). Priority order reflects decision risk: what could kill or redirect the concept if the desk evidence is wrong. Total: roughly 20 to 30 conversations plus one survey.

**Priority 1: Committed amateurs, the H1 base rate and bundling test.** 8 to 12 interviews. Profile: 3 to 5 runs per week, 2 to 4 races per year, self-coached, mix of genders, at least 4 who travel monthly (this doubles as the Priya sample; `personas.md` open question 1). Must answer:

- Does Marcus feel route boredom and route friction as pain or as mild inconvenience? (The H1 base rate for the core segment.)
- Do the six pain themes register as one problem or unrelated annoyances? (The bundling assumption under the main job statement in `jobs-to-be-done.md`.)
- Willingness to switch and pay against the free heatmap workflow, with price anchors from the Phase 2 pricing matrix.
- Actual route-selection habits, and where exactly in the tool chain (heatmap plus watch plus maps) frustration peaks.
- Does workout-route matching (need 3) resonate as felt need once demonstrated, or only as a neat feature?

This study arbitrates H1 and the umbrella job framing; it gates the Phase 4 concept more than any other single input.

**Priority 2: Women runners, the safety trust test.** 4 to 6 interviews across urban densities; consider a specialist moderator given the topic's sensitivity (`personas.md` open question 3). Must answer:

- Would a safety-conscious runner trust an algorithmically generated route at all?
- What evidence (lighting data, population signals, community validation, explanation of why the route was chosen) earns that trust?
- Which digital safety tools does she actually use and trust today?
- How can safety claims be communicated without fear-based framing or implied guarantees?

A wrong answer here is a product-killing liability (`pain-points.md`, Section 10), which is why this ranks above the travel study despite the wedge's travel framing.

**Priority 3: Frequent-traveler runners, the Priya deep dive.** 3 to 5 interviews. Profile: 20+ travel nights per year, mid training plan. Overlap with Priority 1 travelers is acceptable and efficient. Must answer:

- The actual night-before research ritual, minute by minute, and where it breaks.
- How often the workaround fails, and whether a failed run on a trip actually matters to her.
- What she would pay to delete the ritual (`personas.md` open question 2).
- Watch versus phone execution behavior on the road, including offline needs.

**Priority 4: Ambitious beginners, the secondary-segment test.** 3 to 5 interviews. Profile: under 2 years running, race-committed, run-club member, Gen Z weighted. Informs the free tier and the Jake onboarding, not the core wedge. Must answer:

- Coaching or community first? Identity and belonging may outrank training quality (`personas.md` open question 4).
- Free-tier feature ranking: what earns the install before the race commitment justifies paying.
- Injury and calibration history with current apps (the Runna-aggressive versus TrainAsONE-conservative middle).
- Post-race churn intent: does the subscription survive the goal race?

**Priority 5: Returners, exploratory.** 2 to 3 interviews. Profile: previously committed, lapsed 6+ months, restarting. Lowest priority because the segment is deferred, but cheap to bolt onto recruitment screening. Must answer: prevalence signals, restart triggers, and app re-adoption behavior (`segmentation.md` open question 3).

**Parallel survey, not interviews: wearable and phone split.** A short screener survey (n of 100+ target-segment runners) for the Apple Watch versus Garmin versus phone-only split that gates H6 integration scope (`personas.md` open question 6; `pain-points.md` Section 10). Interview samples are too small to size this reliably [inferred].

## (d) Signals to instrument in the MVP

These uncertainty areas can be resolved with product telemetry once an MVP exists, and should not consume interview budget beyond directional checks. All instrumentation must respect the privacy stakes of location data (route privacy is a Phase 1 compliance headline; Elena's trust depends on it) [verified for the stakes] (`personas.md`, Elena).

1. **Travel frequency and the activation thesis.** Share of route generations starting far from the user's home area, per user per month. Resolves the missing cross-tabulation of running frequency with travel frequency (`segmentation.md` open question 2) with real behavior instead of recall.
2. **Novelty demand versus loop loyalty.** Repeat-route rate versus new-route requests per user; uptake of any "surprise me" or unrun-streets option. Separates the explorer segment from same-loop loyalists (`pain-points.md` Section 2 counter-evidence) and tests whether novelty retains (Section b, implication 1).
3. **Safety constraint usage.** Share of generations with safety or time-of-day constraints active, by local hour (dawn, day, dusk, dark). Measures whether safety routing is a daily driver or an occasional mode; interpret with care and never expose or retain more location detail than needed [inferred; privacy review required before shipping this metric].
4. **Workout-route attach rate.** Share of generated routes linked to a planned workout, and completion rate of those runs versus unlinked runs. This is the H7 seam metric: it tests whether the training-state-to-route connection (need 3) is felt value or product-logic fantasy.
5. **Plan-flexibility behavior.** After a missed run, do users reschedule within the app, generate a shorter time-boxed route, or go silent? Measures whether plan disruption connects to route intelligence in behavior, resolving the inference flagged in Section b (H7 caveat).
6. **Execution and form factor.** Watch versus phone execution split, audio-prompt settings chosen, mid-run route-deviation and completion rates. Resolves the navigation-behavior question (`pain-points.md` Section 10) and hardens H6 scope.
7. **Weather-adaptation acceptance.** When a weather-adjusted route is offered, acceptance rate versus override. Tests whether need 9 is felt value once surfaced, which desk evidence could not establish.
8. **Willingness to pay, revealed.** Paywall encounter-to-conversion by triggering feature (which constraint or coaching feature the user hit the paywall on). Replaces the unmeasurable desk question "would they pay" (`pain-points.md` Section 10) with revealed preference; RevenueCat-style cohort benchmarks frame the targets (`segmentation.md` Section 4).

**What telemetry cannot resolve (interviews stay mandatory):** trust formation for safety claims (a user who never installs because she distrusts the claim never appears in telemetry); pre-adoption workaround behavior and switching triggers; price framing before launch; returner restart triggers; and everything gating concept decisions that must be made before an MVP exists, which is precisely the Priority 1 and 2 interview material [inferred].

## Assumptions

- [assumption] The evidence-strength rubric (two independent evidence classes for "strong") is a reasonable proxy for real-world need intensity; no quantitative weighting was applied and a different analyst could rank needs 3 and 4 in the opposite order.
- [assumption] Merging pain themes and competitor gaps into single needs assumes community-expressed pain and competitor-visible absence describe the same underlying need; where they diverge (need 3: total gap, no expressed demand) the divergence is flagged but the merged framing may still overstate coherence.
- [assumption] Interview counts (8 to 12, 4 to 6, 3 to 5) follow qualitative-research convention for saturation within a segment, not a power calculation; they are inherited from the flags in `personas.md` and `pain-points.md`.
- [assumption] The reframed H1 (travel as activation, safety plus novelty as retention) is a synthesis judgment consistent with all desk evidence but validated by none of it directly; interviews and MVP telemetry (Section d, signals 1 to 3) are the arbiters.
- [assumption] Telemetry signals assume users grant location and health permissions at rates typical for running apps; a consent-rate collapse would gut the instrumentation plan.
- [assumption] No competitor shipped relevant features between the source documents' access date and this synthesis (same day, 2026-07-30).

## Open questions

1. Does the interview program confirm the reframed H1, or does travel friction turn out to be either stronger (travelers desperate, workarounds failing more than forums admit) or weaker (nobody switches apps for an episodic problem) than the desk read?
2. Where is the ethical and commercial line on safety routing: free tier as the defensible default (per `personas.md`, Elena), and what does legal review say about liability framing for any safety-adjacent claim?
3. Can the Priority 1 and Priority 2 studies run in parallel within the Strava window's planning clock (12 to 18 months, `gap-analysis.md` Section c), and who moderates the safety study?
4. If interviews kill the bundling assumption (runners see six unrelated annoyances), does Waypoint narrow to the single strongest need (safety routing) or hold the umbrella and let the product teach the frame?
5. What monetizable share of the committed amateur segment do needs 1 to 3 cover together, and does that share clear the H4 freemium bar tested in Phase 6?
6. Which telemetry signals need to be designed into the MVP architecture from day one (privacy-preserving location aggregation especially) rather than bolted on after launch?

## Sources

- Internal (all accessed 2026-07-30): `research/03-users/pain-points.md`, `research/03-users/segmentation.md`, `research/03-users/personas.md`, `research/03-users/jobs-to-be-done.md`, `research/02-competitors/gap-analysis.md`, `vault/01-Project/Founder-Brief.md`.
- All external evidence is cited in the source documents above; no new external claims are introduced in this synthesis.
