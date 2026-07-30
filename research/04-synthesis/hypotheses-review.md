# Hypotheses Review: Verdicts on the Founder Brief (H1 to H7)

Version-Timestamp: 2026-07-30 16:10:00 UTC-4

**Executive summary.** This document delivers the Phase 4 verdict on each of the seven testable hypotheses in `vault/01-Project/Founder-Brief.md`, using only the completed Phase 1 to 3 desk research. Headline: the competitive hypotheses hold up best (H2 SUPPORTED cleanly, H3 SUPPORTED with a monetization caveat), the founder's original demand framing needed surgery (H1 PARTIALLY SUPPORTED: travel is the activation moment, not the daily wedge; safety plus home novelty carry retention), and the two money questions remain honestly open (H4 PARTIALLY SUPPORTED on category-level evidence only, H5 UNCERTAIN pending an expansion story). H6 (iOS first) is SUPPORTED by the data-access landscape and device evidence. H7 (routines deepen retention) is PARTIALLY SUPPORTED: every link in its chain except the last is verified, and the last link (retention causation) cannot be proven without a product. No hypothesis is REFUTED. Every verdict below rests on desk research alone; the interview backlog in `research/03-users/unmet-needs.md` Section c is the designated arbiter for H1, H4, and H7 before irreversible product decisions.

## Verdict summary

| ID | Hypothesis (short form) | Verdict | Primary evidence source |
|---|---|---|---|
| H1 | Travel "where do I run" friction drives adoption | PARTIALLY SUPPORTED (reframed) | `research/03-users/unmet-needs.md` Section b |
| H2 | No incumbent solves constraint-based route generation | SUPPORTED | `research/02-competitors/gap-analysis.md` Section b |
| H3 | Route wedge beats another plan product | SUPPORTED (monetization caveat) | `research/02-competitors/gap-analysis.md` Section b |
| H4 | Committed amateurs pay freemium for adaptive routes plus coaching | PARTIALLY SUPPORTED | `research/01-market/market-sizing.md` Sections 3 and 5 |
| H5 | Addressable market is venture-scale | UNCERTAIN | `research/01-market/market-sizing.md` Section 6 |
| H6 | Mobile-first iOS with wearables is the right v1 form factor | SUPPORTED (Phase 5 confirms scope) | `research/02-competitors/gap-analysis.md` Section c; `research/03-users/segmentation.md` Section 4 |
| H7 | Personalized routines deepen retention after the route wedge | PARTIALLY SUPPORTED | `research/03-users/unmet-needs.md` Section b |

Reading rules: claims are tagged [verified] (traced to sourced evidence in the cited document), [inferred] (reasoned from verified inputs), or [assumption] (working belief). All evidence is desk research accessed 2026-07-30; none of it is validated by Waypoint user interviews [verified, per the desk research disclaimers in `research/03-users/unmet-needs.md` and `research/03-users/segmentation.md`].

## H1: Travel route friction drives adoption

**Hypothesis as stated.** "Where do I run" friction is frequent and painful enough for committed amateurs (especially when traveling) to drive app adoption (`vault/01-Project/Founder-Brief.md`, testable hypotheses table).

**Verdict: PARTIALLY SUPPORTED, and reframed.**

**Evidence summary.**

- For: the travel question is asked constantly across decades of forum threads, sustains a workaround cottage industry (Great Runs, Reddit FAQ infrastructure, hotel-desk rituals), and is painful enough to change hotel-booking behavior [verified] (`research/03-users/unmet-needs.md`, Section b, H1 verdict).
- For, on breadth: location is the top factor in race choice, and 83 percent of business travelers consider workout access when booking a hotel [verified] (`research/03-users/segmentation.md`, Section 5).
- Against the literal framing: the workaround stack (heatmap, Street View, hotel desk) usually succeeds in 15 to 20 minutes, the treadmill is an accepted fallback, and travel is episodic for the core segment [verified] (`research/03-users/unmet-needs.md`, Section b).
- Against, on payment: no mined community thread expressed willingness to pay for generated routes [verified as absence] (`research/03-users/unmet-needs.md`, Section b).
- The reframe Phase 3 lands on: travel is the activation moment and sharpest demo; the daily retention wedge is safety-aware routing plus home route novelty, which recur 3 to 5 times per week for the target segment and are the two strongest-evidenced needs in the ranked table [inferred] (`research/03-users/unmet-needs.md`, Section a, needs 1, 2, and 4; `research/03-users/_index.md`, headline findings).

