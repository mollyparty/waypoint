# Waypoint API and Integration Map (MVP)

Version-Timestamp: 2026-07-30 18:30:00 UTC-4

Scope: the definitive inventory of every external API, data source, platform service, and vendor integration Waypoint needs for the 15-feature MVP (`mvp-scope.md`), plus the v1.x items that shape architecture now. Because a parallel study is deciding whether MVP targets iOS only or iOS plus Android, every domain maps BOTH platforms wherever they differ. This document extends, and does not re-litigate, `stack-recommendation.md` and `stack-validation.md`; where those documents already verified a fact on 2026-07-30, the citation is reused and marked "(verified in stack docs)". All new sources were accessed 2026-07-30. Every claim carries a [verified]/[inferred]/[assumption] tag per `research/00-RESEARCH-PLAYBOOK.md`. Prices exclude VAT unless stated; re-verify at contract time.

How to read each integration entry: purpose (which MVP feature it serves), provider plus alternatives, auth model, pricing and limits at MVP (roughly 1k MAU) and at 10k MAU, data in/out with privacy classification, compliance notes, failure mode and fallback, and build phase. Phases: WS (walking skeleton, month 3 to 4), MVP (v1.0 launch), v1.x (fast-follow).

Privacy classes used below: P0 (no personal data), P1 (pseudonymous or coarse), P2 (personal data), P3 (sensitive: precise location, health, Article 9 adjacent).

Executive summary: Waypoint's MVP needs roughly 20 integrations across 7 domains, but only 6 gate the walking skeleton, and almost everything on the critical path is either first-party platform capability (HealthKit, MapKit), open data (OSM, elevation), or self-hosted (GraphHopper). Total external-services cost is roughly $80 to $130 per month at MVP and roughly $350 to $500 per month at 10k MAU, both platforms included. The riskiest third-party dependencies are Strava (discretionary program admission, a June 1, 2026 API agreement with a sweeping AI ban, and a 2,000-upload-per-day default ceiling) and the Android review stack (Health Connect declaration plus the new fine-location declaration), which is why Android, if greenlit, must start its Play Console paperwork in month 1.

## 1. Routing and geo

### 1.1 GraphHopper (self-hosted, internal API)

| Field | Detail |
|---|---|
| Purpose | H-01 core constraint route generation, H-02 elevation constraint, H-05 safety-aware routing, H-07 novelty (candidate generation), X-01 voice navigation (instruction list source) |
| Provider | Self-hosted GraphHopper open source, Apache 2.0, on the Hetzner VM (verdict locked in `stack-recommendation.md` section 1, validated in `stack-validation.md`) [verified in stack docs] |
| Alternatives | Stadia Maps hosted Valhalla (degraded fallback via `linear_cost_factors`), GraphHopper cloud API (prototyping only; cannot ingest moat data) [verified in stack docs] |
| Auth | Internal service, not exposed publicly. Network-level isolation plus a shared secret between the orchestration API and GraphHopper; end users never call it directly. [inferred design] |
| Cost MVP / 10k | $25 / $120 per month (Hetzner VM sizing, verified in stack docs; A9 load test pending) |
| Data in/out | In: start coordinate (P3, treat as home-address proxy per `regulatory-compliance.md` section 1), target distance, custom model JSON built from user constraints (P2). Out: route polyline, turn instructions, elevation profile (P3 while associated with the user). |
| Compliance | No DPA (self-hosted, we are the controller and host). Coordinates processed in memory, logged only truncated with short TTL (stack rec section 5). ODbL attribution required on rendered routes; routing instructions are a Produced Work under the OSMF routing safe harbour [verified in stack docs]. |
| Failure mode | VM down: no NEW route generation; saved routes, recorded runs, and voice guidance on an already-loaded route keep working on-device. Fallback: rehearsed restore from off-provider snapshots (hours); strategic fallback Stadia hosted Valhalla. [verified in stack docs] |
| Phase | WS |

