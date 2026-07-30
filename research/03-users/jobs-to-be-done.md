# Jobs-to-be-Done: What Runners Hire Waypoint to Do

Version-Timestamp: 2026-07-30 15:45:00 UTC-4

**Executive summary.** This document applies the jobs-to-be-done framework to the four Phase 3 personas (Marcus the committed amateur racer, Priya the traveling professional, Elena the safety-first city runner, Jake the ambitious beginner) and derives the jobs Waypoint should be hired for. The recommended main job is the umbrella job, not the travel job: "When it is time to run and my usual route does not fit today, I want to be handed the right route for me, right now, from here, so I can spend my energy running instead of planning and worrying." Travel is the sharpest episode of that job but is episodic; safety and home novelty are its daily forms (per the H1 synthesis in `pain-points.md`, Section 9). Eleven functional jobs are scored qualitatively for opportunity: the largest opportunities are safety-aware routing, matching the route to today's workout, and route novelty at home, because each combines high importance with low or nonexistent satisfaction from current solutions. Emotional jobs (feeling safe, feeling like a real runner, guilt-free flexibility) carry more retention weight than the social jobs, which Waypoint should serve by feeding Strava rather than building community. The wedge natively serves the where-and-which-route jobs; the coaching layer serves the calibration and plan-flexibility jobs; community, content libraries, and logging depth are explicitly not chased.

**Desk research disclaimer.** This is a synthesis of Phase 3 desk research (`pain-points.md`, `segmentation.md`, `personas.md`) and the Phase 2 gap analysis (`research/02-competitors/gap-analysis.md`), all dated 2026-07-30. No Waypoint user interviews exist. Job statements are constructed from community evidence and competitor complaint records, not from job-mapping interviews; satisfaction ratings and opportunity reasoning are qualitative judgments over that evidence, not survey-measured scores. Every job traces to its source document inline. Findings tagged [verified] trace to sourced evidence in those documents; [inferred] are reasoned conclusions; [assumption] is unsupported working belief. Interview validation requirements are consolidated in `unmet-needs.md`, Section c.

