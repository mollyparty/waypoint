---
type: decision
id: DEC-005
status: accepted
created: 2026-07-30
updated: 2026-07-30
tags: [decision, research, process]
---

# DEC-005 Phased research program with gated approvals

## Context

With the foundation in place, the project moves to discovery: market, industry, user, and competitor research culminating in an MVP definition and an investor-facing Business Blueprint (Claudio's reference example: premiumcuts-blueprint.vercel.app). The process must be runnable autonomously by any agent in any IDE, must never lose context between sessions, and must not cut corners or absorb unverified claims into conclusions.

## Decision

1. **Nine-phase gated pipeline.** Phase 0 (founder brief and infrastructure) through Phase 8 (Business Blueprint), specified in `research/00-RESEARCH-PLAYBOOK.md`. Each phase builds on the previous one and does not start until Claudio approves the prior phase's deliverables at a gate. The Phase 4 gate (concept lock) is the heaviest.
2. **Evidence standards.** Every claim cited (source, date, methodology for market numbers) and labeled `[verified]`, `[inferred]`, or `[assumption]`. Desk research is never presented as validated primary research.
3. **Founder Brief as hypothesis source.** Claudio's vision was captured in a structured interview ([[Founder-Brief]]) and framed as seven testable hypotheses (H1 to H7). Research confirms or kills them; Phase 4 delivers the verdict.
4. **Deliverable homes.** Research Markdown in `research/`, dashboard in `dashboard/`, blueprint in `blueprint/`. Key findings distilled into `vault/04-Knowledge/` so the graph and future sessions can reach them cheaply.
5. **Vercel for HTML deliverables** (Claudio's choice): research dashboard and investor blueprint deployed to Vercel. The research dashboard must have deployment protection enabled; pre-launch research is confidential.
6. **Version tags.** v0.2.0 after Phases 1 to 4, v0.3.0 after Phases 5 to 6, v0.4.0 after Phases 7 to 8.

## Rationale

- Phase gates were chosen over full autonomy (drift risk compounds across eight phases) and over per-document review (too slow); Claudio selected this explicitly.
- A written playbook makes the process tool-agnostic: any agent reads the playbook plus the phase index and can execute to the same standard, which is the same "one canonical file" principle as [[DEC-004 Continuous push and cross-IDE agent files]].
- Competitors are researched before users (Phase 2 before 3) because competitor app store reviews and community complaints are the richest desk-research proxy for user pain points.

## Alternatives considered

- **Fully autonomous end-to-end run**: rejected by Claudio; review debt at the end would be enormous.
- **In-repo-only HTML deliverables**: rejected by Claudio in favor of Vercel deployment; mitigated with deployment protection for the confidential dashboard.
- **Ad hoc research without a playbook**: rejected; it is exactly how corners get cut and context gets lost across tools.

## Consequences

- Each phase ends with the full memory routine (knowledge notes, session note, START-HERE, graph, push) before its gate; this is overhead, and it is the point.
- The premiumcuts example was unreachable at planning time; the blueprint structure falls back to a standard investor structure unless it becomes fetchable or Claudio shares its sections.

## Related

- [[_Decision-Log]]
- [[Founder-Brief]]
- [[DEC-004 Continuous push and cross-IDE agent files]]
