# User Journeys: Complete Experience Maps

Version-Timestamp: 2026-07-30 15:55:00 UTC-4

**Executive summary.** Five end-to-end journeys operationalize the locked concept (DEC-006, `research/04-synthesis/concept.md`) into design-ready experience maps: (1) first-run onboarding for all personas, install to first generated route in under 3 minutes; (2) Marcus's daily home run, from route boredom to a novel workout-matched route shared to Strava, including the paid-layer upsell moment; (3) Priya's hotel-lobby run, the activation moment, including the offline fallback and the trust-building "why this route" explanation; (4) Elena's dark winter morning, safety-aware routing as the primary constraint, including the claim-liability communication rule (never promise "safe") and honest degradation when safety data is missing; (5) Jake's week-6 plan disruption and the adaptive routine repair flow. Each journey maps stages (doing, thinking, feeling, product response), moments of truth, failure states with recovery, and a success metric. The document closes with ten cross-journey design principles and the five screens or flows that design work should start from. Per the accepted H1 reframe: journey 3 is how users arrive, journeys 2 and 4 are why they stay, journey 5 is why they pay.

**Desk research disclaimer.** These journeys are synthesized from Phase 3 desk research (`personas.md`, `jobs-to-be-done.md`, `pain-points.md`) and the locked Phase 4 concept. No Waypoint user interviews or usability sessions exist yet. Stage-level thinking and feeling entries are grounded in documented community evidence where cited and are otherwise reasoned persona projections, labeled accordingly. Journeys must be pressure-tested against the interview program running alongside Phase 5 and against first usability tests before they harden into final flows.

## How to read this document

- [verified] traces to a sourced finding in a prior research document; citation inline.
- [inferred] is a reasoned conclusion from verified inputs.
- [assumption] is unverified working belief, consolidated at the end.
- "Product response" columns are design intent, not shipped behavior; they inherit the concept's obligations (privacy zones, private-by-default, EU AI Act transparency, the safety claim-liability rule).

---

## Journey 1: First-run onboarding (all personas)

**Goal: install to first generated route in under 3 minutes.** The first generated route IS the onboarding payoff; everything else is deferred until it has a reason to exist. Onboarding drop-off concentrates at permission walls and long questionnaires [inferred from category patterns; usability testing needed], so Waypoint asks for nothing before showing value and asks for everything at the moment it becomes useful.

### Permission sequencing and copy principles

Order of asks, each at its moment of value, never as a cold-launch wall:

| # | Ask | When | Copy principle | Skippable? |
|---|---|---|---|---|
| 1 | Location (While Using, precise) | The moment the user taps "Generate my route", not before | One pre-permission screen in plain language: "Waypoint generates routes from wherever you stand. Location is used to build your route and guide your run. Your routes are private by default and your home is never shared." Then the system dialog | Yes: manual start point via map search (degraded but functional) |
| 2 | Home privacy zone | Immediately after the first route is generated from a location the user marks as home, or on first save or share, whichever comes first | "Hide where you start. Runs near home will show a trimmed route to anyone you share with. Only you see the real start." Zone suggested on the map, user adjusts radius, confirms | No default sharing exists to leak; zone confirmation required before any share from home area [verified as compliance obligation, `concept.md` section 4] |
| 3 | HealthKit (read, granular) | After the first completed run, or when the user first touches a training-state feature, whichever comes first | "Waypoint can shape routes around what your body needs: readiness, recent load, recovery. Connect Apple Health to turn this on. Read-only, on-device where feasible, never sold." | Yes: constraint-based generation works fully without it |
| 4 | Notifications | Only after there is something worth notifying: first completed run triggers "Want a heads-up when tomorrow's route is ready?" | Ask tied to a named, concrete benefit; never "turn on notifications" in the abstract | Yes, and declining is never re-prompted inside the same month [inferred best practice] |

EU AI Act Article 50 transparency (effective 2026-08-02): the first screen that shows AI-generated output (the first route reveal) carries the AI disclosure, integrated into the "why this route" card rather than a separate legal interstitial [verified as obligation, `concept.md` section 4].

### Calibration questions (kept minimal)

Three questions maximum, all tappable chips, all skippable, total budget 20 seconds:

1. "How often do you run?" (rarely / 1 to 2 / 3 to 5 / most days). Seeds distance defaults.
2. "What feels like a normal run?" (distance chips, unit toggle). Seeds the generate screen.
3. "Training for something?" (no / 5K / 10K / half / marathon / other). Seeds the coaching layer conversation later; "no" ends the topic.

Everything else (surface preference, elevation taste, safety priorities, crossing tolerance) is learned from behavior or set contextually when the relevant constraint first matters, never front-loaded [inferred from FJ-level evidence that constraint needs are situational, `jobs-to-be-done.md`].

### Stages

