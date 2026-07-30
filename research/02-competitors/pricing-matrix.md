# Competitive Pricing Matrix

Version-Timestamp: 2026-07-30 14:50:00 UTC-4

This matrix consolidates pricing, trials, free tiers, and bundles from the ten competitor profiles (all prices as checked 2026-07-30 in the profiles; the profiles carry the URLs). The market shows a clear two-band structure: route and navigation utilities price between about $24 and $80 per year with real free tiers, while coaching apps price between about $80 and $156 per year with little or no free tier. The umbrella is bounded below by Garmin Connect+ at $69.99 per year (with free Garmin Coach plans under it) and above by the Strava + Runna bundle at $149.99 per year. Free web generators anchor basic loop generation at zero, which directly shapes what Waypoint can charge for.

## Core competitor pricing

| Competitor | Free tier (what is actually free) | Monthly | Annual | Trial | Bundles / other tiers | Source |
|---|---|---|---|---|---|---|
| Runna | None meaningful; subscription gated | $19.99 | $119.99 | 1 week (2 with promo codes) | Strava + Runna $149.99/yr (annual only, not purchasable in iOS app) | `profile-runna.md` |
| TrainAsONE | Real but limited: 7-day plan detail, pace-based workouts, single goal, basic analysis | £9.99 | £99.00 | 21 days, no credit card | None | `profile-trainasone.md` |
| AI Endurance | None | $25.89 (monthly billing) | $12.99/mo billed annually (approx. $155.88/yr) | 14 days, no upfront payment | B2B coaching portal for clubs | `profile-ai-endurance.md` |
| Coopah | None | $14.99 (also £14.99) | $79.99 (also £79.99); $29.99/quarter | 1 week (2 with promo/partner codes) | "Coopah Coaching" IAP tier at $119.99 to $159.99/yr (scope unconfirmed) | `profile-coopah.md` |
| Joggo | None; quiz-funnel checkout, no trial | ~$33 reference; store IAPs $49/mo | ~$93.99 to $99.99 (12-month IAP); funnel prices vary widely by cohort | None | Paid workout add-ons ($19.99); Kilo Health B2B wellness bundles | `profile-joggo.md` |
| Komoot | Route planning, community content, core navigation | €6.99 (web); €4.99/week (mobile) | €59.99 (also $59.99 / £59.99) | Not documented | Legacy one-time map packs ended Feb 2025 for new users | `profile-komoot.md` |
| AllTrails | Trail discovery, basic weather | Not documented (annual-led) | Plus $35.99; Peak $79.99 | 7 days (Peak, at launch) | Two-tier ladder (Plus, Peak) | `profile-alltrails.md` |
| Strava | Activity tracking, social feed, clubs, basic heatmap view; ALL routing features paid | $11.99 | $79.99 | Not documented in profile | Student $39.99/yr, Family $139.99/yr, Strava + Runna $149.99/yr | `profile-strava-routes.md`, `adjacent-platforms.md` |
| Footpath | 5 saved routes, core drawing | $3.99 | $23.49 | 7 days | $1.99 single route pass | `profile-footpath-rungo.md` |
| RunGo | Follow routes, log runs | $5.99 | $59.99 | Not documented | $119.99 lifetime; Creator tier $19.99/mo or $199/yr (route publishers) | `profile-footpath-rungo.md` |

## Price context: adjacent platforms and the free floor

| Player | Free | Paid | Source |
|---|---|---|---|
| Garmin | Garmin Coach adaptive plans, training load, readiness, VO2 max (free with watch hardware) | Connect+ $6.99/mo or $69.99/yr | `adjacent-platforms.md` |
| Apple | Core Watch running features, Workout Buddy (with capable hardware) | Fitness+ $9.99/mo or $79.99/yr | `adjacent-platforms.md` |
| Nike Run Club | Everything (plans, guided runs, tracking) | Nothing; free by strategic design | `adjacent-platforms.md` |
| WHOOP | Nothing | $199 to $359/yr, hardware included | `adjacent-platforms.md` |
| Web route generators (Routeshuffle, Circa, Route Random, JustGo, Run Randomizer) | Basic loop generation from start point plus distance | Routeshuffle Premium $5/mo or $49/yr (saving, export, surface and lighting detail) | `profile-footpath-rungo.md` |

## Price umbrella analysis

Where the market sits:

- Route and navigation utilities: $23.49 (Footpath) to $79.99 (AllTrails Peak), with Komoot and RunGo at $59.99 and Strava at $79.99. All have genuine free tiers. [verified across profiles]
- Coaching apps: $79.99 (Coopah) to roughly $156 (AI Endurance annualized), with Runna at $119.99 as the category leader's reference price. Free tiers are absent or token (TrainAsONE is the only real one). [verified across profiles]
- The ceiling: Strava + Runna at $149.99 per year is the most expensive pure-software running offer, and it bundles the two things Waypoint combines (community routes plus adaptive coaching). [verified, `profile-runna.md`]
- The floor: Garmin Coach adaptive plans are free with a watch, Nike Run Club is entirely free, and hobby web generators give away basic loop generation. Garmin Connect+ at $69.99 sets the low end of paid AI-flavored coaching. [verified, `adjacent-platforms.md`, `profile-footpath-rungo.md`]

