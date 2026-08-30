---
type: session
created: 2026-08-30
updated: 2026-08-30
tags: [session, product, scope, blueprint, catalog, tooling, phase-8, phase-9]
---

# Session 2026-08-30 - Features Catalog Inside the Blueprint

## Goal

Put the features catalog inside the business blueprint as a section rather than leaving it as a side tool, condensed to essentials so the investor document gains a clear picture of what the platform does without gaining 2,500 lines of planning detail.

## The problem, stated precisely

Section 05 of `blueprint/index.html` was already a features section. It was also the weakest version of the feature story in the repository, and it was the version investors read.

It named 15 MVP features and tabled 7 of them, dumping the other 8 into a prose run-on: "GPS tracking · run history · HealthKit sync · onboarding · audio cues · route save and re-run · Strava share · privacy, consent and AI disclosure." It quoted "22.75 person-months plus roughly 2 months of release overhead" — the exact rounded line [[DEC-020 Features catalog is the source of truth for release phase]] had found under-counted 34 obligations by about 2.8 React Native person-months. It said "~17 person-months" for fast-follow. And it described the scope as "a solo founder's MVP" three weeks after Phase 9 established a team of three part-time founders.

Meanwhile the good version lived at `catalog/` and the blueprint never mentioned it. DEC-020 had annotated the three research documents that used to answer "what ships when" and missed the fourth: the document that actually gets sent to people.

## The approach: generate it

Hand-writing a corrected section 05 would have been correct on the day it was written and stale within a month, by exactly the mechanism DEC-020 exists to stop. So `catalog/build.py` gained `render_blueprint_html()` and `render_blueprint_md()`, which replace everything between `<!-- CATALOG:START -->` and `<!-- CATALOG:END -->` and leave the rest of each file untouched. Recorded as [[DEC-021 Blueprint features section is generated from the catalog]].

Generated at build time, not fetched at runtime. The blueprint has no `fetch` anywhere and carries an `@media print` stylesheet; a runtime fetch would leave a blank section in any PDF and break the self-contained property that makes the file sendable as one artifact. `catalog/index.html` is where live data belongs.

## What the section contains

Grouped by the eight modules, four columns per feature: ID and name, the one-line purpose, the release badge, the personas served with primaries in bold. Thirty rows total. A four-card stats strip above it with every count computed at build time. Then a warning callout, the never-build table, and one closing pointer to `/catalog/`.

Deliberately left out: per-feature person-months and RICE ranks (internal planning detail, and section 12 owns the schedule), and capabilities, acceptance criteria, dependencies, risks and open questions (that is what the filterable tool is for).

Two modules collapse rather than tabling, which is where the bloat would have come from. Trust and Privacy shows `O-01` and then one sentence covering the 15 compliance requirements as a count. Platform Quality has no user-facing features at all — it is 19 non-functional requirements — so it becomes a single paragraph naming them by group.

Kept from the old section because it is good and short: the positioning pull quote, the "Know where to run" tagline callout, and the five non-negotiable design rules. All three sit outside the markers. The never-build card was kept too, but is now rendered from the catalog's six `excluded` entries rather than retyped prose.

Nothing new entered the stylesheet. The section reuses `.stats`, `.stat`, `.tw`, `.badge b-green|b-amber|b-gray`, `.callout warn` and `.kbd` verbatim, so the `max-width` and print rules keep working.

## The honesty problem, and how it was handled

The 15 features carry a green "launch" badge because that is what `assigned` says in the catalog. But the standing Phase 9 recommendation is to launch a thinner first cut through eight of them, and that decision is still an open gate card.

Badging the recommendation as "launch" would have pre-empted a decision the founders have not made. Badging approved scope without saying anything would have implied 15 features ship in one go. So the section reports approved scope and follows it immediately with a warning callout: those 15 plus their 34 obligations price at 32 to 33 person-months against 7.5 a year, the recommendation is reduced versions of 8 of them wrapped in the compliance minimum, section 12 has the dates, and the choice is open at the gate.

One imprecision was caught while writing that callout and fixed in the generator: the first draft said "those 15 features come to 32 to 33 person-months", which is wrong. The 32.52 figure is the 15 features *plus* the 34 obligations. Exactly the class of slippage the catalog was built to eliminate, appearing in the text describing the catalog.

## Consistency pass

Once the section states full scope honestly, the rest of the blueprint contradicted it. Fixed as part of the same change rather than deferred:

