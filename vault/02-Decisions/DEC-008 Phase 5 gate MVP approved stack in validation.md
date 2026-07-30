---
type: decision
id: DEC-008
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, product, mvp, stack, phase-5]
---

# DEC-008 Phase 5 gate: MVP approved, stack held for validation

## Context

Phase 5 produced the PRD, RICE prioritization, MVP scope, user journeys, and a stack recommendation. Claudio reviewed via the dashboard and decided three of the four gate calls, holding the stack for deeper validation.

## Decision (2026-07-30)

1. **MVP scope APPROVED as drawn**: 15 features, ~25 person-months, 8 to 10 calendar months with founder plus two contractors, walking skeleton on TestFlight at month 3 to 4.
2. **Launch v1 entirely free.** The paywall ships in v1.x together with training-state-aware generation, once week-4 retention clears the bar. **Safety-aware routing stays free permanently**, which also resolves the safety-ethics question deferred at the Phase 4 gate.
3. **Apple Watch is a fast-follow at launch+30**, built during beta; v1 carries the Watch story via WorkoutKit sync to the native Workout app.
4. **The stack is NOT yet approved.** Claudio requires a rigorous second-opinion validation before committing: whether Supabase is truly the best database/backend choice, hosting options including other VPS providers, and proof that every layer is rock solid, scalable, and long-term viable for business growth. A dedicated validation study (`research/05-product/stack-validation.md`) compares alternatives layer by layer with real-world evidence; the stack decision reopens when it lands.

## Additional directives recorded at this gate

- **Everything publishes to Vercel.** All research artifacts and HTML documents must be accessible in the git-connected Vercel project (per DEC-007's protected-preview pipeline) so Claudio's partner always sees current material. GitHub to Vercel auto-deploy is the continuity mechanism.
- **The Graphify viewer must be genuinely usable.** The raw Graphify HTML was judged too bulky and hard to review. A purpose-built interactive explorer (`graph/index.html`) replaces it as the primary graph surface: search, topic-cluster filtering, node detail panels with rationale and connections, and neighbor highlighting, reading the live `graph.json` on every deploy.

## Consequences

- Build sequencing (walking skeleton, contractor hiring) can proceed on the approved scope; only stack-dependent commitments wait for the validation verdict.
- Phase 6 (business model) starts after the stack verdict, since unit economics depend on infrastructure cost conclusions.
- The landing page (`index.html`) now links the dashboard and the new graph explorer as live artifacts.

## Related

- [[_Decision-Log]]
- [[DEC-006 Concept lock route-first positioning]]
- [[DEC-007 Vercel publishing pipeline with protected previews]]
- `research/05-product/mvp-scope.md`, `research/05-product/stack-validation.md`
