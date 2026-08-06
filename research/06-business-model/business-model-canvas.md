# Business Model Canvas

> Version-Timestamp: 2026-08-06 13:10:00 UTC-4
>
> **Status: Phase 6 gate CLOSED 2026-08-06.** All six decisions in section 11 are made and recorded as DEC-011, DEC-012, and DEC-013. Five followed the recommendation; the launch-sequence call was overridden in favor of an iOS-first public launch.

**What this document is.** The integrating artifact for Phase 6. The other four documents in this folder each answer one question in depth: `revenue-model.md` sets price and the free/paid boundary, `unit-economics.md` models whether the arithmetic closes, `metrics.md` defines what gets measured, and `gtm-plan.md` decides how the product reaches people. This canvas holds all nine blocks in one place, states where the four documents agree, and — more usefully — states precisely where they disagree and what the founder has to decide as a result.

**Confidence.** Every block below traces to a source document rather than inventing new claims. Where a figure originates outside Waypoint's research it carries its confidence tag per `00-RESEARCH-PLAYBOOK.md`. Nothing in this canvas is measured; the company has no users. Read it as a coherent hypothesis about how the business works, not a description of how it does work.

**What is locked and not reopened here.** Route-first positioning and the tagline "Know where to run" ([[DEC-006 Concept lock route-first positioning]]). MVP scope, v1 launching entirely free, and safety-aware routing free permanently ([[DEC-008 Phase 5 gate MVP approved stack in validation]]). The Aiven split data architecture with decoupled auth ([[DEC-009 Revised data layer Aiven split architecture with decoupled auth]]). One React Native codebase, iOS at month 9 to 10 and Android 4 to 8 weeks later ([[DEC-010 Staged cross-platform MVP on React Native]]). The NOT list: no social network, no route library, no multi-sport, no plan-quality brand war with Runna.

---

## 1. Customer segments

Phase 3 named the committed amateur as the primary segment. Phase 6 sharpened that into something a solo founder can actually reach, because "committed amateur" is roughly 13 million people in the US alone and contains at least three unrelated acquisition problems (`gtm-plan.md` section 1.1).

| Segment | Role in the business | Evidence |
|---|---|---|
| **Urban committed amateur running from a home doorstep**, three to five times a week, in one metro | **The beachhead.** Both of the strongest-evidenced needs, safety-aware routing and home-turf novelty, are satisfied by deep data about one place | `segmentation.md`, `gtm-plan.md` 1.1 |
| **Women runners inside that group** | Highest-intensity cohort on the safety need. Approached through participation and listening, never a campaign, and never with safety statistics in the copy | `personas.md` (Elena), `gtm-plan.md` 9.1 |
| **Frequent travelers** | **The demo carriers, not the target.** Travel is the most legible activation story and the weakest retention story, because it needs data about everywhere rather than data about one place | Phase 3 reframe, DEC-006 |
| **Ambitious beginners** | Secondary. Served by the free tier being genuinely complete rather than by a cheaper paid tier | `segmentation.md`, `revenue-model.md` 4.1 |

**The geographic dimension is not incidental, it is structural.** Route quality is a function of OpenStreetMap pedestrian data density, which varies enormously between cities, and crossings are documented as the hardest features to map. So coverage is deliberately three-tiered: globally functional for distance, elevation and novelty; two to three metros where the safety layer is actually built; and one beachhead metro that absorbs all human effort. A thin national launch would ship bad routes to most of the country, and a bad route is the single failure mode this product cannot survive (`gtm-plan.md` 1.2, `mvp-scope.md` GD-3).

## 2. Value propositions

**The core:** every training app prescribes workouts without knowing where you are standing, and every route app draws static lines without knowing what your body needs today. Waypoint answers the question both halves ignore: where should I run, right now, from here, for me.

| For whom | The job | Why Waypoint and not the alternative |
|---|---|---|
| Anyone, free forever | Generate a route that fits distance, elevation, start point and round-trip from wherever I am standing | Strava's heatmaps rank by popularity, not by constraints. Komoot and Footpath require manual drawing. Nobody generates against a constraint set |
| Runners in the dark | Route weighted toward lit, populated, well-crossed streets | The strongest-evidenced unmet need in Phase 3, and free permanently by decision, not by tactic |
| Runners bored at home | Streets I have not run, near where I already am | Novelty is a retention driver, and it is the half of the wedge that works without travel |
| Travelers | A trustworthy route in an unfamiliar city in under 30 seconds | Highest activation salience; the reason people first install |
| Paying runners (v1.x) | "Your training, routed": the day's workout turned into the right route | The paid job nobody in the category does at all |

