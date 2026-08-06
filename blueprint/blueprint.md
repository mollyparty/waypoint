# Waypoint: Business Blueprint

> Version-Timestamp: 2026-08-06 14:00:00 UTC-4
> Status: Draft for founder review. Investor-facing HTML edition: `blueprint/index.html`.

**Know where to run.**

---

## How to read this document

This blueprint packages eight phases of research into one investor-facing argument. It invents nothing. Every figure traces to a document in `research/`, every external claim carries a publisher and an access date, and every number carries a confidence tag: **[verified]** traces to a credible source, **[inferred]** is reasoned from verified inputs with the reasoning shown, **[assumption]** is an unvalidated working belief.

**The disclosure that belongs at the top, not buried in an appendix.** Waypoint has no users, no code in production, and has conducted **zero user interviews**. Everything here is desk research plus reasoning. The personas are assembled from published surveys and competitor review mining, not from conversations. The financial model is directional. Section 16 lists what would have to be true, what we do not know, and the 90-day plan to find out. An investor who reads only the executive summary and section 16 will have an honest picture.

---

## 01 · Executive summary

**In one sentence:** every training app tells runners what workout to do without knowing where they are standing, and every route app draws static lines without knowing what the runner's body needs today, and nobody in a fifteen-product market answers the question runners actually ask, which is *where should I run, right now, from here.*

Waypoint is a mobile running app that generates a route on demand against a constraint set: distance, elevation, round-trip from your current position, street crossings, surface, weather, time of day, and how lit and populated the streets are. Coaching layers on top of that later. The atomic unit is the route, not the training plan.

### Why this is a company and not a feature

Three things have to be true at once, and the research says all three are.

**The gap is verified, not assumed.** Fifteen-plus products were profiled across the market. Zero of them accept safety, lighting, weather, or street crossings as routing inputs. Zero of them connect a runner's training state to route choice. The coaching apps (Runna, TrainAsONE, Coopah, AI Endurance) have no routes at all. The route apps (Komoot, AllTrails, Footpath, RunGo) have no training context. Strava is the only major on-demand generator and it ranks by popularity, which is a different and occasionally dangerous thing. [verified, `research/02-competitors/feature-matrix.md`]

**The need has real evidence behind it.** The strongest-evidenced unmet need is safety-aware routing: 54 percent of runners report changing their routes for safety reasons, 42 percent say their routine is dictated by safety, and 82 to 92 percent hold safety concerns. The second strongest is route novelty at home, evidenced by CityStrides' 90,000-plus users paying to track streets they have not yet run. [verified, `research/03-users/unmet-needs.md`]

**The category pays.** Runna reached roughly 90,000 paying members by April 2025, its third year, and was acquired by Strava. Strava itself has 180 million-plus registered users and revenue reported between $415 million and roughly $500 million ARR, at a $2.2 billion valuation. Komoot, with 45 million users, went to Bending Spoons the month before. Health and fitness is the only app category where annual plans still dominate, at 60.6 percent of revenue. [verified, `research/01-market/market-landscape.md`]

### The honest version of the size question

**Hypothesis H5, that the addressable market is venture-scale, came back UNCERTAIN.** The route-generation wedge alone models to $5 million to $30 million in ARR by year three to five. That is a strong business. It is not, on its own, a venture outcome. The venture case requires a credible expansion story past the initial wedge, and this document argues one in section 03 rather than hiding the finding. Any investor conversation that skips this is a conversation that ends badly later. [inferred, `research/01-market/market-sizing.md`]

### The numbers that matter

| | |
|---|---|
| **Price** | $99.99 per year list, $12.99 per month. Only the coaching layer is paid; routing, safety constraints, the Watch app and GPX export are free permanently |
| **Break-even** | ~3,000 paying subscribers, which is 3.3 percent of Runna's year-three payer base |
| **Build cost** | ~$230,000 cash, from 29 to 31 person-months across a founder plus two contractors |
| **Time to launch** | iOS public launch at month 9 to 10, Android 4 to 8 weeks later, from one React Native codebase |
| **Competitive window** | 12 to 18 months before Strava could ship a shallow version; roughly 24 months before anyone could match the constraint depth |
| **The one constraint that governs everything** | Unit economics are a function of distribution, not pricing. Paid acquisition returns 53 to 70 cents on the dollar at every credible price, so the model needs roughly 84 percent organic acquisition to work |

### What the money buys

The pre-seed requirement derives to roughly **$350,000 to $400,000**: about $230,000 to reach a dual-platform launch, plus six to nine months of runway past it at roughly $15,000 a month to prove week-4 retention and test the paid layer. This is a derived figure, not yet a decided ask. [inferred, section 13]

---

## 02 · The problem

### The question nobody answers

A runner opens an app. The app says: today is a 45-minute easy run. The runner is standing in a hotel lobby in a city they have never visited, or on their own doorstep for the four-hundredth time, and the app has nothing more to say. Where the run should physically go is left entirely to the human, every single day.

The workarounds are visible and they are all bad. Runners hand-draw routes in Footpath. They ask Reddit the night before a trip. They run the same three loops until they are bored enough to stop. They pay for Great Runs and similar curated-route cottage industries. They scroll Strava heatmaps and hope popularity is a proxy for suitability. Decades of forum threads document the same question being re-asked. [verified, `research/03-users/unmet-needs.md`]

### Three distinct failures, one root cause

**The training apps do not know where you are.** Runna, TrainAsONE, Coopah and AI Endurance all build sophisticated adaptive plans and then hand the runner a duration and an intensity. Location is not a variable in any of them. [verified]

**The route apps do not know what your body needs.** Komoot and AllTrails are excellent at planning, and both are designed around a different activity: Komoot is cyclist-first, AllTrails is trail-locked. Footpath and RunGo execute routes well but generate nothing. None of them know that today is a recovery day. [verified]

**Everyone ignores the constraints that actually decide a route.** This is the load-bearing finding. Across the whole market, the rows for *weather as a routing constraint*, *street crossings*, and *safety as a constraint* are empty. Not weak. Empty. Runna and TrainAsONE adjust your target *pace* for heat; neither considers routing you somewhere shaded. Nobody prefers streets with fewer crossings so an interval session is not interrupted every 200 metres. Nobody weights toward lit and populated streets at 6 a.m. in January. [verified, `research/02-competitors/feature-matrix.md`]

### Why safety is the sharpest edge of it

