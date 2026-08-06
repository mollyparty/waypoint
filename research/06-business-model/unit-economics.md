# Waypoint Unit Economics (Directional)

Version-Timestamp: 2026-08-06 12:15:00 UTC-4

## Read this first

**Everything in this document is directional.** Waypoint has no users, no revenue, no app, and no paid tier. There is no Waypoint data in this model. What follows is a structure for reasoning about the business, populated with verified external unit prices where they exist and with clearly labeled assumptions where they do not. The honest framing throughout is **"what has to be true"**, not "what will be". Any figure here that is quoted to an investor without that framing is a misrepresentation.

**The price is not set here.** A parallel Phase 6 deliverable, `revenue-model.md`, sets the price point and packaging. This document deliberately models a **scenario band from $4.99 to $11.99 per month** (with an annual plan at ten times the monthly price) so that when the price lands, the founder reads the answer off the tables rather than re-deriving the model. **Re-read every number here against `revenue-model.md` once it exists.** If the final price falls outside this band, the row structure still holds and only the arithmetic needs redoing.

**Three structural facts drive everything below**, and they are unusual for a subscription business:

1. **v1 launches entirely free** with no paywall at all (DEC-008). The paid layer (TS-08 plus P-01) arrives in v1.x, months 10 to 12. Year-one revenue is therefore zero by design.
2. **Safety-aware routing is free permanently** (DEC-008, reinforced by the product-ethics line in `personas.md`: charging women a safety premium is not on the table).
3. **Route generation, the compute-heavy hero feature, is the free-tier anchor** (`mvp-scope.md` Section 5, forced by the commoditized free floor documented in `pricing-matrix.md`). Free users therefore consume real server compute and real API calls while producing zero revenue. Section 4 quantifies exactly how much that matters, and it is the most important section in this document.

Every claim carries `[verified]`, `[inferred]`, or `[assumption]` per `research/00-RESEARCH-PLAYBOOK.md`. External sources carry a URL and an access date. Sources newly researched for this document were accessed **2026-08-06**; internal cost figures reuse Phase 5 citations dated 2026-07-30 and are marked as such.

---

## 1. Cost structure

Three cost pools, kept strictly separate because they behave differently: **cost of goods sold (COGS)** scales with active users, **fixed operating cost** does not, and **build cost** is a one-time investment to be repaid.

### 1.1 The verified cost base and one correction to it

`api-integration-map.md` Section 8.2 gives total external services at roughly **$80 to $130 per month at MVP** and **$350 to $500 per month at 10k MAU**, both platforms included [verified in Phase 5, accessed 2026-07-30]. Those totals include a Supabase Pro line of $25 per month at MVP and roughly $40 at 10k MAU.

**DEC-009 superseded Supabase.** The approved data layer is Aiven for PostgreSQL (EU) for personal data plus self-managed PostGIS on the Hetzner private network for the geospatial moat, costed in `database-deep-dive.md` Section 6 at **roughly $80 to $150 per month at MVP** and **roughly $230 to $310 per month at 10k MAU** for both stores combined [verified as to the component prices, accessed 2026-07-30; the split-architecture total is inferred]. Substituting that line is the only correction this document makes to the Phase 5 cost base. No new unit prices are invented anywhere in this document.

| Line | MVP (~1k MAU) | 10k MAU | Source |
|---|---|---|---|
| External services per `api-integration-map.md` 8.2 | $80 to $130 | $350 to $500 | Phase 5 [verified], accessed 2026-07-30 |
| Less the superseded Supabase line | ($25) | ($40) | `api-integration-map.md` 8.1 row 25 [verified] |
| Plus the DEC-009 split data layer (Aiven EU plus self-managed PostGIS) | $80 to $150 | $230 to $310 | `database-deep-dive.md` 6 [verified prices, inferred total] |
| **Total COGS, both platforms** | **$135 to $255** | **$540 to $770** | [inferred] sum |
| Working midpoint used below | $195 | $655 | [inferred] |

Extending to the larger tiers using `stack-validation.md` Section 5, adjusted upward for the same data-layer substitution:

| Scale | Monthly COGS | Per active user per month | Basis |
|---|---|---|---|
| MVP, ~1k MAU | $135 to $255 (mid $195) | $0.135 to $0.255 (mid **$0.195**) | Table above [inferred] |
| 10k MAU | $540 to $770 (mid $655) | $0.054 to $0.077 (mid **$0.066**) | Table above [inferred] |
| 100k MAU | $2,700 to $5,000 (mid $3,850) | $0.027 to $0.050 (mid **$0.039**) | `stack-validation.md` 5 ($2,500 to $4,500) plus the data-layer delta [inferred] |
| 1M MAU | $15,000 to $40,000 (mid $27,500) | $0.015 to $0.040 (mid **$0.028**) | `stack-validation.md` 5, carried assumption A13 [assumption] |

The shape matters more than the dollars: **unit cost falls roughly 7x from MVP to 1M MAU**, because most of the MVP cost base is a fixed floor (one routing VM, one managed database, one developer program membership) spread across almost nobody.

### 1.2 Fixed versus marginal inside COGS

Not all of COGS scales with users, and the distinction decides Section 4.

| Component | Behavior | 10k MAU cost | Note |
|---|---|---|---|
| Routing VMs (GraphHopper on Hetzner) | Steps with peak concurrency, not smoothly with MAU | $120 | 2x 32 GB behind a load balancer at 10k [verified in `stack-validation.md` 5, accessed 2026-07-30] |
| Map tiles (self-hosted Protomaps, Android) | Scales with map views | $5 to $20 | [verified in `api-integration-map.md` 1.5] |
| Weather (WeatherKit, Open-Meteo fallback) | Scales with generations | $0 to $79 | 500k WeatherKit calls included with ADP [verified] |
| Product analytics (TelemetryDeck) | Scales with signals | $10 to $30 | [verified] |
| Personal-data store (Aiven), moat store, monitoring, email, crash reporting, dev programs | Near-fixed at this scale | $405 to $541 | [inferred] |
| **Truly marginal share** | | **roughly 25 to 31 percent of COGS** | [inferred] |

**Marginal cost of one additional active user: roughly $0.015 to $0.025 per month** at 10k-MAU scale [inferred from the split above]. That is the number to use when asking "what does one more free user cost me today". The fully allocated $0.066 is the number to use when asking "what does the whole free base cost the business".