**Two constraints that are part of the value proposition rather than limits on it.** Privacy is architecture: health data never leaves the device, which collapses the GDPR Article 9 server surface and is the reason the product can make claims competitors cannot. And honesty is a feature: "safety-aware" is the ceiling, the product never promises "safe", and it refuses openly when the data will not support a good route. `metrics.md` makes that refusal behavior a monitored guardrail rather than a slogan, which is what stops it from quietly eroding under growth pressure.

## 3. Channels

Ranked by `gtm-plan.md` section 3 on four axes: cash cost, plausible return at Waypoint's scale, time to work, and whether one person can run it while building the product.

| Rank | Channel | Verdict | Year-one plausible return |
|---|---|---|---|
| 1 | Physical run clubs | **Primary**, start month 2. Destroyed by delegation, so it works only while the founder does it personally | 100 to 400 high-intent installs in one metro, plus the beta cohort and interview subjects |
| 2 | Reddit and running forums | **Primary**, start month 1 with four to eight weeks of pure participation and zero promotion | 50 to 300 beta testers; a durable feedback loop |
| 3 | Store optimization | **Mandatory infrastructure**, not growth. Includes the free Featuring Nominations form, which needs three months' lead | The compounding baseline under every other channel |
| 4 | Founder-led build-in-public | **Cheap lottery ticket**, asymmetric payoff | 500 to 3,000 waitlist signups if it lands, zero if it does not |
| 5 | Micro-creators and coaches | **Secondary.** Gifted only until launch, paid only after funding | Strongest post-launch lever once there is something to show |
| 6 | PR and press | **One-shot asset.** Spend it on the Android public launch | One coverage cycle; a credibility artifact for investors |
| 7 | Content and SEO | **Deprioritize.** AI Overviews cut clicks 39.8 to 58 percent and the payback lands past the competitive window | Structurally impaired in 2026 |
| 8 | Paid acquisition | **Do not run pre-funding** | Negative. See the reconciliation in section 10 |

**Run clubs rank first on evidence, not instinct.** New Strava clubs nearly quadrupled in 2025, running clubs specifically grew 3.5x, and club participation rose 59 percent globally over two years [verified, sources in `gtm-plan.md` 3.2]. The channel also solves Waypoint's demo problem: the value is invisible in a screenshot and obvious in ninety seconds standing next to someone.

**The launch is deliberately split.** iOS at month 9 to 10 is a quiet quality burn-in in the beachhead metro; the Android date at month 10 to 12 is the real public launch, because the one-shot assets can only be spent once and a mixed-platform run club is the wrong room in which to tell half the people "not yet". Hard rule already set: if Android is not certified by month 13, the public launch fires on iOS alone within two weeks.

## 4. Customer relationships

| Relationship | How it works |
|---|---|
| **Self-serve product** | Install to first generated route in under three minutes; permissions requested at the moment of value, never at cold launch |
| **Founder-present community** | Run clubs, Reddit, and the beta cohort. The founder is personally visible for the whole of year one, which is both the acquisition channel and the research instrument |
| **Explain, never assert** | Every route carries a checkable "why this route" card. The design principles make explanation and honest degradation mandatory, which is what earns trust in a product that sends people down unfamiliar streets |
| **No social graph** | The NOT list rules out the obvious retention crutch. Retention has to come from the routes being good, which is a harder bet and the honest one |
| **The paywall transition** | Governed by a seven-rule protocol: never take anything away, name the permanent free tier publicly at launch before anyone has paid, grandfather the pre-paywall cohort by name, 30 days' notice, and hold the whole thing behind the week-4 retention bar |

The paid-layer moment is the most dangerous point in the plan and both `gtm-plan.md` section 7 and `revenue-model.md` section 4.4 treat it as such. The relationship risk is specific: a base that has had everything free for months experiences a paywall as a takeaway unless the paywall gates capability that did not exist the day before. The build sequence already supports that, because the paid coaching layer and the paywall ship together.

## 5. Revenue streams

