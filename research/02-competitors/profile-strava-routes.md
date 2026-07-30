# Competitor Profile: Strava Routes (routing and route recommendation capabilities)

Version-Timestamp: 2026-07-30 14:30:00 UTC-4

Scope note: this profile covers Strava's routing and route recommendation capabilities only; a separate profile covers Strava as a platform.

Strava is the only profiled competitor with true on-demand route generation: subscribers can generate loop routes from any start point filtered by sport, distance, elevation preference, and surface preference, ranked by Global Heatmap popularity, refreshed with an "AI-powered Routes" engine in May 2025. Through mid-2026 it added tappable points of interest, point-to-point routing, a night heatmap, hiking route tools, Samsung Health routes integration, and Runna-powered Race Discovery, making Routes a fast-moving flagship of the subscription. What it still does not do is adapt routes to training needs: no workout-length targeting from a plan, no weather, street crossing, or safety constraints, and community reports of dangerous road suggestions persist.

## Company snapshot (routing-relevant facts)

- Strava: private, San Francisco, more than 195 million users in over 185 countries as of June 2026 (150 million plus at the April 2025 Runna acquisition). [verified] (Strava press, "Strava Adds New Features for Hiking...", https://press.strava.com/ea/articles/strava-adds-new-features-for-hiking-making-the-outdoor-experience-more-discoverable-navigable-and-social, accessed 2026-07-30; Strava press, "Strava to Acquire Runna, A Leading Running Training App", https://press.strava.com/articles/strava-to-acquire-runna-a-leading-running-training-app, accessed 2026-07-30)
- Acquired Runna (UK, founded 2021, personalized running training plans, an Apple App of the Year finalist 2024) in April 2025; terms undisclosed. Apps continue to operate separately. [verified] (Strava press Runna announcement above; Wareable, "Strava makes its first big move since acquiring Runna: a combined subscription", https://www.wareable.com/sport/strava-runna-combined-subscription-announcement-price, accessed 2026-07-30)
- Revenue not public; subscription-driven. [verified that no public figure exists in reviewed sources]

## Route capabilities in depth

Suggested Routes (the core generator, subscriber-only, mobile Maps tab):

- Constraint parameters accepted: start location (current location, any address, or dropped pin), sport type (run, ride, walk; originally run and ride), distance (preset target values), elevation preference (flat, hilly, or any), surface preference (paved, dirt, or any). Generates three or more loop options that return to the start, ranked by community popularity from the Global Heatmap plus OpenStreetMap data. [verified] (DC Rainmaker, "Strava Rolls Out Significant New Routes Feature", https://www.dcrainmaker.com/2020/03/strava-significant-feature.html, accessed 2026-07-30; Strava Community Hub, "Spotlight on Maps and Routes", https://communityhub.strava.com/insider-journal-9/spotlight-on-maps-and-routes-1498, accessed 2026-07-30; MakeUseOf, "How to Use Strava Routes to Discover New Places to Exercise", https://www.makeuseof.com/how-to-use-strava-routes/, accessed 2026-07-30)
- Outputs per suggestion: map, distance, elevation profile, difficulty, terrain and surface breakdown, community photos, estimated time, active times (when the route is most popular, positioned partly as a crowd-avoidance and comfort signal). [verified] (Strava Stories, "Strava Routes and Heatmap: Find New Places to Go", https://stories.strava.com/ea/articles/strava-routes-and-heatmap-how-to-find-new-places-to-go, accessed 2026-07-30)

May 2025 "AI-powered Routes" refresh and follow-ons:

- Updated Routes engine described as "AI-powered... smarter, intuitive suggestions by leveraging Strava's Global Heatmap", generating community-backed routes from current location or any custom start. [verified] (Strava press, "Strava Unveils Suite of New Subscriber Features", https://press.strava.com/pb/articles/strava-unveils-suite-of-new-subscriber-features, accessed 2026-07-30)
- Tappable Points of Interest (June 2025): tap a cafe, restroom, or viewpoint to generate a route to it or routes that include it. [verified] (same press release)
- Point-to-Point Routing (July 2025): drop a pin, get the most efficient activity-specific A to B route on mobile; for running it prefers pedestrian-friendly paths. [verified] (same press release; Runner's World UK, "Strava steps up its AI-powered routes and leaderboard policing", https://www.runnersworld.com/uk/news/a64840682/strava-running-updates-2025/, accessed 2026-07-30)
- Night Heatmap: a map layer of popular after-dark routes, explicitly framed around visibility and safety. It is a display layer, not a routing constraint. [verified] (GearJunkie, "Latest Strava Updates Use AI to Recommend Routes, Level Leaderboards, and More", https://gearjunkie.com/technology/strava-updates-2025-ai-routes, accessed 2026-07-30)
- June 2026 hiking update: subscriber Route Discovery (popular routes anywhere), Route Builder with live distance, elevation, and surface feedback, route saves, offline routes, richer trail surface data later in summer 2026. [verified] (Strava press hiking release above)
- July 2026: Samsung partnership with Routes integration into Samsung Health; Race Discovery brings Runna's race database into Strava's new Events tab (July 9, 2026). [verified] (press items listed on Strava press releases above, accessed 2026-07-30)

Runna integration status (through 2026-07-30):

- The $149.99 per year Strava + Runna bundle (July 2025) markets "personalized routes linked to your training plan" as a bundle benefit. Exactly what this does is unclear from available sources; the Strava help center describes it as "custom Route recommendations based on your location" plus Runna's coaching, which reads as existing Suggested Routes rather than workout-aware generation. Weighting: the help center FAQ is more precise and operational than the marketing bullet, so treat workout-aware route generation as NOT shipped. [verified conflict] (Strava press, "Strava + Runna Launch Combined Subscription Bundle", https://press.strava.com/articles/strava-runna-launch-combined-subscription-bundle, accessed 2026-07-30; Strava support, "Strava and Runna Subscription FAQs", https://support.strava.com/en-us/articles/15401576, accessed 2026-07-30)
- Deeper integrations so far are training and events focused (Race Discovery, workout detail in feed), not routing focused. [verified] (press items above)

Parameters not accepted: workout or training plan distance targeting (beyond manual distance presets), elevation gain targets in meters, weather or heat, street crossings, traffic, lighting or safety as constraints, personal history ("roads you have not run"). Personalization is popularity-based (everyone in a locale sees community favorites), not individual-based. [inferred from complete absence in documentation and reviews; the "AI" label refers to heatmap-driven suggestion quality]

## Pricing (2026, US)

- Free tier: activity tracking, basic heatmap view; Suggested Routes, Route Builder, point-to-point, offline routes are all subscriber features. [verified] (MakeUseOf above; Strava hiking press release above)
- Individual subscription: $11.99 per month or $79.99 per year plus tax. Student $39.99 per year, Family $139.99 per year, Strava + Runna $149.99 per year (annual only). [verified] (Strava, "Pricing", https://www.strava.com/pricing, accessed 2026-07-30)

## Positioning

Routes is positioned as "the most dynamic and dependable routing tool for any activity, all in one place", with the community data moat (billions of activities) as the differentiator: "run, ride, or walk like locals wherever they go". Routing is a subscription-conversion feature, not a standalone product. [verified] (Strava May 2025 press release above)

## Strengths and weaknesses

Strengths:

- Only competitor with genuine on-demand generation by distance, elevation, and surface from any start point. [verified] (capability analysis above)
- Unmatched data moat: the Global Heatmap encodes where millions of runners actually run, a proxy for runnability and (imperfectly) safety that no startup can replicate. [verified for the data scale; inferred for the moat judgment]
- Massive distribution (195 million plus users) and now owns Runna, the leading running coaching app, giving it all the pieces (routes plus adaptive training) under one roof. [verified] (sources above)
- Rapid shipping cadence on maps and routes through 2025 to 2026. [verified] (press timeline above)

Weaknesses:

- [verified] Route quality and safety complaints: users report generated routes on interstates and busy shoulder-less roads, with no way to flag dangerous roads (details in sentiment section).
- [inferred] Popularity is not personalization: suggestions ignore the individual's training state, preferences, and history; two different runners at the same corner get the same routes. Reasoning: no documented personal inputs beyond the four filters.
- [inferred] Routes plus Runna are not yet connected at the workout level; a Runna user still picks a route manually for today's prescribed 8 km tempo. Reasoning: help center description and absence of any launch announcement through 2026-07-30.
- [inferred] Multi-sport surface area means running-specific route depth (crossings, lighting, footing) is unlikely to be prioritized over broadly applicable features. Reasoning: 2025 to 2026 roadmap invested in hiking, POIs, and partnerships rather than run-specific constraints.

## Review sentiment and common complaints

- "AI-generated route generator creates lousy routes": a Strava Community Hub user reports routes placing them on an interstate and "about 12 miles of very unsafe roads that were single lane, no shoulder, busy with traffic", concluding the routes "should just not be trusted and only used in areas you're already familiar with", and asking for time-of-day awareness and crowd-sourced "don't ride here" flags. [verified] (Strava Community Hub, https://communityhub.strava.com/strava-features-chat-5/ai-generated-route-generator-creates-lousy-routes-10052, accessed 2026-07-30)
- "Flag dangerous routing": user documents Strava suggesting an illegal turn across four lanes in Liverpool and notes there is no mechanism to flag dangerous Strava-built routes. [verified] (Strava Community Hub, https://communityhub.strava.com/strava-features-chat-5/flag-dangerous-routing-323, accessed 2026-07-30)
- Positive sentiment exists too: press and Strava's own community spotlight praise Suggested Routes for travel and breaking routine; Runner's World framed the 2025 updates as solving "what if your route is just plain boring" and unsafe-area anxiety. [verified] (Runner's World UK above; Strava Community Hub spotlight above)
- Broader complaint themes: features locked behind the subscription and route navigation friction on wearables. [verified for the paywall framing] (MakeUseOf above; community synthesis in search results, accessed 2026-07-30)

## Threat assessment for Waypoint

High threat. Strava is the only incumbent already answering a version of "where should I run from here" with real generation parameters (distance, elevation, surface), it owns both the largest runner community and, via Runna, the leading adaptive training plan product, and its 2025 to 2026 shipping pace shows routing is a strategic priority. The obvious next move (Runna prescribes today's workout, Strava generates a matching route) would directly collide with Waypoint's hero wedge, and the bundle marketing already gestures at it, though it has not shipped as of 2026-07-30. Waypoint's defensible ground is the constraint depth Strava ignores: weather and heat adaptation, street crossings, lighting and safety as first-class routing inputs, and true per-user personalization rather than popularity ranking. The documented safety complaints are also an attack surface: heatmap popularity demonstrably produces dangerous suggestions, and a safety-aware generator is a clear differentiation story. Timing risk is real; assume 12 to 18 months, not years, before Strava connects Runna workouts to route generation.

## Assumptions

- [assumption] "Personalized routes linked to your training plan" in the bundle marketing does not mean workout-aware route generation; based on the more precise help center wording, not on hands-on testing.
- [assumption] Strava's "AI-powered" Routes label describes heatmap-driven algorithms rather than a distinct generative model; no technical disclosure exists either way.
- [assumption] Suggested Routes distance options remain preset values rather than free-form input as of mid-2026; verified in earlier documentation, not re-verified on-device for the current app version.
- [assumption] No weather, crossing, or safety constraints shipped to Routes between the last reviewed press release (July 2026) and 2026-07-30.
