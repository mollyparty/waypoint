# Go-to-Market Plan

> Version-Timestamp: 2026-08-06 12:20:00 UTC-4

**Executive summary.** Waypoint's year-one go-to-market job is not revenue. It is proof that committed amateur runners adopt a route generator and come back to it, gathered cheaply enough that a solo founder can run the whole program alongside building the product. The plan concentrates on one metro and one segment: the urban committed amateur who runs three to five times a week from a home doorstep, with women runners as the highest-intensity cohort inside that group and monthly travelers as the demo carriers rather than the target. Concentration is not a stylistic preference here; route quality is a function of local pedestrian data density, and the safety layer is built metro by metro (`../05-product/mvp-scope.md`, GD-3), so a thin national launch ships bad routes in most of the country and a bad route is the one failure mode this product cannot survive. Channels rank in this order: physical run clubs, Reddit and running forums, store optimization, founder-led build-in-public content, micro-creators and coaches, press, and last, two channels that look obvious and are wrong for this company at this stage: SEO content (structurally broken by AI Overviews in 2026) and paid acquisition (unaffordable pre-seed against a $2.50 to $5.50 category cost per install with no revenue to pay it back). The launch is deliberately split: iOS at month 9 to 10 is a quiet quality burn-in for the beachhead metro, and the Android date at month 10 to 12 is the real public launch, because the one-shot assets (press, creators, Product Hunt, an Apple featuring nomination) can only be spent once and the top-ranked channel is a physically mixed-platform run club where telling half the room "not yet" kills the word of mouth. The paid layer at months 10 to 12 is the plan's most dangerous moment and gets a full transition protocol: never take anything away, grandfather the free cohort permanently and publicly, and pair the paywall with genuinely new capability rather than newly locked doors.

**Desk research disclaimer.** This plan is built from prior Waypoint research phases plus external channel benchmarks accessed 2026-08-06. No Waypoint user interviews have been conducted, no Waypoint marketing has been run, and every conversion rate, install estimate, and traction milestone below is a planning figure derived from published category benchmarks, not a measurement of this product. External claims carry a source and an access date. Internal claims cite the source document. Confidence tags follow `../00-RESEARCH-PLAYBOOK.md`: `[verified]` traces to a credible source, `[inferred]` is reasoned from verified inputs with the reasoning shown, `[assumption]` is unvalidated working belief and appears in the register at Section 10.

**What is locked and not reopened here.** Positioning is Candidate A, route-first, and the tagline is "Know where to run" ([[DEC-006 Concept lock route-first positioning]]). v1 launches entirely free and safety-aware routing stays free permanently ([[DEC-008 Phase 5 gate MVP approved stack in validation]]). iOS ships month 9 to 10 and Android 4 to 8 weeks later from one React Native codebase ([[DEC-010 Staged cross-platform MVP on React Native]]). The NOT list stands: no social network, no route library, no multi-sport, no plan-quality brand war with Runna (`../04-synthesis/concept.md`, Section 7). This document takes those as given and takes the product to market.

## 0. The capacity and cash budget this plan must fit

Before any channel decision, the honest constraint. The founder is 1.0 FTE inside a 2.5 to 3.0 FTE team and is the product owner, the client engineer, and the routing lead (`../05-product/mvp-scope.md`, Section 7). Go-to-market cannot consume more than a fraction of that without slipping a launch date that already consumes ten of the twelve to eighteen months of competitive window (`../02-competitors/gap-analysis.md`, Section c).

| Period | GTM time budget per week | GTM cash budget per month | Rationale |
|---|---|---|---|
| Months 1 to 3 | 3 to 4 hours | $0 to $100 | Build dominates. GTM is the interview program (which is research, not marketing, but doubles as recruiting) plus a landing page. |
| Months 4 to 6 | 5 to 7 hours | $100 to $250 | Beta community management, run club presence starts, Reddit reputation accrues. |
| Months 7 to 8 | 8 to 10 hours | $200 to $400 | Store assets, press list, creator outreach, nomination filings. |
| Launch window (months 9 to 13) | 15 to 25 hours | $400 to $800 | Two launch moments, review triage, community response. Product work slows deliberately for roughly six weeks total. |
| Post-funding | Re-plan | Re-plan | Every channel labeled "needs budget or headcount" below unlocks here, not before. |

Every recommendation in Section 3 is filtered through this table. A channel that cannot be run inside these numbers is labeled as such and sequenced after funding, per the brief. [inferred, from the team model in `../05-product/mvp-scope.md` Section 7 and the pre-seed constraint in `../../vault/01-Project/Founder-Brief.md`]

## 1. The beachhead

### 1.1 The segment: narrower than "committed amateur"

Phase 3 recommends the committed amateur as the primary segment and the ambitious beginner as secondary (`../03-users/segmentation.md`, Section 7). That is the right monetization target but it is not yet a beachhead, because "committed amateur" is roughly 13 million people in the US alone and contains at least three different acquisition problems.

**The beachhead is the urban committed amateur who runs from a home doorstep three to five times a week in a single metro, with women runners as the highest-intensity cohort inside that group.**

The argument, from the research rather than asserted:

1. **The retention evidence points at home, not at travel.** Phase 3's H1 reframe is explicit: travel friction is the activation moment and demo story, while safety-aware routing and home novelty carry daily retention, because those two recur three to five times per week for exactly this segment while travel is episodic (`../03-users/unmet-needs.md`, Section b). A beachhead is chosen for retention, not for demo quality. Choosing travelers as the beachhead would optimize the launch for the weaker retention evidence. [inferred]
2. **The two strongest-evidenced needs in the entire corpus are both local.** Safety-aware routing ranks first on evidence and route novelty at home ranks second (`../03-users/unmet-needs.md`, Section a). Both are satisfied by data about one place. Travel is satisfied only by data about everywhere.
3. **Women are the sharpest-need cohort and the most reachable one.** 92 percent of women runners report safety concerns, 69 percent take specific precautions, and 54 percent have changed routes over safety, while zero of fifteen-plus examined products accept safety as a routing input (`../03-users/personas.md`, Elena; `../02-competitors/gap-analysis.md`, unmet need 2). Women are also 53 percent of US race participants (`../03-users/segmentation.md`, Section 3.3) and run crews are repeatedly cited as providing women safety and camaraderie (`../01-market/industry-trends.md`, Section 5), which means the highest-intensity need concentrates in exactly the physical venue that ranks first in the channel plan. This is a rare alignment and the plan should exploit it. The constraint is that it must be exploited without fear-based framing or a safety promise (Section 2.5). [inferred]
4. **Who the beachhead is not.** Not Priya the traveler (episodic, and unserveable at high quality from a single-metro data build; she remains the demo). Not Jake the ambitious beginner (secondary segment, gentler calibration, and his primary job is injury-safe progression, which is coaching-layer work deferred to v2+). Not casual runners (zero-price anchor). Not serious racers (already coached). These exclusions are inherited from `../03-users/segmentation.md`, Section 7.

### 1.2 The geography: one marketing metro, two to three data metros

Route quality is not uniform across space. Waypoint's differentiating constraints depend on OpenStreetMap pedestrian features (footways, crossings, surface, lighting) whose completeness varies enormously by city and depends on volunteer effort. OpenStreetMap US reports that across the top ten US cities contributors added 9,896 km of footways and 62,153 crossings in 2024, its largest recorded pedestrian mapping increase, and explicitly notes that crossings are "particularly difficult and time consuming to map" and often require local knowledge, while singling out Seattle as having "some of the highest quality data in the US" thanks to a multiyear effort by the Taskar Center for Accessible Technology [verified] (Source: OpenStreetMap US, "Walking the Path to Progress: Pedestrian Data Trends in American Cities", https://openstreetmap.us/news/2025/03/pedestrian-data-trends/, accessed 2026-08-06). The community formalized a four-tier quality schema (bronze, silver, gold, diamond) in March 2026 precisely because coverage is uneven enough to need one [verified] (Source: OpenStreetMap US, "Introducing the PWG Sidewalk Mapping Schema 1.0", https://openstreetmap.us/news/2026/03/pwg-schema-release/, accessed 2026-08-06).

That fact drives the entire geographic strategy: **the product is globally functional but only locally excellent, so the marketing must be locally concentrated even though the app is not geofenced.**

Concretely, three tiers of coverage:

| Tier | What works | Where |
|---|---|---|
| Global (anywhere OSM has a road graph) | Distance, round-trip generation, elevation, novelty against personal history, voice guidance | Everywhere the app installs. This is what makes travel mode possible at launch. |
| Data metros (2 to 3, per GD-3) | The above plus the lighting and populated-path safety layer at full depth | The beachhead metro plus one or two contrast metros |
| Beachhead metro (1) | The above plus founder ground truth: routes personally run, run clubs personally attended, beta testers personally known | One metro, all the human effort |

**Metro selection rule, in priority order.** [inferred]

1. **The founder's home metro is the beachhead unless it fails the data floor.** This is not sentiment. The founder must personally run generated routes to catch the failure mode that kills this product (a route that sends someone somewhere bad), must show up at run clubs weekly, and must recruit twenty to fifty TestFlight runners face to face by month 4 (`../05-product/mvp-scope.md`, assumption list). None of that is remote work.
2. **The data floor**: the month-1 A3 spike (GD-3) must confirm the metro reaches at least the silver tier of the PWG schema for footways and crossings and has usable `highway=street_lamp` or `lit=*` density. If the home metro fails, the beachhead moves to the nearest metro that passes and the founder commits to two days per month there, which is a real cost the plan should name rather than hide.
3. **The contrast metros are chosen to be harder, on purpose.** Pick one metro with known-strong pedestrian data (Seattle is the documented example above) and one sprawlier metro with weaker but fast-improving data (Austin, Phoenix, Dallas, and Miami each grew footway edits over 50 percent in 2024 per the OSM US source). The point is to learn the shape of degradation before the product is national, not to serve those markets.
4. **English-language, iOS-plus-Android metro, per the locked sequence** (`../04-synthesis/concept.md`, Section 6: iOS English-first, then Android and more geographies).

**Named shortlist if the founder is geographically free** [inferred, not a substitute for the spike]: Seattle first on documented pedestrian data quality plus dark wet winters that make the lighting constraint salient plus hills that make the elevation constraint felt; Boston second on runner density, compactness, and marathon culture; New York third because crossing minimization is most valuable there (the Manhattan crossing complaint in `../03-users/pain-points.md` is the sharpest expression of FJ10) but the press and creator noise floor is highest and the founder's time is most expensive there; London fourth as the UK is geography two and parkrun plus the record 1,133,813-application 2026 marathon ballot show the density (`../01-market/industry-trends.md`, Section 5), but it splits the founder across an ocean.

### 1.3 Why concentrating beats spreading

Four reasons, in descending strength:

