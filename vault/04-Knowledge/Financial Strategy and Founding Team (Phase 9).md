---
type: knowledge
created: 2026-08-06
updated: 2026-08-06
tags: [knowledge, research, financial, burn, equity, fundraising, team, legal, phase-9]
---

# Financial Strategy and Founding Team (Phase 9)

Distilled from `research/09-financial-team/` (5 documents: legal-formation, operating-model, team-roadmap, capital-structure, fundraising-plan). **Gate OPEN as of 2026-08-06** with six decisions pending. This phase was not in the original program; [[DEC-005 Phased research program with gated approvals]] ended at Phase 8.

## Why the phase exists

Every financial figure in this project rested on one sentence in [[Charter]]: *"Solo founder building from scratch."* It was wrong. The real team is **three partners, none full-time, two in 10th grade, building AI-assisted rather than hiring**.

Three figures collapsed as a direct consequence, and they should not be quoted again from their original sources:

| Figure | Source | Why it died |
|---|---|---|
| ~$230,000 cash build | `unit-economics.md` 1.5 | The price of contractor person-months nobody is buying |
| ~$15,000/month operating base | `unit-economics.md` 1.4 | A founder draw plus a contractor retainer nobody is drawing |
| ~$350,000 to $400,000 pre-seed | `blueprint.md` section 13 | Just the sum of the other two |

## The finding that governs everything else

**The binding constraint is no longer money. It is calendar time, and there is not enough of it.**

Burn falls roughly 97 percent, from ~$15,000/month to ~$400. That sounds like unambiguously good news and is not, for two reasons. The constraint moved rather than disappeared: the scarce input is now founder hours, which cannot be bought at any price. And **there is no longer a financial forcing function** — at $400 a month nothing ever runs out, so nothing ever forces a decision.

The arithmetic: 29 to 31 person-months of approved scope against roughly **7.5 person-months a year** of real capacity, which even at a generous AI multiplier is 21 to 28 months, against a **12 to 18 month** competitive window. It does not fit. The response is to cut scope, not to work harder or raise more.

## The numbers worth remembering

- **Burn: ~$260/month pre-formation, ~$400 during build, ~$1,050 post-launch.** AI tooling at $160 (Cursor Pro+ $60 plus Claude Max 5x $100) plus a $50 overage allowance is the largest controllable line, and it is the engineering budget, not overhead.
- **Cash to public launch: ~$27,000 to $47,000.** Three-year cash all the way to break-even: **~$40,000 to $53,000**.
- **Break-even: ~235 paying subscribers**, not the ~3,000 the research asserted. Against a base case of 480 by month 12 of revenue. Caveats: counts no founder compensation, and holds only while the team stays unpaid.
- **The largest single expense is legal, not engineering.** The $8,000 to $20,000 privacy and compliance package exceeds everything else combined once salaries are removed, and it is the strongest argument for raising something rather than nothing.
- **The ask: $50,000 on a post-money SAFE at a $1.5M cap**, roughly 3.3 percent.

## The AI leverage assumption, which is the weakest link

The claim that one part-time builder delivers work scoped for 2.5 to 3.0 engineers is **the least validated number in the entire repo**. AI assistance is strong on conventional surface (auth, settings, history, forms, store integration, tests) and weak on exactly Waypoint's hard parts (GraphHopper crossing penalties, OSM ingestion, Android OEM geolocation, the constraint solver).

Modeled at 60 percent conventional at 2.5x and 40 percent hard at 1.3x, giving a **1.8x blend**. Sensitivity:

| Multiplier | Calendar for full scope |
|---|---|
| 1.3x | 37 months |
| **1.8x modeled** | **26 months** |
| 2.5x | 19 months |
| 4.0x (marketing claim) | 12 months |

**Even the optimistic case misses the window.** A month-6 checkpoint replaces the guess with a measurement and has pre-committed actions per outcome band; below 1.2x the plan is rebuilt rather than adjusted.

## The recommendation: ship the skeleton

Make the walking skeleton the product rather than a milestone. `../05-product/mvp-scope.md` section 6 already argues this against itself: its job is to make the core hypothesis testable, and the real MVP risk is bad routes rather than missing features.

