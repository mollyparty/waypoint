---
type: project
created: 2026-07-30
updated: 2026-08-06
status: locked
tags: [project, charter]
---

# Charter

> [!note] Locked
> Concept locked by Claudio at the Phase 4 gate on 2026-07-30 ([[DEC-006 Concept lock route-first positioning]]). The governing concept document is `research/04-synthesis/concept.md`. Changes require a new decision record.

## What is Waypoint?

**Know where to run.** Waypoint is the running app that knows where you should run: its hero capability is **constraint-based adaptive route generation**, answering "where should I run, right now, from here, for me" with routes that treat distance, elevation, weather and humidity, street crossings, surface, safety-awareness, and the runner's training state as routing inputs. A paid adaptive coaching layer connects what the runner's body needs to where the runner goes; voice-guided navigation executes it; privacy zones are day-one architecture.

**Positioning (locked):** For committed amateur runners who never quite know where today's run should go, Waypoint is the running app that generates the right route for you, right now, from wherever you stand.

## Problem it solves

Runners never quite know where today's run should go: a new city, a dark morning, a heat wave, a tempo workout, or plain boredom with the same loops. Training apps prescribe workouts without location intelligence; route apps draw static lines without training context. Travel is the sharpest activation moment; safety-aware routing and route novelty at home are the daily retention wedge (H1 reframe, accepted at the gate).

## Audience

- **Primary: the committed amateur** (persona Marcus): 3 to 5 runs/week, races a few times a year, self-coached, the only segment with proven willingness to pay.
- **Secondary: the ambitious beginner** (persona Jake): the Gen Z growth pipeline, same product with gentler calibration.
- Activation-critical profiles within the primary: the traveling professional (Priya) and the safety-first runner (Elena).

## Success criteria

- 12 months out: MVP live, thousands of active runners, seed round closed or in motion.
- The Business Blueprint (Phase 8) is the fundraising instrument; the investor story carries the expansion path (geographies, the same route engine pointed at walking, cycling, hiking). Android is no longer an expansion item: it ships with the MVP under DEC-010.
- Monetization: freemium subscription; free tier anchors on route generation, paid tier on the adaptive layer. Boundary set at the Phase 6 gate by [[DEC-011 Pricing and the permanent free tier]]: the coaching layer alone is paid, everything else including safety-aware routing is free permanently, and the safety-free-tier question deferred from Phase 3 is closed.

## Team

Three founding partners, none full-time. Equity, vesting and legal structure are Phase 9 work and are not yet decided.

- **Asher** - embedded target user and subject matter expert; owns real-world route testing. In 10th grade.
- **Claudio** - project manager and operations; the elastic role that covers whatever the business needs. In 10th grade. Co-originated the concept with Asher.
- **Daniel** - technical and commercial lead; product management, business and brand development; funds the initial AI tooling. Runs another business full-time.

The build is AI-assisted rather than contracted: the plan is to avoid hiring while the team is this small.

## Constraints

- No founder is full-time, and two are minors. This governs capacity, legal capacity, and the timeline (Phase 9). The engineering mantra (security, stability, reliability, compliance) applies to everything shipped regardless.
- Location plus health data make privacy compliance first-class: privacy zones, private-by-default, the 15-item MVP compliance checklist.
- v1: **one React Native codebase shipping iOS and Android** ([[DEC-010 Staged cross-platform MVP on React Native]]); MapLibre maps on both. **The month 9 to 10 iOS date is under review in Phase 9**, because DEC-010 assumed 2.5 to 3.0 full-time-equivalent people and the actual founding team has none. HealthKit-first on iOS, Health Connect on Android (Garmin developer program paused; Strava API bans AI use of its data).
- Data layer: Aiven for PostgreSQL (EU) for personal data, self-managed PostGIS on Hetzner for the geospatial moat, auth in Waypoint's own API layer ([[DEC-009 Revised data layer Aiven split architecture with decoupled auth]]; revisitable before the walking skeleton).
- Execution window: an estimated 12 to 18 months before Strava plausibly ships plan-linked route generation. Speed is a business requirement.

## Related

- [[Founder-Brief]] - the original vision and hypotheses
- [[DEC-006 Concept lock route-first positioning]] - the gate decisions
- [[00-START-HERE]]
- [[_Decision-Log]]