| Stream | Status | Detail |
|---|---|---|
| **Subscription (the only real stream)** | Recommended | **$99.99 per year list**, $12.99 per month, a 36 percent annual discount merchandised as "$8.33 a month". 21-day trial, annual plan only |
| **Founding Runner rate** | Recommended | $69.99 per year, price-preserved indefinitely for the free-era cohort. Emotional payload of a lifetime deal with none of the unfunded liability |
| Lifetime tier | **Rejected** | Health and fitness has the lowest lifetime-plan share of any category, and Waypoint carries real per-user compute cost, so a lifetime plan converts recurring cost into perpetual obligation |
| Second paid tier | **Rejected at v1.x** | Architected for, not shipped |
| Data monetization, location advertising | **Rejected on the record** | Directly contradicts the privacy architecture that is the product's structural advantage |

**The pricing tactic worth remembering:** list high and discount, never the reverse. Apple applies price decreases silently but requires explicit consent from every existing subscriber for increases above roughly 50 percent or $50 a year [verified, `revenue-model.md` 3.5]. Launching at $69.99 and reaching $99.99 later would be a consent-required event across the whole base; launching at $99.99 and discounting is fully reversible.

**Revenue phasing:** zero for months 1 through 9, by design. First revenue lands months 10 to 12 with the paid layer. Year two is where the model is actually tested, and it is a retention problem more than a pricing one.

## 6. Key resources

| Resource | Why it is key | Status |
|---|---|---|
| **The constraint-routing engine** | Self-hosted GraphHopper with custom cost models. The only engine combining a round-trip primitive with cost models that can ingest proprietary data | Decided (DEC-008), beta-flagged custom models are the named risk |
| **The proprietary safety and crossing layer** | The actual moat. Built metro by metro on top of OpenStreetMap, in a self-managed PostGIS store with no personal data in it | Decided (DEC-009). ODbL share-alike boundary needs counsel |
| **The founder** | Product owner, client engineer and routing lead simultaneously, and the top-ranked acquisition channel personally | The binding constraint on everything below |
| **The privacy architecture** | On-device health processing plus EU-resident personal data. Enables claims competitors structurally cannot make | Decided (DEC-009) |
| **The beta cohort and run-club presence** | The only distribution asset that compounds pre-launch | To be built months 2 through 8 |

## 7. Key activities

1. **Making the routes good.** `mvp-scope.md` is explicit that the real MVP risk is bad routes, not missing features. Everything else is downstream.
2. **Building the safety layer metro by metro**, starting with the month-1 buildability spike that doubles as the go-to-market gate (see section 10).
3. **Shipping one React Native codebase to two stores**, with Android's long-lead paperwork started in month 1.
4. **Running the interview program** (12 to 18 conversations by month 4), which is research first and recruitment second.
5. **Being personally present** in run clubs and forums for the whole of year one.
6. **Measuring route quality behaviorally**, since users will rarely rate anything explicitly.

## 8. Key partnerships

| Partner | The trade | First step |
|---|---|---|
| Local run clubs (3 to 6, one metro) | Waypoint generates the club's weekly route; the leader stops drawing by hand | Month 2, attend without pitching |
| Run specialty stores (1 to 3) | Store hosts a club night, Waypoint supplies the route and demo | Month 6, walk in with a route from their own front door |
| Local running coaches (5) | Free lifetime access; they prescribe where athletes run | Month 6, email five named coaches with a route for their usual loop |
| One local half marathon or 10K | Beta recruitment table, not a sponsorship | Month 8 |
| OpenStreetMap local mappers | Contribute pedestrian and crossing data back | Month 3, attend a Mappy Hour as a contributor |
| Women's running groups | Presence and listening only | Month 4, attend and do not pitch |

**Strava is a partner at the product level and never an opponent.** Waypoint feeds Strava and does not compete with it, which is both the right relationship and the only safe one given Strava's API terms and its 2026 AI restrictions. The infrastructure partners are Aiven, Hetzner, RevenueCat, Apple and Google, all decided in Phase 5.

## 9. Cost structure

| Line | MVP scale | 10k monthly actives |
|---|---|---|
| Cost of goods sold (routing VM, Aiven, self-managed PostGIS, external APIs) | $135 to $255 per month | $540 to $770 per month |
| Cost per free active user | — | **under $1 per year** |
| One-time build | **~$230,000 cash**, from ~29 to 31 person-months (DEC-010) | — |
| Revenue-linked | Store commission 15 percent on both small-business tiers, RevenueCat ~1.4 percent of net, ~3.5 percent refund allowance. Net multiplier **0.8088** | Same |
| Operating base at break-even modeling | — | ~$15,000 per month |

