---
type: knowledge
created: 2026-08-06
updated: 2026-08-06
source: "catalog/features.json; research/05-product/{mvp-scope,prd,rice-prioritization}.md; research/09-financial-team/team-roadmap.md"
tags: [knowledge, product, scope, roadmap, effort-model, phase-5, phase-9]
---

# Features Catalog and Scope Arithmetic

## Summary

Release phase for every feature, compliance requirement and quality obligation is canonical in `catalog/features.json` (70 entries) as of [[DEC-020 Features catalog is the source of truth for release phase]], with the interactive surface at `catalog/index.html` and a generated markdown mirror at `catalog/FEATURES.md`. The catalog carries an effort model that reproduces four separately-published figures from one set of constants, and in doing so it corrected the full-scope total from 29-to-31 up to roughly 32-to-33 React Native person-months. The recut v1 recommendation from Phase 9 is unaffected and is the default preset.

## The effort model in one place

Four constants, and every projection follows from them:

| Constant | Value | Where it comes from |
|---|---|---|
| Capacity | 7.5 person-months/year | `team-roadmap.md` line 83: three part-time founders, ~1,200 hours a year |
| Platform multiplier | 1.20x | Converts the iOS-native RICE estimates to React Native under [[DEC-010 Staged cross-platform MVP on React Native]] |
| AI leverage multiplier | 1.8x default, 1.0 to 2.5 range | Unmeasured. Exposed as a slider, not a constant |
| Pre-launch offset | 1.5 months | Formation, store accounts and the month-1 spike run before build capacity flows |

`calendarMonths = (nativeEffort x 1.20 / aiMultiplier) / 7.5 x 12 + 1.5`

**Why 1.20 is defensible rather than convenient.** It reproduces two independently published conversions. DEC-010 restated the 15-feature scope from 22.75 native to 29-to-31 React Native: 22.75 plus 2.0 overhead, times 1.20, is 29.7. Separately, `team-roadmap.md` scaled the 6-to-7 native walking skeleton to 8-to-9: 6.8 times 1.20 is 8.16. One factor, two documents, both land in band.

## What the model reproduces, and what it corrects

| Scenario | Native pm | React Native pm | Projected iOS launch | Published figure |
|---|---:|---:|---:|---|
| Walking skeleton only | 6.80 | 8.16 | month 9 | 8 to 9 pm ✓ |
| **Recut v1 (recommended)** | 11.15 | 13.38 | **month 13** | 12 to 15 pm, month 12 to 14 ✓ |
| Full MVP v1 (15 features) | 27.10 | 32.52 | month 30 | 29 to 31 pm — **corrected upward** |
| PRD P0 list | 43.10 | 51.72 | month 47 | never costed before |

Component checks inside the recut: compliance minimum 2.52 React Native person-months against a published 2 to 3, and launch hardening 2.70 against a published 2 to 3. Both in band.

## Three findings worth carrying forward

1. **The ~2.0 person-month "release overhead" line under-counted the obligations.** Priced individually, the 15 compliance requirements need about 2.1 native person-months beyond what O-01 already engineers, and the 19 non-functional requirements another 2.25. That is 4.35 native, or 5.22 React Native, against a 2.4 React Native placeholder — a gap of roughly 2.8. Full approved scope is therefore **32 to 33 React Native person-months, not 29 to 31**. The recut is unaffected because `team-roadmap.md` had already broken compliance and hardening out as separate lines.

2. **The walking skeleton is a thin slice through eight features, not a subset of whole features.** Adding up the whole features named in `mvp-scope.md` section 6 gives 14.0 native person-months, twice the 6-to-7 that document quotes. The skeleton is reduced versions: single-screen onboarding rather than the full flow, one candidate route rather than three, private-by-default storage rather than the privacy-zone interface. The catalog therefore records a separate `skeletonEffort` per feature, and those sum to 6.8, which is what makes the published estimate correct. Anyone reading section 6 as a feature list will over-estimate by 2x.

3. **The PRD's P0 tier is close to four years of work at this capacity.** The 19 features it marks launch-critical, plus the obligations it also marks launch-gating, come to 43.1 native person-months and project to month 47 against a 12-to-18-month window. This is not a defect in the PRD: it was written against an assumed 2.5-to-3.0 full-time-equivalent team. It does mean the priority tiers cannot be read as a release plan.

