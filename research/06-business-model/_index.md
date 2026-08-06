# Phase 6: Business Model and Go-to-Market

> Version-Timestamp: 2026-08-06 12:45:00 UTC-4

**Status: DELIVERABLES COMPLETE, gate open.** All five documents written 2026-08-06. Six gate decisions await the founder on `dashboard/index.html` section "Phase 6". Program catalog: `../00-PROGRESS.md`.

## Deliverables

(See `../00-RESEARCH-PLAYBOOK.md` for full specs and standards.)

| File | Contents | Status |
|------|----------|--------|
| `business-model-canvas.md` | All nine blocks, plus the cross-document reconciliation and the six gate cards. **Read this one first** | complete |
| `revenue-model.md` | $99.99/yr list, $12.99/mo, 21-day annual trial, Founding Runner at $69.99/yr price-preserved; lifetime tier and data monetization rejected | complete |
| `unit-economics.md` | Directional model across a $4.99-$11.99 band; break-even ~3,000 subscribers; paid acquisition unviable at every price | complete |
| `metrics.md` | North Star = Weekly Routed Runners; activation = first generated route completed as a recorded run; Good Route Rate; ten guardrails | complete |
| `gtm-plan.md` | One metro, one segment; run clubs > Reddit > store optimization; Android date is the real public launch; paywall transition protocol | complete |

## The finding that governs this phase

**Waypoint's unit economics are a function of its distribution strategy, not its pricing.** Paid acquisition returns 53 to 70 cents on the dollar at every price in the credible band, so the business clears a 3:1 lifetime-value-to-acquisition-cost ratio only at roughly 84 percent or better organic acquisition. The go-to-market plan independently rejects paid acquisition pre-funding, so the plans agree, but the dependency is permanent: if community-first distribution fails, no price rescues the model.

## Open gate decisions (see dashboard, or `business-model-canvas.md` section 11)

1. Price: $99.99/yr list and the Founding Runner rate
2. Free/paid boundary breadth, and whether to keep an escape hatch
3. Analytics identity conflict (TelemetryDeck cannot deliver cohort retention)
4. Re-base PRD goals G3 and G4
5. Beachhead metro (needs the founder's local knowledge plus the month-1 spike)
6. Whether the Android date is the real public launch

## Corrections to Phase 5 that this phase surfaced

- PRD goals G3 and G4 need re-basing (gate card 4).
- `../05-product/api-integration-map.md` names TelemetryDeck for analytics, which cannot support cohort retention (gate card 3).
- The month-1 safety-data buildability spike should be treated as a **go-to-market gate**, not merely a technical one, because the beachhead choice depends on its result.

## Inputs this phase depends on (all now available)

- Locked concept (Phase 4 / DEC-006)
- Approved MVP scope (DEC-008) and revised stack (DEC-009: Aiven + self-managed PostGIS + Better Auth)
- Platform decision (DEC-010: staged React Native; iOS month 9-10, Android month 10-12; ~29-31 person-months)
- Cost inputs: external services ~$80-130/mo at MVP and ~$350-500/mo at 10k MAU (`../05-product/api-integration-map.md`), store commissions at the 15 percent small-business tiers on both stores, RevenueCat ~1.4 percent of net
- Market sizing and competitive pricing matrices (Phases 1 to 2)

## Constraints this phase must respect

- v1 launches **entirely free**; safety-aware routing stays free permanently (DEC-008). The paid layer arrives in v1.x, months 10 to 12, so year-one revenue modeling starts from a free base.
- Both app stores must be modeled separately past $1M: Apple's small-business tier is a cliff, Google's is graduated.
