# Competitive Feature Matrix

Version-Timestamp: 2026-07-30 14:50:00 UTC-4

This matrix consolidates the ten competitor profiles in `research/02-competitors/` into one capability table across training plan capabilities, route capabilities, platform reach, and community. Every cell traces to a profile file (cited per column below; the profiles carry the underlying URLs). The headline finding: no competitor holds a Yes in both the training intelligence block and the route generation block. Strava is the only product with on-demand route generation, and its constraint set stops at coarse distance presets, an elevation preference, and surface type. The weather, street crossing, and safety constraint rows are empty across the entire market. Waypoint's planned column is the only one that fills the intersection.

## Column key and source files

| Column | Competitor | Source profile |
|---|---|---|
| Runna | Runna (Strava-owned) | `profile-runna.md` |
| TAO | TrainAsONE | `profile-trainasone.md` |
| AIE | AI Endurance | `profile-ai-endurance.md` |
| Coopah | Coopah | `profile-coopah.md` |
| Joggo | Joggo (Kilo Health) | `profile-joggo.md` |
| Komoot | Komoot (Bending Spoons) | `profile-komoot.md` |
| AllTrails | AllTrails | `profile-alltrails.md` |
| Strava | Strava incl. Suggested Routes | `profile-strava-routes.md`, `adjacent-platforms.md` |
| Footpath | Footpath Route Planner | `profile-footpath-rungo.md` |
| RunGo | RunGo | `profile-footpath-rungo.md` |
| Waypoint | Waypoint (planned, per Founder Brief) | `vault/01-Project/Founder-Brief.md` |

## Master matrix

### Training plan capabilities

| Feature | Runna | TAO | AIE | Coopah | Joggo | Komoot | AllTrails | Strava | Footpath | RunGo | Waypoint (planned) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Adaptive training plans | Yes | Yes | Yes | Yes | Partial [1] | No | No | No [2] | No | No | Yes |
| LLM coach chat | No [3] | No | Yes | Partial [4] | No | No | No | Partial [5] | No | No | Yes |
| Readiness / recovery input | Partial [6] | Yes | Yes | Partial [7] | No | No | No | No | No | No | Yes |
| Race-specific plans | Yes | Yes | Yes | Yes | Partial [8] | No | No | No [9] | No | No | Yes |
| Injury prevention | Partial [10] | Yes | Partial [11] | Partial [12] | No | No | No | No | No | No | Yes |

### Route capabilities

| Feature | Runna | TAO | AIE | Coopah | Joggo | Komoot | AllTrails | Strava | Footpath | RunGo | Waypoint (planned) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| On-demand route generation | No | No | No | No | No | Partial [13] | Partial [14] | Yes | No | No | Yes |
| Constraint: distance | No | No | No | No | No | No | Partial [15] | Partial [16] | No | No | Yes |
| Constraint: elevation | No | No | No | No | No | No | Partial [17] | Partial [18] | No | No | Yes |
| Constraint: surface | No | No | No | No | No | Partial [19] | No | Yes | Partial [20] | No | Yes |
| Constraint: weather | Partial [21] | Partial [22] | No | No | No | Partial [23] | Partial [24] | No | No | No | Yes |
| Constraint: street crossings | No | No | No | No | No | No | No | No | No | No | Yes |
| Constraint: safety | No | No | No | No | No | No | No | Partial [25] | No | No | Yes |
| Start-anywhere routing | No | No | No | No | No | Yes | Partial [26] | Yes | Yes | Partial [27] | Yes |
| Turn-by-turn audio navigation | Partial [28] | No | No | No | No | Partial [29] | Partial [30] | Partial [31] | Yes | Yes | Yes |

### Platform

| Feature | Runna | TAO | AIE | Coopah | Joggo | Komoot | AllTrails | Strava | Footpath | RunGo | Waypoint (planned) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| iOS app | Yes | Partial [32] | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Android app | Yes | Yes | Partial [33] | Yes | Yes | Yes | Yes | Yes | Yes | Partial [34] | No (v1 iOS-first) |
| Watch apps | Yes | Yes | Partial [35] | Yes | Partial [36] | Yes | Partial [37] | Yes | Yes | Yes | Yes |
| Wearable integrations | Yes | Yes | Yes | Yes | Partial [38] | Yes | Partial [37] | Yes | Yes | Partial [39] | Yes [40] |

### Social / community

| Feature | Runna | TAO | AIE | Coopah | Joggo | Komoot | AllTrails | Strava | Footpath | RunGo | Waypoint (planned) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Social / community layer | No | No | No | No | Partial [41] | Yes | Yes | Yes | No | Partial [42] | No (not in v1 scope) |