v1 becomes 12 to 15 person-months (skeleton 8 to 9, compliance minimum 2 to 3, launch hardening 2 to 3), landing **iOS at month 12 to 14** and Android at month 20 to 26. Not cut: safety-aware routing, privacy architecture, honest refusal.

## Legal: the item that could actually kill the company

**An IP assignment signed by a minor is voidable at the minor's election**, and under US copyright and patent law code belongs to its creator until assigned in writing. The two founders whose assignments are voidable are the two the concept came from. This is a question about the company's title to its own technology.

The cure needs both halves and neither alone suffices: **guardian co-signature at formation** (defensible today) plus **re-execution within 30 days of each founder turning 18** (clean). The second is the one teams forget, because it falls two or three years later. Both dates go in the diligence tracker now.

Shares are held under **Delaware UTMA** (Title 12, Chapter 45): custodial property vests indefeasibly in the minor while the custodian holds voting and contractual rights and files the 83(b). Guardians are willing, which is what makes the structure available.

Other operational facts: Apple requires the **legal age of majority** and authority to bind the organization, so Daniel is Account Holder; organization enrollment needs a **D-U-N-S number, up to 14 business days**. The 83(b) deadline is **30 days with no extensions**, the hardest deadline in the formation.

## Equity: 40 / 30 / 30, recommended

Daniel 40, Claudio 30, Asher 30, before a 10 percent pool, all with four-year vesting and a one-year cliff.

- **Daniel's premium** is for execution, capital and the only legal capacity. **Not more than 40** because he is part-time too, did not originate the concept, and a majority holder would make the other two advisory in practice in a company where they already depend on his legal capacity.
- **Claudio and Asher equal** despite Claudio's greater hours, because they co-originated together, Asher's embedded-user role is the harder one to replace, and a five-point gap between two friends buys almost nothing while creating a permanent quiet ranking.
- Alternatives argued rather than dismissed: 34/33/33 (defensible, most likely to be quietly regretted) and 50/25/25 (justifiable only if Daniel were full-time and the others passive).
- **College-transition review** at three named moments, with three named outcomes (continue, reduced role with slowed vesting, transition out with unvested repurchased). Naming these while nothing is at stake is worth more than the rest of the document.
- **Founders hold ~56 percent combined after a seed** on the modeled waterfall.

## The strategic question nobody has answered yet

Break-even at ~235 subscribers means **Waypoint can plausibly become self-sustaining without institutional money at all.** That is a genuine option, not a fallback, and it fits the honest reading of H5, which came back **uncertain** on venture scale.

A profitable $3M to $10M business is an excellent outcome for three founders and a poor one for a fund. **Which game is being played should be decided explicitly**, because it changes what to build, how fast, and whom to talk to. It is open question 4 in `fundraising-plan.md`.

## Cross-document corrections this phase made

- **Infrastructure at MVP:** use $135 to $255/month (`unit-economics.md` 1.1), not the $80 to $130 in `api-integration-map.md` 8.2, which was summed before DEC-009 replaced Supabase.
- **Net revenue multiplier:** use **0.8088** (`unit-economics.md` 1.3), not 0.84 (`revenue-model.md` 6.2). The former includes refunds.
- **`unit-economics.md` is still priced at a $7.99/month mid case** that DEC-011 replaced with $99.99/year. Every correction runs in Waypoint's favor (LTV ~$107 to $115 rather than $86, margin ~70 percent rather than 63 at 10k MAU), so nothing is hidden, but **the published tables understate the business and should not be quoted to an investor as they stand.** A full re-run is queued, not done.

## Riskiest assumption in the phase

**The 1.8x AI leverage multiplier.** Everything downstream depends on it: the schedule, the scope cut, the round size, and whether Waypoint reaches market inside its window. It has never been measured on this team or this codebase. The month-6 checkpoint exists solely to replace it with evidence.

## Related

- [[Business Model and GTM Key Findings (Phase 6)]]
- [[Product Definition Key Findings (Phase 5)]]
- [[DEC-010 Staged cross-platform MVP on React Native]] - whose dates this phase reopens
- [[DEC-011 Pricing and the permanent free tier]]