**What would change the verdict.**

- The Priority 1 (committed amateurs, 8 to 12 interviews) and Priority 3 (frequent travelers, 3 to 5 interviews) studies in the interview backlog (`research/03-users/unmet-needs.md`, Section c).
- If travelers report the workaround failing more often than forums admit, H1 strengthens toward SUPPORTED as originally framed; if nobody switches apps for an episodic problem, it weakens toward REFUTED for travel specifically.
- MVP telemetry signal 1 (share of route generations far from home) settles the base rate with behavior instead of recall (`research/03-users/unmet-needs.md`, Section d).

**Consequence for the concept.** Keep travel as the marketing hero and onboarding demo; build safety and novelty as the product's daily muscles; do not size the business on travel frequency [inferred] (`research/03-users/unmet-needs.md`, Section b, implication 1).

## H2: No incumbent solves constraint-based adaptive route generation

**Hypothesis as stated.** No incumbent adequately solves constraint-based adaptive route generation (distance, elevation, weather, crossings, safety, surface) (`vault/01-Project/Founder-Brief.md`).

**Verdict: SUPPORTED.**

**Evidence summary.**

- Across fifteen-plus products profiled in Phase 2, zero accept weather, street crossings, or safety as routing constraints, and zero connect route capability to training state [verified] (`research/02-competitors/gap-analysis.md`, Section b, H2; `research/02-competitors/_index.md`, headline findings).
- The strongest incumbent, Strava Suggested Routes, offers preset distances, a flat or hilly preference, and a surface filter ranked by popularity, with documented dangerous outputs (interstates, shoulder-less roads) and no flagging mechanism [verified] (`research/02-competitors/gap-analysis.md`, Sections a.2 and b).
- AllTrails Peak's AI accepts only four relative adjustments on existing routes and cannot generate from scratch; Komoot cannot take a target distance as input; the coaching apps (Runna, TrainAsONE, AI Endurance, Coopah, Joggo) have no route capability at all [verified] (`research/02-competitors/gap-analysis.md`, Section b).
- Qualifier: "adequately" is time-sensitive. The pieces (Strava's generator, Runna's plan engine) have sat under one owner since April 2025 [verified] (`research/02-competitors/gap-analysis.md`, Section c, threat 1).

**What would change the verdict.**

- Strava shipping plan-linked route generation, AllTrails moving Custom Routes from adjustment to generation, or Apple building OS-level route suggestion (10 to 20 percent estimated within 18 months).
- The weekly early-warning signals (Runna beta strings, Strava routing engineer postings, bundle marketing language) are defined in `research/02-competitors/gap-analysis.md`, Section c.

**Consequence for the concept.** The wedge is real and open today; the verdict expires on the competitive clock, so the concept must ship inside the 12 to 18 month window (see H3 and the risk ledger in `research/04-synthesis/opportunity.md`).

## H3: Route generation is a stronger acquisition wedge than another plan product

**Hypothesis as stated.** Route generation is a stronger acquisition wedge than yet another training plan product (`vault/01-Project/Founder-Brief.md`). The Founder Brief assigns H3 to Phases 2 to 4, so this document is the final call.

**Verdict: SUPPORTED, with a monetization caveat.**

**Evidence summary.**

- The plan wedge is crowded and consolidating: Runna is the branded leader with Strava's 150M+ user funnel, Coopah owns a marathon channel, and Garmin and Apple give generic AI plans away free at the platform level [verified] (`research/02-competitors/gap-analysis.md`, Section b, H3).
- The route wedge is structurally open: the entire constraint block in the Phase 2 feature matrix is empty, and the only shipping generator is training-blind and generating documented safety complaints [verified] (same section).
- Demand for the route side is validated at three price points: free generators exist because runners keep asking, RunGo charges $59.99 per year for navigation alone, and Strava gates routes behind its $79.99 subscription as a conversion flagship [verified] (same section).
- Phase 3 strengthens the acquisition case: the two strongest-evidenced user needs (safety-aware routing, route novelty at home) are both wedge-native, and the third (training-state-to-route) is the wedge's seam with coaching [verified for the rankings] (`research/03-users/unmet-needs.md`, Section a, needs 1 to 3).
- The caveat: the wedge acquires better than it monetizes alone. Basic generation is price-anchored at zero by free web tools; revenue lives in the adaptive layer on top [inferred] (`research/02-competitors/gap-analysis.md`, Section b, H3 caveat; ties directly to H4 and H5).

