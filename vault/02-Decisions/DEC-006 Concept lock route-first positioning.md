---
type: decision
id: DEC-006
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, concept, positioning, phase-4]
---

# DEC-006 Concept lock: route-first positioning

## Context

Phases 1 to 3 of the research program completed with strong results: H2 and H3 supported (the constraint-based route generation whitespace is real and the route wedge beats another plan product), H1 partially supported with a reframe (travel friction is frequent but usually worked around; safety-aware routing and home route novelty carry the daily retention evidence), H6 supported (HealthKit-first iOS is both forced and correct), H5 uncertain (the wedge alone is a $5M to $30M ARR business; venture scale needs the expansion story). Strava's Instant Workouts (January 2026) already links basic heatmap routes to workouts, so the 12 to 18 month window is consuming from now. Claudio reviewed via the new HTML dashboard and decided at the Phase 4 gate.

## Decision (all four gate calls, decided 2026-07-30)

1. **The concept is LOCKED** as written in `research/04-synthesis/concept.md` sections 1 to 7: constraint-based adaptive route generation as the hero and free-tier anchor; the adaptive coaching layer (training-state-aware routes, adaptive routines, explainable coach) as the paid tier; voice-guided navigation as the execution surface; privacy zones and private-by-default as day-one architecture. Explicitly not: social network, route library, multi-sport, hardware, plan-quality brand war.
2. **Positioning: route-first (Candidate A)**: "For committed amateur runners who never quite know where today's run should go, Waypoint is the running app that generates the right route for you, right now, from wherever you stand."
3. **Tagline: "Know where to run"**, retiring "Your AI Running Coach" (which priced Waypoint against free Garmin/Apple coaching and branded it against Runna).
4. **H1 reframe accepted**: travel is the activation moment and demo story; safety plus home novelty are the daily retention wedge.

## Rationale

- Route-first claims the entire empty quadrant from the Phase 2 positioning map and contains the other candidates: safety survives as the hero constraint and Elena message, coaching survives as the paid-tier centerpiece.
- The tagline change follows the category strategy: position inside the running app market as "the running app that knows where you should run" rather than the commoditizing "AI running coach" label or an expensive new-category campaign.
- The reframe follows the evidence: retention needs daily-frequency jobs, and the desk evidence puts safety and novelty at 3 to 5 times per week versus episodic travel.

## Alternatives considered

- Safety-first positioning: strongest single evidence base, rejected as the lead because it narrows the audience and elevates claim-liability risk; retained as the hero constraint inside route-first.
- Coach-first positioning: rejected; prices against free platform coaching and brands against Runna.
- Keeping travel as the headline wedge: rejected; it leads with the weaker retention evidence, though it remains the demo story and activation moment.

## Consequences

- Phase 5 (PRD, MVP scope) proceeds against the locked concept; changes now require a new decision record.
- README, Charter, and vault notes update to the new tagline and positioning.
- The safety-free-tier question (must safety-critical routing be free) is explicitly deferred to Phase 6 pricing.
- The real-user interview backlog (`research/03-users/unmet-needs.md`) runs alongside Phase 5; results can recalibrate tiers and messaging without unlocking the concept.

## Related

- [[_Decision-Log]]
- [[Founder-Brief]]
- [[DEC-005 Phased research program with gated approvals]]
- `research/04-synthesis/concept.md` (the locked document)
