# Operating Model, Overhead and Burn Rate

> Version-Timestamp: 2026-08-06 14:00:00 UTC-4
>
> Supersedes the $15,000/month operating base and the $230,000 cash build in `../06-business-model/unit-economics.md` sections 1.4 and 1.5, both of which were derived from a solo-founder-plus-contractors team that does not exist.

## 1. The headline

**Monthly burn is roughly $400 during the build, not $15,000.** That is a reduction of about 97 percent against the model eight phases of research were resting on.

| Model | Monthly operating cost | Cash to reach launch |
|---|---|---|
| Previous (`unit-economics.md` 1.4, 1.5) | ~$15,000 | ~$230,000 |
| **Actual, this team** | **~$400** | **~$12,000 to $18,000** |

The reason is not cleverness. It is that the two largest line items in any early software budget, salaries and contractors, are both zero. Nobody draws pay. Nobody is hired. What remains is subscriptions, servers, store fees, and one legal bill.

**This is good news that comes with a trap, and the trap is the more important half.** Cheap burn means there is no financial forcing function, no month where the money runs out and a decision gets made. The constraint moved rather than disappeared: it is now the founders' available hours, which cannot be bought back at any price. `team-roadmap.md` is where that gets confronted. This document only establishes what things cost.

## 2. Overhead by category

Prices verified 2026-08-06 unless marked otherwise.

### 2.1 AI tooling, the largest controllable line

The build strategy is AI-agent-assisted development instead of hiring, so this line is not overhead in the ordinary sense. It is the engineering budget.

| Tool | Tiers | Note |
|---|---|---|
| Cursor | Hobby free / Pro $20 / Pro+ $60 / Ultra $200 per month | Annual billing takes 20 percent off. Cursor's own docs put daily agent users in the $60 to $100 range [verified] |
| Claude | Pro $20 (or $17 billed annually) / Max 5x $100 / Max 20x $200 per month | Includes Claude Code [verified] |
| ChatGPT | Plus $20 / Pro $200 per month | OpenAI guidance puts typical Codex usage at $100 to $200 per developer per month [verified] |

**Recommended combination: Cursor Pro+ at $60 plus Claude Max 5x at $100, for $160 per month.** [inferred]

The reasoning. Only one person is building, so this is one seat, not three. The two tools are complementary rather than redundant, since Cursor is the IDE accelerator and Claude Code is the terminal agent, and the work here spans both shapes. Starting at the $200 Ultra and Max 20x tiers is premature at a stage where nobody yet knows the actual consumption rate; the honest move is to start at $160, watch for a month, and escalate on evidence. Escalating is instant, and over-buying for six months is $480 wasted for nothing.

**Watch the metering.** Every one of these tiers is a prepaid credit pool metered against model API rates, not an unlimited licence. Once the pool is exhausted the marginal token cost is real. Budget **$50 per month of expected overage** and treat a sustained overage above that as the signal to move up a tier rather than bleed. [inferred]

### 2.2 Infrastructure

From `../05-product/api-integration-map.md` section 8 and `../06-business-model/unit-economics.md` section 1.1, which is the authoritative post-DEC-009 source. See section 5 below for why two different totals exist in the repo.

| Stage | Monthly | What is running |
|---|---|---|
| Pre-build | **$0 to $25** | Nothing but a routing VM if the month-1 spike needs one |
| Build, pre-users | **$40 to $80** | Hetzner routing VM ~$25, a minimal Aiven tier, domain and email |
| Beta, 20 to 300 testers | **$80 to $150** | Full data layer per DEC-009, Sentry free tier, TelemetryDeck free tier |
| Launch, ~1k MAU | **$135 to $255** (mid $195) | `unit-economics.md` 1.1 |
| 10k MAU | **$540 to $770** (mid $655) | Same source. Add 15 percent store commission and RevenueCat ~1.4 percent of net once revenue starts |

### 2.3 Store and developer programs

| Item | Cost | Timing |
|---|---|---|
| Apple Developer Program | $99/year (~$8/month) | Before TestFlight, so month 1 to 2 |
| Google Play Console | $25 one-time | Month 1, because verification is a long-lead item |
| D-U-N-S number | $0 | Free, up to 14 business days |

### 2.4 Formation and legal