The evidence here is stronger than for anything else in the research, and it is quantified: 54 percent of runners have changed a route for safety reasons, 42 percent say safety dictates their routine, and 82 to 92 percent report holding safety concerns. There is peer-reviewed work behind it, and there are verified incidents of Strava's popularity-ranked routes sending runners somewhere they should not have gone. [verified, `research/03-users/unmet-needs.md`]

It is also the highest-liability surface in the product, which is precisely why no incumbent has touched it. Waypoint's answer is a discipline rather than a disclaimer: the product says **safety-aware**, never *safe*. It never promises. It names the data behind every claim and its limits, and when the data will not support a good route it says so out loud instead of inventing one. That rule is enforced in continuous integration by a banned-terms lint, not left to copywriting judgment. [verified requirement, `research/05-product/prd.md` section 5.4]

---

## 03 · Market opportunity and sizing

### The layers

| Layer | 2025 size | Growth | Confidence |
|---|---|---|---|
| Fitness apps overall | $12.12B | 13.4% CAGR to $33.58B by 2033 | [verified] Grand View Research |
| Health and fitness apps (subscription-weighted) | ~$6.0B, up 17.7% YoY, ~80% subscriptions | — | [verified] Business of Apps |
| **Running apps (the category)** | **~$1.5B**, published estimates clustering $1.3B to $2.9B | **11% to 14% per year**, toward $3B to $5B by the early 2030s | **[inferred]** |

**A word on that TAM, because it deserves one.** The only category-exact figures come from syndicated report mills with undisclosed methodology, and they disagree with each other by more than a factor of two. Cross-checked against observable company revenue, the bottom-up view of running-adjacent app revenue is roughly $0.6 billion to $1.0 billion today. The research deliberately weights the observable-revenue cross-check over the report mills, which is why the working figure sits at the low end of the published range. An investor should treat any running-app TAM quoted with more precision than this as unearned. [inferred with stated method, `research/01-market/market-sizing.md`]

### Participation is growing, with a caveat that matters

Global running participation went from 672 million in 2022 to roughly 785 million in 2025, with Gen Z runners rising from 186 million to 259 million [verified, GWI]. In the US, 52.3 million people ran on roads in 2025, up more than a million year over year, and trail running is up 57 percent since 2019 [verified, Outdoor Industry Association 2026 Running Report]. In England, roughly 7.1 million adults ran in the 12 months to November 2025, up more than half a million in a year [verified, Sport England].

**The caveat, stated because it cuts against us.** The same OIA report notes that growth is coming from casual, lower-frequency runners while *"the dedicated core has softened."* Waypoint's primary segment is the dedicated core. The tailwind is real but it is not blowing directly on our target. [verified caveat, read-through inferred]

### SAM

Roughly **14 million committed amateur iOS runners** across the US, UK, EU-27, Canada and Australia. Built bottom-up: roughly 110 million runners across those geographies, narrowed by an assumed 25 percent who run three to five times a week, times a weighted 50 percent iOS share. [inferred, with the 25 percent flagged as an assumption]

In money, that is a **$1.4 billion theoretical ceiling** at $100 a year, against **$150 million to $300 million of demonstrated willingness to pay**, using the 10 to 15 percent of committed runners who actually pay for a running subscription. The anchor is RevenueCat's verified median download-to-paid rate of 2.7 percent for health and fitness, with a top decile of 12.1 percent. [inferred]

### SOM, and the uncertain verdict

**70,000 to 300,000 paying subscribers by year three to five, which is $5 million to $30 million in ARR, or about 1 to 2 percent of SAM.** Benchmarked against Runna at roughly 90,000 payers in year three. Bottom-up and top-down agree at this level, which is the one place in the sizing work where two methods converge. [inferred]

**This is where hypothesis H5 came back UNCERTAIN, and the reasoning is worth stating in full.** A $5 million to $30 million ARR business built on the route wedge alone is a genuinely good outcome for a founder. It is not a venture outcome. The honest venture case therefore rests on expansion, and there are four credible directions, each of which the research can size or at least bound:

1. **Android**, already in the MVP by decision, roughly doubles the addressable population versus the iOS-only SAM.
2. **Non-English geographies**, where the constraint-routing problem is identical and the incumbents are weaker.
3. **The coaching layer**, which is where the revenue is and which puts Waypoint into the same wallet Runna already proved.
4. **Outdoor navigation adjacency**, the Komoot and AllTrails surface, reachable because the routing engine is activity-agnostic even though v1 deliberately is not.

**What would move H5 from uncertain to supported:** Runna passing 500,000 payers, published AllTrails Peak attach rates, validated non-English expansion, or an observed payer share above 15 percent. These are the specific tests, named in the research before we knew whether we would like the answers. [verified as stated tests]

### The structural tailwind that is genuinely ours

Apple's Foundation Models framework, shipped with iOS 26, puts a 3-billion-parameter model on the device at **zero inference cost**, working offline. For a product whose coaching narration would otherwise be a per-user API bill, this converts a variable cost into a fixed one and makes a privacy claim structurally true rather than merely promised. The hardware floor is iPhone 15 Pro and above. [verified, Apple WWDC25]

---

## 04 · Competitive landscape

### The field

| Product | What it is | Price |
|---|---|---|
| **Runna** (Strava-owned) | Category-leading adaptive plans. No route generation | $119.99/yr; Strava+Runna bundle $149.99/yr |
| **Strava** | Social tracking hub; the only major on-demand route generator, ranked by popularity | $79.99/yr |
| **TrainAsONE** | AI-adaptive plans, rebuilt after every run. Zero route capability | £99.00/yr |
| **AI Endurance** | Neural-net plan optimization plus an LLM chat coach. No routes | ~$155.88/yr |
| **Coopah** | Adaptive plans with a human coaching layer. No location features | $79.99/yr |
| **Joggo** | Quiz-funnel beginner plans, shallow engine | ~$93.99 to $99.99/yr |
| **Komoot** (Bending Spoons) | Europe-leading outdoor route planning. Cyclist-first | €59.99/yr |
| **AllTrails** | Trail discovery, with AI route *adjustments* rather than generation | Peak $79.99/yr |
| **Footpath** | Manual route drawing and navigation. No generation | $23.49/yr |
| **RunGo** | Static route library with voice navigation. No generation | $59.99/yr |
| **Garmin Connect+** | AI insights over free Garmin Coach plans, watch-locked | $69.99/yr plus hardware |
| **Apple Fitness+ / Workout Buddy** | OS-level fitness; Workout Buddy is motivational, not prescriptive | $79.99/yr |
| **Nike Run Club** | Free static plans and audio. Effectively in maintenance | Free |

