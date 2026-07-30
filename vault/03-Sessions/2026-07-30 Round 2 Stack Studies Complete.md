---
type: session
created: 2026-07-30
updated: 2026-07-30
tags: [session, research, phase-5, stack, platform]
---

# Session 2026-07-30 - Round 2 stack studies complete

## Goal

Relaunch the three Phase 5 round-2 studies after Claudio fixed the API access issue, verify their output, digest them into the dashboard, and stage the stack + platform gate.

## What was done

- All three round-2 studies completed and are on disk in `research/05-product/`:
  - `database-deep-dive.md` (committed by its research agent, bd99512): 12 candidates scored; **Aiven 4.46 vs Supabase 3.45**; verdict is a split architecture (Aiven EU for personal data, self-managed PostGIS on the Hetzner private net for the moat, auth decoupled via Better Auth). Supersedes round 1's "Supabase with conditions".
  - `dual-platform-strategy.md` (committed by its research agent): recommends **Option D, staged cross-platform on React Native + MapLibre** (~29-31 pm, iOS month 9-10, Android +4-8 weeks). Runna is the existence proof. Amends DEC-006 client stack if chosen.
  - `api-integration-map.md` (committed this session): ~20 required integrations across 7 domains; ~$80-130/mo external services at MVP; 6 gate the walking skeleton; Android paperwork must start month 1 if greenlit.
- Dashboard: card 8 rewritten as "Approve the revised stack?" with the split-architecture table and integration cost digest; new card 9 "Platform strategy" with options D / C / reconsider; round-1 stack table flagged as partially superseded.
- Catalogs updated in agreement: `research/00-PROGRESS.md`, `research/05-product/_index.md`, [[00-START-HERE]], [[Product Definition Key Findings (Phase 5)]] (round 2 section added; Open-Meteo pricing question resolved).
- Knowledge graph updated via the `--update` flow.

## Decisions made

None; two are now STAGED for Claudio on the dashboard (protected Vercel preview, `/dashboard/`):

1. **Card 8, revised stack:** Aiven split architecture + Better Auth, replacing Supabase. Recommended: approve.
2. **Card 9, platform:** Option D staged React Native recommended; alternatives are dual-native staged (C) or iOS-only with Android in v1.x. Requires a new DEC either way; Option C/D also amends `mvp-scope.md` effort (~29-31 pm) and the Charter client stack.

## Open threads

- Cards 8 and 9 block Phase 6. #open
- Garmin Connect → Health Connect write path unverified (H6 was HealthKit-only); confirm before Android commitment. #open-question
- Note for the DEC when written: `api-integration-map.md` section 4 still names Supabase Auth for sign-in; it predates the database verdict and should be read as "the auth layer" (Better Auth per the deep dive).

## Next steps for the next agent (any tool)

1. If Claudio has answered cards 8 and 9: record the two DECs (next numbers DEC-009, DEC-010), update `mvp-scope.md`, Charter, and PROGRESS, then open Phase 6.
2. If not: nothing to build; the gate is with the founder.

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] `research/00-PROGRESS.md` current and agreeing with START-HERE
- [x] Graph updated
- [x] Committed and pushed
