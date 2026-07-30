# Competitor Profile: Footpath Route Planner and RunGo (plus on-demand generator scan)

Version-Timestamp: 2026-07-30 14:30:00 UTC-4

Footpath and RunGo are small independent apps that each own one slice of the running route problem: Footpath is the best-in-class manual route drawing tool, and RunGo is the leader in voice-guided turn-by-turn navigation over a large curated route library. Neither generates routes on demand from constraints; that niche is served by a long tail of free or cheap web tools (Routeshuffle, Route Random, JustGo, Circa, Run Randomizer) that accept only distance and a start point. Individually these are low threats, but collectively they validate demand for "just give me a route from here" and set a price anchor near zero for basic generation.

## Footpath Route Planner (Half Mile Labs)

Company snapshot: developed by Half Mile Labs LLC, a small independent developer based in Covina, California. No funding, user, or revenue figures are public. [verified for developer identity] (Apple App Store, "Footpath Route Planner", https://apps.apple.com/us/app/footpath-route-planner/id634845718, accessed 2026-07-30; Footpath, "Privacy Policy", https://footpathapp.com/legal/privacy/, accessed 2026-07-30)

Route capabilities:

- Creation is manual: trace a route with your finger and it snaps to roads and trails, or long-press points and Footpath calculates the path between them per activity mode. Supports 35 plus activity types including running. [verified] (Footpath, "Drawing a route", https://footpathapp.com/user-guide/drawing-a-route/, accessed 2026-07-30)
- Constraint parameters accepted: activity mode (affects snapping preferences) and user-placed points. That is all. No target distance, no loop generation, no elevation targets, no weather, no safety inputs. Elevation and slope are analysis outputs (color-coded steepness), not inputs. [verified for what exists; inferred for absences based on complete feature table] (Footpath, "Footpath Elite Pricing", https://footpathapp.com/pricing/, accessed 2026-07-30)
- Strong execution layer: turn-by-turn audio cues (iPhone, Apple Watch), offline navigation, cue sheets, GPX, FIT, and TCX export to Garmin, Wahoo, Coros, Suunto, premium topo maps. [verified] (App Store listing above; Footpath Elite guide, https://footpathapp.com/user-guide/elite/, accessed 2026-07-30)

Pricing (2026): free tier (5 saved routes, core drawing); Footpath Elite at $3.99 per month or $23.49 per year, plus a $1.99 single route pass; 7-day trial. [verified] (App Store listing and Footpath pricing page above)

Positioning: a precision planning instrument ("the exact roads and trails you want") for people who already know where they want to go. Multi-sport, not running-first. [verified] (Footpath user guide above)

Strengths: excellent drawing UX, cheap, cross-platform, strong device export. [verified from feature set] Weaknesses: [inferred] zero discovery or generation intelligence, no training awareness, and a tiny team that cannot expand scope quickly. Reasoning: single-purpose product from a small LLC with no disclosed funding.

Review sentiment: App Store rating is strong and reviews praise the drawing and navigation combination; complaints in aggregate reviews center on subscription expectations and occasional routing snap errors. [inferred from App Store presence; individual Footpath complaint threads were not deeply sampled, noted as a gap in Assumptions]

## RunGo

Company snapshot: founded by Craig Slagel, development from 2012, based in Vancouver, Canada; 1 to 10 employees. Bootstrapped indie with hotel, race, and run club partnership revenue alongside subscriptions. [verified] (Craig Slagel, LinkedIn profile, https://ca.linkedin.com/in/craigslagel, accessed 2026-07-30; Canadian Running Magazine, "Follow planned and guided workout routes with the RunGo app", https://runningmagazine.ca/sections/training/follow-planned-and-guided-workout-routes-with-the-rungo-app/, accessed 2026-07-30)

Route capabilities:

- Model: a large static library plus manual creation. RunGo claims over 1 million routes with thousands of "verified routes" (race courses, city tours) and voice-guided turn-by-turn navigation as the hero feature, including Apple Watch support and VoiceOver accessibility. An older third-party aggregator cites 600,000 routes across 171 countries; weight the official site as current and the aggregator as stale. [verified with the count conflict noted] (RunGo, https://www.rungoapp.com/, accessed 2026-07-30; JustUseApp, "RunGo Reviews", https://justuseapp.com/en/app/712628644/rungo-the-best-routes-to-run/reviews, accessed 2026-07-30)
- Constraint parameters accepted: none for generation. Users pick from the library or build routes manually on the web creator or app (waypoints, GPX import, Strava import). Running-first, which is rare in this set. [verified] (RunGo Premium page, https://routes.rungoapp.com/gopremium, accessed 2026-07-30)
- Stats layer: time, pace, distance, elevation, estimated finish time, live tracking, interval training on iOS. [verified] (JustUseApp summary and RunGo Premium page above)

Pricing (2026): free tier (follow routes, log runs); Premium $5.99 per month, $59.99 per year, or $119.99 lifetime; Creator tier $19.99 per month or $199 per year for route publishers (hotels, races, coaches). [verified] (RunGo Premium page above; App Store listing, https://apps.apple.com/us/app/rungo-the-best-routes-to-run/id712628644, accessed 2026-07-30)

Positioning: "the best routes to run", navigation beyond maps, targeting travelers, hotels, races, and accessibility users (notable low-vision support). [verified] (RunGo site and Slagel LinkedIn above)

Strengths: running-specific voice navigation is genuinely differentiated; B2B hotel and race channel; accessibility credibility. [verified] Weaknesses: [inferred] dated UX and reliability issues at scale, no generation, no training layer, and a team of under 10 cannot fight platform incumbents. Reasoning: review complaints below plus team size.

Review sentiment: praise for turn-by-turn accuracy and the web route creator ("the most functional... I can put in stair counts, points of interest, which side of the street to walk on"); complaints about GPS reliability, spurious off-route and u-turn prompts ("may tell me to make a u-turn in the middle of the road"), and route editing bugs. [verified] (App Store reviews page, https://apps.apple.com/us/app/rungo-the-best-routes-to-run/id712628644?see-all=reviews, accessed 2026-07-30; JustUseApp above)

## Scan: other on-demand route generators

These tools do exactly one thing Waypoint's hero feature does (instant loop generation) with none of the intelligence:

- Routeshuffle (routeshuffle.com): random route generator for run, walk, bike; inputs are start location, distance (or duration), and activity. Free core; Premium at $5 per month or $49 per year adds saving, export, and surface, way type, and lighting condition details. Built by a teenage runner; long-running hobby product. [verified] (Routeshuffle, https://routeshuffle.com/ and https://routeshuffle.com/premium/, accessed 2026-07-30; SaaSHub, "Routeshuffle reviews", https://www.saashub.com/routeshuffle, accessed 2026-07-30)
- Route Random (route-random.lukasolivier.be): free, no account; distance or time, activity type, GPX and GeoJSON export; built on OpenStreetMap and OpenRouteService. [verified] (site, accessed 2026-07-30)
- JustGo (justgo.rooot.it): generates 8 loop options from a time budget; Europe only; free with a supporter pass for unlimited packs and bulk GPX. [verified] (site, accessed 2026-07-30)
- Circa (circa.fit): free circular route generation by exact distance (1 to 50 km) from any address. [verified] (site, accessed 2026-07-30)
- Run Randomizer (run-randomizer.vercel.app): distance, route type (loop, out-and-back, one-way), and a "prefer flat route" toggle. [verified] (site, accessed 2026-07-30)
- Generoute: waitlist-stage app promising distance presets (5K to marathon) plus a terrain preference slider for loops. Not yet launched. [verified as pre-launch] (strange.tech/stargen/generoute, accessed 2026-07-30)

Pattern: every generator accepts start point plus distance, a couple accept a coarse hilliness or terrain preference, and none accepts weather, crossings, safety, surface specifics, or training context. All are web-first hobby projects with no coaching layer and no mobile execution experience. [verified from the feature sets above]

## Threat assessment for Waypoint

Low threat individually, moderate signal collectively. Footpath and RunGo are sub-10-person companies without generation capability or training intelligence, and the web generators are hobby tools that compete only on "free". The real lessons are strategic: RunGo proves committed runners will pay ($59.99 per year, matching Komoot and Strava's annual price) for running-specific navigation execution, and the generator long tail proves organic demand for instant "route from here at distance X" while setting the free price anchor for that baseline capability. Waypoint must therefore charge for the adaptive layer (training, weather, safety, personalization), not for basic loop generation. Worth monitoring in case any of these ships constraint-based generation or gets acquired for its niche (RunGo's voice navigation and accessibility assets would be attractive to a larger player).

## Assumptions

- [assumption] Footpath and RunGo revenues are small (low single-digit millions at most); inferred from team size, pricing, and absence of any funding or revenue disclosures.
- [assumption] Footpath review complaints were not deeply sampled; the sentiment line for Footpath rests on aggregate store impressions rather than a thread-by-thread review, unlike the other profiles.
- [assumption] RunGo's "over 1 million routes" includes user-generated routes of highly variable quality; the verified route subset (thousands) is the practically useful library.
- [assumption] None of the scanned web generators has meaningful recurring revenue or a funded team behind it; based on site presentation and single-developer attribution.