### What the matrix shows

Plot every product on two axes, route intelligence and training intelligence, and the top-right quadrant is empty. Coaching apps cluster high-left. Route apps cluster low-right. Strava sits mid-low on training and highest among incumbents on routing, and it is the only product with a foot in both. Waypoint's planned position is the empty corner. [verified, `research/02-competitors/positioning-map.md`]

The specific empty rows, which is the more useful way to say it: **weather as a routing constraint, street crossings, and safety as a constraint are empty across the entire market.**

### The threat, stated as plainly as it deserves

**Strava connecting Runna's plan engine to its own route generation is the kill shot.** Strava owns every piece: the only shipping generator, a heatmap built on more than 10 billion activities, the leading coaching app since April 2025, and a $149.99 bundle already marketed with the words *"personalized routes linked to your training plan."*

Assessed likelihood of Strava shipping a shallow version, meaning popularity-ranked routes attached to plans, is **50 to 60 percent within 18 months** [assumption, analytical judgment]. Likelihood of them matching full constraint depth, meaning weather, crossings, safety and surface, is **20 to 30 percent** [assumption], because that is niche, liability-adjacent work for a multi-sport platform with a much larger business to protect.

**And part of that window has already closed.** Strava launched Instant Workouts globally in January 2026, attaching heatmap-generated routes to suggested workouts. The shallow version effectively exists. Waypoint's differentiation therefore cannot be *"they don't link workouts to routes"* — it has to be constraint depth and personalization, which is what this plan actually builds. This correction is recorded in `research/04-synthesis/positioning.md` rather than quietly dropped.

**Working window: 12 to 18 months to launch something defensible, and roughly 24 months before constraint depth could be matched.** The build consumes 9 to 13 of those months, which is the single most uncomfortable fact in this document and the reason the timeline is not padded.

### Why the incumbents' own rules help us

Strava's API terms **ban AI use of its data**, and Garmin has **paused new Connect Developer Program applications**. Waypoint therefore cannot and does not depend on incumbent data. It is HealthKit-first by necessity, and the moat has to live in proprietary context data: the crossing graph, safety scoring, and micro-weather. That is a harder build and a better business, because it is the one asset an incumbent cannot acquire by changing an API term. [verified]

---

## 05 · The product

### Positioning, locked

> **For committed amateur runners who never quite know where today's run should go, Waypoint is the running app that generates the right route for you, right now, from wherever you stand** — because it is the only product that treats safety, weather, street crossings, surface, distance, and your training state as routing inputs rather than afterthoughts.

Tagline: **"Know where to run."** This replaced "Your AI Running Coach", deliberately. Category data shows AI-branded apps earn about 41 percent more per payer but churn roughly 30 percent faster, so the brand markets the utility of the route rather than the intelligence behind it. [verified, RevenueCat 2026; decision recorded in DEC-006]

### The MVP: 15 features, and what they are for

Scored at 22.75 person-months plus roughly 2 months of release overhead.

**The wedge itself**
- **H-01 Core route generation.** Constraint-based, round-trip from any start point. The product.
- **H-02 Elevation constraint.** Flat when you want flat, hills when you want hills.
- **H-05 Safety-aware routing v1.** Weighting toward lit and populated streets. The strongest-evidenced need, and free permanently.
- **H-07 Route novelty.** Streets you have not run, near where you already are. The half of the wedge that works without travel.
- **H-08 Travel mode.** Not a separate engine: the same generator with zero-configuration defaults and offline resilience. It is the activation story.
- **H-09 Honest degradation.** When the data will not support a good route, say so. Refusing well is a feature.

**Execution, because a route you cannot follow is not a route**
- **X-01 Voice turn-by-turn navigation.** Generation plus execution in one product is itself a gap: Footpath and RunGo execute but do not generate.

**Table stakes, because their absence would disqualify the app**
- TS-01 GPS tracking · TS-02 run history · TS-03 HealthKit sync · TS-04 onboarding · TS-05 audio cues · TS-06 route save and re-run · TS-07 Strava share

**Obligation**
- O-01 Privacy, consent and AI disclosure.

### What ships after, and what never ships

**Fast-follow, 30 to 120 days post-launch (~17 person-months):** the Watch app, GPX export, remaining routing constraints (crossings, weather, surface), the preference-learning loop, and the paid coaching layer.

**Never, and this list is locked (DEC-006):** no social network — Waypoint posts *to* Strava and does not compete for the social graph. No route content library — generate, do not curate. No multi-sport in v1. No hardware. No plan-quality brand war with Runna. No charging for basic loop generation.

The NOT list is doing real work. It is what keeps a solo founder's MVP at 15 items instead of 40, and it is what makes the paid tier nameable.

### The design rules that are not negotiable

- **Explain, never assert.** Every route carries a checkable "why this route" card.
- **Honest degradation everywhere.** Never fake confidence.
- **Safety-aware, never safe.** Six binding language rules, enforced by a banned-terms lint in CI.
- **Private by default.** Privacy zones, start-point obfuscation before anything leaves the device.
- **Accessible from the first sprint.** WCAG 2.2 AA and EN 301 549, not retrofitted.

---

## 06 · Who it is for

### The beachhead

Not "committed amateurs", which is roughly 13 million people in the US alone and contains at least three unrelated acquisition problems. The beachhead is **the urban committed amateur who runs three to five times a week from a home doorstep, in one metro**, with women runners as the highest-intensity cohort inside that group.

**Why one metro is structural and not timid.** Route quality is a function of OpenStreetMap pedestrian data density, which varies enormously between cities, and street crossings are documented as the hardest features to map. Coverage is therefore deliberately three-tiered: globally functional for distance, elevation and novelty; two to three metros where the safety layer is actually built; and one beachhead metro that absorbs all human effort. A thin national launch ships bad routes to most of the country, and a bad route is the one failure mode this product cannot survive.

### The four personas

| Persona | Who | The job |
|---|---|---|
| **Marcus** — committed amateur racer (core) | Runs 4x a week around a job and family, races a spring half and a fall marathon, bored of three loops, self-coaches with apps | Tell me today's workout *and* where to do it, keep me injury-free, make the daily decision effortless |
| **Priya** — traveling professional (sharpest case) | Consultant in a different city each week, mid marathon block, 6 a.m. in a hotel lobby with miles to run | Answer "where do I run, right now, from here", keep the plan intact while traveling, keep me safe in an unknown city |
| **Elena** — safety-first city runner | Plans every run around daylight, lighting and escape routes before pace | Find a route where I will feel and be safe at this hour, widen my world past two proven loops, never expose where I live |
| **Jake** — ambitious beginner (secondary) | Nine months in via a run club, first half on a dare, motivated and injury-prone | Finish uninjured, tell me what "easy" actually means, do not make me feel slow |

