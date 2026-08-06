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

- **Phase:** Research program Phases **0 to 5 COMPLETE and gated**; **Phase 6 deliverables written, gate open with six decisions** on the dashboard (price, free/paid boundary breadth, the analytics identity fix, re-basing PRD G3/G4, beachhead metro, and which date is the real launch). Governing Phase 6 finding: unit economics depend on distribution, not pricing, since paid acquisition returns 53 to 70 cents on the dollar and the model needs ~84 percent organic. See [[Business Model and GTM Key Findings (Phase 6)]]. Concept **LOCKED** ([[DEC-006 Concept lock route-first positioning]]). Phase 5 closed 2026-08-06: MVP scope, free launch, Watch fast-follow ([[DEC-008 Phase 5 gate MVP approved stack in validation]]); data layer revised to Aiven EU + self-managed PostGIS + decoupled Better Auth, Supabase dropped ([[DEC-009 Revised data layer Aiven split architecture with decoupled auth]], **revisitable by design**); dual-platform MVP from one React Native codebase, iOS month 9-10, Android +4-8 weeks, ~29-31 person-months ([[DEC-010 Staged cross-platform MVP on React Native]]). **Next: Phase 6** (business model, unit economics, metrics, GTM).
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
- [x] **Phase 6 deliverables** 2026-08-06: business model canvas, revenue model, unit economics, metrics, GTM plan → [[Business Model and GTM Key Findings (Phase 6)]]

## What unlocks next (in order)

1. **Close the Phase 6 gate:** six decisions staged on `dashboard/index.html`. Once answered, record the DECs (next numbers DEC-011 onward), apply the two Phase 5 corrections the phase surfaced (PRD G3/G4 re-basing, and the TelemetryDeck analytics conflict in `api-integration-map.md`), and tag v0.3.0.
2. **Phase 7 formal close:** polish dashboard/Vercel packaging (core HTML already live).
3. **Phase 8:** investor Business Blueprint (`blueprint/`).
4. Parallel: real-user interview backlog in `research/03-users/unmet-needs.md`; sanctioned spikes (safety-data buildability, GraphHopper crossing penalties, Ferrostar voice-guidance now answering for two platforms).

## Open threads

- **The stack is deliberately revisitable.** DEC-009 was approved "for now" with Claudio's standing instruction that infrastructure detail must not block product definition. Re-open it at any of its four named checkpoints (before the walking skeleton, when architecture design starts, at Aiven contract time, or if ops burden proves real) with a superseding DEC. #open
- Verify Garmin Connect writes into Health Connect before Android work begins (H6 verified for HealthKit only). #open-question
- `api-integration-map.md` section 4 still names Supabase Auth; superseded by DEC-009. Correct when architecture notes are written. #open
- Six Phase 6 gate decisions are open on the dashboard and block Phase 7 close and Phase 8. #open
- Riskiest open assumption in the whole program: whether the beachhead metro clears the OpenStreetMap pedestrian-data floor. The month-1 buildability spike answers it, and should be treated as a **go-to-market gate**, not only a technical one. #open-question
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
