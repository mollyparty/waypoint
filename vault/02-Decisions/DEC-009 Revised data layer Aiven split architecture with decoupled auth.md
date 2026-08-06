---
type: decision
id: DEC-009
status: accepted
created: 2026-08-06
updated: 2026-08-06
tags: [decision, stack, database, security, compliance, phase-5]
---

# DEC-009 Revised data layer: Aiven split architecture with decoupled auth

## Context

DEC-008 approved the MVP scope but explicitly **held** the stack, because Claudio was not convinced Supabase was the right foundation and asked whether something more secure, stable, reliable, and compliant existed. Round 1 (`research/05-product/stack-validation.md`) had answered a narrower question ("is Supabase good enough?": yes, with conditions) without ever putting EU-incorporated managed-Postgres specialists on the table. Round 2 (`research/05-product/database-deep-dive.md`) scored 12 candidates against Claudio's four pillars, weighted Security 25 / Reliability 20 / Compliance 20 / Stability 15, plus PostGIS 10, Ops 5, Cost 5.

## Decision

**Supabase is replaced by a split data architecture**, approved 2026-08-06:

1. **Personal data** (accounts, entitlements, consent ledger, privacy-zone geometries): **Aiven for PostgreSQL**, EU region. Single node at MVP, Business HA with a synchronous standby before public launch. Firewall allowlisted to the application server's IP only.
2. **Geospatial moat** (OSM-derived layers, lighting and crossing scores): **self-managed Postgres + PostGIS on the Hetzner private network**, no public IP, no personal data, pgBackRest to off-provider object storage, quarterly restore drills.
3. **Authentication**: **decoupled into Waypoint's own API layer via Better Auth**, with identity tables living in the Aiven Postgres so identity inherits EU data residency.

Unchanged from earlier rounds: Postgres + PostGIS as the engine, self-hosted GraphHopper on Hetzner compute, RevenueCat for subscriptions, and the on-device wall for health data.

## Rationale

- Aiven scored **4.46 of 5** against Supabase's **3.45** on the founder's own weighting. It is EU-incorporated (Finland), carries ISO 27001 and SOC 2 Type II, runs dedicated VMs, operates a Bugcrowd bounty, and offers a credit-backed 99.99 percent SLA with point-in-time recovery as standard. That is the cleanest available answer to the Schrems II / EU data-residency question, which matters because Waypoint's data is location history.
- Decoupling auth **deletes** round 1's single hardest exit problem (Supabase Auth lock-in) rather than merely containing it. Once auth and client-side database access are gone, Supabase's remaining bundle is precisely the set of features Waypoint's security posture would switch off anyway.
- Splitting the stores matches their actual risk profiles: the moat database is large, rebuildable in hours, and holds nothing personal; the personal-data store is small, precious, and compliance-bearing. Separating them shrinks both the DPIA surface and the blast radius of any single compromise.

## Alternatives considered

- **Supabase with round 1 conditions**: workable, and it keeps developer velocity high, but it loses on every pillar to Aiven and leaves auth lock-in as a standing exit cost. Rejected.
- **Crunchy Bridge (4.25)**: the best US specialist security engineering, but a US entity now owned by Snowflake (June 2025), which reintroduces the CLOUD Act exposure the EU choice removes.
- **Google Cloud SQL Enterprise Plus (4.13)**: technically excellent, but US CLOUD Act plus the operational cost of adding a second cloud.
- **OVHcloud managed Postgres (4.10)**: the named **runner-up**, and the coherent choice if the OVH compute fallback ever executes (shared vRack). Priced down by the 2021 Strasbourg fire and the subsequent backup court rulings.
- **Fully self-managed Postgres on Hetzner for everything**: strongest security score (zero public exposure) but only 3.0 on reliability at solo-founder scale. Adopted for the moat only, where that trade is correct.

## Consequences

- Two managed relationships instead of one: an Aiven contract and DPA plus a self-managed PostGIS box to patch and back up. Ops burden is higher than Supabase's; the mitigation is that the self-managed half holds nothing irreplaceable. #risk
- Auth is now Waypoint's own responsibility. Better Auth must be hardened per the conditions in the deep dive (the three 2026 CVEs were in plugins Waypoint does not need). Ory Kratos remains the security-maximal fallback if self-owned auth proves heavier than expected. #risk
- Estimated ~$80 to $120 per month for Aiven at MVP (tier is assumption A15 in the deep dive, to confirm at contract time), plus roughly 0 to 30 EUR per month for the moat box.
- `research/05-product/api-integration-map.md` section 4 still names Supabase Auth for sign-in; it was written before this verdict and must be read as "the auth layer" (Better Auth).

## Revisit clause (explicit founder instruction)

Claudio approved this **for now**, with the standing instruction that infrastructure detail must not block product definition. **This decision is deliberately revisitable.** Re-open it, with a superseding DEC, at any of these checkpoints:

1. **Before the walking skeleton is built** (month 3 to 4): the last cheap moment to change data-layer shape.
2. **Whenever architecture design starts in earnest** (`vault/05-Architecture/`), if the detailed design surfaces a requirement these studies did not anticipate.
3. **At Aiven contract time**, if the real quoted tier or DPA terms differ materially from the assumptions above.
4. **If ops burden proves real**: two databases plus self-owned auth is the cost of this choice; if it is eating founder time that route quality needs, consolidating is a legitimate pivot, not a failure.

Nothing here is load-bearing for Phase 6 economics beyond the monthly cost line, which is a rounding error against store commissions.

## Related

- `research/05-product/database-deep-dive.md` (full scoring matrix and sources)
- `research/05-product/stack-validation.md` (round 1, superseded on the data layer)
- [[DEC-008 Phase 5 gate MVP approved stack in validation]]
- [[DEC-010 Staged cross-platform MVP on React Native]]
- [[_Decision-Log]]
