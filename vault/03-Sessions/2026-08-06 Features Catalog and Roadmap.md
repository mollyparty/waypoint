---
type: session
created: 2026-08-06
updated: 2026-08-06
tags: [session, product, scope, roadmap, catalog, tooling, phase-5, phase-9]
---

# Session 2026-08-06 - Features Catalog and Roadmap

## Goal

Build one place that answers "what ships when, and for whom", detailed enough to discuss internally and dynamic enough to change your mind in. Every feature broken out and tied to a specific persona and need, filterable, with the release assignment adjustable so the consequences of moving something are visible immediately. Compliance and non-functional requirements included, because they are real work that the planning documents had been treating as a rounding line.

## The problem, stated precisely

Four documents defined features and they disagreed with each other.

`prd.md` marks the Apple Watch companion, all ten routing constraints, route explanations and the paid seam as P0. `mvp-scope.md` defers every one of those to v1.x. `team-roadmap.md` recuts v1 again to 12 to 15 person-months against Phase 9's part-time capacity. `rice-prioritization.md` ranks the same thirty features by a formula whose own summary warns it is not a release order. Nothing said which document won.

Worse, the arithmetic was not reversible. 22.75 person-months in `mvp-scope.md`, restated as 29 to 31 by DEC-010, then recut with an unmeasured 1.8x multiplier. Changing your mind about one feature meant recomputing three documents by hand, which is why nobody did — and which is how the four drifted apart in the first place.

None of the four authors was careless. Each was right when written, and the ground moved: the PRD assumed 2.5 to 3.0 full-time equivalents, DEC-010 changed the platform, Phase 9 discovered the team is three part-time founders. A fifth prose document would have gone stale by the same mechanism, which is why this is a data file with a calculator on top instead.

## What was built

`catalog/features.json`, 70 entries, canonical for release phase per [[DEC-020 Features catalog is the source of truth for release phase]]:

- **30 features** with capabilities breakout, acceptance criteria, persona and need and job linkage, RICE values verbatim, dependencies, integrations, pull-forward triggers, risks and source citations with line numbers.
- **15 compliance requirements**, locked into the MVP. Four are engineered by O-01 and carry zero effort with a `satisfiedBy` pointer so the privacy work is not double counted; C-14 points at TS-08 the same way.
- **19 non-functional requirements**, locked. Performance, offline, accessibility and the safety-claim language rules.
- **6 excluded items**, the DEC-006 NOT list, carried as zero-effort locked entries. Not in the plan, but a catalog that silently omits what was rejected invites someone to propose a social feed again in six months.

`catalog/index.html` is the working surface: filter by module, release, persona, need, job, effort, type or flag, plus free-text search; a detail drawer per entry; and a sticky bar that recomputes effort, calendar and projected iOS launch month against the 12-to-18-month competitive window on every change. Four presets seed it, with the recommended recut as the default. The AI leverage multiplier is a **slider from 1.0x to 2.5x** rather than a hardcoded 1.8x, because it is the riskiest number in the repository and the sensitivity should be felt rather than assumed. Dragging it to 1.0 moves launch from month 13 to month 23.

`catalog/build.py` validates referential integrity and regenerates `catalog/FEATURES.md` so agents reading without a browser get the same catalog.

## The findings

**One effort model reproduces four separately-published figures.** Capacity 7.5 person-months a year, a 1.20x React Native factor over the native estimates, 1.8x leverage, 1.5 months of pre-build offset. That produces the walking skeleton at 8.16 React Native person-months against a published 8 to 9; the compliance minimum at 2.52 against 2 to 3; launch hardening at 2.70 against 2 to 3; the recut v1 total at 13.38 against 12 to 15; and an iOS launch at month 13 against a published month 12 to 14. Four independent checks from one set of constants is the reason to trust the fifth number it produces.

