---
type: home
created: 2026-07-30
updated: 2026-08-06
tags: [home]
---

# START HERE

This is the single always-current entry point to the Waypoint project. Every session (human or agent, in any tool) begins by reading this note. It is updated at the end of every session and represents the latest approved snapshot of project state.

> Cross-tool rule: after this note, read the newest file in `03-Sessions/`, then `research/00-PROGRESS.md` for the phase catalog. Do not re-read the whole repo. Query the graph first.

## Project state

- **Phase:** Research program Phases **0 to 6 COMPLETE and gated**. Phase 6 closed 2026-08-06 with [[DEC-011 Pricing and the permanent free tier]], [[DEC-012 Measurement corrections analytics identity and re-based targets]] and [[DEC-013 Home-metro beachhead and iOS-first public launch]]. Price is $99.99/yr with the coaching layer as the only paid product; the beachhead is the home metro; **the iOS date at month 9 to 10 carries the public launch**, overriding the plan's Android recommendation. Governing Phase 6 finding: unit economics depend on distribution, not pricing, since paid acquisition returns 53 to 70 cents on the dollar and the model needs ~84 percent organic. See [[Business Model and GTM Key Findings (Phase 6)]]. Concept **LOCKED** ([[DEC-006 Concept lock route-first positioning]]). Phase 5 closed 2026-08-06: MVP scope, free launch, Watch fast-follow ([[DEC-008 Phase 5 gate MVP approved stack in validation]]); data layer revised to Aiven EU + self-managed PostGIS + decoupled Better Auth, Supabase dropped ([[DEC-009 Revised data layer Aiven split architecture with decoupled auth]], **revisitable by design**); dual-platform MVP from one React Native codebase, iOS month 9-10, Android +4-8 weeks, ~29-31 person-months ([[DEC-010 Staged cross-platform MVP on React Native]]). **Next: Phase 6** (business model, unit economics, metrics, GTM).
- **Product:** **Know where to run.** Constraint-based adaptive route generation (hero / free-tier anchor), adaptive coaching (paid), voice navigation, privacy day-one. Ships on iOS and Android from one React Native codebase. Governing doc: `research/04-synthesis/concept.md`. See [[Charter]].
- **Review surface:** `dashboard/index.html` (dashboard-first gates). Also live on the protected Vercel preview with `graph/index.html` (interactive knowledge graph).
- **Publishing:** GitHub → Vercel auto-deploy ([[DEC-007 Vercel publishing pipeline with protected previews]]). Real content: https://waypoint-git-main-mollypartys-projects.vercel.app (login required). Production domains serve a placeholder only.
- **Latest version:** **v0.2.0** (Phases 1 to 4 complete, concept locked). Next planned tag: v0.3.0 after Phases 5 to 6.

## What is done

- [x] Git + GitHub (`mollyparty/waypoint`), trunk-based versioning ([[DEC-001 Trunk-based versioning on main]])
- [x] Obsidian vault as project memory ([[DEC-002 Obsidian vault as project memory]])
- [x] Graphify knowledge graph + post-commit hook ([[DEC-003 Graphify as queryable project brain]])
- [x] Agent memory protocol (`AGENTS.md`, Cursor rule); cross-IDE files (`CLAUDE.md`, `CONTRIBUTING.md`) ([[DEC-004 Continuous push and cross-IDE agent files]])
- [x] Research playbook + nine gated phases ([[DEC-005 Phased research program with gated approvals]]); progress catalog at `research/00-PROGRESS.md`
- [x] Founder Brief + Charter ([[Founder-Brief]], [[Charter]]); hypotheses H1 to H7
- [x] Phase 1 market research (`research/01-market/`) → [[Market Research Key Findings (Phase 1)]]
- [x] Phase 2 competitors (`research/02-competitors/`, 14 docs) → [[Competitive Landscape Key Findings (Phase 2)]]
- [x] Phase 3 users (`research/03-users/`) → [[User Research Key Findings (Phase 3)]]
- [x] Phase 4 synthesis; concept LOCKED → [[Concept and Positioning (Phase 4)]], DEC-006, tag v0.2.0
- [x] Research dashboard (`dashboard/index.html`); graph explorer (`graph/index.html`); Vercel publishing (DEC-007)
- [x] Phase 5 drafts: PRD, RICE, MVP scope, journeys, stack recommendation, stack validation → [[Product Definition Key Findings (Phase 5)]]; DEC-008 (partial gate)
- [x] Phase 5 round 2 studies: `database-deep-dive.md` (Aiven split architecture beats Supabase), `dual-platform-strategy.md` (staged React Native), `api-integration-map.md` (~20 integrations, ~$80-130/mo MVP)
- [x] **Phase 5 gate closed** 2026-08-06: stack revised (DEC-009) and dual-platform strategy chosen (DEC-010); amendments propagated to `mvp-scope.md` and [[Charter]]
- [x] **Phase 6 complete and gate closed** 2026-08-06: business model canvas, revenue model, unit economics, metrics, GTM plan → [[Business Model and GTM Key Findings (Phase 6)]]. DEC-011, DEC-012, DEC-013 recorded; PRD G3/G4 and the API integration map amended to match; tagged v0.3.0