- Four instances of "29 to 31 person-months" in `index.html` and four in `blueprint.md` now read 32 to 33, with the reason stated once at the section 12 occurrence.
- The derived "21 to 28 months" full-scope projection is now **22 to 30**. Worth recording the derivation: the original range turns out to be the 2.5x-to-1.8x leverage band applied to ~29.7 React Native person-months, which reproduces 20.5 and 27.9. The same band on 32.52 gives 22.3 and 30.4. So the new range was recomputed the way the old one was derived rather than guessed.
- The DEC-010 row in the blueprint's decision log **keeps** its original ~29-31 figure, with a note that both its dates and its total are superseded. Rewriting the row would have falsified the record of what was decided.
- "A solo founder's MVP" is gone; the generated text says "a part-time team's v1". No `solo founder` string remains anywhere in `blueprint/`.
- Section 05's heading is now "The product and its features" and the nav label "Product and features", so the catalog is findable from the sidebar. `#s05` was referenced from exactly one place, so no renumbering.
- `research/08-blueprint/_index.md`: the "~$350k to $400k pre-seed" open item is closed, since Phase 9 replaced it with a $50k SAFE at a $1.5M cap. The file also now records that section 05 is generated, so nobody hand-edits inside the markers and wonders why their change vanished.

## Verification

`python catalog/build.py` clean, and the second run reports `unchanged` for both blueprint files. That matters: the blueprint block deliberately carries no timestamp, so a rebuild that changes nothing produces no diff in the document an investor reads. `FEATURES.md` keeps its `Version-Timestamp` and therefore always diffs, which is the right trade for a mirror and the wrong one for a document.

Marker failure modes tested explicitly rather than assumed, since `build.py` is now load-bearing for the investor document: a missing `CATALOG:END`, a duplicated `CATALOG:START`, and an inverted pair each exit non-zero with the file named and nothing written.

Browser-verified: console clean; all 17 nav anchors resolve to elements that exist; the 05 nav link reads "Product and features" and takes the `active` class on scrollspy; the stats strip renders as four cards and the tables as four columns with distinct green, amber and grey badges; no literal `&mdash;` or `&amp;` anywhere in the rendered text; no table clipped or overflowing its container. At 390px wide `scrollWidth` equals `clientWidth` at 390, so the tables scroll inside their own wrappers without dragging the page sideways, and the Contents toggle opens and closes. Under print emulation the stats cards, table headers, badges and warning callout all keep readable contrast.

## Propagation

- DEC-021 recorded and logged. DEC-014 through DEC-019 remain reserved for the still-open Phase 9 gate.
- `research/08-blueprint/_index.md` gains a generator row in its deliverables table and the note that section 05 is generated.
- CHANGELOG entry under Unreleased, still targeting v0.4.0.
- Graph merge, START-HERE and `research/00-PROGRESS.md` updated together.

## Open threads

- **The six Phase 9 gate cards are still open**, including card 1. The blueprint now states the gap rather than resolving it, which is correct but means an investor reading section 05 sees an open question. That is deliberate and should stay that way only until the gate is settled.
- **`catalog/build.py` is still not wired into any hook.** The risk grew with this change: editing `features.json` without running the build now leaves the *investor document* stale, not just an internal mirror. #risk
- **Section 05's subtitle and the design rules are hand-written** and sit outside the markers. The subtitle deliberately carries no counts so it cannot drift, but the design-rules list mentions "six binding language rules", which is currently true (NF-L1 to NF-L6) and would silently go stale if a seventh were added. #open-question
- **`blueprint/blueprint.md` and `blueprint/index.html` are still maintained as two hand-written documents outside the markers.** Section 05 is now generated in both, but the other sixteen sections are duplicated prose that can drift. #risk

## Next

1. Settle the Phase 9 gate, starting with card 1 in `catalog/index.html`.
2. On card 1's outcome: write DEC-014, update `features.json`, run `python catalog/build.py` (which now updates the blueprint too), then tag v0.4.0 with its CHANGELOG entry.
3. Consider `python catalog/build.py --check` in a pre-commit hook, given the staleness risk above.

## Related

- [[DEC-021 Blueprint features section is generated from the catalog]]
- [[DEC-020 Features catalog is the source of truth for release phase]]
- [[Features Catalog and Scope Arithmetic]]
- [[2026-08-06 Features Catalog and Roadmap]]
- [[Session-Note]]