Endpoints Waypoint uses (GraphHopper API, docs accessed 2026-07-30, https://docs.graphhopper.com/openapi/routing/getroute and https://github.com/graphhopper/graphhopper/blob/master/docs/core/custom-models.md) [verified in stack docs]:

| Endpoint | Use | Notes |
|---|---|---|
| POST /route with `algorithm=round_trip` | The hero primitive: loop from one start point at a target distance | Parameters `round_trip.distance` and `round_trip.seed` (seed drives H-07 novelty variation); foot profile |
| POST /route with `custom_model` and `ch.disable=true` | Per-request constraint weighting: elevation preference, surface, safety encoded values | Custom models are officially beta; node-level crossing penalties likely need Java-level work (open question carried from stack rec) |
| GET /health (and /info) | Liveness for monitoring (section 6) | Internal only |

### 1.2 OSM data pipeline (Geofabrik extracts)

| Field | Detail |
|---|---|
| Purpose | Base road and path network for the routing graph; source tags for surface, footways, crossings, `lit=*` (the moat derivation inputs, stack rec section 2) |
| Provider | Geofabrik free download server: pre-cut regional extracts (`.osm.pbf`), updated daily around 21:00 CET, with daily diffs (`.osc.gz`) compatible with osmupdate and pyosmium for continuous local updating. Free of charge. [verified] (Geofabrik, https://download.geofabrik.de/ and https://www.geofabrik.de/en/data/download.html and https://download.geofabrik.de/technical.html, accessed 2026-07-30) |
| Alternatives | planet.openstreetmap.org (full planet, overkill at launch), SliceOSM on-demand cutouts (referenced by Protomaps docs) [verified] |
| Auth | None (public download; extracts strip user metadata for EU data protection) [verified, same sources] |
| Cost MVP / 10k | $0 / $0 (bandwidth only) |
| Data in/out | In: nothing of ours. Out to us: ODbL map data (P0). |
| Compliance | ODbL 1.0: attribution ("© OpenStreetMap contributors") everywhere map data or derived routes render; derivative databases keep the same license. The sharp edge remains our OSM-derived context layers (crossing graph): publicly using them makes them Derivative Databases subject to share-alike on request; keep independent-source layers (municipal lighting) separate as a Collective Database and get counsel review before launch (stack rec section 1 license notes). [verified in stack docs plus Geofabrik license statement] |
| Failure mode | Download server outage delays a graph rebuild, nothing user-facing. Fallback: mirror the last-good extract in our own object storage (also needed for the restore drill). [inferred] |
| Phase | WS |

Update cadence recommendation: monthly graph rebuilds at MVP (constraint data changes slower than OSM edits), moving to weekly rebuilds via daily diffs when the safety layer's freshness starts mattering; the rebuild runs on an on-demand import box per the official import/serve split. [inferred, on the verified daily-diff mechanics]

### 1.3 Elevation data

| Field | Detail |
|---|---|
| Purpose | H-02 elevation constraint, elevation profiles in route preview (WS step 2) |
| Provider | AWS Terrain Tiles (open data on S3, no AWS account needed to read) for the graph-build pipeline; Copernicus GLO-30 (free and open license, attribution required: DLR and Airbus under Copernicus by EU and ESA) as quality cross-check. Both verified in stack docs (registry.opendata.aws/terrain-tiles/, Copernicus license PDF, accessed 2026-07-30). [verified in stack docs] |
| Alternatives | Mapterhorn (Terrarium-encoded RGB terrain tiles in PMTiles format, aggregated global sources) if the Android client ever needs client-side hillshade alongside Protomaps basemaps [verified] (Protomaps docs, https://docs.protomaps.com/basemaps/downloads, accessed 2026-07-30) |
| Auth | None (public buckets) |
| Cost MVP / 10k | $0 / $0 (tiles cached during builds; egress negligible) [verified in stack docs] |
| Data in/out | Out to us: elevation rasters (P0). Nothing of ours goes out. |
| Compliance | Attribution notices in the app's data-sources screen. No DPA needed. |
| Failure mode | Source outage delays graph builds only. Cache tiles locally per build region. [inferred] |
| Phase | WS |

### 1.4 Geocoding and reverse geocoding

Waypoint's geocoding needs are small: forward geocoding for typed start points ("start my route near X", travel mode), reverse geocoding for human-readable run and route names. The default start is "current location" (no geocoding call at all).

Usage-policy reality check: the public Nominatim instance (nominatim.openstreetmap.org) is explicitly not an option for a commercial product: absolute hard limit of 1 request per second summed across ALL of an application's users, "no heavy uses", bulk geocoding and autocomplete prohibited, identifying User-Agent required, and the policy warns commercial applications that access may be withdrawn without notice. [verified] (OSMF Nominatim Usage Policy, https://operations.osmfoundation.org/policies/nominatim/, accessed 2026-07-30). Photon's public demo instance (photon.komoot.io) is similarly best-effort: "reasonable limit" only, throttling or bans for extensive use, no availability guarantees. [verified] (komoot/photon README, https://github.com/komoot/photon, accessed 2026-07-30)

| Field | Detail |
|---|---|
| Purpose | Start-point search (H-08 travel framing, generation screen), run naming (TS-02 history) |
| Provider recommendation | Two-layer approach. (a) On-device platform geocoders first: CLGeocoder on iOS and the Android platform `Geocoder` class, both free, first-party, and sufficient for occasional reverse geocoding of run locations; both are rate-limited for heavy use, which Waypoint's per-user volume never approaches [inferred; platform geocoder availability is long-standing OS capability, but per-call limits were not verified this pass, assumption B1]. (b) Self-hosted Photon (Apache 2.0, Komoot's OSM geocoder with search-as-you-type) for server-side forward search in v1.x if typed-search volume or quality demands it: pre-built database dumps make setup "downloading two files and starting the server"; a planet index needs about 95 GB disk and 64 GB RAM recommended, but launch-country JSON-dump extracts run far smaller and can colocate on the routing VM. [verified as to license, dumps, and sizing] (OSM wiki Photon page, https://wiki.openstreetmap.org/wiki/Photon; komoot/photon README and discussion #1011; accessed 2026-07-30) |
| Alternatives | Commercial OSM geocoders if self-hosting is not worth it at our tiny volume: Stadia Maps geocoding is included in its paid plans (20 credits per request against the $20/month 1M-credit Starter plan), MapTiler geocoding costs 1 request per call against its plans; LocationIQ and Geocode Earth are the other named commercial Nominatim providers. [verified] (Stadia pricing, https://stadiamaps.com/pricing/; MapTiler pricing, https://www.maptiler.com/cloud/pricing/; Nominatim docs naming commercial providers; all accessed 2026-07-30) |
| Auth | Platform geocoders: none (OS API). Photon self-host: internal. Commercial: API key. |
| Cost MVP / 10k | $0 / $0 (platform geocoders); Photon self-host adds $0 (colocated) to ~$10 per month if it needs its own small VM [inferred] |
| Data in/out | In: coordinates or place-name text (P3 when it is the user's location; reverse geocoding of run start points should use the privacy-zone-jittered point, never the true origin). Out: place names (P1). On-device geocoding keeps coordinates inside the OS vendor relationship the user already has. [inferred design implementing compliance checklist item 1] |
| Compliance | If a commercial geocoder is adopted: DPA plus SDK/data-flow audit (coordinates are sensitive; FTC location orders apply, `regulatory-compliance.md` section 1). Self-host avoids the processor entirely. |
| Failure mode | Geocoding down: start-point search degrades to map-pin placement and current location; run names fall back to coordinates-free defaults ("Morning run"). Non-blocking by design. [inferred] |
| Phase | MVP (WS uses current location only) |

### 1.5 Map tiles and rendering (the platform-split decision)

iOS: MapKit, free for native apps with no usage-based pricing, first-party, no SDK audit; renders generated route polylines and overlays fine (verdict from stack docs, MapKit docs accessed 2026-07-30). [verified in stack docs]

Android (and optional cross-platform parity): MapLibre (open-source BSD renderer, the de facto standard for non-Google vector maps on Android) plus a tile source. MapLibre itself is free; the tile source is the cost decision. [verified as to MapLibre being free open source; renderer choice is [inferred] standard practice]

| Tile source option | Terms and cost | Fit |
|---|---|---|
| Protomaps self-host (recommended) | Free daily planet basemap builds (~120 GB full planet, regional extracts via `pmtiles extract`) distributed as an ODbL Produced Work; host the single PMTiles file on object storage (S3, R2) behind a CDN, no tile server process needed (HTTP range requests). Cost is storage plus egress, characterized by Protomaps as 10 to 100x cheaper than hosted APIs: single-digit dollars per month at MVP scale. [verified as to builds, format, license, and cost characterization] (Protomaps docs, https://docs.protomaps.com/basemaps/downloads and https://docs.protomaps.com/pmtiles; Protomaps blog, https://protomaps.com/blog/open-core-to-open-source/; accessed 2026-07-30). Exact monthly figure is [inferred]: roughly $1 to $6 at MVP. | Best fit: matches the self-host posture, no per-MAU meter, no third-party SDK data flow to audit (tiles come from our own domain) |
| Stadia Maps (managed fallback) | Free tier 200k credits/month is non-commercial only; commercial Starter $20/month with 1M credits (vector tile = 1 credit), Standard $80/month with 7.5M credits; hard-limit or opt-in overage. [verified] (https://stadiamaps.com/pricing/ and https://docs.stadiamaps.com/limits/, accessed 2026-07-30) | Good managed option; also bundles geocoding (1.4) and hosts Valhalla (routing fallback), so one vendor covers three fallbacks |
| MapTiler (alternative) | Free tier is non-commercial/R&D only; Flex $30/month with 500k requests and 25k sessions, overage $0.10 per 1,000 requests. [verified] (https://www.maptiler.com/cloud/pricing/ and https://www.maptiler.com/terms/cloud/, accessed 2026-07-30) | Fine product; no advantage over Stadia for us and free tier unusable commercially |

Recommendation: MapKit on iOS (zero cost, zero audit), MapLibre plus self-hosted Protomaps extracts for Android. If the platform study demands pixel-identical cross-platform maps, MapLibre plus Protomaps on BOTH platforms is the parity option at the cost of losing MapKit's zero-integration convenience; do not pay for that parity unless design actually requires it. [inferred recommendation]

| Field | Detail (Android tile stack) |
|---|---|
| Auth | None beyond a CDN key on our own bucket; Stadia/MapTiler would use API keys |
| Data in/out | Tile requests reveal viewport location to the tile host (P3-adjacent). Self-hosting keeps that traffic first-party, which is exactly the Strava lesson applied to map tiles. [inferred] |
| Compliance | Self-host: OSM attribution on-map. Stadia/MapTiler: DPA plus privacy audit of request logging before adoption (compliance checklist items 8 and 9). |
| Failure mode | Tile outage: cached tiles plus route polyline on a blank canvas still navigates; voice guidance is unaffected. [inferred] |
| Phase | WS if Android is in scope from day one, else with the Android build |

### 1.6 Sunrise/sunset and daylight

No API. Civil twilight and daylight windows are computed locally with standard solar-position math (NOAA algorithms) in both clients and in the graph/scoring pipeline; zero cost, offline-safe, no data leaves the device. Serves H-05 time-of-day heuristics and H-09 honest degradation copy. [verified as to the algorithms being standard published math; the design choice is [inferred]]

## 2. Weather and environment

### 2.1 Apple WeatherKit REST API (primary, both platforms)

| Field | Detail |
|---|---|
| Purpose | H-06 weather and heat route adjustment (v1.x feature, but weather display and heat warnings appear in MVP generation UI per H-09 honest messaging); server-side generation context |
| Provider | Apple WeatherKit. The REST API is explicitly for "websites and other platforms, like Android": Apple's own documentation names Android as a REST API target, so one weather vendor covers both clients. 500,000 calls/month are included with the Apple Developer Program membership we already carry; paid tiers from $49.99/month for 1M calls and $249.99/month for 5M (tier prices verified in stack docs). [verified] (Apple, WeatherKit REST API docs, https://developer.apple.com/documentation/weatherkitrestapi; Get started, https://developer.apple.com/weatherkit/get-started/; accessed 2026-07-30) |
| Auth | ES256-signed JWT developer token created from a WeatherKit key in the Apple Developer account. The private key must never ship in an app binary, so all WeatherKit calls route through Waypoint's server (which also lets one cached call serve many users per location cell). [verified as to the auth mechanics] (Apple, Request authentication for WeatherKit REST API, https://developer.apple.com/documentation/weatherkitrestapi/request-authentication-for-weatherkit-rest-api, accessed 2026-07-30) |
| Cost MVP / 10k | $0 / $0 to $50 (1 to 2 calls per generated route stays far under 500k/month; the $50 line appears only if per-user call patterns exceed roughly 50 calls/month) [verified tier prices; usage model inferred, carried from stack docs] |
| Data in/out | In: coordinates (P3; send graph-cell or truncated coordinates, not exact start points, since forecast resolution does not need house-level precision). Out: forecast data (P0). [inferred mitigation] |
| Compliance | Attribution required: Apple Weather trademark plus legal link to data sources; special display rules for severe weather alerts (embedded link, unmodified alert text). Terms for safety-adjacent use remain the open question carried from the compliance doc; keep weather copy advisory. [verified attribution requirements] (Apple, WeatherKit get started, attribution section, accessed 2026-07-30) |
| Failure mode | WeatherKit outage or quota exhaustion: fall back to Open-Meteo (2.2); if both fail, generation proceeds without weather context and H-09 messaging says so. [inferred] |
| Phase | MVP (weather context), v1.x (H-06 adjustment) |

### 2.2 Open-Meteo (fallback plus pipeline)

| Field | Detail |
|---|---|
| Purpose | Server-side fallback for 2.1; historical heat-exposure data for the graph pipeline (H-06 groundwork) |
| Provider | Open-Meteo. The free API is non-commercial only (10,000 calls/day, 300,000/month); commercial use requires a subscription: Standard $29/month for 1M calls/month (includes Weather Forecast, Marine, Air Quality, Geocoding, Elevation, Flood APIs), Professional $99/month for 5M calls and adds the Historical Weather, Ensemble, and Climate APIs. This resolves stack rec assumption A5 (prices were previously uncaptured). Data is CC BY 4.0, attribution required. [verified] (Open-Meteo pricing, https://open-meteo.com/en/pricing; announcement, https://openmeteo.substack.com/p/api-subscriptions-for-commercial; accessed 2026-07-30) |
| Auth | API key on the customer endpoint (customer-api.open-meteo.com); free tier is keyless but off-limits to us commercially. [verified, same sources] |
| Cost MVP / 10k | $0 (not yet wired) / $29 Standard when the fallback goes live. Note: the historical heat pipeline needs the Historical Weather API, which sits in the $99 Professional tier; defer that spend until H-06 is actually being built. [verified tier contents; phasing inferred] |
| Data in/out | In: coordinates (P3, same truncation rule as 2.1). Out: forecast and historical weather (P0). |
| Compliance | CC BY 4.0 attribution in data sources screen. EU-based provider; DPA per checklist item 9 when wired. [verified license; DPA mechanics assumption B2] |
| Failure mode | It IS the fallback; if both weather sources fail, degrade per 2.1. |
| Phase | v1.x (activate with H-06; contract Standard tier then) |

### 2.3 Air quality: defer

Recommendation: DEFER to v1.x or later. No MVP v1 feature consumes air quality (H-06 weather adjustment is itself v1.x), and adding an environmental signal the product does not act on violates data minimization instincts and adds explanation burden. When it comes: Open-Meteo's Air Quality API is included in the same commercial subscription already recommended at 2.2 (zero marginal vendor), against Google's Air Quality API at $5.00 per 1,000 requests after a 10,000/month free cap ($4.00/1k above 100k). Open-Meteo wins on cost and vendor count unless product needs Google's pollutant detail. [verified] (Open-Meteo pricing, accessed 2026-07-30; Google Maps Platform pricing list, https://developers.google.com/maps/billing-and-pricing/pricing, accessed 2026-07-30) [recommendation inferred]

## 3. Health and fitness platforms

### 3.1 Apple HealthKit

| Field | Detail |
|---|---|
| Purpose | TS-03 HealthKit sync (write workouts, read training history), the locked HealthKit-first data posture; WorkoutKit scheduling per stack rec section 3 |
| Provider | Apple HealthKit plus WorkoutKit (first-party frameworks, free) |
| Auth | HealthKit entitlement in the app ID plus per-data-type user permission prompts; purpose strings must fully describe use (guideline 5.1.1). [verified in regulatory doc] |
| Cost | $0 (covered by the $99/year Apple Developer Program) |
| Data in/out | Health data is P3 / GDPR Article 9. The architecture keeps ALL HealthKit data on-device (stack validation condition 2, load-bearing for the entire compliance posture); nothing flows to our servers. |
| Compliance and review | Guideline 5.1.3: no health data to third parties for advertising/marketing/data mining; disclosure to any third party requires express permission AND the third party must itself provide a health service to the user. 5.1.3(ii): no false HealthKit writes, no personal health info in iCloud. Privacy nutrition labels must declare health and precise-location collection accurately. From spring 2026, Health & Fitness apps declare medical device regulatory status per region: declare non-device wellness status. Expect App Review to scrutinize purpose strings and the standalone health privacy policy. [verified in regulatory doc, sections 3 and 7] |
| Failure mode | User denies permission: app runs with degraded personalization (the defined degraded mode from checklist item 3); tracking still works via CoreLocation. [inferred] |
| Phase | WS (write workout on run finish) |

### 3.2 Health Connect (Android)

| Field | Detail |
|---|---|
| Purpose | The Android analog of TS-03: write completed workouts, read training history, keep the health-data-on-device posture symmetric across platforms |
| Provider | Health Connect (Android on-device health data store, free, part of the platform since Android 14; SDK for earlier versions) [verified as to it being the platform health API; version specifics assumption B3] |
| Auth | Granular per-data-type runtime permissions (Android 16 made them finer-grained per the April 15, 2026 Play policy update); users grant read/write per type. [verified] (AppCompliance summary of the April 15, 2026 policy update, https://appcompliance.io/blog/google-play-health-connect-android-16-declaration/, accessed 2026-07-30) |
| Declaration process | Two mandatory Play Console artifacts: the Data Safety form and the Health apps declaration form (App content page, Policy > App content), declaring every health data type with a specific user-facing feature justification; narrowest-permission rule enforced; the app's privacy policy on the store listing must match the one linked inside Health Connect. Review happens as part of the standard app review process (no separate standalone approval anymore; the old Health Connect API Request form was retired January 2025). [verified] (Google Play Console Help, https://support.google.com/googleplay/android-developer/answer/14738291; Android developers, publish your health app, https://developer.android.google.cn/health-and-fitness/health-connect/publish; accessed 2026-07-30) |
| Review timeline | Bundled with app review, but sensitive-permission declarations are explicitly subject to extended review that Google says "may require up to several weeks", during which the release sits in pending publication. Plan Android submission at least 4 to 6 weeks before any launch date. [verified as to the extended-review language] (Play Console Help, declare permissions, https://support.google.com/googleplay/android-developer/answer/9214102, accessed 2026-07-30) [the 4 to 6 week planning buffer is inferred] |
| Cost | $0 |
| Data in/out | P3 / Article 9. Same on-device wall as HealthKit: workout data written locally to Health Connect, never to Waypoint servers. |
| Compliance | Prohibited uses tightened April 2026 (no employment or insurance eligibility use, no unauthorized sharing); Data Safety form must stay consistent with actual collection. [verified, AppCompliance source above] |
| Failure mode | Permission denied: same degraded mode as 3.1. |
| Phase | WS-equivalent for the Android build (if Android greenlit) |

### 3.3 Strava Upload API (write-only share)

| Field | Detail |
|---|---|
| Purpose | TS-07 Strava share: post completed runs TO Strava; never read Strava data (DEC-006 posture) |
| Provider | Strava API v3, Upload endpoints (POST /uploads with FIT/TCX/GPX, or POST /activities) |
| Auth | OAuth 2.0 authorization code flow; request ONLY `activity:write` scope (write-only by construction; do not request `activity:read` or `read_all`). Tokens refresh via the standard flow. [verified as to OAuth and scopes existing; the minimal-scope choice is our design] (Strava developers, https://developers.strava.com/docs/rate-limits/ and the API agreement below, accessed 2026-07-30) |
| Program admission | Admission to the Strava Developer Program is "at Strava's discretion and is not guaranteed", with no review-time SLA; the same discretion applies to rate limit and athlete capacity increases. The API Agreement was last updated June 1, 2026. Apply early. [verified] (Strava API Agreement, sections 3.1 and 3.6, https://cdn-1.strava.com/legal/api_policy; developers.strava.com noting the June 1, 2026 agreement date; accessed 2026-07-30) |
| Rate limits | Default overall: 200 requests per 15 minutes, 2,000 per day (upload endpoints count here); non-upload endpoints: 100 per 15 minutes, 1,000 per day; 429 on breach; daily reset midnight UTC. Documented raised example: 400/15min and 4,000/day with athlete capacity constraints. [verified] (https://developers.strava.com/docs/rate-limits/, accessed 2026-07-30) |
| Capacity math | At 10k MAU, if 30 percent of users share roughly 8 runs/month to Strava, that is ~24k uploads/month, ~800/day average but with evening/weekend peaks that can brush the 2,000/day default. A rate increase request (discretionary) belongs on the roadmap before 10k MAU; webhooks are irrelevant (we never poll). [inferred arithmetic on the verified limits] |
| The AI/ML ban and what it means for us | API Agreement section 5.3 prohibits using Strava API Materials or Strava Data, directly or indirectly, in connection with development, training, evaluation, or operation of ANY AI application, explicitly including fine-tuning, RAG, embeddings, and even "ingestion into a context window", and extends to derived, aggregated, or anonymized forms. For a write-only integration this is survivable BUT binding: (a) Waypoint must never read anything back from Strava (including athlete profile data beyond the OAuth handshake) into any feature, log, or model context; (b) even Strava's API responses to our uploads (activity IDs, status) are API Materials: store them for dedupe/bookkeeping only and wall them off from the coaching LLM surface entirely; (c) this re-confirms the prior-phase finding that Strava can never be a model input. [verified prohibition text] (Strava API Agreement section 5.3, accessed 2026-07-30) [the design consequences are inferred, high confidence] |
| Brand guidelines | "Connect with Strava" OAuth button and Strava attribution per their brand guidelines; screenshots of Strava-data surfaces and the connect button are what Strava asks for in rate-increase requests, so build to the guidelines from day one. [verified as to the screenshot expectation in Strava's rate-limit guidance; detailed brand rules assumption B4] |
| Data in/out | Out: completed run file (P3: GPS trace), cropped on-device by privacy zones BEFORE upload (compliance checklist item 1, stack rec section 5). In: upload status only. Sharing is per-run opt-in (checklist item 3, separate sharing consent). |
| Compliance | Strava becomes a recipient of user data on user instruction: disclose in the privacy policy and consent flow; it is not our processor (no DPA; it acts as an independent controller) [inferred, standard characterization; confirm with counsel]. Apple 5.1.3 is satisfied because Strava provides a fitness service to the user and the user grants express permission. [verified rule, inferred application] |
| Failure mode | Strava down or token revoked: queue the share locally and retry; run data is never lost (it lives on-device and in HealthKit). Honest-degradation copy on repeated failure. [inferred] |
| Phase | MVP (explicitly excluded from WS per mvp-scope section 6) |

### 3.4 Explicitly NOT integrating at MVP

| Platform | One-line status |
|---|---|
| Garmin | Garmin Connect Developer Program is PAUSED for new applications: the application form was removed, no projected reopening date, no waitlist; monitor developer.garmin.com. Do not put Garmin on any near-term roadmap. [verified via Garmin's own forum responses and corroborating coverage] (Garmin forums, https://forums.garmin.com/developer/connect-iq/f/discussion/434542/; Momentum analysis, https://www.themomentum.ai/blog/garmin-developer-program-closed-roadmap; accessed 2026-07-30) |
| Polar | v2 candidate: AccessLink API is self-serve (register at admin.polaraccesslink.com, OAuth2, no approval period), the easiest of the three when the time comes. [verified] (https://www.polar.com/accesslink-api/, accessed 2026-07-30) |
| Suunto | v2 candidate: requires the Suunto partner program application plus a signed API agreement; commercial use supported, personal use not. [verified] (https://apizone.suunto.com/faq, accessed 2026-07-30) |
| COROS | v2 candidate: API access by application to api@coros.com with company details; no self-serve portal. [verified as to the contact-based process per search results; process details assumption B5] |

## 4. Platform services

### 4.1 Push notifications: APNs and FCM

| Field | Detail |
|---|---|
| Purpose | No MVP v1 feature requires SERVER push (no social, no messages; run cues are local notifications). Wire push in v1.x with the paywall (renewal, win-back) and any safety features that need it. |
| Providers | APNs (free with the Apple Developer Program, token-based auth via .p8 key) and FCM (free on both Spark and Blaze plans, no message caps or per-message fees; delivers to iOS via APNs too). [verified as to FCM being free with no caps] (Firebase pricing, https://firebase.google.com/pricing/, accessed 2026-07-30) [APNs being included with ADP is long-standing platform behavior, verified via Apple's developer program scope] |
| Recommendation | Direct APNs on iOS; FCM on Android. Do NOT route iOS through FCM: it adds a Google SDK to the iOS binary for zero benefit and enlarges the privacy audit surface (checklist item 8). [inferred] |
| Auth | APNs: ES256 JWT from a .p8 key (server-side). FCM: Firebase service account (server-side). |
| Cost | $0 / $0 both. |
| Data in/out | Push tokens (P2) and notification payloads; never put health or location data in a push payload. [inferred rule implementing 5.1.3 posture] |
| Compliance | FCM requires accepting Google's Data Processing and Security Terms (GDPR mechanics exist; FCM is certified under the EU-US Data Privacy Framework per Firebase's compliance documentation). [verified via Firebase compliance summary in search sources; execute and archive per checklist item 9] |
| Failure mode | Push is never load-bearing for a run in progress (local notifications and audio run on-device). [inferred] |
| Phase | v1.x |

### 4.2 Sign-in

> **AMENDED 2026-08-06 by [[DEC-009 Revised data layer Aiven split architecture with decoupled auth]].** This section predates the database verdict and names Supabase Auth throughout. Read every "Supabase Auth" below as **Better Auth running in Waypoint's own API layer**, with identity tables in the Aiven Postgres so identity inherits EU residency. The App Store 4.8 analysis, the recommendation to ship Sign in with Apple plus email/passkey, and the decision to skip Google Sign-In at MVP are all unaffected. Cost changes from "inside the Supabase Pro line" to "inside the Aiven line"; the auth-outage failure mode becomes Waypoint's own API rather than a vendor's.

| Field | Detail |
|---|---|
| The rule | App Store guideline 4.8: apps using a third-party or social login (Google, Facebook, etc.) for the PRIMARY account must also offer an equivalent privacy-preserving option (limits data to name and email, private email relay, no ad tracking without consent). Sign in with Apple satisfies it by design. 4.8 does NOT apply if the app exclusively uses its own account system. [verified] (Apple App Review Guidelines section 4.8, https://developer.apple.com/app-store/review/guidelines/, accessed 2026-07-30) |
| Recommendation | Sign in with Apple (iOS, and via web flow on Android if needed) plus email/passkey through Supabase Auth as the equivalent-and-own-system option. SKIP Google Sign-In at MVP: it adds a Google SDK and OAuth consent-screen review for a marginal conversion gain on Android, where email/passkey plus Sign in with Apple's web flow suffice; adding it later is a v1.x decision that changes nothing architecturally (4.8 is already satisfied by Sign in with Apple). The walking skeleton ships Sign in with Apple only, per mvp-scope section 6. [inferred recommendation on the verified rule] |
| Providers | Sign in with Apple (free with ADP), Supabase Auth (included in the $25/month Pro plan, 100k MAU of auth, verified in stack docs), passkeys via the platform credential managers (free). |
| Auth model | OIDC (Sign in with Apple) into Supabase Auth; JWTs per stack validation condition 4 (auth blast-radius containment). |
| Cost MVP / 10k | $0 marginal (inside existing Supabase and ADP line items) |
| Data in/out | Name, email (possibly relay address) (P2). |
| Compliance | Consent ledger per checklist item 3; account deletion in-app (Apple requirement, checklist item 6). |
| Failure mode | Auth outage (Supabase): existing sessions keep working offline-first; new sign-ins blocked, which does not block an in-progress run. [inferred] |
| Phase | WS (Sign in with Apple), MVP (email/passkey) |

### 4.3 App review and beta channels

| Item | Detail |
|---|---|
| TestFlight (iOS) | Free with ADP; internal testers (up to 100) instant after processing, external testers (up to 10,000) require a lightweight beta review; builds expire after 90 days. The WS milestone (TestFlight by month 3 to 4, 20 to 50 runners) runs on external TestFlight. [verified as to TestFlight being the ADP beta channel; tester counts are long-standing published limits, assumption B6 to re-confirm at setup] |
| Play Console (Android) | $25 one-time developer registration. Internal testing (up to 100 testers, near-instant), then closed and open testing tracks. Gotcha for new PERSONAL accounts: Google requires a sustained closed test (on the order of 12 testers for 14 days) before production access; registering as an ORGANIZATION account avoids this. Waypoint should register the business account day one if Android is greenlit. [assumption B7 as to the exact tester/day numbers this pass; the personal-account testing requirement is widely documented and the org-account recommendation stands regardless] |
| Health app review gotchas (both stores) | iOS: 5.1.3 scrutiny, nutrition labels, medical-device status declaration (3.1). Android: Health apps declaration plus Data Safety consistency (3.2). Both: privacy policy links must be live at review time. [verified in regulatory doc and section 3 sources] |

### 4.4 Background location entitlements and store review

| Platform | What Waypoint needs | Review gotchas |
|---|---|---|
| iOS | "When In Use" authorization plus the location background mode (UIBackgroundModes: location) so tracking continues with the screen off during an active run started in the foreground. "Always" authorization is NOT needed for run tracking and should never be requested (smaller consent ask, smaller review surface). [inferred design on long-standing CoreLocation behavior; assumption B8 to validate in the WS build] | Purpose strings must name the feature ("records your route during runs"); App Review may ask why background mode is justified; the blue location indicator during runs is expected UX. [inferred from published guideline practice] |
| Android | ACCESS_FINE_LOCATION plus a foreground service with `foregroundServiceType="location"` and a persistent notification during runs. This is the standard fitness-tracker pattern and AVOIDS the ACCESS_BACKGROUND_LOCATION permission entirely (tracking happens while the user is "using" the app via the foreground service). [inferred, standard platform practice] | Two Play review layers regardless: (1) the new fine-location declaration (April 15, 2026 policy): all apps requesting ACCESS_FINE_LOCATION must justify in Play Console why coarse location or the new one-shot "location button" is insufficient; turn-by-turn navigation is Google's own named example of a justified persistent use; enforcement for Android 17+ targeting begins around late October 2026. (2) If ACCESS_BACKGROUND_LOCATION is ever added, it triggers the full background-location review: declaration form plus a 30-second-or-shorter video showing the feature, the prominent disclosure, and the runtime prompt, with reviews taking up to several weeks. [verified] (Play Console Help, minimum scope / location button, https://support.google.com/googleplay/android-developer/answer/17033915; background location, https://support.google.com/googleplay/android-developer/answer/9799150; accessed 2026-07-30) |

## 5. Monetization

### 5.1 RevenueCat over StoreKit 2 and Play Billing (both platforms confirmed)

| Field | Detail |
|---|---|
| Purpose | TS-08 subscription infrastructure (v1.x per gate decision GD-1: launch free, paywall after retention proof) |
| Both-platform coverage | Confirmed: RevenueCat wraps StoreKit on iOS and the Google Play Billing Library on Android (native SDKs plus a Kotlin Multiplatform SDK; the Android SDK 9.x line wraps Play Billing Library 8.x and handles the BillingClient lifecycle, receipt verification against the Google Play Developer API, acknowledgment, and RTDNs). One dashboard and entitlement model across both stores. [verified] (RevenueCat engineering blog and handbook, https://www.revenuecat.com/blog/engineering/kmp-migration and https://www.revenuecat.com/documents/revenuecat-handbook and https://www.revenuecat.com/guides/google-play-billing, accessed 2026-07-30) |
| Pricing | Free to $2,500 monthly tracked revenue, then 1 percent of gross MTR (roughly 1.4 percent of net after store commission); legacy-plan repricing history noted. (verified in stack docs, RevenueCat pricing accessed 2026-07-30) |
| Auth | SDK API keys per platform; server-side: Google service account with Financial data viewer for Play receipt validation, App Store Connect API key for Apple. [verified in RevenueCat docs above] |
| Cost MVP / 10k | $0 / roughly $65 (stack rec assumption A8 revenue model) |
| Data in/out | Purchase and subscription state (P2); no health, no location. Small SDK audit surface; DPA required (checklist item 9). [verified in stack docs] |
| Failure mode | RevenueCat outage: cached entitlements honor paid state on-device; purchases fall back to store-native flows and reconcile later. [inferred, standard RevenueCat behavior] |
| Phase | v1.x (paywall), account wiring can land at MVP |

### 5.2 Store commission tiers and small business programs

| Store | Standard | Reduced tier and how to get it | The trap |
|---|---|---|---|
| Apple App Store | 30 percent | Small Business Program: 15 percent for developers under $1M USD in prior-calendar-year proceeds (net of commission); ENROLLMENT REQUIRED: Account Holder enrolls at the program page, accepts the Paid Apps agreement (Schedule 2), lists Associated Developer Accounts; approval typically days, effective the following month. New developers qualify. [verified] (Apple, https://developer.apple.com/app-store/small-business-program/, accessed 2026-07-30) | The cliff: crossing $1M in the current year moves FUTURE sales to 30 percent for the rest of that year and the next; re-qualify the year after falling back under. Enroll BEFORE the first paid transaction (v1.x paywall), not after. [verified, same source] |
| Google Play | Historically 30 percent above the reduced tier | 15 percent service fee on the FIRST $1M of annual earnings for enrolled developers (enroll in Play Console: create the account group with any Associated Developer Accounts, accept the 15 percent tier terms); auto-renewing subscriptions get the reduced treatment regardless. Google restructured fees in some markets in 2026: subscriptions there are 10 percent plus a 5 percent billing fee. [verified] (Google Play Console Help, service fees, https://support.google.com/googleplay/android-developer/answer/112622, accessed 2026-07-30) | Graduated, not a cliff: only revenue ABOVE $1M pays the standard rate. Model each store separately in Phase 6 unit economics; the two programs behave differently past $1M. [verified structure; modeling note inferred] |

## 6. Observability and ops

### 6.1 Crash reporting: Sentry (recommended) vs Crashlytics

| Field | Detail |
|---|---|
| Purpose | Release overhead line in mvp-scope section 7 (crash triage); engineering standards (no silent failures) |
| Recommendation | Sentry. Crashlytics is free but is a Firebase/Google Analytics-coupled SDK, and the compliance posture (Apple 5.1.3, no-ad-tech wall, checklist item 8) already rejected tight Google analytics coupling in the stack rec's Firebase verdict. Sentry: Developer plan free (1 user, 5k errors/month, 30-day retention), Team $26/month (50k errors, unlimited users, 90-day retention), overages from ~$0.00029 per error. Self-host exists (Fair Source licensed, not OSI open source) as an exit if vendor posture ever changes. [verified] (Sentry pricing docs, https://docs.sentry.io/pricing/; cubeapm and nurbak 2026 pricing summaries; accessed 2026-07-30) |
| Auth | DSN keys in-app; SSO for dashboard. |
| Cost MVP / 10k | $0 (Developer) / $26 (Team) |
| Data in/out | Stack traces, device model, OS (P1 to P2). Configuration duties: disable IP collection, scrub coordinates and user identifiers from breadcrumbs, no health data in events ever; EU data residency option selected at org creation [assumption B9 on the EU region mechanics; verify at signup]. DPA required (checklist item 9). |
| Failure mode | Crash reporter down: app unaffected (fire-and-forget). |
| Phase | WS (first build should report crashes) |

### 6.2 Product analytics: TelemetryDeck plus a first-party cohort table

> **AMENDED 2026-08-06 by [[DEC-012 Measurement corrections analytics identity and re-based targets]].** The analysis below is correct about aggregate signals but incomplete, and the gap is load-bearing. TelemetryDeck deliberately provides **no stable per-user identifier**, which is exactly why it needs no consent banner, and that means it **structurally cannot produce cohort retention** — the number the MVP exists to prove and the gate for the paid layer. The approved split: **TelemetryDeck keeps the aggregate signal counters**, and **cohort retention lives in a first-party Postgres event table** keyed on the account identifier already held for sync, inside the Aiven personal-data store (DEC-009). No new vendor, no new consent basis, no new DPA. That event table is personal data and belongs in the DPIA and the consent ledger. PostHog EU stays the v1.x option for funnel analysis, as a deliberate decision rather than a default. Metric definitions live in `../06-business-model/metrics.md`.

The PRD's eight telemetry signals (route generation counts, repeat-generation rate, travel-mode share, acceptance rates, and similar) are aggregate behavioral counters, not user-journey funnels, which is exactly the shape a no-PII analytics service handles.

| Option | Terms | Fit |
|---|---|---|
| TelemetryDeck (recommended) | Privacy-first app analytics, German-hosted, no personal data collected (hashed identifiers, differential privacy), no consent banner and no ATT prompt needed; free tier 50,000 signals/month for accounts created after July 1, 2026 (100k grandfathered), paid plans from roughly $10/month with a July 2026 price increase; hard stop on free tier when exhausted. [verified] (TelemetryDeck pricing update, https://telemetrydeck.com/blog/pricing-update-2026/; press and FAQ pages; accessed 2026-07-30; exact new paid-tier prices not captured, assumption B10) | Best GDPR-clean fit: the eight signals fit signal-count analytics; no DPIA expansion, no consent UI, native Swift and Kotlin SDKs |
| PostHog EU (alternative) | Frankfurt-hosted cloud, 1M events/month free forever, then $0.00005/event sliding down; full funnel/cohort tooling; MIT-licensed self-host exists but is officially not recommended. [verified] (PostHog pricing and FAQ, https://posthog.com/pricing and https://posthog.com/faq, accessed 2026-07-30) | More power, more data processed (event-level, pseudonymous user level): requires DPA, cookieless config, and a consent story TelemetryDeck avoids; adopt only if v1.x funnel analysis demands it |
| First-party events into Postgres | $0, zero vendors | Viable at MVP scale but rebuilds dashboards; keep as the fallback posture |

Recommendation: TelemetryDeck at MVP ($0, then roughly $10/month at 10k MAU signal volume); revisit PostHog EU when paywall funnel analysis arrives in v1.x. This resolves stack rec assumption A6. Cost MVP / 10k: $0 / roughly $10 to $30. Data: anonymized signals (P1). No DPA needed for no-PII posture but execute their standard terms anyway and archive (checklist item 9 discipline). [inferred recommendation on verified facts]

### 6.3 Server monitoring and alerting

| Layer | Choice | Terms | Notes |
|---|---|---|---|
| Uptime and health checks | Uptime Kuma (self-host, MIT, free) on a separate tiny VM or free-tier host, NOT on the routing VM it monitors | Free software; a monitor must live off the monitored box | Watches GraphHopper /health, the orchestration API, Supabase endpoints, tile CDN [verified as to Uptime Kuma being free MIT self-hosted; placement rule inferred] |
| Metrics and dashboards | Grafana Cloud Free | Free forever tier: 10k active metric series, 50 GB each logs/traces/profiles, 3 users, 14-day retention, no credit card; Pro adds $19/month platform fee plus usage | Enough for one VM plus one API at MVP and 10k MAU [verified] (Grafana, https://grafana.com/products/cloud/free-tier/, accessed 2026-07-30) |
| Cron and pipeline heartbeats | healthchecks.io | Free tier for a handful of checks (exact free-check count not captured this pass, assumption B11); pings on missed graph-build or backup jobs | The graph rebuild and the nightly pg_dump (stack validation condition 5) each get a heartbeat [inferred design] |
| Alert routing | Grafana Cloud alerting plus healthchecks.io email/webhook to the founder's phone | Included in free tiers | Keep pager complexity at zero until there is an on-call rotation [inferred] |

Cost MVP / 10k: $0 to $5 / $5 to $20 (a small VM for Uptime Kuma if not colocated with anything). All monitoring data is P0 to P1 (infrastructure metrics; never user data in logs per stack rec section 5).

## 7. Comms

### 7.1 Transactional email

Waypoint's transactional volume is tiny by construction: auth emails (via Supabase Auth custom SMTP), account and consent notices, and deletion confirmations. Purchase receipts come from Apple and Google, not from us. Expected volume: well under 3,000/month even at 10k MAU. [inferred]

| Option | Terms | Verdict |
|---|---|---|
| Resend (recommended) | 3,000 emails/month free with no expiry (100/day cap); Pro $20/month for 50k. Developer-first, clean API. [verified] (2026 comparisons: dreaming.press and buildmvpfast.com email pricing pages, accessed 2026-07-30) | Free tier covers MVP and 10k MAU; adopt with DPA and EU-processing review at signup (data residency mechanics not captured this pass, assumption B12) |
| Postmark | Best-deliverability reputation; free tier only 100/month (test allowance), $15/month for 10k | The upgrade path if auth-email deliverability ever becomes a churn issue [verified, same sources] |
| Amazon SES | $0.10 per 1,000; the old 12-month free tier is gone for new accounts as of July 21, 2026 (new plan structure; $200 general AWS credits for the first 6 months); raw infrastructure, you build bounce/complaint handling | The at-scale exit, not the MVP choice; SES in eu-central-1 is also the cleanest EU-residency option if that requirement hardens [verified as to pricing and free-tier removal] (AWS blog, https://aws.amazon.com/blogs/messaging-and-targeting/introducing-amazon-simple-email-service-ses-pricing-plans/, accessed 2026-07-30) [EU note inferred] |

Cost MVP / 10k: $0 / $0 to $20. Data: email addresses (P2). DPA per checklist item 9.

### 7.2 Marketing stack

Deferred entirely: no marketing email, no engagement campaigns, no attribution SDKs at MVP (the no-ad-tech wall, checklist item 8); revisit with the v1.x paywall under a separate consent basis. [inferred, one line by design]

## 8. Summary artifacts

### 8.1 Master integration table

Costs are monthly, both platforms included. Compliance flags: ODbL (attribution/share-alike), DPA (processor agreement needed), A9 (GDPR Article 9 adjacency), LOC (sensitive location flows), REV (store review gate).

| # | Domain | Integration | Provider | Auth | MVP cost | 10k MAU cost | Compliance flags | Phase |
|---|---|---|---|---|---|---|---|---|
| 1 | Routing | Route generation | Self-hosted GraphHopper (Hetzner) | Internal | $25 | $120 | ODbL, LOC | WS |
| 2 | Routing | OSM data pipeline | Geofabrik extracts + daily diffs | None | $0 | $0 | ODbL | WS |
| 3 | Routing | Elevation data | AWS Terrain Tiles + Copernicus GLO-30 | None | $0 | $0 | Attribution | WS |
| 4 | Routing | Geocoding | Platform geocoders now; self-host Photon later | OS API / internal | $0 | $0 to $10 | LOC | MVP |
| 5 | Maps | iOS map rendering | MapKit | None | $0 | $0 | None | WS |
| 6 | Maps | Android map rendering | MapLibre + self-hosted Protomaps (Stadia fallback $20) | CDN key | $1 to $6 | $5 to $20 | ODbL, LOC | WS (if Android) |
| 7 | Weather | Forecast primary | Apple WeatherKit REST (both platforms) | ES256 JWT (server) | $0 | $0 to $50 | Attribution | MVP |
| 8 | Weather | Forecast fallback + history | Open-Meteo commercial | API key | $0 | $29 | DPA, CC BY 4.0 | v1.x |
| 9 | Weather | Air quality | Defer (Open-Meteo bundled when needed) | n/a | $0 | $0 | n/a | v1.x+ |
| 10 | Weather | Daylight/sun times | Local computation, no API | n/a | $0 | $0 | None | WS |
| 11 | Health | iOS health sync | HealthKit + WorkoutKit | Entitlement + user grant | $0 | $0 | A9, REV | WS |
| 12 | Health | Android health sync | Health Connect | Granular permissions + Play declaration | $0 | $0 | A9, REV | WS (if Android) |
| 13 | Health | Run sharing | Strava Upload API (activity:write only) | OAuth 2.0 | $0 | $0 | LOC, terms | MVP |
| 14 | Platform | Push (iOS) | APNs direct | .p8 JWT | $0 | $0 | DPA n/a | v1.x |
| 15 | Platform | Push (Android) | FCM | Service account | $0 | $0 | DPA (Google terms) | v1.x |
| 16 | Platform | Sign-in | Sign in with Apple + **Better Auth** email/passkey (DEC-009) | OIDC/JWT | $0 | $0 | Inside the Aiven DPA | WS |
| 17 | Platform | Beta channels | TestFlight + Play internal/closed testing | Store accounts | $8 (ADP) + $25 once (Play) | $8 | REV | WS |
| 18 | Platform | Background location | iOS background mode; Android FGS + fine-location declaration | OS + Play declaration | $0 | $0 | LOC, REV | WS |
| 19 | Monetization | Subscriptions | RevenueCat (StoreKit 2 + Play Billing) | SDK keys + store credentials | $0 | ~$65 | DPA | v1.x |
| 20 | Monetization | Commission tiers | Apple SBP + Play 15% tier (enroll both) | Store consoles | $0 | 15% of revenue | Enrollment | v1.x |
| 21 | Ops | Crash reporting | Sentry (Developer then Team) | DSN | $0 | $26 | DPA, config scrubbing | WS |
| 22 | Ops | Product analytics (aggregate signals) | TelemetryDeck | SDK key | $0 | $10 to $30 | No-PII posture | MVP |
| 22b | Ops | Cohort retention (DEC-012) | First-party Postgres event table in the Aiven store | Existing account identifier | $0 | $0 | Personal data: DPIA and consent ledger | MVP |
| 23 | Ops | Monitoring | Uptime Kuma + Grafana Cloud Free + healthchecks.io | Self-host / free accounts | $0 to $5 | $5 to $20 | None | WS |
| 24 | Comms | Transactional email | Resend (Postmark/SES alternates) | API key | $0 | $0 to $20 | DPA | MVP |
| 25 | Backend | Platform (reference) | **Superseded by DEC-009.** Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on the Hetzner private network for the moat, Better Auth in Waypoint's own API layer | Connection strings, IP allowlist | ~$80 to $120 | ~$150 to $250 | DPA, EU region | WS |

### 8.2 Total external-services cost

| Line | MVP (~1k MAU) | 10k MAU |
|---|---|---|
| Stack baseline (routing VM, data layer, ADP, misc). Originally costed on Supabase; DEC-009 substitutes Aiven plus the self-managed PostGIS box, which `../06-business-model/unit-economics.md` re-prices at $135 to $255 and $540 to $770 | $75 to $95 | $290 to $340 |
| New in this map: Android tiles, Sentry Team, TelemetryDeck, Open-Meteo commercial, email, monitoring VM, Play account amortized | $5 to $35 | $75 to $160 |
| Total external services | roughly $80 to $130 per month | roughly $350 to $500 per month |

Plus revenue-linked costs at 10k MAU: store commission 15 percent of gross (both programs, enrollment required) and RevenueCat roughly 1.4 percent of net, consistent with stack validation. All line items trace to the verified unit prices above; totals are [inferred] sums. iOS-only MVP trims roughly $10 to $30/month (no Android tiles, no Play account) but changes nothing structurally.

### 8.3 Critical path: integrations that gate the walking skeleton

In dependency order; everything else can land after the skeleton demo.

1. Apple Developer Program membership ($99/year): gates signing, TestFlight, HealthKit entitlement, WeatherKit, Sign in with Apple. Enroll day one. [verified dependencies]
2. Geofabrik extract + elevation tiles + GraphHopper local instance: the routing graph build; the week-one "loop primitive" proof from the stack rec build order. No account or approval needed from anyone. [verified]
3. Hetzner account with clean business verification (the account-risk mitigation from stack validation): production routing VM before any beta user. [verified in stack docs]
4. **Aiven for PostgreSQL (EU) project + DPA executed** (DEC-009, superseding the Supabase line): accounts, entitlements, consent ledger, and the DEC-012 cohort event table. Firewall allowlisted to the Hetzner VPS IP only.
5. HealthKit entitlement + purpose strings + Sign in with Apple capability: in the first Xcode project configuration. [verified]
6. Sentry DSN in the first build; TestFlight external beta review before the month 3 to 4 skeleton distribution. [inferred ordering]

If Android is greenlit for MVP, three long-lead items join the critical path in month 1, not month 6: Play Console organization account (avoids the personal-account closed-testing gate), the Health apps declaration draft, and the fine-location declaration justification (turn-by-turn navigation wording). Review cycles of up to several weeks make these the longest external lead times in the whole map. [verified review mechanics; scheduling inference]

Explicitly NOT on the critical path: Strava (MVP, not skeleton), WeatherKit (MVP), RevenueCat and both commission programs (v1.x), push (v1.x), air quality (deferred).

### 8.4 Top 5 integration risks

| # | Risk | Evidence | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Strava dependency: discretionary program admission with no SLA, a June 1, 2026 agreement whose AI ban reaches "ingestion into a context window" of even derived data, and a 2,000-upload/day default ceiling with discretionary increases | Strava API Agreement sections 3.6 and 5.3; rate-limit docs (accessed 2026-07-30) [verified] | TS-07 is the distribution and credibility play; losing or capping it hurts growth, not the core product | Apply for the program in month 1; write-only architecture with API responses walled off from every AI surface; request the rate increase before 10k MAU; the app must remain fully useful with Strava disconnected (it is, by design) |
| 2 | Android review stack delays: Health apps declaration, Data Safety consistency, fine-location declaration (enforcement from late October 2026 for Android 17 targeting), and possible background-location review with video, each able to hold a release for weeks | Play Console Help pages (accessed 2026-07-30) [verified] | Slips the Android launch date, and re-reviews can hold UPDATES hostage later | Start Play Console paperwork in month 1 if Android is greenlit; foreground-service design avoids ACCESS_BACKGROUND_LOCATION entirely; keep declarations version-controlled with the release checklist |
| 3 | WeatherKit terms for non-Apple use: the REST API officially serves Android today, but Waypoint would be depending on Apple's continued goodwill to power a competitor platform's client, plus the unresolved safety-adjacent licensing question | Apple WeatherKit REST docs naming Android (accessed 2026-07-30) [verified]; terms-shift risk [inferred] | Weather features degrade on Android; cost jumps if Apple tiers change | Open-Meteo commercial ($29/month) is a same-shape drop-in already planned as fallback; weather is never load-bearing for safety claims (H-09 framing) |
| 4 | ODbL share-alike boundary on the moat: the crossing graph and any OSM-derived context layer may be a Derivative Database that must be made available on request, and tiles/geocoding/routing all amplify OSM exposure | OSMF license guidance (verified in stack docs); Geofabrik license terms (accessed 2026-07-30) [verified] | Worst case: a competitor requests the derived crossing dataset; moat narrows to scoring models and freshness | Counsel review of layer boundaries before launch (already an open question in stack rec); keep municipal and user-derived layers as separate Collective Database members; accept that scoring models and personalization are the defensible moat |
| 5 | Public-instance and free-tier policy traps: Nominatim public API bans commercial heavy use outright, Photon's demo throttles, MapTiler and Stadia free tiers are non-commercial only, and TelemetryDeck just cut its free tier 50 percent with a price increase | Provider policies and July 2026 pricing pages (accessed 2026-07-30) [verified] | An innocently wired free endpoint becomes a production outage or a terms violation | The self-host-first posture in this map (Photon, Protomaps, Uptime Kuma) plus explicit commercial tiers everywhere else; nothing in the shipped app may call a donated public instance |

## Assumptions

- B1: iOS CLGeocoder and Android platform Geocoder per-call rate limits and terms for our reverse-geocoding volume were not verified this pass; validate in the WS build before relying on them.
- B2: Open-Meteo DPA execution mechanics (self-serve vs request) not verified; confirm when contracting the Standard tier.
- B3: Health Connect minimum Android version and SDK back-compat specifics not captured this pass; confirm during Android platform decision.
- B4: Strava brand guideline details (button assets, naming rules) not read in full this pass; pull the brand guidelines page during TS-07 implementation.
- B5: COROS API onboarding details rest on secondary sources; confirm directly with api@coros.com if COROS moves up the roadmap.
- B6: TestFlight tester limits (100 internal, 10,000 external, 90-day builds) are long-standing published values but were not re-verified this pass.
- B7: Google Play's closed-testing requirement for new personal accounts (on the order of 12 testers for 14 days) not re-verified this pass; the organization-account recommendation stands regardless.
- B8: iOS "When In Use" plus background location mode sufficing for continuous run tracking is standard platform behavior but must be validated in the walking skeleton on real devices.
- B9: Sentry EU data residency selection mechanics at org creation not verified this pass; confirm at signup and record in the processor inventory.
- B10: TelemetryDeck post-July-2026 paid-tier price points not captured; budget uses the roughly $10/month starter figure pending signup verification.
- B11: healthchecks.io free-tier check count not captured this pass.
- B12: Resend data residency and DPA mechanics not verified; review at signup, with SES eu-central-1 as the EU-residency fallback.

## Open questions

- Does the platform study greenlight Android for MVP? It changes the critical path (8.3) and adds roughly $10 to $30/month, but no provider choices. #open-question
- Strava Developer Program application outcome and timeline (discretionary, no SLA): apply month 1 and track. #open-question
- ODbL layer-boundary counsel review (carried from stack rec): now also covers tiles and geocoding surfaces. #open-question
- WeatherKit safety-adjacent licensing (carried from compliance doc). #open-question
- Ferrostar spike outcome (carried from stack validation): decides whether a navigation SDK joins this map or guidance stays fully in-house. #open-question

## Related

- `research/05-product/mvp-scope.md` (the 15 features this map serves)
- `research/05-product/stack-recommendation.md` and `stack-validation.md` (architecture and verified pricing this map extends)
- `research/01-market/regulatory-compliance.md` (the 15-item checklist referenced throughout)
- `research/00-RESEARCH-PLAYBOOK.md` (standards followed here)