**What would change the verdict.** Interviews showing runners perceive the six pain themes as unrelated annoyances rather than one job (the bundling test, `research/03-users/unmet-needs.md`, Section c and Open questions), which would narrow the wedge to safety routing alone.

**Consequence for the concept.** Adopt the Founder Brief's layering exactly as stated: route wedge for acquisition, adaptive coaching layer for revenue [inferred] (`research/02-competitors/gap-analysis.md`, Section b).

## H4: Committed amateurs will pay a freemium subscription for adaptive routes plus coaching

**Hypothesis as stated.** Committed amateurs will pay a freemium subscription where adaptive routes plus coaching are the paid tier (`vault/01-Project/Founder-Brief.md`). Assigned to Phases 1 and 6; Phase 6 owns the pressure test, so this is an interim verdict on desk evidence.

**Verdict: PARTIALLY SUPPORTED. Category-level willingness to pay is verified; feature-level and tier-split willingness to pay is unproven.**

**Evidence summary (what the desk evidence proves).**

- The target segment demonstrably pays in this category: Runna reached roughly 90,000 payers at $119.99 per year selling to exactly this user [verified as reported] (`research/01-market/market-sizing.md`, Section 4).
- RunGo proves payment for route navigation alone at $59.99 per year [verified] (`research/03-users/segmentation.md`, Section 3.3).
- AllTrails shipped an AI route tier (Peak, $79.99 per year, June 2025), validating paid demand adjacent to Waypoint's hero feature [verified] (`research/01-market/market-sizing.md`, Sections 5 and 6).
- Health and fitness apps lead all categories in payer lifetime value, with median download-to-paid conversion of 2.7 percent and top decile 12.1 percent [verified] (`research/01-market/market-sizing.md`, Section 3.3).

**What remains unproven, precisely.**

- That route generation specifically, rather than training plans, drives willingness to pay; AllTrails Peak attach rates would be the best proxy and are unknown [verified as open] (`research/01-market/market-sizing.md`, Sections 6 and 8, open question 3).
- That the specific freemium split (free basic routes, paid adaptive constraints plus coaching) converts: no mined community thread expressed willingness to pay for generated routes [verified as absence] (`research/03-users/unmet-needs.md`, Section b).
- Whether the 10 to 15 percent payer-share assumption holds for this segment [assumption] (`research/01-market/market-sizing.md`, Section 7, assumption 3).
- Where the safety-routing free-tier ethics line sits, which directly shapes the paid tier's contents [verified as open decision] (`research/03-users/unmet-needs.md`, Open question 2; `research/03-users/_index.md`).

**What would change the verdict.**

- The validation path runs through the interview backlog: Priority 1 interviews carry the explicit willingness-to-switch-and-pay questions with Phase 2 price anchors (`research/03-users/unmet-needs.md`, Section c).
- MVP telemetry signal 8 (paywall encounter-to-conversion by triggering feature) replaces the unmeasurable desk question with revealed preference (`research/03-users/unmet-needs.md`, Section d).
- Interview evidence of payment intent against the free heatmap workflow moves this to SUPPORTED; discovery that only the plan layer triggers payment moves it toward REFUTED for the specific tier design and forces repackaging.

**Consequence for the concept.** Price nothing the market gives away free; put the adaptive constraints and the training-state-to-route seam in the paid tier; resolve the safety free-tier decision with a decision record before Phase 6 pricing work [inferred] (`research/02-competitors/gap-analysis.md`, Section d; `research/03-users/unmet-needs.md`, Section b, implication 2).

## H5: The addressable market is venture-scale

**Hypothesis as stated.** The addressable market is large enough to support an investor story (`vault/01-Project/Founder-Brief.md`).

**Verdict: UNCERTAIN, leaning supported only with an expansion story. Adopted unchanged from Phase 1.**

**Evidence summary.**