| Stage | Doing | Thinking | Feeling | Product response |
|---|---|---|---|---|
| 1. Install and open (0:00 to 0:20) | Opens app from the App Store | "Another running app. Show me fast." | Skeptical, low patience [inferred] | One value screen, five words plus the tagline "Know where to run". Single button: "Find my first run". No account wall; sign-in deferred to first save [assumption: deferred auth is technically acceptable for v1, flag for `prd.md`] |
| 2. Calibration (0:20 to 0:40) | Taps three chip questions or skips | "Fine, but this better be short" | Tolerant if visibly finite | Progress shown as "2 of 3". Skip visible on every screen |
| 3. Location ask (0:40 to 1:00) | Reads pre-permission screen, taps allow | "Why do you need this? ... OK, that is what the app is for" | Guarded; this is the trust gate | Plain-language reason, privacy promise, then the system dialog. Denial path stays functional (stage F1 below) |
| 4. First generation (1:00 to 1:40) | Watches the route draw, reads the summary | "Is this actually good? Would I run this?" | The make-or-break moment: curiosity turning to either trust or dismissal | Route appears in under 30 seconds with distance, elevation, surface summary and the "why this route" card. Regenerate button beside it: variety is one tap away |
| 5. Home zone (1:40 to 2:20) | Confirms or adjusts the suggested privacy zone | "Good that they asked. This app takes it seriously" | Reassured, especially Elena [verified for the stakes: route privacy is existential for the safety persona, `personas.md`] | Suggested radius on the map, drag to adjust, one tap to confirm. Copy explains what it does, not just what it is |
| 6. Ready to run (2:20 to 3:00) | Taps "Start" or saves for later | "That was easy. I know where I am running" | Small win banked | "Start with voice guidance" primary, "Save for later" secondary. HealthKit and notifications NOT asked yet |

### Moments of truth

1. **The location pre-permission screen.** Denial without a recovery path kills the product at minute one. The explainer must earn the grant; the manual fallback must catch the denial [inferred].
2. **The first route reveal.** Under 30 seconds, and the route must be visibly sane (no highways, no dead-end industrial parks). One bad first route confirms the skeptic's prior; the category's only shipping generator is documented producing "12 miles of very unsafe roads" [verified, `gap-analysis.md` via `personas.md` Marcus] and Waypoint must not repeat that first impression.
3. **The 3-minute budget.** Every added screen is paid for in activation. Anything not on the critical path to a generated route moves after it.

### Failure states and recovery

| Failure | Recovery |
|---|---|
| F1. Location denied | Map search for a start point ("Where will you run from?"). Full generation still works. Soft re-ask only at natural moments (first travel use, first voice-guided start) |
| F2. No network at first open | Honest empty state: "Waypoint needs a connection to build your first route." Retry button, no spinner theater. Nothing to cache yet, so no pretend-offline |
| F3. Route engine returns a weak route (sparse map data area) | Label honestly on the reveal card: "Limited route data around here. This is the best loop we could build; help us by flagging anything wrong." Never present a weak route as confident [inferred from the degrade-honestly principle] |
| F4. GPS fix poor (urban canyon, indoors) | Start point snaps to nearest plausible outdoor point with a "starting near..." confirmation instead of silently guessing |
| F5. User abandons mid-onboarding | State is saved; next open resumes at the last stage, not the beginning |

### Success metric

Median time from first open to first generated route, target under 3 minutes; supporting: percent of installs that generate a route in the first session (activation), location grant rate at the pre-permission screen. [assumption: specific numeric targets belong to `metrics.md`, Phase 6]

---

## Journey 2: Marcus, the daily home run

**From "bored of my loops" to a novel route matched to today's workout, voice-guided, saved, and shared to Strava.** Route boredom at home is verified, emotionally loud pain ("almost reduced me to tears", "dreading going out on my run") and the run-every-street movement proves 90,000+ people pay for exactly the "roads not yet run" desire [verified, `pain-points.md` section 2]. Marcus is the retention persona: this journey is the one that must work three to five times a week.

Preconditions: onboarded, several runs logged, home zone set, Strava connected (connect prompted at first share, not before). Free tier throughout except the marked upsell moment.

### Stages