Assumed route generation volume: **8 generations per active user per month** [assumption A6]. At 10k MAU that is 80,000 generations against a $120 routing tier, or roughly **$0.0015 per generated route** [inferred]. This single assumption is the most load-bearing unverified number in the cost model, and Section 8 explains why.

### 1.3 Revenue-linked costs

These are not COGS; they are deductions from gross billings, applied before any margin calculation.

| Deduction | Rate | Source |
|---|---|---|
| Apple App Store, Small Business Program | 15 percent of gross, for developers under $1M USD in prior-calendar-year proceeds. **Enrollment required**, and enrollment must happen before the first paid transaction | Apple, https://developer.apple.com/app-store/small-business-program/ [verified, accessed 2026-07-30] |
| Apple past $1M | **Cliff.** Crossing $1M in proceeds in the current year moves all FUTURE sales to 30 percent for the rest of that year and the whole next year | Same source [verified] |
| Google Play, 15 percent tier | 15 percent on the first $1M of annual earnings for enrolled developers; auto-renewing subscriptions get reduced treatment regardless. Some 2026 markets restructured to 10 percent plus a 5 percent billing fee | Google, https://support.google.com/googleplay/android-developer/answer/112622 [verified, accessed 2026-07-30] |
| Google past $1M | **Graduated.** Only revenue above $1M pays the standard rate | Same source [verified] |
| RevenueCat | 1 percent of gross monthly tracked revenue, which is **roughly 1.4 percent of net** after the store cut. Free below $2,500 MTR | RevenueCat pricing [verified in `stack-validation.md` 4, accessed 2026-07-30] |
| Refunds | Model at **3.5 percent** of first-period paid subscriptions. Most categories cluster 3 to 4 percent; high-priced apps run 4.5 percent, low-priced 2.7 percent; North America median 3.4 percent | RevenueCat, State of Subscription Apps 2026, https://www.revenuecat.com/state-of-subscription-apps-2026-health-and-fitness/ [verified, accessed 2026-08-06] |

**Net multiplier on gross billings: 0.85 x 0.986 x 0.965 = 0.8088.** Every dollar billed becomes roughly **81 cents** of recognized net revenue below the $1M line [inferred arithmetic on verified rates]. Above the Apple cliff the multiplier falls to **0.666**, a 17.6 percent cut in net revenue per iOS subscriber. Section 9 flags this as a planning trap, not a modeling detail.

### 1.4 Fixed operating cost

Everything that does not scale with users and is not build capital. Paid marketing is excluded here because it is handled inside CAC (Section 5); double-counting it is the most common error in models of this shape.

| Line | Lean | Base | Funded | Note |
|---|---|---|---|---|
| Founder draw | $5,000 | $7,000 | $9,000 | [assumption A9] |
| Contractor retainer (maintenance, Android hardening, on-call) | $3,000 | $6,000 | $12,000 | 0.25 to 1.0 FTE at roughly $65 to $75 per hour [assumption A10, rate band from 2026 contractor surveys cited in 1.5] |
| Tools, CI, code hosting, design software | $300 | $300 | $600 | [assumption A11] |
| Accounting, legal, insurance (amortized) | $600 | $1,200 | $2,500 | [assumption A11] |
| Developer programs, contingency | $100 | $500 | $900 | Apple $99 per year amortized [verified] |
| **Total monthly fixed operating cost** | **$9,000** | **$15,000** | **$25,000** | [assumption, composed of the above] |

The base case of **$15,000 per month** is used throughout. It is a founder-plus-half-a-contractor company, not a funded startup.

### 1.5 One-time build cost

DEC-010 sets MVP effort at **~29 to 31 person-months** across a founder plus two contractors, iOS at month 9 to 10 and Android at month 10 to 12 [verified: DEC-010, `mvp-scope.md` Section 7 as amended]. Splitting that: the founder carries roughly 11 person-months (no cash cost, real opportunity cost), leaving **roughly 18 to 20 contractor person-months** to buy [inferred from the stated team shape of 0.75 to 1.0 FTE plus 0.5 to 1.0 FTE over an 11-month calendar].

**Stated rate assumption: 160 billable hours per person-month.** Verified 2026 senior React Native contractor rates: United States $100 to $150 per hour, Western Europe $80 to $120, Eastern Europe $55 to $80, Latin America $60 to $90; seniors with New Architecture or native-module experience command a 20 to 30 percent premium, which DEC-010's HealthKit, Health Connect, and background-geolocation requirements make relevant [verified] (hirereactnativedevs.com, "React Native Developer Cost in 2026", https://hirereactnativedevs.com/blog/react-native-developer-cost-2026, accessed 2026-08-06; corroborated by fonzi.ai, https://fonzi.ai/blog/hire-react-native-developers, and Cadence, which quotes US contractor day rates of $960 to $1,400 for New Architecture seniors, https://cadence.withremote.ai/blog/how-to-hire-a-react-native-developer, both accessed 2026-08-06).

| Contractor sourcing | Blended rate | Per person-month | 19 contractor pm | Plus non-labor | **Total cash build cost** |
|---|---|---|---|---|---|
| Nearshore / CEE senior | $65 per hour | $10,400 | $197,600 | $32,000 | **~$230,000** |
| Western Europe senior | $100 per hour | $16,000 | $304,000 | $32,000 | **~$336,000** |
| United States senior | $125 per hour | $20,000 | $380,000 | $32,000 | **~$412,000** |

Non-labor build cost of $32,000 comprises: infrastructure during a 12-month build at $100 to $250 per month ($1,200 to $3,000) [verified unit prices]; counsel for the ODbL layer-boundary review, DPIA, privacy policy, terms, and DPA review ($8,000 to $20,000) [assumption A12]; brand and UI design contract ($8,000 to $20,000) [assumption A12]; test devices ($3,000) [assumption]; entity and accounting setup ($2,000) [assumption]; Apple and Play program fees ($124) [verified].

**Base case used throughout: $230,000 cash build cost** (nearshore contractors). Founder opportunity cost of 11 person-months at $10,000 to $16,000 per month adds a further **$110,000 to $176,000 of non-cash investment**, giving a fully loaded figure near **$355,000** [inferred]. Investors will ask for the fully loaded number; lenders and runway math want the cash number. Report both.

