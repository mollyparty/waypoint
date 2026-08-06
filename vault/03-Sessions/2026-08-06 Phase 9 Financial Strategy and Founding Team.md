---
type: session
created: 2026-08-06
updated: 2026-08-06
tags: [session, phase-9, financial, equity, legal, memory-audit]
---

# Session 2026-08-06 - Phase 9: Financial Strategy and Founding Team

## Goal

Two things, in order. First, audit the vault and the graph and close every gap, because the financial work was about to build on them. Then produce the financial strategy and the internal team roadmap: overhead, burn, the three-way founder equity split, and the fundraising path, articulated internally and rewritten for investors.

## Part A: the memory audit

Three parallel audits (vault, graph, financial data inventory) found the structure sound and the content drifting. DEC-001 through DEC-013 complete and correctly logged, zero broken wikilinks, but real problems underneath.

**The contradiction worth naming.** [[Business Model and GTM Key Findings (Phase 6)]] asserted both that the Android date was the public launch and that DEC-013 overrode it to iOS, in the same document. An agent reading only the distillate, which is exactly what the retrieval order tells agents to do, could act on the wrong one. The graph carried the same error in the `phase6_gtm` node label. Both now state the recommendation and its override.

**Eleven documents had no graph node at all**, meaning they were invisible to every query: five competitor profiles, DEC-007, four session notes, and the Phase 6 distillate. Coverage is now 86 of 86 with zero dangling links and zero isolated nodes. Also dropped six Obsidian settings nodes extracted by the AST pass from `vault/.obsidian/app.json`, which were configuration noise, and corrected three node labels still asserting "gate pending" or "not started" for work finished weeks ago.

**Phases 7 and 8 were recorded inside the Phase 6 session note**, where nothing finds them, since agents locate the newest session by filename. Split into [[2026-08-06 Phase 7 Dashboard Closed and Phase 8 Blueprint Drafted]].

Also: START-HERE and 00-PROGRESS synced to actual state, resolved open questions closed in the Phase 3 and 4 distillates, DEC-007 given the alternatives section its template requires, the architecture index rewritten to point at the stack decisions instead of calling them future work, and the Vercel session note retrofitted to the template.

**Fixed the graphify post-commit hook**, which had been quietly clobbering curated work for weeks. The hook's rebuild has no LLM pass, so on a markdown-only tree it extracts headings as nodes and drops hand-written ones; the Part A commit lost 9 nodes and 19 links to it before being restored. It is now scoped to code file extensions. AGENTS.md session-end step 3 already warned about this. **The hook lives in `.git/hooks/`, which is not tracked**, so this fix does not travel to another machine or another collaborator; anyone cloning fresh will need to reapply it or watch for the same clobbering.

## Part B: what changed, and why it invalidated eight phases of arithmetic

The founding team was defined for the first time this session. Three partners, none full-time, two in 10th grade, building AI-assisted rather than hiring. Every financial figure in the repo had been resting on one sentence in [[Charter]]: *"Solo founder building from scratch."*

Three numbers died immediately. The **$230,000 cash build** was the price of contractor person-months nobody is buying. The **$15,000/month operating base** was a founder draw plus a contractor retainer nobody is drawing. The **$350,000 to $400,000 pre-seed** in the blueprint was simply their sum, and it was already labeled derived rather than decided, which is the only reason this was recoverable rather than embarrassing.

Five deliverables in `research/09-financial-team/`. Written in dependency order, with `legal-formation.md` first because the equity and fundraising documents both rest on the custodial and IP mechanics it settles.

## The finding that governs the phase

**The binding constraint is no longer money. It is calendar time, and there is not enough of it.**

Burn falls roughly 97 percent, to about $400 a month. That reads as unambiguously good news and it is not. The constraint moved rather than disappeared: the scarce input is founder hours, which cannot be bought at any price. And there is no longer a financial forcing function, because at $400 a month nothing ever runs out and nothing ever forces a decision.

29 to 31 person-months of approved scope against roughly 7.5 person-months a year of capacity is 21 to 28 months even at a generous AI multiplier, against a 12 to 18 month window. The recommendation is to make the walking skeleton the product rather than a milestone, which lands iOS at month 12 to 14 and supersedes DEC-010's dates.

## The two things worth remembering beyond the numbers

**Break-even is ~235 paying subscribers, not ~3,000.** An order of magnitude, and it means Waypoint can plausibly become self-sustaining without institutional money at all. That should be decided explicitly rather than by default, because a profitable independent business and a venture outcome are different games and the choice changes what to build and how fast. It also fits the honest reading of H5, which came back uncertain.

**An IP assignment signed by a minor is voidable at their election, and the two minors are the two the concept came from.** This is not a footnote; it is the company's title to its own technology. Cure is guardian co-signature now plus re-execution within 30 days of each 18th birthday, both tracked as dated diligence items.

## Decisions made

None yet. Six gate cards are live on the dashboard awaiting founder decisions, which will become DEC-014 onward. One of them supersedes DEC-010's timeline.

## Open threads

- **The 1.8x AI leverage multiplier is the riskiest number in the repo** and has never been measured. The month-6 checkpoint exists to replace it with evidence, with pre-committed actions per outcome band. #risk
- **`unit-economics.md` is still priced against a $7.99/month mid case** that DEC-011 replaced with $99.99/year. Corrections all run in Waypoint's favor, so nothing is hidden, but the published tables understate the business and a full re-run is queued rather than done. #open
- **Venture scale or profitable independence?** Open question 4 in `fundraising-plan.md`, and the answer changes strategy rather than presentation. #open-question
- Daniel's other business has unknown seasonality, which could collide with the only engineering capacity there is. #open-question
- The graphify hook fix is local-only because `.git/hooks/` is untracked. #open
- Blueprint approval and the v0.4.0 tag both wait on the Phase 9 gate.

## Next steps for the next agent (any tool)

1. **Answer the six Phase 9 gate cards** on `dashboard/index.html`, then record DEC-014 onward, including the one superseding DEC-010's dates.
2. Founder review of the rewritten blueprint, then tag v0.4.0.
3. Then the build begins: formation first, and the month-1 A3 safety-data spike, which is a go-to-market gate rather than only a technical one.

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] `research/00-PROGRESS.md` current and agreeing with START-HERE
- [x] Graph updated (curated merge, coverage verified at 86 of 86)
- [x] Committed and pushed
