---
type: knowledge
created: 2026-08-06
updated: 2026-08-06
tags: [knowledge, research, business-model, pricing, gtm, metrics, phase-6]
---

# Business Model and GTM Key Findings (Phase 6)

Distilled from `research/06-business-model/` (5 documents: business-model-canvas, revenue-model, unit-economics, metrics, gtm-plan). Governed by [[DEC-006 Concept lock route-first positioning]], [[DEC-008 Phase 5 gate MVP approved stack in validation]], and [[DEC-010 Staged cross-platform MVP on React Native]]. **Gate CLOSED 2026-08-06:** [[DEC-011 Pricing and the permanent free tier]], [[DEC-012 Measurement corrections analytics identity and re-based targets]], [[DEC-013 Home-metro beachhead and iOS-first public launch]].

## The finding that governs everything else

**Waypoint's unit economics are a function of its distribution strategy, not its pricing.** Paid acquisition costs roughly $160 per subscriber (a $4.00 cost-per-install divided by a 2.5 percent download-to-paid rate) against a lifetime value of $86 to $107 depending on price. That returns 53 to 70 cents on the dollar at every price in the credible band. The model clears the conventional 3:1 bar only at roughly **84 percent or better organic acquisition** at the recommended $99.99 price point.

The go-to-market plan independently rejects paid acquisition pre-funding, on separate reasoning: a bought install before month 10 has a lifetime value of exactly zero and contaminates the retention signal the MVP exists to produce. So the plans agree, and they agree for different reasons, which is the strongest kind of agreement. But the dependency is permanent: **if community-first distribution fails, no price rescues the model.**

## Pricing

- **$99.99 per year list**, $12.99 per month, 36 percent annual discount merchandised as "$8.33 a month". 21-day trial, annual plan only.
- **Founding Runner: $69.99 per year, price-preserved indefinitely** for the free-era cohort. Same emotional payload as a lifetime deal, none of the unfunded liability.
- **Lifetime tier rejected**: health and fitness has the lowest lifetime-plan share of any category, and route generation carries real per-user compute cost.
- **Data and location monetization rejected on the record**: contradicts the privacy architecture that is the structural advantage.
- **List high and discount, never the reverse.** Apple applies price decreases silently but requires explicit consent for increases above roughly 50 percent or $50 a year. Launching at $69.99 and reaching $99.99 later would be a consent-required event across the entire base.
- Anchors: Runna $119.99/yr, Strava $79.99/yr, the assembled Strava+Runna alternative $149.99/yr, AllTrails Peak $79.99/yr, RunGo $59.99/yr, Footpath $23.49/yr. Waypoint sits under Runna and a third under the assembled alternative, well above the utility band.
- Category data supports pricing at the top of the band: higher-priced apps convert **better**, not worse, at the download-to-paid step (2.8 percent high band vs 1.4 percent low).

## Unit economics

- Gross margin per subscriber: **63 percent at the mid price at 10k monthly actives**, 78 percent at 100k, 84 percent at 1M. Negative at MVP scale, because a ~$195/month infrastructure floor spread across ~30 payers exceeds net revenue per subscriber.
- ~~Break-even ~3,000 paying subscribers against a $15,000/month base; ~6,800 held for a year also repays the ~$230,000 cash build.~~ **SUPERSEDED by [[Financial Strategy and Founding Team (Phase 9)]].** Both inputs assumed a solo founder with contractors. Against the real team's ~$1,050/month post-launch base, **break-even is ~235 paying subscribers**, and there is no $230,000 build to repay. Do not quote the 3,000 figure.
- **A free active user costs under $1 per year.** "Free users are expensive" is false in absolute terms. What bites is revenue share: the free base consumes 55 percent of net subscription revenue at 2 percent conversion, 36 percent at 3 percent, and becomes a rounding error above roughly 5.3 percent.
- Net revenue multiplier **0.8088** after the 15 percent store commission, RevenueCat's ~1.4 percent of net, and a 3.5 percent refund allowance.
- The three variables that move the outcome: **organic share of acquisition** (an 8.4x swing in blended acquisition cost), **free-to-paid conversion**, and **annual first-renewal rate**. Price is a distant fourth; infrastructure cost does not make the top five.
- The uncomfortable interaction: the first two pull against each other, because the generous free tier that keeps acquisition cost low is the same thing that suppresses conversion.

## Metrics

