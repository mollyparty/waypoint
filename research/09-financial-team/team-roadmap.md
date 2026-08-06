# Team Roadmap and Capacity Reconciliation

> Version-Timestamp: 2026-08-06 14:00:00 UTC-4
>
> **Read this document first in Phase 9.** It carries the finding that governs the phase, and it reopens [[DEC-010 Staged cross-platform MVP on React Native]].

## 1. The finding

The approved MVP is **29 to 31 person-months** of work, and [[DEC-010 Staged cross-platform MVP on React Native]] dates iOS at month 9 to 10 on a stated assumption of **2.5 to 3.0 full-time-equivalent people** (`../05-product/mvp-scope.md` section 7).

The actual team has **zero** full-time people. Two founders are in 10th grade. The third runs another business full-time.

Run the arithmetic honestly, with generous assumptions about AI leverage, and the full scope lands somewhere around **21 to 28 months**. The competitive window from Phase 1 is **12 to 18 months**. The full MVP does not fit inside it, and no amount of optimism closes a gap that size.

**This is not a reason to stop. It is a reason to ship something smaller.** The recommendation in section 5 is to make the walking skeleton the product rather than a milestone on the way to one, which lands a public launch at roughly month 12 to 14 and keeps Waypoint inside the window. The scope decision, not the funding decision, is the one that matters at this gate.

## 2. Who does what

Three founders, none full-time. Roles below are what each person owns, meaning accountable for the outcome rather than necessarily doing all the work.

### Asher, embedded user and testing lead

Co-originator of the concept. A real runner in the target segment, which is not a nice-to-have on this particular product.

- Owns real-world route testing: runs the generated routes, judges whether they are good, and reports why when they are not
- Subject matter expert on the customer, and the standing answer to "would a runner actually want this"
- Owns the Good Route Rate qualitative layer, the human counterpart to the eleven behavioral signals in `../06-business-model/metrics.md`
- Leads beta cohort recruitment through run clubs, where being a runner is the entire credential

**Why this is a real role and not a courtesy.** `../06-business-model/business-model-canvas.md` names bad routes as the failure mode Waypoint cannot survive, and `../05-product/mvp-scope.md` section 6 says outright that the real MVP risk is bad routes rather than missing features. Continuous, honest, unpaid route testing by a target-segment runner is a structural advantage most seed-stage teams buy expensively and get less of.

**The limit, stated plainly.** Asher is one runner in one city. `../03-users/unmet-needs.md` still carries an interview backlog of 12 to 18 conversations, and a founder-user does not close it. `blueprint/blueprint.md` states in a callout under the hero that zero user interviews have been conducted, and that remains true. An embedded user is a fast feedback loop, not a substitute for research.

### Claudio, project manager and operations

Co-originator. The elastic role: whatever the business needs that is not building.

- Owns the memory system, the research program, and the vault and graph discipline this repo runs on
- Owns project coordination: what happens next, what is blocked, what slipped
- Owns store operations: listing copy, screenshots, review responses, the Apple featuring nomination due at month 6 to 7 per DEC-013
- Owns GTM execution alongside Asher: Reddit and forum presence, run club logistics
- Absorbs quality assurance and release-management work that would otherwise land on Daniel

**Why this matters more than it sounds.** Every hour of non-engineering work Claudio absorbs is an hour returned to the only person who can write code. That is the highest-leverage thing anyone other than Daniel can do, and section 4 quantifies it.

### Daniel, technical and commercial lead

The execution engine, and the only adult.

- Owns the build entirely: architecture, code, infrastructure, the AI-agent workflow
- Owns product management and prioritization
- Owns business and brand development
- Holds every account requiring legal capacity: Apple, Play, banking, vendors (`legal-formation.md` section 5)
- Funds the AI tooling pre-formation

**This is a concentration risk and should be named as one.** If Daniel stops, Waypoint stops: there is no second builder, no second signatory, and no second person who can hold the Apple account. Investors will see this immediately, and `fundraising-plan.md` section 6 treats it as a real question rather than an awkward one. Two mitigations are available and cheap: document architecture decisions as they are made rather than after (that is what `vault/05-Architecture/` exists for), and get Claudio far enough into the codebase and the AI workflow that a bus factor of two is at least conceivable.

## 3. Available hours

The honest input, and the one everything else multiplies.