---

## 2. Gross margin per subscriber across the price band

### 2.1 The price band and what survives the deductions

Annual plans are set at ten times the monthly price (the standard two-months-free construction). Blended figures assume **50 percent of subscribers on annual plans**, which is what reconciles with the verified category fact that Health and Fitness draws 68 percent of its revenue from annual plans [verified, RevenueCat SOSA 2026, accessed 2026-08-06; the subscriber-share back-solve is inferred].

| Monthly price | Annual price | Blended gross per month | After 15% store | After RevenueCat | **After 3.5% refunds (net-net)** |
|---|---|---|---|---|---|
| $4.99 | $49.99 | $4.58 | $3.89 | $3.84 | **$3.70** |
| $6.99 | $69.99 | $6.41 | $5.45 | $5.37 | **$5.19** |
| **$7.99 (mid)** | **$79.99** | **$7.33** | **$6.23** | **$6.14** | **$5.93** |
| $9.99 | $99.99 | $9.16 | $7.79 | $7.68 | **$7.41** |
| $11.99 | $119.99 | $11.00 | $9.35 | $9.22 | **$8.89** |

All [inferred] arithmetic on the verified rates in 1.3. Competitive context, for whether this band is even credible: Strava sits at $11.99 per month and $79.99 per year, RunGo at $5.99 and $59.99, Komoot at about EUR 6.99, Coopah at $14.99 and $79.99, Runna at $19.99 and $119.99 [verified, `pricing-matrix.md`, accessed 2026-07-30]. Phase 2 concluded the credible annual band for Waypoint is $79.99 to $119.99 [inferred, `pricing-matrix.md`]. The $4.99 rung is modeled to show the floor, not to recommend it.

### 2.2 Gross margin at each scale

