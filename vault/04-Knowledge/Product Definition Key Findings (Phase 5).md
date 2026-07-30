---
type: knowledge
created: 2026-07-30
updated: 2026-07-30
tags: [knowledge, research, product, mvp, stack, phase-5]
---

# Product Definition Key Findings (Phase 5)

Distilled from `research/05-product/` (9 documents: prd, rice-prioritization, mvp-scope, user-journeys, stack-recommendation, stack-validation, database-deep-dive, dual-platform-strategy, api-integration-map). Governed by the locked concept ([[DEC-006 Concept lock route-first positioning]]). Gate partially passed (DEC-008); stack and platform decisions open.

## The MVP line

- **15 features in MVP v1** (of 30 RICE-scored candidates): core constraint generation (distance, start-anywhere, round-trip, elevation), route novelty, safety-aware routing v1, travel mode, honest degradation, voice turn-by-turn, GPS tracking, run history, HealthKit sync, Strava share, onboarding, full privacy/compliance architecture.
- **Effort**: ~25 person-months; 8 to 10 calendar months with founder plus two contractors. Walking skeleton (generate route, run with voice, save) on TestFlight month 3 to 4; App Store launch month 8 to 9; paid layer months 10 to 12. Fits inside the Strava window.
- **Fast-follow v1.x**: paywall plus training-state generation (together), Watch app (launch+30), crossings, weather, surface, offline, GPX. Each deferral has a named pull-forward trigger.
- **v2+**: adaptive plans, injury calibration, race progression, readiness, live location sharing (pending privacy review).

## The recommended stack

- **Routing: self-hosted GraphHopper** (Apache 2.0). The only engine with a native round-trip primitive AND custom cost models that can ingest proprietary crossing/lighting data. Hosted APIs cannot, which would reduce Waypoint to commodity routing. Prototype on the cloud free tier weeks 1 to 4; production self-host before beta. Fallback: Stadia-hosted Valhalla (degraded moat).
- **Moat data: Supabase Postgres + PostGIS** for crossing and lighting layers. ODbL share-alike boundary needs counsel review.
- **Weather: WeatherKit** (500k calls/month free). **Map/nav: SwiftUI + MapKit with custom voice guidance** (2-day Ferrostar spike planned; Mapbox is the fallback).
- **Coaching AI: on-device Apple Foundation Models**: health data never leaves the device, collapsing the GDPR Article 9 server surface.
- **Subscriptions: RevenueCat** (1 percent of revenue; revisit past ~$50k MTR).
- **Infra cost**: $75 to $95/month at MVP; ~$300/month at 10k MAU. Infra is a rounding error; the scaling cost is ops time.

## Journeys and design principles

Five journeys mapped (onboarding under 3 minutes, Marcus daily, Priya hotel lobby under 30 seconds, Elena dark morning, Jake plan repair). Ten design principles, led by: explain reasoning always, degrade honestly, never promise "safe" (enforceable copy rule: "safety-aware" is the ceiling), ask at the moment of value, the free path always works, feed Strava and never compete with it. Top design surfaces: generate screen, route reveal with why-card, onboarding/permissions, in-run navigation, plan repair flow.

## Stack validation (second opinion, requested by Claudio at the gate)

`stack-validation.md`: **no layer revised**. Supabase CONFIRMED WITH CONDITIONS (Frankfurt region day one, health data stays on-device which keeps compliance at $25/month instead of $950+, DPA executed, auth blast radius contained via own API layer, nightly off-platform backups). Hetzner CONFIRMED WITH CONDITIONS (off-provider backups plus IaC week one, restore drill, OVH fallback runbook, week-one GraphHopper memory load test). MapKit, on-device Apple AI, RevenueCat, and Vercel-for-artifacts-only all CONFIRMED. Every Supabase alternative failed on at least one criterion (Neon metering and acquisition risk, RDS 5 to 10x cost, Fly.io Postgres deprecated, Firestore no geo queries, PlanetScale PostGIS disabled vendor-side). Scale narrative: zero migrations through 10k MAU; 100k is a checkpoint not a forced move; at 1M every migration is a 2 to 6 week project. Top risks: Supabase Auth lock-in, Hetzner account termination, GraphHopper US-graph memory sizing.

