---
type: home
created: 2026-07-30
updated: 2026-07-30
tags: [home]
---

# START HERE

This is the single always-current entry point to the Waypoint project. Every session (human or agent, in any tool) begins by reading this note. It is updated at the end of every session and represents the latest approved snapshot of project state.

> Cross-tool rule: after this note, read the newest file in `03-Sessions/`, then `research/00-PROGRESS.md` for the phase catalog. Do not re-read the whole repo. Query the graph first.

## Project state

- **Phase:** Research program Phases **0 to 4 COMPLETE**. Concept **LOCKED** ([[DEC-006 Concept lock route-first positioning]]). Phase 5 deliverables drafted; gate **partially passed** ([[DEC-008 Phase 5 gate MVP approved stack in validation]]): MVP scope, free launch, Watch fast-follow approved. **Open:** stack final decision (round 2 research) and whether MVP launches on **both iOS and Android** (amends prior iOS-first assumption). Phase 6 blocked until those close.
- **Product:** **Know where to run.** Constraint-based adaptive route generation (hero / free-tier anchor), adaptive coaching (paid), voice navigation, privacy day-one. Governing doc: `research/04-synthesis/concept.md`. See [[Charter]].
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

## What unlocks next (in order)

1. **Finish Phase 5 open gate:** land round 2 studies (`database-deep-dive.md`, `dual-platform-strategy.md`, `api-integration-map.md` in `research/05-product/`), then Claudio decides stack + iOS/Android platform strategy. Record as a new DEC if the platform or stack changes.
2. **Phase 6:** business model, unit economics, metrics, GTM (`research/06-business-model/`).
3. **Phase 7 formal close:** polish dashboard/Vercel packaging (core HTML already live).
4. **Phase 8:** investor Business Blueprint (`blueprint/`).
5. Parallel: real-user interview backlog in `research/03-users/unmet-needs.md`; sanctioned spikes (safety-data buildability, GraphHopper crossing penalties, voice-guidance) once stack is locked.

## Open threads

- Round 2 stack/platform/API studies must complete before Phase 6. #open
- Dual-platform MVP amends DEC-006 / DEC-008 iOS-first assumption; needs an explicit founder decision and decision record. #open
- Blueprint example URL (premiumcuts-blueprint.vercel.app) was unreachable; retry at Phase 8 or get section list from Claudio. #open-question
- Partner onboarding: `CONTRIBUTING.md` ready; confirm which tool they use. #open-question
- No app CI/CD yet (add when application code exists). #open-question

## Map of the vault

- [[Charter]] - what Waypoint is (LOCKED with concept, DEC-006)
- [[Founder-Brief]] - vision and hypotheses H1 to H7
- [[_Decision-Log]] - all decisions
- `03-Sessions/` - newest note is freshest working context
- `04-Knowledge/` - distilled research (see [[_Knowledge-Index]])
- `05-Architecture/` - empty until stack locks and build starts
- `_templates/` - session, decision, knowledge templates

## How memory works here

1. Session start: this note → newest `03-Sessions/` note → `research/00-PROGRESS.md`.
2. Task context: `graphify query "<question>" --budget 2000` (or open `/graph/` on Vercel), not a full repo read.
3. During work: write decisions immediately to `02-Decisions/`.
4. Session end: update this note, session note, `research/00-PROGRESS.md` if phases moved, graphify update if docs changed, commit and push.