**Break-even is roughly 3,000 paying subscribers** at the mid price against a $15,000 monthly base, and roughly 6,800 subscribers held for a year also repays the build. For scale: 3,000 is 3.3 percent of Runna's year-three payer base, so it is reachable. The hard part is the roughly 60,000 monthly actives it implies at a 5 percent conversion rate.

**Infrastructure is not a lever.** It does not make the top five variables in the sensitivity analysis. Anyone optimizing hosting cost here is optimizing the wrong thing.

---

## 10. Where the four documents meet, and where they pull apart

This is the section worth reading twice. Four documents written in parallel will always agree in some places by construction and disagree in others by accident; the disagreements are where the thinking is.

### 10.1 The pricing and distribution decisions are coupled, and the coupling is favorable

`unit-economics.md` headlines that the business clears the conventional 3:1 lifetime-value-to-acquisition-cost bar only at roughly **90 percent organic acquisition** — but that figure is calculated at a $7.99 mid price. `revenue-model.md` independently recommends **$99.99 a year**, which maps to the economics grid's $9.99 column, where base lifetime value rises to $107. Recomputing the break-even organic share at that lifetime value gives **roughly 84 percent**, not 90. [inferred, arithmetic on `unit-economics.md` sections 5.3 and 6.3]

Meanwhile `gtm-plan.md` does not merely lean organic, it **rejects paid acquisition outright pre-funding**, on independent reasoning: a paid install before month 10 has a lifetime value of exactly zero, and it contaminates the retention signal the whole MVP exists to produce. The planned mix is therefore near 100 percent organic, which sits comfortably above the 84 percent the economics require and lands the ratio between 4:1 and 5.6:1.

**The three documents agree, and they agree for different reasons, which is the strongest kind of agreement.** But it makes one dependency explicit and permanent: **Waypoint's unit economics are a function of its distribution strategy, not its pricing.** If the community-first plan fails to deliver, no price in the credible band rescues the model. That is the single most important sentence in Phase 6.

### 10.2 Three conversion numbers with three different denominators

A trap for anyone reading these documents quickly, and worth fixing in the founder's head now:

| Document | The number | The denominator |
|---|---|---|
| `revenue-model.md` A6 | 2 / 4 / 7 percent | of **installs** present at the paywall date |
| `gtm-plan.md` traction table | 4 to 8 percent | of **week-4-retained users** |
| `unit-economics.md` free-tier analysis | 2 / 3 / 5 / 8 percent | of **free active users** |

These are not comparable and must never be quoted side by side to an investor. The GTM figure is the most demanding-sounding and the easiest to hit, because its denominator is already filtered for retention. [inferred]

### 10.3 A mild disagreement on renewal, in the safe direction

`revenue-model.md` plans on roughly 30 percent first-year annual renewal, citing 2026 cancellation data. `unit-economics.md` uses RevenueCat's verified Health and Fitness median of 36 percent as its base case and 24 percent as its pessimistic case. The revenue model is therefore running slightly more conservative than the economics base case, which is the correct direction for two documents to differ in. No reconciliation needed; the founder should simply know the base case is mildly optimistic relative to the category median, which `unit-economics.md` says plainly rather than burying.

Both documents independently flag the same hazard from the same source: AI-branded apps earn about 41 percent more per payer but churn roughly 30 percent faster [verified, RevenueCat State of Subscription Apps 2026]. That is an argument for marketing the utility of the route rather than the intelligence behind it, which is what DEC-006's "Know where to run" already does.

### 10.4 An unresolved contradiction inside the existing plan

`metrics.md` surfaced a genuine conflict that predates Phase 6. Cohort retention — the number the entire MVP exists to produce and the gate for the paid layer — requires a stable per-user identifier over time. TelemetryDeck, the analytics vendor already selected in `../05-product/api-integration-map.md`, deliberately does not provide one, which is precisely why it needs no consent banner. **So the PRD's privacy-preserving analytics choice does not deliver the retention metric the PRD's own goals require.** The proposed resolution keeps cohort retention in a first-party Postgres event table keyed on the account identifier already held for sync: no new vendor, no new consent basis, a handful of hand-built SQL views. This needs a founder decision at the gate (card 3 below).

### 10.5 Two Phase 5 targets that should be re-based

`metrics.md` recommends re-basing PRD goals G3 and G4. G4's 25 percent day-30 retention, measured at install level, would place Waypoint far outside the top decile of the entire Health and Fitness category in its first month against every published benchmark. It works as an **activated-cohort** target, paired with a separate 8 to 12 percent install-level line for benchmark comparison. This is a correction to Phase 5, not a Phase 6 finding, and it should be applied to the PRD rather than left as a discrepancy between two documents.