**These are desk personas.** Assembled from published surveys and mined competitor complaints, with no Waypoint interviews behind them. Section 16 makes fixing that the first item of work.

### The reframe that changed the strategy

The founder's original hypothesis (H1) was that travel friction drives adoption. Research came back **partially supported, and reframed.** The travel question is constant and demonstrably monetized by workarounds, but those workarounds usually succeed within 15 or 20 minutes, and travel is episodic. You cannot retain a user on a problem they have six times a year.

So: **travel is the activation moment and the demo; safety plus novelty at home is the daily retention wedge.** This changed which features are load-bearing and which metro strategy is correct, and it is why H-05 and H-07 are in the MVP while a richer travel mode is not. Correcting the founder's own hypothesis early is the most valuable thing the research did.

---

## 07 · Business model and pricing

### The structure

| Item | Decision |
|---|---|
| **Annual** | **$99.99/year**, merchandised as "$8.33 a month, billed annually" |
| **Monthly** | $12.99/month |
| **Trial** | 21 days, annual plan only |
| **Founding Runner** | **$69.99/year, price-preserved indefinitely** for everyone who joined during the free era |
| **Lifetime tier** | Rejected |
| **Data or location monetization** | Rejected on the record |

### Where the paywall sits, which is further out than most would put it

**Free forever:** all route generation, every routing constraint including the safety layer, the Watch app, GPX export, run tracking, HealthKit sync, Strava posting, and the preference-learning loop.

**Paid:** the coaching layer alone. One nameable job — *your training, routed.*

This is the most aggressive concession in the plan and it was made deliberately, with the escape hatch explicitly declined. The reasoning: the permanent free tier gets **named publicly at launch, before anyone has paid anything**. Promising it later, at the moment the paywall appears, reads as damage control. A paywall that gates capability which did not exist the day before is an announcement; a paywall that closes doors that were open yesterday is a betrayal. The build sequence supports the former, because the coaching layer and the paywall ship together.

### Why $99.99 and not less

It sits 17 percent under Runna's $119.99 while doing something Runna cannot do at all, a third under the $149.99 assembled Strava-plus-Runna alternative, and clearly above the utility band where Footpath ($23.49) and Komoot (€59.99) live.

**The counterintuitive support:** higher-priced apps in this category convert *better* at the download-to-paid step, 2.8 percent in the high band against 1.4 percent in the low, and generate roughly six times the year-one lifetime value per payer. Nothing in the data supports discounting into the utility band to buy conversion. [verified, RevenueCat]

**The tactical rule:** list high and discount, never the reverse. Apple applies price *decreases* silently, but increases above roughly 50 percent or $50 a year require explicit consent from every existing subscriber, and non-consenting subscriptions simply expire. Launching low and raising later would be a consent event across the entire base. Discounts and regional pricing stay fully reversible. [verified]

### Why not lifetime

Health and fitness has the lowest lifetime-plan share of any app category while leading in annual adoption, and route generation carries genuine per-user compute cost. A lifetime plan converts a recurring cost into a perpetual unfunded obligation. The Founding Runner rate delivers the same emotional payload with none of the liability, and both stores support price preservation operationally.

### The risk this creates, named

The paid product now rests entirely on one job. If training-state-aware generation turns out not to be felt value, there is no second paid thing at v1.x to fall back on. Its demand evidence is **inferred from the category's total absence of it**, not verified from anyone paying for it. That is the deepest unknown in the business, and no price fixes it.

---

## 08 · Unit economics

Directional. Modeled across a $4.99 to $11.99 monthly-equivalent band.

### Margins and break-even

| | MVP scale | 10k monthly actives | 100k | 1M |
|---|---|---|---|---|
| Gross margin per subscriber | Negative | **63%** | 78% | 84% |
| Infrastructure | $135 to $255/mo | $540 to $770/mo | — | — |

Margin is negative at MVP scale for an unremarkable reason: a roughly $195 monthly infrastructure floor spread across roughly 30 payers exceeds net revenue per subscriber. It resolves with scale, not with optimization.

**Break-even: roughly 3,000 paying subscribers** against a $15,000 monthly operating base. Roughly 6,800 subscribers held for a year also repays the build. For scale, 3,000 is **3.3 percent of Runna's year-three payer base**. The hard part is not the 3,000; it is the roughly 60,000 monthly actives it implies at a 5 percent conversion rate.

**Net revenue multiplier: 0.8088**, after the 15 percent small-business store commission on both platforms, RevenueCat at roughly 1.4 percent of net, and a 3.5 percent refund allowance.

### The free tier costs less than people assume

**A free active user costs under $1 per year** in infrastructure. In absolute terms, "free users are expensive" is simply false here.

What bites is revenue *share*. The free base consumes 55 percent of net subscription revenue at 2 percent conversion, 36 percent at 3 percent, and becomes a rounding error above roughly 5.3 percent. The generous free tier is therefore a conversion bet, not a cost problem.

### The finding that governs the whole business

**Paid acquisition does not work at any price in the credible band.** A roughly $4.00 category cost per install divided by a 2.5 percent download-to-paid rate gives roughly **$160 per acquired subscriber**, against a lifetime value of $86 to $107. That is 53 to 70 cents returned on the dollar.

**Which means the model clears a 3:1 lifetime-value-to-acquisition-cost bar only at roughly 84 percent or better organic acquisition.** Pricing at $99.99 rather than a $7.99 mid case is what brings that requirement down from about 90 percent, so price and distribution are coupled — favorably, but tightly.

The go-to-market plan in section 09 independently rejects paid acquisition, for a different reason: a bought install before month 10 has a lifetime value of exactly zero and contaminates the retention signal the entire MVP exists to produce. **Two documents reached the same conclusion from different directions, which is the strongest form of agreement.** But it makes the dependency permanent: **if community-first distribution fails, no price rescues the model.** That is the single most important sentence in this blueprint.

### What actually moves the outcome

In order: **organic share of acquisition** (an 8.4x swing in blended acquisition cost), **free-to-paid conversion**, then **annual first-renewal rate**. Price is a distant fourth. Infrastructure cost does not make the top five, so anyone optimizing hosting here is optimizing the wrong thing.

The uncomfortable interaction between the top two: the generous free tier that keeps acquisition cost low is the same thing that suppresses conversion.

