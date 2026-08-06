# Revenue Model: Pricing Strategy and Revenue Streams

Version-Timestamp: 2026-08-06 12:10:00 UTC-4

**Executive summary.** One revenue stream: a single-tier consumer subscription, sold through the app stores, at a **list price of $99.99 per year or $12.99 per month** (defensible band $79.99 to $119.99 per year), with a **21-day free trial on the annual plan** and a **grandfathered Founding Runner rate of $69.99 per year** for everyone who installed during the free v1 period. Every other candidate stream is assessed below and rejected or deferred, and the two that look most tempting on paper (advertising or sponsored routes, and licensing the street-context data) are rejected permanently and on the record, because both are illegal-adjacent under the compliance posture Waypoint has already committed to and both corrupt the one thing the product sells.

The free/paid line: **everything that ships in MVP v1 is free forever, plus every remaining routing constraint, the Watch app, GPX export and the preference-learning loop; the paid tier is the coaching layer only, one nameable job, "your training, routed."** Safety-aware routing is free permanently (DEC-008) and is never mentioned in an upgrade prompt.

Revenue is **zero through month 9 by design**, starts in months 10 to 12 with the v1.x paywall, and exits month 24 at a modeled $86,000 to $857,000 net annual run rate depending almost entirely on how large the free base is when the paywall ships. Three things can break the model: the paid layer's job (training-state-aware generation) is the one part of the concept whose demand is `[inferred]` rather than verified; category annual renewal is far worse than intuition suggests (roughly a quarter of annual subscribers renew at median, per RevenueCat 2026); and every month of launch slip pushes first revenue past the 12-month goal, so the seed has to be raised on retention telemetry rather than on revenue.

**Standards.** Every external claim carries a source and an access date, and every claim is tagged `[verified]`, `[inferred]`, or `[assumption]`. Prices reused from Phase 2 carry their original 2026-07-30 access date through `pricing-matrix.md`; new external claims were accessed 2026-08-06. Assumptions are collected in the register at the end (A1 to A16) and never silently absorbed into a conclusion.

## 0. What is already locked (the constraints this document obeys)

| Locked input | Source | Consequence for pricing |
|---|---|---|
| v1 launches entirely free, no active paywall | DEC-008, `mvp-scope.md` GD-1 | Months 1 to 9 revenue is zero by design, not by failure |
| Safety-aware routing is free permanently | DEC-008 (resolves the Phase 4 ethics defer) | Safety never appears on a paywall, in an upgrade prompt, or in a "unlock" string |
| Route generation is the free-tier anchor | `concept.md` S4, `gap-analysis.md` (d), `pricing-matrix.md` | The hero feature is the acquisition engine, not the meter |
| The adaptive coaching layer is the paid anchor | `concept.md` S4, H3 monetization caveat | The paid tier's job is training, not more routing |
| Paid layer ships in v1.x, months 10 to 12 | DEC-008, `mvp-scope.md` S7 (as amended by DEC-010) | Pricing decisions must survive a 9-month free period first |
| Both stores, iOS month 9 to 10, Android month 10 to 12 | DEC-010 | Two commission regimes, two billing-health profiles, one price |
| NOT list: no social, no route library, no multi-sport, no plan-quality brand war | DEC-006 | Kills several otherwise attractive secondary streams outright |
| "Safety-aware" is the ceiling, never "safe" | `positioning.md` S6 | Binding on all pricing and paywall copy, reviewed by counsel |

## 1. Revenue streams

### 1.1 The recommendation in one table

| # | Stream | Verdict | When |
|---|---|---|---|
| 1 | Consumer subscription (single tier) | **ADOPT. The only stream.** | v1.x, month 10 to 12 |
| 2 | Advertising, sponsored routes, brand placements | **REJECT permanently. Add to the NOT list.** | never |
| 3 | Data licensing (aggregate route, safety, or mobility data) | **REJECT permanently. Add to the NOT list.** | never |
| 4 | Affiliate commerce (shoes, gear) | **REJECT for v1 and v1.x.** Conditional revisit only. | not before year 3 |
| 5 | B2B travel (hotels, hotel groups, tourism boards) | **REJECT as revenue. Reclassify as a GTM channel.** | GTM only |
| 6 | Race organizer and event partnerships | **REJECT as revenue. Reclassify as a GTM channel.** | GTM only |
| 7 | Corporate wellness / B2B2C seats | **DEFER.** No structural conflict, no capacity. | year 3+, inbound only |
| 8 | One-time purchases (route passes, trip packs) | **REJECT as a standing stream.** One bounded experiment allowed. | test only, year 2 |
| 9 | Lifetime plan | **REJECT.** See section 3.4. | never |
| 10 | Web checkout to reduce store commission | **NOT a stream: a margin lever. Do not build for v1.x.** | revisit at ~$50k MTR |

### 1.2 Primary stream: the consumer subscription

