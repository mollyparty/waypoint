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

- **Phase:** Phases **0 to 8 COMPLETE** (Phase 8's blueprint awaits founder review), and **Phase 9 deliverables are done with its gate OPEN: six decisions await you on the dashboard.** Phase 9 was opened 2026-08-06 when the founding team was defined as **three part-time partners, two of them minors, building AI-assisted rather than hiring**. That invalidated the $230k build, the $15k/month base, and the $350k to $400k ask, all of which derived from a solo-founder-with-contractors assumption. Real burn is **~$400/month**, break-even is **~235 paying subscribers** rather than ~3,000, and the ask is **$50k on a SAFE at a $1.5M cap**. The finding that governs it: **the binding constraint is calendar time, not money** — 29 to 31 person-months of scope (the catalog has since corrected this to **~32-33**, see below) against ~7.5 person-months a year of capacity, so the recommendation is to ship the walking skeleton as the product, landing iOS at month 12 to 14 and superseding DEC-010's dates. See [[Financial Strategy and Founding Team (Phase 9)]]. Phase 6 closed 2026-08-06 with [[DEC-011 Pricing and the permanent free tier]], [[DEC-012 Measurement corrections analytics identity and re-based targets]] and [[DEC-013 Home-metro beachhead and iOS-first public launch]]. Price is $99.99/yr with the coaching layer as the only paid product; the beachhead is the home metro; **the iOS date at month 9 to 10 carries the public launch**, overriding the plan's Android recommendation. Governing Phase 6 finding: unit economics depend on distribution, not pricing, since paid acquisition returns 53 to 70 cents on the dollar and the model needs ~84 percent organic. See [[Business Model and GTM Key Findings (Phase 6)]]. Concept **LOCKED** ([[DEC-006 Concept lock route-first positioning]]). Phase 5 closed 2026-08-06: MVP scope, free launch, Watch fast-follow ([[DEC-008 Phase 5 gate MVP approved stack in validation]]); data layer revised to Aiven EU + self-managed PostGIS + decoupled Better Auth, Supabase dropped ([[DEC-009 Revised data layer Aiven split architecture with decoupled auth]], **revisitable by design**); dual-platform MVP from one React Native codebase, ~29-31 person-months ([[DEC-010 Staged cross-platform MVP on React Native]]; **its month 9-10 iOS date is superseded pending the Phase 9 gate**).
- **Product:** **Know where to run.** Constraint-based adaptive route generation (hero / free-tier anchor), adaptive coaching (paid), voice navigation, privacy day-one. Ships on iOS and Android from one React Native codebase. Governing doc: `research/04-synthesis/concept.md`. See [[Charter]].
- **Scope source of truth:** **`catalog/features.json`** and its interactive surface `catalog/index.html` ([[DEC-020 Features catalog is the source of truth for release phase]], 2026-08-06). 70 entries — 30 features, 15 compliance requirements, 19 non-functional requirements, 6 items ruled out by DEC-006 — each tied to persona, need and job, with release assignment adjustable and the projected launch month recomputed live. `mvp-scope.md`, `prd.md` and `rice-prioritization.md` keep their analysis but no longer decide phase; all three are annotated. It corrected full scope to **~32-33 person-months from 29-31**, because the obligations were absorbed into a single ~2 pm overhead line. See [[Features Catalog and Scope Arithmetic]].
- **Review surface:** `dashboard/index.html` (dashboard-first gates). Also live on the protected Vercel preview with `graph/index.html` (interactive knowledge graph) and `catalog/index.html`.
- **Publishing:** GitHub → Vercel auto-deploy ([[DEC-007 Vercel publishing pipeline with protected previews]]). Real content: https://waypoint-git-main-mollypartys-projects.vercel.app (login required). Production domains serve a placeholder only.
- **Latest version:** **v0.3.0** (Phases 5 to 6 approved). Next planned tag: v0.4.0 once the blueprint is approved, which now waits on the Phase 9 rewrite of its capital and team sections.

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
- [x] Phase 5 drafts: PRD, RICE, MVP scope, journeys, stack recommendation, stack validation → [[Product Definition Key Findings (Phase 5)]]; DEC-008 closed three of five cards, with stack and platform held for round 2
- [x] Phase 5 round 2 studies: `database-deep-dive.md` (Aiven split architecture beats Supabase), `dual-platform-strategy.md` (staged React Native), `api-integration-map.md` (~20 integrations, ~$80-130/mo MVP)
- [x] **Phase 5 gate closed** 2026-08-06: stack revised (DEC-009) and dual-platform strategy chosen (DEC-010); amendments propagated to `mvp-scope.md` and [[Charter]]
- [x] **Phase 6 complete and gate closed** 2026-08-06: business model canvas, revenue model, unit economics, metrics, GTM plan → [[Business Model and GTM Key Findings (Phase 6)]]. DEC-011, DEC-012, DEC-013 recorded; PRD G3/G4 and the API integration map amended to match; tagged v0.3.0

- [x] **Phase 7 closed** 2026-08-06: dashboard covers Phases 0 to 6, HTML validated, landing page links all three artifacts
- [x] **Phase 8 blueprint drafted** 2026-08-06: `blueprint/blueprint.md` and `blueprint/index.html`; sections 12 and 13 rewritten by Phase 9
- [x] **Memory audit and remediation** 2026-08-06: graph coverage 86 of 86 documents (eleven had no node at all), the Phase 6 launch-shape contradiction fixed, Phases 7 and 8 split into their own session note, catalogs synced. The graphify post-commit hook is now scoped to code paths, because its no-LLM rebuild was silently dropping curated nodes on doc commits (**local-only fix; `.git/hooks/` is untracked**)
- [x] **Phase 9 deliverables complete** 2026-08-06: legal formation, operating model, team roadmap, capital structure, fundraising plan → [[Financial Strategy and Founding Team (Phase 9)]]
- [x] **Features and functionality catalog** 2026-08-06 (DEC-020): `catalog/features.json` plus `catalog/index.html`, `catalog/FEATURES.md` and `catalog/build.py`. One effort model that reproduces four separately-published figures, four document conflicts resolved with written recommendations, and the instrument for settling Phase 9 gate card 1 → [[Features Catalog and Scope Arithmetic]]
- [x] **Graph current as of 2026-08-06**: 227 nodes, 542 edges, 15 communities, coverage measured at 104 of 104 corpus documents with zero dangling links and zero isolated nodes. A "what ships when" query now lands on the catalog rather than on one of the three documents that disagree

## What unlocks next (in order)

1. **Answer the six Phase 9 gate cards** on `dashboard/index.html`, then record DEC-014 onward. Card 1 (scope and timeline) is the consequential one and it supersedes DEC-010's dates. **Settle card 1 in `catalog/index.html`**, where the recommended recut is loaded by default and the three alternatives are one click away, each showing its projected launch month against the competitive window. Cards 2 to 4 are the founder agreement: equity split, vesting, option pool. Cards 5 and 6 are formation timing and the round. Once card 1 is decided, update `features.json` to match and rerun `python catalog/build.py`.
2. **Founder review of the blueprint.** Its capital and team sections are now rebuilt on real numbers, so the largest of the four open items in `research/08-blueprint/_index.md` is resolved. Remaining: whether to publish to a separate public Vercel project, whether an EN/ES edition is wanted, and the Runna ARR conflict between two source documents.
3. **Tag v0.4.0** with a CHANGELOG entry once the blueprint is approved. The entry is already staged under Unreleased.
4. **Then the build begins**, starting with formation (see `research/09-financial-team/legal-formation.md` section 6 for the sequence) and the month-1 A3 safety-data buildability spike, which is a **go-to-market gate** since the beachhead metro depends on it.
5. Parallel: real-user interview backlog in `research/03-users/unmet-needs.md`; sanctioned spikes (safety-data buildability, GraphHopper crossing penalties, Ferrostar voice-guidance now answering for two platforms).

## Open threads

- **The riskiest number in the whole repo is the 1.8x AI leverage multiplier**, which underwrites the schedule, the scope cut and the round size, and has never been measured on this team. The month-6 checkpoint exists to replace it with evidence; below 1.2x the plan is rebuilt rather than adjusted. It is now a slider in `catalog/index.html` so the sensitivity can be seen: at 1.0x the recut's launch moves from month 13 to month 23. #risk
- **A scope decision made in the catalog UI lives in one browser only.** Scenario state is `localStorage`, so it must be exported and written back into `features.json` to become real. Likewise `catalog/build.py` is not wired to a hook, so editing the JSON without running it leaves `FEATURES.md` stale — which is exactly the drift the catalog was built to end. #risk
- **Venture scale or profitable independence?** Break-even at ~235 subscribers means Waypoint can plausibly self-sustain without institutional money, which fits the uncertain H5 verdict. These are different games and the answer changes what to build and how fast. Decide it explicitly. #open-question
- **`unit-economics.md` is still priced at a $7.99/month mid case** that DEC-011 replaced with $99.99/year. Every correction runs in Waypoint's favor, so nothing is hidden, but the published tables understate the business and must not be quoted to an investor as they stand. Full re-run queued. #open
- **Minor-founder IP assignments are voidable**, and the two minors are the two the concept came from. Cure is guardian co-signature at formation plus re-execution within 30 days of each 18th birthday. Both dates belong in the diligence tracker the moment they are known. #risk
- **The stack is deliberately revisitable.** DEC-009 was approved "for now" with Claudio's standing instruction that infrastructure detail must not block product definition. Re-open it at any of its four named checkpoints (before the walking skeleton, when architecture design starts, at Aiven contract time, or if ops burden proves real) with a superseding DEC. #open
- Verify Garmin Connect writes into Health Connect before Android work begins (H6 verified for HealthKit only). #open-question
- ~~`api-integration-map.md` section 4 still names Supabase Auth~~ resolved 2026-08-06; sections 4.2 and 6.2 amended, and the Supabase rows in the master table and critical path replaced.
- Riskiest open assumption in the whole program: whether the home metro clears the OpenStreetMap pedestrian-data floor. The month-1 buildability spike answers it, and is now a **go-to-market gate**, not only a technical one (DEC-013). #open-question
- The launch override removed the quiet burn-in period, so the month-8 beta cohort target of 150 to 300 testers is now a **hard gate on the launch date**. #open
- The paid product rests entirely on one job. If training-state-aware generation is not felt value, there is no fallback paid thing at v1.x (DEC-011). #risk
- Verify a distinct Founding Runner SKU can carry its own 21-day introductory trial on both stores. A 30-minute check that prevents a launch-week surprise. #open-question
- ~~Blueprint example URL (premiumcuts-blueprint.vercel.app) was unreachable~~ resolved 2026-08-06; it fetched on retry and its structure informed the 17-section blueprint.
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