| Founder | Term-time hours/week | Summer hours/week | Constraint |
|---|---|---|---|
| Daniel | 12 to 20 (model 15) | 12 to 20 (model 15) | Runs another business full-time |
| Claudio | 8 to 14 (model 10) | 20 to 30 (model 25) | 10th grade, plus other responsibilities |
| Asher | 3 to 8 (model 5) | 8 to 15 (model 10) | 10th grade, narrower role |
| **Total** | **~30** | **~50** | |

A conventional full-time engineer is treated as 160 hours per month throughout, matching `../06-business-model/unit-economics.md` section 1.5.

Two adjustments matter before these numbers can be used.

**Only some of these hours are engineering hours.** Daniel's 15 is the only reliably technical block. Claudio's time is mostly coordination, operations and QA, though some is genuinely build-adjacent (store assets, test data, documentation, and with AI assistance, plausibly some real implementation). Asher's is testing and GTM, which does not burn down the person-month total but does prevent expensive mistakes.

**Part-time hours are worth less per hour than full-time hours.** Context reloading is real, particularly on a codebase touched twice a week. This is not pessimism, it is the standard reason part-time work does not scale linearly, and it argues for longer contiguous sessions over daily fragments.

Modeled engineering-equivalent capacity, after those adjustments:

| Period | Effective engineering hours/week | Per year |
|---|---|---|
| Term time (roughly 9.5 months/year) | ~20 | ~825 |
| Summer (roughly 2.5 months/year) | ~35 | ~380 |
| **Annual total** | | **~1,200 hours, or ~7.5 person-months/year** |

## 4. The AI leverage question

This is the load-bearing assumption of the whole plan and it deserves to be treated as such rather than waved at.

The claim being made is that AI-agent-assisted development lets one part-time builder deliver work that was scoped for two to three full-time engineers. Some of that claim is true. Not all of it is, and the part that is false is concentrated in exactly the work Waypoint is hardest on.

**Where AI leverage is large.** Conventional application surface: authentication flows, profile and settings screens, run history, list and detail views, form handling, store integration, test scaffolding, API client code, boilerplate, documentation. Waypoint has a lot of this.

**Where it is small.** Novel algorithmic work, systems integration debugging, platform-specific native modules, and anything requiring judgment about a domain the model has not seen much of. Waypoint's hard parts are all in this bucket: GraphHopper customization with crossing penalties, OpenStreetMap pedestrian-data ingestion and quality assessment, background geolocation across fragmented Android OEMs (`../05-product/dual-platform-strategy.md` section 3.8 budgets 1 to 1.5 person-months for OEM hardening alone), voice navigation timing, and the constraint solver at the center of the product.

Splitting the 29 to 31 person-months roughly 60 percent conventional and 40 percent hard, and applying different multipliers:

| Portion | Raw person-months | Multiplier | Effective |
|---|---|---|---|
| Conventional | ~18 | 2.5x | 7.2 |
| Hard | ~12 | 1.3x | 9.2 |
| **Total** | **~30** | **~1.8x blended** | **~16.4 person-months of human time** |

At 7.5 person-months of capacity per year, 16.4 person-months is **roughly 26 months**. Sensitivity:

| Blended multiplier | Effective person-months | Calendar at 7.5 pm/year |
|---|---|---|
| 1.3x (pessimistic) | 23.1 | **37 months** |
| 1.8x (modeled) | 16.4 | **26 months** |
| 2.5x (optimistic) | 12.0 | **19 months** |
| 4.0x (the marketing claim) | 7.5 | **12 months** |

**Even the optimistic case misses the competitive window.** Only the marketing claim fits, and no serious plan should be built on it.

Three honest notes on this table. The multiplier is [assumption] and it is the least validated number anywhere in this repo; nobody has measured this team on this codebase. It should be recalibrated against real data at the month-6 checkpoint, when the walking skeleton has produced actual evidence. And AI leverage on *review* and *debugging* is weaker than on *generation*, which matters because a part-time builder shipping AI-generated code they did not write line by line will spend proportionally more time on exactly those activities.

## 5. The recommendation: ship the skeleton

The gap cannot be closed by working harder or by raising money. It can be closed by shipping less.

`../05-product/mvp-scope.md` section 6 already defines the thing to ship, and describes its purpose in terms that make this recommendation almost self-evident: *"Its job is to make the core hypothesis testable with 20 to 50 TestFlight runners"* and *"the real MVP risk is bad routes, not missing features."*