The subscription is the whole business, and the category says that is the correct answer rather than a lazy one. Health and fitness is the app category with the highest realized lifetime value per payer after year one ($35.64 median, more than three times gaming's $11.22) and the only category where annual plans dominate revenue `[verified]` (RevenueCat, State of Subscription Apps 2026, Health and Fitness, https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/, accessed 2026-08-06). Every proven payer benchmark in the competitive set is a subscription: Runna at $119.99 per year with roughly 90,000 payers, Strava at $79.99, RunGo at $59.99 for navigation alone `[verified via `pricing-matrix.md` and `market-sizing.md` S4, underlying sources accessed 2026-07-30]`.

Waypoint's structural advantage inside that model is that **nobody prices the combination**. A runner assembling Waypoint's promise today buys Runna ($119.99) plus Strava ($79.99) for routes, or the $149.99 bundle, and still gets no constraint-based generation `[verified, `pricing-matrix.md`]`. That is the pricing argument in one sentence, and it is the only pricing argument Waypoint needs.

### 1.3 Rejected on the record: advertising, sponsored routes, location-based ads

This is the stream that will keep being suggested (by advisors, by investors, by the founder at 2 a.m. in month 11 when revenue is still zero), so the rejection is written out rather than assumed.

**The legal case.** Apple App Review Guideline 5.1.3(i) prohibits using or disclosing data gathered in the health and fitness context for advertising, marketing, or use-based data mining, and 2.5.18 plus 5.1.1 prohibit targeted or behavioral advertising based on health or HealthKit data `[verified]` (Apple App Review Guidelines, https://developer.apple.com/app-store/review/guidelines/, accessed 2026-07-30 via `regulatory-compliance.md` S3). Maryland's MODPA bans the sale of sensitive personal information outright with consent being irrelevant, and Maryland, Oregon, Virginia and Connecticut prohibit the sale of precise geolocation data `[verified]` (`regulatory-compliance.md` S1, sources accessed 2026-07-30). The FTC's X-Mode, InMarket and Kochava orders establish that liability attaches to derived audience products, not only to raw coordinates `[verified]` (same). Adding any ad SDK also triggers App Tracking Transparency, which conflicts with the health data rules and destroys the tracking-free posture the whole compliance architecture assumes (`regulatory-compliance.md` assumption A3).

**The product case, which is the stronger one.** Waypoint sells exactly one thing: the belief that the route on the screen was chosen for the runner. A sponsored route is a routing input the runner did not ask for and cannot see. The moment a coffee chain can pay to be on the way, the product's only claim is false, and there is no disclosure copy that repairs it. This is a sharper version of the same reason the concept forbids ranking by popularity.

**Verdict: reject permanently.** Recommend adding "advertising, sponsored routes, and any paid placement inside a generated route" to the DEC-006 NOT list at the Phase 6 gate, so no future session reopens it casually.

### 1.4 Rejected on the record: data licensing

The temptation is real and specific. Waypoint will build street-level context data (crossing graphs, lighting and populated-area scoring, later real running-line traces) that cities, insurers, retailers and mobility researchers would plausibly want. Four reasons it is still a no:

1. **It is the same sale, one abstraction away.** The InMarket order exists precisely because aggregating and deriving does not launder the underlying sensitive category `[verified]` (`regulatory-compliance.md` S1). Waypoint's users would be handing over precise geolocation under a private-by-default promise.
2. **The market price appears to be zero.** Strava, which holds the largest human-powered movement dataset in the world, gives Metro to qualified planning organizations free of charge and has done since 2020 `[verified]` (Strava Metro, https://metro.strava.com/ and https://metro.strava.com/case-studies/the-new-human-powered-era, both accessed 2026-08-06). If the category leader cannot charge for this, a startup with a rounding error of the data certainly cannot, and the effort would be spent for a revenue line that never materializes.
3. **The licence boundary is already tight.** OSM-derived context layers may constitute a Derivative Database under ODbL share-alike; the mitigation strategy in `stack-recommendation.md` depends on keeping independent-source layers separate and not publicly using a merged derived database. Selling it is the one action most likely to force the share-alike question `[verified as to the licence structure, `stack-recommendation.md` S1]`.
4. **It contradicts the positioning.** Privacy-as-architecture is the differentiation. A data licensing line item on a pitch deck reprices the entire trust story.

**Verdict: reject permanently.** One narrow non-revenue carve-out is worth keeping alive: donating aggregated, opt-in, k-anonymized safety-gap findings to a city safe-streets program is a brand asset rather than a revenue stream, and should only ever happen with explicit standalone consent and counsel sign-off. Do not model a dollar against it.

### 1.5 Affiliate commerce: reject for now, with a named condition

Running retail affiliate programs typically pay in the mid single digits to low tens of percent, and running is a gear-heavy sport, so the arithmetic is not absurd `[assumption A1: no affiliate rate was verified for this document]`. Two reasons to say no anyway. First, it is the sponsored-route problem in a milder form: once shoe revenue exists, every surface-preference and injury-calibration output is suspect, and Waypoint's coaching credibility is already the thing it is least able to defend against Runna. Second, it is a distraction against a 12 to 18 month competitive window with a solo founder and two contractors.

The condition under which it becomes a yes: a surface where the **user initiates** the commercial question and Waypoint gives no recommendation (for example a shoe-rotation mileage tracker that links out to a retailer of the user's choosing). Not before year 3.

### 1.6 B2B travel and race partnerships: real, but they are channels, not revenue

The Priya persona and the Great Runs cottage industry make hotel-side distribution obviously attractive (`personas.md`, `unmet-needs.md` need 4). But selling to hotel groups means enterprise sales cycles, an account-management function, and a roadmap pull toward curated route content, which the NOT list forbids ("generate, do not curate"). Race organizer partnerships have the same shape, and Runna already owns that channel through race and elite partnerships `[verified, `profile-runna.md` via `gap-analysis.md` (c)]`.

**Reclassify both into `gtm-plan.md` as acquisition channels.** A co-branded free "runs from our door" surface at a hotel partner costs Waypoint nothing marginal (routing compute is roughly $0.03 per MAU per month at 10k MAU, section 6.4), reaches exactly the activation persona at exactly the activation moment, and monetizes through the same single subscription. That is a better use of the same relationship than an invoice.

### 1.7 Corporate wellness: defer, do not design for it

There is money here (AI Endurance runs a B2B club portal, Joggo's parent sells B2B wellness bundles, per `pricing-matrix.md`), and unlike advertising it carries no ethical conflict. It also requires SSO, admin dashboards, seat billing, procurement, invoicing and a support function, none of which exist in the 15-feature MVP or in the team. **Defer to year 3 and only in response to inbound demand.** Do not add multi-seat concepts to the entitlement model now.

### 1.8 One-time purchases: reject as a standing stream

Footpath sells a $1.99 single-route pass and RunGo sells a $119.99 lifetime unlock `[verified, `pricing-matrix.md`]`. Both are utility-shaped businesses. For Waypoint, consumables fragment the value story, complicate the entitlement model, and add exactly the billing surface area that produced documented trust damage across Joggo, Runna and Komoot `[verified, `gap-analysis.md` unmet need 7]`. Trustworthy subscription mechanics are themselves a differentiator in this category; do not spend that asset on a $1.99 SKU.

One bounded experiment is defensible in year 2: a consumable **travel week pass** aimed at users who will never subscribe but who face the Priya moment three times a year. Run it as a test with a kill date, not as a plan.

### 1.9 Web checkout: a margin lever, not a stream, and not yet

Since May 2025 apps on the United States storefront may include external purchase links without the StoreKit External Purchase Link Entitlement and, following the Epic ruling, without Apple commission on those transactions; the matter was remanded in April 2026 and the fee question is unresolved `[verified as reported; secondary sources, medium credibility]` (PTKD, https://ptkd.com/journal/apple-rejection-3-1-1-in-app-purchase-links, and Funnelfox, https://blog.funnelfox.com/apple-app-store-fees-2026-eu-dma/, both accessed 2026-08-06). In the EU the entitlement is required and the fee stack (5 percent Core Technology Commission plus Store Services Fee plus a 2 percent Initial Acquisition Fee on new users, with Small Business Program members at the reduced Store Services tier) lands near 20 percent rather than zero `[verified as reported; secondary sources]` (Foresight Mobile, https://foresightmobile.com/blog/app-store-fees-2026-web-to-app-billing, accessed 2026-08-06; Apple, https://developer.apple.com/support/communication-and-promotion-of-offers-on-the-app-store-in-the-eu/, accessed 2026-08-06).

Three reasons not to touch it at v1.x. The saving against the Small Business Program's 15 percent is small in the US and negative-to-marginal in the EU. It moves ROSCA, state auto-renewal law, and the EU withdrawal-button mechanics from Apple's plate onto Waypoint's (`regulatory-compliance.md` assumption A4). And its US legal status could reverse inside the modeling window. **Revisit at roughly $50,000 monthly tracked revenue**, the same threshold `stack-recommendation.md` sets for revisiting RevenueCat.

## 2. The free/paid boundary, feature by feature

### 2.1 The rule

> **Everything that ships in MVP v1 is free, permanently. The paid tier is the coaching layer: the features that require Waypoint to know what the runner's body needs, not merely where the runner is standing.**

Two tests, both from the brief, both applied honestly below.

**Test 1: does the free tier stand alone as a product someone keeps using?** Yes, and this is not a close call. The free tier is a complete, polished, cross-platform running app that generates constraint-aware routes from anywhere, runs them with voice guidance, records them, syncs to Health and posts to Strava. No product on the market gives that away: Strava puts every routing feature behind $79.99, AllTrails puts AI route adjustment in its top $79.99 tier, and the free web generators have no mobile execution experience `[verified, `pricing-matrix.md`, `gap-analysis.md` unmet need 8]`. The free tier is not a demo. It is the acquisition wedge, and it is deliberately better than the competition's paid product at the one job it does.

**Test 2: does the paid tier deliver a distinct, nameable job?** Yes: **"your training, routed."** Not "more routes", not "faster routes", not "the safe ones". The paid job is the seam that `gap-analysis.md` found structurally empty across fifteen-plus products: today's workout, your fatigue, your race, expressed as the route that gets generated. A runner can describe what they bought in one sentence, which is the test a paid tier has to pass.

The honest caveat, stated here rather than buried: this boundary makes the paid tier carry conversion entirely on its own, against a free tier engineered to be sufficient. That is risk number one in section 7, and it is the direct cost of the locked decisions. It is the right cost to pay, because the alternatives (metering generation, or paywalling constraints) either charge for what the market gives away free or put safety behind a paywall.

### 2.2 MVP v1: all fifteen features, free forever

| ID | Feature | Side | Why this side |
|---|---|---|---|
| TS-04 | Onboarding and permissions | Free | Activation gate. Nothing before value. |
| TS-01 | GPS run tracking | Free | Table stakes across all ten competitors; Nike Run Club gives it away entirely. |
| TS-05 | Audio pace and distance cues | Free | Zero-price basic; every headphone runner expects it. |
| TS-02 | Run history and basic stats | Free | The return visit needs something to return to. Charging for a user's own history contradicts the privacy brand. |
| TS-03 | HealthKit / Health Connect sync | Free | The moat accrues from day one; gating it starves the data that makes the paid tier possible. |
| TS-06 | Route save and re-run | Free | A generated route the user cannot keep is a broken promise, not an upsell. |
| TS-07 | Strava share | Free | Free distribution and credibility. Paywalling it would suppress the cheapest acquisition loop the product has. |
| O-01 | Privacy zones, private-by-default, consent, AI disclosure | Free | Legal obligation (EU AI Act Article 50, GDPR) and the trust floor. Never a feature. |
| H-01 | Core constraint route generation | Free | The hero and the anchor. Commoditized at zero by free web tools and forced by `pricing-matrix.md`. |
| H-02 | Elevation constraint | Free | A constraint, therefore hero, therefore free (see 2.4). |
| H-07 | Route novelty, "roads you have not run" | Free | Evidence rank 2 need and the daily retention driver. Retention features belong in the tier that has to retain. |
| H-05 | Safety-aware routing v1 | **Free permanently** | DEC-008. Ethical commitment, not a growth tactic. Never appears in an upgrade prompt. |
| H-08 | Travel mode framing | Free | The activation moment and the demo. Paywalling the demo is self-defeating. |
| H-09 | Honest degradation messaging | Free | Inseparable from the safety commitment. |
| X-01 | Voice turn-by-turn navigation | Free | The execution surface of the free hero. Note the tension: RunGo proves runners pay $59.99 a year for navigation alone `[verified]`, so this is real value given away. It is given away because generation without execution strands the value, and a half-usable hero is worse than no hero. |

### 2.3 Fast-follow v1.x: where the line actually gets drawn

| ID | Feature | Side | Why this side |
|---|---|---|---|
| X-02 | Apple Watch companion | Free | Anti-positioning list: never compete on device features, and Garmin and Apple set a zero floor there `[verified, `positioning.md` S6]`. A paywalled watch app is a paywall on the free hero's execution. |
| TS-08 + P-01 | Paywall plus **training-state-aware generation** | **PAID. The anchor.** | This is the seam: today's workout type, fatigue and readiness, and race progression shaping the route that gets generated. Total market absence `[verified, `gap-analysis.md` unmet need 1]`. It is the first thing a runner can only get here. |
| H-04 | Street-crossing minimization | Free | A constraint (see 2.4). |
| H-06 | Weather and heat route adjustment | Free | A constraint, and heat is safety-adjacent. Runna and TrainAsONE only slow the pace; adjusting the route is the differentiator, and it belongs in the wedge. |
| H-03 | Surface constraint | Free | A constraint. |
| TS-10 | Offline route access | **Split** | The route you have loaded works offline: free, because a route that fails in a dead zone is a safety failure, not an upsell. Multi-route and region offline packs: paid, matching the Komoot and AllTrails pattern `[verified, `pricing-matrix.md`]`. |
| P-03 | Explainable generation ("why this route") | **Split** | Constraint and safety explanations ("this route avoids the unlit park section"): free, because they are inseparable from the safety commitment and from EU AI Act Article 50 transparency. Coaching explanations ("this is a flat uninterrupted loop because today is a tempo day and your readiness is down"): paid, because they are the coaching layer talking. |
| TS-09 | GPX export | Free | Data portability. Charging a user to remove their own data from the product is exactly the move the privacy positioning forbids, and GDPR Article 20 makes export an obligation-adjacent expectation anyway. |

### 2.4 The constraint rule, stated explicitly because it is the counter-intuitive part

**Every routing constraint is free. All of them. Permanently.** Elevation, surface, crossings, weather and heat, lighting and populated areas, time of day, novelty.

The instinct is to sell constraint depth, since constraint depth is the moat. Three reasons not to:

1. **The concept says the hero is constraint-based generation.** A free tier with two constraints and a paid tier with six is not "free route generation, paid coaching". It is a crippled hero, which is exactly the pattern the brief's test rules out and which TrainAsONE's users describe as "so limited as to be unworthy of anyone's time" `[verified, `pricing-matrix.md`]`.
2. **Safety cannot be separated from the others in practice.** Lighting is free by decision. But crossings, surface and heat are all safety-adjacent in the situations that matter (a dark route with six unlit crossings, a heat-exposed route at 2 p.m.). Drawing a paid line through the constraint set means litigating "is this one safety" in every product review for the life of the company. One rule removes the argument.
3. **Constraint depth is a moat against competitors, not a lever against users.** It defends the free tier's superiority over Strava's popularity-ranked generation, which is where the acquisition advantage lives. Monetizing it would trade the acquisition advantage for a small conversion gain.

### 2.5 Deferred v2+ features

| ID | Feature | Side | Why |
|---|---|---|---|
| P-02 | Adaptive routines (plans that reshape) | Paid | The coaching layer's depth. The single most important paid-tier investment after P-01. |
| P-06 | Injury-calibrated progression | Paid | Coaching. The Runna-too-aggressive to TrainAsONE-too-conservative middle `[verified, `gap-analysis.md` unmet need 4]`. |
| P-05 | Race-goal progression | Paid | Coaching. |
| P-04 | Readiness and fatigue input | Paid | Coaching. The input that makes P-01 more than a workout-type filter. |
| H-10 | Learning loop (preference model) | **Free** | Contrarian call. The learning loop is the compounding switching cost and it needs volume to work at all; restricting it to payers starves the model of exactly the data that makes it good. "Waypoint learns your preferences for free; Waypoint coaches your training for money" is also a cleaner sentence than any alternative. |
| X-03 | Live location sharing | Free if built | Safety. Same rule as H-05. (`mvp-scope.md` says build it only if interviews show Strava Beacon and Find My leave a real gap.) |

### 2.6 Free-tier cost control without a meter

`pricing-matrix.md` correctly warns that a free tier needs a strict cost ceiling per free user or it becomes subsidy without conversion. The numbers say the ceiling is generous. Total external infrastructure is roughly $80 to $130 per month at MVP and roughly $350 to $500 per month at 10,000 MAU, and roughly $2,000 to $3,500 per month at 100,000 MAU `[verified as estimates, `api-integration-map.md` S8.2, `stack-recommendation.md` S6]`. That is on the order of $0.02 to $0.04 per MAU per month, which is roughly one three-hundredth of the annual subscription price. Free users are affordable at any scale Waypoint will reach before a seed round.

Recommendation: **no generation cap at launch.** Instrument cost per free MAU from day one and add an anti-abuse soft limit only at a threshold well above genuine use (a working figure of 30 generations per day, tuned once the 95th percentile is known), framed and worded as abuse prevention, never as a paywall `[assumption A2: the 30-per-day figure is a placeholder until telemetry exists]`.

## 3. Price point recommendation

### 3.1 The recommendation

| Item | Recommendation | Range considered |
|---|---|---|
| Annual (list) | **$99.99 per year** | $79.99 to $119.99 |
| Monthly (list) | **$12.99 per month** | $9.99 to $14.99 |
| Annual discount | **36 percent off the monthly run rate** ($155.88 to $99.99), merchandised as "$8.33 a month, billed annually" | 25 to 40 percent |
| Trial | 21 days, annual plan only | 7 to 30 days |
| Founding Runner rate | **$69.99 per year, price-preserved for as long as the subscription stays active** | $59.99 to $79.99 |
| Lifetime tier | **No** | rejected, see 3.4 |
| Second paid tier | **No at v1.x**, architected for but not shipped | see section 4.1 |

### 3.2 Why $99.99 against the competitor anchors

| Anchor | Price | What it tells us |
|---|---|---|
| Runna | $119.99/yr, $19.99/mo | The category leader's reference price for coaching alone, with no route capability at all. Waypoint at $99.99 sits 17 percent under the brand it cannot out-brand, while doing something Runna cannot do. |
| Strava | $79.99/yr, $11.99/mo | Every routing feature is paid here. $79.99 is the price of popularity-ranked generation with no personalization. Waypoint's monthly at $12.99 sits a dollar above, which is the correct signal: more per-runner work, not a utility. |
| Strava + Runna bundle | $149.99/yr | The assembled alternative, and the effective ceiling on what a committed amateur spends on running software `[assumption, carried from `adjacent-platforms.md` A7]`. Waypoint at $99.99 undercuts it by a third. |
| AllTrails Peak | $79.99/yr | AI route features at the top of a two-tier ladder. Proves paid demand for the hero capability, and sets the price of a shallower version of it. |
| Coopah | $79.99/yr, $14.99/mo | Committed amateurs accept $79.99 for coaching alone. |
| Garmin Connect+ | $69.99/yr | The low end of paid AI-flavored coaching, with free Garmin Coach plans underneath it. This is why $69.99 is the floor for the founder rate, not for list. |
| RunGo | $59.99/yr | Runners pay this for navigation execution alone. |
| Komoot | €59.99/yr | Route planning depth in the utility band. |
| Footpath | $23.49/yr | The bottom of the utility band. Waypoint must not be read as living here. |

All figures `[verified, `pricing-matrix.md`, underlying profiles accessed 2026-07-30]`.

`pricing-matrix.md` independently derived a credible band of $79.99 to $119.99 per year and pointed at roughly $99.99 as the number that undercuts the assembled alternative while pricing above the utility band. This document reaches the same place from the persona side and adopts it.

### 3.3 Why $99.99 against stated willingness to pay

- **Marcus (core payer, highest willingness).** Already pays for at least one running subscription and benchmarks against Runna's $119.99 `[verified as benchmark, `personas.md`]`. A price below Runna that replaces part of what Runna does plus part of what Strava does is a legible trade for him.
- **Priya (activation, high willingness).** She is buying insurance against a lost long run mid-block, and she already lets fitness drive a hotel booking decision (83 percent of business travelers weigh workout facilities or walkable areas when booking) `[verified, `personas.md`]`. Price is not her constraint; trust in the 6 a.m. route is.
- **Elena (retention, complicated willingness).** Resolved by DEC-008 rather than by pricing: she never sees a paywall on the thing she needs. Her willingness to pay is therefore irrelevant to the price point and highly relevant to the brand.
- **Jake (secondary, medium and event-driven).** $99.99 is a real ask for an early-20s beginner, and his conversion is trial-heavy and churns after the goal race `[assumption, `personas.md`]`. He is served by the free tier being genuinely complete, which is what the boundary in section 2 delivers, and by the monthly plan existing at all. Do not build a cheaper tier for him (section 4.1).

The category benchmark supports pricing at the top of the plausible band rather than the bottom: higher-priced apps generate materially higher lifetime value per payer ($62.19 median year-one RLTV in the high-price band versus $10.69 in the low band, a roughly six-fold spread) and also convert **better**, not worse, at the download-to-paid step (2.8 percent high band, 2.0 percent mid, 1.4 percent low) `[verified]` (RevenueCat, State of Subscription Apps 2026, https://www.revenuecat.com/state-of-subscription-apps, accessed 2026-08-06). Treat the direction rather than the digits: these are cross-category medians and are confounded by product quality, but nothing in them supports discounting into the utility band to buy conversion.

### 3.4 Lifetime and founder tiers

**Lifetime: no.** Three reasons.

1. Health and fitness has the **lowest** lifetime-plan share of any app category, while leading annual adoption at 68 percent of revenue `[verified]` (RevenueCat 2026, above). The category's own behavior says lifetime is not how this product is bought.
2. Waypoint carries per-user marginal cost (routing compute, weather calls, map tiles, and later on-device model updates). A lifetime plan converts a recurring cost into an unfunded perpetual obligation. RunGo's $119.99 lifetime works because RunGo is a navigation utility serving pre-made routes, not a generator.
3. It caps the metric the whole business runs on. Health and fitness leads all categories on year-one RLTV precisely because payers renew.

**Founder tier: yes, but as a preserved price, not a lifetime unlock.** The Founding Runner rate of $69.99 per year delivers the same emotional payload ("you were here first and it costs you less, forever") with none of the unfunded liability, and Apple and Google both support it operationally: Apple lets a developer keep an unlimited number of existing subscribers at their current price indefinitely while raising the price for new subscribers `[verified]` (Apple, Auto-renewable Subscriptions, https://developer.apple.com/app-store/subscriptions/, and Manage pricing for auto-renewable subscriptions, https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions/, both accessed 2026-08-06). Section 4.4 covers eligibility, implementation and cost.

### 3.5 Price the list high and discount, never the reverse

The strongest tactical recommendation in this document, and the one most likely to be got wrong: **set list price at the number you intend to hold and use reversible discounts to reach the market, rather than launching cheap and raising later.**

The store mechanics are asymmetric and verified. Price decreases apply to existing subscribers automatically and silently `[verified]` (Apple, Auto-renewable Subscriptions, above). Price increases either notify or require explicit consent, and consent is required when the increase exceeds roughly 50 percent of the current price and about US$50 per year for annual plans; a subscriber who does not consent has their subscription expire at the end of the current cycle `[verified]` (Apple, Manage pricing for auto-renewable subscriptions, above). Cancellations attributable to developer-initiated price changes are statistically negligible in aggregate (under 0.5 percent of cancellations on both stores) `[verified]` (RevenueCat 2026, above), which is reassuring but is measured on a population of developers who mostly avoid large increases.

Practically: launch at $99.99 list with the $69.99 Founding Runner SKU and a 21-day trial. If conversion is weak, discount (offer codes, seasonal intro offers, a lower regional price). Do not launch at $69.99 and try to reach $99.99 later, which is a 43 percent increase, over the $50 annual threshold, and therefore a consent-required event across the entire base.

## 4. Pricing structure

### 4.1 One tier, not two

**Ship one paid tier at v1.x.** A second tier requires a second nameable job, and at v1.x the paid product is a single feature (P-01 training-state-aware generation). AllTrails can run a Plus and Peak ladder because it has a decade of content depth to stratify `[verified, `pricing-matrix.md`]`; Waypoint stratifying one feature would produce a cheap tier that reads as crippled, which is the failure mode the boundary test exists to prevent.

**But architect for two.** Model entitlements in RevenueCat as named capabilities (`coaching.training_state`, `coaching.adaptive_plan`, `offline.packs`) rather than as a single boolean `is_pro`, so that a "Coach" tier above a "Plus" tier becomes a packaging decision in v2 rather than a migration project. This costs nothing now `[inferred, standard RevenueCat entitlement practice]`.

Family and gift plans (Strava sells Family at $139.99) are packaging questions for year 2 and are out of scope here.

### 4.2 Trial mechanics

**Recommendation: 21 days, on the annual plan only, delivered as a store introductory offer.**

- **Length.** Trials of 17 to 32 days convert at a 42.5 percent median versus 25.5 percent for trials of four days or fewer, roughly 70 percent better, and health and fitness leads all categories on trial-to-paid at a 37.7 percent median (top quartile above 51.4 percent) `[verified]` (RevenueCat 2026 Health and Fitness, accessed 2026-08-06). The correlation is confounded (apps confident enough to run long trials are probably better apps), so treat the direction rather than the digit. The product-side argument is independent and stronger: the paid tier's value is adaptation across a training week, which a 7-day trial physically cannot demonstrate and 21 days spans three times. TrainAsONE's 21-day trial is the one long trial in the competitive set `[verified, `pricing-matrix.md`]`.
- **Card required?** On both stores a free trial is an introductory offer attached to a subscription, so the store already holds payment credentials and auto-converts. A genuinely card-free trial requires a web funnel, which section 1.9 rejects for v1.x. So: card-on-file via the store, and compensate with honesty rather than pretending otherwise.
- **Honest trial mechanics as a differentiator.** Send an in-app and push reminder 48 hours before conversion (above what the stores send), state the conversion date and price on the paywall itself, and put a one-tap link to Manage Subscriptions in settings. This is nearly free to build and directly attacks the category's loudest trust failure (Joggo's renewal traps, Runna's double-charging, `gap-analysis.md` unmet need 7). It also front-runs ROSCA and state auto-renewal law rather than doing the minimum `[verified as to the obligations, `regulatory-compliance.md` S5]`.
- **Monthly plan: no trial.** Monthly is the low-commitment option already; adding a trial there both cannibalizes annual and invites a one-cycle-and-cancel pattern.
- **A note worth internalizing.** For most apps the trial proves the product. For Waypoint, **the free tier is the trial**, and it runs for months. The 21-day paid trial exists only to demonstrate the coaching layer, which is a narrower and more honest job. Do not over-invest in trial optimization; invest in the paywall's ability to explain one feature.

### 4.3 Presenting the transition: the one rule

> **Nothing that is free on the day before the paywall becomes paid on the day after.**

This is already implicit in DEC-008 (the paid feature ships *with* the paywall, so it is new capability rather than removed capability), but it should be stated explicitly, recorded as a decision, and written into the launch communication verbatim. It is the difference between "Waypoint added a coach" and "Waypoint took my app away", and the two produce different App Store rating distributions at exactly the moment ratings matter most (Android launch, seed conversations).

Communication sequence, all of it before the paywall ships:

1. **Month 8 to 9, at v1 launch.** Say the quiet part in the App Store description and onboarding: the app is free, a paid coaching layer is planned, and safety-aware routing will always be free. Setting the expectation nine months early converts the paywall from a betrayal into a delivery. Do not name a price.
2. **Month 10, roughly 30 days before.** In-app notice to the whole base: what is arriving, what stays free (the full v1 feature list, explicitly enumerated), and that early users get a permanent rate.
3. **Paywall day.** The upgrade surface names one job ("your training, routed") and lists exactly what it adds. It contains no reference to safety, and no mention of any feature the user already has.
4. **Ongoing.** The paywall appears at the moment of intent (a user asking for a workout-shaped run) and nowhere else. No interstitials on the free hero.

### 4.4 The migration risk, priced

**The risk.** Users who joined during the free v1 period will have used the whole product free for up to three months (and the earliest TestFlight cohort for nine). Any paywall lands on them as a takeaway regardless of what is technically being added, because reference points are set by experience rather than by feature lists. The category punishes this specifically: Komoot's paywall expansion triggered cancellations and public exit posts `[verified, `pricing-matrix.md`, `gap-analysis.md` unmet need 7]`.

**The three options, costed.** Base case for the arithmetic: 12,000 cumulative installs at paywall date and a 4 percent first-90-day conversion, giving roughly 480 subscribers (assumptions A5 and A6, section 6).

| Option | Mechanics | First-year revenue effect | Verdict |
|---|---|---|---|
| **Clean cutover** | Paywall ships, no acknowledgment of the free era | Highest nominal revenue: 480 x $99.99 = ~$48,000 gross | **Reject.** Saves roughly $14,000 against a review-bombing risk at the worst possible moment, and spends the trust asset the brand is built on. |
| **Grandfather the base free forever** | Everyone who installed pre-paywall keeps the coaching layer free | Roughly $48,000 forgone in year one, and permanently | **Reject.** Removes the entire warm cohort from the funnel, teaches the market that waiting is rewarded, and leaves no revenue signal for the seed. |
| **Founding Runner rate (RECOMMENDED)** | Free-era installers get $69.99 per year, preserved for as long as they stay subscribed; everyone gets an explicit "nothing you have today becomes paid" guarantee | 480 x $69.99 = ~$33,600 gross. **Cost of the discount: roughly $14,400 in year one**, less thereafter as new users arrive at list | **Adopt.** Roughly $14,000 buys the goodwill of the exact cohort that writes the launch reviews, seeds word of mouth, and gets quoted in the seed deck. |

**Eligibility and window.** Anyone with an install (or account) created before the paywall ship date, claimable for 60 days after the paywall ships. A window matters: an open-ended offer never converts, and 60 days is long enough to catch a monthly-cadence user.

**Two implementation notes that will otherwise cause pain.**

1. **Free users cannot be grandfathered by store price preservation.** Apple's preserve-price mechanism applies to existing *subscribers*, not to free users `[verified]` (Apple, Manage pricing for auto-renewable subscriptions, above). Founding Runner eligibility must therefore be a **server-side entitlement** keyed to account creation date, surfaced through RevenueCat offerings as a separate $69.99 annual SKU. Build the eligibility flag into the account model at v1, before the paywall exists, because retrofitting a trustworthy "who was here first" record after launch is unpleasant.
2. **Do not stack the founder price on top of a free trial as two store offers.** Store introductory offers are limited per subscription group, so the reliable pattern is a distinct SKU whose own introductory offer is the 21-day trial `[inferred; confirm the exact eligibility rules in App Store Connect and Play Console before building, open question 6]`.

## 5. Regional pricing

### 5.1 The launch geographies

`market-sizing.md` defines the SAM as the US, UK, EU-27, Canada and Australia, and the concept sets the expansion sequence as English-first, then Android, then more geographies `[verified, `market-sizing.md` S1, `concept.md` S6]`. Within that set, purchasing power differences are small and currency equalization is adequate. **Set the United States as the base territory, accept Apple's and Google's generated equivalents across the launch set, and override deliberately in the three cases below.**

Apple auto-generates comparable prices across 175 storefronts from the base territory, accounting for foreign exchange and certain taxes, and stops auto-adjusting any territory where a manual price is set `[verified]` (Apple, Set a price, https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/, accessed 2026-08-06). Sources conflict on whether the generated prices incorporate purchasing power: Apple's own documentation describes exchange rates and taxes, while some secondary commentary describes a purchasing-power blend `[verified as a conflict]` (vmobify, https://vmobify.com/blog/app-price-localization-ppp, and AppsOps, https://appsops.store/blog/app-store-tier-vs-custom-pricing, both accessed 2026-08-06, both low-to-medium credibility). Treat the direction rather than the digits: assume currency equalization, not purchasing-power equalization, and verify the generated grid against local competitor prices before shipping.

### 5.2 The three overrides worth making at launch

1. **VAT-inclusive display pricing in the EU and UK.** Store prices in Europe are shown tax-inclusive, so a $99.99 US anchor can generate a euro price meaningfully above Runna's and Strava's local numbers even though the pre-tax revenue is identical. **Check each launch storefront against the local competitor price, not against the dollar figure.** Runna and Komoot both price natively in GBP and EUR, so the comparison a European runner makes is direct `[verified as to native pricing, `pricing-matrix.md`; the VAT-inclusion trap is `[inferred]` from Apple's tax-inclusive generation described above]`. Working targets to validate against the generated grid: £89.99 and €99.99 annual, £11.99 and €12.99 monthly `[assumption A9]`.
2. **Canada and Australia.** Generated equivalents are fine; sanity-check that the annual lands on a locally conventional ending rather than a converted oddity.
3. **Nothing else.** Do not set discounted prices in markets outside the launch set.

### 5.3 Why aggressive regional discounting is the wrong instinct here

Two independent reasons, and the second is the decisive one.

- **Value per payer drops faster than conversion does.** Median year-one realized lifetime value per payer is $32 in North America, $25 in Western Europe, $23 globally and $14 in India and Southeast Asia, while median day-35 download-to-paid conversion is 2.6 percent, 2.0 percent and 1.4 percent respectively `[verified]` (RevenueCat 2026, accessed 2026-08-06). Sensor Tower measured the US at more than half of category spend and the UK at about 8 percent `[verified, `market-sizing.md` S2.2]`. Expansion beyond the English-speaking core buys users at materially lower value.
- **Waypoint's product quality is metro-by-metro, not global.** The constraint data (crossing graphs, lighting and populated-area scoring) is built per launch metro `[verified, `mvp-scope.md` GD-3, `stack-recommendation.md` S1]`. Discounting into a market where the safety and crossing layers do not exist sells a degraded product at a reduced price and burns the market. **Regional pricing follows the data footprint, not the other way around.** When Waypoint does enter a purchasing-power-adjusted market, set the price manually, lock the territory against Apple's automatic adjustments (which will otherwise quietly revise a deliberate decision), and review quarterly `[verified as to the lock mechanism, Apple Set a price, above; the review cadence is `[inferred]`]`.

### 5.4 Store-level net revenue differences

The two stores are not interchangeable revenue-wise and should be modeled separately from day one:

| | Apple App Store | Google Play |
|---|---|---|
| Reduced commission | 15 percent under the Small Business Program, under $1M prior-year proceeds. **Enrollment required, effective the following month.** | 15 percent on the first $1M of annual earnings for enrolled developers; some markets moved to 10 percent plus a 5 percent billing fee in 2026 |
| Behavior past $1M | **Cliff:** crossing $1M moves future sales that year and the next to 30 percent | **Graduated:** only revenue above $1M pays the standard rate |
| Billing-error share of cancellations | 15.2 percent | 32.2 percent |
| Median year-one RLTV per payer | $23.38 | $21.62 |

Commission rows `[verified, `api-integration-map.md` S5.2, Apple and Google sources accessed 2026-07-30]`. Billing and RLTV rows `[verified]` (RevenueCat 2026, accessed 2026-08-06). RevenueCat takes roughly 1 percent of gross tracked revenue, about 1.4 percent of net `[verified, `api-integration-map.md` S5.1]`.

Two operational consequences: **enroll in both reduced-commission programs before the first paid transaction**, not after (Apple's takes effect the following month, and enrolling late means paying 30 percent on the earliest and most reputationally important cohort); and **model Android net ARPU below iOS**, both for the RLTV gap and for the structurally higher billing-failure rate, which is a recoverable-revenue problem (grace periods and billing retry should be configured in RevenueCat at launch, not later).

## 6. Revenue phasing

All figures below are models built on stated assumptions, not forecasts. Net revenue means after 15 percent store commission and roughly 1.4 percent of net to RevenueCat, so net is modeled at 84 percent of gross `[inferred arithmetic on verified rates]`.

### 6.1 Months 1 to 9: zero, by design

Revenue: **$0**. Not a shortfall, a decision (DEC-008, `mvp-scope.md` GD-1). The MVP's only job is proving adopt-and-return, and a paywall before that proof contaminates the retention signal that gates the paywall itself.

Costs in this window are small and known: roughly $80 to $130 per month of external services, rising toward $350 to $500 at 10,000 MAU `[verified as estimates, `api-integration-map.md` S8.2]`. The dominant cost is people, which `unit-economics.md` will carry.

Three things must nonetheless happen in this window, all revenue-critical:

1. Enroll in the Apple Small Business Program and the Play 15 percent tier (both require enrollment; Apple's takes effect the following month).
2. Ship the account-creation-date flag that Founding Runner eligibility will depend on (section 4.4).
3. Set the expectation of a future paid layer in launch copy (section 4.3, step 1).

Explicitly rejected for this window: paid presales, founder lifetime deals, crowdfunding of the paid tier, and any "support the build" tip jar. All of them create an obligation before the product is proven and all of them contradict the free-launch decision.

### 6.2 Months 10 to 12: first revenue

Trigger: week-4 retention of route generators clears the healthy-cohort bar, then TS-08 and P-01 ship together (DEC-008).

Model assumptions: cumulative installs at paywall date (A5); first-90-day conversion of the installed base (A6), anchored on the health and fitness download-to-paid median of 2.9 percent and top quartile of 6.2 percent, adjusted upward for a warm base that has used the product for months and adjusted for the finding that freemium apps convert later in the funnel than hard-paywall apps (week-6 conversion share 22.9 percent versus 15.3 percent) `[verified]` (RevenueCat 2026, accessed 2026-08-06). Blended gross ARPU of $72, reflecting Founding Runner dominance in this window plus some monthly mix (A7).

| Scenario | Installs at paywall | 90-day conversion | Subscribers at month 12 | Gross bookings, months 10 to 12 | Net | Exit ARR run rate (net) |
|---|---|---|---|---|---|---|
| Conservative | 6,000 | 2% | 120 | ~$8,600 | ~$7,200 | ~$7,200 |
| Base | 12,000 | 4% | 480 | ~$34,600 | ~$29,000 | ~$29,000 |
| Optimistic | 25,000 | 7% | 1,750 | ~$126,000 | ~$106,000 | ~$106,000 |

Read this correctly. **Bookings are not recognized revenue.** Annual plans collect twelve months of cash up front and recognize monthly, which is excellent for a self-funded runway and is the number to put in front of a seed investor as bookings, clearly labeled. The base case produces roughly $29,000 of net cash inside the 12-month goal window and an exit run rate under $30,000, which is not a business yet and was never going to be. The 12-month goal is "MVP live, thousands of active runners, seed closed or in motion" (`concept.md` S6), and the revenue line's job in that window is to prove that the seam converts at all.

The single most sensitive input is not price and not conversion: it is **installs at the paywall date**, which varies 4x across the scenarios and drives a 15x revenue spread. That makes months 1 to 9 a distribution problem, and pushes the weight onto `gtm-plan.md`.

### 6.3 Year two (months 13 to 24)

Assumptions: both platforms live, list pricing for all new users, P-02 (adaptive routines) arriving during the year to deepen the paid job, and paid acquisition beginning only if unit economics permit (`unit-economics.md` decides this).

The critical and counter-intuitive input is renewal. Category data says roughly 72 percent of annual subscribers cancelled within year one in 2026, worsening from about 56 percent in 2025, with month 1 accounting for about 35 percent of all annual cancellations and a further 9 to 14 percent clustering at month 12 just before renewal; median year-one retention for mid and high-priced annual plans clusters at 23 to 26 percent `[verified]` (RevenueCat 2026 and the accompanying summary, https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/, accessed 2026-08-06). Cancellation here means auto-renew switched off rather than a refund, but the practical read stands: **model annual renewal at 30 percent, not at the 60 to 70 percent that intuition suggests** (A8). Winback is not a rescue: high-priced annual churners reactivate at roughly 4 percent `[verified]` (same source).

| Scenario | Subscribers at month 24 | Blended gross ARPU | Gross ARR | Net ARR |
|---|---|---|---|---|
| Conservative | 1,200 | $85 | ~$102,000 | ~$86,000 |
| Base | 4,500 | $85 | ~$383,000 | ~$321,000 |
| Optimistic | 12,000 | $85 | ~$1,020,000 | ~$857,000 |

Sanity check against Phase 1: `market-sizing.md` puts a well-executed specialist at 70,000 to 300,000 payers and $5M to $30M ARR by year five, with Runna reaching roughly 90,000 payers in three years as the breakout case. Month 24 here is only about 14 months after first revenue, so the base case of 4,500 subscribers is a modest fraction of a Runna-shaped trajectory and the optimistic case requires Runna-class marketing spend and App Store featuring `[inferred]`.

Two notes for the model's edges. The Apple Small Business Program cliff at $1M in proceeds is not a year-two concern in any scenario, but enrollment still must happen in year one. And ARPU rises across year two as Founding Runner mix dilutes, which is the intended shape: the discount is a launch cost, not a permanent price cut.

### 6.4 What the revenue has to cover

Infrastructure is a rounding error at every modeled scale: roughly $350 to $500 per month at 10,000 MAU and $2,000 to $3,500 at 100,000 MAU `[verified as estimates, `api-integration-map.md` S8.2, `stack-recommendation.md` S6]`. In the base case, month-24 net ARR of roughly $321,000 covers infrastructure roughly fifty times over. The business is people-cost-bound and acquisition-cost-bound, not infrastructure-bound, which is why the free tier is affordable and why `unit-economics.md` and `gtm-plan.md` carry more weight than this document does.

## 7. The three risks that would break this model

1. **The paid job may not be felt value.** Training-state-aware generation is the entire paid product at v1.x, and its demand evidence is `[inferred]` from total market absence rather than `[verified]` from anyone paying for it (`unmet-needs.md` need 3, "demand confirmation is interview priority 1"). If runners do not experience "the route should match today's workout" as a want, no price fixes it and the free tier has no paid product above it. Mitigation: interview priority 1 during months 1 to 3, and the workout-route attach rate telemetry signal, both already scheduled. If the seam fails, the fallback is not a price cut, it is to move the paid anchor to adaptive routines (P-02) and accept a later paywall.
2. **Annual renewal is far worse than intuition.** At roughly 30 percent modeled renewal, year-two revenue is driven by new acquisition rather than by a compounding base, which makes the whole model a distribution model wearing a pricing model's clothes.
3. **Revenue starts at month 10, and the calendar has no slack.** Any launch slip pushes first revenue past the 12-month goal, and the seed then has to be raised on retention telemetry alone. The slippage rule in `mvp-scope.md` S7 (cut safety data depth or novelty scope, never the walking skeleton, never add scope to catch up) is a revenue protection rule as much as a product one.

## 8. Open questions for the founder

1. **Do you accept $99.99 per year as list, or do you want to anchor at $119.99 to match Runna and discount harder?** The case for $119.99: it makes the Founding Runner rate look like a bigger gift and leaves headroom. The case against, which this document takes: Waypoint has no brand yet, and pricing at the leader's number invites a comparison it loses on brand.
2. **Is the Founding Runner rate $69.99, or lower?** Every $10 below list costs roughly $4,800 per year in the base case. $59.99 would read as more generous and would sit just above RunGo.
3. **Do you accept giving the Apple Watch app away free**, given that it is 4.0 person-months of build and is the single most obvious paywall candidate outside the coaching layer?
4. **Do you accept the constraint rule (all constraints free forever)?** This is the largest revenue concession in the document and the one most likely to be second-guessed later. If you want an escape hatch, the only clean one is to place *future* constraints invented after v2 (not the ones named in the concept) on the paid side, and that hatch should be decided now rather than improvised.
5. **Which launch metros?** Regional pricing, and the credibility of the safety layer, both follow the data footprint (`mvp-scope.md` open question 3).
6. **Confirm the store offer mechanics before building**: whether a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores, and how RevenueCat offerings should gate eligibility. This is a 30-minute verification that prevents a launch-week surprise.
7. **Do you want the pre-paywall expectation-setting language in the v1 App Store listing** (section 4.3, step 1)? It slightly dampens v1 install conversion in exchange for materially reducing the month-10 takeaway reaction.
8. **Should the "no advertising, no data licensing" rejections be added to the DEC-006 NOT list** as permanent commitments, so they cannot be reopened without a new decision record? Recommendation: yes, and say so publicly, because it is a differentiator that competitors cannot copy without repricing their own businesses.
9. **What is the acceptable floor on paid conversion before the model is declared broken?** Setting this number now, before there is data to rationalize against, is worth more than any pricing decision in this document.

## 9. Assumptions register

- **A1** Running-retail affiliate commission rates were not verified for this document; the affiliate rejection rests on the conflict-of-interest and focus arguments, not on the arithmetic.
- **A2** The 30-generations-per-day anti-abuse soft limit is a placeholder; the real threshold must be set from the 95th percentile of genuine use once telemetry exists.
- **A3** The committed amateur holds at most one or two running subscriptions, making the $149.99 Strava plus Runna bundle an effective ceiling. Carried from `adjacent-platforms.md` A7 via `pricing-matrix.md`.
- **A4** Competitor prices are the 2026-07-30 snapshot in `pricing-matrix.md`. Runna has a history of price changes; re-verify the whole matrix before the paywall ships in month 10.
- **A5** Installs at the paywall date of 6,000 / 12,000 / 25,000 are planning figures with no basis in Waypoint data. This is the single most load-bearing assumption in section 6 and the one the founder is most likely to be able to improve.
- **A6** First-90-day conversion of 2 / 4 / 7 percent adjusts category download-to-paid medians upward for a warm, months-old free base. No direct benchmark exists for "freemium app that was free for nine months then added a paywall".
- **A7** Blended gross ARPU of $72 in months 10 to 12 and $85 in year two assumes Founding Runner dominance early, diluting later, with an annual-heavy mix consistent with the category's 68 percent annual revenue share.
- **A8** Annual renewal modeled at 30 percent, derived from category medians rather than from anything running-specific. Waypoint's compounding personalization is an argument for beating it, but there is no evidence yet.
- **A9** The suggested £89.99 / €99.99 annual targets are working figures to validate against the store-generated grid; they are not derived from local willingness-to-pay research.
- **A10** Net revenue at 84 percent of gross assumes successful enrollment in both reduced-commission programs and roughly 1.4 percent of net to RevenueCat, and ignores the 2026 markets where Google moved to 10 percent plus a 5 percent billing fee (immaterial at modeled scale, material later).
- **A11** The US external-purchase-link position (no commission) is legally unsettled and could reverse; nothing in this model depends on it.
- **A12** RevenueCat and Adapty benchmark data are cross-category medians from subscription-app populations that skew toward apps using those SDKs; they describe the category's shape, not Waypoint's.
- **A13** The RevenueCat 2026 report is internally inconsistent on one point: it describes health and fitness as leading annual adoption at 68 percent in one section and as "monthly-heavy (68 percent)" in another, while Adapty's 2026 report puts health and fitness annual revenue share at 60.6 percent. The direction (annual dominates this category) is consistent across both sources and is what this document relies on.
- **A14** Apple's generated international prices are treated as currency and tax equalization rather than purchasing-power adjustment; sources conflict (section 5.1) and this should be checked empirically against the generated grid before launch.
- **A15** Store introductory-offer eligibility rules are assumed to permit a distinct Founding Runner SKU with its own trial; unverified, and listed as open question 6.
- **A16** All of section 6 assumes the v1.x paywall ships in months 10 to 12 as scheduled under DEC-010. A slip moves every figure right by the slip.

## 10. Sources

**New external sources, all accessed 2026-08-06:**

- RevenueCat, State of Subscription Apps 2026, Health and Fitness edition, https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/
- RevenueCat, State of Subscription Apps 2026, https://www.revenuecat.com/state-of-subscription-apps
- RevenueCat, "The State of Subscription Apps in 10 minutes", https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026/
- Adapty, In-app subscription benchmarks for Health and Fitness apps, https://adapty.io/blog/health-fitness-app-subscription-benchmarks/
- Adapty, State of In-App Subscriptions 2026, https://adapty.io/state-of-in-app-subscriptions/
- Apple, Auto-renewable Subscriptions, https://developer.apple.com/app-store/subscriptions/
- Apple, Manage pricing for auto-renewable subscriptions (App Store Connect Help), https://developer.apple.com/help/app-store-connect/manage-subscriptions/manage-pricing-for-auto-renewable-subscriptions/
- Apple, Set a price (App Store Connect Help), https://developer.apple.com/help/app-store-connect/manage-app-pricing/set-a-price/
- Apple, Communication and promotion of offers on the App Store in the EU, https://developer.apple.com/support/communication-and-promotion-of-offers-on-the-app-store-in-the-eu/
- Strava Metro, https://metro.strava.com/ and case study "The new human-powered era", https://metro.strava.com/case-studies/the-new-human-powered-era
- Foresight Mobile, "App Store Fees 2026: Apple EU Fee Stack and Web-to-App Billing", https://foresightmobile.com/blog/app-store-fees-2026-web-to-app-billing (secondary, medium credibility)
- Funnelfox, "App Store Fees and Commission Rates in 2026", https://blog.funnelfox.com/apple-app-store-fees-2026-eu-dma/ (secondary, medium credibility)
- PTKD Journal, "Why did Apple reject my app under 3.1.1 for an in-app purchase link?", https://ptkd.com/journal/apple-rejection-3-1-1-in-app-purchase-links (secondary, low credibility; used only for the May 2025 guideline change)
- vmobify, "App Price Localisation by Country (PPP Guide)", https://vmobify.com/blog/app-price-localization-ppp (secondary, low credibility)
- AppsOps, "App Store tier pricing vs. custom pricing", https://appsops.store/blog/app-store-tier-vs-custom-pricing (secondary, low credibility)

**Internal sources (each carries its own external citations with 2026-07-30 access dates):**

- `research/02-competitors/pricing-matrix.md`, `gap-analysis.md`
- `research/03-users/personas.md`, `segmentation.md`, `unmet-needs.md`
- `research/01-market/market-sizing.md`, `regulatory-compliance.md`
- `research/04-synthesis/concept.md`, `positioning.md`
- `research/05-product/mvp-scope.md`, `api-integration-map.md`, `stack-recommendation.md`
- `vault/02-Decisions/DEC-006`, `DEC-008`, `DEC-010`

## Related

- `research/06-business-model/unit-economics.md` (CAC, LTV and margin, which consume this document's price points and phasing)
- `research/06-business-model/gtm-plan.md` (owns the installs-at-paywall number that dominates section 6)
- `research/06-business-model/metrics.md` (should carry paid conversion, trial-to-paid, and annual renewal as tracked metrics against the benchmarks cited here)
- `research/05-product/mvp-scope.md` (the feature list the boundary is drawn against)