| Stage | Doing | Thinking | Feeling | Product response |
|---|---|---|---|---|
| 1. Tuesday 6:10 a.m., kitchen | Opens Waypoint while lacing up | "Tempo day. Not the canal loop again. I cannot face the canal loop" | Bored before the run starts [verified as segment pattern, `pain-points.md` section 2] | Generate screen defaults are already right: distance from his plan or his habit, "New roads" toggle remembered from last time |
| 2. Generate | Taps "Generate", glances at constraint chips (10K, flat, minimize crossings) | "Flat and uninterrupted, it knows it is a tempo... let us see" | Mild anticipation | Route in under 15 seconds from warm location. Novelty engine excludes his logged history: 40 percent of this route is streets he has never run [inferred capability from concept section 4, "roads you have not run"] |
| 3. The reveal | Scans map, reads "why this route" | "Huh. I did not know that street connected through" | The novelty spark: the CityStrides "endorphin rush" moment [verified for the emotion, `pain-points.md` section 2] | Card: "Flat (23m gain), 2 crossings, 40 percent new streets for you. Long uninterrupted stretch on the greenway for your tempo blocks" |
| 4. Run, voice-guided | Pockets phone, runs on watch cues | "Turn cues are early enough. I am not thinking about the map at all" | Flow; attention on pace, not navigation | Voice turn-by-turn calibrated to running speed; Apple Watch haptic plus glance. No chatter between turns: the Garmin "phone will not shut up" rage is the anti-pattern [verified, `pain-points.md` section 6] |
| 5. Missed turn | Overshoots a turn mid-interval | "Do not make me stop" | A flash of the old navigation anxiety | Silent recompute within seconds, next cue adjusts, distance target preserved. No "recalculating" scolding |
| 6. Finish and save | Ends run at his door | "That was a good one. Keeping it" | Satisfied; a new loop enters the rotation | Post-run summary; "Save route" one tap; the run teaches preferences (he never took the gravel spur: noted) [inferred from concept learning loop] |
| 7. Share to Strava | Taps share | "The club will ask where that route came from" | Small pride, social payoff [verified as social job, `jobs-to-be-done.md` section d] | Posts activity to Strava with the home privacy zone trimming the start and end. Waypoint never hosts the feed [verified strategy, `gap-analysis.md` via concept section 7] |

### The paid-layer upsell moment

Trigger: Marcus's plan (or his pattern) calls for hill repeats on Thursday. He opens the generate screen and manually drags elevation to "hilly", as he can, free, forever.

