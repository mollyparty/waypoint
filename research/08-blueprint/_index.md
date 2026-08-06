# Phase 8: Business Blueprint

> Version-Timestamp: 2026-08-06 14:20:00 UTC-4

**Status: DRAFT COMPLETE, awaiting founder review.** Program catalog: `../00-PROGRESS.md`.

## Deliverables

| File | What it is | Status |
|------|-----------|--------|
| `blueprint/blueprint.md` | Master markdown, the citable source of truth. 17 sections | complete |
| `blueprint/index.html` | Investor-facing site: numbered sections, fixed nav, stat cards, risk matrix, print stylesheet | complete |
| Root `index.html` | Landing page updated, blueprint card now live | complete |
| CHANGELOG entry and **v0.4.0** tag | At founder approval | pending |

## Structure

Modeled on the example Claudio provided (`https://premiumcuts-blueprint.vercel.app/`), which fetched successfully on the retry. Adopted from it: numbered sections, a hero with headline stat cards, a fixed section navigator, and — the most valuable borrowing — a dedicated self-audit section covering known gaps, a validation sprint, and an explicit go / no-go.

Not adopted: the bilingual EN/ES toggle. The example serves a Dominican market; Waypoint's investor audience is English-first, and a half-built translation would read worse than none. Easy to add later if the audience changes.

**Seventeen sections:** executive summary · the problem · market opportunity · competitive landscape · the product · who it is for · business model · unit economics · go-to-market · measurement · technology · execution timeline · capital and team · risk analysis · legal and privacy · what we do not know · appendix and sources.

## Editorial stance

The blueprint invents nothing. Every figure traces to a research document, and the confidence tags survive into the investor-facing text rather than being laundered into false precision. Three findings that a less honest document would have buried are instead given their own emphasis:

1. **H5 came back UNCERTAIN.** The route wedge alone models to $5M to $30M ARR, which is not a venture outcome. Section 03 argues four expansion paths and names the tests that would resolve it.
2. **Zero user interviews have been conducted.** Stated in a callout directly under the hero, not in an appendix.
3. **Unit economics depend on distribution, not pricing.** Paid acquisition returns 53 to 70 cents on the dollar, so the community-first plan is load-bearing arithmetic.

The reasoning: an investor discovers all three in diligence anyway, and discovering them in diligence is much worse than reading them on page one.

## Open items for founder review

- [ ] The capital requirement (~$350k to $400k pre-seed) is **derived, not decided**. No decision record covers the raise. Section 13 shows the arithmetic so it can be argued with.
- [ ] Whether to publish the blueprint to a **separate public Vercel project**. This repo's project stays confidential per [[DEC-007 Vercel publishing pipeline with protected previews]], so an investor-facing URL needs its own deployment with its own protection posture.
- [ ] Whether an EN/ES edition is wanted.
- [ ] Two source documents disagree on Runna's ARR ($40M vs ~$10M implied). The blueprint sidesteps it by citing the payer count both agree on, but the underlying conflict in `02-competitors/gap-analysis.md` and `01-market/market-sizing.md` is still unresolved.

## Access

- Local: open `blueprint/index.html`
- Protected preview: https://waypoint-git-main-mollypartys-projects.vercel.app/blueprint/