## Round 2 studies (requested by Claudio; all complete 2026-07-30)

- **Database deep dive** (`database-deep-dive.md`): asked "is Supabase really necessary" and the answer is no. 12 candidates scored on Security 25% / Reliability 20% / Compliance 20% / Stability 15% / PostGIS 10% / Ops 5% / Cost 5%. **Aiven for PostgreSQL 4.46 vs Supabase 3.45.** Verdict: **split architecture**: Aiven (EU-incorporated, ISO 27001 + SOC 2 Type II, 99.99% SLA, PITR standard) for personal data; **self-managed Postgres+PostGIS on the Hetzner private network** (zero public exposure, zero personal data, rebuildable in hours) for the geospatial moat; **auth decoupled into Waypoint's API layer via Better Auth** (identity tables in Aiven; Ory Kratos is the security-maximal alternative). Runner-up: OVHcloud managed Postgres. This supersedes round 1's "Supabase with conditions" verdict; unchanged: Postgres+PostGIS itself, Hetzner compute, on-device health wall.
- **Dual-platform strategy** (`dual-platform-strategy.md`): four options costed. Simultaneous dual-native = 38 to 40 pm, launch month 11 to 13, endangers the window. **Recommended: Option D, staged cross-platform on React Native (Expo) + MapLibre on both platforms**: ~29-31 pm, iOS month 9-10, Android 4 to 8 weeks later, one codebase forever. Existence proof: Runna (category leader, Strava-acquired) ships both platforms from one React Native codebase. Flutter runner-up; KMP rejected at this team size. Amends DEC-006-adjacent choices: SwiftUI → React Native, MapKit → MapLibre. iOS carries ~85% of category subscription revenue, so an honest third option is iOS-only launch with Android in v1.x.
- **API integration map** (`api-integration-map.md`): ~20 required integrations across 7 domains (30 cataloged incl. fallbacks/deferrals); only 6 gate the walking skeleton. External services **~$80-130/mo at MVP, ~$350-500/mo at 10k MAU**, plus store commission (15% small-business tiers both stores, enrollment required before first paid transaction) and RevenueCat ~1.4% of net. Top risks: Strava discretionary program terms and its 2026 AI ban; Android Health Connect + fine-location review lead times (start Play paperwork month 1 if Android greenlit); WeatherKit-on-Android goodwill (Open-Meteo commercial $29/mo is the drop-in fallback, resolving assumption A5); ODbL share-alike boundary (counsel).

## Gate decisions (dashboard cards 5 to 9)

1. MVP scope as drawn: **approved** (DEC-008).
2. Free/paid line: **launch v1 entirely free**; safety routing free permanently (DEC-008).
3. Watch: **fast-follow** at launch+30 (DEC-008).
4. Stack: **awaiting decision** (card 8). Round 2 recommends the Aiven split architecture with decoupled auth, replacing Supabase.
5. Platform: **awaiting decision** (card 9). Round 2 recommends staged React Native (Option D). Whichever way it goes needs a new DEC.

Operational, no gate once stack locks: month-1 safety-data buildability spike; interviews priorities 1 and 2 in parallel.

## Open items carried forward

- Age floor (16+ vs 18+) needs its own DEC. #open-question
- Redlining/fairness exposure of safety scoring: counsel plus fairness review before launch. #open-question
- Strava upload terms re-read at build time (write-only from an AI app).
- ~~Weather API paid tiers unverified~~ Resolved: Open-Meteo commercial pricing verified ($29/mo Standard) in `api-integration-map.md`.
- Garmin Connect → Health Connect write path unverified (H6 verified for HealthKit only); must confirm before Android commitment. #open-question

## Related

- [[DEC-006 Concept lock route-first positioning]]
- [[Concept and Positioning (Phase 4)]]
- [[User Research Key Findings (Phase 3)]]
