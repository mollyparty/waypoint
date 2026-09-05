---
type: decision
id: DEC-010
status: accepted
created: 2026-08-06
updated: 2026-09-05
tags: [decision, platform, mvp, stack, phase-5]
---

# DEC-010 Staged cross-platform MVP on React Native (iOS first, Android 4 to 8 weeks later)

## Amendment, 2026-09-05

[[DEC-014 Recut v1 first-release baseline]] supersedes the first-release scope and earlier schedule. The React Native platform choice remains accepted. Original reasoning below is historical.

## Context

DEC-006 locked the concept on an iOS-first assumption, and DEC-008 approved a ~25 person-month iOS-native MVP. Claudio then amended the requirement: **the MVP must launch on both iOS and Android.** `research/05-product/dual-platform-strategy.md` costed four ways to honor that against the competitive window that `positioning.md` puts at 12 to 18 months.

## Decision

**Option D, approved 2026-08-06: one React Native (Expo) codebase, MapLibre maps on both platforms, staged launch.** iOS ships first at month 9 to 10; Android is certified and ships 4 to 8 weeks later. Native modules are used where the platform requires them (HealthKit, Health Connect, background geolocation, on-device Apple Foundation Models); native Swift is reserved for the Watch app fast-follow.

This **amends** two previously approved items:

- **Client framework**: SwiftUI + MapKit → **React Native + MapLibre Native** on both platforms.
- **MVP effort**: ~25 person-months → **~29 to 31 person-months**; iOS month 9 to 10, Android month 10 to 12.

The 15-feature MVP list itself is unchanged, on both platforms.

## Rationale

- **The switching cost is at its lifetime minimum right now.** No application code exists. Rebasing the client before the first line is written costs roughly 4 to 6 added person-months; the same move after an iOS build would cost a rewrite.
- **Runna is the existence proof.** The top-rated app in Waypoint's exact category, at millions of users and an Apple App of the Year finalist, ships GPS run tracking, adaptive training plans, health and wearable integrations, and RevenueCat subscriptions on both platforms from one React Native codebase, keeping native Swift only for the Watch app. Every hard requirement except custom turn-by-turn guidance has a production precedent, and guidance is shared TypeScript geometry over platform TTS.
- **It protects the window.** Simultaneous dual-native costs 38 to 40 person-months and pushes launch to month 11 to 13, putting the paid layer at the window's edge. Option D lands iOS inside the approved envelope's buffer.
- **One codebase keeps the roadmap at approved cost.** Under two native codebases, the ~17 person-months of v1.x fast-follow work (paywall plus training-state generation, crossings, weather, surface, offline, GPX) becomes 28 to 30. The window battle is won in v1.x, not v1.
- **MapLibre on both platforms beats MapKit for parity**: one styling system, one render behavior to debug, zero usage fees, no third-party data flow, and direct alignment with Ferrostar, whose UI is built on it.

## Alternatives considered

- **Option A/B, simultaneous launch**: 38 to 40 person-months (native) or a compressed cross-platform push; both endanger the competitive window for reach that carries little MVP-stage revenue. Rejected.
- **Option C, staged native (two codebases)**: preserves every approved stack choice, but costs ~38 to 40 person-months and doubles client maintenance permanently. Rejected.
- **iOS-only launch, Android in v1.x**: honestly supported by the revenue evidence (iOS carries roughly 85 percent of category subscription revenue, and Strava, AllTrails, and Komoot all staged their launches). Rejected because both-platform coverage is a founder requirement, and Option D's codebase makes Android cheap enough that the trade is worth 4 to 6 person-months.
- **Flutter**: credible runner-up, with Coopah proving the category. Lost on talent pool and the Runna precedent. **Kotlin Multiplatform**: rejected at this team size, because it still requires writing two UI layers, which is most of Option A's cost.

## Consequences

- MVP effort rises to ~29 to 31 person-months; iOS month 9 to 10, Android month 10 to 12, full launch month 11 to 13. `research/05-product/mvp-scope.md` numbers are amended accordingly. No added headcount.
- Framework dependency on React Native and Expo is accepted in exchange for permanent one-codebase economics. #risk
- **Android long-lead paperwork starts month 1**: Play organization account, Health Connect declaration (roughly 2 weeks of review lead time), and the fine-location declaration. Missing this is the most likely cause of an Android slip. #risk
- **Background GPS survival against OEM battery killers** is the hardest Android-specific engineering problem. It is a hardening tax every Android running app pays (Strava, Runna, adidas Running all live with the foreground-service pattern), not a wall. #risk
- The **Ferrostar week-one spike now has to answer for two platforms**, and its React Native bindings are work-in-progress with no published package, so guidance ships via thin native modules or a shared-TypeScript reimplementation of its core pattern.
- **Open verification before Android work begins**: whether Garmin Connect writes the needed data into Health Connect. H6 was verified for HealthKit only. #open-question
- On-device Apple Foundation Models remain iOS-only; Android gets template explanations at launch, which matches the older-iPhone degradation path already approved.

## Related

- `research/05-product/dual-platform-strategy.md` (four-option costing, competitor launch history, sources)
- `research/05-product/api-integration-map.md` (per-platform integration inventory)
- [[DEC-006 Concept lock route-first positioning]] (client stack amended here)
- [[DEC-008 Phase 5 gate MVP approved stack in validation]] (effort amended here)
- [[DEC-009 Revised data layer Aiven split architecture with decoupled auth]]
- [[_Decision-Log]]