- **North Star: Weekly Routed Runners** — distinct runners completing two or more generated routes in a rolling seven days, with an 80 percent completion floor inside the definition so it cannot be inflated by abandoned routes.
- Rejected alternatives, each for a specific failure: raw monthly actives (inflatable by the Android launch), total routes generated (**rises when routes are bad**, since rejection drives regeneration), total distance run (a GPS-tracker-only cohort would score perfectly while refuting the hypothesis).
- **Activation: first generated route completed as a recorded run within seven days of install.** The PRD's current "generate and start" definition counts mid-run abandonment as success, which is the exact bad-route signature the MVP needs to see. Paired with "Ignition", the daily-readable share of first sessions reaching a route on screen under 180 seconds.
- **Route quality**: eleven behavioral signals collapsed into a weekly **Good Route Rate**. Strongest positive proxy is the 30-day repeat rate; quietest negative is the reveal abandon rate. Investigate below 65 percent, stop feature work below 50 percent.
- **The guardrail that matters most: honest-refusal rate stability.** The easiest way to lift acceptance is to quietly relax constraints when the engine struggles, and a product whose honest refusals disappear looks like a product that got better.

## Go-to-market

- **Beachhead: one metro, one segment.** The urban committed amateur running three to five times a week from a home doorstep, women runners as the highest-intensity cohort, travelers as demo carriers rather than the target. Geographic concentration is structural: route quality depends on OpenStreetMap pedestrian data density and crossings are the hardest features to map.
- **Channels ranked**: run clubs (new Strava clubs nearly quadrupled in 2025; the channel solves the demo problem because the value is invisible in a screenshot and obvious in ninety seconds in person), Reddit and forums, store optimization as mandatory infrastructure, build-in-public as a cheap lottery ticket, creators, press as a one-shot asset.
- **Two popular channels argued against**: SEO content (AI Overviews cut clicks 39.8 to 58 percent, payback past the competitive window) and paid acquisition (unaffordable and signal-contaminating pre-revenue).
- **The plan recommended the Android date as the real public launch, and that recommendation was OVERRIDDEN at the gate.** Its reasoning was that iOS at month 9 to 10 should be a quiet quality burn-in, since the one-shot assets can only be spent once and a mixed-platform run club is the wrong room in which to tell half the people "not yet". [[DEC-013 Home-metro beachhead and iOS-first public launch]] rejected this. **The iOS date carries the public launch.** See the gate outcome below for the reasoning and the four compensating conditions.
- **Paywall transition: never take anything away.** Gate only capability that did not exist the day before, name the permanent free tier publicly at launch before anyone has paid, grandfather the pre-paywall cohort by name, give 30 days' notice, and hold it behind the week-4 retention bar.

## Cross-document catches worth remembering

- **Three conversion numbers with three different denominators** and they must never be quoted side by side: 2/4/7 percent of *installs at the paywall date* (revenue model), 4 to 8 percent of *week-4-retained users* (GTM), 2/3/5/8 percent of *free active users* (economics).
- The revenue model plans on ~30 percent first-year annual renewal; the economics model uses the verified category median of 36 percent as base and 24 percent as pessimistic. The revenue model is the more conservative of the two, which is the safe direction to differ in.
- Both independently flag that **AI-branded apps earn ~41 percent more per payer but churn ~30 percent faster**, which argues for marketing the utility of the route rather than the intelligence behind it. DEC-006's "Know where to run" already does this.

## Gate outcome (all six closed 2026-08-06)

1. **Price approved as recommended** (DEC-011).
2. **Free/paid boundary approved, escape hatch declined** (DEC-011). Everything but the coaching layer is free forever, including all routing constraints, the Watch app and GPX, and the free tier is named publicly at launch. The paid product now rests on one job, and if training-state-aware generation is not felt value there is no fallback at v1.x.
3. **Analytics fixed with a first-party Postgres cohort table** on the existing account identifier; TelemetryDeck keeps aggregate signals; PostHog EU deferred to v1.x (DEC-012).
4. **PRD G3 and G4 re-based** to activated-cohort definitions with a separate install-level benchmark line; activation redefined as a completed recorded run (DEC-012).
5. **Beachhead: the founder's home metro**, subject to the month-1 pedestrian-data spike (DEC-013).
6. **Launch shape OVERRIDDEN: the iOS date at month 9 to 10 carries the public launch** (DEC-013). The Apple featuring nomination is iOS-only, speed matters in a 12 to 18 month window, and iOS carries ~85 percent of category subscription revenue. Losing the quiet burn-in attaches four conditions: the month-8 beta cohort target becomes a hard gate on the launch date, reviews are seeded from that cohort behind a 99.5 percent crash-free release gate, Android waitlist capture starts at launch, and the featuring nomination is filed at month 6 to 7.

## Riskiest assumption in the phase

**A1: that the beachhead metro clears the OpenStreetMap pedestrian-data floor.** It sits underneath the segment choice, the metro choice, the top-ranked channel, and the differentiation claim. The month-1 buildability spike answers it before marketing effort is committed, which is why that spike should be treated as a **go-to-market gate**, not merely a technical one.

## Related

- [[Product Definition Key Findings (Phase 5)]]
- [[Concept and Positioning (Phase 4)]]
- [[DEC-008 Phase 5 gate MVP approved stack in validation]]
- [[DEC-010 Staged cross-platform MVP on React Native]]
