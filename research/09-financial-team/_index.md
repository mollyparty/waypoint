# Phase 9: Financial Strategy and Founding Team Roadmap

> Version-Timestamp: 2026-08-06 14:00:00 UTC-4

**Status: DELIVERABLES COMPLETE; card 1 accepted (DEC-014), five cards open.** Program catalog: `../00-PROGRESS.md`.

This phase was not in the original program. [[DEC-005 Phased research program with gated approvals]] defined Phases 0 through 8. Phase 9 was opened on 2026-08-06 when the founding team was defined for the first time, and the definition invalidated assumptions that eight phases of research had been quietly resting on.

## Approval update, 2026-09-05

Recut v1 is the approved first-release baseline under DEC-014. Catalog assignments now reflect eight reduced slices plus 34 obligations. Approximately month 13 is a model estimate, not a dated commitment. The five founder agreement/formation/funding decisions remain open. Historical estimates below are superseded where they conflict with the catalog.

## Why this phase exists

Every financial figure in the repo was built on a single sentence in the Charter: **"Solo founder (Claudio) building from scratch."** That sentence was wrong. The real founding team is three partners, none of them full-time, two of them minors, building with AI agents instead of contractors.

Three numbers collapse as a direct result:

| Figure | Where it lived | Why it fails |
|---|---|---|
| **~$230,000 cash build** | `../06-business-model/unit-economics.md` section 1.5 | It is the price of buying 18 to 20 contractor person-months. The team is not buying them. |
| **~$15,000/month operating base** | `unit-economics.md` section 1.4 | It is a $7,000 founder draw plus a $6,000 contractor retainer. Nobody is drawing a salary. |
| **~$350,000 to $400,000 pre-seed** | `blueprint/blueprint.md` section 13 | It is the sum of the two figures above. Both inputs are gone, so the ask was unsupported. |

And one estimate becomes unsafe rather than merely wrong: [[DEC-010 Staged cross-platform MVP on React Native]] costs the MVP at 29 to 31 person-months and dates iOS at month 9 to 10, on the stated assumption of **2.5 to 3.0 full-time-equivalent people**. The actual team has none.

## Deliverables

| File | Contents | Status |
|------|----------|--------|
| `legal-formation.md` | Delaware C-corp sequence, UTMA custodial shares for the two minor founders, the IP-assignment cure path, 83(b) mechanics, and who must hold the Apple, Play, banking and vendor accounts | complete |
| `operating-model.md` | Real overhead by category, a four-stage burn table, runway against the friends-and-family round, a 36-month projection, and the reconciliation of three cross-document cost conflicts | complete |
| `team-roadmap.md` | Role definition per founder, the capacity reconciliation against the 29 to 31 person-month scope, the re-derived schedule, and school seasonality | complete |
| `capital-structure.md` | Founder equity split with alternatives argued rather than dismissed, vesting, the option pool, and the dilution waterfall | complete |
| `fundraising-plan.md` | Friends-and-family SAFE mechanics, the milestones that make institutional money raisable, process, and the diligence-readiness checklist | complete |

**Read `team-roadmap.md` first.** It carries the finding that governs the phase.

## The finding that governs this phase

**Waypoint's binding constraint is no longer money. It is calendar time, and there is not enough of it.**

The old model was capital-constrained: buy 18 to 20 person-months of contractor time for $230,000, or do not ship. The new model is capacity-constrained. Burn falls by roughly 96 percent, from about $15,000 a month to a few hundred, which sounds like unambiguously good news and is not. Money can be raised in weeks. The team cannot buy back the calendar, because the scarce input is the founders' available hours, and those are fixed by school and by another full-time business.

Run the arithmetic and the full 29 to 31 person-month scope does not land inside the 12 to 18 month competitive window from Phase 1. This is not a reason to stop. It is a reason the scope decision, not the funding decision, is the one that matters at this gate.

## Gate decisions for the founders

| # | Decision | Recommendation |
|---|---|---|
| 1 | **Scope and timeline.** How to close the gap between 29 to 31 person-months and the hours actually available | Ship the walking skeleton as the product, not as a milestone. Supersede the DEC-010 dates. See `team-roadmap.md` section 5 |
| 2 | **Equity split** across three founders | Daniel 40, Claudio 30, Asher 30, with two alternatives argued in `capital-structure.md` section 3 |
| 3 | **Vesting** | Four years, one-year cliff, all three, with a college-transition re-evaluation trigger |
| 4 | **Option pool** | 10 percent at formation, because equity is the only currency available for engineering help |
| 5 | **Formation timing** | Incorporate before the round, not after. See `legal-formation.md` section 6 |
| 6 | **Round size and terms** | $50,000 on a post-money SAFE at a $1.5M cap, roughly 3.3 percent |

## What this phase is not

It is not legal, tax, or investment advice, and it must not be used as a substitute for any of them. It is a founder-level framework whose purpose is to make an hour with a startup attorney productive instead of exploratory. Formation involving minor founders is specifically the case where that hour is not optional. The build budget already carries $8,000 to $20,000 for counsel.

## Inputs this phase depends on

- `../06-business-model/unit-economics.md` for infrastructure cost, store commissions and the net revenue multiplier
- `../06-business-model/revenue-model.md` for the locked pricing and revenue phasing ([[DEC-011 Pricing and the permanent free tier]])
- `../05-product/mvp-scope.md` section 6 for the walking skeleton and section 7 for effort
- `../05-product/api-integration-map.md` section 8 for per-service unit costs
- [[DEC-010 Staged cross-platform MVP on React Native]] for the effort estimate this phase reopens