1. **Bad routes are unrecoverable and only local presence catches them.** The competitive opening exists partly because Strava's generator has produced documented dangerous outputs with no flagging mechanism, including "12 miles of very unsafe roads that were single lane, no shoulder, busy with traffic" (`../02-competitors/gap-analysis.md`, unmet need 2). Waypoint's entire differentiation claim is that it does not do that. A product that repeats the incumbent's most-cited failure has no story left. The only cheap defense at pre-seed scale is a founder who has run the routes.
2. **The safety data layer is built per metro and is the riskiest technical assumption in the plan.** GD-3 explicitly scopes the spike to "2 to 3 launch metros" and names A3 (open-data buildability at solo scale) as the single riskiest technical assumption (`../05-product/mvp-scope.md`, GD-3). Marketing wider than the data build markets a promise the engine cannot keep.
3. **The top-ranked channel is physical and therefore geographic.** Run clubs are the fastest-growing social structure in the sport (Section 3.1) and they meet at a specific corner at a specific time. Word of mouth in running propagates through Tuesday night group runs, not through impressions.
4. **Concentration is how a solo founder gets a real signal.** Two hundred engaged runners in one metro produce interpretable retention data, comparable route-quality complaints, and a recruitable interview pool. Two hundred runners scattered across forty metros produce noise and forty different data-quality confounds. [inferred]

**The honest tension.** The demo story is travel, and travel is by definition not local. The resolution is the coverage tiering above: travel mode ships globally at launch on the distance, elevation, and novelty constraints, and degrades honestly (H-09, honest degradation messaging, is in MVP v1) when the deep safety layer has no data for a location. Marketing may show the hotel-lobby demo; marketing may not imply that the safety layer is everywhere. That distinction has to be enforced in copy, and it is the second most likely place this plan gets the company in trouble after the safety-promise line itself. [inferred]

## 2. Positioning to message translation

### 2.1 The one-liner and the ladder

| Surface | Copy |
|---|---|
| Tagline (locked) | Know where to run. |
| One-liner | Waypoint generates the right route for today's run, from wherever you are standing, sized to your distance and aware of light, weather, and street crossings. |
| One-breath version (for a run club, out loud) | It is a running app that tells you where to run, not just how far. You say five miles, it hands you a five-mile loop from your door that it picked on purpose. |
| Investor version | Every training app prescribes the workout without knowing where you are standing; every route app draws lines without knowing what your body needs. Waypoint owns the seam. |

The one-breath version matters more than it looks. The founder will say it forty times before launch and every run club conversation is a fifteen-second window. It deliberately avoids the words "AI", "safety", and "personalized", all of which either trigger skepticism or trigger liability. [inferred]

### 2.2 App Store and Play Store listing angle

Store search is a primary discovery surface and the listing is the highest-leverage free asset the company owns. Health and Fitness page-view-to-install conversion benchmarks disagree across vendors, which is itself the finding: SplitMetrics puts the category median at 18.52 percent and AppTweak's panel at 30.8 percent, both measuring page-view-to-install, a spread of about 1.5x driven by panel composition and redownload handling [verified] (Source: AppScreenshotStudio, "Good App Store Conversion Rate: 4% to 32% by Category", https://appscreenshotstudio.com/blog/good-app-store-conversion-rate-benchmarks-2026, accessed 2026-08-06; Adapty, "App Store conversion rate benchmarks", https://adapty.io/blog/app-store-conversion-rate/, accessed 2026-08-06). The operational conclusion is to ignore published charts and read the peer benchmark inside App Store Connect, which since the March 2026 update shows 25th, 50th, and 75th percentile values for your own category, business model, and download-volume tier [verified] (Source: AppScreenshotStudio, same, accessed 2026-08-06). Target: at or above the 50th percentile of the peer group; two consecutive weeks below the 25th means the listing is the problem, not the market.

**Draft metadata (to be A/B tested, not shipped as gospel).**

| Field | Draft | Note |
|---|---|---|
| App Store name (30) | `Waypoint: Running Routes` | Brand plus the category noun people search |
| App Store subtitle (30) | `Know where to run today` | The locked tagline plus the temporal hook |
| Keyword field (100) | `run route,route planner,running routes,route generator,jog,loop,run map,marathon,travel run` | Draft only; run a keyword pass in month 7 |
| Play title (30) | `Waypoint: Running Routes` | Parity |
| Play short description (80) | `Know where to run. Routes made for today's run, from wherever you're standing.` | |
| Promotional text (170, updatable without review) | Reserved for the launch moment and later for the "founding runner" paid-layer message. This field changes without a review cycle and should be treated as the only fast-moving copy on the page. | |

**The three screenshots that matter.** Health and Fitness has the widest conversion variance of any category, and the first three screenshots are the highest-leverage assets, with pages that resolve the user's specific intent outperforming generic lifestyle imagery [verified] (Source: Strataigize, "What Actually Improves App Store Conversion Rates in 2026", https://www.strataigize.com/blog/app-store-conversion-rate-optimization, accessed 2026-08-06). Waypoint's three:

1. **The generation moment.** A phone showing a distance input and a generated loop on a map, captioned "Say 5 miles. Get a 5 mile loop from right here." This resolves the intent in one frame.
2. **The reason.** The same route annotated with why it was chosen (lit streets, fewer crossings, a park segment), captioned "It tells you why it picked this one." This is the differentiation frame and the trust frame in one.
3. **The travel frame.** A hotel pin with a route leaving it, captioned "Works from any front door, including one you have never seen." This is the demo story and it belongs in slot three, not slot one, because slot one must serve the beachhead's daily job.