### Renewal, and a category hazard

The model runs on RevenueCat's verified 36 percent Health and Fitness median first-year annual renewal as its base case, with 24 percent as the pessimistic case. The revenue plan independently assumed roughly 30 percent, which is the safe direction for two models to differ in.

**The hazard both flagged from the same source:** AI-branded apps earn about 41 percent more per payer but churn roughly 30 percent faster. This is a direct argument for the brand decision in section 05.

### One measurement warning for anyone reading the source documents

Three different conversion rates appear across the research with **three different denominators**: percent of *installs at the paywall date*, percent of *week-4-retained users*, and percent of *free active users*. They are not comparable and must never be quoted side by side.

---

## 09 · Go-to-market

### The budget this has to fit inside

The founder is 1.0 FTE within a 2.5 to 3.0 FTE team and is simultaneously the product owner, the client engineer and the routing lead. Go-to-market gets 3 to 4 hours a week in months 1 to 3, rising to 15 to 25 hours in the launch window, on a cash budget from $0 to $800 a month. Every channel below is filtered through that.

### Channels, ranked

| Rank | Channel | Verdict | Year-one plausible return |
|---|---|---|---|
| 1 | **Physical run clubs** | Primary, from month 2 | 100 to 400 high-intent installs in one metro, plus the beta cohort and interview subjects |
| 2 | **Reddit and running forums** | Primary, from month 1, with 4 to 8 weeks of pure participation and zero promotion first | 50 to 300 beta testers, and a durable feedback loop |
| 3 | **Store optimization** | Mandatory infrastructure, not growth | The compounding baseline under everything else |
| 4 | Founder-led build-in-public | A cheap lottery ticket, asymmetric | 500 to 3,000 waitlist signups if it lands, zero if it does not |
| 5 | Micro-creators and coaches | Secondary. Gifted only until launch | The strongest post-launch lever |
| 6 | PR and press | A one-shot asset | One coverage cycle, plus a credibility artifact |
| 7 | Content and SEO | **Deprioritize** | Structurally impaired: AI Overviews cut clicks 39.8 to 58 percent, and payback lands past the competitive window |
| 8 | Paid acquisition | **Do not run pre-funding** | Negative, per section 08 |

**Run clubs rank first on evidence.** New Strava clubs nearly quadrupled in 2025 to one million total, running clubs specifically grew 3.5x, and club participation rose 59 percent globally over two years [verified, Strava Year in Sport 2025 and the Running Industry Association]. The channel also solves Waypoint's specific demo problem: the value is invisible in a screenshot and obvious in ninety seconds standing next to someone. There is a partnership angle too, since somebody in every club currently draws the weekly route by hand.

### The launch

**iOS at month 9 to 10 is the public launch**, carrying the one-shot assets: press, creators, Product Hunt, and the Apple featuring nomination. Android follows 4 to 8 weeks later as a second, smaller moment.

This overrode the research recommendation, which favored holding the loud moment for the Android date so a mixed-platform run club would not hear "not yet" from half the room. Three things outweighed it: the **Apple featuring nomination is iOS-only** and cannot be spent on an Android launch, **speed matters** inside a window the build already consumes most of, and **iOS carries roughly 85 percent of category subscription revenue**, so the audience whose behavior decides the paid layer is reached sooner.

**The override costs the quiet burn-in period, which was absorbing three risks, so four conditions are attached and they are commitments rather than intentions:**
1. The month-8 beta cohort target of 150 to 300 active testers becomes a **hard gate on the launch date**, because it now carries the entire route-quality load alone. If the beta is thin, the launch slips.
2. Reviews are seeded from the beta cohort at launch, with crash-free sessions above 99.5 percent as a release gate.
3. Android waitlist capture starts at every in-person event from launch onward.
4. The Apple featuring nomination is filed at month 6 to 7, given its roughly three-month lead.

### The paywall transition, months 10 to 12

The most dangerous moment in the plan, and it gets a protocol rather than a hope. Never take anything away. Gate only capability that did not exist the day before. Name the permanent free tier publicly at launch. Grandfather the pre-paywall cohort permanently and by name as founding runners, identified through StoreKit 2 and Play Billing entitlements. Give 30 days notice in-app and by email in plain language. Hold the whole thing behind the week-4 retention bar, and slip the date out loud if retention does not clear it.

Tripwire, with a number: **no more than a 20 percent drop in weekly active generators in the 30 days after the paywall.** The one unavailable response is silence, since silence is exactly the competitor failure that created this opening.

### Traction milestones, and what each would prove

| Milestone | Target | Timing | What it proves |
|---|---|---|---|
| Interview program complete | 12 to 18 conversations | Month 4 | The umbrella job is real or it is not. **The highest-information milestone in the plan**, and not a growth metric |
| TestFlight cohort | 20 to 50 target-segment runners | Month 4 | The founder can reach the segment without paying for it |
| Beta cohort | 150 to 300 active testers | Month 8 | Route quality has been stress-tested beyond one runner's habits. Now a launch gate |
| iOS launch, first 30 days | 500 to 1,500 installs, 4.5-plus rating, 99.5%+ crash-free | Month 9 to 10 | Quality, not volume |
| First-generation success rate | Above 85 percent of first sessions produce a route the user starts | Continuous | Activation works. Below this, the problem is onboarding, not acquisition |
| **Week-4 retention of route generators** | **20 percent or better** | Month 10 to 11 | **The core hypothesis.** To an investor, the difference between a feature and a product |
| Repeat generation rate | 2-plus per active user per week | Month 10 onward | Route generation is a habit, not a novelty |
| Monthly active runners | 2,000 to 5,000 | Month 12 | The Founder Brief's "thousands of active runners", met honestly |
| Travel-mode share | 10 to 25 percent of generations far from home | Month 12 | Resolves the H1 reframe with behavior instead of recall |
| Paid layer, first 90 days | 4 to 8 percent of week-4-retained users convert | Month 12 to 15 | Willingness to pay, revealed rather than surveyed |

**What none of this proves, and it should be said in the same breath:** that the company can acquire users outside one metro, that the loops compound, or that the coaching layer monetizes at scale. Those are the seed round's job.

---

## 10 · How success is measured

### North Star: Weekly Routed Runners

Distinct runners completing **two or more generated routes in a rolling seven days**, with an 80 percent completion floor inside the definition.

The floor is the point. It means the metric **mechanically cannot rise by shipping more routes people abandon.**

