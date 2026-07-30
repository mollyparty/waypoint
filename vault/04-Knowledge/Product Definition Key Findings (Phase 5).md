---
type: knowledge
created: 2026-07-30
updated: 2026-07-30
tags: [knowledge, research, product, mvp, stack, phase-5]
---

# Product Definition Key Findings (Phase 5)

Distilled from `research/05-product/` (5 documents: prd, rice-prioritization, mvp-scope, user-journeys, stack-recommendation). Governed by the locked concept ([[DEC-006 Concept lock route-first positioning]]). Gate pending Claudio's review.

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

## Gate decisions (dashboard cards 5 to 8)

1. MVP scope as drawn: **approved** (DEC-008).
2. Free/paid line: **launch v1 entirely free**; safety routing free permanently (DEC-008).
3. Watch: **fast-follow** at launch+30 (DEC-008).
4. Stack: **still open**. Round 1 validation done; Claudio required round 2 (`database-deep-dive.md`, `dual-platform-strategy.md`, `api-integration-map.md`). Dual-platform MVP requirement amends prior iOS-first assumption.

Operational, no gate once stack locks: month-1 safety-data buildability spike; interviews priorities 1 and 2 in parallel.

## Open items carried forward

- Age floor (16+ vs 18+) needs its own DEC. #open-question
- Redlining/fairness exposure of safety scoring: counsel plus fairness review before launch. #open-question
- Strava upload terms re-read at build time (write-only from an AI app).
- Weather API paid tiers unverified (WeatherKit figures verified; Open-Meteo/Tomorrow.io marked [assumption]).

## Related

- [[DEC-006 Concept lock route-first positioning]]
- [[Concept and Positioning (Phase 4)]]
- [[User Research Key Findings (Phase 3)]]