## What unlocks next (in order)

1. **Phase 7 formal close:** polish dashboard and Vercel packaging (core HTML already live and current through Phase 6).
2. **Phase 8:** investor Business Blueprint (`blueprint/`).
4. Parallel: real-user interview backlog in `research/03-users/unmet-needs.md`; sanctioned spikes (safety-data buildability, GraphHopper crossing penalties, Ferrostar voice-guidance now answering for two platforms).

## Open threads

- **The stack is deliberately revisitable.** DEC-009 was approved "for now" with Claudio's standing instruction that infrastructure detail must not block product definition. Re-open it at any of its four named checkpoints (before the walking skeleton, when architecture design starts, at Aiven contract time, or if ops burden proves real) with a superseding DEC. #open
- Verify Garmin Connect writes into Health Connect before Android work begins (H6 verified for HealthKit only). #open-question
- ~~`api-integration-map.md` section 4 still names Supabase Auth~~ resolved 2026-08-06; sections 4.2 and 6.2 amended, and the Supabase rows in the master table and critical path replaced.
- Riskiest open assumption in the whole program: whether the home metro clears the OpenStreetMap pedestrian-data floor. The month-1 buildability spike answers it, and is now a **go-to-market gate**, not only a technical one (DEC-013). #open-question
- The launch override removed the quiet burn-in period, so the month-8 beta cohort target of 150 to 300 testers is now a **hard gate on the launch date**. #open
- The paid product rests entirely on one job. If training-state-aware generation is not felt value, there is no fallback paid thing at v1.x (DEC-011). #risk
- Verify a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores. A 30-minute check that prevents a launch-week surprise. #open-question
- Blueprint example URL (premiumcuts-blueprint.vercel.app) was unreachable; retry at Phase 8 or get section list from Claudio. #open-question
- Partner onboarding: `CONTRIBUTING.md` ready; confirm which tool they use. #open-question
- No app CI/CD yet (add when application code exists). #open-question

## Map of the vault

- [[Charter]] - what Waypoint is (LOCKED with concept, DEC-006)
- [[Founder-Brief]] - vision and hypotheses H1 to H7
- [[_Decision-Log]] - all decisions
- `03-Sessions/` - newest note is freshest working context
- `04-Knowledge/` - distilled research (see [[_Knowledge-Index]])
- `05-Architecture/` - empty until build starts; stack is decided (DEC-009, DEC-010) and this is where the detailed design, and any stack revisit, gets written
- `_templates/` - session, decision, knowledge templates

## How memory works here

1. Session start: this note → newest `03-Sessions/` note → `research/00-PROGRESS.md`.
2. Task context: `graphify query "<question>" --budget 2000` (or open `/graph/` on Vercel), not a full repo read.
3. During work: write decisions immediately to `02-Decisions/`.
4. Session end: update this note, session note, `research/00-PROGRESS.md` if phases moved, graphify update if docs changed, commit and push.
