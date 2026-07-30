# Competitor Profile: Komoot

Version-Timestamp: 2026-07-30 14:30:00 UTC-4

Komoot is Europe's largest outdoor route planning and navigation platform, historically strongest with cyclists and hikers, acquired by Bending Spoons in March 2025 for roughly 300 million euros. Its sport-aware routing engine plans routes between user-chosen points but does not generate routes on demand from a target distance or training constraint. Post-acquisition layoffs of roughly 85 percent of staff, expanded paywalls, and a September 2025 redesign have triggered visible user backlash and subscription cancellations, leaving the product's future development capacity in doubt.

## Company snapshot

- Founded 2010 in Germany; grew into "Europe's leading outdoor platform" per its own CEO. [verified] (DC Rainmaker, "Komoot Acquired: History Says This Won't End Well", https://www.dcrainmaker.com/2025/03/komoot-acquired-history-says-this-wont-end-well.html, accessed 2026-07-30)
- Acquired by Bending Spoons (Italian technology holding, also owns Evernote, WeTransfer, Meetup, Vimeo) announced March 20, 2025, at a reported price of about 300 million euros. [verified] (DC Rainmaker, "Komoot Team Says Goodbye", https://www.dcrainmaker.com/2025/05/komoot-team-goodbye.html, accessed 2026-07-30)
- Roughly 85 percent of the approximately 150-person staff laid off within weeks of the acquisition; founders departed. [verified] (DC Rainmaker, same article above; BikeRadar, "Komoot unveils bold redesign and price increase, but few of original team remain after post-acquisition layoffs", https://www.bikeradar.com/news/komoot-redesign-2025, accessed 2026-07-30)
- Users: 45 million registered at acquisition (March 2025); company claimed over 50 million by September 2025. Conflicting figures reflect different dates, not disagreement; the 50 million figure is newer and comes from Komoot's own press release, so treat it as the current marketing number and 45 million as the independently repeated one. [verified] (Business Wire via NTB, "Komoot Unveils Modern Design as Part of Ambitious Product Roadmap", https://kommunikasjon.ntb.no/pressemelding/18653163/komoot-unveils-modern-design-as-part-of-ambitious-product-roadmap, accessed 2026-07-30; DC Rainmaker acquisition article above)
- Revenue: not public. Bending Spoons' standard playbook is price increases with minimal feature investment. [inferred] (pattern documented in DC Rainmaker, "Komoot Team Says Goodbye", above)

## Product and route capabilities

Komoot is a multi-sport planner (hiking, running, mountaineering, road cycling, gravel, MTB, e-bike variants). Running is one supported sport among many, not the product's center of gravity. [verified] (Komoot, "Create Running Routes", https://www.komoot.com/running-app/create-running-routes, accessed 2026-07-30)

Constraint parameters the route planner actually accepts:

- Sport type: the primary routing input. It determines preferred surfaces and way types (asphalt for road cycling, singletrack for MTB, runner-friendly paths for running) and traffic rule handling. [verified] (Komoot, "Create Running Routes", above; Loop, "Is Komoot the best route planner for cycling?", https://loop.cc/en-us/blogs/news/is-komoot-the-best-route-planner-for-cycling, accessed 2026-07-30)
- Start point, destination, and intermediate waypoints: routes are computed between user-placed points. [verified] (Komoot support, "Change the route direction and type", https://support.komoot.com/hc/en-us/articles/10207909543066, accessed 2026-07-30)
- Route type: One Way (default) or Round Trip. A round trip with only start and destination typically produces an out-and-back on the fastest path for the sport; users shape loops manually by adding waypoints. [verified] (Komoot support, same article)
- Fitness level: affects only the estimated duration, not the route itself. Komoot states this explicitly. [verified] (Komoot, "Fitness vs Fun-ness When Planning a Route on komoot", https://www.komoot.com/adventure-hub/186OZJztsNtyEOgjSnbQkf/fitness-vs-fun-ness-when-planning-a-route-on-komoot, accessed 2026-07-30)

Parameters it does not accept: target distance as a generation input (you cannot ask for "a 12 km loop from here"), elevation targets, weather, street crossings, safety, or anything training-related. Elevation and surface breakdowns are displayed as outputs for a planned route, not accepted as inputs. [verified for the displayed outputs, inferred for the absence: no Komoot documentation or third-party review describes distance-targeted or constraint-targeted generation] (sources above)

On-demand generation vs static library: hybrid. The planner computes routes on demand between points; discovery relies on community Tours, Highlights, and Collections. Premium adds "Weather on route" but this is a forecast display along a planned route, not a routing constraint. [verified] (Komoot support, "komoot plans: Maps and Premium", https://support.komoot.com/hc/en-us/articles/360034377771, accessed 2026-07-30)

2025 roadmap items under Bending Spoons: redesign (September 2025), community heatmaps, streamlined Highlights, advanced route filters and preferences, route descriptions. Heatmaps mirror Strava functionality. [verified] (Komoot Newsroom, "Komoot unveils modern design as part of ambitious product roadmap", https://newsroom.komoot.com/254252, accessed 2026-07-30; BikeRadar redesign article above)

## Pricing (2026)

- Free: browse and plan routes, view community content, core navigation on the standard map. [verified] (Localsinsider, "How to Plan Hikes and Bike Routes With Komoot App (Review) and New Pricing Explained", https://localsinsider.com/apps/how-to-plan-hikes-bike-routes-with-komoot-review/, accessed 2026-07-30)
- Komoot Premium: 59.99 euros (or dollars or pounds) per year, 6.99 euros per month on web, 4.99 euros per week on mobile. Includes worldwide offline maps, multi-day planning, weather on route, sport-specific maps, live tracking, 3D maps, Garmin map integration. [verified] (BikeRadar redesign article above; Komoot support Premium guide above)
- Legacy one-time map purchases (region packs, World Pack at about 29.99 pounds) ended for new users on February 27, 2025; new users need Premium to sync routes to external devices such as Garmin and Wahoo. [verified] (road.cc, "Totally blindsided: Cuts and job losses expected at Komoot after route planning app bought by Italian tech firm infamous for mass layoffs", https://road.cc/content/news/job-cuts-expected-komoot-after-tech-firm-purchase-313159, accessed 2026-07-30; DC Rainmaker, "Komoot's Expanded Paywalls: Trying to make sense of it", https://www.dcrainmaker.com/2025/03/komoots-expanded-paywalls-trying-to-make-sense-of-it.html, accessed 2026-07-30)
- Conflict: BikeRadar's article (updated September 17, 2025 at Komoot's request) states that "following the acquisition, the Route Sync to Device feature is now accessible to more users, including free users", which contradicts the February 2025 paywall reporting. Weighting: the BikeRadar update is newer and was issued with Komoot's cooperation, so some sync capability has likely been restored to free users, but the exact current split between free and Premium sync is unclear. [verified conflict, resolution uncertain]

## Positioning

Outdoor adventure and exploration platform, "explore more of the outdoors", strongest in Europe and in cycling, bikepacking, and hiking. Runners are served but are not the core persona; marketing, Highlights content, and Premium features (multi-day Tours, sport-specific cycling maps) skew heavily toward bike and hike use cases. [verified for positioning language, inferred for the runner skew based on feature mix] (Komoot Newsroom above; Komoot Premium pages above)

## Strengths and weaknesses

Strengths:

- Deep European route and trail data, community Highlights, and sport-aware routing quality built over 15 years. [verified] (DC Rainmaker, "Komoot Team Says Goodbye", above)
- Large installed base (45 to 50 million registered users) and strong brand in Europe. [verified] (sources in snapshot)
- Broad device ecosystem integration (Garmin, Wahoo, Hammerhead, Apple Watch). [verified] (road.cc article above)

Weaknesses:

- [inferred] Development capacity is gutted: with 85 percent of staff gone, substantial new features are unlikely, so the routing engine will probably stagnate while owners harvest subscription revenue. Reasoning: this is the documented Bending Spoons pattern (Evernote) and DC Rainmaker draws the same conclusion.
- [inferred] Trust erosion: churn among engaged users (the ones who contribute route data) degrades the community data flywheel that Komoot's discovery features depend on. Reasoning: DC Rainmaker notes Komoot is heavily dependent on user-contributed data; cancellation reports are concentrated among power users.
- [verified] No on-demand, constraint-based route generation: the planner requires manual waypoint work and answers "how do I get there" rather than "where should I run today". (capability analysis above)
- [inferred] Running is structurally second-class: fitness level does not even influence routing, and Premium's flagship features (multi-day Tours, cycling maps) are irrelevant to a daily urban runner.

## Review sentiment and common complaints

- Paywall anger: long-time users objected to the shift from one-time map purchases to a 59.99 subscription for device sync. "It means new users will have to pay 59.99 pounds per year for the functionality which previously would have been covered by a one-off payment of 29.99 pounds." [verified] (road.cc article above)
- Acquisition backlash and cancellations: forum users report cancelling subscriptions and deleting the app, citing Bending Spoons' history ("As soon as I saw Bending Spoons mentioned, I knew I was out... Komoot is now deleted."). [verified] (Canion.blog, "Komoot Enshittification Incoming", https://canion.blog/2025/05/31/komoot-enshittification-incoming.html, accessed 2026-07-30; Cycling UK Forum thread, https://forum.cyclinguk.org/viewtopic.php?t=164527, accessed 2026-07-30)
- Migration behavior: departing users publicly evaluate Mapy.com, Ride with GPS, cycle.travel, OutdoorActive as replacements. [verified] (jonworth.eu, "Komoot: you saved me on Lithuanian dirt lanes... but it's time for something new", https://jonworth.eu/komoot-you-saved-me-on-lithuanian-dirt-roads-and-the-streets-of-roma-but-its-time-for-something-new/, accessed 2026-07-30)
- Routing quality: even before the acquisition, "poor routing choice has been a bug-bear for some Komoot users". [verified] (Loop article above)
- The September 2025 redesign "divided power users" with its heavy photo emphasis. [verified] (Localsinsider review above)

## Threat assessment for Waypoint

Medium threat, trending down. Komoot has the largest European outdoor route dataset and a huge installed base, so if it shipped distance-targeted or training-aware route generation it would be dangerous, but its post-acquisition staffing reality makes ambitious new routing features unlikely, and its planner today answers a fundamentally different question than Waypoint's "where should I run, right now, from here, for me". The user backlash creates a window: engaged European users are actively shopping for alternatives, and a running-first product with on-demand adaptive generation would not collide with Komoot's cyclist and hiker core. The main risk is Bending Spoons using Komoot's distribution to bolt on a cheap generation feature (heatmap-based suggestions are already on the roadmap). Watch the promised "advanced route filters and preferences" work for any move toward constraint-based generation.

## Assumptions

- [assumption] Bending Spoons will continue its harvest strategy (price increases, minimal feature investment) at Komoot through 2026 and beyond; based on its documented pattern at Evernote, WeTransfer, and Meetup, not on any Komoot-specific announcement.
- [assumption] Komoot's revenue is majority Premium subscriptions; no public revenue breakdown exists.
- [assumption] Runner share of Komoot's user base is a minority relative to cyclists and hikers; consistent with feature mix and marketing but no public sport-split data.
- [assumption] The free vs Premium boundary for device sync as of mid-2026 follows the BikeRadar September 2025 update (some free sync restored); Komoot's own support pages were not conclusive at access time.
