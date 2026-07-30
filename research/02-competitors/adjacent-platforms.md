# Adjacent Platform Players: Lighter Profiles

Version-Timestamp: 2026-07-30 14:30:00 UTC-4

**Executive summary.** Five platforms sit adjacent to Waypoint's wedge (adaptive, contextual route generation with coaching on top). Strava is the most dangerous: it owns Runna (the leading adaptive training app), ships an AI insight layer (Athlete Intelligence), already markets "personalized routes linked to your training plan" in its bundle, and has locked its API against exactly the kind of AI product Waypoint is building. Garmin monetizes AI through Connect+ but its coaching is watch-locked and its data API is closed to new partners, which limits both its reach and Waypoint's integration options. Apple shipped generative voice motivation (Workout Buddy) in watchOS 26 and keeps HealthKit open, making it more a distribution rail than a route-generation threat near term. Nike Run Club is a free, content-driven marketing channel in maintenance-plus mode with no AI or route ambitions visible. WHOOP has the most advanced consumer AI coach but no screen, no GPS, and no mapping competence, so it threatens the coaching layer, not the route wedge. Net: the wedge is defensible today, but the Strava plus Runna route-and-plan combination is the single scenario to monitor weekly.

## Strava (as platform)

**Snapshot**

- More than 150 million registered users in over 190 countries as of April 2025. [verified] (Strava Press, "Strava to Acquire Runna, A Leading Running Training App", https://press.strava.com/articles/strava-to-acquire-runna-a-leading-running-training-app, accessed 2026-07-30)
- Raised at a $2.2 billion valuation (including debt) in May 2025, led by Sequoia; CEO Michael Martin said the company was on track for $500 million in annual recurring revenue. [verified] (Crunchbase News, "Strava Valuation Powers Up To $2.2B As Fitness Startup Funding Falters", https://news.crunchbase.com/venture/fitness-startup-funding-falters-strava-raise/, accessed 2026-07-30)
- Confidentially filed a draft S-1 in February 2026 for a proposed US IPO. [verified] (Sacra, "Strava revenue, funding & growth rate", https://sacra.com/c/strava/, accessed 2026-07-30)
- Conflicting revenue figures: Business of Apps estimates roughly $415 million for 2025, the CEO's WSJ framing points near $500 million, and The Information reported in January 2026 the number was believed below $500 million. [verified as reported claims] (Curved Trading, "Strava IPO: The Confidential S-1 and the Missing Numbers", https://curvedtrading.com/articles/en/investing/strava-ipo/, accessed 2026-07-30)
- Weighting rationale: treat "$400 to 500 million, closer to the low end" as the working figure. The CEO quote is promotional; The Information's skeptical report is more recent and better sourced for a pre-IPO reality check.
- Paid subscriber counts are not public; third-party estimates run from 1.2 million to roughly 4 million and cannot all be true. [verified as reported claims, same Curved Trading source] Working figure: low single-digit millions (see Assumptions).

**Offer to the committed amateur runner**

- Free: activity tracking, social feed, clubs. Subscription ($11.99/month or $79.99/year US): segments, leaderboards, route building, training analytics, Athlete Intelligence. [verified] (Strava, "Pricing", https://www.strava.com/pricing, accessed 2026-07-30)
- Strava + Runna bundle ($149.99/year US, annual only, launched July 2, 2025) adds Runna's full adaptive training plans and audio coaching. [verified] (Strava Press, "Strava + Runna Launch Combined Subscription Bundle", https://press.strava.com/articles/strava-runna-launch-combined-subscription-bundle, accessed 2026-07-30)

**Route and location intelligence**

- Structural advantage: the global heatmap and more than 10 billion uploaded activities form the best proprietary dataset of where people actually run. [verified activity count] (Runner's World UK, "Strava launches Athlete Intelligence on mobile app", https://www.runnersworld.com/uk/news/a62488273/strava-athlete-intelligence/, accessed 2026-07-30)
- The bundle marketing already promises "personalized routes linked to your training plan". [verified] (bundle press release above)
- Not offered today: real-time route generation adapted to weather, crossings, safety, or surface constraints. [inferred from absence in Strava's published feature descriptions as of 2026-07-30]

**AI coaching as of mid-2026**

- Athlete Intelligence (public beta since October 3, 2024): generative AI post-activity summaries and roughly 30-day trend insights for subscribers, mobile only, visible only to the account owner. [verified] (Strava Press, "Strava's Athlete Intelligence Translates Workout Data into Simple and Personalized Insights", https://press.strava.com/articles/stravas-athlete-intelligence-translates-workout-data-into-simple-and, accessed 2026-07-30; Strava Help Center, "Athlete Intelligence on Strava", https://support.strava.com/en-us/articles/15401629-athlete-intelligence-on-strava, accessed 2026-07-30)
- It is analysis and encouragement, not a plan generator. Plan generation and adaptive coaching live in Runna, kept as a separate app "for the foreseeable future". [verified] (acquisition press release above)

**API and ecosystem posture**

- Publicly "firmly committed" to being the open platform, with 100+ training apps on the API. [verified] (acquisition press release above)
- In practice, the November 2024 API agreement banned third-party display of a user's data to anyone but that user and prohibited AI/ML use of API data. [verified] (Strava Press, "Updates to Strava's API Agreement", https://press.strava.com/articles/updates-to-stravas-api-agreement, accessed 2026-07-30; The Verge, "Strava closes the gates to sharing fitness data with other apps", https://www.theverge.com/2024/11/19/24301056/strava-api-ai-data-sharing-policy-change-fitness-tracking, accessed 2026-07-30)
- The current API policy goes further: Strava's own MCP is the sole authorized agent-mediated interface, third-party MCP servers and aggregators are banned, and AI training, fine-tuning, grounding, embedding, and RAG on Strava data are all prohibited. [verified] (Strava, "API Policy", https://cdn-1.strava.com/legal/api_policy, accessed 2026-07-30)
- Implication for Waypoint: do not build anything load-bearing on the Strava API, and never touch Strava data with the route or coaching models.

**How they could attack the wedge, and likelihood**

- [inferred] The credible kill shot: "generate me a route for today's Runna workout", combining heatmap popularity, segment data, and Runna's plan engine. They have the data, the coaching asset, the distribution, and pre-IPO pressure to ship subscription-driving features.
- [inferred] Likelihood of a meaningful v1 within 18 months: 50 to 60 percent. Likelihood it matches Waypoint's full constraint depth (weather, crossings, safety, surface): 20 to 30 percent, because popularity ranking and constraint solving are different engineering problems.

**What they will probably NOT do, and why**

- [inferred] Real-time environmental adaptation, street-crossing minimization, and safety-scored routing: deep, niche, liability-adjacent problems serving a fraction of a multi-sport base; pre-IPO incentives favor broad engagement over vertical depth.
- [inferred] Reopening the API generously: the direction of travel since November 2024 is consistently toward enclosure.

## Garmin

**Snapshot**

- Fiscal 2025: record consolidated revenue of $7.25 billion (up 15 percent); Fitness segment $2.36 billion (up 33 percent), the strongest segment, expected to lead 2026 growth. [verified] (Garmin Newsroom, "Garmin announces fourth quarter and fiscal year 2025 results", https://www.garmin.com/en-US/newsroom/press-release/corporate/garmin-announces-fourth-quarter-and-fiscal-year-2025-results/, accessed 2026-07-30; The Motley Fool, "Garmin (GRMN) Q4 2025 Earnings Transcript", https://www.fool.com/earnings/call-transcripts/2026/02/18/garmin-grmn-q4-2025-earnings-transcript/, accessed 2026-07-30)
- Connect+ subscriber numbers are not disclosed. [inferred from their absence in the Q4 2025 earnings materials]

**Offer to the committed amateur runner**

- The deepest free training stack for watch owners: Garmin Coach adaptive run plans, training load, readiness, VO2 max, all free with the hardware. [verified that Coach plans and existing features remain free] (Garmin Newsroom, "Elevate your health and fitness goals with Garmin Connect+", https://www.garmin.com/en-US/newsroom/press-release/wearables-health/elevate-your-health-and-fitness-goals-with-garmin-connect/, accessed 2026-07-30)
- Connect+ ($6.99/month or $69.99/year, launched March 27, 2025): Active Intelligence AI insights, performance dashboard, extra Garmin Coach expert content and videos, LiveTrack extras, badges. [verified] (same Garmin press release)
- Added since launch: Trails+ routing, 3D Maps, year-end Rundown, and AI nutrition tracking (January 2026, CES). [verified] (the5krunner, "Garmin Connect Plus review", https://the5krunner.com/2026/04/20/garmin-connect-plus-review/, accessed 2026-07-30)

**Route and location intelligence**

- Static course planning, not contextual generation: Connect+ adds Trails+ and 3D Maps. [verified] (the5krunner review above)
- Garmin watches have long offered on-device round-trip course creation and popularity-based routing (Trendline). [inferred from Garmin product documentation generally; not re-verified against a current manual, flagged in the unverified list]
- No weather, safety, or crossing adaptation appears in any Connect+ or watch feature list reviewed. [inferred from absence]

**AI coaching as of mid-2026**

- Active Intelligence: AI-generated prompts at wake, post-workout, and evening, drawing on sleep, HRV, training load, and stress. [verified] (the5krunner review above)
- Independent verdict is that it is thin: "Active Intelligence continues to restate thin insights" and Connect+ "is still not worth paying for as a general proposition". [verified as reviewer opinion] (the5krunner review above)
- It is a nudge layer, not an adaptive coach. The actual coaching engine (Garmin Coach) predates the AI push and remains free. [verified] (Garmin Connect+ press release above)

**Developer program pause**

- New applications to the Garmin Connect Developer Program (the cloud API for health and activity data) are paused: form removed, no reopening date, no waitlist, per replies from Garmin's program team on its own forums. Existing integrations still work. Connect IQ (on-device apps) remains open. [verified] (Garmin Forums, "Garmin Connect Developer Program - Access Request Rejected Without Notification", https://forums.garmin.com/developer/connect-iq/f/discussion/434542/garmin-connect-developer-program---access-request-rejected-without-notification, accessed 2026-07-30; Momentum, "Garmin Developer Program Paused: Roadmap Impact", https://www.themomentum.ai/blog/garmin-developer-program-closed-roadmap, accessed 2026-07-30)
- Implication for Waypoint: a Garmin data integration cannot be counted on for launch. Plan HealthKit-first ingestion; treat Garmin API access as a later, uncertain unlock.

**Watch coaching lock-in**

- Garmin's coaching value proposition requires owning a Garmin watch; Connect+ features explicitly "vary by device". [verified] (Garmin Connect+ press release above)
- The lock-in is both moat and ceiling: it cannot serve the Apple Watch or phone-only runner Waypoint targets first. [inferred]

**How they could attack the wedge, and likelihood**

- [inferred] Garmin could fold constraint-aware route generation into Connect+ or the watch; it owns mapping DNA from its navigation heritage.
- [inferred] Likelihood of a contextual route generator matching Waypoint's concept within 18 months: 20 to 30 percent. The Connect+ track record (thin AI, incremental features) and a hardware-first org that ships software to sell watches argue against fast, deep movement.

**What they will probably NOT do, and why**

- [inferred] A phone-first iOS coaching experience for non-Garmin owners: it would cannibalize the hardware attach driving the $2.36 billion Fitness segment.
- [inferred] Reopening generous API access soon: the pause is framed as restructuring with no timeline.

## Apple

**Snapshot**

- Apple does not report Fitness+ subscribers or revenue. [inferred from absence in Apple disclosures]
- Fitness+ costs $9.99/month or $79.99/year US, included in Apple One Premier ($37.95/month). [verified] (MacRumors, "The Future of Apple Fitness+ Remains 'Under Review'", https://www.macrumors.com/2026/02/08/apple-fitness-remains-under-review/, accessed 2026-07-30)
- Bloomberg's Mark Gurman reports the future of Fitness+ is "under review", that Apple scaled back plans for a separate AI-powered Health+ subscription, and that he expects Apple to eventually meld Health with Fitness+. [verified as reported by Gurman] (same MacRumors source)

**Offer to the committed amateur runner**

- Apple Watch is arguably the default committed-amateur running device on iOS: pacer workouts, custom structured workouts, and training metrics free in the Workout app. [inferred characterization; feature existence verified in Apple's watchOS materials cited below]
- Fitness+ adds trainer-led video (including treadmill running) and Custom Plans (schedules built from preferred activities, trainers, durations). [verified] (Apple Support, "How to use Apple Fitness+", https://support.apple.com/en-gb/108761, accessed 2026-07-30)
- Content investment continues (new 2026 programs, guest trainers) with no major overhaul and no price increase. [verified] (Yahoo Tech, "Apple Fitness+ is starting 2026 with new programs", https://tech.yahoo.com/ai/apple-intelligence/articles/apple-fitness-starting-2026-programs-140000411.html, accessed 2026-07-30)

**Route and location intelligence**

- None generative. The Workout app tracks routes and offers Pacer; no route generation or suggestion product exists for runners in watchOS 26 or iOS 26. [inferred from absence in Apple's watchOS 26 communications] (Apple Newsroom, "watchOS 26 delivers more personalized ways to stay active and connected", https://www.apple.com/ml/newsroom/2025/06/watchos-26-delivers-more-personalized-ways-to-stay-active-and-connected/, accessed 2026-07-30)

**AI coaching as of mid-2026**

- Workout Buddy (watchOS 26, announced WWDC June 2025): generative spoken motivation using Apple Intelligence, workout history, and live metrics, voiced by a text-to-speech model built from Fitness+ trainer voice data. [verified] (Apple Newsroom watchOS 26 release above)
- Requirements and scope: Apple Intelligence-capable iPhone nearby (iPhone 15 Pro or later), Bluetooth headphones, English only; covers running, walking, cycling, HIIT, strength, and a few others. [verified] (Apple Support, "Use Workout Buddy in Workout on Apple Watch", https://support.apple.com/guide/watch/use-workout-buddy-apd65c7938e6/watchos, accessed 2026-07-30)
- Critically: motivation and milestone commentary, not a plan. It does not prescribe workouts, adapt training, or choose where you run. [verified from feature descriptions, same sources]

**Pricing**

- Watch hardware plus optional Fitness+ at $9.99/month or $79.99/year; Workout Buddy and core running features are free with the hardware. [verified, sources above]

**What Apple is likely to do next, and the attack scenario**

- [inferred] The reported direction (Health+ features folded into the Health app, possible Health and Fitness+ merger, an AI health coach) points at holistic health coaching, not running-specialist training. Expect Workout Buddy to gain languages and light plan awareness before Apple builds adaptive periodized run coaching.
- [inferred] Apple could Sherlock route suggestion at the OS level (Maps has the road graph, Weather has conditions, Watch has fitness data). Likelihood of a true adaptive route generator within 18 months: 10 to 20 percent. Apple builds broad, conservative, privacy-first features for casual users; a constraint-solving route engine for committed runners is the kind of narrow, opinionated product it historically leaves to the App Store.
- [inferred] The bigger near-term Apple risk is soft: Workout Buddy plus free Watch training features raise the bar for what "coaching" must feel like.

**What they will probably NOT do, and why**

- [inferred] Deep adaptive training plans, safety-scored routing (liability exposure), or anything Android.
- [inferred] Closing HealthKit: Apple's incentive is to make the iPhone the health hub that apps like Waypoint build on, which makes Apple the distribution rail, not the enemy.

## Nike Run Club

**Snapshot**

- Free app, no subscription, available in 11 languages in more than 160 countries; active user counts not disclosed. [verified availability; user count absence inferred] (Nike Newsroom, "Nike Run Club App Delivers New Features to Prepare, Support and Empower Runners", https://about.nike.com/en/newsroom/releases/nike-run-club-app-new-features, accessed 2026-07-30)

**Offer to the committed amateur runner**

- Roughly 300 audio guided runs and six structured training plans (getting started through marathon), run tracking, challenges, community. [verified] (Nike Newsroom release above)
- Know-before-you-go local weather and sunrise/sunset tips, plus live location sharing with friends and family. [verified] (same source)
- Syncs to Strava and to Apple, Garmin, and Coros watches. [verified] (same source)

**Route and location intelligence**

- None. Weather tips and location sharing are the extent of location awareness; no route builder, no route suggestion, nothing generative. [verified for the named features; absence of routing [inferred] from app documentation and store listings reviewed 2026-07-30]

**AI coaching as of mid-2026**

- None. Coaching is pre-recorded human audio (Nike coaches, athletes such as Eliud Kipchoge) and static plans; no AI features are present or announced. [inferred from absence across Nike's newsroom and current app store listings as of 2026-07-30]

**Is Nike still investing?**

- Maintenance-plus. The app ships regular releases (iOS version 7.79.2 in late July 2026), but recent changelogs are small quality items: re-running guided runs, an average pace calculation fix. [verified] (Apple App Store, "Nike Run Club: Running Coach", https://apps.apple.com/us/app/nike-run-club-running-coach/id387771637, accessed 2026-07-30; Google Play, https://play.google.com/store/apps/details?id=com.nike.plusgps, accessed 2026-07-30)
- Nike frames the app as "free and distinct digital experiences grounded in coaching and guidance". [verified] (Nike Newsroom release above) In practice it is a brand and retention channel for shoe sales, not a product P&L. [inferred]

**Pricing**

- Free, and its strategic role depends on staying free. [inferred: the app exists to sell shoes and build brand loyalty; paywalling would undercut its purpose]

**How they could attack the wedge, and likelihood**

- [inferred] Very low: 5 to 10 percent within 18 months. An adaptive route engine requires mapping, weather, and safety infrastructure Nike has never shown, and its digital division has been narrowing rather than expanding scope. The realistic move is licensing or partnering rather than building.

**What they will probably NOT do, and why**

- [inferred] Charge for the app, build AI coaching in-house, or enter route intelligence. NRC matters to Waypoint mainly as the free baseline anchoring price expectations for guided-run content, and as proof that audio coaching content alone is a commodity.

## WHOOP

**Snapshot**

- Private company; subscriber and revenue figures not public. [inferred from absence of disclosures]
- Hardware-included subscription, restructured May 2025 with WHOOP 5.0 and WHOOP MG into three annual tiers. [verified] (TrackerVS, "WHOOP Pricing 2026", https://trackervs.com/pricing/whoop-pricing/, accessed 2026-07-30)

**Offer to the committed amateur runner**

- Recovery-side intelligence: strain, recovery, sleep scores, HRV, VO2 max, heart rate zones, and readiness-style guidance on when to push or back off. [verified] (WHOOP, "Membership Options", https://www.whoop.com/us/en/membership/, accessed 2026-07-30)
- A complement to a run tracker, not a replacement: the band is screenless with no in-run pacing display, and no onboard GPS appears in any tier's spec list, so pace and route during runs depend on the phone or paired devices. [inferred: WHOOP publishes no explicit "no GPS" statement in the sources reviewed; based on official spec and membership pages] (same WHOOP membership page)

**Route and location intelligence**

- None, and no mapping assets or ambitions visible anywhere in WHOOP's product communications. [inferred from absence as of 2026-07-30]

**AI coaching as of mid-2026**

- The strongest consumer AI health coach of the five. On May 8, 2026 WHOOP announced My Memory (a user-controllable persistent context layer: goals, lifestyle, health history) and Proactive Check-Ins (unprompted, timely recommendations such as adjusting training around travel or prioritizing sleep before a key event). [verified] (WHOOP Press Center, "WHOOP Expands Health Platform with On-Demand Clinician Access and New AI Features", https://www.whoop.com/us/en/press-center/whoop-expands-health-platform-with-on-demand-clinician-access-and-new-ai-features/, accessed 2026-07-30)
- Same announcement: redesigned voice/text Journal with AI-suggested behaviors, EHR record integration, and upcoming on-demand clinician access. [verified] (same source)
- This is proactive, memory-backed coaching: exactly the interaction pattern Waypoint's coaching layer will be judged against. [inferred]

**Pricing (subscription hardware model)**

- WHOOP One: $199/year, WHOOP 5.0 device, core sleep, strain, and recovery. [verified] (WHOOP membership page above; Wareable, "Whoop 5.0 vs. Whoop MG: Key differences explained", https://www.wareable.com/wearable-tech/whoop-5-vs-whoop-mg-which-membership-explained, accessed 2026-07-30)
- WHOOP Peak: $239/year, adds Healthspan, Health Monitor, Stress Monitor. [verified] (same sources)
- WHOOP Life: $359/year, WHOOP MG hardware with ECG and blood pressure insights. [verified] (same sources)
- Hardware is included in the membership; annual plans include hardware upgrades after 12 months. [verified] (TrackerVS pricing above)

**How they could attack the wedge, and likelihood**

- [inferred] Route generation: 5 percent or less within 18 months. No screen, no GPS, no maps, and a strategic arc pointed at clinical-grade health (ECG, blood pressure, labs, clinicians), not run navigation.
- [inferred] The credible threat is absorption of the coaching layer: WHOOP Coach recommending daily run intent ("easy 40 minutes today") could make a runner feel coached before Waypoint reaches them. Likelihood WHOOP deepens run-specific training guidance: 30 to 40 percent. Even then it lacks the "where to run" answer.

**What they will probably NOT do, and why**

- [inferred] Ship a screen, onboard GPS, or a routing product: the screenless always-on form factor and 14+ day battery are core to the brand, and the R&D roadmap points at healthcare, not navigation.
- [inferred] WHOOP is a positioning benchmark for coaching quality and a potential integration partner, not a wedge competitor.

## Platform risk summary for Waypoint

The three platform moves most capable of killing the route-generation wedge, ranked by danger.

**Risk 1: Strava ships plan-aware route generation (Strava plus Runna convergence).**

- The scenario: "generate today's route for today's Runna workout", built on the heatmap, segment data, and Runna's plan engine, sold inside a $149.99/year bundle to 150M+ registered users. Strava already uses "personalized routes linked to your training plan" language in bundle marketing.
- [inferred] Likelihood within 18 months: 50 to 60 percent for a v1 (popularity-based, plan-linked); 20 to 30 percent for full constraint depth matching Waypoint (weather, crossings, safety, surface).
- Early-warning signals: Runna app teardowns or beta strings mentioning route generation; Strava job postings for routing or graph engineers; S-1 or roadshow language featuring routes as a growth pillar; bundle marketing shifting from "route discovery" to "route creation for your workout".

**Risk 2: Apple builds route suggestion into Workout or Maps at the OS level.**

- The scenario: a free, default, on-device "suggest a run route" using Maps data and fitness history resets iOS user price expectations to zero and commoditizes basic route generation on Waypoint's first platform.
- [inferred] Likelihood within 18 months: 10 to 20 percent. Apple's pattern is broad and shallow; Workout Buddy shipped motivation rather than planning, and Fitness+ itself is under strategic review.
- Early-warning signals: WWDC sessions or APIs touching route suggestion or pedestrian route generation primitives in MapKit; Workout Buddy gaining "plan" vocabulary; Gurman reporting on the Health app AI coach expanding into workout prescription.

**Risk 3: Data enclosure squeezes Waypoint's ingestion and distribution rails.**

- The scenario: Strava's API already bans AI use of its data, and Garmin has paused new data API partners. Further tightening degrades Waypoint's cold-start personalization (importing run history) and social distribution (posting runs to Strava), killing the wedge indirectly by starving personalization and growth.
- [inferred] Likelihood of material further tightening within 18 months: 40 to 50 percent, given the consistent direction of both platforms since November 2024.
- Early-warning signals: Garmin Connect Developer Program reopening with restrictive tiers or fees (monitor developer.garmin.com); further Strava API policy revisions; enforcement actions against coaching apps that survived the 2024 changes. Counter-signal that keeps the iOS-first plan viable: HealthKit remaining open on current terms.

**Standing mitigation for all three:** build the moat in the constraint engine and proprietary context data (safety scoring, crossing graphs, surface data, micro-weather) rather than anything an incumbent's existing dataset trivially replicates, and keep ingestion HealthKit-first so no single platform's API decision is fatal.

## Assumptions

Collected assumptions used above, each tagged [assumption]:

1. [assumption] Strava's paying subscriber base is in the low single-digit millions. Public estimates range from 1.2 million to roughly 4 million and conflict; no authoritative figure exists pre-S-1.
2. [assumption] Runna remains the primary vehicle for Strava's training-plan ambitions through 2027, per Strava's stated "separate apps for the foreseeable future" posture. A sudden merge would accelerate Risk 1.
3. [assumption] Garmin's Connect Developer Program pause is restructuring rather than permanent closure. Garmin has said only "stay tuned"; treat any Waypoint roadmap item requiring Garmin data as blocked until it reopens.
4. [assumption] Apple keeps HealthKit read access open on current terms through the planning horizon. The mitigation strategy leans on this; no signal contradicts it today, but it is Apple's choice, not a guarantee.
5. [assumption] Nike's digital strategy keeps NRC free and content-led; no paid or AI pivot is assumed.
6. [assumption] WHOOP hardware continues without a screen or onboard GPS through the next hardware cycle, keeping it out of in-run navigation.
7. [assumption] The committed amateur runner will pay for at most one or two running subscriptions, so platform bundle pricing (Strava plus Runna at $149.99/year, Connect+ at $69.99/year, Fitness+ at $79.99/year, WHOOP at $199 to $359/year) directly constrains Waypoint's pricing headroom.

**Items that could not be verified as of 2026-07-30:** Strava's true revenue and paid subscriber count (contested, pre-S-1); Garmin Connect+ subscriber numbers (never disclosed); Apple Fitness+ subscriber and revenue figures (never disclosed); NRC active user counts (not disclosed); WHOOP subscriber and revenue figures (private company); the claim that Garmin watches offer on-device round-trip course creation (not re-verified against a current Garmin manual, tagged [inferred] in the Garmin section).
