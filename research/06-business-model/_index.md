# Phase 6: Business Model and Go-to-Market

> Version-Timestamp: 2026-08-06 11:40:00 UTC-4

**Status: UNBLOCKED, not yet started.** The Phase 5 stack and platform gates closed on 2026-08-06 (DEC-009, DEC-010). Program catalog: `../00-PROGRESS.md`.

## Expected deliverables

(See `../00-RESEARCH-PLAYBOOK.md` for full specs and standards.)

- [ ] `business-model-canvas.md` - all nine blocks
- [ ] `revenue-model.md` - pricing strategy and revenue streams (free-launch and permanent free safety routing already decided in DEC-008)
- [ ] `unit-economics.md` - directional CAC, LTV, margins, all labeled directional
- [ ] `metrics.md` - North Star metric and supporting metric tree
- [ ] `gtm-plan.md` - launch strategy, channels, early traction plan

## Inputs this phase depends on (all now available)

- Locked concept (Phase 4 / DEC-006)
- Approved MVP scope (DEC-008) and revised stack (DEC-009: Aiven + self-managed PostGIS + Better Auth)
- Platform decision (DEC-010: staged React Native; iOS month 9-10, Android month 10-12; ~29-31 person-months)
- Cost inputs: external services ~$80-130/mo at MVP and ~$350-500/mo at 10k MAU (`../05-product/api-integration-map.md`), store commissions at the 15 percent small-business tiers on both stores, RevenueCat ~1.4 percent of net
- Market sizing and competitive pricing matrices (Phases 1 to 2)

## Constraints this phase must respect

- v1 launches **entirely free**; safety-aware routing stays free permanently (DEC-008). The paid layer arrives in v1.x, months 10 to 12, so year-one revenue modeling starts from a free base.
- Both app stores must be modeled separately past $1M: Apple's small-business tier is a cliff, Google's is graduated.
