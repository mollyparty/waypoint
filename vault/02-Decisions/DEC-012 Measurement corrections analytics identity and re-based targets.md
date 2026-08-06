---
type: decision
id: DEC-012
status: accepted
created: 2026-08-06
updated: 2026-08-06
tags: [decision, metrics, analytics, privacy, phase-6, correction]
---

# DEC-012 Measurement corrections: analytics identity and re-based targets

## Context

Phase 6's `research/06-business-model/metrics.md` found two problems in work already approved in Phase 5. Neither was a Phase 6 question; both were caught because designing the metric tree forced someone to check whether the chosen instrumentation could actually produce the numbers the PRD promised.

**Problem one, a genuine contradiction.** Cohort retention is the number the entire MVP exists to produce and the gate for the paid layer. Measuring it requires a stable per-user identifier that persists over time. TelemetryDeck, the analytics vendor selected in `research/05-product/api-integration-map.md`, **deliberately does not provide one** — that design choice is precisely why it requires no consent banner. So the privacy-preserving analytics decision, as specified, cannot deliver the metric the PRD's own goals require.

**Problem two, an untenable target.** The PRD's goal G4 sets 25 percent day-30 retention measured at install level. Against every published benchmark, that would place Waypoint far outside the top decile of the entire Health and Fitness category in its first month. G3 has a related definitional problem.

## Decision

Approved 2026-08-06 at the Phase 6 gate:

1. **Cohort retention lives in a first-party Postgres event table**, keyed on the account identifier Waypoint already holds for sync, inside the Aiven personal-data store (DEC-009). No new vendor, no new consent basis, no new data-processing agreement: a handful of hand-built SQL views. **TelemetryDeck stays** for aggregate, identifier-free product analytics, which is what it is good at.
2. **PRD goals G3 and G4 are re-based to activated-cohort definitions**, each paired with a separate install-level line retained purely for benchmark comparison.
3. **Activation is redefined** as *first Waypoint-generated route completed as a recorded run, within seven days of install*, replacing the PRD's "generate and start". The daily-readable leading indicator is Ignition: the share of first sessions reaching a route on screen, median under 180 seconds.

## Rationale

- **The first-party route resolves the contradiction without weakening the privacy posture.** The account identifier already exists and already has a lawful basis, because it is what makes sync work. Reusing it for retention analysis adds no new personal data, no new processor, and no new consent surface, while keeping the data inside the EU-resident store chosen in DEC-009. Adding PostHog EU would have been more capable out of the box but introduces a vendor, a consent basis, and an agreement to negotiate, which is a v1.x decision rather than a default.
- **A target nobody can hit stops functioning as a target.** G4 at install level would have been missed in month one no matter how good the product was, which teaches the team nothing and misleads any investor who sees it. Split into an activated-cohort target (honest internal signal) plus an install-level line (comparable external benchmark), both numbers do a job.
- **The activation redefinition matters more than it looks.** "Generate and start" counts mid-run abandonment as success, and mid-run abandonment is exactly the signature of a bad route. Since `mvp-scope.md` names bad routes as the real MVP risk, an activation metric that cannot see them is actively harmful.

## Alternatives considered

- **Add PostHog EU.** More capable, but a new vendor, consent basis, and DPA for a job the existing account identifier can already do. Deferred to v1.x as a deliberate decision rather than adopted as a default.
- **Drop cohort retention and rely on aggregate metrics.** Rejected: retention is the gate for the paid layer and the core evidence for the seed round. It is not optional.
- **Leave the PRD targets as written.** Rejected for the reason above.

## Consequences

- Retention analysis becomes hand-built SQL rather than a vendor dashboard, which costs founder time each week. Acceptable at this scale, and `metrics.md` already limits the reporting cadence to what one person can sustain. #risk
- `research/05-product/prd.md` and `research/05-product/api-integration-map.md` both require edits to match this decision; leaving them unamended would recreate the contradiction for the next reader.
- The event table is personal data under GDPR and belongs in the DPIA and the consent ledger alongside the rest of the Aiven store.
- Four further privacy tensions identified in `metrics.md` section 9 are resolved there and inherit this decision's approach: coarse on-device metro labels with k-anonymity suppression for geographic route-quality segmentation, never attached to a user timeline, because a per-user sequence of metro labels is a travel diary. GPS-trace mining stays deferred behind a DPIA.

## Related

- `research/06-business-model/metrics.md` (sections 1, 3, 9), `business-model-canvas.md` section 10.4
- `research/05-product/prd.md`, `research/05-product/api-integration-map.md` (both amended by this decision)
- [[DEC-009 Revised data layer Aiven split architecture with decoupled auth]]
- [[_Decision-Log]]