## Footnotes

1. Joggo adjusts template plans only after a bi-weekly assessment run; no per-run adaptation or physiological modeling (`profile-joggo.md`).
2. Strava itself has no plan engine; adaptive plans live in the separately operated Runna app it owns (`profile-strava-routes.md`, `adjacent-platforms.md`).
3. Runna's engine is algorithmic adaptation on coach-designed templates marketed as AI; no public evidence of LLM components (`profile-runna.md`, [inferred] in that profile).
4. Coopah's 24/7 chat combines "instant AI answers" with human coaches; conversational, but not documented as an LLM that controls the plan, and some users suspect bot responses (`profile-coopah.md`).
5. Strava's Athlete Intelligence generates AI post-activity summaries and trend insights; it is not a conversational coach and cannot modify training (`adjacent-platforms.md`).
6. Runna accepts "Not Feeling 100%" feedback on some plans; no HRV, sleep, or recovery modeling documented (`profile-runna.md`).
7. Coopah's Race Day Score (0 to 100% readiness) and weekly Coach's Report are assessments, not physiological recovery inputs to the plan (`profile-coopah.md`).
8. Joggo plans stop at half marathon and target beginners; no marathon or ultra support (`profile-joggo.md`).
9. Strava's Race Discovery (July 2026) surfaces Runna's race database in the Events tab; it is event discovery, not a training plan (`profile-strava-routes.md`).
10. Runna includes strength and physio content, but widespread 2026 discourse attributes injuries to aggressive default progressions (`profile-runna.md`).
11. AI Endurance downgrades workouts based on its HRV-driven recovery model; no explicit injury risk model documented (`profile-ai-endurance.md`).
12. Coopah includes strength and conditioning in every plan and skews conservative; no injury risk modeling documented (`profile-coopah.md`).
13. Komoot computes routes on demand between user-placed waypoints (including round trips) but cannot generate from a target distance or any constraint; loops require manual waypoint work (`profile-komoot.md`).
14. AllTrails Peak's AI adjusts an existing route (reverse, shorter, less climb, more scenic); a human must first pick or build the route, and generation from scratch from constraints does not exist (`profile-alltrails.md`).
15. AllTrails accepts only the relative command "make it shorter" on an existing route, not a target distance (`profile-alltrails.md`).
16. Strava accepts distance as preset target values, not free-form input (`profile-strava-routes.md`, and its [assumption] that presets persist as of mid-2026).
17. AllTrails accepts only "reduce elevation gain" as a relative adjustment on an existing route (`profile-alltrails.md`).
18. Strava accepts an elevation preference (flat, hilly, any), not elevation gain targets (`profile-strava-routes.md`).
19. Komoot's sport type selection indirectly sets preferred surfaces and way types; surface is not a direct user constraint (`profile-komoot.md`).
20. Footpath's activity mode affects road and trail snapping preferences during manual drawing; not a generation constraint (`profile-footpath-rungo.md`).
21. Runna's Adapt for Heat (July 2026) uses local heat and humidity to slow target paces; it answers "how fast", never "where" (`profile-runna.md`).
22. TrainAsONE's Environment Adjusted Pace uses weather forecasts and local route undulation to adjust pacing prescriptions, not route choice; humidity is on the roadmap, not shipped (`profile-trainasone.md`).
23. Komoot Premium's "Weather on route" displays a forecast along an already planned route; it is not a routing constraint (`profile-komoot.md`).
24. AllTrails Trail Conditions (15 weather factors, Meteomatics and Tomorrow.io) is planning information display along a trail, not a routing constraint (`profile-alltrails.md`).
25. Strava's Night Heatmap and "active times" are display layers framed around visibility and comfort; safety is not a generation constraint, and users document dangerous generated routes with no flagging mechanism (`profile-strava-routes.md`).
26. AllTrails custom routes snap only to marked trails, paths, and roads, and the library, conditions data, and AI adjustments center on trails; doorstep urban starts are outside the design center (`profile-alltrails.md`).
27. RunGo relies on its route library plus manual creation; you can build from anywhere but nothing is generated from an arbitrary start point (`profile-footpath-rungo.md`).
28. Runna can import public Strava routes and follow them with turn guidance on Apple Watch; import-and-follow only, no planning or audio navigation product of its own (`profile-runna.md`).
29. Komoot's core navigation is verified; the profile did not capture whether audio turn cues are included in the free tier (`profile-komoot.md`).
30. AllTrails offers navigation with wrong-turn alerts (Plus and above); runner-tuned audio turn-by-turn cues are not documented (`profile-alltrails.md`).
31. Strava offers route navigation with reported friction on wearables; dedicated audio turn-by-turn cues are not documented in the profile (`profile-strava-routes.md`).
32. TrainAsONE is a web-first platform with companion iOS, Android, and Garmin apps; the phone apps are not the primary surface (`profile-trainasone.md`).
33. AI Endurance serves Android via the web app; only an iOS native app is verified (`profile-ai-endurance.md`).
34. RunGo's Android availability was not captured in the profile research; treat as unknown, not as absent (`profile-footpath-rungo.md`).
35. AI Endurance exports workouts to Garmin, Suunto, Coros, and Wahoo devices; no native watch app documented (`profile-ai-endurance.md`).
36. Joggo supports Apple Watch only, with documented watch-to-phone sync failures (`profile-joggo.md`).
37. AllTrails watch app and wearable integrations were not captured in the profile research; treat as unknown (`profile-alltrails.md`).
38. Joggo integrates Apple Watch and Apple Health only; no Garmin, Coros, Polar, or Strava (`profile-joggo.md`).
39. RunGo documents Strava import and Apple Watch support; broader wearable integrations were not captured (`profile-footpath-rungo.md`).
40. Waypoint plans HealthKit-first ingestion; Garmin's Connect Developer Program is paused to new applicants, so Garmin data access is an uncertain later unlock (`adjacent-platforms.md`).
41. Joggo markets a "support group" and referral mechanics; no real community layer documented (`profile-joggo.md`).
42. RunGo has a community route library (1M+ routes claimed, thousands verified) but no social feed or community interaction layer (`profile-footpath-rungo.md`).

