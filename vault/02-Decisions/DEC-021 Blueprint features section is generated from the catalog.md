---
type: decision
id: DEC-021
status: accepted
created: 2026-08-30
updated: 2026-08-30
tags: [decision, product, scope, blueprint, tooling, phase-8, phase-9]
---

# DEC-021 Blueprint features section is generated from the catalog

## Context

[[DEC-020 Features catalog is the source of truth for release phase]] made `catalog/features.json` canonical for what ships when, and annotated the three research documents that used to answer that question. It missed one document: the blueprint.

Section 05 of `blueprint/index.html` was already a features section, and it was the weakest version of the feature story in the repository. It named 15 MVP features and tabled only 7 of them, dumped the remaining 8 into a prose run-on ("GPS tracking · run history · HealthKit sync · ..."), quoted 22.75 person-months plus "roughly 2 months of release overhead" — the exact rounded line the catalog had found under-counted 34 obligations by about 2.8 React Native person-months — and described the scope as "a solo founder's MVP" three weeks after Phase 9 established a team of three part-time founders.

That is the document investors read. The strongest version of the feature story lived at `catalog/` and the blueprint never mentioned it.

## Decision

Approved 2026-08-30:

1. **Blueprint section 05 is generated, not written.** `catalog/build.py` gained `render_blueprint_html()` and `render_blueprint_md()`, which replace everything between `<!-- CATALOG:START -->` and `<!-- CATALOG:END -->` markers in `blueprint/index.html` and `blueprint/blueprint.md`. Missing, duplicated or inverted markers raise rather than guessing where the block belongs.
2. **Generated at build time, never fetched at runtime.** The blueprint carries an `@media print` stylesheet and has no `fetch` call anywhere; a runtime fetch would leave a blank section in any PDF and break the self-contained property that makes the file sendable as one artifact.
3. **The blueprint gets a deliberately thinner view than `FEATURES.md`.** Four columns per feature: ID and name, the one-line purpose, the release badge, the personas served with primaries in bold. Grouped by the eight modules. Per-feature person-months and RICE ranks stay out, because they are internal planning detail and section 12 already owns the schedule.
4. **The two obligation-heavy modules collapse rather than tabling.** Trust and Privacy shows `O-01` and then one sentence covering the 15 compliance requirements as a count; Platform Quality has no user-facing features at all and becomes a single paragraph naming the 19 non-functional requirements by group. Tabling 34 obligations in an investor document is where all the bloat would have come from.
5. **The section states approved scope, not the recommendation.** The 15 features carry the "launch" badge because that is what `assigned` says. A warning callout immediately after states that those 15 plus their 34 obligations price at 32 to 33 person-months against 7.5 a year, that the standing recommendation is a thinner first cut through 8 of them, and that the choice is still open at the Phase 9 gate.
6. **The nav label changed from "The product" to "Product and features"** so the catalog is findable from the sidebar. `#s05` is referenced from exactly one place, so no renumbering was needed.

## Rationale

Hand-authoring a fifth copy of the feature story inside the blueprint would have reintroduced precisely the drift DEC-020 was created to end. The four source documents did not disagree through carelessness; they disagreed because each was written once and the ground moved. A blueprint section written once would have gone stale by the same mechanism, and this one already had.

Generation also makes the counts honest for free. Every number in the section — 30 features, 15 approved, 9 fast-follow, 6 ruled out, 15 compliance, 19 non-functional, 8 skeleton features — is computed from the JSON at build time rather than typed. The section subtitle deliberately carries no counts, so that the one hand-written line above the markers cannot drift either.

Reporting approved scope rather than the recut is the uncomfortable choice and the correct one. Badging the recommendation as "launch" would pre-empt a decision the founders have not made, and the gate card exists precisely so they make it.

## Alternatives considered

- **Adding a new section 18 for the catalog.** Rejected: section 05 was already the features section, and a second one would have left the stale version in place while burying the good one at the end.
- **Hand-writing a corrected section 05.** Rejected on the DEC-020 argument: correct on the day written, stale within a month, and it would have made the blueprint a fifth disagreeing document.
- **Fetching `features.json` at runtime, as `catalog/index.html` does.** Rejected: it breaks print and breaks the self-contained file. The interactive surface is the right place for live data; the blueprint is a document.
- **Embedding the full catalog detail — capabilities, acceptance criteria, dependencies, risks.** Rejected: that is roughly 2,500 lines of markdown in `FEATURES.md`, and the reason to put it in a filterable tool was that nobody reads it as a wall. The blueprint links to `/catalog/` for the depth.
- **Deleting the never-build card as redundant with section 16.** Rejected: the NOT list is load-bearing product definition, it is six short lines, and it is now sourced from the catalog's six `excluded` entries rather than retyped.

## Consequences

1. **Nobody should hand-edit between the markers.** The next `python catalog/build.py` overwrites it. Both markers say so, and `research/08-blueprint/_index.md` repeats it.
2. **`catalog/build.py` is now load-bearing for the investor document**, not just for an internal mirror. Its failure modes had to become loud, so the marker checks exit non-zero with the file named.
3. **Blueprint output is idempotent, `FEATURES.md` is not.** The blueprint block carries no timestamp, so a rebuild that changes nothing produces no diff in the document an investor reads. `FEATURES.md` keeps its `Version-Timestamp` and therefore always diffs.
4. **Five contradicting scope figures were corrected as part of the same change.** Four instances of "29 to 31 person-months" in each of `index.html` and `blueprint.md` now read 32 to 33, and the derived "21 to 28 months" full-scope projection is now 22 to 30, recomputed the same way it was originally derived (the 1.8x-to-2.5x leverage band applied to the corrected total).
5. **The DEC-010 row in the blueprint's decision log keeps its original ~29-31 figure** with a note that both its dates and its total are superseded. Rewriting the row would have falsified the record of what was decided.
6. **Phase 8's stale open item is closed.** The "~$350k to $400k pre-seed" open item in `research/08-blueprint/_index.md` was Phase 9's to answer and Phase 9 answered it: a $50k SAFE at a $1.5M cap. The decision itself remains an open gate card.

## Related

- `catalog/build.py` (`render_blueprint_html`, `render_blueprint_md`, `inject`)
- `blueprint/index.html`, `blueprint/blueprint.md` (section 05, between the markers)
- `research/08-blueprint/_index.md` (records that the section is generated)
- [[DEC-020 Features catalog is the source of truth for release phase]] (the authority this extends to the blueprint)
- [[DEC-010 Staged cross-platform MVP on React Native]] (the 29-to-31 figure this corrects in the blueprint text)
- [[DEC-006 Concept lock route-first positioning]] (the NOT list, now rendered from the catalog)
- [[_Decision-Log]]