The walking skeleton is one flow, fully working: **generate a route, run it with voice guidance, save the run.** It is 6 to 7 person-months of the original 22.75-point iOS scope, which scales to roughly **8 to 9 person-months** of the 29 to 31 React Native total.

### What v1 becomes

| Component | Raw pm | Rationale |
|---|---|---|
| Walking skeleton (`mvp-scope.md` section 6) | 8 to 9 | The core loop, unchanged |
| Privacy and compliance minimum | 2 to 3 | Not optional with location plus health data; the 15-item checklist in `../05-product/prd.md` |
| Public-launch hardening: onboarding, error states, store assets, crash triage | 2 to 3 | The gap between a TestFlight build and a public one |
| **v1 total** | **12 to 15** | |
| Effective after 1.8x leverage | **~7 to 8.5** | |
| **Calendar at 7.5 pm/year** | **~11 to 14 months** | |

Everything else in the 15-feature scope becomes post-launch iteration, prioritized by what real users do rather than by what was ranked before anyone had used the product. That is not a concession; `../05-product/rice-prioritization.md` ranked features against assumptions, and the skeleton replaces assumptions with behavior.

### What this deliberately does not cut

- **Safety-aware routing is not cut**, subject to the month-1 spike. It is the strongest-evidenced unmet need in `../03-users/unmet-needs.md`, the differentiation claim, and permanently free under DEC-011. If the spike fails, the documented GD-3 fallback applies: time-of-day and daylight heuristics with honest degradation.
- **Privacy architecture is not cut.** Private-by-default and home-area blurring are day-one items in the locked concept, and retrofitting privacy is both harder and less credible.
- **Honest refusal is not cut.** `../06-business-model/metrics.md` names honest-refusal-rate stability as the guardrail that matters most, precisely because quietly relaxing constraints is the easy way to fake quality.

### Android moves out

DEC-013 already made the iOS date the public launch. With v1 recut, Android moves to **month 20 to 26**, after iOS launch and retention proof. Keep the month-1 Play paperwork anyway, since it is a long-lead item that costs $25 and blocks nothing, and keep capturing the Android waitlist from launch as DEC-013 requires.

## 6. Re-derived schedule

Months counted from formation. This supersedes the DEC-010 dates and requires a superseding decision record.

| Months | Milestone | Notes |
|---|---|---|
| 1 to 2 | Formation, accounts, A3 safety-data spike | Spike is a go-to-market gate per DEC-013; D-U-N-S and Play verification start now |
| 3 to 8 | Walking skeleton to TestFlight | Was month 3 to 4 under DEC-010 |
| 6 to 8 | Interview priorities 1 and 2 (12 to 18 conversations) | Runs in parallel; Asher and Claudio lead |
| 8 to 10 | TestFlight cohort of 20 to 50 runners; route quality burn-in | The single most valuable period in the plan |
| 9 to 11 | Privacy and compliance package; counsel engaged | The $8k to $20k bill lands here |
| 10 to 11 | Apple featuring nomination filed | Roughly three months of lead time, per DEC-013 |
| 11 to 13 | Public-launch hardening; beta cohort to 150 to 300 | Hard gate on the launch date per DEC-013 |
| **12 to 14** | **iOS public launch, free** | Was month 9 to 10 under DEC-010 |
| 16 to 20 | Paid layer (TS-08 plus P-01), after week-4 retention clears 20 percent | GD-1 gate is unchanged |
| 20 to 26 | Android | Was month 10 to 12 |

**Against the competitive window.** Phase 1 estimates 12 to 18 months before Strava plausibly ships plan-linked route generation. A month 12 to 14 launch sits at the late end of that window. It is tight, and it is honest. The full-scope alternative at 21 to 28 months sits outside it entirely, which is the whole argument for cutting.

## 7. Seasonality

Two thirds of the team is on a school calendar, and pretending otherwise produces schedules that miss.

| Period | Capacity | Plan around it |
|---|---|---|
| September to December | Baseline | Steady build |
| Exam periods | **Near zero for Asher and Claudio** | Assume two dead weeks per semester. Do not schedule milestones into them |
| January to May | Baseline | Steady build |
| **June to August** | **Roughly double** | **Front-load the hardest work here.** The single biggest capacity block available |
| Daniel's other business | Unknown seasonality | Map it before finalizing the schedule. If it has a crunch period, it collides with the only engineering capacity there is |