**The rejected alternatives are more informative than the choice:**
- *Monthly active users* — inflatable by the Android launch, and would hide a collapsing weekly cadence for a month.
- *Total routes generated* — disqualifying, because it **rises when routes are bad**: a rejected route drives regeneration.
- *Total distance run* — a cohort using Waypoint as a plain GPS tracker would score perfectly while refuting the core hypothesis.

### Activation

**First generated route completed as a recorded run, within seven days of install.** The earlier definition, "generate and start", counted mid-run abandonment as success, and mid-run abandonment is precisely the signature of a bad route. Since bad routes are the named MVP risk, an activation metric blind to them is worse than none.

Daily leading indicator, called Ignition: the share of first sessions reaching a route on screen, median under 180 seconds.

### Route quality

Eleven behavioral signals collapse into one weekly **Good Route Rate**, because users will rarely rate anything explicitly. The strongest positive proxy is the 30-day repeat rate. The quietest and most damning negative is the reveal abandon rate: a user sees the route and leaves. Investigate below 65 percent; stop feature work below 50 percent.

### The guardrail that matters most

**Honest-refusal rate stability.** The easiest way to lift acceptance numbers is to quietly relax constraints when the engine struggles. A product whose honest refusals disappear looks exactly like a product that got better. Monitoring refusal stability is what keeps the core design principle from eroding under growth pressure.

### The contradiction we found in our own plan

Cohort retention requires a stable per-user identifier over time. TelemetryDeck, the privacy-first analytics vendor originally selected, **deliberately provides none** — that is exactly why it needs no consent banner. So the privacy-preserving analytics choice could not produce the single metric the product exists to prove.

Resolved by keeping cohort retention in a **first-party Postgres event table**, keyed on the account identifier already held for sync, inside the EU-resident store. No new vendor, no new consent basis, no new data-processing agreement. TelemetryDeck keeps the aggregate signals it is good at.

We report this because finding it before building is the useful outcome, and because it is a fair illustration of what the research process is for.

---

## 11 · Technology and architecture

### The stack

| Layer | Choice | Why |
|---|---|---|
| **Client** | React Native with Expo, MapLibre maps, one codebase for both platforms | Dual-platform MVP without two teams |
| **Routing** | Self-hosted GraphHopper with custom cost models, on Hetzner | The only engine combining a round-trip primitive with cost models that can ingest proprietary data |
| **Moat data** | Self-managed PostGIS on the Hetzner private network | The crossing graph and safety layer. Contains no personal data |
| **Personal data** | Aiven for PostgreSQL, EU region | EU-owned, ISO 27001 and SOC 2, 99.99% SLA |
| **Auth** | Better Auth, in Waypoint's own API layer | Decoupled, so identity is not hostage to a platform vendor |
| **Health data** | HealthKit-first, processed on-device | Structural, not a policy |
| **On-device AI** | Apple Foundation Models (3B params, zero inference cost) | Makes free coaching narration economically possible |
| **Monetization** | RevenueCat over StoreKit 2 and Play Billing | Both small-business 15 percent programs |

### The two decisions worth explaining

**Supabase was evaluated and dropped.** Against four pillars — security, stability, reliability and compliance — it did not survive. The replacement is a deliberate split: personal data in a managed EU database with real certifications and a real SLA, and the geospatial moat self-managed where it is cheap and where nobody else's terms of service apply to it. Auth was pulled out of the database vendor entirely, because auth being someone else's product is how a data layer becomes unswappable.

This carries an **explicit revisit clause** at four named checkpoints, at the founder's instruction: before the walking skeleton, when architecture design starts, at Aiven contract time, and if the two-database plus self-owned-auth operational burden proves real in practice. Infrastructure detail is not permitted to block product definition.

**iOS-first was replaced by one cross-platform codebase.** The requirement to launch on both platforms is a founder decision, not a research finding. React Native with MapLibre delivers it at roughly 29 to 31 person-months instead of the near-double a two-native-team approach would cost.

### Integrations

Roughly **20 required integrations across 7 domains**, with 30 cataloged including fallbacks. Every price and rate limit verified. Total **$80 to $130 a month at MVP scale**, rising to $350 to $500 at 10,000 monthly actives, both platforms included.

**The self-host-first posture is a compliance decision as much as a cost one.** Nominatim's public API bans commercial heavy use outright, Photon's demo instance throttles, and several map free tiers are non-commercial only. Nothing in the shipped app may call a donated public instance, because an innocently wired free endpoint becomes either a production outage or a terms violation.

### The licensing question we have not resolved

The crossing graph and any OpenStreetMap-derived context layer may constitute a Derivative Database under ODbL share-alike, which could require making it available on request. Worst case, a competitor requests the derived crossing dataset and the moat narrows to the scoring models and data freshness. This needs counsel review before launch and is listed in section 16 rather than glossed.

---

## 12 · Execution timeline

| Month | Milestone |
|---|---|
| **1** | Android long-lead paperwork starts (Play Console organization account, Health apps declaration, fine-location justification). **A3 technical spike: is the safety layer buildable from open data at solo-founder scale?** |
| 1 | Reddit and forum participation begins, zero promotion |
| 2 | Run club presence begins |
| **3 to 4** | **Walking skeleton on TestFlight.** Interview priorities 1 and 2 complete (12 to 18 conversations) |
| 3 | First OpenStreetMap local mapping meetup as a contributor |
| 4 | TestFlight cohort of 20 to 50 target-segment runners |
| 6 to 7 | **Apple featuring nomination filed** (three-month lead). Store assets, press list, creator outreach |
| **7** | Feature-complete beta, all 15 MVP items |
| **8** | **Beta cohort of 150 to 300 active testers — a hard gate on the launch date** |
| **9 to 10** | **iOS public launch.** One-shot assets spent here |
| 10 to 12 | Android certification and release, as a second local moment |
| **10 to 11** | **Week-4 retention measured. The number the MVP exists to produce** |
| 10 to 12 | Paid coaching layer ships, behind the retention gate |
| 12 | 2,000 to 5,000 monthly active runners; seed round in motion |

**The month-1 spike deserves its emphasis.** Whether lighting and population scoring can be built from open data at this scale is the riskiest technical assumption in the plan, and because the beachhead metro choice depends on the answer, it is a **go-to-market gate and not merely a technical one**. It converts the largest unknown into a scoped decision before any marketing effort is committed.

---

## 13 · Capital and team

### The team the plan assumes

**Founder full-time**, covering product ownership, client engineering and routing. Plus **two contractors**: a senior client engineer at 0.75 to 1.0 FTE, and a backend, routing and data engineer at 0.5 to 1.0 FTE. Effective capacity: **2.5 to 3.0 FTE**. [assumption]