**Full scope is more expensive than DEC-010 said.** This is the correction worth carrying. Priced individually the obligations need 4.35 native person-months, against the single ~2.0 "release overhead" line the planning documents carried — a gap of about 2.8 React Native person-months. Full approved scope is **32 to 33, not 29 to 31**. The recut is unaffected, because `team-roadmap.md` had already broken compliance and hardening out as separate lines. Making obligations visible is exactly what surfaced this; while they were a rounding line, nobody could see they were mispriced.

**The walking skeleton is a thin slice through eight features, not a subset of whole ones.** Adding up the whole features named in `mvp-scope.md` section 6 gives 14.0 native person-months against the 6 to 7 that document quotes. It is reduced versions: single-screen onboarding rather than the full flow, one candidate route rather than three, private-by-default storage rather than the privacy-zone interface. Each entry now carries a separate `skeletonEffort`, and those sum to 6.8. Anyone reading section 6 as a feature list over-estimates by 2x.

**The PRD's P0 list is close to four years of work.** 19 features plus the launch-gating obligations, 43.1 native person-months, month 47. Not a defect in the PRD, which was written against a team that no longer exists, but conclusive that its priority tiers cannot be read as a release plan.

**`team-roadmap.md`'s open question 4 is answered.** It flagged "public-launch hardening" as the least-specified line in the estimate. It is now 19 named requirements with individual effort figures.

## The four disagreements, resolved with reasons

Each gets a visible badge and a written recommendation in the drawer rather than a silent pick. In all four cases the catalog follows the later gate decision or decision record, because in every case the PRD's tier predates the thing that settled the question: the Apple Watch companion (GD-2), the ten-constraint set (evidence strength plus 6.0 person-months for the weakest needs), route explanations (split, with honest degradation at launch and the richer layer after), and the paid seam (GD-1 and then DEC-011, on the grounds that a paywall before proof contaminates the retention signal the MVP exists to produce).

## Two things the validator caught

Worth recording because both were silent.

**Reverse dependency edges had diverged.** Eleven `dependsOn` relationships had no matching `blocks` entry. Rather than patch the data, `build.py` now derives `blocks` from `dependsOn` and rewrites the file, so the class of error is gone rather than fixed once.