- TAM: roughly $1.5B in 2025 for running app subscriptions globally, growing 11 to 14 percent per year [inferred from verified inputs] (`research/01-market/market-sizing.md`, Section 2).
- SAM: about 14 million committed amateur iOS runners in launch geographies, with a demonstrated spend pool of $150M to $300M [inferred] (Section 3).
- SOM at years 3 to 5, anchored on Runna's actual trajectory as the breakout specialist: 70,000 to 300,000 payers, roughly $5M to $30M ARR [inferred] (Sections 4 and 5).
- The tension: the category is real and growing, produced two strategic acquisitions in 2025 and a near-IPO (Strava at roughly $500M ARR, $2.2B valuation), but the wedge alone points to a strong $10M to $30M ARR business, not a standard venture path to $100M+ ARR [verified inputs, inferred conclusion] (Section 6).

**What would change the verdict.** Runna passing 500,000+ payers post-acquisition (raises the specialist ceiling); AllTrails Peak attach rates proving route-specific willingness to pay; validated Android and non-English economics (roughly doubling SAM); or payer-share evidence above 15 percent [verified as stated tests] (`research/01-market/market-sizing.md`, Section 6).

**Consequence for the concept.** The Business Blueprint must carry a credible expansion story (Android, geographies, broader coaching or outdoor surface) from day one, and the exit environment (Runna, Komoot acquisitions) is a legitimate secondary narrative [inferred] (`research/01-market/market-sizing.md`, Section 6; `research/01-market/_index.md`).

## H6: Mobile-first iOS with wearable integration is the right v1 form factor

**Hypothesis as stated.** Mobile-first iOS with wearable integration is the right v1 form factor (`vault/01-Project/Founder-Brief.md`). Assigned to Phases 3 and 5; Phase 5 (product definition) still confirms integration scope.

**Verdict: SUPPORTED on Phases 1 to 3 evidence.**

**Evidence summary.**

- Data access forces the choice as much as preference does: Garmin has paused new Connect Developer Program applications, and Strava's API bans AI use of its data, so personalization must be built HealthKit-first; HealthKit is the one open, first-party pathway to health and training data [verified] (`research/01-market/_index.md`, headline findings; `research/02-competitors/gap-analysis.md`, Section c, data enclosure multiplier).
- Device evidence points the same way: Apple Watch has been the most popular device on Strava since 2024, and Gen Z cites wearables as its biggest fitness investment 63 percent more often than Gen X [verified] (`research/03-users/segmentation.md`, Section 4).
- Market evidence: iOS is roughly 50 percent of the runner base weighted across launch geographies, skewing higher in the US at 58.9 percent, and subscription spend concentrates in the US and UK [verified inputs, inferred weighting] (`research/01-market/market-sizing.md`, Sections 2.3 and 3.2).
- Residual unknowns: the Apple Watch versus Garmin versus phone-only split within the target segment is not sized by any found source; the parallel screener survey (n of 100+) in the interview backlog gates integration scope, and MVP telemetry signal 6 hardens it after launch [verified as plan] (`research/03-users/unmet-needs.md`, Sections c and d).

**What would change the verdict.** Survey evidence that the target segment is Garmin-dominated to a degree that HealthKit-only personalization degrades the core experience; or Garmin reopening its developer program (which would relax the constraint, not reverse the verdict).

**Consequence for the concept.** iOS plus HealthKit plus Apple Watch is the v1 stack; treat Garmin users as a known-degraded experience and monitor the Garmin program status [inferred] (`research/02-competitors/gap-analysis.md`, Sections c and d).

## H7: Personalized routine building deepens retention after the route wedge acquires

**Hypothesis as stated.** Personalized routine building (body, schedule, needs) is a strong secondary need that deepens retention after the route wedge acquires the user (`vault/01-Project/Founder-Brief.md`).

**Verdict: PARTIALLY SUPPORTED. Every link in the chain is verified except the one the hypothesis actually asserts.**

**Evidence summary.**

- Link 1, verified: plan disruption is near-universal among plan followers; over 50 percent of marathoners miss 7 or more consecutive days in a build [verified] (`research/03-users/unmet-needs.md`, Section b, H7).
- Link 2, verified: trust breaks on adaptation quality, not plan quality; Runna's injury and rigidity complaint record documents it [verified] (same; `research/02-competitors/gap-analysis.md`, Section a, need 4).
- Link 3, verified: the calibration middle ground between Runna-aggressive and TrainAsONE-conservative is unclaimed [verified] (same).
- The unproven link: the community expresses plan pain as guilt and schedule, not as routes; the leap from "my plan broke" to "give me a personalized routine with routes" is Waypoint's inference, not users' words [inferred, flagged as such in the source] (`research/03-users/unmet-needs.md`, Section b, H7 caveat).
- The structural limit: retention mechanics (does routine depth reduce churn) are unmeasurable until a product exists [verified as limitation] (same section).