| Element | Design intent |
|---|---|
| Timing | At the moment the manual constraint visibly duplicates what the plan already knows: once, contextually, after he has set a workout-shaped constraint by hand |
| Copy | "Your plan wants hills on Thursday. Waypoint can read your plan and your recovery and build each day's workout as a route automatically. Try the coach free for N days." |
| Rules | Shown once per trigger context, dismissible, dismissal remembered. The free path (manual constraints) is never degraded to force the upgrade. Never interrupts pre-run flow: shown on the reveal card or post-run, not between him and the door [inferred from the never-nag principle and category billing distrust, `gap-analysis.md` unmet need 7] |
| Why here | FJ4 (match the route to today's workout) is structurally unserved in the entire market [verified, `jobs-to-be-done.md` FJ4]; the upsell moment is the exact seam where the free wedge meets the paid layer |

### Moments of truth

1. **The novelty is real.** If "new route" is his canal loop with one extra spur, the promise dies quietly. Personal history exclusion is the feature, not a nicety.
2. **Voice guidance stays silent between turns.** The verified anti-pattern is the incumbent's unstoppable chatter [verified, `pain-points.md` section 6]; Waypoint wins by respecting attention.
3. **The Strava post renders beautifully with the home trimmed.** One home-location leak destroys trust permanently; one ugly post kills the social payoff [verified for the privacy stakes, `personas.md` Elena, applies to all].
4. **The upsell lands as a helpful observation, not a toll booth.** Category-wide billing distrust means one pushy moment reads as a trap [verified, `gap-analysis.md` unmet need 7].

### Failure states and recovery

| Failure | Recovery |
|---|---|
| F1. Generated route overlaps his known loops heavily | "Regenerate" with an explicit "more new streets" nudge; if the area is genuinely exhausted, say so: "You have run 92 percent of streets within 5K of home. Want to start from a different point?" (honest, and itself a delight moment) |
| F2. Voice nav audio fails mid-run (Bluetooth drop) | Watch haptics carry navigation alone; phone banner on next glance. Never a dead route mid-run |
| F3. Strava API down or token expired | Run is safe locally; share queued with visible status and auto-retry; re-auth prompted calmly. Never lose a run [inferred from stability standard] |
| F4. Plan wants hills, area is flat | Honest constraint conflict: "Your area tops out at 40m of gain in 10K. Here is the hilliest option; want the workout adapted to what is here instead?" (the coaching layer's adaptation as visible value) |
| F5. He ignores the upsell forever | Nothing happens. Free tier remains fully useful; the relationship is the asset [verified strategy, concept section 6, trust as brand] |

### Success metric

Generated-route runs per weekly active user (the retention wedge measured directly); supporting: percent of runs on freshly generated vs repeated saved routes, save rate of generated routes, trial-start rate from the workout-constraint upsell moment.

---

## Journey 3: Priya, the hotel-lobby run

**Opens the app in a new city at 6 a.m. and gets a trustworthy route immediately.** This is the activation moment and demo story [verified, DEC-006 gate decision 4]. The verified failure modes she is escaping: the 15-to-20-minute heatmap-plus-Street-View ritual, the front-desk map, the treadmill surrender, and the documented disasters (a 4-mile London run becoming 8 miles of "urban orienteering", 3 hours lost in Trieste) [verified, `pain-points.md` section 1].

Preconditions: onboarded at home weeks ago; mid marathon block; landed last night; 10 miles on the plan; flight-drained and time-boxed.

### Stages

| Stage | Doing | Thinking | Feeling | Product response |
|---|---|---|---|---|
| 1. 5:55 a.m., hotel lobby | Opens Waypoint | "Ten miles, unknown city, meeting at nine. I do not have time to research" | Time pressure plus low-grade unease about an unfamiliar place [verified as pattern, `pain-points.md` section 1] | App detects she is far from her home zone: travel context activates automatically. No mode to find, no setup |
| 2. One decision | Confirms distance (pre-filled from her plan if paid, from habit if free) | "It already knows what I need to do today" | Relief at zero configuration | Generate screen pre-filled; travel defaults bias toward populated, well-lit, low-crossing streets at this hour without being asked [inferred design intent from FJ1 plus FJ2 overlap] |
| 3. The 30-second trust decision | Reads the route and the "why this route" card | "Waterfront path, main avenues, nothing sketchy-looking... can I trust an algorithm here?" | The whole journey compresses into this moment | Route in under 30 seconds. Why-card: "Follows the riverfront path popular with morning runners, stays on lit main streets, 4 crossings in 10 miles, loops back past your start at mile 5 in case you need to cut it short." Data confidence stated plainly (see degradation below) |
| 4. Out the door, voice-guided | Runs on watch and earbuds, phone pocketed | "I am not stopping on a corner staring at my phone in a strange city" | Growing confidence; the city becomes scenery, not threat [inferred, `personas.md` Priya emotional job] | Turn cues tuned for unfamiliar ground: slightly earlier, with street names. Mid-route landmark confirmations sparse but present ("along the river for the next 3 miles") |
| 5. The cut-short option | At mile 5, checks time | "I have margin. Full ten" | In control | Route was built with a bail-out point by design; watch shows "shortcut back: 1.2 miles" as a standing option, never a nag |
| 6. Back at the hotel | Ends run, showers, makes the meeting | "That just worked. In a city I have never seen" | The activation high: this is the story she tells | Post-run: run saved, plan updated, share to Strava. Tomorrow's city? Same one tap |

### The "why this route" explanation (trust architecture)

In an unfamiliar place she cannot verify the route from knowledge, so the explanation carries the entire trust load [inferred]:

- Name the concrete, checkable reasons: street types, path names, crossing counts, lighting basis, popularity signals ("used by morning runners" style evidence).
- State what the data is and is not: "Lighting scores here are from street-lamp map data, last verified [date]." Never imply on-the-ground verification that does not exist.
- Always include the escape hatch in the route itself (bail-out points on long routes) and say so; knowing the exit exists is itself trust [inferred].
- The AI disclosure (EU AI Act Article 50) lives here naturally: "Generated by Waypoint's route engine from OpenStreetMap and open lighting data."

### Offline and poor-data fallback

| Condition | Behavior |
|---|---|
| Connectivity at generation, lost mid-run | Full route, voice cues, and map corridor are cached at generation time by default; the run continues offline without degradation [inferred requirement from the travel form-factor stress case, `personas.md` H6 row] |
| No connectivity at 6 a.m. (roaming failure, hotel dead zone) | Two layers: (a) if the app saw the new city the evening before (location change detected at arrival), it prompted "In Chicago? Build tomorrow's route now" and pre-generated; (b) if nothing is cached, honest offline mode offers a conservative cached-tile out-and-back along major streets, clearly labeled: "No connection. This is a simple out-and-back on main streets, not a full Waypoint route." |
| Sparse map or context data in this city | Confidence labeling on the why-card: "Limited lighting data in this area. This route sticks to major streets as a precaution." Degrade honestly, never silently [inferred from Elena's principle, applied globally] |

### Moments of truth

1. **Speed to a credible route: under 30 seconds.** Her alternative costs 15 to 20 minutes she does not have [verified, `pain-points.md` section 1]. Slow is identical to broken at 6 a.m.
2. **The first two turns are correct.** One wrong early cue in an unknown city and the phone comes out of the pocket for the rest of the run, and the treadmill wins tomorrow.
3. **The why-card survives her skepticism.** She is deciding whether to bet a workout, and some personal safety, on an algorithm; specific checkable reasons beat reassuring adjectives [inferred; interview open question 3 in `personas.md` applies].
4. **The pre-generation prompt the night before fires at the right moment.** It is the difference between a fallback and a failure when roaming data drops.

### Failure states and recovery

| Failure | Recovery |
|---|---|
| F1. No network, nothing cached | Labeled conservative out-and-back (above); never a blank screen at 6 a.m. |
| F2. Route blocked on the ground (construction, closed gate) | One-tap "reroute around this" on watch or phone; recompute preserves target distance |
| F3. Route feels wrong (isolated stretch she does not like) | One-tap "route me via busier streets" recompute; her correction is logged as a preference and, aggregated and anonymized, as a data signal [assumption: feedback aggregation design pending privacy review] |
| F4. GPS urban-canyon drift downtown | Navigation falls back to distance-and-street-name cues rather than snapping wrongly; states uncertainty instead of guessing |
| F5. Her plan needed 10 miles, safe options cap at 7 | Honest conflict: "Best route meeting your constraints here is 7 miles. Run it plus a 3-mile repeat of the riverfront section, or accept fewer constraints?" Never silently shorten her training |

### Success metric

Travel activation rate: percent of away-from-home-zone opens that end in a started route within 5 minutes; supporting: cached-route usage rate on travel runs, completion rate of travel routes vs home routes (a trust proxy).

---

## Journey 4: Elena, the dark winter morning

**Safety-aware routing as the primary constraint.** The strongest-evidence unmet need in the research program: 92 percent of women runners report safety concerns, 54 percent changed routes over safety, 42 percent say safety dictates routine over preference, and zero of fifteen-plus products accept safety as a routing input [verified, `pain-points.md` section 3, `concept.md` section 3]. For Elena the route IS the safety decision; today's workaround is shrinking her running world to two proven loops [verified as pattern].

Preconditions: onboarded; home zone set on day one; it is 6:15 a.m. in January, dark for another 90 minutes.

### How safety preferences are set

- Not a buried mode. Safety-aware is a first-class, always-visible constraint on the generate screen, weighted up or down like distance or elevation [verified as requirement, `personas.md` Elena: "first-class routing constraints, not a mode"].
- Set contextually, not interrogatively. The first time she generates in dark hours, one card: "Running in the dark? Waypoint can prioritize lit, populated streets. Set how strongly." Choices: prioritize strongly / balance / off. Adjustable anytime; the setting is remembered per time-of-day context [inferred].
- Onboarding never asks "are you worried about safety": that framing is presumptuous and fear-based, which the brand explicitly avoids [verified as flagged brand-ethics position, `personas.md` Elena].
- Granular sub-preferences (avoid parks after dark, avoid underpasses, prefer open-business corridors) live one tap deeper for those who want them; defaults are sensible without them.

### The claim-liability communication rule

Waypoint never promises "safe." The word "safe" as a product claim is banned; the framing is "safety-aware," always [verified as locked concept language, `concept.md` section 4; liability basis in `unmet-needs.md` via concept].

| Surface | Copy rule |
|---|---|
| Constraint label | "Safety-aware" with an info tap, never "safe routes" |
| The info explainer | States exactly what the engine considers: "This weighting prefers streets with mapped lighting, more foot traffic, open businesses, and residential density at this hour. It cannot see current conditions, people, or events. No route is guaranteed safe, and this is not a substitute for your own judgment." |
| Why-card on a safety-weighted route | Concrete factors, no adjectives of assurance: "Lit throughout (street-lamp map data), passes 24-hour pharmacy and two bus stops, avoids the towpath after dark" and never "this route is safe" |
| Marketing and App Store copy | Same rule; additionally no fear-based imagery or framing [verified as brand position, `personas.md` Elena] |
| Degradation states | Missing data is stated, never papered over (below) |

This rule is testable in copy review: any sentence where "safe" is an unqualified predicate of a route fails review [inferred, proposed as a design-system lint rule].

### Stages

| Stage | Doing | Thinking | Feeling | Product response |
|---|---|---|---|---|
| 1. 6:05 a.m., apartment | Considers whether today is a run day at all | "Dark until 7:45. The two loops again, or nothing" | The fear tax: preference already surrendered to safety [verified at survey scale, `pain-points.md` section 3] | App is already in her dark-hours context: safety-aware weighting on, as she set it |
| 2. Generate | Taps generate, 5K, safety-aware strong | "Show me something that is not loop A or loop B... and do not send me somewhere stupid" | Guarded hope; algorithmic routes have a documented record of dangerous output [verified, `gap-analysis.md` unmet need 2] | Route generated with the why-card leading on the safety factors, concrete and checkable |
| 3. Scrutiny | Zooms the map, checks the streets she knows | "Main road, the high street, past the station... it avoided the canal path. It actually avoided the canal path" | The trust hinge: the app just demonstrated it knows what she knows | Every segment choice is explainable on tap: "canal towpath excluded after dark per your setting" |
| 4. Run | Runs it, phone pocketed, watch cues | "Populated the whole way. I know where the exits are because it showed me" | Vigilance still present (the app never removes it, and never claims to) but the planning burden is lifted | Cues favor early warning before turns; the route was built with no dead-end segments and bail-outs to main roads [inferred design intent] |
| 5. A segment feels wrong | A stretch is emptier than expected | "That bit was dead. The data did not know" | Momentary spike; trust dented but not broken IF the app was honest up front | One-tap mid-run "avoid this next time" flag; reroute option to the nearest main street. Flag feeds her preferences immediately and the scoring layer in aggregate [assumption: aggregation pending privacy design] |
| 6. Home | Finishes, third new route this month | "My running world is growing again" | The retention emotion: expansion instead of shrinkage [verified as goal, `personas.md` Elena] | Streak of new-streets shown without gamification pressure; share to Strava trims her home zone automatically, route private by default |

### Graceful degradation when safety data is missing

The rule: degrade honestly, offer agency, never pretend [verified as persona requirement: "degrade gracefully by saying no good route meets your constraints rather than pretending", `personas.md` Elena].

| Data condition | Product behavior |
|---|---|
| No lighting data for her area | Why-card states it plainly: "We do not have street-lighting data for this area yet. This route uses main roads and residential density as stand-ins. Treat it as less certain." Weighting falls back to the proxies it does have, and says which |
| Partial data (lighting known downtown, unknown in her neighborhood) | Per-segment honesty: confident segments and unknown segments visually distinguished on the route preview, with a one-line legend |
| No route satisfies her constraints at this hour | The honest refusal, offered with options: "No route within 5K meets your safety weighting right now. Options: your saved Loop A (you know it), a shorter 3K on the high street, or a route after 7:45 when it is light." A non-answer with agency beats a pretend answer |
| Data exists but is stale | Freshness stated on the info tap ("lighting data last updated ...") rather than implied current |

### Moments of truth

1. **The first dark-morning route she actually runs.** Everything before it is theory; interview evidence says the trust threshold for algorithmic safety claims is unknown and possibly very high [verified as open question, `personas.md` open question 3]. The concrete, checkable why-card is the only instrument that can pass this test.
2. **The honest refusal.** The first time the app says "no good route right now" it either cements trust permanently (it does not pretend) or churns her (it failed to deliver). Pairing the refusal with real alternatives is what separates the two [inferred].
3. **Zero home leakage, ever, across every surface.** One leak is unrecoverable for this persona and a public trust incident for the brand [verified for the stakes, `personas.md`, `concept.md` day-one obligations].
4. **The empty-street moment (stage 5).** Reality will contradict the data sometimes. Whether trust survives depends entirely on whether the app claimed certainty it did not have.

### Failure states and recovery

| Failure | Recovery |
|---|---|
| F1. Missing or stale safety data | Honest degradation ladder above |
| F2. Route contradicts her local knowledge ("that street is bad at night") | "Avoid this street" flag pre-run from the preview; correction respected permanently for her, weighted into aggregate scoring |
| F3. Mid-run discomfort | One-tap reroute to nearest main street; live cue recompute; post-run flag prompt kept optional (no forced incident reporting) |
| F4. Constraints unsatisfiable | The honest refusal with alternatives (above); never a silently relaxed constraint. If the app loosens anything, it says exactly what and asks first |
| F5. She shares a route and worries afterward | Shared routes from her home area are always zone-trimmed; a "what others can see" preview is available before every share (transparency as reassurance) |

### Success metric

Dark-hours retention: weekly generated-route runs during her local dark hours per safety-weighted user (measures whether her running world expanded); supporting: honest-refusal follow-through rate (percent who take an offered alternative rather than closing the app), mid-run safety flag rate trending down per area over time.

---

## Journey 5: Jake, week 6, the missed week

**The adaptive routine repair flow.** More than 50 percent of marathon-plan runners miss at least seven consecutive training days [verified, `pain-points.md` section 4]; the market's failure modes are documented at both ends: Runna-style plans too aggressive ("even a easy day was a grind", injury discourse) and TrainAsONE-style too conservative (ambition-capping) [verified as sentiment, `gap-analysis.md` unmet need 4]. Jake is the persona the aggressive end injures [verified, `personas.md` Jake]. The repair flow is the paid layer's clearest demonstration of value and the emotional deliverable is verified: "the plan bent, you did not fail" [verified framing, `jobs-to-be-done.md` section c].

Preconditions: Jake is a paying (or trialing) coach-layer user, week 6 of a 12-week half-marathon plan, first race. A chest cold took out the whole of week 5. He has opened the app once during the week and closed it fast, guilt intact.

### Stages

| Stage | Doing | Thinking | Feeling | Product response |
|---|---|---|---|---|
| 1. During the missed week | Not running; avoiding the app | "I am falling behind. Every day makes it worse" | The documented guilt spiral [verified, `pain-points.md` section 4] | Silence, mostly: no streak-shame, no "we miss you" pressure. One neutral message mid-week: "Plans bend. When you are back, yours will be ready." Nothing else |
| 2. Day 1 back, opens app | Taps the app expecting a wall of red missed workouts | "How bad is it? Can I still do this race?" | Dread mixed with hope | No red wall. One screen: "Welcome back. One question: what happened?" (sick / too busy / something hurt / just life). One tap, because the answer changes the repair: illness needs a gentler ramp than busyness; pain needs caution flags [inferred from coaching practice in the corpus] |
| 3. The repair proposal | Reads the rebuilt plan | "It did not just delete a week and cram the rest" | Cautious relief | The repair, with reasoning shown: "You lost one week to illness. Cramming it back raises injury risk, so we rebuilt weeks 6 to 12: two easy runs to restart, your long run steps back to week-4 distance and rebuilds, race goal unchanged and still realistic. Here is why." Accept, adjust, or talk it through |
| 4. The comeback run | Taps today's run | "Short and easy. I can do short and easy" | The achievable first step: confidence restart | The workout arrives as a route (the seam where coaching meets the wedge): 3K, flat, soft surface where available, from his door. Set up to be finished, not survived [inferred from FJ8] |
| 5. Completing it | Runs it, finishes comfortably | "I am back. That did not hurt" | Momentum; identity restored ("feel like a real runner" is his core emotional job [verified, `jobs-to-be-done.md` section c]) | Post-run: "Week one of the rebuild done. Two more easy days, then we step back up." Progress framing, zero guilt vocabulary. Share-to-Strava moment ready for the club feed |
| 6. The following weeks | Follows the reshaped plan | "It adapts. I do not have to be perfect for this to work" | Trust in the system: the H7 retention bet [verified as hypothesis mapping, `personas.md`] | Plan continues adapting to what he actually does, not what was scheduled. If he crushes the rebuild, it advances; if he struggles, it eases without comment |

### Moments of truth

1. **The first message after the gap.** Guilt-flavored copy ("you missed 4 workouts!") confirms his fear and churns him; the verified coaching-content consensus is that guilt is the enemy of the return [verified, `pain-points.md` section 4]. Neutral, forward-facing copy is the whole game.
2. **The repair's credibility.** It must visibly avoid both documented failure modes: not cramming (the aggressive end), not capping him at 10-minute runs (the conservative end). Showing the reasoning is what makes the middle believable [verified for the transparency lever, `concept.md` section 4: "the coach explains its reasoning"].
3. **The comeback run's difficulty.** Too hard and it injures the persona the market already injures; too trivial and it insults his ambition. This single run calibration carries the retention of the whole repair [inferred].
4. **Honesty if the race is no longer realistic.** If the gap were four weeks, the app must say so and offer real choices (adjust goal time, switch to a later race, finish-not-PR framing) rather than quietly presiding over a bad race day [inferred from truth-telling standards].

### Failure states and recovery

| Failure | Recovery |
|---|---|
| F1. He tries to cram anyway (manually schedules missed workouts) | The app warns once, honestly and specifically ("adding these three runs to this week triples your load jump; injury risk rises sharply"), then respects his choice. Warn, never block, never nag twice |
| F2. The gap was injury, not illness | "Something hurt" branches to caution: suggests the pain persists check, gates intensity behind pain-free runs, surfaces the see-a-professional line where warranted. No diagnosis, ever [inferred compliance posture] |
| F3. Repeated disruptions (weeks 7 and 9 also break) | The plan re-repairs without escalating drama; after repeated breaks it offers "maintenance mode" (keep fitness, release the race commitment) as a dignified option rather than a failure state |
| F4. Race genuinely out of reach | The honest conversation (moment of truth 4): reset options with reasoning, framed on what he can still own ("finish strong" over "pretend the PB is on") |
| F5. He churns from the paid tier post-race | Expected pattern for the segment [assumption, `personas.md` Jake churn note]. Exit is clean (billing trust as brand [verified, `concept.md` section 6]); the free wedge keeps him running Waypoint routes, and the next race re-opens the coach conversation |

### Success metric

Return-and-repair rate: percent of plan users with a 7-plus-day gap who complete the comeback run within 7 days of returning; supporting: repair-proposal acceptance rate, post-repair injury-signal rate (self-reported pain flags) not exceeding baseline, plan completion rate to race day.

---

## Cross-journey design principles

Distilled from the five journeys; each traces to evidence or a locked concept obligation.

1. **Explain reasoning, always.** Every route and every plan change carries a "why" in concrete, checkable terms. Transparency is the trust lever for AI advice [verified, `concept.md` section 4] and the entire trust mechanism in unfamiliar and safety contexts (journeys 3, 4).
2. **Degrade honestly.** Missing data, weak routes, unsatisfiable constraints, and offline states are stated plainly with the best available alternative. "No good route right now" is a valid answer; pretending is the only unforgivable answer [verified as persona requirement, `personas.md` Elena; generalized].
3. **Never promise "safe".** "Safety-aware" is the ceiling of the claim, everywhere: UI, why-cards, marketing, App Store. Enforceable as a copy-review rule (journey 4) [verified, `concept.md` liability note].
4. **Ask at the moment of value.** No permission, account, or integration is requested before the user can see what it buys them, and every ask is skippable with a functional fallback (journey 1).
5. **Private by default, home never leaks.** Privacy zones from day one, zone-trimmed sharing, a "what others see" preview. One leak is unrecoverable [verified obligation, `concept.md` section 4].
6. **Never nag.** One contextual upsell per trigger, dismissals remembered, no guilt vocabulary, no streak shame, notifications only with a named benefit (journeys 2, 5). Category billing distrust makes pushiness expensive [verified, `gap-analysis.md` unmet need 7].
7. **Speed is trust.** Route in under 30 seconds, onboarding under 3 minutes, travel route before the lobby doubt hardens (journeys 1, 3). The competitor is a 15-minute manual workflow that mostly works [verified, `pain-points.md` section 1]; being slow forfeits the only advantage.
8. **The free path always works.** Paid deepens (training-state awareness, adaptive plans); it never gates the escape hatch or degrades the wedge (journey 2). Basic generation is anchored at zero by the market [verified, `concept.md` section 7].
9. **Feed Strava, never compete with it.** The social payoff is a beautiful post in their feed, not ours (journeys 2, 5) [verified strategy, `gap-analysis.md` section d].
10. **Every run teaches, lightly.** Skipped spurs, avoided streets, mid-run flags, and reroutes become preferences without questionnaires; personalization compounds into switching cost [verified as concept mechanism, `concept.md` section 5].

## Top 5 screens and flows implied for design work

Priority order for Phase 5 design effort; each names the journeys that depend on it.

| # | Screen or flow | What it must do | Journeys served |
|---|---|---|---|
| 1 | **Generate screen** (the home screen) | One-tap generation with visible, adjustable constraint chips (distance, elevation, surface, crossings, safety-aware weighting, new-roads toggle); context-aware defaults (time of day, travel detection, plan state for paid) | All five |
| 2 | **Route reveal with the "why this route" card** | Map plus stats plus concrete reasoning; per-segment explainability; data-confidence and degradation labeling; regenerate and constraint-adjust in place; AI disclosure; bail-out points on long routes | 2, 3, 4 (the trust surface of the product) |
| 3 | **Onboarding and permission flow** | The 3-minute critical path: value screen, 3-chip calibration, location pre-permission explainer, first generation, home privacy zone setup; deferred HealthKit and notification asks with moment-of-value triggers | 1 (and gates everything else) |
| 4 | **In-run navigation surface** (phone plus Apple Watch) | Voice turn-by-turn silent between turns; watch haptics and glance; silent missed-turn recompute; one-tap reroute (busier streets, around blockage, shortcut home); offline continuation from cache | 2, 3, 4 |
| 5 | **Plan repair conversation flow** (paid layer) | Gap detection with neutral copy, one-question triage, repair proposal with visible reasoning, accept-adjust-discuss actions, comeback-run-as-route handoff, honest goal-reset branch | 5 (and the upsell moment in 2) |

Adjacent but lower priority: the post-run summary and Strava share flow (serves 2, 4, 5) and the safety preference sheet (serves 4); both are contained enough to design alongside screens 2 and 4.

## Assumptions

- [assumption] Deferred authentication (no account wall before first route) is acceptable for v1 architecture; needs confirmation in `stack-recommendation.md` and `prd.md`.
- [assumption] Stage-level thinking and feeling entries not tied to a cited source are persona projections; usability sessions and the interview program must validate them, especially Elena's trust thresholds (`personas.md` open question 3).
- [assumption] Numeric targets implied here (30-second generation, 3-minute onboarding, cue timing) are design budgets, not validated thresholds; Phase 6 `metrics.md` owns the targets.
- [assumption] Mid-run safety flags and reroute corrections can be aggregated into the scoring layer in a privacy-compliant way; the aggregation design needs the compliance checklist review before commitment.
- [assumption] The night-before pre-generation prompt (journey 3) is technically feasible with background location change detection under iOS permission constraints; needs technical validation in Phase 5.
- [assumption] Live location sharing with a trusted contact (Elena's third job in `jobs-to-be-done.md`) is NOT in these v1 journeys because the locked execution surface does not include it; this is a scope judgment, flagged for the PRD and possibly a decision record if it becomes contentious.
- [assumption] Jake is modeled as already paying at journey 5 start; the free-user variant of plan disruption (no coach layer) is out of scope here and belongs to the PRD's free-tier definition.

## Open questions

1. Where exactly is the free-paid boundary on the generate screen (which constraint chips are free)? Deferred by design to Phase 6 with the safety-free-tier decision (DEC-006, deferral 5); these journeys assume safety-aware weighting is free-tier per the defensible default flagged in `personas.md`.
2. What evidence threshold makes Elena trust an algorithmic safety-aware route at all? Interview open question; the why-card design should be tested in those interviews (`personas.md` open question 3).
3. Does the upsell moment in journey 2 (workout-constraint duplication) convert better than a post-run moment? Needs experimentation post-launch; both are designed non-nagging.
4. Watch-only running (no phone carried): journeys assume phone present; the watch-only variant stresses caching, generation, and reroute flows and needs a technical feasibility answer before it becomes a journey (`pain-points.md` open question on phone-carry rates).
5. Should the honest refusal (journey 4) offer a lower-weighting regenerate ("loosen safety weighting for more options")? Ethically loaded: offering it respects agency, but the app suggesting she lower safety standards is a bad look. Flag for design review with the interview findings.

## Sources

- Internal (all accessed 2026-07-30): `research/04-synthesis/concept.md` (locked, DEC-006), `research/03-users/personas.md`, `research/03-users/jobs-to-be-done.md`, `research/03-users/pain-points.md`, `research/02-competitors/gap-analysis.md` (via Phase 3 citations), `research/00-RESEARCH-PLAYBOOK.md` (deliverable spec and writing standard).
- All external evidence is cited transitively through the Phase 3 documents above; no new external sources were introduced in this synthesis.
