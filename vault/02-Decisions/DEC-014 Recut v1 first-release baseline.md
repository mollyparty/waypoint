---
type: decision
id: DEC-014
status: accepted
created: 2026-09-05
updated: 2026-09-05
tags: [decision, scope, phase-9]
---

# DEC-014 Recut v1 first-release baseline

## Context

Claudio explicitly approved: "I approve the Recut v1 scope for our first-release baseline." The full 15-feature MVP model required 32.52 React Native person-months against approximately 7.5 person-months of annual team capacity. The catalog already defines Recut v1 as reduced slices of eight features plus all 34 compliance and quality obligations.

## Decision

Adopt the existing Recut v1 preset as the first-release baseline: H-01, X-01, TS-01, TS-03, TS-04, TS-05, TS-06 and O-01, using each entry's `skeletonScope` and `skeletonEffort`, plus the 15 compliance and 19 non-functional requirements. Preserve all future feature specifications and the historical full-MVP comparison. Detailed acceptance criteria must be mapped to these reduced slices before implementation.

## Rationale

This first release tests the core loop: generate a route, run it with voice guidance, and save the run. The accepted catalog model is 13.38 React Native person-months, projecting iOS at about month 13, within the existing month 12 to 14 planning range. This is a relative planning estimate, not a committed calendar launch date. Team capacity and the unmeasured 1.8x AI productivity assumption must be validated.

## Alternatives considered

- Full 15-feature MVP: retained as historical comparison, not the first-release commitment; approximately month 30 under the same assumptions.
- Walking skeleton alone: insufficient for public release because it omits the compliance and quality package.
- PRD P0 scope: retained as requirements analysis, not approved first-release scope.

## Consequences

Phase 9 card 1 closes. DEC-010's earlier scope/schedule is superseded for the first release; the React Native platform choice remains. The other five Phase 9 decisions remain open. No equity, vesting, option pool, incorporation or fundraising approval is implied.

The reduced slice removes some feature interfaces but does not waive obligations. Before coding, reconcile safety-aware routing, honest refusal, consent and accessibility requirements with the thin slices. Any missing work requires an explicit scope/cost correction, not silent omission. Deferred release assignments are planning buckets, not promises of shipment immediately after launch.

## Next steps

1. Review the remaining founder agreement decisions together: equity, vesting and option pool, then formation timing and financing.
2. Prepare a sprint-zero backlog mapping the eight slices and obligations to acceptance criteria and dependency checks.
3. Confirm the beachhead metro, available founder hours and build start before dating milestones. Plan the safety-data/buildability spike and real-user interviews.
4. Reconcile finances to the accepted scope and approved pricing before blueprint sign-off. Tag v0.4.0 only after remaining approvals.

## Related

- [[DEC-020 Features catalog is the source of truth for release phase]]
- [[DEC-010 Staged cross-platform MVP on React Native]]
- [[_Decision-Log]]