This is the constraint that shapes every other decision in this document. It is why the NOT list is long, why the MVP is 15 items, why paid acquisition is off the table, and why the top-ranked channel is one the founder must run personally.

### The requirement, derived

| Line | Amount | Basis |
|---|---|---|
| Build to dual-platform launch | **~$230,000** | 29 to 31 person-months at the assumed team shape |
| Post-launch runway, 6 to 9 months | **~$90,000 to $135,000** | ~$15,000/month operating base, through the retention proof and the paid-layer test |
| **Total** | **~$320,000 to $365,000** | Round to a **$350,000 to $400,000** pre-seed with buffer |

**This is a derived figure and not yet a decided ask.** No decision record covers the raise, and the Founder Brief states the funding goal only as "seed round closed or in motion within 12 months". The arithmetic is shown so it can be argued with. [inferred]

### What it buys, stated as evidence rather than features

Twelve months of capital produces four things an investor can check: a dual-platform product in both stores, a **measured week-4 retention number** for runners who generate routes, a revealed-preference read on whether anyone pays for training-state-aware routing, and a validated or invalidated answer on whether one metro's pedestrian data can carry a safety layer.

If week-4 retention clears 20 percent, this is a company. If it does not, the capital bought a definitive answer for well under a million dollars, which is the honest framing.

---

## 14 · Risk analysis

| # | Risk | Severity | Mitigation |
|---|---|---|---|
| **1** | **Bad routes.** The one failure mode the product cannot survive. A viral complaint about a route that sent someone somewhere bad is precisely the incumbent's documented wound | **Critical** | Founder personally runs beachhead routes. One metro, not a thin national launch. Honest degradation over invented confidence. Beta cohort is a hard launch gate |
| **2** | **Strava ships constraint-aware generation.** They own the generator, the heatmap, the coaching app and the bundle | **Critical** | 20 to 30 percent likelihood for full depth; the shallow version already shipped in January 2026. Differentiate on depth, ship inside the window, and build the moat in data they cannot acquire by changing an API term |
| **3** | **A1: the beachhead metro fails the pedestrian-data floor.** Sits underneath the segment choice, the metro choice, the top channel, and the entire differentiation claim | **Critical** | Month-1 spike answers it before marketing effort is committed. Shortlist held in reserve: Seattle, Boston, New York, London |
| **4** | **Community-first distribution underperforms.** The economics require roughly 84 percent organic and paid acquisition cannot rescue it | **Critical** | Two primary channels started early and cheaply, with month-4 and month-8 checkpoints that fail loudly rather than quietly |
| **5** | **Safety-liability exposure.** The strongest-evidenced need is the highest-liability surface | High | Six binding language rules enforced by CI lint. Never "safe", always "safety-aware". Data basis and limits stated on every safety surface. Counsel review pre-launch. Open question on redlining exposure if scoring steers away from neighborhoods |
| **6** | **The paid job is not felt value.** The entire paid product is one job whose demand is inferred from market absence | High | The 12 to 18 interviews in month 4 are the cheapest possible test. The free tier means the company is not staked on the paywall to survive year one |
| **7** | **ODbL share-alike narrows the moat** | Medium-High | Counsel review of layer boundaries. Keep municipal and user-derived layers as separate Collective Database members. Accept that scoring models and freshness are the truly defensible part |
| **8** | **The launch override backfires**, since public launch now happens without a quiet burn-in | Medium-High | Four named compensating conditions in section 09, with the beta cohort as a hard gate |
| **9** | **H5 stays uncertain** and the wedge proves to be a $10M business rather than a venture one | Medium | Four named expansion paths. Named tests that would resolve it. Disclosed rather than hidden |
| **10** | **Solo-founder key-person risk** | Medium | Two contractors on the build. The one thing that cannot be delegated, run-club presence, is explicitly acknowledged as founder-only |
| **11** | **Renewal lands at the 24 percent pessimistic case** rather than the 36 percent median | Medium | Annual-only trial, price-preserved founding cohort, and a brand deliberately positioned on route utility rather than AI |

---

## 15 · Legal, privacy and compliance

**Fifteen checklist items gate launch.** Not advisory: goal G6 is zero compliance regressions, and no submission happens without all fifteen verified.

### GDPR, which applies from day one

Heart rate, training load and injury reports are **Article 9 special category health data**, requiring explicit consent through a dedicated gateway. GPS and planned routes are personal data under Article 4(1), and can themselves become Article 9 data when they reveal health information. A **DPIA is required** under Article 35, since systematic location plus health processing at scale is high-risk. Data processing agreements are needed with every processor, an EU representative under Article 27 if there is no EU establishment, and consent withdrawal must be as easy as granting it, with a defined degraded mode when health consent is withdrawn.

### The architecture is the compliance strategy

Health data is processed **on-device** and never leaves it, which collapses the Article 9 server surface rather than managing it. Raw GPS is processed on-device where feasible, meeting Maryland MODPA's necessity standard. Start points are obfuscated before leaving the device for any shared surface. **No CloudKit for health data**, per Apple guideline 5.1.3(ii). The Strava integration is **write-only**, since Strava's API bans AI use of its data.

This is why the privacy claim is a structural advantage rather than a marketing line: competitors would have to re-architect to make it, and Waypoint's biggest competitor's own API terms prevent the shortcut.

### Also in scope

Washington's My Health My Data Act, the FTC Health Breach Notification Rule, and roughly 20 comprehensive US state privacy laws as of mid-2026. The **EU AI Act Article 50(1)** transparency obligation takes effect **2026-08-02**, requiring AI disclosure at first interaction — which is inside the build window, not after it.

### The claim discipline