| Item | Cost | Timing |
|---|---|---|
| Incorporation, agent, counsel, minor-founder structure | **$5,000** modeled, range $3,300 to $9,000 | One-time, month 1 to 2. Composition in `legal-formation.md` section 7 |
| Delaware franchise tax | $175 to $450/year | Annual, from year two |
| Accounting and bookkeeping | $0 to $100/month | A pre-revenue company with one bank account needs very little. Rises at revenue |
| Privacy counsel: ODbL, DPIA, terms, DPAs | $8,000 to $20,000 | **Deferred until pre-launch.** Real and unavoidable given location plus health data, but it does not gate the build. See section 4 |

### 2.5 Design, devices and everything else

| Item | Cost | Note |
|---|---|---|
| Brand and UI design | $0 to $8,000 | Daniel covers brand development. Budget a contract designer only if the store listing needs it |
| Test devices | $500 to $3,000 | Android fragmentation is the real driver. Buy used, buy late, buy the OEMs that actually fail |
| Domain, email, misc tooling | $20 to $40/month | Resend is free to 3,000 emails/month |
| GTM cash | $0 to $800/month | Already modeled in `../06-business-model/gtm-plan.md` section 0. Effectively $0 until month 6 |

## 3. The burn table

Four stages. Figures are monthly unless marked one-time.

| Line | Stage 1: Formation (mo 1 to 2) | Stage 2: Build (mo 3 to 18) | Stage 3: Beta and launch | Stage 4: Post-launch, ~1k MAU |
|---|---|---|---|---|
| AI tooling | $160 | $160 | $160 | $160 |
| AI overage allowance | $50 | $50 | $50 | $50 |
| Infrastructure | $0 to $25 | $40 to $80 | $80 to $150 | $135 to $255 |
| Apple Developer Program | $8 | $8 | $8 | $8 |
| Domain, email, tooling | $30 | $30 | $30 | $40 |
| Accounting | $0 | $0 | $50 | $100 |
| GTM cash | $0 | $0 to $100 | $200 to $800 | $200 to $800 |
| **Recurring monthly** | **~$260** | **~$300 to $430** | **~$580 to $1,250** | **~$700 to $1,415** |
| **Modeled monthly** | **$260** | **$400** | **$900** | **$1,050** |
| One-time this stage | Formation $5,000, Play $25 | Devices $500 to $3,000 | Privacy counsel $8,000 to $20,000 | — |

### Cash to reach launch

| Item | Low | Modeled | High |
|---|---|---|---|
| Formation and legal (one-time) | $3,300 | $5,000 | $9,000 |
| Play Console (one-time) | $25 | $25 | $25 |
| Stage 1, 2 months | $520 | $520 | $600 |
| Stage 2, 16 months | $4,800 | $6,400 | $6,880 |
| Test devices | $500 | $1,500 | $3,000 |
| Contingency at 15 percent | $1,371 | $2,017 | $2,926 |
| **Total to launch** | **$10,516** | **$15,462** | **$22,431** |

**Call it $12,000 to $18,000 to get a product into the App Store**, excluding the privacy counsel bill, which is treated separately in section 4 because its timing is genuinely optional and its size is not.

Stage 2 is modeled at 16 months rather than the 8 to 10 in `../05-product/mvp-scope.md` section 7 because that schedule assumed 2.5 to 3.0 full-time-equivalent people. `team-roadmap.md` section 5 derives the real one. Note how little the burn cares: sixteen months of build costs $6,400, and even a 24-month build only adds $3,200. **Time is nearly free in cash terms here, which is precisely why the calendar has to be managed on other grounds.**

## 4. The privacy counsel bill, treated honestly

`../06-business-model/unit-economics.md` section 1.5 budgets $8,000 to $20,000 for counsel covering the ODbL boundary, a DPIA, privacy policy, terms, and data processing agreements. That figure is not padding. Waypoint handles precise location plus health data, `../05-product/prd.md` carries a 15-item MVP compliance checklist, and DEC-009 put personal data in the EU specifically for the regulatory posture.

It is **excluded from the launch cash figure above** because it does not gate the build. A walking skeleton in TestFlight with 20 to 50 known testers does not need the full public-launch legal package. It absolutely is needed before a public App Store launch.

Two consequences worth stating plainly:

1. **The largest single expense in this plan is legal, not engineering.** Once salaries and contractors are removed, the privacy package alone is more than everything else combined.
2. **This is the strongest argument for raising something rather than nothing.** A $50,000 round covers the whole thing with room left over. Bootstrapping means either finding the money at month 15 or shipping with an inadequate legal position, which for a location plus health product is not an acceptable risk.

## 5. Reconciling three cost conflicts in the existing research

The audit found three places where the repo quotes conflicting figures for the same thing. Left alone they would propagate into this model. Resolved here, with the reason.

### 5.1 Infrastructure at MVP: $135 to $255 versus $80 to $130

| Source | Figure | Verdict |
|---|---|---|
| `unit-economics.md` 1.1 | $135 to $255/month at ~1k MAU | **Authoritative** |
| `api-integration-map.md` 8.2 | $80 to $130/month | Superseded |

The Phase 5 rollup was summed before DEC-009 replaced Supabase, which cost $25/month, with the Aiven plus self-managed PostGIS split, which costs $80 to $150. `unit-economics.md` applied that correction; the integration map's total line did not, although its master table row 25 does carry the corrected figure. **Use $135 to $255.** The integration map's per-service table remains correct and useful; only its section 8.2 total is stale.

### 5.2 Net revenue multiplier: 80.88 percent versus 84 percent

| Source | Figure | Composition |
|---|---|---|
| `unit-economics.md` 1.3 | **0.8088** | 15 percent store commission, RevenueCat ~1.4 percent of net, 3.5 percent refund allowance |
| `revenue-model.md` 6.2 | 0.84 | Store commission and a rounding |

**Use 0.8088.** It is the one that shows its work and the one that includes refunds, which are not optional. The revenue model's phasing figures are therefore about 4 percent optimistic; that is within the noise of everything else in those projections, but the correct multiplier should be used in any new calculation.

### 5.3 The unit-economics tables are priced at the wrong price

`../06-business-model/unit-economics.md` was written against a $4.99 to $11.99 monthly scenario band and centers its sensitivity tables on a **$7.99/month mid case**. [[DEC-011 Pricing and the permanent free tier]] subsequently locked **$99.99/year and $12.99/month**. The document flags this against itself in its own open questions, which is to its credit, but the flag was never actioned.

The practical effect on the figures most often quoted:

| Figure | As published (at $7.99 mid) | At the locked price | Direction |
|---|---|---|---|
| Base LTV | $86 | Roughly $107 to $115 | Better |
| Gross margin at 10k MAU, 3 percent conversion | 63 percent | Roughly 70 percent | Better |
| Break-even paying subscribers | ~2,985 against $15k/month | See 5.4 | Much better |
| Organic share needed for 3:1 | ~90 percent | ~84 percent | Better |

Every correction runs in Waypoint's favor, so nothing here rescues a broken model or hides a problem. But **the published numbers understate the business and should not be quoted to an investor as they stand.** A full re-run of those tables at $99.99 is queued as an open item rather than done here, because this document's job is the cost side.

### 5.4 What break-even actually is now

The most consequential correction in the whole phase.

`unit-economics.md` section 8.1 puts operating break-even at roughly **3,000 paying subscribers**, and the blueprint repeats it. That figure is $15,000 of monthly fixed cost divided by contribution per subscriber. With fixed cost at $1,050 per month instead:

| Input | Old | New |
|---|---|---|
| Monthly operating base | $15,000 | $1,050 |
| Net revenue per annual subscriber | $80.87 ($99.99 × 0.8088) | Same |
| Less allocated infrastructure | ~$2.20/month at 3 percent conversion | Same |
| Contribution per subscriber per year | ~$54 | Same |
| **Paying subscribers to break even** | **~3,000** | **~235** |

**Roughly 235 paying subscribers, not 3,000.** At a 3 percent conversion rate that is about 7,800 free active users. For scale, `../06-business-model/revenue-model.md` section 6.2 models 480 subscribers in the base case by month 12 of revenue.

The honest caveats, because this number is too good to state without them. It counts no founder compensation at all, so it is a break-even on cash out the door and not on the true cost of the work. It excludes the one-time privacy counsel bill. And it holds only while the team stays unpaid, which is by definition temporary; the day anyone takes a salary it moves sharply. **What it genuinely means is that Waypoint reaches self-sustaining operation at a scale roughly one order of magnitude smaller than the research assumed.** That changes the strategic picture more than any other number in this phase.