**What would change the verdict.**

- Priority 1 interviews test whether workout-route matching resonates as felt need once demonstrated (`research/03-users/unmet-needs.md`, Section c).
- MVP telemetry signals 4 (workout-route attach rate and completion delta) and 5 (post-disruption behavior) are the designated instruments (`research/03-users/unmet-needs.md`, Section d).
- Unprompted interview evidence connecting routines to route intelligence moves this to SUPPORTED; attach-rate telemetry near zero after launch moves it to REFUTED and demotes the coaching layer to a conventional plan feature.

**Consequence for the concept.** Build the training-state-to-route seam as the paid-tier centerpiece (it is also the defensible moat per H2 and H3), but do not promise retention economics on it to investors without labeling the inference [inferred] (`research/03-users/unmet-needs.md`, Section b, implication 3).

## Cross-hypothesis reading

- The verdicts interlock: H2 (open gap) and H3 (wedge strength) establish the position; H1's reframe redefines what the wedge retains on; H4 and H7 define what the paid layer must prove; H5 defines what the investor story must add; H6 fixes the platform.
- The load-bearing unknowns concentrate on the demand side (H1, H4, H7), and all three route through the same instrument: the five-study interview backlog plus MVP telemetry (`research/03-users/unmet-needs.md`, Sections c and d).
- Nothing in Phases 1 to 3 refutes the founder's concept; what the evidence changed is the emphasis (safety and novelty over travel, expansion story over wedge-alone economics) [inferred].

## Assumptions

- [assumption] Verdicts weigh desk evidence classes per the Phase 3 rubric (two independent classes for "strong"); a different analyst could move H1 or H4 one notch in either direction.
- [assumption] The 12 to 18 month Strava window used in H2's expiry note is an analytical judgment from Phase 2, not a sourced fact (`research/02-competitors/gap-analysis.md`, Assumptions).
- [assumption] No competitor shipped relevant features between the source documents' access date and this review (same day, 2026-07-30).
- [assumption] H3's SUPPORTED verdict treats acquisition and monetization as separable; if the wedge must carry monetization alone, H3 weakens toward UNCERTAIN (`research/02-competitors/gap-analysis.md`, Assumptions).
- [assumption] The 25 percent committed-amateur share and the 10 to 15 percent payer share, both load-bearing for H4 and H5, are Phase 1 judgment calls carried forward unvalidated (`research/01-market/market-sizing.md`, Section 7).

## Open questions

1. Do the Priority 1 interviews confirm the reframed H1 (travel as activation, safety plus novelty as retention), and does the bundling assumption survive contact with real runners? (`research/03-users/unmet-needs.md`, Section c.)
2. What do AllTrails Peak attach rates and Runna's post-acquisition payer count show? These are the two external numbers that would most move H4 and H5. (`research/01-market/market-sizing.md`, Section 8.)
3. Where does the safety free-tier ethics and liability line sit? This gates H4's tier design and needs a decision record before Phase 6. (`research/03-users/unmet-needs.md`, Open question 2.)
4. What is the Apple Watch versus Garmin versus phone-only split in the target segment? The parallel survey gates H6 integration scope. (`research/03-users/unmet-needs.md`, Section c.)
5. Does the Strava early-warning monitoring (Runna beta strings, routing engineer postings, bundle marketing language) stay quiet long enough for the 12 to 18 month window to hold? (`research/02-competitors/gap-analysis.md`, Section c.)

## Sources

Internal only, all accessed 2026-07-30: `vault/01-Project/Founder-Brief.md`; `research/01-market/_index.md`; `research/01-market/market-sizing.md`; `research/02-competitors/_index.md`; `research/02-competitors/gap-analysis.md`; `research/03-users/_index.md`; `research/03-users/unmet-needs.md`; `research/03-users/segmentation.md`. All external evidence is cited within those documents; no new external claims are introduced here.
