---
type: decision
id: DEC-013
status: accepted
created: 2026-08-06
updated: 2026-08-06
tags: [decision, gtm, launch, beachhead, phase-6]
---

# DEC-013 Home-metro beachhead and iOS-first public launch

## Context

`research/06-business-model/gtm-plan.md` concentrated go-to-market on one segment in one metro, and recommended splitting the launch: a quiet iOS release at month 9 to 10 for quality burn-in, with the Android date at month 10 to 12 carrying the public launch and the one-shot assets. Two calls were needed at the Phase 6 gate: which metro, and which date is the real launch.

## Decision

Approved 2026-08-06:

1. **Beachhead: the founder's home metro**, subject to the month-1 OpenStreetMap pedestrian-data buildability spike. The segment is the urban committed amateur running three to five times a week from a home doorstep, with women runners as the highest-intensity cohort and travelers as demo carriers rather than the target.
2. **The public launch is the iOS date at month 9 to 10**, not the Android date. The one-shot assets — press, creators, Product Hunt, and the Apple featuring nomination — are spent there. Android follows 4 to 8 weeks later as a second, smaller moment.

**This second call overrides the recommendation in `gtm-plan.md` section 5.1.** The reasoning for the override, and the conditions it creates, are recorded below rather than left implicit.

## Rationale

### The home metro

The founder must personally run these routes. Bad routes are the one failure mode this product cannot survive (`mvp-scope.md` section 2), and detecting them requires standing on the street, not reading a map. That is not delegable and not remote-doable, which makes the home metro correct unless the data fails. The month-1 spike is the check, and it runs before any marketing effort is committed.

### iOS as the public launch

The go-to-market plan's argument for the Android date was real: a mixed-platform run club is a bad room in which to tell half the people "not yet", and four to eight quiet weeks would buy a 4.5-plus rating and route-quality burn-in before the loud moment. Three considerations outweigh it.

1. **The most valuable one-shot asset is iOS-only anyway.** An Apple featuring nomination cannot be spent on an Android launch. Holding the whole launch for Android means either filing the nomination against a quiet release, which wastes it, or filing it months after the app has been public, which is a weaker submission. Spending it at a loud iOS launch is its natural home. The go-to-market plan underweighted this.
2. **Speed is a business requirement, not a preference.** The competitive window is an estimated 12 to 18 months, and the build already consumes ten. Landing the story four to eight weeks earlier is a material fraction of what remains, and the window is the reason DEC-010 chose a staged plan in the first place.
3. **iOS carries roughly 85 percent of category subscription revenue.** The audience whose behavior determines whether the paid layer works is on iOS. Getting them in earlier, and getting real retention telemetry from them sooner, is what the seed round will be raised on.

## Alternatives considered

- **Android date as the public launch** (the plan's recommendation). Rejected for the three reasons above, while accepting the costs named below.
- **Two equal launch moments.** Rejected: one-shot assets cannot be spent twice, and a "launch" that happens twice is a launch that lands neither time.
- **Another metro from the data-quality shortlist** (Seattle, Boston, New York, London). Held in reserve for the case where the month-1 spike shows the home metro fails the pedestrian-data floor.

## Consequences

The override removes the quiet burn-in period, which the plan was using to absorb three risks. Each now needs a compensating condition, and these are commitments, not suggestions:

1. **Route quality must clear its bar *before* launch, not during it.** The beta cohort now carries the entire load the quiet iOS weeks were going to carry. The month-8 target of 150 to 300 active testers becomes a hard gate on the launch date rather than a milestone to aim at. If the beta is thin, the launch slips; it does not proceed quietly. #risk
2. **Early reviews are formed in public.** Without a burn-in period there is no established 4.5-plus rating to launch into. Mitigation: seed genuine reviews from the beta cohort in the launch window, and hold the crash-free-sessions bar above 99.5 percent as a release gate.
3. **The mixed-platform run club problem is now live at launch.** Android runners in the beachhead metro will hear the pitch and be unable to install. Mitigation: capture them on an Android waitlist at every in-person event from the launch onward, and treat the Android release as a real second moment in the local community ("now on Android") even though the global one-shot assets are already spent. #risk
4. **The Apple featuring nomination must be filed at month 6 to 7**, given its roughly three-month lead time, so that it lands against the public launch.
5. **Android's long-lead paperwork keeps its month-1 start** (DEC-010). Nothing about this decision relaxes it; a late Android release is now a community-relations problem in the beachhead metro rather than merely a slipped date.

**Carried forward as the riskiest assumption in the program (A1):** whether the home metro clears the OpenStreetMap pedestrian-data floor. It sits underneath the segment choice, the metro choice, the top-ranked channel, and the differentiation claim. Consequently the month-1 buildability spike is **a go-to-market gate, not merely a technical one**, and its result should be treated as capable of changing the beachhead. #open-question

## Related

- `research/06-business-model/gtm-plan.md` (sections 1 and 5; section 5.1's recommendation is overridden here), `business-model-canvas.md`
- [[DEC-010 Staged cross-platform MVP on React Native]] (the staggered calendar this decision sequences)
- [[DEC-011 Pricing and the permanent free tier]]
- [[_Decision-Log]]
