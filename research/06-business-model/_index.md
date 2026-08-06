# Phase 6: Business Model and Go-to-Market

> Version-Timestamp: 2026-08-06 13:20:00 UTC-4

**Status: COMPLETE. Gate closed 2026-08-06** as DEC-011, DEC-012 and DEC-013. Program catalog: `../00-PROGRESS.md`.

## Deliverables

(See `../00-RESEARCH-PLAYBOOK.md` for full specs and standards.)

| File | Contents | Status |
|------|----------|--------|
| `business-model-canvas.md` | All nine blocks, plus the cross-document reconciliation and the six gate cards. **Read this one first** | complete |
| `revenue-model.md` | $99.99/yr list, $12.99/mo, 21-day annual trial, Founding Runner at $69.99/yr price-preserved; lifetime tier and data monetization rejected | complete |
| `unit-economics.md` | Directional model across a $4.99-$11.99 band; break-even ~3,000 subscribers; paid acquisition unviable at every price | complete |
| `metrics.md` | North Star = Weekly Routed Runners; activation = first generated route completed as a recorded run; Good Route Rate; ten guardrails | complete |
| `gtm-plan.md` | One metro, one segment; run clubs > Reddit > store optimization; paywall transition protocol. Its recommendation that the Android date carry the public launch was **overridden** at the gate | complete |

## The finding that governs this phase

**Waypoint's unit economics are a function of its distribution strategy, not its pricing.** Paid acquisition returns 53 to 70 cents on the dollar at every price in the credible band, so the business clears a 3:1 lifetime-value-to-acquisition-cost ratio only at roughly 84 percent or better organic acquisition. The go-to-market plan independently rejects paid acquisition pre-funding, so the plans agree, but the dependency is permanent: if community-first distribution fails, no price rescues the model.

## Gate outcome (2026-08-06): all six closed

| # | Decision | Outcome |
|---|---|---|
| 1 | Price | Approved as recommended: $99.99/yr, $12.99/mo, 21-day annual-only trial, Founding Runner $69.99/yr price-preserved (DEC-011) |
| 2 | Free/paid boundary | Approved as recommended, escape hatch declined. Coaching layer alone is paid; the free tier is named publicly at launch (DEC-011) |
| 3 | Analytics identity | First-party Postgres cohort table on the existing account identifier; TelemetryDeck keeps aggregate signals (DEC-012) |
| 4 | PRD G3 and G4 | Re-based to activated-cohort definitions with a separate install-level benchmark line (DEC-012) |
| 5 | Beachhead metro | The founder's home metro, subject to the month-1 pedestrian-data spike (DEC-013) |
| 6 | Which date is the real launch | **OVERRIDDEN: iOS at month 9 to 10**, not the Android date (DEC-013) |

**On the override.** The Apple featuring nomination is iOS-only and cannot be spent on an Android launch, speed matters inside a 12 to 18 month window the build already consumes ten months of, and iOS carries roughly 85 percent of category subscription revenue. The cost is losing the quiet burn-in, so DEC-013 attaches four conditions: the month-8 beta cohort target becomes a hard gate on the launch date, reviews are seeded from that cohort with a 99.5 percent crash-free release gate, Android waitlist capture starts at launch, and the featuring nomination is filed at month 6 to 7.

## Corrections to Phase 5 this phase produced (all applied)

- `../05-product/prd.md`: goals G3 and G4 re-based; activation redefined; assumption A1 partly resolved.
- `../05-product/api-integration-map.md`: section 6.2 amended for the analytics split, section 4.2 for Better Auth, and the remaining Supabase references replaced per DEC-009.
- The month-1 safety-data buildability spike is now a **go-to-market gate**, not merely a technical one, because the beachhead choice depends on its result.

## Inputs this phase depends on (all now available)

- Locked concept (Phase 4 / DEC-006)
- Approved MVP scope (DEC-008) and revised stack (DEC-009: Aiven + self-managed PostGIS + Better Auth)
- Platform decision (DEC-010: staged React Native; iOS month 9-10, Android month 10-12; ~29-31 person-months)
- Cost inputs: external services ~$80-130/mo at MVP and ~$350-500/mo at 10k MAU (`../05-product/api-integration-map.md`), store commissions at the 15 percent small-business tiers on both stores, RevenueCat ~1.4 percent of net
- Market sizing and competitive pricing matrices (Phases 1 to 2)

## Constraints this phase must respect

- v1 launches **entirely free**; safety-aware routing stays free permanently (DEC-008). The paid layer arrives in v1.x, months 10 to 12, so year-one revenue modeling starts from a free base.
- Both app stores must be modeled separately past $1M: Apple's small-business tier is a cliff, Google's is graduated.