**Framework note.** Job statements use the standard situation-motivation-outcome format. Opportunity reasoning follows the logic of the Ulwick opportunity algorithm (opportunity grows with importance and with the gap between importance and current satisfaction: Opportunity = Importance + max(Importance - Satisfaction, 0)), applied qualitatively because no quantitative outcome survey exists yet [verified for the method] (Strategyn, "Jobs to Be Done: The Original Framework", https://strategyn.com/jobs-to-be-done/, accessed 2026-07-30; Ulwick, "What is Outcome-Driven Innovation", https://innovationroundtable.com/summit/wp-content/uploads/2014/05/Strategyn_what_is_Outcome_Driven_Innovation.pdf, accessed 2026-07-30).

## (a) Main job statement candidates

1. **The travel job.** "When I arrive in an unfamiliar city mid-training block, I want to know exactly where to run from my door, so I can keep my plan intact without spending my evening on research." Grounded in `pain-points.md` Section 1 (LetsRun threads, Great Runs existing solely to answer this question) and the Priya persona. Sharpest and most demo-able, but episodic for the core segment (a few trips per year for most committed amateurs) [verified for the pain, inferred for the frequency cap] (`pain-points.md`, Sections 1 and 9).
2. **The safety job.** "When I run at hours or in places where I do not feel safe, I want routes chosen with safety as the first constraint, so I can run without fear dictating my running life." Grounded in `pain-points.md` Section 3 (54 percent of surveyed women changed routes, 42 percent say safety dictates routine over preference) and the Elena persona. Highest intensity and best quantified, but segment-specific rather than universal [verified] (`pain-points.md`, Section 3; `personas.md`, Elena).
3. **The coaching job.** "When I am self-coaching toward a race around a busy life, I want each day's run decided for me, both what and where, so I can just lace up and go." Grounded in the Marcus persona and gap-analysis unmet need 1 (no product connects training state to route choice). Strong for the core payer but describes the layered product, not the wedge alone [verified for the gap, inferred for the demand] (`gap-analysis.md`, need 1; `personas.md`, Marcus).
4. **The umbrella job (recommended).** "When it is time to run and my usual route does not fit today (a new city, a dark morning, a heat wave, a tempo workout, or plain boredom with my loops), I want to be handed the right route for me, right now, from here, so I can spend my energy running instead of planning and worrying."

**Recommendation: candidate 4.** Reasoning [inferred]: the H1 synthesis concluded that travel friction alone is an activation moment, not a retention driver, while the same underlying question recurs daily through safety and novelty (`pain-points.md`, Section 9). The umbrella job contains all three narrower jobs as situations, matches the founder's own framing of the hero feature ("where should I run, right now, from here, for me", `vault/01-Project/Founder-Brief.md`), and keeps the coaching layer as a deepener rather than the wedge. Marketing can still lead with the travel situation because it is the most vivid instance of the job. The untested risk: whether runners themselves experience these situations as one job or as unrelated annoyances; this bundling assumption is flagged as the top open question in `pain-points.md` and must be arbitrated in interviews [assumption].

## (b) Functional jobs

Each job lists: situation trigger, current solution, satisfaction with current solution (rated from evidence), and opportunity reasoning. Satisfaction scale: none, low, moderate, high.

**FJ1. Find a trustworthy route in an unfamiliar place.**
- Trigger: business trip, race trip, vacation, relocation; morning run due, zero local knowledge (`pain-points.md`, Section 1; `personas.md`, Priya).
- Current solution: Strava heatmap scouting, Street View checks, hotel front desk, Great Runs guides, treadmill surrender [verified] (`pain-points.md`, Section 1).
- Satisfaction: moderate. The workaround stack usually produces an acceptable answer in 15 to 20 minutes; failure stories (3-hour lost run in Trieste, 8-mile "urban orienteering" in London) are vivid but anecdotal [verified] (`pain-points.md`, Sections 1 and 9).
- Opportunity: medium-high. Importance is high in the moment and frequency is high across the population, but satisfaction is not low enough for desperation. Strongest as activation, not retention [inferred].

**FJ2. Find a route that is safe at this hour.**
- Trigger: dark mornings and evenings, unfamiliar neighborhoods, winter; disproportionately women (`pain-points.md`, Section 3; `personas.md`, Elena).
- Current solution: manual "safety work": restricting to two proven loops, daylight-only running, keys between fingers, live-location sharing, route vetting on foot [verified] (`pain-points.md`, Section 3).
- Satisfaction: low. The current solution is self-restriction; 48 percent of surveyed women no longer feel comfortable running in their local area, and the only shipping route generator has produced actively dangerous output [verified] (`pain-points.md`, Section 3; `gap-analysis.md`, need 2).
- Opportunity: highest in the set. Very high importance, quantified at survey scale, zero product-side satisfaction (no competitor accepts safety as a routing input across fifteen-plus products) [verified for the gap, inferred for the score].

**FJ3. Get novelty and variety from my own front door.**
- Trigger: 3 to 5 runs per week from the same start point; long-run repetition in a marathon block (`pain-points.md`, Section 2; `personas.md`, Marcus).
- Current solution: manual map work, reversing loops, CityStrides street-completion projects, tolerated boredom [verified] (`pain-points.md`, Section 2).
- Satisfaction: low to moderate. Manual novelty engineering works but is effortful; emotional language ("reduced me to tears", "dreading") and a 90,000-user paying movement prove the gap [verified] (`pain-points.md`, Section 2).
- Opportunity: high. High frequency for the exact target segment, low satisfaction, and the incumbent actively steers the other way (Strava ranks by popularity, the opposite of "roads not yet run") [verified] (`gap-analysis.md`, need 6). Counter-evidence: same-loop loyalists exist, so novelty is a segment desire, not universal [verified] (`pain-points.md`, Section 2).

**FJ4. Match the route to today's workout.**
- Trigger: plan prescribes a tempo (needs flat, uninterrupted), an easy day (soft surface), or hill repeats; the app names the workout but not the place (`personas.md`, Marcus; `gap-analysis.md`, need 1).
- Current solution: none. Coaching apps have zero route capability; route apps have zero training context; "two different runners at the same corner get the same routes" [verified] (`gap-analysis.md`, need 1).
- Satisfaction: none. This job is structurally unserved across the entire competitive set [verified].
- Opportunity: high, with a caveat. The gap is total, but demand is inferred from product logic rather than expressed community pain; nobody in the mined threads asked for workout-matched routes in those words [inferred; interview needed].

**FJ5. Keep my training plan intact when life disrupts it.**
- Trigger: travel, illness, work, family; more than 50 percent of marathoners miss at least seven consecutive training days in a build [verified] (`pain-points.md`, Section 4).
- Current solution: guilt, cramming, manual plan surgery; apps adapt pace and schedule but never the where [verified] (`pain-points.md`, Section 4; `gap-analysis.md`, needs 1 and 3).
- Satisfaction: low on adaptation quality. Runna's loudest complaints are plans that adapt poorly to individual reality [verified] (`pain-points.md`, Section 4).
- Opportunity: high for the coaching layer. Important, frequent, poorly served; but the community expresses it as a schedule-and-guilt problem, and the route connection is Waypoint's framing, not theirs [inferred, flagged].

**FJ6. Adjust the route for heat and weather.**
- Trigger: summer heat and humidity, unmovable long runs (`pain-points.md`, Section 5).
- Current solution: change time of day first, cut pace 5 to 15 percent, eyeball shade; Runna's Adapt for Heat slows pace only [verified] (`pain-points.md`, Section 5; `gap-analysis.md`, need 3).
- Satisfaction: moderate. Satisficing by timing and pace mostly works; little organic first-person demand for route-level tooling was found [verified as absence].
- Opportunity: medium. Expert practice validates the lever (coaches tell runners to change routes for shade and water), but felt pain is the weakest of the six themes. Better positioned as a differentiating constraint inside FJ1 to FJ4 than as a standalone hook [inferred].

**FJ7. Execute an unfamiliar route hands-free.**
- Trigger: running any generated or new route, especially traveling; watch-course navigation prompts that cannot be silenced [verified] (`pain-points.md`, Section 6).
- Current solution: phone in hand, Garmin course navigation with documented rage ("I literally just want my phone to stop talking"), RunGo at $59.99 per year [verified] (`pain-points.md`, Section 6; `gap-analysis.md`, need 8).
- Satisfaction: low within the affected group, which is a minority of all runners.
- Opportunity: medium. Intense, verified anger plus a proven willingness-to-pay signal, but a narrower population. Strategically mandatory regardless of score: without execution, generated routes do not get run, and no product today takes a runner from "generate my run" through voice-guided execution [verified for the gap] (`gap-analysis.md`, need 8).

**FJ8. Get training calibration that will not injure me.**
- Trigger: beginner or returner starting a race build; overstated fitness meets aggressive defaults (`personas.md`, Jake; `gap-analysis.md`, need 4).
- Current solution: Runna (injury discourse, "even a easy day was a grind") or TrainAsONE (so conservative it caps ambition); the calibrated middle is unclaimed [verified as sentiment] (`gap-analysis.md`, need 4).
- Satisfaction: low at both ends of the market.
- Opportunity: high for the coaching layer, and the primary job for Jake and for returners [verified for the gap, inferred for the score].

**FJ9. Fit the run into the time I actually have.**
- Trigger: shortened windows; schedule is the top exercise blocker for business travelers at 71 percent [verified] (`segmentation.md`, Section 5).
- Current solution: "run for time instead of distance" advice, manually cutting routes short [verified] (`pain-points.md`, Section 4).
- Satisfaction: moderate. The workaround is easy but imprecise and plan-degrading.
- Opportunity: medium. Real and frequent, but low intensity; naturally served as a constraint (duration as input) rather than a separate feature [inferred].

**FJ10. Avoid interruptions and street crossings.**
- Trigger: urban tempo work, unfamiliar dense cities; "should I basically use it as a warmup... if I have to stop at every single street crossing" [verified] (`pain-points.md`, Section 1, Manhattan thread).
- Current solution: local human knowledge relayed in forum replies; trial and error [verified].
- Satisfaction: low where it matters (urban, quality workouts); currently solved only by asking locals.
- Opportunity: medium-high. A hero constraint that no competitor accepts as input [verified] (`gap-analysis.md`, Section b, H2 evidence); demand is expressed in community language, which strengthens it relative to FJ4 [inferred].

**FJ11. Track and log my running life.**
- Trigger: every run; race-build progress checks (`personas.md`, Marcus).
- Current solution: Strava, Garmin, Runna. Satisfaction: high. The incumbent stack serves this well [verified] (`gap-analysis.md`, Section d).
- Opportunity: low. Overserved. Waypoint posts TO Strava and does not compete here [verified for the strategy] (`gap-analysis.md`, Section d).

## (c) Emotional jobs

- **Feel safe, not brave.** Elena's core hire. Running should not require courage arithmetic; 82 percent of surveyed women runners worry about personal safety [verified] (`pain-points.md`, Section 3). The product corollary: explain WHY a route was chosen and degrade honestly ("no good route meets your constraints right now") rather than pretend [inferred] (`personas.md`, Elena).
- **Feel like a real runner.** Jake's core hire: identity formation through visible progress, a race finish, and not being made to feel slow; twice as many Gen Z as Gen X find picking up a new sport intimidating [verified] (`personas.md`, Jake).
- **Guilt-free flexibility.** Marcus and Priya. The guilt spiral around missed runs is the explicit framing of an entire coaching-content genre [verified] (`pain-points.md`, Section 4). The emotional deliverable is "the plan bent, you did not fail."
- **Confidence in unfamiliar places.** Priya's core hire. Replace the night-before research ritual and the 6 a.m. lobby doubt with trust; the run becomes a way to experience the city instead of a risk [inferred] (`personas.md`, Priya).
- **Novelty and exploration joy.** Marcus and Jake. "Now with CityStrides, it's always an adventure" and the documented "endorphin rush for completing new streets" show novelty is an emotional payoff, not just a functional one [verified] (`pain-points.md`, Section 2).

## (d) Social jobs

- **Post-worthy runs.** Jake wants "a personal best to post" and shareable moments for the club feed; Marcus logs everything to Strava [verified for the patterns] (`personas.md`, Jake and Marcus). Waypoint serves this by making generated routes and milestones export beautifully to Strava, not by hosting the feed [verified for the strategy] (`gap-analysis.md`, Section d).
- **Club belonging.** Run clubs grew 3.5x on Strava in 2025 and are Jake's entry point into the sport [verified] (`personas.md`, Jake). Waypoint should be club-compatible (routes you can share with a group) but must not compete with the social graph [verified] (`gap-analysis.md`, Section d).
- **Race identity.** Race motivation is the strongest for Gen Z (75 percent more likely than Gen X to cite a race as main motivation) and Marcus's calendar is anchored by 2 to 4 races per year [verified] (`personas.md`, Jake and Marcus). Served through the coaching layer's race builds, not through race content or community features [inferred].

Evidence note: social jobs have the thinnest direct evidence in the Phase 3 corpus; they are inferred from segment behavior data rather than mined complaints, and they rank below functional and emotional jobs for v1 [inferred].

## (e) Job map: persona x top 3 jobs

| Persona | Job 1 | Job 2 | Job 3 |
|---|---|---|---|
| Marcus (committed amateur racer) | FJ4 match route to today's workout | FJ3 novelty from my front door | FJ8 + FJ5 stay uninjured and keep the plan intact (guilt-free flexibility) |
| Priya (traveling professional) | FJ1 trustworthy route in an unfamiliar city, fast | FJ5 keep the plan intact across travel chaos | FJ7 hands-free execution (confidence in unfamiliar places) |
| Elena (safety-first city runner) | FJ2 route that is safe at this hour | FJ3 widen my running world beyond two proven loops | Privacy-preserving live sharing and home-location protection (emotional: feel safe) |
| Jake (ambitious beginner) | FJ8 get to the finish line uninjured | Emotional: feel like a real runner (progress, shareable moments) | FJ3 make runs feel like exploration, not laps |

Sources: persona job lists in `personas.md`; pain themes in `pain-points.md`; gap evidence in `gap-analysis.md`. Elena's third job is a trust requirement rather than a routing job; it is listed because route privacy is existential for her persona [verified for the stakes] (`personas.md`, Elena).

## (f) Which jobs the wedge serves, which the coaching layer serves, which not to chase

**Wedge-native (constraint-based route generation serves these directly):**
- FJ1 travel routes, FJ2 safety-aware routing, FJ3 novelty at home, FJ6 weather-adjusted routes, FJ9 time-boxed routes, FJ10 crossing-aware routes. All are route-selection problems under constraints, exactly the hero feature (`vault/01-Project/Founder-Brief.md`). FJ2 and FJ3 are the daily retention jobs; FJ1 is the activation and demo job [inferred from `pain-points.md`, Section 9].
- FJ7 navigation execution is wedge-adjacent and mandatory: generation without execution leaves the job half done, and the execution layer has proven standalone willingness to pay [verified] (`gap-analysis.md`, need 8).

**Coaching layer (serves after the wedge acquires):**
- FJ4 workout-route matching (the seam where wedge and coaching meet, and the single most important gap in the market per `gap-analysis.md` need 1), FJ5 plan flexibility without guilt, FJ8 injury-safe calibration. These carry H7 (routine personalization as retention deepener) and the monetization load, since basic generation is anchored at zero by free tools [verified] (`gap-analysis.md`, Section b, H3 caveat).

**Do not chase (with reasoning):**
- FJ11 logging and the social graph: overserved by Strava's 195M-user moat; post to it instead [verified] (`gap-analysis.md`, Section d).
- Club and community hosting: same moat; club growth happens on Strava, and v1 correctly has no social scope [verified] (`gap-analysis.md`, Section d).
- Trail content and curated route libraries: AllTrails' 500,000+ verified trails and Komoot's 15 years of data are unreplicable; generate, do not curate [verified] (`gap-analysis.md`, Section d).
- Beginner invisibility routing (the Section 7 bonus theme in `pain-points.md`): real, but the pre-committed beginner is below the target segment; park as a future persona input [inferred] (`pain-points.md`, Section 7).
- Human-coach warmth positioning: Coopah owns it; Waypoint's coaching flag is the route, not the relationship [verified] (`gap-analysis.md`, Section d).

## Assumptions

- [assumption] The four personas experience their situations as one umbrella job rather than unrelated annoyances; this bundling assumption underlies the recommended main job and the hero-feature thesis, and it is untested (flagged in `pain-points.md`, open questions).
- [assumption] Qualitative opportunity ratings substitute acceptably for measured importance and satisfaction scores until interviews and surveys exist; ratings here would not survive an ODI practitioner's scrutiny as data.
- [assumption] Demand for FJ4 (workout-route matching) exists even though no community post articulates it; it is derived from product logic and founder intuition, the weakest evidence class in this document.
- [assumption] Satisfaction ratings inherit the biases of the Phase 3 corpus: forum posters over-index on the aggrieved, and satisfaction of the silent majority may be higher than rated.
- [assumption] Emotional and social job rankings are inferred from behavior data, not from interviews about feelings; the identity jobs (Jake) could outrank functional jobs in reality.

## Open questions

1. Do committed amateurs recognize the umbrella job when it is played back to them, or do they see six unrelated problems? This is the make-or-break framing test for the main job statement [interview needed, feeds `unmet-needs.md` Section c].
2. Does FJ4 (workout-route matching) resonate as a felt need once demonstrated, or only as a neat feature? Demand is currently inferred, not expressed.
3. Which of FJ2 (safety) and FJ3 (novelty) retains better in practice? The H1 synthesis bets on the combination; instrumentation should separate them (see `unmet-needs.md`, Section d).
4. What does Elena require before she trusts an algorithmic safety claim, and does any evidence threshold exist at all? A wrong answer is a product-killing liability (`pain-points.md`, Section 10).
5. Is Priya a distinct persona or Marcus-in-a-hotel? If the latter, the travel job is a mode of the main job, which strengthens the umbrella framing (`personas.md`, open question 5).
6. Do social jobs matter enough to shape v1 export features, or is a clean Strava post sufficient for launch?

## Sources

- Internal (all accessed 2026-07-30): `research/03-users/pain-points.md`, `research/03-users/segmentation.md`, `research/03-users/personas.md`, `research/02-competitors/gap-analysis.md`, `vault/01-Project/Founder-Brief.md`.
- Strategyn (Tony Ulwick), "Jobs to Be Done: The Original Framework", https://strategyn.com/jobs-to-be-done/, accessed 2026-07-30.
- Ulwick, "What is Outcome-Driven Innovation" (opportunity algorithm), https://innovationroundtable.com/summit/wp-content/uploads/2014/05/Strategyn_what_is_Outcome_Driven_Innovation.pdf, accessed 2026-07-30.