Gross margin per subscriber = (net-net revenue minus COGS allocated per paying subscriber) divided by net-net revenue. COGS per paying subscriber = per-MAU cost divided by the free-to-paid conversion rate, because **the paying base carries the cost of the entire active base**. This table holds conversion at **3 percent**, which is close to the Health and Fitness median download-to-paid of 2.9 percent [verified, RevenueCat SOSA 2026 via the-diff, https://tools.the-diff.com/health/, accessed 2026-08-06].

Allocated COGS per paying subscriber per month at 3 percent conversion: MVP $6.50, 10k MAU $2.20, 100k MAU $1.30, 1M MAU $0.93 [inferred].

| Monthly price | MVP (~1k MAU) | 10k MAU | 100k MAU | 1M MAU |
|---|---|---|---|---|
| $4.99 | **-76%** | 41% | 65% | 75% |
| $6.99 | **-25%** | 58% | 75% | 82% |
| **$7.99 (mid)** | **-10%** | **63%** | **78%** | **84%** |
| $9.99 | 12% | 70% | 83% | 87% |
| $11.99 | 27% | 75% | 85% | 90% |

Read this table carefully, because the left column is the one that surprises people.

- **At MVP scale, gross margin is negative or negligible at most of the band.** That is not a pricing failure. It is arithmetic: a $195 per month fixed infrastructure floor divided across roughly 30 paying subscribers is $6.50 per subscriber, which exceeds the net revenue of a $7.99 plan. This is also mostly moot, because DEC-008 says v1 has no paywall at all. It matters only as a warning: **do not launch the v1.x paywall while the active base is still around 1,000 people and expect the unit economics to look like a software business.** They will not until the base is roughly 5,000 to 10,000 actives.
- **At 10k MAU the model turns**, reaching 63 percent gross margin at the mid price. Respectable, well below the 80 to 90 percent a pure-software subscription usually shows, and the gap is entirely the free base.
- **At 100k and 1M MAU the business looks normal**, 78 to 84 percent at the mid price. There is no cost cliff anywhere on that path; `stack-validation.md` Section 5 established that every layer scales by replication rather than re-architecture [verified].

### 2.3 The same table, holding scale and moving conversion

At 10k MAU and the mid price of $7.99:

| Free-to-paid conversion | Paying subs at 10k MAU | Allocated COGS per subscriber | **Gross margin** |
|---|---|---|---|
| 2% | 200 | $3.30 | **44%** |
| 3% | 300 | $2.20 | **63%** |
| 5% | 500 | $1.32 | **78%** |
| 8% | 800 | $0.83 | **86%** |

Conversion moves gross margin by 42 percentage points across a plausible range. Price, across the entire $4.99 to $11.99 band at fixed conversion, moves it by 34 points. **Conversion is a bigger margin lever than price.** That is the first of the three findings this model exists to surface.

---

## 3. Interpreting the store commission structures past $1M

Both stores must be modeled separately once Waypoint approaches $1M, and the failure modes are different [verified structures, `api-integration-map.md` 5.2].

- **Apple is a cliff.** $1M in *proceeds* (which are already net of commission) triggers 30 percent on all future sales for the remainder of that year and the following year. At the mid price, $1M of Apple proceeds is roughly $1.18M in gross billings, which is roughly **14,700 annual subscribers on iOS** [inferred]. The step-down in net multiplier from 0.8088 to 0.666 removes about **$14 per subscriber-year** at the $79.99 annual price. Crossing the line late in a calendar year is the worst possible timing, because the penalty runs through the whole next year regardless.
- **Google is graduated.** Only earnings above $1M pay the higher rate, so there is no discontinuity, and in some 2026 markets subscriptions are 10 percent plus a 5 percent billing fee rather than 15 percent flat.
- **Practical consequence:** enroll in both programs before the first paid transaction (Apple's enrollment takes days and is effective the following month), and once revenue is within roughly 25 percent of the Apple threshold, model the cliff explicitly in the annual plan. [inferred, on the verified enrollment mechanics]

---

## 4. The free-user cost problem

This is the section that is unusual for this business, and the one an investor will probe hardest.

### 4.1 What a free active user actually costs

| Scale | Fully allocated cost per active user | Per free user per year | Marginal cost of one more free user |
|---|---|---|---|
| MVP (~1k MAU) | $0.195 per month | **$2.34** | roughly $0.02 to $0.04 per month |
| 10k MAU | $0.066 per month | **$0.79** | roughly $0.015 to $0.025 per month |
| 100k MAU | $0.039 per month | **$0.47** | roughly $0.010 to $0.020 per month |
| 1M MAU | $0.028 per month | **$0.34** | roughly $0.008 to $0.015 per month |

All [inferred] from Section 1. **In absolute terms a free user is cheap.** Under a dollar a year at any scale past MVP. Nobody goes out of business paying 79 cents a year to serve someone. The absolute number is not the problem, and any framing that says "free users are expensive" is wrong.

### 4.2 The actual problem: free cost as a share of net revenue

The right question is not "what does a free user cost" but "what fraction of the money we collect from payers is consumed by serving people who pay nothing". At 10k-MAU unit costs and the mid price:

| Free-to-paid conversion | Free-base COGS as a share of net subscription revenue | Reading |
|---|---|---|
| 2% | **55%** | The free tier consumes more than half of net revenue. Not viable. |
| 3% | **36%** | A serious drag. Gross margin caps out around 63 percent. |
| 5% | **21%** | Uncomfortable but workable. |
| 8% | **13%** | Manageable. |
| 12% | **8%** | A rounding error. |

[inferred] arithmetic. **The crossover, defined as the point where the free base consumes 20 percent of net subscription revenue, sits at roughly 5.3 percent conversion at 10k-MAU unit costs, and improves to roughly 3.2 percent at 100k-MAU unit costs** [inferred].

So the answer to "at what point does free-tier cost stop being a rounding error" is precise and it is a conversion answer, not a cost answer: **below roughly 5 percent free-to-paid conversion, the free tier is a genuine constraint on the business. Above roughly 8 percent, it is noise.**

### 4.3 What happens if conversion lands at the low end

The realistic low case is not hypothetical. Freemium apps convert downloads to paid at a **2.1 percent median**, against 10.7 percent for hard paywalls, and Health and Fitness overall sits at **2.9 percent** [verified, RevenueCat SOSA 2026, accessed 2026-08-06]. Waypoint has deliberately chosen the freemium side of that split (DEC-008), and has additionally chosen to give away the hero feature, which is a more generous free tier than the median freemium app. The honest planning case is therefore **2 to 3 percent, not 5 percent**.

At 2.5 percent conversion, 10k MAU, and the mid price:

- 250 paying subscribers producing net-net revenue of roughly **$17,800 per year**
- Total COGS of roughly **$7,860 per year**, of which roughly **$7,660 is spent on the 9,750 people who pay nothing**
- Gross margin of roughly **56 percent**, against the 80 to 90 percent an investor expects from a subscription app
- Fixed operating cost of $180,000 per year is untouched by any of this

The business is not dead at 2.5 percent, but it is a **volume business, not a margin business**, and the entire path to profitability runs through MAU growth rather than price. That is a materially different company from the one the pricing analysis in `pricing-matrix.md` implies, and the founder should know which one is being built before the paywall ships.

### 4.4 The tail risk that the averages hide

Averages understate the risk because generation volume is almost certainly not evenly distributed. The model assumes 8 route generations per active user per month [assumption A6]. Two things follow:

- **A heavy free user is not individually expensive.** At roughly $0.0015 per generated route, someone generating 60 routes a month costs about $0.09 in compute. Per-request abuse is not a real financial threat.
- **Peak concurrency is the real cost driver, and it steps.** The routing tier is a persistent JVM holding a memory-mapped graph; capacity is bought in whole 32 GB nodes at roughly $60 to $125 each per month, not in fractions [verified, `stack-validation.md` 3, accessed 2026-07-30]. A 3x miss on the generations-per-user assumption does not raise COGS by cents, it forces additional nodes and **roughly doubles total COGS**, which pushes the free-tier crossover from about 5 percent conversion to about 9 percent. This is why A6 is the single most consequential unverified number in the cost model.

### 4.5 What would have to change if free-tier cost becomes a real constraint

In the order they should be reached for, cheapest and least user-hostile first. None of these touch safety routing, which is free permanently and non-negotiable (DEC-008, and the ethics line in `personas.md` on Elena).

1. **Cache and reuse generation candidates.** Keyed on (start cell, target distance, constraint set), served from the geospatial store that DEC-009 already put on the private network. Cuts compute without any user-visible change. Cheapest lever, do it regardless. [inferred]
2. **Split the free and paid generation paths by cost, not by value.** The fast contraction-hierarchy round-trip stays free (it is the commoditized primitive the free market already gives away). The expensive path, `custom_model` with `ch.disable=true` and per-request constraint weighting [verified, `api-integration-map.md` 1.1], is exactly the constraint depth that Phase 2 concluded should be the paid boundary anyway [verified, `pricing-matrix.md` freemium boundary analysis]. Cost and value happen to align here, which is fortunate and should be exploited.
3. **Soft-cap free generation volume** with honest H-09 degradation copy, never a silent failure. A cap of, say, 15 generations per week affects almost nobody at the assumed mean of 8 per month and removes the concurrency tail. [inferred]
4. **Sunset warm capacity for dormant accounts.** The cost is capacity, not storage; storage of a lapsed account is effectively free. [inferred]
5. **Raise conversion instead of cutting cost.** The crossover is a conversion problem in every scenario modeled. Twenty percent better onboarding is worth more than any infrastructure optimization on this list. Note that 55 percent of three-day trial cancellations happen on Day 0, and that trials of 17 or more days convert 70 percent better than short trials (42.5 percent versus 25.5 percent) [verified, RevenueCat SOSA 2026, accessed 2026-08-06]: the highest-leverage conversion work is first-session activation and trial length, both cheap.
6. **Not on the list, ever:** paywalling safety-aware routing, or degrading it for free users. It is a DEC-008 commitment and a brand-integrity line.

---

## 5. LTV

### 5.1 Retention benchmarks, and a conflict between two sources

| Benchmark | Value | Source |
|---|---|---|
| Health and Fitness, download-to-paid | 2.9% median | RevenueCat SOSA 2026 [verified, accessed 2026-08-06] |
| Health and Fitness, monthly plan first renewal | 57.0% | Same [verified] |
| Health and Fitness, annual plan first renewal | 36.0% | Same [verified] |
| Health and Fitness, 12-month retention (blended) | 34.2% | Same [verified] |
| Health and Fitness, trial start rate / trial-to-paid | 7.2% / 37.7% | Same [verified] |
| All-category 12-month retention by plan | annual 28% (down from 31%), monthly 8%, weekly 1% | Same [verified] |
| Health and Fitness, yearly active renewal rate | 86.4%, the highest of any category | Same [verified] |
| Health and Fitness, yearly RLTV per payer | $35.64 median, top quartile above $60 | Same [verified] |
| Fitness apps, monthly churn | median 10 to 13%, top quartile 4 to 6%, bottom quartile 18 to 25% | Lifecycle Architect, https://lifecyclearchitect.com/benchmarks/fitness-apps-churn-rate-benchmarks/ [verified as published, accessed 2026-08-06; methodology not disclosed, credibility medium] |
| Fitness apps, annual churn | median 55 to 65%, top quartile 35 to 45% | Same [verified as published] |

**The two sources conflict.** Lifecycle Architect's 10 to 13 percent median monthly churn implies an average subscriber life of 7.7 to 10 months. RevenueCat's monthly-plan 12-month retention of 8 percent implies roughly 19 percent monthly churn and a 5.3-month life. **We weight RevenueCat**, because it discloses its methodology, covers 115,000-plus apps, and measures subscriptions rather than self-reported cohorts; Lifecycle Architect does not disclose its sample. We use Lifecycle Architect only as the upper bound in the optimistic scenario. [inferred, per the playbook's conflicting-sources rule]

Two further verified facts shape the model:

- **Higher prices cost you the first renewal, not the relationship.** High-priced annual plans renew at 24 percent versus 37 percent for low-priced, but survivors behave identically by the third renewal [verified, RevenueCat SOSA 2026]. Pricing at the top of the band is therefore a first-renewal risk, not a lifetime-value risk, and it is partially self-correcting.
- **AI-branded apps monetize better and retain worse.** They earn 41 percent more per payer but churn 30 percent faster, with 12-month annual retention of 21.1 percent versus 30.7 percent, and refund rates of 4.2 percent versus 3.5 percent [verified, RevenueCat SOSA 2026]. Waypoint's on-device coaching layer and generated routes sit squarely in that pattern. **This is a real risk to the LTV numbers below**, and it argues for positioning Waypoint on the utility of the route rather than on the AI, which happens to be what DEC-006's "Know where to run" already does.

### 5.2 Lifetime model

Expected paid periods are built from sequential renewal rates rather than a flat churn rate, because the verified data shows retention breaking at commitment checkpoints and then flattening, not decaying smoothly.

| Scenario | Annual plan renewals (r1, r2, r3, steady) | Expected years | Monthly plan renewals (r1, r2, r3, steady) | Expected months |
|---|---|---|---|---|
| Pessimistic | 0.24, 0.55, 0.65, 0.70 | **1.66** | 0.45, 0.60, 0.70, 0.82 | **2.8** |
| Base | 0.36, 0.60, 0.70, 0.75 | **2.18** | 0.57, 0.70, 0.80, 0.88 | **4.63** |
| Optimistic | 0.50, 0.70, 0.78, 0.82 | **3.37** | 0.65, 0.78, 0.85, 0.90 | **8.0** |

Base-case r1 values are the verified Health and Fitness medians. Pessimistic r1 for annual is the verified high-priced-app figure. Later renewals are [assumption A13], anchored on the verified pattern that renewal rates climb steeply by the third cycle and cluster tightly across geographies thereafter.

### 5.3 LTV across the price band

Net revenue per period uses the 0.8088 multiplier. Blend is 50 percent annual subscribers, 50 percent monthly.

| Monthly / annual price | Pessimistic LTV | **Base LTV** | Optimistic LTV |
|---|---|---|---|
| $4.99 / $49.99 | $39 | **$53** | $84 |
| $6.99 / $69.99 | $55 | **$75** | $118 |
| **$7.99 / $79.99 (mid)** | **$63** | **$86** | **$135** |
| $9.99 / $99.99 | $78 | **$107** | $169 |
| $11.99 / $119.99 | $94 | **$128** | $202 |

[inferred] arithmetic on the verified inputs above.

**Sanity check against the category.** The base case at the mid price implies roughly **$47 of realized value per payer in year one**, against a verified Health and Fitness median of $35.64 and a top quartile above $60 [verified, RevenueCat SOSA 2026]. Waypoint's base case therefore assumes **above-median but not top-quartile performance**. That is a defensible place to sit, but it must be stated plainly: the base case is not conservative, it is slightly optimistic relative to the median app in the category. An investor who anchors on the category median should be shown the pessimistic column.

---

## 6. CAC

### 6.1 What acquisition actually costs in this category in 2026

All figures accessed 2026-08-06.

| Channel | Metric | Value | Source |
|---|---|---|---|
| Apple Search Ads, Health and Fitness (US) | median CPT | $1.59 | AppTweak, https://www.apptweak.com/en/aso-blog/apple-ads-benchmarks [verified] |
| Apple Search Ads, Health and Fitness (US) | median CPI | $3.83 | Same [verified] |
| Apple Search Ads, Health and Fitness | CPT range / CPI range | $1.20 to $3.00 / $2.00 to $7.00 | Admiral Media, https://admiral.media/apple-search-ads-benchmarks/ [verified as published] |
| Apple Search Ads, "Fitness and Workouts" niche | CPT $1.60, install CR 49.95%, **CPA $3.20** | | Adapty, https://adapty.io/blog/apple-ads-benchmarks-2026/ [verified as published] |
| Apple Search Ads, "Health and Fitness" niche | CPT $1.64, install CR 54.2%, **CPA $3.02** | | Same [verified as published] |
| Meta / Facebook | CPI | $2.00 to $5.50 | AdAction 2026, cited by Airbridge, https://www.airbridge.io/en/blog/cost-per-trial-cost-per-subscription-subscription-app-ua-metrics [verified as published] |
| Google App Campaigns | CPI | $1.50 to $4.50 | Same [verified as published] |
| TikTok | CPI | $1.75 to $4.00 | Same [verified as published] |
| Fitness apps generally | CPI | $2 to $8 Android, $4 to $20 iOS | Adwave, https://adwave.com/resources/fitness-app-advertising [verified as published, agency source] |
| Fitness apps, paid social | **cost per paid subscriber $20 to $120** | | Same [verified as published] |
| Fitness apps, creator channel | **cost per paid subscriber $30 to $200** | | Same [verified as published] |
| Micro-creator CPM (10k to 100k followers) | TikTok $8 to $20, Instagram Reels $12 to $30, YouTube $25 to $60; organic-only deals run 30 to 50 percent lower | | ChannelCore, https://channelcore.io/influencer-marketing-benchmarks-2026/ [verified as published] |
| Micro-creator flat fees | $200 to $1,500 per post (10k to 100k followers) | | Stan, https://stan.store/blog/influencer-rates/ [verified as published] |
| Worked cost-per-subscriber example | Meta $58, Google $45 | | Airbridge, link above [verified as published] |
| Real-portfolio cost-per-subscriber example | Meta $192, Google $89, Apple Search Ads $133 | | Airbridge, https://www.airbridge.io/en/blog/marketing-dashboard-cost-per-subscriber-by-channel [verified as published] |

One structural warning from the same research, and it is directly adverse to Waypoint: **Health and Fitness user-acquisition budget concentration among the top apps rose from 54 percent to 73 percent** [verified as reported by Airbridge citing the AppsFlyer 2026 State of Subscriptions report, accessed 2026-08-06]. A solo-founder app is bidding into auctions dominated by a handful of very large spenders. Every CPI in the table above is a market price set by people with more money than Waypoint has.

### 6.2 Translating CPI into cost per paying subscriber

CPI is the wrong unit for a subscription business, and doubly wrong for Waypoint, where **v1 has no paywall at all**, so a paid install cannot become a subscriber for months. Cost per subscriber is CPI divided by the download-to-paid rate.

| CPI | Download-to-paid | **Paid-channel CAC per subscriber** |
|---|---|---|
| $2.50 | 4.0% | $63 |
| $2.50 | 2.9% (H&F median) | $86 |
| $4.00 | 2.5% | **$160 (base case used below)** |
| $4.00 | 2.1% (freemium median) | $190 |
| $6.00 | 2.1% | $286 |
| $6.00 | 1.5% | $400 |

[inferred] arithmetic. The $63 to $286 band brackets every sourced cost-per-subscriber observation in 6.1 ($45 to $192), which is the cross-check that says the model is not detached from the market.

Organic CAC is modeled as total non-paid go-to-market spend (creator seeding, run-club sponsorship, ASO tooling, PR, content) divided by organically attributed subscribers: **$12 per subscriber base case, $5 to $25 band** [assumption A15]. Founder time is excluded, which is a deliberate understatement and should be disclosed to anyone who reads the LTV/CAC ratio.

### 6.3 Blended CAC by acquisition mix

The GTM plan (being written in parallel, `gtm-plan.md`) leans on community and organic channels. This table is how much that decision is worth.

| Organic share of new subscribers | Blended CAC (mid price) |
|---|---|
| 95% | **$19** |
| 90% | **$27** |
| 75% | **$49** |
| 50% | **$86** |
| 25% | **$123** |
| 0% (paid only) | **$160** |

[inferred] using organic $12 and paid $160.

---

## 7. LTV/CAC and payback

### 7.1 The benchmarks

The conventional bars, stated so Waypoint can be measured against them: **LTV/CAC of 3:1 is the floor** for a healthy subscription business, 4:1 to 5:1 is good, below 1:1 means every new customer destroys value; **CAC payback under 12 months** is the consumer-subscription norm. Category-specific corroboration: fitness apps are advised to target a 3:1 to 4:1 ratio and to spend 30 to 50 percent of LTV on acquisition during growth [verified as published, Adwave, accessed 2026-08-06].

### 7.2 The grid

Base-case LTV from 5.3, blended CAC from 6.3.

| Organic share | $4.99 | $6.99 | **$7.99 (mid)** | $9.99 | $11.99 |
|---|---|---|---|---|---|
| 95% | 2.8 | 3.9 | **4.5** | 5.6 | 6.8 |
| 90% | 2.0 | 2.8 | **3.2** | 4.0 | 4.8 |
| 75% | 1.1 | 1.5 | **1.8** | 2.2 | 2.6 |
| 50% | 0.6 | 0.9 | **1.0** | 1.2 | 1.5 |
| 0% (paid only) | 0.3 | 0.5 | **0.5** | 0.7 | 0.8 |

**Waypoint's position against the benchmarks, stated plainly: paid acquisition alone does not work at any price in this band.** At the mid price, buying subscribers through paid channels returns 53 cents of lifetime value per dollar of CAC. Even at $11.99 per month, the top of the credible band, paid-only acquisition returns 80 cents on the dollar. This is not a Waypoint-specific failure; it is the arithmetic of a freemium app in a category where the top spenders control 73 percent of the paid budget.

**The business clears the 3:1 bar only at roughly 90 percent organic acquisition or better.** That is a demanding but not absurd target for a product whose distribution story is Strava sharing, run clubs, and word of mouth, and it is precisely why the GTM plan's community-first bet is load-bearing rather than stylistic. If `gtm-plan.md` cannot credibly deliver 85 to 95 percent organic, the unit economics do not close at any price in this band, and the correct response is to fix distribution, not to raise the price.

### 7.3 Payback period

Payback = CAC divided by monthly contribution per subscriber. At the mid price and 10k-MAU costs, contribution is $5.93 minus $2.20, or **$3.73 per subscriber per month**.

| Blended CAC | Accounting payback | Cash payback on an annual subscriber |
|---|---|---|
| $19 (95% organic) | 5.1 months | Immediate |
| $27 (90% organic) | 7.2 months | Immediate |
| $49 (75% organic) | 13.1 months | Immediate |
| $86 (50% organic) | 23.1 months | Recovered within year 1 |
| $160 (paid only) | 42.9 months | Not recovered in year 1 |

Two nuances worth carrying into an investor conversation. First, **annual plans collect roughly $64.69 net on day one at the mid price**, so cash payback on an annual subscriber is immediate at any CAC below that, even where accounting payback looks slow. Second, that cash arrives before the refund window closes, so the 3.5 percent refund deduction is a real timing risk on aggressively acquired cohorts, not just a revenue haircut.

---

## 8. Break-even

### 8.1 Covering monthly operating cost

Break-even subscribers = (fixed operating cost plus COGS) divided by net-net revenue per subscriber per month. COGS is solved at 5 percent conversion, which is the level at which the free base stops dominating (Section 4.2); at 3 percent conversion every figure below rises by roughly 8 to 10 percent because the same subscriber count implies a much larger, costlier free base.

| Monthly price | Lean ($9,000 fixed) | **Base ($15,000 fixed)** | Funded ($25,000 fixed) |
|---|---|---|---|
| $4.99 | 2,865 | **4,784** | 7,919 |
| $6.99 | 2,043 | **3,410** | 5,645 |
| **$7.99 (mid)** | **1,788** | **2,985** | **4,941** |
| $9.99 | 1,430 | **2,388** | 3,954 |
| $11.99 | 1,192 | **1,991** | 3,296 |

[inferred] arithmetic on the assumptions in 1.4.

**Headline: at the mid price and a $15,000 per month cost base, Waypoint breaks even at roughly 3,000 paying subscribers**, which at 5 percent conversion implies roughly 60,000 monthly actives, and at 3 percent conversion roughly 100,000 monthly actives.

Two sanity checks on whether that is reachable. Runna, the category's breakout, reached roughly 90,000 payers in three years [verified as reported, `market-sizing.md`, accessed 2026-07-30]; Waypoint's break-even is **3.3 percent of Runna's year-three base**. Phase 1's SOM range is 70,000 to 310,000 paying subscribers by year five [inferred, `market-sizing.md`]; break-even sits at **1 to 4 percent of that range**. Break-even is not the hard part of this business. Getting the first 60,000 actives is.

### 8.2 Repaying the build investment

Separate question, and it comes after break-even, since these are subscribers above the break-even line. Annual contribution per subscriber is net-net revenue times twelve, less allocated COGS of roughly $0.90 per month at 5 percent conversion.

| Monthly price | Annual contribution per subscriber | **Subscriber-years to repay $230,000** |
|---|---|---|
| $4.99 | $33.60 | 6,845 |
| $6.99 | $51.48 | 4,468 |
| **$7.99 (mid)** | **$60.36** | **3,810** |
| $9.99 | $78.12 | 2,944 |
| $11.99 | $95.88 | 2,399 |

[inferred]. A "subscriber-year" is one subscriber retained for one year. At the mid price, repayment needs roughly **3,800 subscriber-years above break-even**: for example 3,800 additional subscribers held for a year, or 1,900 held for two.

**Combined: roughly 6,800 paying subscribers held for a full year both covers the $15,000 monthly cost base and repays the $230,000 cash build**, at the mid price. If the build is bought at Western European contractor rates ($336,000), that rises to roughly 8,550; at United States rates ($412,000), roughly 9,800. The contractor-sourcing decision moves the payback target by 25 to 45 percent, which makes it a financing decision as much as a hiring one.

---

## 9. Sensitivity: the three variables that actually move the outcome

Ranked by how far each one swings the answer across its plausible range, holding everything else at base case.

| Rank | Variable | Plausible range | Swing in the outcome |
|---|---|---|---|
| **1** | **Organic share of acquisition** | 0% to 95% | Blended CAC $160 down to $19, an **8.4x swing**. LTV/CAC at the mid price moves from **0.5 to 4.5**. This one variable decides whether the business works. |
| **2** | **Free-to-paid conversion** | 2% to 8% | Gross margin at 10k MAU moves from **44% to 86%**. Free-base cost moves from 55% of net revenue to 13%. Break-even MAU moves by roughly **3x** at a fixed subscriber count. |
| **3** | **Annual retention past the first renewal** | r1 of 24% to 50% | Base LTV at the mid price moves from **$63 to $135**, a 2.1x swing, and it compounds directly into LTV/CAC. |
| 4 | Price within the band | $4.99 to $11.99 | LTV moves 2.4x, break-even moves 2.4x. Large, linear, and the **least uncertain** of the four, which is why it ranks below the others. |
| 5 | Route generations per active user (A6) | 4 to 24 per month | A 3x miss roughly **doubles COGS** and pushes the free-tier crossover from 5% conversion to 9%. Low probability of a large miss, high consequence if it happens. |
| 6 | Contractor sourcing geography | $65 to $125 per hour | Cash build cost $230,000 to $412,000; combined break-even-plus-repayment target moves 25% to 45%. A one-time effect, not a recurring one. |

**The three to watch, named explicitly: organic acquisition share, free-to-paid conversion, and annual first-renewal rate.** Price is a distant fourth. Infrastructure cost, the thing founders most often optimize first, is not in the top five as a lever; it matters only through the free-tier ratio in variable 2.

The uncomfortable interaction: variables 1 and 2 are correlated in the wrong direction. A generous free tier (which is what makes organic word of mouth and Strava-share distribution work, holding down CAC) is the same thing that suppresses conversion and inflates the free-base cost ratio. **Tightening the free tier to fix margin will raise CAC.** There is no setting that optimizes both, and finding the balance is what the first 90 days of telemetry are for.

---

## 10. Assumptions register

Every number in this document that could not be verified. Each one names what would replace it with data.

| ID | Assumption | Value used | What would settle it |
|---|---|---|---|
| A1 | Free-to-paid conversion for a freemium running app giving away the hero feature | 3% base, 2% to 8% band | The v1.x paywall's first 60 days of RevenueCat cohort data |
| A2 | Annual-plan share of subscribers | 50% | First 90 days of plan-mix data post-paywall |
| A3 | Refund rate applies at the all-category 3.5% median rather than a Waypoint-specific rate | 3.5% | Store refund reports in the first two billing cycles |
| A4 | The Phase 5 cost bands hold at real load; A9 (the routing load test) is still open from `stack-validation.md` | $135 to $255 at MVP | The A9 load test, mandatory before any 10k-MAU sizing commitment |
| A5 | 100k and 1M MAU cost bands (carried from `stack-validation.md` A13) | $2,700 to $5,000 and $15,000 to $40,000 | Real cost-per-MAU curve measured between 1k and 10k |
| A6 | **Route generations per active user per month** (the most consequential unverified number in the cost model) | 8 | Telemetry signals 1 to 3 from the walking skeleton, which already measure generation counts and repeat-generation rate |
| A7 | Marginal share of COGS | 25% to 31% | Cost attribution once the routing tier has real traffic |
| A8 | Annual price set at 10x monthly | Ten times | `revenue-model.md` |
| A9 | Founder draw | $5,000 to $9,000 per month | Founder decision, not research |
| A10 | Post-launch contractor retainer | 0.25 to 1.0 FTE at $65 to $75 per hour | Actual maintenance load after launch |
| A11 | Tools, accounting, legal, insurance run-rate | $900 to $3,100 per month | Real quotes at incorporation |
| A12 | Non-labor build cost (counsel, design, devices, entity) | $32,000 | Quotes; the ODbL counsel review is already an open question from Phase 5 |
| A13 | Renewal rates beyond the first cycle | Base 0.60 / 0.70 / 0.75 annual, 0.70 / 0.80 / 0.88 monthly | 18 to 24 months of Waypoint cohort data; nothing sooner |
| A14 | 160 billable hours per contractor person-month | 160 | Contractor agreements |
| A15 | Organic CAC, excluding founder time | $12 base, $5 to $25 | Attribution on the first 1,000 organic subscribers |
| A16 | Paid CAC base case | $160 per subscriber (CPI $4.00 at 2.5% download-to-paid) | A $2,000 to $5,000 Apple Search Ads test post-paywall |
| A17 | Category benchmarks generalize to a route-generation app with no direct comparable | Health and Fitness medians throughout | Waypoint's own cohorts; no external source can settle this |
| A18 | RevenueCat RLTV figures are comparable to our net-of-commission LTV | Treated as broadly comparable | RevenueCat methodology detail; the comparison in 5.3 is directional only |
| A19 | 11 of the 29 to 31 person-months are founder time and cost no cash | 11 pm | The actual staffing plan at build start |
| A20 | Fixed operating cost stays flat as the user base grows to break-even | Flat | It will not stay perfectly flat; support load rises with users |

### 10.1 What the walking skeleton must measure

The skeleton reaches TestFlight at month 3 to 4 with 20 to 50 runners [verified, `mvp-scope.md` Section 6]. Its telemetry should be instrumented to retire the cost-side assumptions, because those are the ones that cannot be fixed later without re-architecting.

1. **Route generations per active user per week** (retires A6, the single highest-consequence assumption). Instrument the distribution, not just the mean; the tail is what buys servers.
2. **Generation latency and CPU-seconds per generation under real constraint mixes**, separately for the fast contraction-hierarchy path and the expensive `custom_model` path (retires A4 and A7, and tells you whether the free-and-paid split in 4.5 item 2 is even necessary).
3. **Peak concurrent generation requests per 100 actives** (this is what determines node count, and therefore the step function that dominates COGS).
4. **Actual per-service spend against the Phase 5 forecast**, monthly, so the cost band narrows from $135 to $255 into a real number before the paywall ships.
5. **Device eligibility for on-device Foundation Models** (already required by `stack-validation.md` condition; it changes the AI-positioning risk in 5.1).

### 10.2 What the first 90 days after launch must measure

Launch is free, so these are the pre-paywall signals that decide whether the paid layer is even ready to ship (the GD-1 gate in `mvp-scope.md`).

1. **Week-4 retention of users who generated at least one route** (the GD-1 bar, directionally 20 percent or better). Without this, do not ship the paywall.
2. **Cost per active user, measured not modeled** (retires A4, A5, A7 and the entire Section 4 crossover analysis).
3. **Acquisition mix by source, with organic and paid separated at the subscriber level, not the install level** (retires A15 and A16, and settles the number one sensitivity variable). Cost per subscriber by channel, not cost per install; the sourced Airbridge example shows CPI-based budget decisions systematically scaling the most expensive subscriber channel.
4. **Free-tier generation distribution across the whole base**, specifically the 95th and 99th percentiles (confirms or kills the tail risk in 4.4).
5. **Day-0 activation rate**, meaning the share of installs that complete one generate-run-save loop in the first session (55 percent of trial cancellations happen on Day 0, so this is the highest-leverage conversion input).

Once the paywall ships in v1.x:

6. **Download-to-paid and free-active-to-paid conversion, tracked separately** (retires A1, the number two sensitivity variable).
7. **Plan mix and first renewal rate on both plan durations** (retires A2 and starts retiring A13, the number three sensitivity variable).
8. **Refund rate in the first billing period, split by plan and by acquisition source** (retires A3).
9. **Involuntary churn on Google Play specifically.** Nearly a third of Play subscription cancellations are billing failures, more than double the App Store's 14 percent [verified, RevenueCat SOSA 2026, accessed 2026-08-06], and most of it is recoverable with dunning. On a dual-platform launch this is free money left on the table if unmeasured.

---

## Open questions

- What price does `revenue-model.md` land on, and does it sit inside the $4.99 to $11.99 band modeled here? Every table above must be re-read against it. #open-question
- Can `gtm-plan.md` credibly deliver 85 to 95 percent organic acquisition? Below roughly 90 percent organic, LTV/CAC does not clear 3:1 at any price in the band. This is the single largest open dependency in the model. #open-question
- Does the AI-app retention penalty (churn 30 percent faster, annual 12-month retention 21.1 percent versus 30.7 percent) apply to Waypoint, given that the product is positioned on routes rather than on AI? #open-question
- Should the paid tier launch at all below roughly 5,000 monthly actives, given that gross margin is negative to thin at MVP scale (Section 2.2)? This is a sequencing question `revenue-model.md` and `gtm-plan.md` jointly own. #open-question
- Where does the contractor sourcing decision land? It moves the build-repayment target by roughly 40 percent. #open-question

## Related

- `research/06-business-model/revenue-model.md` (sets the price; this document is subordinate to it on pricing)
- `research/06-business-model/gtm-plan.md` (owns the organic acquisition share, the number one sensitivity variable)
- `research/05-product/api-integration-map.md` (Sections 8.2 and 8.3, the verified cost base)
- `research/05-product/database-deep-dive.md` (the DEC-009 data-layer costs that correct that base)
- `research/05-product/stack-validation.md` (Section 5, the cost curve to 1M MAU)
- `research/05-product/mvp-scope.md` (build effort, GD-1 free-launch gate)
- `research/01-market/market-sizing.md` (SOM, the sanity check on break-even reachability)
- `research/02-competitors/pricing-matrix.md` (the price umbrella and the freemium boundary)
- `vault/02-Decisions/DEC-008`, `DEC-009`, `DEC-010` (free launch, data layer, platform and effort)
- `research/00-RESEARCH-PLAYBOOK.md` (standards followed here)