## 6. Who is paying today, and why that must change

Daniel is currently funding the AI tooling personally. That is normal pre-formation and it must not persist past formation, for three reasons: those subscriptions are a company expense and should sit on the company's books for tax and diligence purposes; untracked founder spend becomes an awkward conversation later about who put in what; and a cap table conversation is much cleaner when contributions are documented.

**Recommendation.** Log every pre-formation contribution now, with date and amount, however small. At formation, either reimburse from the round proceeds or record it explicitly as a documented founder contribution. Do not leave it informal. `capital-structure.md` section 6 covers how cash contribution interacts with the equity split, and the short version is that it should be handled as reimbursement or a note rather than by adjusting percentages, because a few thousand dollars of tooling should not buy meaningful ownership in a company that intends to be worth something.

## 7. Thirty-six month projection

Revenue phasing from `../06-business-model/revenue-model.md` section 6, corrected to the 0.8088 multiplier and the locked $99.99 price. Months are counted from formation. This projection assumes the re-derived schedule in `team-roadmap.md` section 5, not the DEC-010 dates.

| Period | Stage | Monthly burn | Cumulative cash out | Revenue | Net position |
|---|---|---|---|---|---|
| Months 1 to 2 | Formation | $260 + $5,025 one-time | ~$5,545 | $0 | Funded by the round |
| Months 3 to 18 | Build | $400 | ~$13,445 | $0 | Round covers it |
| Months 19 to 21 | Beta | $900 | ~$16,145 | $0 | Privacy counsel lands here: +$8k to $20k |
| Months 22 to 24 | Launch, free | $1,050 | ~$27,295 to $39,295 | $0 | v1 is free by DEC-008 |
| Months 25 to 30 | Paid layer live | $1,050 | ~$33,595 to $45,595 | Ramping to ~$2,400/mo net | Approaching break-even |
| Months 31 to 36 | Growth | $1,200 | ~$40,795 to $52,795 | ~$3,200 to $9,600/mo net | **Break-even crossed** |

Read the last column and the shape of this business becomes clear: **total cash consumed over three years is roughly $40,000 to $53,000.** A $50,000 friends-and-family round funds the entire path to self-sustaining operation, with the privacy counsel bill as the only line that could force a second raise, and even that only at the top of its range.

That is the case for raising **something small now rather than something large later**, and it is a genuinely different company from the one described in `blueprint/blueprint.md` section 13.

## 8. Assumptions

- [assumption] AI tooling at $160/month with $50 overage is sufficient for one builder. Unvalidated: nobody has measured this team's actual consumption. Revisit after two months of real usage.
- [assumption] AI-assisted development delivers the scope at all. This is a capacity question, not a cost question, and `team-roadmap.md` section 4 treats it properly. If it fails, cash requirements revert toward the contractor model.
- [assumption] Formation at $5,000 including the minor-founder premium. Not quoted by an actual firm.
- [assumption] The privacy package at $8,000 to $20,000, inherited from `unit-economics.md` 1.5. Also not quoted.
- [assumption] No founder takes cash compensation for 36 months. This is the load-bearing assumption of the entire model and it is a real cost being borne by real people, not a saving.
- [assumption] The 36-month revenue ramp inherits `revenue-model.md` section 6, which itself depends on install volume at the paywall date, the single largest source of variance in that model (a 15x spread across its scenarios).
- [verified] All AI tooling, Apple, Play and infrastructure unit prices, sourced as cited.

## 9. Open questions

1. What is this team's actual monthly AI token consumption? Answerable with two months of data, and it moves the largest controllable line.
2. Do the founders want to reimburse Daniel's pre-formation spend from the round, or record it as a contribution? (`capital-structure.md` section 6.)
3. Can the privacy counsel package be staged, with a smaller TestFlight-scope engagement first and the full public-launch package later?
4. Should the unit-economics tables be fully re-run at the locked $99.99 price, or is the directional correction in section 5.3 sufficient for now?

## Related

- `team-roadmap.md` for the capacity constraint that replaced the money constraint
- `fundraising-plan.md` for how the $50,000 gets raised
- `legal-formation.md` section 7 for the formation cost composition
- `../06-business-model/unit-economics.md` for everything on the revenue side, which this document does not supersede