What positioning is available to Waypoint. [inferred, reasoning below]

- The credible band is roughly $79.99 to $119.99 per year (about $9.99 to $14.99 per month). Below $79.99 signals a utility and undercuts the coaching value story; above $119.99 asks a solo-founder startup to out-price Runna's brand, and above $149.99 collides with the full Strava + Runna bundle, which the adjacent-platforms profile assumes caps what a committed amateur pays for running software (its [assumption] 7: users hold at most one or two running subscriptions).
- The structural opening is that nobody prices the combination. A runner today assembling Waypoint's promise needs Runna ($119.99) plus Strava ($79.99, for routes) or the $149.99 bundle, and still gets no constraint-based generation. Waypoint at around $99.99 per year would undercut the assembled alternative while pricing above the utility band, signaling coaching-grade value. [inferred]
- Coopah at $79.99 proves committed amateurs accept that price for coaching alone; RunGo at $59.99 proves runners pay for navigation execution alone (`profile-coopah.md`, `profile-footpath-rungo.md`). A product doing both plausibly supports the mid point of those anchors plus a premium.

## Freemium boundary patterns

What competitors gate free versus paid:

- Coaching apps gate the product itself. Runna, Coopah, AI Endurance, and Joggo have no meaningful free tier; the plan is the paywall and trials (1 to 3 weeks) carry acquisition. TrainAsONE's free tier exists but users call it "so limited as to be unworthy of anyone's time" (`profile-trainasone.md`). [verified]
- Route platforms give away discovery and gate depth. Komoot: planning free, offline maps and device sync paid. AllTrails: discovery free, offline and navigation in Plus, AI custom routes in the top Peak tier. Strava: tracking and social free, every routing feature (Suggested Routes, Route Builder, point-to-point, offline) subscriber-only (`profile-komoot.md`, `profile-alltrails.md`, `profile-strava-routes.md`). [verified]
- Notable pattern: both AI routing incumbents put generation at the TOP of the ladder (AllTrails Peak, Strava subscription), while hobby web tools give basic generation away free. The paid boundary the incumbents chose is generation itself; the free market says basic generation is worth zero. [verified from profiles; the tension is the finding]
- Cautionary pattern: Joggo's funnel pricing and adversarial refunds, Runna's bundle billing friction, and Komoot's paywall expansion each generated documented trust damage (`profile-joggo.md`, `profile-runna.md`, `profile-komoot.md`). Freemium mechanics are a trust surface, not just a conversion lever.

Implication for Waypoint's H4 (free basic routes, paid adaptive layer). [inferred]

- H4's boundary placement looks right and is arguably forced. Basic loop generation cannot be the paid gate: free web tools and a $79.99 Strava subscription already commoditize it, and Strava gating ALL routing behind its paywall leaves "genuinely free basic route generation in a polished iOS app" as an open acquisition play no incumbent offers.
- The paid tier must be the adaptive layer: constraint depth (weather, crossings, safety, surface), plan-aware generation, and personalized coaching. This mirrors where every profiled user community assigns value and matches the RunGo and Coopah willingness-to-pay evidence.
- The risk to H4 is the coaching-app pattern: every direct coaching competitor found free tiers unworkable and went trial-first. Waypoint's free tier therefore needs a strict cost ceiling per free user (generation compute, map data) and a sharp upgrade trigger, or it becomes subsidy without conversion. TrainAsONE shows a too-thin free tier actively annoys; Joggo shows no-free-plus-dark-patterns destroys trust. The workable pattern is Komoot/AllTrails style: real daily utility free, depth and intelligence paid.

## Assumptions

- [assumption] All prices are as captured in the profiles on 2026-07-30; several profiles flag regional variation, promo cohorts (Joggo especially), and history of price changes (Runna). Treat any single figure as a snapshot.
- [assumption] Currency mixing (Runna and Coopah in USD, TrainAsONE in GBP, Komoot in EUR) is left as sourced; no FX conversion applied. £99 and €59.99 are treated as roughly comparable to their USD figures for banding purposes.
- [assumption] The committed amateur holds at most one or two running subscriptions, so the $149.99 bundle is an effective ceiling on Waypoint's pricing headroom (carried from `adjacent-platforms.md` assumption 7).
- [assumption] The Coopah Coaching IAP tier ($119.99 to $159.99) is a premium human-coaching bundle; unconfirmed by company documentation per `profile-coopah.md`.
- [assumption] Strava's trial policy and Komoot's trial policy were not captured in the profiles; their absence in the table is a research gap, not evidence of no trial.