**The P0 preset was string-matching `prdPriority`.** That pulled in items marked P0 only by reference from a compliance or quality requirement, over-counting by roughly 4 person-months. Replaced with an explicit `prdP0` boolean plus a `prdP0Basis` note per entry recording whether membership is direct (named in section 4's P0 row) or as an enabler (a named P0 requirement cannot ship without it). False precision replaced with documented reasoning.

## Verification

`python catalog/build.py` clean: 70 entries, all persona, need, job, conflict and dependency IDs resolve, no entry depends on something scheduled later than itself, RICE ranks contiguous 1 to 30, no double-counted effort.

Browser-verified end to end: no console errors across the whole interaction; all four presets recompute correctly; the slider moves the launch month at both extremes; persona, search, type and flag filters all correct; reassignment updates the totals and the card's border colour; the detail drawer renders every section with no undefined, null or raw markup; the conflict callout appears on X-02; scenario state survives a reload and Reset restores the baseline; and the 390-wide mobile layout has no horizontal overflow, with cards stacking and filter controls wrapping.

## The post-commit hook clobbered the graph again

Worth writing down because the earlier fix looked sufficient and was not. The hook was scoped to code file extensions after a doc commit dropped curated nodes. This commit contained `catalog/build.py`, which is a generator rather than application code, and that was enough: the hook fired, rebuilt without an LLM pass, and cut the graph from 227 nodes to 216. Restored with `git checkout -- graphify-out/` since the curated version was already in the commit.

The filter now excludes `catalog/`, `scripts/` and `tools/` as well as matching on extension, verified three ways: repository tooling skips, application source still triggers, doc-only commits still skip. The general lesson is that "is this code" was the wrong question. The right one is "does the AST pass have anything useful to say about this," and for build scripts it does not. `.git/hooks/` is untracked, so none of this travels to another machine, and the session-end habit of checking `git status` for `graphify-out/` churn after every commit is the only thing that catches it.

## Two more defects found while merging the graph

Both were caught by cross-checking the generated markdown against the interactive page, which is worth doing every time because the two compute the same numbers independently.

**The PRD-P0 projection was month 47, not 48.** `build.py` rounded to one decimal and then to whole months, so 47.47 became 48, while the browser showed 47 from identical inputs. The generator now rounds once, half-up, matching JavaScript's `Math.round`, and the six places that had quoted 48 were corrected. Small number, but it had already propagated into a decision record, a knowledge note, the PRD annotation and a graph node label, which is how a rounding artifact becomes a fact nobody can trace.

**The graph explorer's legend showed the same name up to five times.** It took the first keyword rule that matched anywhere in a cluster, and because nearly every cluster mentions the MVP or the stack somewhere, five of fourteen clusters came out labeled "Product and MVP" with indistinguishable show/hide toggles. Rules are now scored by hit count, a `community_name` shared by every member wins outright, and any surviving collision is suffixed with the cluster's hub node. Verified: fourteen clusters, fourteen distinct names.

## Propagation

- Banner annotations on `mvp-scope.md`, `prd.md` and `rice-prioritization.md`. Their reasoning stays authoritative; only phase assignment moved. Each annotation also states what the catalog found about that specific document.
- A card on the root `index.html`, a Tools group in the dashboard navigation, and a paragraph inside Phase 9 gate card 1 pointing at the catalog as the instrument for settling it.
- DEC-020 recorded. DEC-014 through DEC-019 remain reserved for the still-open Phase 9 gate.
- Knowledge distillate: [[Features Catalog and Scope Arithmetic]].
- Graph merged by hand: 20 nodes and 46 edges covering the catalog files, the effort model and its multiplier, the three findings, the four resolved conflicts, and the compliance, non-functional and never-ship sets. Now 227 nodes and 542 edges across 15 communities, coverage measured at 104 of 104 corpus documents with zero dangling links and zero isolated nodes. `graphify query "what ships in the MVP and what is deferred"` returns the catalog and the upward correction in its first few nodes, which was the point. The stale `mvp-scope` node label asserting 29 to 31 person-months was rewritten to carry the correction, so the wrong figure cannot be read without the right one beside it. While measuring, the corpus figures in `GRAPH_REPORT.md` turned out to be stale and rule-less (94 documents, ~150,000 words); they are now 104 and 259,550 with the counting rule stated so the number is reproducible.

## What this unlocks

Phase 9 gate card 1 asks how to close the capacity gap. It can now be settled by direct comparison rather than argument: the recommended recut is loaded by default and the three alternatives are one click away, each with its launch month and its verdict against the competitive window. Nothing was pre-decided.

## Open threads

- **The six Phase 9 gate cards are still open**, including card 1. The catalog is the instrument, not the answer.
- **The 1.20x platform multiplier is a reconciliation, not a measurement.** It reproduces two published conversions, which is good evidence and not proof. The walking-skeleton build is the first chance to check it. #open-question
- **The AI leverage multiplier remains unmeasured**, and the whole recut rests on it. The month-6 checkpoint replaces it with evidence. Below 1.2x the plan gets rebuilt rather than adjusted. #risk
- **Exported scenarios are not committed automatically.** Scenario state lives in `localStorage` in one browser. If a scope decision is made in the catalog, the export has to be handed back and `features.json` updated, or the decision exists only in one person's browser. #risk
- **`catalog/build.py` is not wired into any hook.** Editing `features.json` without running it leaves `FEATURES.md` stale, and a stale generated mirror is exactly the drift this catalog was built to end.

## Next

1. Settle the Phase 9 gate, starting with card 1 in the catalog.
2. On card 1's outcome: write DEC-014, update `features.json` to match, regenerate, and tag v0.4.0 with its CHANGELOG entry.
3. Consider adding `python catalog/build.py --check` to a pre-commit hook, given the staleness risk above.

## Related

- [[DEC-020 Features catalog is the source of truth for release phase]]
- [[Features Catalog and Scope Arithmetic]]
- [[2026-08-06 Phase 9 Financial Strategy and Founding Team]]
- [[Session-Note]]
