---
type: decision
id: DEC-011
status: accepted
created: 2026-08-06
updated: 2026-08-06
tags: [decision, pricing, revenue, free-tier, phase-6]
---

# DEC-011 Pricing and the permanent free tier

## Context

DEC-008 established that v1 launches entirely free and that safety-aware routing stays free permanently, but left the eventual price and the exact free/paid boundary undecided. Phase 6's `research/06-business-model/revenue-model.md` set both against the competitor pricing matrix, the personas' willingness to pay, and verified 2026 category subscription data.

## Decision

Approved 2026-08-06 at the Phase 6 gate:

| Item | Decision |
|---|---|
| Annual list | **$99.99 per year** |
| Monthly list | **$12.99 per month** |
| Annual discount | 36 percent off the monthly run rate, merchandised as "$8.33 a month, billed annually" |
| Trial | 21 days, annual plan only, store-billed |
| Free-era cohort | **Founding Runner: $69.99 per year, price-preserved for as long as the subscription stays active** |
| Lifetime tier | **No** |
| Second paid tier | **No at v1.x** (architected for, not shipped) |
| Data or location monetization | **Rejected on the record** |

**The free tier, permanently:** everything in MVP v1, plus every remaining routing constraint (crossings, weather, surface), plus the Watch app, GPX export, and the preference-learning loop. **The paid tier is the coaching layer alone**, one nameable job: "your training, routed." The permanent free tier is to be **named publicly at launch**, before anyone has paid anything.

## Rationale

- **$99.99 is the right rung on the ladder.** It sits 17 percent under Runna's $119.99 while doing something Runna cannot do at all, a third under the $149.99 assembled Strava-plus-Runna alternative, and clearly above the utility band where Komoot (€59.99) and Footpath ($23.49) live. `pricing-matrix.md` independently derived the same $79.99 to $119.99 band from the competitor side; the revenue model reached the same place from the persona side.
- **Pricing at the top of the band is supported, not contradicted, by conversion data.** Higher-priced apps in this category convert *better* at the download-to-paid step (2.8 percent high band versus 1.4 percent low) and generate roughly six times the year-one lifetime value per payer. Nothing in the data supports discounting into the utility band to buy conversion.
- **The higher price also relaxes the acquisition constraint.** At $99.99 the base lifetime value is $107 rather than the $86 at the $7.99 mid case, which drops the organic-acquisition share needed to clear a 3:1 ratio from roughly 90 percent to roughly 84 percent. Pricing and distribution are coupled, and this is the favorable direction.
- **List high and discount, never the reverse.** Apple applies price decreases silently and automatically, but increases above roughly 50 percent or $50 a year require explicit consent from every existing subscriber, and non-consenting subscriptions simply expire. Launching at $69.99 and reaching $99.99 later would be a consent-required event across the entire base. Discounts, offer codes, and regional pricing remain fully reversible.
- **The generous free tier is a deliberate strategic asset, not a concession made by accident.** Naming it publicly at launch, before anyone has paid, is what makes the later paywall a non-event. Promising it at the moment of the paywall announcement reads as damage control.
- **Lifetime is rejected on category behavior and cost structure.** Health and fitness has the lowest lifetime-plan share of any app category while leading annual adoption, and route generation carries genuine per-user compute cost, so a lifetime plan converts a recurring cost into an unfunded perpetual obligation. The Founding Runner rate delivers the same emotional payload with none of the liability, and both stores support price preservation operationally.

## Alternatives considered

- **Price lower to buy conversion.** Rejected: the category data points the other way, and pricing into the utility band re-frames the product as a utility.
- **Price at or above Runna's $119.99.** Rejected: Waypoint cannot out-brand the category leader at launch, and the first-renewal penalty on high-priced annual plans (24 percent versus 37 percent) is steeper than the revenue gain at this stage.
- **Hold back one routing constraint, or the Watch app, as future paid.** Rejected in favor of the clean promise. The escape hatch was considered explicitly and declined; see the consequence below.
- **A cheaper tier for beginners.** Rejected: beginners are served by the free tier being genuinely complete, not by a stripped paid tier that fragments the proposition.

## Consequences

- **The paid product now rests entirely on one job.** If training-state-aware generation turns out not to be felt value, there is no second paid thing to fall back on at v1.x. Its demand evidence is inferred from the category's total absence of it rather than verified from anyone paying for it. This is the deepest unknown in the business, and no price fixes it. #risk
- **The escape hatch was declined deliberately.** Every routing constraint, the Watch app, and GPX are free forever. Reversing any of that later is a trust event, not a pricing change, and should be treated as requiring a superseding decision plus a public explanation. #risk
- Revenue is zero for months 1 through 9 by design; first revenue lands months 10 to 12.
- Founding Runner status is identified through StoreKit 2 and Play Billing entitlements at the paywall date.
- **Verification still open:** whether a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores. A 30-minute check in App Store Connect and Play Console that prevents a launch-week surprise. #open-question

## Related

- `research/06-business-model/revenue-model.md`, `business-model-canvas.md`, `unit-economics.md`
- [[DEC-008 Phase 5 gate MVP approved stack in validation]] (free launch, permanent free safety routing)
- [[DEC-013 Home-metro beachhead and iOS-first public launch]]
- [[_Decision-Log]]