Custom Product Pages are underused (only 31 percent of apps use them) and deliver conversion lifts up to 8.6 percent [verified] (Source: Adapty, "App Store conversion rate benchmarks", https://adapty.io/blog/app-store-conversion-rate/, accessed 2026-08-06). Runna's own growth playbook used race-specific Custom Product Pages and long-tail landing pages [verified as reported] (Source: Phil Carter summarizing Runna Director of Growth Miranda Paine, LinkedIn, https://www.linkedin.com/posts/philgcarter_yesterday-runna-director-of-growth-miranda-activity-7369036572668674049-TQxy, accessed 2026-08-06). Waypoint's equivalents: one CPP per beachhead metro leading with a recognizable local landmark route, and one CPP for the travel angle used in any press or creator link. Build two at launch, not ten.

### 2.3 The three proof points

Every claim below traces to Phase 2 or Phase 3 evidence and none of them requires a competitor to be named unfavorably.

1. **"It is the only running app that treats light, weather, crossings, and surface as inputs, not decoration."** Across fifteen-plus products examined, zero accept weather, crossings, or safety as routing constraints (`../02-competitors/gap-analysis.md`, Section b, H2 verdict). This is the H2 claim and it is the strongest sentence the company owns.
2. **"It knows the roads you have already run, and it can send you somewhere else."** Route novelty at home is the second-strongest evidenced need, proven commercially by a 90,000-user paying street-completion movement, and the incumbent generator ranks by popularity, which is the exact opposite behavior (`../03-users/unmet-needs.md`, need 2; `../02-competitors/gap-analysis.md`, unmet need 6).
3. **"It tells you why it chose this route, and it tells you when it cannot find a good one."** Honest degradation (H-09) is in MVP v1 and the explanation layer follows in v1.x (`../05-product/mvp-scope.md`, Sections 2 and 3). This is a differentiator precisely because the category's AI trust bar is high and unforgiving: research on conversational fitness coaches finds trust collapses quickly on errors or generic advice (`../01-market/industry-trends.md`, Section 2). A product that says "I could not find one" is making a credibility deposit.

### 2.4 Objection handles

These are written to be said out loud, in a run club car park, in under twenty seconds each.

**"Why not just use Strava heatmaps?"**
> Heatmaps show you where other people ran. That is a great answer to "what is popular here" and a bad answer to "what should I run today." Strava ranks by popularity, so two different runners standing on the same corner get the same routes, and popularity has no opinion about whether a street is lit at 6 a.m. or has a crossing every hundred meters. We start from your distance, your history, and the conditions right now. Also, we post to Strava. We are not asking you to leave it.

Grounding: the popularity ranking and the "two different runners at the same corner" quote are from `../02-competitors/profile-strava-routes.md` via `../02-competitors/gap-analysis.md`, unmet need 1. The closing sentence is mandatory, not optional, and Section 2.6 explains why.

**"How is this different from Runna?"**
> Runna tells you the workout. It is very good at that. It cannot tell you where to run it, because its only route capability is importing routes you already made. We are the other half. If you love Runna, keep it. We will put the tempo run somewhere flat and uninterrupted, and both apps will post to Strava.

Grounding: Runna's route capability is import-and-follow of Strava routes only (`../02-competitors/positioning-map.md`, map 1). The "keep it" framing is a deliberate refusal of the plan-quality brand war ruled out by the NOT list (`../04-synthesis/concept.md`, Section 7). It is also strategically correct: Runna is owned by Strava, and a founder-level fight with the category leader is unwinnable on brand and distribution grounds (`../02-competitors/gap-analysis.md`, Section d).

**"Is it safe to let an app route me somewhere I do not know?"**
> Fair question, and the honest answer is that no app can promise you a safe run, including this one. What we do is take the things you would check yourself if you had time, whether the street is lit, whether there are people around at this hour, how many crossings you will hit, and use them to choose. We show you the route before you start, we tell you why we picked it, and when the constraints you asked for cannot be met, we say so instead of handing you something anyway.

Grounding: this is the only permitted register for the safety question and it follows the anti-positioning rule in `../04-synthesis/positioning.md`, Section 6. Note what it does: it concedes the limit first, which is what makes the rest credible, and it never uses the word "safe" as an adjective attached to a route.

### 2.5 The safety copy rule, marketing edition

The product rule is "safety-aware, never safe" (`../04-synthesis/positioning.md`, Section 6). The marketing version is stricter, because marketing copy is repeated by people who did not read the rule.

**Rule S, binding on all outbound copy including store metadata, ads, press quotes, creator briefs, and anything the founder says on a podcast:**

1. Describe **inputs**, never **outcomes**. Waypoint considers lighting; Waypoint does not deliver safety.
2. Never use "safe", "safer", or "safest" as a modifier of a route, a street, an area, or a run.
3. Never imply crime data, personal-security guarantees, or protection. Waypoint deliberately does not use crime data at MVP for ethics, comparability, and framing reasons (`../05-product/stack-recommendation.md`), and copy must not imply otherwise.
4. Never use fear-based framing. No statistics about assault in an ad, no "do not run alone" imagery, no implied threat. The Elena persona work rules this out on brand ethics (`../03-users/personas.md`, Elena).
5. Always pair a safety-adjacent claim with the honest limit in the same asset, not in a footnote.
6. Legal review of every safety-adjacent asset before it ships, per the Phase 4 requirement.
7. Creator and ambassador contracts carry Rule S as a written deliverable requirement with a review-before-publish clause. **This is the highest-risk leak in the whole plan**: the sentence that creates liability is most likely one the founder never wrote, said cheerfully by a creator who was trying to be helpful. [inferred]

| Fails | Passes |
|---|---|
| "Waypoint finds you safe routes." | "Waypoint routes around unlit streets when you ask it to." |
| "Run safe, anywhere." | "Know where to run, at 6 a.m. in a city you have never seen." |
| "The safest way to run at night." | "Built for dark mornings: lighting and populated paths are routing inputs, not filters you apply afterwards." |
| "Never run somewhere dangerous again." | "When nothing meets your constraints, it tells you that instead of guessing." |
| "Our AI keeps you safe." | "Our routing takes light, crossings, and time of day into account before it picks a street." |
| "92 percent of women fear for their safety. We fixed it." | "Most running apps treat lighting as a map layer. We treat it as a routing input." |
| "Safety-first routing." | "Safety-aware routing." (the exact locked phrase, and the ceiling) |

The right-hand column is also better marketing, which is worth saying plainly: specific mechanism beats vague promise in a category where the audience has been burned by overclaiming AI features (`../01-market/industry-trends.md`, Section 2).

### 2.6 The Strava rule, marketing edition

Strava is a partner at the product level and must be a partner at the message level. Three binding rules: [inferred, from `../02-competitors/gap-analysis.md` Section d and `../04-synthesis/positioning.md` Section 6]

1. **Never position against Strava as a company.** Counter-position against a specific behavior (popularity ranking) when a user asks, never in outbound copy, never in a headline, never in a press quote.
2. **Always volunteer the integration.** "It posts to Strava" is said in the first thirty seconds of every conversation. It removes the switching objection, which is the single biggest one, and it signals that Waypoint knows its place in the stack.
3. **Acknowledge the window internally, never externally.** The 12 to 18 month estimate before Strava plausibly ships plan-linked route generation is a planning clock for the founder and the investor deck (`../02-competitors/gap-analysis.md`, Section c). It is never a marketing message. "Before the giant crushes us" is not a value proposition and it tells the giant where to look.

## 3. Channel strategy, ranked

### 3.1 The ranking

Assessed on four axes: cash cost, plausible return at Waypoint's scale, time to work, and whether one person can run it alongside building the product.

| Rank | Channel | Cash cost | Plausible return (year 1) | Time to work | Solo-runnable? | Verdict |
|---|---|---|---|---|---|---|
| 1 | Run clubs and in-person running community | Near zero (travel, coffee, maybe race entry) | 100 to 400 high-intent installs in one metro, plus the beta cohort, plus interview subjects, plus the only real word-of-mouth engine | 2 to 4 months to become a known face | Yes, and only if solo. This channel is destroyed by delegation | **Primary.** Start month 2. |
| 2 | Reddit and running forums | Zero | 50 to 300 beta testers pre-launch; a durable feedback loop; occasional launch spikes | 4 to 8 weeks of reputation before any mention | Yes, 2 to 3 hours per week | **Primary.** Start month 1 with zero promotion. |
| 3 | Store optimization (App Store and Play) | Zero to $200 for screenshot tooling | The compounding baseline for every other channel; roughly 70 percent of app discovery is search | Weeks to index, months to rank | Yes | **Mandatory infrastructure**, not a growth channel. |
| 4 | Founder-led content and build-in-public | Zero | 500 to 3,000 waitlist signups if it works, zero if it does not; asymmetric | 3 to 6 months | Yes, 2 hours per week | **Primary, cheap lottery ticket.** |
| 5 | Micro-creators and coaches | $0 gifted, $300 to $3,000 per paid post | Unpredictable pre-launch; the strongest post-launch lever once there is a product to show | 1 to 3 months per relationship | Partly. Paid programs need budget and coordination | **Secondary.** Gifted only until launch; paid after funding. |
| 6 | PR and press | Zero to $0 (do it yourself) | One launch cycle of coverage; a credibility artifact for investors; few installs | Weeks, and it is one shot | Yes, but it is a week of work | **One-shot asset.** Spend it on the Android public launch. |
| 7 | Content and SEO | Zero cash, high time | Structurally impaired in 2026; see 3.7 | 9 to 18 months | Technically yes, but the payback window is past the plan horizon | **Deprioritize.** A popular channel that is a bad fit here. |
| 8 | Paid acquisition | $2.50 to $5.50 per install and up | Negative until there is revenue | Days | Yes mechanically, no financially | **Do not run pre-funding.** Post-funding only, and even then behind retention proof. |

Two channels are deliberately called bad fits. The reasoning is in 3.7 and 3.8, and both deserve the argument rather than the dismissal.

### 3.2 Run clubs and in-person community (rank 1)

**Why it ranks first.** Run club growth is the strongest structural trend in the sport right now. New clubs on Strava nearly quadrupled in 2025 to one million total, running clubs specifically grew 3.5x, and club-organized events rose 1.5x year over year [verified] (Source: Strava, "Strava Releases 12th Annual Year in Sport Trend Report", https://press.strava.com/articles/strava-releases-12th-annual-year-in-sport-trend-report-2025, 2025-12-03, accessed 2026-08-06). Participation in running clubs grew 59 percent globally over two years, making group running the fastest-growing social activity on a platform of more than 100 million athletes [verified] (Source: Running Industry Association, "By The Numbers: Run Club Expansion", https://runningindustry.org/resources/research/by-the-numbers-run-club-expansion, published 2026-03-19, accessed 2026-08-06). Mid-2026 data shows new run club creation tripling year over year, with run clubs now 39 percent of all Strava groups [verified] (Source: Australasian Leisure Management, "Strava data shows global surge in running clubs", https://www.ausleisure.com.au/news/strava-data-shows-global-surge-in-running-clubs-as-social-fitness-reshapes-running-culture, accessed 2026-08-06).

Three properties make this channel uniquely right for Waypoint specifically, not just for running apps generally: [inferred]

- **It is where the beachhead physically is**, at a known time, weekly, in the launch metro.
- **It solves the demo problem.** Waypoint's value is invisible in a screenshot and obvious in ninety seconds of standing next to someone while the app produces a loop from where you are both standing. This is a channel where the product can be demonstrated, not described.
- **Run clubs have a real, recurring, unmet route problem.** Somebody has to decide the route every week. That person is a group leader who is currently drawing routes by hand. Waypoint solves a job the club organizer has, not just a job the individual runner has, which makes the organizer a natural advocate without any incentive scheme. This is an inference, not a documented finding, and it is worth testing in the first three club visits. [inferred, flagged as A6]

**Runna precedent.** Runna built a program of 550-plus ambassadors who build online running communities and engage runners in real life on race days [verified as reported] (Source: Phil Carter summarizing Runna's Director of Growth, LinkedIn, https://www.linkedin.com/posts/philgcarter_yesterday-runna-director-of-growth-miranda-activity-7369036572668674049-TQxy, accessed 2026-08-06; Everflow, "The Runna App Ambassador Program Case Study", https://www.everflow.io/post/the-runna-app-ambassador-program-case-study, accessed 2026-08-06). Waypoint cannot run 550 ambassadors at 2.5 FTE. It can run six, in one metro, personally.

**First concrete step (do this in month 2, week 1):** open Strava club search filtered to the beachhead metro, list every running club with a recurring weekly meetup and more than thirty members, sort by proximity, pick three, and attend one run per week for four consecutive weeks **without mentioning the product at all**. Introduce as a runner building something, only when asked. The fifth week is when the demo happens, and only to individuals who asked. The four-week no-pitch rule is the whole trick: these are communities, and a founder who arrives pitching is a vendor forever.

**Adjacent physical venues, in priority order:** run specialty stores (they host clubs, they need content for their own club nights, and they have a commercial interest in local runners), parkrun events on Saturday mornings where available (18.2 million global finishes in 2025 per `../03-users/segmentation.md`, but note parkrun is protective of its volunteer culture and commercial approaches must go through official channels), and one local half marathon expo in months 8 to 12 as a beta-recruitment table rather than a booth.

**What this channel cannot do:** scale beyond one metro at solo capacity, produce installs faster than roughly ten to forty per club per month once active, or produce a launch spike. It is a compounding trickle with the highest quality per install in the plan.

### 3.3 Reddit and running forums (rank 2)

**The rule that matters.** Reddit retired the formal 9:1 self-promotion guideline years ago and there is no site-wide policy; every subreddit enforces its own rules, and the operative principle is that promotion survives only where the account has a genuine contribution history, typically two to four weeks minimum [verified] (Source: ScreenFast, "Reddit Promotion for Indie iOS Apps: The Honest 2026 Playbook", https://screenfast.app/blog/reddit-promotion-indie-ios-app, accessed 2026-08-06; RedditGrowthDB, "Reddit Self-Promotion Rules 2026", https://www.redditgrowthdb.com/guides/reddit-self-promotion-rules, accessed 2026-08-06). Large general subreddits ban direct promotion outright; beta-testing subreddits exist precisely for recruitment and are the most promotion-friendly pre-launch venues, with one source reporting beta recruitment driving over 1,000 installs in a few days as a best case rather than a benchmark [verified] (Source: ScreenFast, same, accessed 2026-08-06).

**Runna precedent again, and it is instructive.** Runna's founders engaged deeply and often on Reddit, run their own subreddit at roughly 14,000 members, and treat it as a daily candid feedback channel where the upvote system reveals which requests have consensus [verified as reported] (Source: Bunce, "3 ways Runna went from idea to acquisition", https://readbunce.com/p/runna-acquired, accessed 2026-08-06). The lesson is not "post about your app on Reddit". It is "Reddit is a product research instrument that occasionally produces users".

**How Waypoint should use it, in order:**

1. **Months 1 to 3, pure participation.** One account, real name attached, flair identifying as a developer where the subreddit requires disclosure. Answer "where should I run in [city]" questions in r/running, r/RunNYC-class city subreddits, and r/AdvancedRunning with genuinely useful local answers and no links. This is also free Phase 3 validation: the questions people actually ask are the copy for the store listing.
2. **Month 4 onward, beta recruitment in the venues built for it.** r/AlphaAndBetaUsers, r/BetaTestersNeeded, r/TestFlight and equivalents, clearly labeled. This is the cheapest path to the twenty to fifty TestFlight runners the walking skeleton needs (`../05-product/mvp-scope.md`, Section 6), and it de-risks the assumption that the founder's network plus run clubs can supply them.
3. **Never**: cross-posting the same launch text to five subreddits, a new account, a link with no context, or any post in r/running that reads as an ad. Each of those is a documented removal cause and a permanent reputation cost in the one online venue where the beachhead concentrates.
4. **Verify before every post.** Subreddit rules change; check the live sidebar each time. Modmail the moderators of the two most important running subreddits in month 6 and ask directly what is permitted at launch. Asking permission is free and moderators remember it.

**Other forums worth the time:** LetsRun (decades of "where do I run in X" threads per `../03-users/pain-points.md`, older and more skeptical audience), Slowtwitch, and the Garmin and Apple Watch community forums where the mid-run navigation rage documented in `../03-users/pain-points.md` Section 6 lives. That last one is underrated: people complaining that "I literally just want my phone to stop talking" are describing a job Waypoint's voice guidance is built for.

**First concrete step (month 1, week 1):** create the account, set the flair, and answer three "where should I run" questions per week in the beachhead metro's subreddit. Track nothing. The asset being built is post history.

### 3.4 Store optimization (rank 3)

Treat this as infrastructure, not a channel. The mechanics and benchmarks are in Section 2.2. Three additional operational points:

**Featuring nominations are free, underused, and have long lead times.** Apple's Featuring Nominations form in App Store Connect is the only formal channel to the editorial team, available to Account Holder, Admin, App Manager, and Marketing roles, with three types (App Launch, App Enhancements, New Content). Apple asks for a minimum of two weeks notice and recommends up to three months in advance for wider consideration; practitioner guidance treats three weeks as the floor and three months as the ceiling, notes the editorial team plans collections eight to twelve weeks ahead, and reports the criteria as user experience, UI design, innovation, uniqueness, accessibility, localization, and product page quality [verified] (Source: Apple Developer, "Getting Featured on the App Store", https://developer.apple.com/app-store/getting-featured/, accessed 2026-08-06; Apple, "Nominate your app for featuring", https://developer.apple.com/help/app-store-connect/manage-featuring-nominations/nominate-your-app-for-featuring/, accessed 2026-08-06; AppScreenshotStudio, "App Store Featuring Nominations: Apple's 7 Scoring Criteria", https://appscreenshotstudio.com/blog/get-featured-on-the-app-store-2026-nominations-guide, accessed 2026-08-06). Editorial reportedly favors a strong human story and adoption of recent Apple frameworks [verified as practitioner analysis] (Source: SEM Nexus, "App Store Featured Placements: How Teams Get Picked", https://semnexus.com/app-store-featured-placements-how-teams-get-picked, accessed 2026-08-06).

Waypoint has an unusually good nomination story and should file two: one App Launch nomination for the iOS date and one App Enhancements nomination for the Android public launch. The pitch writes itself and every element is true: a solo founder, an accessibility-adjacent problem (pedestrian infrastructure data, honest degradation, a product designed around who the map forgets), on-device Apple Foundation Models for explanation generation (`../01-market/industry-trends.md`, Section 4.2), and HealthKit and WorkoutKit integration. Adopting a named recent Apple framework and saying so explicitly is cheap points.

**Rating floor.** Practitioner guidance puts the informal featuring threshold at 4.5 stars and notes a 4.0-plus rating is the general trust threshold [verified as practitioner analysis] (Source: ASOMobile, "App Store and Google Play Featuring 2026", https://asomobile.net/en/blog/app-store-and-google-play-featuring-2026-how-to-get-into-editorial-collections/, accessed 2026-08-06; Adapty, "App Store conversion rate benchmarks", accessed 2026-08-06). This is a direct argument for the quiet iOS launch in Section 5: ratings collected from a small, well-supported cohort are far more likely to sit above 4.5 than ratings collected from a cold launch spike.

**First concrete step (month 7):** open Featuring Nominations in App Store Connect, read the form, and draft the App Launch nomination three months before the iOS date even though the app is not finished. The draft forces clarity about what is notable, which is also the press pitch and the store description.

### 3.5 Founder-led content and build-in-public (rank 4)

**The case.** Runna's founders describe starting with "no distribution channels" and "knowing nothing about marketing", and the first lever was an outcome that felt safe to recommend runner to runner rather than paid spend; the team also treated employees as storytellers documenting their own running journeys rather than buying celebrity endorsement [verified as reported] (Source: Growthcurve, "The exact marketing strategy behind Runna app's growth", https://growthcurve.co/runna-and-strava-the-growth-playbook-when-product-distribution-and-localisation-collide, accessed 2026-08-06; Niall Ratcliffe, LinkedIn analysis, https://www.linkedin.com/posts/niall-ratcliffe_everyone-has-been-talking-about-runna-getting-activity-7322884960254595072-lHuu, accessed 2026-08-06).

**The Waypoint version, which is unusually strong material.** The build has a genuine narrative: a runner building the tool he could not find, working on a problem (pedestrian data, lighting, crossings) that is visibly hard and visibly under-mapped, publishing honest failures. Two content veins that cost almost nothing because the work is happening anyway:

- **Route teardowns.** "Here is the route Waypoint generated this morning, here is what it got right, here is what it got wrong, here is why." Weekly, with a map image. This is simultaneously QA, content, credibility, and the honest-degradation brand in practice.
- **The data problem.** "Here is what OpenStreetMap knows about crossings in [metro] and here is what it does not." This has a second audience: the OSM mapping community, which is small, motivated, and potentially a contributor pool. Approach that community as a participant, never as an extraction target.

**Where to publish:** one owned surface (the waitlist site's changelog), plus wherever the founder already has a presence. Do not start four social accounts. A dormant TikTok is worse than no TikTok.

**Honest expectation:** this is a lottery ticket with a cheap ticket price. It either compounds into a few thousand waitlist signups or it produces nothing but a portfolio of evidence for investors and creators. Both outcomes justify two hours a week; neither justifies ten. [inferred]

**First concrete step (month 2):** ship a one-page waitlist site with a single email capture. Median waitlist landing pages convert about 11 percent of visitors versus a 6.6 percent all-industry landing page median, with well-built pre-launch pages hitting 8 to 20 percent on cold traffic [verified] (Source: Waitlister, "7 Waitlist & Product Launch Statistics", https://waitlister.me/growth-hub/blog/waitlist-and-product-launch-statistics, accessed 2026-08-06; ASO Agency, "App Pre-Launch Marketing: The 2026 Playbook", https://asoagency.io/blogs/pre-launch-app-marketing-strategy, accessed 2026-08-06). One value proposition, one screenshot or animated mockup, one field. Send the welcome email immediately; welcome emails average the highest engagement of any email type, and click rate rather than open rate is the metric to trust post Apple Mail Privacy Protection [verified] (Source: Waitlister, same, accessed 2026-08-06).

### 3.6 Micro-creators and running coaches (rank 5)

**Costs.** Micro creators (10,000 to 100,000 followers) charge roughly $150 to $1,500 for an Instagram feed post, $250 to $2,800 for a Reel, and $600 to $8,000 for a YouTube integration in health and wellness, with fitness-category rates often running above general benchmarks and certified professionals commanding 20 to 40 percent premiums [verified] (Source: InfluencerFee, "Health & Wellness Influencer Rates", https://influencerfee.com/blog/health-wellness-influencer-rates/, accessed 2026-08-06; InfluencerFee, "Fitness Influencer Rates 2026", https://influencerfee.com/blog/fitness-influencer-rates-2025/, accessed 2026-08-06; AMT, "How Much Do Influencers Charge in 2026?", https://amt.ai/blog/how-much-do-influencers-charge, accessed 2026-08-06). Nano creators (1,000 to 10,000) run $15 to $400 per post in the same datasets.

**The arithmetic that kills paid creator work pre-funding.** A single $1,000 micro-creator Reel would need to produce roughly 200 to 400 installs to match the category paid cost per install (Section 3.8), against a product with zero revenue to pay it back. Creator spend is a post-funding channel. [inferred]

**The unpaid version that works now.** Three moves, all free:

1. **Coaches, not influencers.** Local running coaches in the beachhead metro have a real problem Waypoint solves (they prescribe workouts to athletes in neighborhoods they do not know) and an audience of exactly the target segment. Offer free lifetime access and ask for nothing. Five coaches is a plausible target for months 6 to 9.
2. **Gifted early access with no deliverable.** Give twenty relevant micro-creators TestFlight access in month 7 with an explicit "no obligation to post" note. Some fraction post anyway, and the ones who do are the ones whose audience actually cares. The Runna lesson is that long creator arcs following a real journey beat one paid inauthentic post [verified as reported] (Source: Niall Ratcliffe, LinkedIn, accessed 2026-08-06).
3. **Rule S in writing** on every creator relationship, paid or gifted, per Section 2.5 item 7.

**Post-funding version:** a small ambassador program (target six to twenty, not 550) with tracked links, modeled on the Runna structure but sized to the company. Sequenced after the seed, labeled as requiring budget and coordination capacity the founder does not currently have.

### 3.7 Content and SEO (rank 7): a popular channel that is a bad fit here

This is the recommendation most likely to be argued with, so here is the argument.

**The channel is structurally impaired in 2026.** A randomized field experiment with 1,065 desktop Chrome users, published April 2026 and revised June 2026, found that when a Google AI Overview appears it reduces outbound organic clicks by 39.8 percent and increases zero-click searches by 34.5 percent, with AI Overviews triggering on approximately 41 percent of observed queries [verified] (Source: Agarwal and Sen, "The Impact of Google AI Overviews on Publisher Traffic and User Experience: Evidence from a Field Experiment", https://www.tse-fr.eu/sites/default/files/TSE/documents/sem2026/eco_platforms/agarwal_google_search_aio.pdf, accessed 2026-08-06). Ahrefs' December 2025 update found a 58 percent lower average click-through rate for the top-ranking page when an AI Overview is present [verified] (Source: Ahrefs, "Update: AI Overviews Reduce Clicks by 58%", https://ahrefs.com/blog/ai-overviews-reduce-clicks-update/, accessed 2026-08-06). SparkToro's clickstream analysis found US Google searches ended without a click 68.01 percent of the time in the first four months of 2026, up from 60.45 percent in 2024 [verified] (Source: Search Engine Land, "Google zero-click searches reach 68% in early 2026", https://searchengineland.com/google-zero-click-searches-2026-study-479717, accessed 2026-08-06). The two causal and correlational estimates disagree in magnitude (39.8 percent versus 58 percent); the field experiment is methodologically stronger and the correlational study is larger, and both point the same direction, which is all the decision needs.

**Why the impairment lands hardest on exactly Waypoint's content.** "Best running routes in [city]", "how to find running routes when traveling", "is it safe to run at night" are informational, evergreen queries, which is the content type the research identifies as hardest hit. These are also queries an AI Overview answers completely without a click.

**Why the payback window does not fit.** SEO in a competitive consumer category takes nine to eighteen months to produce meaningful traffic. Waypoint's entire pre-launch runway is nine months and its competitive window is twelve to eighteen (`../02-competitors/gap-analysis.md`, Section c). Content started in month 1 begins paying in month 12 to 18, into a search environment that is degrading year over year.

**What survives.** Two narrow uses, both cheap: (a) a small number of pages that exist to be *cited inside* AI answers and to convert the few clicks that remain, meaning genuinely distinctive material like the route teardowns and the pedestrian-data analysis rather than commodity listicles; (b) branded search defense, so that "Waypoint running app" resolves correctly. Budget: two hours a week that is already allocated to Section 3.5, not a separate program.

**Verdict:** do not build a content and SEO program. Revisit at seed with a specialist, when the payback window is affordable.

### 3.8 Paid acquisition (rank 8): do not run it pre-funding

**The numbers.** Apple Search Ads median cost per install for Health and Fitness in the US benchmarks at $3.83, against a $1.80 median across all categories, with cost per tap at $1.59 [verified] (Source: AppTweak, "Apple Ads benchmarks", https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks, accessed 2026-08-06). Practitioner ranges put Health and Fitness at $2.50 to $5.50 and note that category discovery keywords in competitive fitness verticals can run $4.00 to $15.00 cost per install, while branded defense keywords run $0.80 to $3.00 [verified] (Source: LaunchShots, "Apple Search Ads ROI 2026: The Indie Developer Guide", https://launchshots.app/blog/apple-search-ads-roi-2026, accessed 2026-08-06; Admiral Media, "Mobile App Marketing Benchmarks 2026", https://admiral.media/mobile-app-marketing-benchmarks-2026/, accessed 2026-08-06).

**Why it is wrong for Waypoint in year one, in one sentence:** the product has no paid tier until months 10 to 12 by decision (DEC-008), so every dollar spent on installs before then buys a user with a lifetime value of exactly zero dollars, and the plan's stated job for year one is retention evidence rather than volume.

**The counter-argument, considered honestly.** Paid installs would inflate the traction number in an investor conversation. That is real, and it is a bad trade: bought installs from cold keywords retain worse than community installs, they contaminate the week-4 retention signal that GD-1 explicitly protects, and an investor who discovers the number is bought discounts everything else in the deck. Retention on a small organic base is a better artifact than volume on a paid one. [inferred]

**When it unlocks, and in what order.** After the seed and after the paid layer has real conversion data: (1) branded defense first, because it is cheap and competitors bid on your name; (2) a small Apple Search Ads category-discovery test in the beachhead metro only, geo-targeted, with Custom Product Pages per keyword theme; (3) Meta and TikTok only with creative volume the company cannot currently produce. Runna scaled performance marketing from $40,000 to $4 million per month across Meta, TikTok, and Google [verified as reported] (Source: Phil Carter summarizing Runna's Director of Growth, LinkedIn, accessed 2026-08-06). That is what this channel looks like when it works, and it is a description of a company with a marketing team.

### 3.9 Product Hunt, assessed separately

Not a channel, a one-day credibility event. Realistic 2026 expectations: top three of the day pulls roughly 5,000 to 15,000 visitors, top ten pulls 1,000 to 3,000, and outside the top ten expect under 500; consumer products on a successful launch land 500 to 1,500 signups, and the median across a surveyed set of top-6 finishers was about 115 seven-day signups, with the spread driven almost entirely by the audience each founder brought rather than by the platform [verified] (Source: Causo Hub, "Product Hunt traffic 2026: real numbers by daily rank", https://hub.causo.ai/guides/product-hunt-traffic-data-2026, accessed 2026-08-06; Happy Support, "Product Hunt Launch Data: 5 Founders, 8 Questions", https://happysupport.ai/blog/product-hunt-launch-roundup-2026, accessed 2026-08-06). For iOS apps specifically the audience is desktop-heavy and the click to App Store to download path adds friction, so it drives web clicks far more reliably than installs, and the hunter advantage is gone (self-hunt) [verified] (Source: ScreenFast, "How to Launch an iOS App on Product Hunt (2026 Playbook)", https://screenfast.app/blog/how-to-launch-ios-app-product-hunt, accessed 2026-08-06).

**Decision:** launch on Product Hunt once, on the Android public launch date, self-hunted, with the waitlist mobilized in the first two hours. Expect web traffic, a badge, an indexed page, and inbound from operators. Do not expect installs, and do not build the launch plan around it.

## 4. Pre-launch: months 1 to 9

The goal of this phase is not a big list. It is **earning the right to launch to someone**: fifty people who will install on day one because they know the founder, three hundred who will install because they have been reading, and a metro where the word "Waypoint" has been said out loud at a Tuesday night run.

### 4.1 The month-by-month plan

| Month | GTM actions (concrete) | Product context (from `../05-product/mvp-scope.md`) |
|---|---|---|
| 1 | Reddit account created, flair set, three helpful answers per week, zero promotion. Interview recruitment begins (Priority 1 and 2 studies). Play organization account paperwork starts (DEC-010 long-lead item; see 5.4). Waitlist domain and copy drafted. | A3 spike; build starts |
| 2 | Waitlist page live (single email capture). Run club shortlist built from Strava club search; first club attended. Route teardown content begins, weekly. | Spike verdict lands, gating GD-3 |
| 3 | Four run club visits completed, still no pitch. Priority 1 interviews running (8 to 12 committed amateurs, at least 4 monthly travelers). Priority 2 safety interviews scheduled with a specialist moderator. | Walking skeleton nearing TestFlight |
| 4 | **TestFlight cohort assembled: 20 to 50 runners.** Sources in priority order: interview participants who opted in, run club contacts, beta-testing subreddits, founder network. Private Discord or group chat opened for the cohort. Interview findings reviewed at the scope checkpoint. | Walking skeleton on TestFlight; interview checkpoint |
| 5 | Weekly TestFlight build cadence with a written changelog to the cohort. First route-quality bug bounty ("send me a route that was wrong, I will buy you a coffee"). Second and third run clubs added. | Feature build continues |
| 6 | Cohort grows to 80 to 150 via beta subreddits and club referrals. Modmail the two key running subreddits about launch-post rules. Local coach outreach begins (target 5). Press list built (30 to 50 named contacts, not outlets). | Watch app build starts during beta |
| 7 | Store assets produced: icon, three screenshots, two Custom Product Pages, preview video decision (A/B test it; video can reduce conversion in this category). **Apple App Launch featuring nomination filed** (three months before the iOS date). Twenty micro-creators gifted TestFlight access, no obligation. | Feature-complete beta |
| 8 | Waitlist push: the beta cohort gets referral links, the content vein gets its best three pieces, coaches share with athletes. Press pitches drafted but not sent. Play Console store listing prepared; Health Connect and fine-location declarations filed and confirmed. Dry-run the App Store submission with a TestFlight external build to shake out metadata rejections. | Launch prep, QA hardening |
| 9 | iOS submission (Tuesday morning; see 5.2). Quiet iOS launch executes. Android certification begins. | iOS launch month 9 to 10 |

### 4.2 The TestFlight cohort: the most important asset built pre-launch

Twenty to fifty target-segment runners by month 4 is stated as an assumption in the MVP scope, not a plan (`../05-product/mvp-scope.md`, assumption list). Here is the plan that discharges it, with redundancy because a single-source recruitment plan is how this assumption fails:

| Source | Realistic yield | Cost | Notes |
|---|---|---|---|
| Priority 1 and 2 interview participants | 8 to 15 | Zero (already being recruited) | Highest quality; they have already told you their problem |
| Run clubs (3 clubs, months 2 to 4) | 10 to 25 | Zero | Requires the four-week no-pitch investment first |
| Beta-testing subreddits | 15 to 60 | Zero | Lower quality and lower retention; screen for target segment |
| Founder network | 5 to 15 | Zero | Fastest, least representative; use to fill, not to found |
| Local running coach athlete lists | 5 to 20 | Zero | Only if coach outreach lands by month 6 |

**Cohort management rules** that determine whether the cohort is worth having: a weekly build with a written changelog (the single highest-value habit, because it proves the feedback goes somewhere), a named channel where the founder answers personally, an explicit ask each week ("this week, please generate one route in a neighborhood you do not know"), and a route-quality reporting path with one tap. The cohort is simultaneously the QA function, the retention pilot, the launch-day install base, the review source (see 5.2), and the interview pool. Under-investing here is the most expensive available mistake. [inferred]

### 4.3 The interview backlog runs in parallel and doubles as acquisition

`../03-users/unmet-needs.md` Section c specifies roughly 20 to 30 conversations across five prioritized studies plus one screener survey, and GD-4 confirms these run in parallel with the build rather than gating it. Two GTM notes:

- **Every interview ends with an opt-in ask.** "Would you like to try it when there is something to try?" Interview subjects who say yes are the highest-intent pre-launch asset in the company.
- **The Priority 2 safety study is not a marketing exercise and must not become one.** It answers what evidence earns trust and how safety can be communicated without fear-based framing (`../03-users/unmet-needs.md`, Section c, Priority 2). Its output governs Section 2.5, and it should be moderated by a specialist as the research recommends. Do not recruit for it from the beta cohort, because the sample must include women who would not install this app.
- **The screener survey (n of 100 or more) doubles as top-of-funnel.** It resolves the Apple Watch versus Garmin split gating GD-2, and it can carry a waitlist opt-in at the end.

### 4.4 Realistic waitlist target

Working the funnel backwards with published benchmarks: at an 11 percent median landing-page conversion, a waitlist of 1,500 to 3,000 requires roughly 14,000 to 27,000 page visits across eight months, which is roughly 1,700 to 3,400 visits per month from Reddit participation, content, run clubs, coach shares, and beta subreddits combined. That is achievable but not trivial, and it is the number to watch monthly [inferred, from the 11 percent median in the Waitlister source above]. Waitlist to install conversion of 30 to 50 percent for well-nurtured lists is the commonly cited planning range [verified as practitioner guidance] (Source: TheViralApp, "App Launch Strategy 2026", https://theviralapp.com/blog/app-launch-strategy-2026/, accessed 2026-08-06). Applied honestly, a 2,000-person waitlist is 600 to 1,000 launch installs, not 2,000, and roughly half of any consumer waitlist never opens the first email [verified as vendor observation] (Source: LemonPage AI, "Waitlist Conversion Benchmarks by Industry (2026 Report)", https://lemonpage.ai/blog/waitlist-conversion-benchmarks-by-industry, accessed 2026-08-06).

## 5. Launch sequence

### 5.1 The decision: which date is the real launch

DEC-010 gives two launch moments: iOS at month 9 to 10 and Android 4 to 8 weeks later at month 10 to 12. The plan must pick which one carries the one-shot assets, because press, Product Hunt, the creator wave, and the coordinated waitlist email can each be spent exactly once.

**Recommendation: the Android date is the real public launch. The iOS date is a deliberately quiet quality burn-in.**

Reasoning, strongest first: [inferred]

1. **The top-ranked channel is platform-mixed and physical.** A run club in the US splits roughly 60/40 iOS to Android (StatCounter June 2026 via `../05-product/dual-platform-strategy.md`: US iOS 59.8 percent, UK 51.3 percent). Standing in a group of thirty runners and telling twelve of them "not yet" wastes the demo and, worse, wastes the moment, because they will not be assembled again with the same attention. Word of mouth in a physical community does not queue politely for four to eight weeks.
2. **One-shot assets should fire at maximum addressable audience.** Press coverage, a Product Hunt page, and a creator wave all decay fast and cannot be repeated. Firing them at a product half the audience cannot install halves their value permanently.
3. **The quiet iOS period produces the two things that make the real launch work:** a rating above the 4.5 featuring threshold, gathered from a small supported cohort rather than a cold spike, and four to eight weeks of real-world route-quality data in the beachhead metro. Launching loud with an unproven routing engine is the highest-variance choice available, and the failure mode (a viral complaint about a bad route) is precisely the incumbent's documented wound.
4. **The paid layer lands at months 10 to 12, immediately after.** Maximum free base at the moment the paywall arrives is the wrong goal if that base is untrusting, but it is the right goal if the base arrived through a launch that was credible. Sequencing the public launch just before the paid moment concentrates both into one well-managed period rather than three.

**The cost of this choice, stated plainly.** The iOS cohort gets a quieter arrival and some early iOS users will notice the Android launch got the fanfare. Mitigation: the iOS cohort is explicitly told they are first and gets the founding-runner status that later underwrites the paywall transition (Section 7). And the dependency risk is real: if Android slips, the public launch slips with it.

**Hard rule against that risk:** if Android certification is not complete by **month 13**, the public launch fires on iOS alone within two weeks and Android gets a smaller second moment. The launch narrative does not wait indefinitely on a platform. Set this rule now, in writing, so it is not renegotiated under pressure in month 12.

### 5.2 The iOS moment, week by week

Target: month 9 to 10. Objective: prove the engine on real streets, collect 4.5-plus ratings, break nothing.

| Week | Actions |
|---|---|
| iOS minus 12 (month 7) | Featuring nomination filed. Store assets finalized. Metadata dry run via an external TestFlight build to surface privacy-string and metadata problems before the real submission. |
| iOS minus 4 | Beta cohort told the launch date and asked for one thing: install on day one and leave an honest review in week one. Do not ask for five stars; ask for honest. Prepare the in-app review prompt to fire only after a successfully completed generated run, never on first open. |
| iOS minus 2 | **Submit.** Submit Tuesday morning. New app submissions in 2026 typically take 2 to 5 days with spikes of 7-plus during peak periods, driven by a reported 60 percent year-over-year jump in submission volume; Apple maintains it reviews 90 percent of submissions within 48 hours, and both statements can be true because the tail is what hurts. Roughly 25 to 30 percent of first-time submissions are rejected and each rejection restarts the clock. Tuesday submissions show the shortest average wait, Friday and Saturday the longest, and September and December are the worst months for new apps [verified] (Source: LaunchShots, "App Store Review Process 2026", https://launchshots.app/blog/app-store-review-process-2026, accessed 2026-08-06; AppStoreReview, "App Store Review Queue Delays in 2026", https://appstorereview.app/guides/app-store-review-queue-delays-2026, accessed 2026-08-06; ExtensionBooster, "Apple App Store Review Time 2026", https://extensionbooster.net/blog/260601-apple-app-store-review-time-2026-how-long-speed-up-guide/, accessed 2026-08-06; Apple statement reported in Business Insider, "Developers Warn Flood of Vibe-Coded Apps Could Slow Apple Approvals", https://www.businessinsider.com/developers-warn-flood-vibe-coded-apps-could-slow-apple-approvals-2026-3, accessed 2026-08-06). **Plan a two-week review buffer, not a two-day one.** |
| iOS week 0 | Release manually (not automatically on approval) so the date is chosen. Email the waitlist a plain, honest note: iOS first, Android in weeks, here is what works and what does not yet. No press, no Product Hunt, no creator push. Post once in the beta subreddits where the cohort was recruited, as a thank-you and a status update. |
| iOS weeks 1 to 2 | Daily review monitoring and personal response to every review. Route-quality triage as the top priority above all feature work. Crash-free rate and first-generation success rate watched hourly for the first 48 hours. |
| iOS weeks 2 to 4 | Run club demos escalate now that there is a real App Store link. Coaches activated. First measurement of week-4 retention on the launch cohort, which is the GD-1 gate input for the paid layer. |
| iOS weeks 4 to 8 | Android certification and closed testing run in parallel. iOS point releases fix what the first cohort found. Featuring nomination for the Android moment (App Enhancements type) filed at the start of this period. |

**Review risks specific to Waypoint, worth planning around** [inferred, from the product's own architecture in `../05-product/mvp-scope.md` and `../04-synthesis/concept.md` Section 4]:

- **Background location.** Continuous location for run tracking and turn-by-turn draws scrutiny. The purpose strings must be specific and the reviewer notes must explain the running use case in one paragraph. This is the single most likely rejection cause for this app.
- **HealthKit.** Read and write justification must match what the app actually does; unused Health permissions are a common rejection.
- **Health-adjacent claims in metadata.** Any store text that implies safety, injury prevention, or medical benefit invites both rejection and liability. Rule S applies to the store listing verbatim.
- **AI disclosure.** EU AI Act Article 50 transparency is a day-one obligation (`../04-synthesis/concept.md`, Section 4, effective 2026-08-02). Disclose the AI in onboarding and describe it in the listing.
- **Account and sign-in.** Sign in with Apple parity requirements if any third-party sign-in ships.
- **Do not submit in September or December**, per the seasonal guidance above. Month 9 to 10 should be checked against the calendar for this.

### 5.3 The Android moment, week by week (the public launch)

Target: month 10 to 12, four to eight weeks after iOS. Objective: the one real launch.

| Week | Actions |
|---|---|
| Launch minus 6 | Press pitches sent to the 30 to 50 named contacts built in month 6. Angle: the solo founder building pedestrian-aware routing, not "new running app launches". Offer an exclusive first look to two outlets, not all of them. Creator wave briefed (Rule S clauses signed). Product Hunt page drafted. |
| Launch minus 4 | Play Store listing final. Confirm Health Connect and fine-location declarations cleared (Health Connect review carries roughly two weeks of lead time per DEC-010). Confirm production access status (see 5.4). Second featuring nomination filed if not already. |
| Launch minus 2 | Waitlist warmed with a dated announcement. Beta cohort briefed on launch day and asked to be present, not to upvote. Run club leaders in the beachhead metro given a heads-up and a route to use for that week's group run. |
| Launch minus 1 | Android submission. Google Play review is generally faster than App Store review but is not instant; treat it as a week, and never submit and announce on the same day. |
| **Launch day (Tuesday or Wednesday)** | Product Hunt goes live 12:01 a.m. Pacific, self-hunted, with a strong maker first comment. Waitlist email at 8 a.m. local. Reddit posts only where rules permit and only in the venues where reputation was built. Press embargo lifts. Creators post. Both store listings updated with the promotional text. |
| Launch week 1 | Review response daily on both stores. Crash triage on Android specifically, where background GPS survival against OEM battery management is the known hardening problem (DEC-010 risk). Watch the Android route-quality reports separately from iOS; the engine is shared but the device population is not. |
| Launch weeks 2 to 4 | The follow-up curve matters more than the spike; a flat post-launch line indicates no real demand. Keep the community channels warm, ship a visible point release in week 2, and publish the first "what we learned in the first thousand runs" post. |

### 5.4 Store listing lead times and the Android paperwork trap

Collected in one place because these are the items that quietly slip a launch:

| Item | Lead time | Owner action |
|---|---|---|
| Apple featuring nomination | 3 weeks minimum, 3 months recommended; editorial plans 8 to 12 weeks out | File in month 7 for iOS, at iOS launch+2 weeks for Android |
| App Store review, new app | 2 to 5 days typical, 7-plus in peaks; 25 to 30 percent first-submission rejection; each rejection restarts | Submit 2 weeks before the intended date, Tuesday morning |
| Play organization account and D-U-N-S | Up to 30 days for D-U-N-S, plus up to 5 days payment verification | Start month 1 (already flagged in DEC-010) |
| Play closed-testing requirement | 12 testers opted in for 14 continuous days, **for personal accounts created after 2023-11-13 only**; organization accounts are scoped out | Confirm the account is an organization account. If it is personal, the 14-day clock is a hard dependency and must start by launch minus 4 weeks |
| Health Connect declaration | Roughly 2 weeks review (DEC-010) | File month 1 to 2, confirm cleared by launch minus 4 |
| Fine-location declaration (Play) | Filed with the listing; can trigger follow-up questions | File with the listing, budget a round trip |

The Play closed-testing rule is worth stating precisely because it is widely misreported: Google requires personal developer accounts created after November 13, 2023 to run a closed test with at least 12 testers opted in for the last 14 continuous days before applying for production access; organization accounts are outside the policy's scope, though Google states the scoping rather than affirming the exemption in a single sentence, so it should be confirmed in the console rather than assumed [verified] (Source: Google Play Console Help, "App testing requirements for new personal developer accounts", https://support.google.com/googleplay/android-developer/answer/14151465, accessed 2026-08-06; Choicely, "The Google Play 12-Tester Rule, Explained (2026)", https://www.choicely.com/blog/google-play-12-tester-rule, accessed 2026-08-06). Waypoint's plan already calls for an organization account (DEC-010), and the beta cohort easily exceeds 12 testers regardless, so this is a confirm-and-move-on item rather than a risk. Confirm it in month 2 anyway.

## 6. Post-launch growth loops

The NOT list removes the obvious loop. Waypoint will never have a feed, a follower graph, or in-app social discovery (`../04-synthesis/concept.md`, Section 7), which means the standard consumer growth engine is unavailable by design. What remains are five structural loops, assessed honestly. None of them produces a viral coefficient above 1. The realistic goal is a leaky but compounding set of loops that lowers effective acquisition cost, not a growth flywheel. [inferred]

### 6.1 The Strava share loop, assessed honestly

**The mechanism.** Every completed run posts to Strava (TS-07, in MVP v1). The activity carries a route map thumbnail, a title, a description, and a device or app attribution field. Strava's API exposes `device_name` on the detailed activity representation, and Strava explicitly encourages displaying attribution identifying the recording source [verified] (Source: Strava, Activities V3 API reference, https://strava.github.io/api/v3/activities/, accessed 2026-08-06; Strava Developers reference, https://developers.strava.com/docs/reference/, accessed 2026-08-06).

**The honest assessment.** This loop mostly buys goodwill and credibility, with discovery as a weak secondary effect. Three reasons: [inferred]

1. **Attribution is technically present but perceptually buried.** A viewer of a Strava activity is looking at a friend's run, not at a source-attribution field. The proportion of viewers who notice the recording app, let alone act on it, is small.
2. **The visible artifact is a map, not a product.** Ironically, this is the loop's real strength and it has nothing to do with attribution: an unusual, interesting, obviously-not-the-usual-loop route shape in a friend's feed is a conversation starter in a way that a pace number is not. The trigger is not "what app is that", it is "where is that, I have never run there". The response happens in the comments and in person, and it is untrackable.
3. **Strava's posture caps what can be built here.** Strava's API bans AI use of its data (`../02-competitors/adjacent-platforms.md`), so there is no path to a deeper integration and no reason to expect Strava to help this loop along. Waypoint gets what a well-behaved third-party gets.

**What to do about it, concretely.** Make the shared artifact worth looking at: the auto-generated activity title and description should be genuinely interesting and never spammy (a route name and a fact about the route beats "Generated by Waypoint"), and the route shape and novelty are the product's own asset. Add a first-party share card for the runner to post wherever they want, with a link. Instrument it: a unique referral parameter on any link Waypoint controls, so the loop's real contribution is measured rather than assumed. Target for measurement, not for hope: if Strava-attributed installs exceed 5 percent of new installs by month 3 post-launch, the loop is real and worth investing in; below 2 percent, treat it as goodwill and stop optimizing it. [inferred, benchmark set as a decision threshold rather than a prediction]

**One thing to never do:** make the Strava post more promotional to improve the loop. That trades the partner relationship and the user's dignity for a rounding error, and users punish it.

### 6.2 The other four loops

| Loop | Mechanism | Honest strength | First step |
|---|---|---|---|
| **Route-to-a-human share** | A runner sends a specific generated route to a friend or a club leader for tonight's group run. Recipient opens a link, sees the route, needs the app to run it hands-free | Moderate and underrated. It is a utility share with a real reason to exist, and it does not require a social graph. This is the closest thing to a native loop that survives the NOT list | Ship a shareable route link in v1.x. Requires a lightweight web route view, which is small |
| **Trusted-contact share** | Before a run, send the planned route to someone. This is a genuine safety-adjacent behavior women runners already perform manually (live location sharing is a documented precaution, `../03-users/personas.md`, Elena) | Moderate on utility, high on trust, low on discovery. Note it overlaps X-03 (live location sharing), which is deferred with a "do not rebuild trusted incumbents" caveat. The route-preview share is not the same thing as live tracking and is much cheaper | Validate in the Priority 2 safety interviews before building anything |
| **Ambassador and referral** | Structured advocacy with tracked links. Runna's precedent is 550-plus ambassadors and a referral program with a reward on both sides | Proven in this exact category, but it is an operations job. Six ambassadors is the right size for this company, not 550 | Post-launch, month 12-plus, after the paid layer gives referrals something to reward |
| **Store ranking flywheel** | Installs plus ratings plus retention improve category rank, which produces more organic installs | Real, slow, and entirely dependent on the other loops feeding it. Also the reason the quiet iOS launch matters: rating quality compounds | Already covered by Section 3.4 |

### 6.3 The loop that does not exist and should not be faked

There is no content loop, no UGC loop, and no leaderboard loop, because each of those is a social network wearing a costume and the NOT list exists for a reason (`../02-competitors/gap-analysis.md`, Section d: Strava's 195M-user graph is the deepest moat in the category). A solo founder who builds a half-hearted social layer gets the maintenance cost of a community product and none of the network effect. Hold the line.

## 7. The paid-layer moment, months 10 to 12

### 7.1 Why this is the plan's most dangerous moment

The base will have had everything free by decision (DEC-008), the category has a documented record of billing rage (Joggo renewal traps, Runna double-charging with 21 days of support silence, Komoot's paywall expansion triggering public exit posts, per `../02-competitors/gap-analysis.md`, unmet need 7), and clean transparent billing was explicitly identified as a differentiator in this market rather than mere hygiene. Waypoint's brand strategy names trust as a pillar (`../04-synthesis/concept.md`, Section 6). A botched paywall does not just cost conversion; it converts the company's differentiator into a punchline in the exact Reddit threads where its reputation was built.

### 7.2 The seven rules

**Rule 1: Never take anything away. The paywall gates only capability that did not exist before.** The paid layer ships as TS-08 plus P-01 together: the paywall and training-state-aware generation arrive in the same release (`../05-product/mvp-scope.md`, Section 3). Everything in v1, including safety-aware routing (permanently free by DEC-008), core generation, novelty, voice guidance, and Strava share, stays free for everyone forever. This is not just ethics; Apple's guidelines prohibit restricting access to something a user already purchased, and the reputational version of that rule is stricter than the legal one [verified for the Apple rule] (Source: AppsOps, "Migrating an iOS app from paid upfront to subscription", https://appsops.store/blog/ios-paid-to-subscription-model-migration, accessed 2026-08-06).

**Rule 2: Name the permanent free tier publicly at launch, before anyone has paid anything.** In the launch announcement, in the store description, and on the site: "Route generation, safety-aware routing, novelty, and voice guidance are free and will stay free. When we add a paid tier, it will be for new capability on top." Promising this before you need it is what makes it credible when you deliver it. Promising it at the paywall announcement reads as damage control. [inferred]

**Rule 3: Grandfather the pre-paywall cohort explicitly, permanently, and by name.** Everyone who used the app before the paywall date keeps their entire feature set forever and is labeled a founding runner in-app. Identify the cohort technically via original purchase or first-launch date through StoreKit 2 entitlements and the RevenueCat layer already in the stack [verified for the mechanism] (Source: AppsOps, same, accessed 2026-08-06). Give founding runners a permanent discount on the paid tier through a promotional offer, which Apple's system supports for cohort targeting without making the offer public.

**Rule 4: 30 days notice minimum, delivered in-app and by email, not by surprise.** Practitioner consensus is 30 days minimum, with 45 to 60 days preferred for annual commitments, and in-app messaging outperforming email because billing subject lines have low open rates [verified] (Source: AppsOps, "Apple grandfathering rules for subscription price changes", https://appsops.store/blog/apple-subscription-price-grandfathering, accessed 2026-08-06; Userpilot, "Price Increase Announcement: How to Do It Right in 2026", https://userpilot.com/blog/price-increase-announcement/, accessed 2026-08-06).

**Rule 5: Write the release notes plainly.** "This update introduces a subscription for new capability. Everything that was free stays free, and everyone who used Waypoint before today keeps their full feature set." Evasive language in release notes generates distrust that in-app messaging cannot repair, and reviewers read them too [verified] (Source: AppsOps, "Migrating an iOS app from paid upfront to subscription", accessed 2026-08-06).

**Rule 6: Charge confidently and lead with gratitude, not apology.** Apologizing for pricing undercuts it; the right register is thanks for shaping the product, an honest statement of what paid funding builds, and a specific date [verified as practitioner guidance] (Source: Salable, "From Free to Paid: A SaaS Migration Guide", https://salable.app/blog/saas-startup-guides/free-to-paid-saas-migration, accessed 2026-08-06).

**Rule 7: Gate the whole thing behind the retention bar, per GD-1.** The paywall ships only when week-4 retention of route generators clears the healthy-cohort bar (directionally 20 percent-plus). Shipping a paywall to a base that is not returning burns the trust budget and produces no revenue, which is the worst available outcome (`../05-product/mvp-scope.md`, GD-1).

### 7.3 The sequence

| When | Action |
|---|---|
| Public launch day | Free tier named as permanent, in writing, in three places |
| Paywall minus 60 days | Retention bar checked. If it fails, the paywall slips and the plan says so out loud rather than shipping anyway |
| Paywall minus 30 days | Announcement: in-app modal (dismissible, shown once), email to all users, blog post, Reddit post in the venue where the community lives. Content: the date, what stays free, what founding runners keep, what the new capability is, and the price |
| Paywall minus 14 days | Founding-runner offer visible in-app. Support article live. Store description updated |
| Paywall day | Release notes per Rule 5. Promotional text updated. Founder present in every community channel for the full day |
| Paywall plus 1 to 14 days | Daily review monitoring on both stores, personal replies. Track the tripwires below |
| Paywall plus 30 days | Public retrospective post with real numbers. This is unusual and it is exactly the kind of thing that earns the trust the brand claims |

### 7.4 Pricing shape (defers to `revenue-model.md`, but GTM has requirements)

The go-to-market requirements on pricing, for the sibling document to honor: annual-first presentation, because Health and Fitness is the only category where annual plans still dominate at 60.6 percent of revenue; a free trial, because trials lift lifetime value 63.6 percent over direct purchase in this category with trial-to-paid benchmarking at 35.0 to 39.9 percent and top quartile above 50 percent; and a price inside the $80 to $120 per year umbrella already established between Garmin Connect+ at $70 and the Strava plus Runna bundle at $150 (`../01-market/industry-trends.md`, Section 3; `../02-competitors/positioning-map.md`, map 2) [verified for the benchmarks]. Cancellation must be one tap and visible, as an explicit counter-position to the category's billing record.

### 7.5 Tripwires and the kill switch

Monitor daily for 14 days after the paywall. Any two of these firing triggers a pause and a public response, not a quiet wait:

| Tripwire | Threshold |
|---|---|
| Store rating | Drops below 4.3 on either store, or more than 0.3 in 7 days |
| Review sentiment | More than 15 percent of new reviews mention pricing negatively |
| Uninstall rate | Exceeds the trailing 30-day baseline by 50 percent |
| Support volume | More than 3x the trailing weekly baseline |
| Free-tier usage | Weekly active generators among the grandfathered cohort drop more than 20 percent |

The response, if triggered, is a founder-signed post explaining what is being changed, and the change itself. The one response that is not available is silence, because silence is the documented failure mode of the competitor whose billing complaints created this opening in the first place. [inferred]

## 8. Traction milestones

All figures are directional planning targets derived from the benchmarks cited above, not forecasts. Each is paired with what it would prove to an investor, because a milestone that proves nothing is a vanity number.

| Milestone | Target | Timing | What it proves |
|---|---|---|---|
| TestFlight cohort assembled | 20 to 50 target-segment runners | Month 4 | The founder can reach the segment without paying for it. Fails the plan if it takes until month 6 |
| Interview program complete (Priorities 1 and 2) | 12 to 18 conversations | Month 4 | The umbrella job is real or it is not. This is the highest-information milestone in the whole plan and it is not a growth metric |
| Beta cohort | 150 to 300 active testers | Month 8 | The pre-launch community is large enough to carry a launch, and route quality has been stress-tested on more than one runner's habits |
| Waitlist | 1,500 to 3,000 | Month 9 | Demand exists outside the founder's network. At 30 to 50 percent conversion this is 450 to 1,500 launch installs |
| iOS launch, first 30 days | 500 to 1,500 installs; crash-free above 99.5 percent; rating 4.5-plus | Month 9 to 10 | Not volume. Quality: the engine works on real streets and the early cohort likes it enough to say so |
| First-generation success rate | Above 85 percent of first sessions produce a route the user starts | Continuous from iOS launch | Activation works. Below this, the funnel problem is onboarding, not acquisition |
| **Week-4 retention of route generators** | **20 percent or better** | Measured from iOS launch cohort, month 10 to 11 | **The core hypothesis.** This is the number the entire MVP exists to produce (`../05-product/mvp-scope.md`, Section 2) and the gate for the paid layer (GD-1). To an investor it is the difference between a feature and a product |
| Repeat generation rate | 2-plus generations per active user per week | Month 10 onward | Route generation is a habit, not a novelty. Directly tests the H1 reframe: if this holds at home, safety and novelty really do carry retention |
| Public launch (Android), first 30 days | 3,000 to 8,000 installs across both platforms | Month 11 to 13 | The channel mix works when fired at once. Also the first real read on whether press and creators move anything for this product |
| Monthly active runners | 2,000 to 5,000 | Month 12 | The Founder Brief's "thousands of active runners" 12-month criterion, met honestly |
| Travel-mode share of generations | 10 to 25 percent of generations far from home | Month 12 | Resolves the missing travel cross-tabulation with behavior instead of recall (`../03-users/unmet-needs.md`, Section d, signal 1). Low share confirms the reframe; high share reopens the travel wedge |
| Safety constraint usage | Share of generations with safety or time-of-day constraints active, by local hour | Month 12 | Whether the strongest-evidenced need is a daily driver or an occasional mode. Investors will not ask; this is for the founder |
| Paid layer, first 90 days | 4 to 8 percent of week-4-retained users convert | Month 12 to 15 | Willingness to pay, revealed rather than surveyed. Context: median download-to-paid across health and fitness apps is 2.7 percent with a top decile of 12.1 percent (`../03-users/segmentation.md`, Section 4), so converting a retained cohort at 4 to 8 percent is a credible target and above 10 percent would be a strong result |
| Retention of the grandfathered cohort | No more than 20 percent drop in weekly active generators post-paywall | Paywall plus 30 days | The trust transition survived. This is the number that proves the brand claim is operational and not just copy |

**What none of these prove, and should be said in the same breath to any investor:** that the company can acquire users outside one metro, that the loops compound, or that the coaching layer monetizes at scale. Those are the seed round's job, and pretending otherwise in month 12 is how a good traction story becomes a credibility problem. [inferred]

## 9. Partnerships

### 9.1 Worth pursuing

| Partner type | What it is | Why it works here | First step |
|---|---|---|---|
| **Local run clubs (3 to 6, one metro)** | Waypoint generates the club's weekly route; the club leader stops drawing them by hand | Solves a real recurring job for the one person in the club with influence, at zero cost, in the top-ranked channel | Month 2, attend without pitching. Offer route generation for one group run in month 5 |
| **Run specialty stores (1 to 3)** | Store hosts a club night; Waypoint provides the route and a short demo | Stores need content for club nights and have a commercial interest in local runners. Run club growth is explicitly reshaping how runners discover stores per the Running Industry Association source | Month 6, walk in with a printed route from their own front door |
| **Local running coaches (5)** | Free lifetime access; they use it to prescribe where their athletes run | High-credibility multipliers with the exact segment, and they surface the FJ4 workout-to-route job that Phase 3 says is inferred rather than expressed | Month 6, email five named local coaches with a specific route for their usual training loop |
| **One local half marathon or 10K** | A beta-recruitment table, a training-route Custom Product Page, not a sponsorship | Race travel and race motivation are documented drivers, and local races are cheap and reachable. Runna partnered with race organizers at scale; Waypoint does the neighborhood version | Month 8, email the race director offering free routes for their training program |
| **OpenStreetMap local mapping community** | Participate in pedestrian mapping in the beachhead metro; contribute back | The data Waypoint depends on is volunteer-built and under-mapped, especially crossings. Contributing is both correct and self-interested | Month 3, attend one local OSM meetup or Mappy Hour as a contributor |
| **Women's running groups** | Presence and listening, not sponsorship | The highest-intensity cohort. But this must be participation and support, never a campaign, and never with the safety statistics in the copy | Month 4, attend. Do not pitch. Ask the Priority 2 study's questions in person |

### 9.2 Not worth pursuing, and why

| Partner type | Why not |
|---|---|
| **Hotels and travel brands** | The seductive one. The travel demo makes hotel partnerships feel inevitable, and they are wrong three times over: travel is the activation moment and not the retention driver (`../03-users/unmet-needs.md`, Section b), a single-metro data build cannot serve arbitrary destinations at the quality that would justify a partner's brand, and hotel and OTA business development cycles run six to eighteen months against a founder with three hours a week. Revisit at Series A with national data coverage |
| **A formal Strava partnership** | Waypoint should integrate with Strava and should not negotiate with it. Strava's API bans AI use of its data (`../02-competitors/adjacent-platforms.md`), it owns the category leader, and it is the company most likely to build this feature. A partnership conversation is a free competitive briefing. Be an excellent, quiet, well-behaved integration |
| **Garmin** | The developer program is paused with no timeline (`../04-synthesis/concept.md`, Section 5; `../01-market/industry-trends.md`, assumption A4). There is nothing to pursue |
| **Shoe and apparel brands** | They want reach and content, which Waypoint does not have. At 2,000 monthly actives there is no trade to make, and chasing one costs months |
| **Corporate wellness and employer channels** | A B2B motion with a procurement cycle, a different product surface, and a different buyer. It is the single most common way a consumer app at this stage loses a year |
| **Insurers and health plans** | A real and growing channel in wearables (`../01-market/industry-trends.md`, Section 3, Essence Healthcare and Oura), and completely unreachable for a pre-seed running app with no clinical claim. Also note: any insurer conversation pushes toward health outcome claims, which collides directly with Rule S |
| **Race majors (Boston, London, NYC)** | Runna has these relationships and the price of entry is sponsorship money. The local version in 9.1 gets 80 percent of the value for zero |
| **Paid affiliate networks** | Runna scaled an ambassador program on a dedicated affiliate platform, but that is infrastructure for hundreds of ambassadors. At six, a spreadsheet and honesty are sufficient |

## 10. Assumptions register and open questions

### 10.1 Assumptions

| ID | Assumption | Why it matters | How it gets tested |
|---|---|---|---|
| A1 | **The beachhead metro clears the pedestrian-data floor** (silver-tier footways and crossings, usable lighting tags). | If it fails, either the safety differentiation is thin at launch or the founder relocates their GTM effort to another city at real personal cost. This is the riskiest assumption in the plan | Month-1 A3 spike (GD-3). Answer arrives before any marketing money is spent, which is the one piece of good news about it |
| A2 | Run clubs will tolerate and then welcome a founder who shows up weekly, and club leaders will adopt generated routes for group runs | The top-ranked channel rests on it. If clubs are indifferent, the whole channel ranking reorders and Reddit plus beta subreddits become primary | First five club visits, months 2 to 4. Signal: does anyone ask what he is building without being prompted |
| A3 | The 20 to 50 TestFlight runners are recruitable by month 4 from the five sources in 4.2 | Inherited from `../05-product/mvp-scope.md`. Slipping it delays every retention measurement downstream | Month 4, countable |
| A4 | A quiet iOS launch does not cost more than it saves | The alternative view is that launch momentum is use-it-or-lose-it and splitting it wastes both. The plan bets on quality compounding, which is a judgment call | Compare iOS launch-cohort rating and week-4 retention against the Android-cohort equivalents |
| A5 | Android certifies within 4 to 8 weeks of iOS | If it slips past month 13 the public launch fires on iOS alone, per the hard rule in 5.1. Background GPS survival against OEM battery management is the named risk (DEC-010) | Android closed testing, months 10 to 11 |
| A6 | Run club leaders experience weekly route selection as a real chore worth solving | Untested inference underlying the strongest partnership idea in Section 9 | Ask three club leaders directly in month 3. Cheap to test, so test it early |
| A7 | The waitlist converts at the published 30 to 50 percent range | Every launch-day install estimate depends on it. Consumer waitlists are known to have 40 to 60 percent of signups who never open the first email, so the effective list may be a quarter of the headline | Measurable at the iOS launch; adjust the Android launch expectations accordingly |
| A8 | Week-4 retention of 20 percent or better is achievable for this product | It is the GD-1 gate and it borrows category subscription-cohort benchmarks rather than route-app benchmarks, because no route-generation retention benchmark was found | Month 10 to 11, and it is the moment of truth for the whole company |
| A9 | The Strava share loop contributes under 5 percent of installs | Assumed weak on purpose so the plan does not depend on it. If it is stronger, that is upside and the loop deserves investment | Referral parameter instrumentation from launch |
| A10 | Rule S survives contact with creators and press | One careless sentence in a video or a headline creates the liability the product design was built to avoid | Written clauses plus review-before-publish, and a monthly search for the phrase "safe route" plus "Waypoint" |
| A11 | The competitive window holds long enough that this sequence completes before Strava ships plan-linked generation with constraint depth | The whole calendar assumes 12 to 18 months from mid-2026 (`../02-competitors/gap-analysis.md`, Section c) | Weekly early-warning monitoring already specified in Phase 2 |
| A12 | Paid conversion of 4 to 8 percent of retained users is achievable at the $80 to $120 price band | Directional, extrapolated from category benchmarks rather than from any route-product comparable | Paywall plus 90 days |
| A13 | The founder can sustain 15 to 25 GTM hours per week during the launch window without the product slipping | The plan explicitly slows product work for roughly six weeks. If that is not acceptable, the launch scope must shrink rather than the timeline stretch | Self-evident by month 10 |

### 10.2 Open questions for the founder

1. **Which metro is the beachhead, and is it the founder's home metro?** This is the first decision the plan needs and it depends on the A3 spike plus a fact the research does not contain. If the home metro fails the data floor, is the founder willing to spend two days a month in another city for a year?
2. **Is the Android date accepted as the real public launch?** This is a strategic call, not an operational one, and everything in Sections 4 and 5 sequences from it. The alternative (loud iOS, quiet Android) is defensible if the founder weighs iOS revenue concentration above physical community reach.
3. **What is the actual GTM cash budget between now and the seed?** Section 0 assumes $100 to $800 per month. If the real number is zero, the creator gifting and any tooling drop out and nothing else changes, which is worth knowing.
4. **Does the founder want an ambassador program at all?** It is the proven category playbook and it is an operations job. Six ambassadors is recommended; zero is a legitimate answer for a solo founder and the plan survives it.
5. **What does legal review say about Rule S**, and does counsel want stricter language than Section 2.5? The Phase 4 requirement for legal review of safety-adjacent copy is unmet and it gates the store listing, not just ads.
6. **Who writes and sends the press pitches?** It is a week of work in the launch window, it is the lowest-ranked channel that still made the list, and it is the easiest thing to cut if the calendar compresses. Decide now rather than in month 11.
7. **What is the founding-runner offer exactly?** Section 7 specifies a permanent discount via promotional offer. The percentage is a pricing decision for `revenue-model.md`, but the GTM requirement is that it be generous enough to feel like a thank-you rather than a coupon.
8. **Is the Play account an organization account, confirmed in the console?** A confirm-and-move-on item that becomes a two-week launch delay if the answer is discovered late.

## Related

- `../04-synthesis/positioning.md` and `../04-synthesis/concept.md` (the locked positioning this document translates)
- `../03-users/unmet-needs.md` (the H1 reframe that shapes the channel and message asymmetry)
- `../02-competitors/gap-analysis.md` (the do-not-compete list and the competitive window)
- `../05-product/mvp-scope.md` (the build calendar this plan is sequenced against)
- `./revenue-model.md`, `./unit-economics.md`, `./metrics.md` (siblings; pricing shape, CAC, and the metric tree live there)
- [[DEC-006 Concept lock route-first positioning]], [[DEC-008 Phase 5 gate MVP approved stack in validation]], [[DEC-010 Staged cross-platform MVP on React Native]]
