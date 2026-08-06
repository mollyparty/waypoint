---
type: decision
id: DEC-020
status: accepted
created: 2026-08-06
updated: 2026-08-06
tags: [decision, product, scope, roadmap, tooling, phase-5, phase-9]
---

# DEC-020 Features catalog is the source of truth for release phase

## Context

Feature definitions were spread across four documents that disagreed with each other, and nothing said which one won.

`research/05-product/prd.md` marks the Apple Watch companion, all ten routing constraints, route explanations and the paid seam as P0. `research/05-product/mvp-scope.md` defers every one of those to v1.x. `research/09-financial-team/team-roadmap.md` then recuts v1 again to 12 to 15 person-months against the part-time capacity Phase 9 established. `research/05-product/rice-prioritization.md` ranks the same thirty features by a formula whose own summary warns it is not a release order.

The effort arithmetic was also not reversible. `mvp-scope.md` totals 22.75 person-months in iOS-native terms, [[DEC-010 Staged cross-platform MVP on React Native]] restates the same scope as 29 to 31 in React Native, and the recut applies an unmeasured 1.8x AI leverage multiplier on top. Changing your mind about one feature meant recomputing three documents by hand, which is why nobody did, and which is how the four came to disagree in the first place.

DEC-020 was numbered after the block reserved for the still-open Phase 9 gate (DEC-014 through DEC-019).

## Decision

Approved 2026-08-06:

1. **`catalog/features.json` is the single source of truth for release phase assignment.** Seventy entries: 30 features, 15 compliance requirements, 19 non-functional requirements, and the 6 items DEC-006 ruled out. Each carries its full detail, its persona, need and job linkage, its RICE values, its dependencies, and what each source document says about it.
2. **The source documents keep their analysis and lose their phase columns.** `mvp-scope.md`, `prd.md` and `rice-prioritization.md` carry banner annotations pointing here. Their reasoning, gate decisions, RICE scores and requirement specifications remain authoritative; only the answer to "what ships when" moved.
3. **`catalog/index.html` is the working surface.** Filter by module, release, persona, need, job, effort, type or flag; move anything between MVP, v1.x, v2 and cut; and read the recomputed effort, calendar and projected iOS launch month against the 12-to-18-month competitive window. The AI leverage multiplier is a slider from 1.0x to 2.5x rather than a hardcoded 1.8x.
4. **`catalog/FEATURES.md` is a generated mirror**, produced by `catalog/build.py`, which also validates referential integrity. Never edited by hand.
5. **Compliance and non-functional entries are locked into the MVP** and cannot be toggled out, but their effort stays in every total. The DEC-006 NOT list entries are locked out and carry zero effort.

## Rationale

The four documents did not disagree because anyone was careless. They disagree because each was correct when written and the ground moved underneath them: the PRD assumed 2.5 to 3.0 full-time equivalents, DEC-010 changed the platform, and Phase 9 discovered the team is three part-time founders. A fifth prose document restating the answer would have been correct on the day it was written and stale by the same mechanism.

What breaks the cycle is making the arithmetic reversible. If moving one feature recomputes the launch date in front of you, the scope conversation can be had by direct comparison instead of by argument, and the documents cannot drift apart again because there is only one place the answer lives.

Exposing the AI multiplier as a slider rather than a constant is deliberate. It is the riskiest number in the repository, it has never been measured on this team, and the whole recut rests on it. A number that load-bearing should be felt rather than assumed.

## Alternatives considered

- **A fifth markdown document declaring the canonical answer.** Rejected: it would have inherited exactly the drift problem it was meant to solve, and it could not make the arithmetic reversible.
- **Amending the three source documents in place.** Rejected: it would destroy the record of what was believed when, and the disagreements are themselves informative. Annotation preserves both.
- **Leaving the PRD's P0 tiers as the release plan.** Rejected on arithmetic: priced at real capacity, the P0 list projects to month 47.
- **Excluding compliance and non-functional work, as the planning documents effectively did.** Rejected: their absence is precisely what made the totals wrong, and the point of a catalog is that nothing load-bearing is invisible.

## Consequences

1. **Full approved scope is more expensive than DEC-010 said.** Pricing the obligations individually gives 4.35 native person-months against the single ~2.0 "release overhead" line the planning documents carried. Full scope is therefore roughly **32 to 33 React Native person-months, not 29 to 31**. The recut v1 is unaffected, because `team-roadmap.md` already priced compliance and hardening as separate line items.
2. **The recut is validated independently.** The catalog's model reproduces the walking skeleton at 8.16 React Native person-months (published: 8 to 9), the compliance minimum at 2.52 (published: 2 to 3), launch hardening at 2.70 (published: 2 to 3), v1 total at 13.38 (published: 12 to 15), and an iOS launch at month 13 (published: month 12 to 14). Four published figures reproduce from one model, which is the check that the model is not inventing numbers.
3. **Open question 4 in `team-roadmap.md` is answered.** "Public-launch hardening" was flagged there as the least-specified line in the estimate. It is now 19 named non-functional requirements with individual effort figures.
4. **The four documented disagreements each get a written recommendation** rather than a silent pick, and each recommendation follows the later gate decision or decision record rather than the earlier document. Resolving them is now a toggle.
5. **Phase 9 gate card 1 has an instrument.** Rather than pre-deciding the capacity gap, the recommended recut loads as the default preset and the three alternatives are one click away. #open-question
6. **First use of `localStorage` in the repository.** Scenario state is client-only and never reaches the repository, which is why an Export button exists to hand a decision back for committing.
7. **`catalog/build.py` must run after every edit to `features.json`.** It validates and regenerates; it also derives the reverse dependency edges, since maintaining them by hand had already let them diverge.

## Related

- `catalog/features.json`, `catalog/index.html`, `catalog/FEATURES.md`, `catalog/build.py`
- `research/05-product/mvp-scope.md`, `prd.md`, `rice-prioritization.md` (all three annotated by this decision)
- `research/09-financial-team/team-roadmap.md` (the recut this catalog defaults to and validates)
- [[DEC-010 Staged cross-platform MVP on React Native]] (the platform multiplier's origin; its 29-to-31 figure is refined here)
- [[DEC-006 Concept lock route-first positioning]] (the NOT list, carried as locked entries)
- [[DEC-011 Pricing and the permanent free tier]] (why the paid seam cannot precede the paywall)
- [[_Decision-Log]]