### 10.6 The largest open revenue question

`revenue-model.md` draws the free/paid boundary generously: everything in MVP v1 free forever, **plus** every remaining routing constraint (crossings, weather, surface), **plus** the Watch app, GPX export, and the preference-learning loop. The paid tier is the coaching layer alone. The document names this as its own largest revenue concession and asks for the escape hatch to be decided now rather than improvised in v2. It is a real decision with a real cost, and it is gate card 2.

---

## 11. Gate outcome (decided 2026-08-06)

All six closed. Five followed the recommendation; one was overridden.

| # | Decision | Outcome |
|---|---|---|
| 1 | Price | **Approved as recommended.** $99.99/yr list, $12.99/mo, 21-day annual-only trial, Founding Runner at $69.99/yr price-preserved. [[DEC-011 Pricing and the permanent free tier]] |
| 2 | Free/paid boundary | **Approved as recommended, escape hatch declined.** All routing constraints, the Watch app, and GPX are free forever; the coaching layer alone is paid; the free tier is named publicly at launch. DEC-011 |
| 3 | Analytics identity | **First-party Postgres cohort table** on the existing account identifier. TelemetryDeck keeps aggregate signals; PostHog EU deferred to v1.x. [[DEC-012 Measurement corrections analytics identity and re-based targets]] |
| 4 | PRD goals G3 and G4 | **Re-based** to activated-cohort definitions with a separate install-level benchmark line. Activation redefined as a completed recorded run. DEC-012 |
| 5 | Beachhead metro | **Founder's home metro**, subject to the month-1 pedestrian-data spike. [[DEC-013 Home-metro beachhead and iOS-first public launch]] |
| 6 | Which date is the real launch | **OVERRIDDEN: the iOS date at month 9 to 10 carries the public launch**, not the Android date. DEC-013 records the reasoning and the compensating conditions |

### Why the launch override is defensible, and what it costs

The recommendation favored Android because a mixed-platform run club is a bad room in which to tell half the people "not yet", and because four to eight quiet iOS weeks would buy a rating and route-quality burn-in before the loud moment. Three things outweighed it: the **Apple featuring nomination is iOS-only** and cannot be spent on an Android launch, which the plan underweighted; **speed is a business requirement** in a 12 to 18 month window the build already consumes ten months of; and **iOS carries roughly 85 percent of category subscription revenue**, so the audience whose behavior decides the paid layer is reached sooner.

The cost is that the quiet burn-in disappears, and it was absorbing three real risks. DEC-013 converts each into a commitment: the beta cohort's month-8 target of 150 to 300 testers becomes a **hard gate on the launch date** rather than a milestone, since it now carries the route-quality load alone; reviews are seeded from the beta cohort with crash-free sessions above 99.5 percent as a release gate; Android runners met in person go onto a waitlist from launch onward; and the featuring nomination is filed at month 6 to 7.

## 12. Assumptions and open questions carried forward

- **A1 (highest risk in the whole phase).** That the beachhead metro clears the OpenStreetMap pedestrian-data floor. It sits underneath the segment choice, the metro choice, the top-ranked channel, and the differentiation claim. The month-1 buildability spike answers it before any marketing effort is committed, which is why **that spike should be treated as a go-to-market gate and not merely a technical one.**
- Installs present at the paywall date (6k / 12k / 25k) drive a 15x revenue spread and are pure planning figures. This number matters far more than price or conversion.
- Whether a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores. A 30-minute check in App Store Connect and Play Console that prevents a launch-week surprise.
- Organic cost per subscriber ($12 base) **excludes founder time**, which is a deliberate understatement and must be disclosed alongside any LTV/CAC figure shown to an investor.
- The paid job itself is the deepest unknown: training-state-aware generation is the entire paid product, and its demand evidence is inferred from the category's total absence of it rather than verified from anyone paying for it.

## Related

- `revenue-model.md`, `unit-economics.md`, `metrics.md`, `gtm-plan.md`
- `../05-product/mvp-scope.md`, `../05-product/api-integration-map.md`
- `../04-synthesis/concept.md`, `../04-synthesis/positioning.md`
- [[DEC-008 Phase 5 gate MVP approved stack in validation]], [[DEC-009 Revised data layer Aiven split architecture with decoupled auth]], [[DEC-010 Staged cross-platform MVP on React Native]]