## The four documented disagreements

Each carries a written recommendation in the catalog rather than a silent pick. In all four the catalog follows the later gate decision or decision record, because in every case the PRD's tier predates the thing that settled the question.

| ID | Question | PRD says | mvp-scope says | Catalog recommends |
|---|---|---|---|---|
| CF-1 | Apple Watch companion | P0 | v1.x | v1.x, per GD-2; the 4.0 pm and watchOS risk do not change what the MVP proves |
| CF-2 | All ten routing constraints | engine P0 | surface, crossings, weather are v1.x | Subset; the deferred three cost 6.0 pm for the least-evidenced needs |
| CF-3 | Route explanations | AC3-F1 at P0 | P-03 is v1.x | Split: honest degradation (H-09, 0.25 pm) at launch, richer layer (P-03, 2.0 pm) after |
| CF-4 | Paid seam at launch | AC-1 P0 | free launch by GD-1 | Free launch, per GD-1 and [[DEC-011 Pricing and the permanent free tier]]; a paywall before proof contaminates the retention signal |

## Structure of the catalog

70 entries across 8 modules: Route Generation, Run Execution, Tracking and Data, Coaching Layer, Trust and Privacy, Distribution and Commerce, Onboarding and Activation, Platform Quality.

- **30 features** (H-01 to H-10, X-01 to X-03, TS-01 to TS-10, P-01 to P-06, O-01), each with capabilities breakout, acceptance criteria, persona and need and job linkage, RICE values, dependencies, integrations, pull-forward trigger, risks and source citations.
- **15 compliance requirements** (C-1 to C-15), locked into the MVP. Four of them (C-1, C-2, C-3, C-11) are engineered by O-01 and carry zero effort with a `satisfiedBy` pointer, so the privacy work is not double counted; C-14 points at TS-08 the same way.
- **19 non-functional requirements** (NF-P1 to P4, NF-O1 to O3, NF-A1 to A6, NF-L1 to L6), locked. These answer `team-roadmap.md`'s open question 4, which flagged "public-launch hardening" as the least-specified line in the estimate.
- **6 excluded items** (N-01 to N-06), the [[DEC-006 Concept lock route-first positioning]] NOT list, carried as locked zero-effort entries so nobody re-proposes a social feed in six months.

## Operating notes

- `python catalog/build.py` validates and regenerates the markdown mirror. Run it after every edit to `features.json`. It checks referential integrity across personas, needs, jobs, dependencies and conflicts; that no entry depends on something scheduled later than itself; that RICE ranks are contiguous; and that no entry with a `satisfiedBy` pointer also carries effort.
- Reverse dependency edges (`blocks`) are **derived** from `dependsOn` by the build script. Hand-maintaining both let them diverge, which the validator caught on its first run.
- Scenario state in the browser lives in `localStorage` only, the first use of it in this repository. It never reaches the repository, which is why the Export button emits JSON plus a markdown diff to hand back for committing.
- The generated markdown and `catalog/index.html` compute the same projections independently, so comparing them is a free consistency check and is worth doing after any change to the model. It has already caught one defect: `build.py` rounded the launch month twice and printed the PRD-P0 case as month 48 where the browser correctly showed 47.
- The catalog is represented in the knowledge graph (community "Features Catalog and Scope Arithmetic", 20 nodes), so a query about what ships when reaches it without a repository read. The `mvp-scope` node label carries the upward correction inline, so the superseded 29-to-31 figure cannot be read without it.

## Sources

- `catalog/features.json` and `catalog/FEATURES.md` (this project)
- `research/05-product/rice-prioritization.md` (the thirty scores, verbatim)
- `research/05-product/mvp-scope.md` (the MVP line, walking skeleton, gate decisions GD-1 to GD-4)
- `research/05-product/prd.md` (requirement IDs, the 15-item compliance checklist, the non-functional set)
- `research/09-financial-team/team-roadmap.md` (capacity, the recut, the multiplier sensitivity table)

## Related

- [[DEC-020 Features catalog is the source of truth for release phase]]
- [[Financial Strategy and Founding Team (Phase 9)]]
- [[Product Definition Key Findings (Phase 5)]]
- [[_Knowledge-Index]]
