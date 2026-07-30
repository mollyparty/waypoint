---
type: session
created: 2026-07-30
updated: 2026-07-30
tags: [session]
---

# Session 2026-07-30 - Research Program Kickoff and Founder Brief

## Goal

Lay the groundwork for the research-to-blueprint program: build the phased research infrastructure and capture Claudio's founding vision, so market, industry, user, and competitor research can run step by step toward an MVP definition and an investor-facing Business Blueprint.

## What was done

- Planned and got approval for a nine-phase gated research program (Phase 0 founder brief through Phase 8 Business Blueprint). Claudio's scoping choices: founder interview first, phase-gate approvals, HTML deliverables on Vercel, standard investor blueprint structure as fallback (his example URL was unreachable).
- Built `research/` scaffolding: `00-RESEARCH-PLAYBOOK.md` (phase specs, citation standard, confidence labels `[verified]`/`[inferred]`/`[assumption]`, definition-of-done gate checklist) plus `_index.md` per phase folder so any agent in any IDE can run a phase to the same standard.
- Ran the founder discovery interview. Key reveal: **the wedge is adaptive route generation**, not another training plan app. Core problem: runners in unfamiliar situations (vacation, travel) do not know where to run or how to get a routine fit to their body, schedule, and needs. Routes adapt to constraints: distance, elevation, humidity, street crossings, and more. Coaching layers on top. This reframes the competitive set (Komoot, Strava routes, Footpath now matter alongside Runna, TrainAsONE).
- Captured [[Founder-Brief]] with seven testable hypotheses (H1 to H7) and upgraded [[Charter]] from stub to draft: committed-amateur target user, iOS-first mobile app, venture-scale ambition, freemium subscription instinct, 12-month goal of MVP live with traction and seed round in motion.
- Recorded [[DEC-005 Phased research program with gated approvals]].
- Claudio approved the Phase 1 gate in-session. Ran Phase 1 with four parallel research agents; all four deliverables completed in `research/01-market/` (landscape, TAM-SAM-SOM, trends, regulatory). Key results distilled into [[Market Research Key Findings (Phase 1)]]: the route-generation whitespace is real and the enabling stack is nearly free, but H5 (venture scale) came back UNCERTAIN (wedge alone benchmarks to $5M to $30M ARR by year 5), the platform giants are commoditizing generic AI coaching, Garmin's developer program is paused (integration risk), and location privacy demands day-one privacy zones and private-by-default routes.
- Claudio approved the Phase 2 gate in-session. Ran Phase 2 with three parallel profile agents plus one synthesis agent: 14 deliverables in `research/02-competitors/` (10 profiles including route-side competitors added after Phase 1, adjacent platforms, feature matrix, pricing matrix, positioning maps, gap analysis). Distilled into [[Competitive Landscape Key Findings (Phase 2)]]: H2 SUPPORTED (zero of 15+ products accept weather, crossings, or safety as routing constraints or connect routes to training state), H3 SUPPORTED with a monetization caveat (route wedge acquires, adaptive layer monetizes), and the kill-shot threat is Strava connecting Runna's plan engine to its route generation (working window 12 to 18 months). Data enclosure means HealthKit-first personalization with a proprietary context-data moat.
- Claudio approved the Phase 3 gate in-session. Ran Phase 3 in two waves (pain mining plus segmentation/personas in parallel, then JTBD and unmet-needs synthesis): 5 deliverables in `research/03-users/`, distilled into [[User Research Key Findings (Phase 3)]]. The phase's strategic reframe: H1 PARTIALLY SUPPORTED; travel friction is frequent but the workaround economy mostly succeeds, so travel is the activation moment and demo story while safety-aware routing and home route novelty are the daily retention wedge. Four personas (Marcus, Priya, Elena, Jake); committed amateur confirmed as primary target with ambitious beginner secondary; consolidated interview backlog written; open founder decision flagged on whether safety routing must be free.

## Decisions made

- [[DEC-005 Phased research program with gated approvals]]

## Open threads

- Claudio's blueprint example (premiumcuts-blueprint.vercel.app) times out on fetch; retry during Phase 8, or Claudio shares its section list. #open-question
- Research dashboard Vercel deployment must have deployment protection enabled before deploy (confidential pre-launch research). #open-question
- Graphify hook quirk fired again on the scaffolding commit (AST-only rebuild, junk heading nodes); changes were discarded per the documented protocol and a proper update runs at session end.

## Next steps

1. Phase 1 gate is open: market and industry research (`research/01-market/`) awaits Claudio's go-ahead.
2. Then Phases 2 to 8 in sequence, each behind its gate per the playbook.

## Session-end checklist

- [x] This note completed
- [x] [[00-START-HERE]] updated
- [x] Graph updated (docs changed this session)
- [x] Committed with attribution footer and pushed to GitHub