## Adjacent platforms (context, not matrix columns)

From `adjacent-platforms.md`: Garmin offers free adaptive Garmin Coach plans locked to its watches, with static course tools and no weather, safety, or crossing awareness. Apple's Workout Buddy (watchOS 26) is generative spoken motivation, not a plan or a route product. Nike Run Club is free static plans and audio content in maintenance mode. WHOOP has the strongest consumer AI coach but no screen, no GPS, and no mapping assets. None of the four holds any cell in the route constraint block.

## What the matrix reveals

1. The market is two half-products. The training block (adaptive plans, readiness, race plans) is dense on the left five columns (Runna, TrainAsONE, AI Endurance, Coopah, Joggo) and empty on route capabilities. The route block is populated only by the right five columns (Komoot, AllTrails, Strava, Footpath, RunGo), which are empty on training. No product spans both. [inferred: direct read of the matrix; every profile's "wedge check" section confirms the absence on its side]
2. The constraint rows are the whitespace. Weather as a routing constraint is Partial at best everywhere (four products apply weather to pace or display it, none to route choice). Street crossings: zero entries. Safety: one Partial (Strava's display layers), zero constraints. These three rows plus true distance and elevation targeting are exactly Waypoint's hero parameters, and they are open across all eleven columns. [inferred from the matrix rows above]
3. Strava is the only genuine generation incumbent, and its generation is popularity-ranked, preset-bound, and not connected to training: the same suggestions for every runner at the same corner, with documented dangerous outputs and no flagging mechanism (`profile-strava-routes.md`). The threat is what it could connect (Runna's plan engine to its heatmap generation), not what it has shipped.
4. Weather-aware training already has consumer acceptance. Runna's Adapt for Heat and TrainAsONE's Environment Adjusted Pace prove runners accept environment-adjusted prescriptions (`profile-runna.md`, `profile-trainasone.md`). Nobody has yet moved that acceptance from "how fast" to "where". [inferred]
5. Turn-by-turn audio navigation for runners is a solved execution problem at indie scale (Footpath, RunGo) but is never paired with generation or coaching. Waypoint does not need to invent the execution layer, only to attach it to an intelligent generator. [inferred]

## Assumptions

- [assumption] "Waypoint (planned)" cells reflect the Founder Brief's v1 scope (route generation wedge with the six named constraints, coaching layered on top, iOS-first with wearable integrations); no Waypoint capability exists yet, and the column is a design intent, not a shipped product.
- [assumption] Cells marked "not captured in profile research" (RunGo Android, AllTrails watch and wearables) are unknowns, not verified absences; they do not affect the whitespace conclusion because they sit outside the constraint block.
- [assumption] The matrix is a snapshot as of 2026-07-30; Strava's shipping cadence on Routes (multiple releases per quarter through 2025 to 2026 per `profile-strava-routes.md`) makes the Strava column the most likely to change first.
- [assumption] Adjacent platforms (Garmin, Apple, Nike, WHOOP) are excluded as columns because none participates in either the adaptive plan market or route generation today per `adjacent-platforms.md`; their threat is platform-level, covered in `gap-analysis.md`.