The product may never say "safe route", "safest route" or "keeps you safe", may never use fear-based marketing, and may never make an unsubstantiated AI claim (the FTC's Operation AI Comply is the live enforcement precedent). Coaching stays advisory and non-diagnostic, with no injury triage, which keeps Waypoint out of both the medical device lane and the AI Act's high-risk tier. A not-medical-advice disclaimer, physician consultation guidance, red-flag symptoms and assumption of risk all appear at onboarding.

Accessibility is WCAG 2.2 AA and EN 301 549 **from the first sprint**, because the European Accessibility Act applies and because retrofitting accessibility is how small teams lose months.

---

## 16 · What we do not know, and the plan to find out

The section that makes the rest of the document trustworthy.

### Known gaps, self-audited

1. **Zero user interviews.** Every persona, pain point and job-to-be-done in this blueprint is assembled from published surveys and mined competitor reviews. This is the largest gap and it is first for a reason.
2. **The paid job is unvalidated.** Demand for training-state-aware route generation is inferred from the market's total absence of it. Nobody has been observed paying for it, and no community post asks for it in these words.
3. **Market sizing rests on report mills.** The only category-exact figures come from vendors with undisclosed methodology that disagree by more than 2x. H5 is UNCERTAIN and is presented that way.
4. **The safety layer's buildability is unproven.** Whether lighting and population scoring can be built from open data at solo-founder scale is the riskiest technical assumption in the plan.
5. **No willingness-to-pay research at the feature level.** Category willingness to pay is proven; Waypoint's specific free/paid split is not.
6. **Route quality has never been tested on a real street** by anyone.
7. **The organic cost per subscriber excludes founder time**, which is a deliberate understatement and must be disclosed alongside any ratio shown to an investor.
8. **Two source documents disagree on Runna's ARR** ($40M in one, roughly $10M implied in another). This blueprint cites the payer count instead, which both agree on.

### The 90-day validation sprint

| Days | Work | Resolves |
|---|---|---|
| **1 to 30** | **The A3 technical spike.** Can lighting, population and crossing scoring be built from open data in the candidate metro, at this team's scale? | Gaps 4 and 6. Also decides the beachhead metro, making this a go-to-market gate |
| 1 to 30 | Begin Reddit and forum participation. Zero promotion | Builds the recruiting surface for the interviews |
| **30 to 60** | **Interview priorities 1 and 2: 12 to 18 conversations** with target-segment runners | Gaps 1, 2 and 5. The highest-information activity in the entire plan |
| 30 to 60 | Run club attendance begins, without pitching | Tests whether the top-ranked channel is reachable |
| **60 to 90** | Walking skeleton on TestFlight with 20 to 50 runners | Gap 6, first real read on route quality |
| 60 to 90 | Price framing tested in interviews, before launch | Gap 5 |
| 60 to 90 | Counsel review scoped: ODbL boundaries, safety-claim liability, redlining exposure | Section 14 risks 5 and 7 |

### Go / no-go

**Go if:** the A3 spike shows the safety layer is buildable in the candidate metro; the interviews confirm the umbrella job in runners' own words; and route quality on real streets holds up with the first 20 to 50 testers.

**Stop or re-plan if:** the pedestrian data will not support the safety layer in any reachable metro, or the interviews show runners do not experience "where should I run" as a problem worth solving. Both answers arrive inside 90 days and for a small fraction of the raise, which is the argument for sequencing them first.

---

## 17 · Appendix and sources

### The research corpus

41 documents across eight phases, each claim carrying a publisher, URL, access date and confidence tag.

| Phase | Location | Contents |
|---|---|---|
| Playbook | `research/00-RESEARCH-PLAYBOOK.md` | Citation rules, confidence labels, definition of done, gate process |
| Progress catalog | `research/00-PROGRESS.md` | Always-current phase status board |
| 0 · Founder | `vault/01-Project/` | Founder Brief with seven testable hypotheses, Charter |
| 1 · Market | `research/01-market/` | Landscape, TAM-SAM-SOM sizing, industry trends, regulatory compliance |
| 2 · Competitors | `research/02-competitors/` | Ten profiles, adjacent platforms, feature and pricing matrices, positioning maps, gap analysis |
| 3 · Users | `research/03-users/` | Pain points, segmentation, four personas, jobs-to-be-done, ranked unmet needs |
| 4 · Synthesis | `research/04-synthesis/` | Opportunity, positioning, hypothesis verdicts, locked concept |
| 5 · Product | `research/05-product/` | PRD, RICE prioritization, MVP scope, user journeys, stack recommendation and validation, database deep dive, dual-platform strategy, API integration map |
| 6 · Business | `research/06-business-model/` | Business model canvas, revenue model, unit economics, metrics, go-to-market plan |
| 7 · Dashboard | `dashboard/index.html` | The readable review surface used for every gate decision |

### Decision record

| # | Decision |
|---|---|
| DEC-006 | Concept locked: route-first positioning, tagline "Know where to run", H1 reframed |
| DEC-008 | Phase 5 gate: MVP scope approved, v1 launches entirely free, Watch as fast-follow |
| DEC-009 | Data layer: Aiven EU for personal data, self-managed PostGIS for the moat, Better Auth decoupled. Supabase dropped. Carries a revisit clause |
| DEC-010 | Staged cross-platform MVP on React Native: iOS month 9-10, Android +4-8 weeks, ~29-31 person-months |
| DEC-011 | Pricing and the permanent free tier: $99.99/yr, coaching layer alone is paid |
| DEC-012 | Measurement corrections: first-party cohort retention, re-based PRD targets |
| DEC-013 | Home-metro beachhead and iOS-first public launch |

### The seven hypotheses, and their verdicts

| ID | Hypothesis | Verdict |
|---|---|---|
| H1 | Travel friction drives adoption | **Partially supported, reframed.** Travel is activation; safety plus home novelty is retention |
| H2 | No incumbent solves constraint-based adaptive route generation | **Supported.** Zero of 15+ products. Time-sensitive since Strava owns both pieces |
| H3 | The route wedge beats another plan product | **Supported**, with a monetization caveat: it acquires better than it monetizes alone |
| H4 | Committed amateurs pay freemium for adaptive routes plus coaching | **Partially supported.** Category willingness to pay proven; feature-level unproven |
| H5 | The addressable market is venture-scale | **UNCERTAIN.** The wedge alone is $5M to $30M ARR; venture scale requires expansion |
| H6 | Mobile-first with wearables is the right v1 form factor | **Supported.** HealthKit-first is effectively mandated by incumbent API terms |
| H7 | Personalized routines deepen retention after the route wedge | **Partially supported.** Plan disruption is near-universal; causation unmeasurable pre-product |

None refuted.

### Principal external sources

Outdoor Industry Association 2026 Running Report · Sport England Active Lives · Strava press and Year in Sport 2025 · RevenueCat State of Subscription Apps 2025 and 2026 · Business of Apps · Sensor Tower · Grand View Research · GWI via Samba Digital · Running Industry Association · Apple Developer WWDC25 and App Store Review Guidelines · Google Play Console Help · OpenStreetMap Foundation license guidance. All accessed 2026-07-30 or 2026-08-06.

---

*Waypoint · Confidential pre-launch material · Prepared from the research corpus at `github.com/mollyparty/waypoint`*