If formation lands around September 2026, the summer 2027 block falls at roughly months 10 to 12: exactly the launch-hardening and beta-growth push. That is fortunate timing and the schedule above is deliberately built to use it.

**The college transition is the bigger seasonal event.** Asher and Claudio are in 10th grade, so college applications hit in late 2027 and 2028, and matriculation in 2029. Application season is a serious capacity hit, and matriculation changes everything about availability. This is precisely why `capital-structure.md` recommends vesting with a college-transition re-evaluation trigger: it is not a hypothetical, it is a scheduled event roughly three years out.

## 8. When to add someone

Adding a person means equity, not cash. The option pool in `capital-structure.md` section 5 exists for exactly this.

| Trigger | Add | Why |
|---|---|---|
| The month-6 checkpoint shows the AI multiplier below ~1.5x | A part-time contract engineer for the hard portion | The leverage assumption failed and the schedule is unrecoverable without help |
| The A3 spike passes but pedestrian-data work exceeds 3 person-months | A data or GIS contractor, scoped and time-boxed | Specialist work, poorly suited to general AI assistance, and on the critical path |
| Android work begins | An Android specialist for OEM hardening | 1 to 1.5 pm of OEM-specific debugging that AI assistance does not shorten much |
| Post-launch, retention clears the GD-1 bar | The first real hire, funded by a priced round | Traction changes what is affordable and what is raisable |

**Do not hire before the month-6 checkpoint.** There is no evidence yet about what this team can actually deliver, and hiring against an unmeasured assumption spends both money and equity on a guess.

## 9. The month-6 checkpoint

One date, one purpose: replace the guessed AI multiplier with a measured one.

Measure three things and nothing else. **Person-months of scope actually completed** against the 8 to 9 budgeted for the skeleton. **Effective multiplier**, computed as raw scope delivered divided by human hours spent. **Where the time actually went**, split between generation, review, debugging and integration, because that split predicts everything about the remaining work.

Then act on it:

| Measured multiplier | Action |
|---|---|
| Above 2.0x | Schedule holds. Consider restoring scope |
| 1.5x to 2.0x | Schedule holds. Change nothing |
| 1.2x to 1.5x | Cut scope further, or add a contract engineer from the pool |
| Below 1.2x | Stop and re-plan. The core strategic assumption failed and the plan needs rebuilding, not adjusting |

## 10. Assumptions

- [assumption] Available hours per founder per week, in section 3. Self-reported and untested against a real build.
- [assumption] The 1.8x blended AI multiplier. **The riskiest number in this phase**, and section 9 exists to replace it with evidence.
- [assumption] The 60/40 conventional-to-hard split of the scope. Directional, from reading the feature list against where AI assistance is known to be strong.
- [assumption] Part-time hours are worth less than full-time hours, applied as a haircut rather than a measured factor.
- [assumption] Walking skeleton at 8 to 9 person-months, scaled from the 6 to 7 in `mvp-scope.md` section 6 by the DEC-010 ratio.
- [assumption] Compliance minimum at 2 to 3 person-months. Not independently estimated.
- [verified] The 29 to 31 person-month scope, the 2.5 to 3.0 FTE assumption behind it, and the walking skeleton definition, all from `../05-product/mvp-scope.md` and DEC-010.
- [verified] The 12 to 18 month competitive window, from `../04-synthesis/positioning.md`.

## 11. Open questions

1. What is Daniel's other business's seasonality, and where does it collide with this schedule?
2. Can Claudio realistically take on implementation work with AI assistance, or is his contribution better spent entirely on absorbing non-engineering load? The answer moves the capacity number materially.
3. Are the modeled hours per week honest? Under-reporting produces a schedule everyone privately knows is fiction, which is worse than a slower schedule everyone believes.
4. What exactly does "public-launch hardening" contain? It is 2 to 3 person-months of the recut v1 and it is the least specified line in the estimate.

## Related

- `operating-model.md` for why time is nearly free in cash terms, which is what makes a longer schedule survivable
- `capital-structure.md` for vesting against these commitment levels and the college trigger
- `fundraising-plan.md` section 6 for how an investor reads a part-time team
- `../05-product/mvp-scope.md` sections 6 and 7 for the scope this document recuts
