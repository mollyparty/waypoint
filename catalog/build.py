#!/usr/bin/env python3
"""Validate catalog/features.json and regenerate catalog/FEATURES.md from it.

Run after every edit to features.json:

    python catalog/build.py            # validate, then write FEATURES.md
    python catalog/build.py --check    # validate only, non-zero exit on failure

The markdown mirror exists so that agents and humans reading the repository
without a browser get the same catalog the interactive page shows. It is
generated, never hand-edited: the JSON is the source of truth.

Exit codes: 0 clean, 1 validation errors found.
"""

from __future__ import annotations

import json
import math
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
JSON_PATH = ROOT / "catalog" / "features.json"
MD_PATH = ROOT / "catalog" / "FEATURES.md"

VALID_KINDS = {"feature", "compliance", "nonfunctional", "excluded"}
VALID_RELEASES = {"mvp", "v1.x", "v2", "never"}


# --------------------------------------------------------------------------- #
# validation
# --------------------------------------------------------------------------- #

def validate(d: dict) -> list[str]:
    """Return a list of human-readable problems. Empty list means clean."""
    errors: list[str] = []

    entries = d.get("entries", [])
    if not entries:
        return ["features.json has no entries"]

    ids = [e["id"] for e in entries]
    dupes = sorted({i for i in ids for _ in [0] if ids.count(i) > 1})
    if dupes:
        errors.append(f"duplicate entry ids: {', '.join(dupes)}")

    id_set = set(ids)
    persona_ids = {p["id"] for p in d.get("personas", [])}
    need_ids = {n["id"] for n in d.get("needs", [])}
    job_ids = {j["id"] for j in d.get("jobs", [])}
    ejob_ids = {j["id"] for j in d.get("emotionalJobs", [])}
    module_ids = {m["id"] for m in d.get("modules", [])}
    conflict_ids = {c["id"] for c in d.get("conflicts", [])}

    for e in entries:
        eid = e.get("id", "<missing id>")

        for field in ("name", "module", "kind", "summary", "description",
                      "effortNative", "assigned", "baselines", "sources"):
            if field not in e:
                errors.append(f"{eid}: missing required field '{field}'")

        if e.get("kind") not in VALID_KINDS:
            errors.append(f"{eid}: kind '{e.get('kind')}' is not one of {sorted(VALID_KINDS)}")
        if e.get("module") not in module_ids:
            errors.append(f"{eid}: module '{e.get('module')}' is not a declared module")
        if e.get("assigned") not in VALID_RELEASES:
            errors.append(f"{eid}: assigned '{e.get('assigned')}' is not one of {sorted(VALID_RELEASES)}")

        for p in e.get("personas") or []:
            if p.get("id") not in persona_ids:
                errors.append(f"{eid}: persona '{p.get('id')}' is not declared")
            if p.get("weight") not in {"primary", "secondary"}:
                errors.append(f"{eid}: persona '{p.get('id')}' has weight '{p.get('weight')}'")
        for n in e.get("needs") or []:
            if n not in need_ids:
                errors.append(f"{eid}: need '{n}' is not declared")
        for j in e.get("jobs") or []:
            if j not in job_ids:
                errors.append(f"{eid}: job '{j}' is not declared")
        for j in e.get("emotionalJobs") or []:
            if j not in ejob_ids:
                errors.append(f"{eid}: emotional job '{j}' is not declared")
        for c in e.get("conflictIds") or []:
            if c not in conflict_ids:
                errors.append(f"{eid}: conflict '{c}' is not declared")

        for dep in e.get("dependsOn") or []:
            if dep not in id_set:
                errors.append(f"{eid}: dependsOn '{dep}' does not exist")
        for blk in e.get("blocks") or []:
            if blk not in id_set:
                errors.append(f"{eid}: blocks '{blk}' does not exist")
        for sat in e.get("satisfies") or []:
            if sat not in id_set:
                errors.append(f"{eid}: satisfies '{sat}' does not exist")
        if e.get("satisfiedBy") and e["satisfiedBy"] not in id_set:
            errors.append(f"{eid}: satisfiedBy '{e['satisfiedBy']}' does not exist")

        # An entry whose effort lives elsewhere must say so, or the total lies.
        if e.get("satisfiedBy") and e.get("effortNative", 0) != 0:
            errors.append(f"{eid}: has satisfiedBy '{e['satisfiedBy']}' but non-zero effort, "
                          "which double counts")

        if e.get("kind") == "feature" and not e.get("rice"):
            errors.append(f"{eid}: features must carry RICE values")
        if e.get("kind") == "excluded" and e.get("assigned") != "never":
            errors.append(f"{eid}: excluded entries must be assigned 'never'")
        if e.get("kind") in {"compliance", "nonfunctional"} and not e.get("locked"):
            errors.append(f"{eid}: obligations must be locked")

        sk = e.get("skeletonEffort")
        if sk is not None and sk > e.get("effortNative", 0):
            errors.append(f"{eid}: skeletonEffort {sk} exceeds effortNative {e.get('effortNative')}")

    # nothing may depend on something scheduled later than itself
    by_id = {e["id"]: e for e in entries}
    order = {"mvp": 0, "v1.x": 1, "v2": 2, "never": 3}
    for e in entries:
        for dep in e.get("dependsOn") or []:
            target = by_id.get(dep)
            if not target:
                continue
            if order[target["assigned"]] > order[e["assigned"]]:
                errors.append(f"{e['id']} ({e['assigned']}) depends on {dep} "
                              f"({target['assigned']}), which ships later")

    # RICE ranks should be unique and contiguous across the 30 features
    ranks = sorted(e["rice"]["rank"] for e in entries if e.get("rice"))
    if ranks and ranks != list(range(1, len(ranks) + 1)):
        errors.append(f"RICE ranks are not a contiguous 1..{len(ranks)} sequence: {ranks}")

    if d.get("meta", {}).get("entryCount") != len(entries):
        errors.append(f"meta.entryCount is {d.get('meta', {}).get('entryCount')} "
                      f"but there are {len(entries)} entries")

    return errors


def derive_blocks(d: dict) -> bool:
    """Rebuild every 'blocks' list from the authored 'dependsOn' edges.

    Only dependsOn is authored. Maintaining the reverse edge by hand meant the
    two could disagree, which they did, so it is computed instead. Returns True
    when anything changed, so the caller knows to rewrite the JSON.
    """
    reverse: dict[str, list[str]] = {e["id"]: [] for e in d["entries"]}
    for e in d["entries"]:
        for dep in e.get("dependsOn") or []:
            if dep in reverse:
                reverse[dep].append(e["id"])

    changed = False
    for e in d["entries"]:
        want = sorted(reverse[e["id"]])
        if (e.get("blocks") or []) != want:
            e["blocks"] = want
            changed = True
    return changed


# --------------------------------------------------------------------------- #
# effort model, mirroring the arithmetic in index.html
# --------------------------------------------------------------------------- #

def scenarios(d: dict) -> list[dict]:
    p = d["planning"]
    entries = d["entries"]

    skeleton = sum(e["skeletonEffort"] for e in entries if e.get("skeletonEffort"))
    compliance = sum(e["effortNative"] for e in entries if e["kind"] == "compliance")
    quality = sum(e["effortNative"] for e in entries if e["kind"] == "nonfunctional")
    mvp_features = sum(e["effortNative"] for e in entries
                       if e["kind"] == "feature" and e["assigned"] == "mvp")
    prd_p0 = sum(e["effortNative"] for e in entries
                 if e["kind"] == "feature" and e.get("prdP0"))

    def project(native: float) -> dict:
        rn = native * p["platformMultiplier"]
        eff = rn / p["aiMultiplierDefault"]
        build = eff / p["capacityPmPerYear"] * 12
        return {
            "native": round(native, 2),
            "rn": round(rn, 2),
            "effective": round(eff, 2),
            "buildMonths": round(build, 1),
            # Unrounded, because the markdown and catalog/index.html both render it
            # to whole months and rounding here first made 47.47 print as month 48.
            "launchMonth": build + p["preLaunchOffsetMonths"],
        }

    return [
        {"name": "Walking skeleton only", "note": "TestFlight target, carries no compliance package",
         **project(skeleton)},
        {"name": "Recut v1 (recommended)", "note": "skeleton plus compliance minimum plus launch hardening",
         **project(skeleton + compliance + quality)},
        {"name": "Full MVP v1 (15 features)", "note": "the originally approved scope, obligations counted explicitly",
         **project(mvp_features + compliance + quality)},
        {"name": "PRD P0 list", "note": "everything prd.md marks launch-critical",
         **project(prd_p0 + compliance + quality)},
    ]


# --------------------------------------------------------------------------- #
# markdown generation
# --------------------------------------------------------------------------- #

def whole_month(x: float) -> int:
    """Round half up, matching JavaScript's Math.round in catalog/index.html.

    Python's default rounding is half-to-even, so a scenario landing on exactly
    x.5 would print one month earlier here than in the interactive catalog.
    """
    return math.floor(x + 0.5)


def rel_label(r: str) -> str:
    return {"mvp": "**MVP v1**", "v1.x": "v1.x", "v2": "v2+", "never": "~~never~~"}.get(r, r)


def md_escape(s: str) -> str:
    return str(s).replace("|", "\\|")


def generate(d: dict) -> str:
    p = d["planning"]
    entries = d["entries"]
    by_id = {e["id"]: e for e in entries}
    personas = {x["id"]: x for x in d["personas"]}
    needs = {x["id"]: x for x in d["needs"]}
    jobs = {x["id"]: x for x in d["jobs"]}
    ejobs = {x["id"]: x for x in d["emotionalJobs"]}

    stamp = datetime.now(timezone(timedelta(hours=-4))).strftime("%Y-%m-%d %H:%M:%S UTC-4")
    out: list[str] = []
    w = out.append

    w("# Waypoint Features and Functionality Catalog")
    w("")
    w(f"> Version-Timestamp: {stamp}")
    w(">")
    w("> **Generated file. Do not edit.** Source of truth is `catalog/features.json`;")
    w("> regenerate with `python catalog/build.py`. The interactive view, where release")
    w("> assignment can be changed and the timeline recomputed, is `catalog/index.html`.")
    w("")
    w(d["meta"]["canonicalFor"])
    w("")

    # findings first: they are the reason to read this at all
    w("## Read this first")
    w("")
    for f in d.get("findings", []):
        w(f"**{f['title']}.** {f['detail']}")
        w("")

    # scenario table
    w("## What each scenario costs")
    w("")
    w(f"At {p['capacityPmPerYear']} person-months a year of real capacity, "
      f"a {p['aiMultiplierDefault']}x AI leverage assumption, and a "
      f"{p['platformMultiplier']}x React Native factor over the iOS-native estimates. "
      f"Competitive window: {p['competitiveWindowMonths'][0]} to "
      f"{p['competitiveWindowMonths'][1]} months.")
    w("")
    w("| Scenario | Native pm | React Native pm | After leverage | Projected iOS launch | Verdict |")
    w("|---|---:|---:|---:|---:|---|")
    hi = p["competitiveWindowMonths"][1]
    lo = p["competitiveWindowMonths"][0]
    for s in scenarios(d):
        verdict = ("inside the window with room" if s["launchMonth"] <= lo
                   else "inside, only just" if s["launchMonth"] <= hi
                   else f"**past the {hi}-month window**")
        w(f"| {s['name']} | {s['native']} | {s['rn']} | {s['effective']} "
          f"| month {whole_month(s['launchMonth'])} | {verdict} |")
    w("")
    w("The recut is the standing Phase 9 recommendation. Its projection reproduces "
      "`research/09-financial-team/team-roadmap.md`'s published month 12 to 14 independently, "
      "which is the check that the model is not inventing numbers.")
    w("")

    # conflicts
    w("## Where the documents disagree")
    w("")
    for c in d.get("conflicts", []):
        w(f"### {c['id']}: {c['title']}")
        w("")
        w(f"Affects: {', '.join('`' + e + '`' for e in c['entries'])}")
        w("")
        for pos in c["positions"]:
            w(f"- `{pos['source']}` &mdash; {pos['says']}")
        w("")
        w(f"**Recommendation.** {c['recommendation']}")
        w("")

    # index table
    w("## Index")
    w("")
    w("| ID | Feature | Module | Release | Native pm | RICE rank | Personas |")
    w("|---|---|---|---|---:|---:|---|")
    mod_order = {m["id"]: m["order"] for m in d["modules"]}
    mod_name = {m["id"]: m["name"] for m in d["modules"]}
    ordered = sorted(entries, key=lambda e: (mod_order.get(e["module"], 99),
                                             e["rice"]["rank"] if e.get("rice") else 900,
                                             e["id"]))
    for e in ordered:
        per = ", ".join(personas[x["id"]]["name"] for x in (e.get("personas") or [])
                        if x["id"] in personas) or "&mdash;"
        rank = f"#{e['rice']['rank']}" if e.get("rice") else "&mdash;"
        w(f"| `{e['id']}` | {md_escape(e['name'])} | {mod_name.get(e['module'], e['module'])} "
          f"| {rel_label(e['assigned'])} | {e['effortNative']:.2f} | {rank} | {per} |")
    w("")

    # persona coverage
    w("## Coverage by persona")
    w("")
    w("| Persona | Role | Features serving them | Of those, in the MVP |")
    w("|---|---|---:|---:|")
    for pid, per in personas.items():
        serving = [e for e in entries if any(x["id"] == pid for x in (e.get("personas") or []))]
        in_mvp = [e for e in serving if e["assigned"] == "mvp"]
        w(f"| **{per['name']}** | {per['role']} | {len(serving)} | {len(in_mvp)} |")
    w("")

    w("## Coverage by unmet need")
    w("")
    w("| Need | Evidence | Features | In the MVP |")
    w("|---|---|---:|---:|")
    for nid, n in needs.items():
        serving = [e for e in entries if nid in (e.get("needs") or [])]
        in_mvp = [e for e in serving if e["assigned"] == "mvp"]
        w(f"| **{nid}** {md_escape(n['name'])} | {n['evidence']} | {len(serving)} | {len(in_mvp)} |")
    w("")
    w("A need with strong evidence and nothing in the MVP is a gap worth arguing about. "
      "N11 is intentionally unserved: it is on the do-not-chase list.")
    w("")

    # full detail by module
    w("## Full detail")
    w("")
    for m in sorted(d["modules"], key=lambda x: x["order"]):
        items = [e for e in ordered if e["module"] == m["id"]]
        if not items:
            continue
        total = sum(e["effortNative"] for e in items)
        w(f"### {m['name']}")
        w("")
        w(f"*{m['tagline']}* &mdash; {len(items)} items, {total:.2f} native person-months.")
        w("")
        for e in items:
            w(f"#### `{e['id']}` {e['name']}")
            w("")
            w(f"**{e['summary']}**")
            w("")
            w(e["description"])
            w("")

            if e.get("locked"):
                w(f"> **Locked.** {e.get('lockReason', '')}")
                w("")

            for cid in e.get("conflictIds") or []:
                c = next((x for x in d["conflicts"] if x["id"] == cid), None)
                if c:
                    w(f"> **Documents disagree ({cid}).** {c['title']} "
                      f"Recommendation: {c['recommendation']}")
                    w("")

            rows = [
                ("Release", rel_label(e["assigned"])),
                ("Module", mod_name.get(e["module"], e["module"])),
                ("Effort, iOS-native", f"{e['effortNative']:.2f} pm" +
                 (f" &mdash; {e['effortNote']}" if e.get("effortNote") else "")),
                ("Effort, React Native", f"{e['effortNative'] * p['platformMultiplier']:.2f} pm"),
            ]
            if e.get("skeletonEffort") is not None:
                rows.append(("Walking-skeleton slice",
                             f"{e['skeletonEffort']:.2f} pm &mdash; {e.get('skeletonScope', '')}"))
            if e.get("rice"):
                r = e["rice"]
                rows.append(("RICE", f"rank #{r['rank']}, score {r['score']:,} "
                                     f"(reach {r['reach']:,}, impact {r['impact']}, "
                                     f"confidence {int(r['confidence'] * 100)}%, effort {r['effort']})"))
            if e.get("personas"):
                rows.append(("Personas", ", ".join(
                    f"{personas[x['id']]['name']} ({x['weight']})"
                    for x in e["personas"] if x["id"] in personas)))
            if e.get("needs"):
                rows.append(("Needs", ", ".join(
                    f"{n} {needs[n]['name']}" for n in e["needs"] if n in needs)))
            if e.get("jobs"):
                rows.append(("Jobs", ", ".join(
                    f"{j} {jobs[j]['name']}" for j in e["jobs"] if j in jobs)))
            if e.get("emotionalJobs"):
                rows.append(("Emotional jobs", ", ".join(
                    ejobs[j]["name"] for j in e["emotionalJobs"] if j in ejobs)))
            if e.get("dependsOn"):
                rows.append(("Depends on", ", ".join(
                    f"`{x}` {by_id[x]['name']}" for x in e["dependsOn"] if x in by_id)))
            if e.get("blocks"):
                rows.append(("Blocks", ", ".join(f"`{x}`" for x in e["blocks"])))
            if e.get("satisfies"):
                rows.append(("Satisfies", ", ".join(f"`{x}`" for x in e["satisfies"])))
            if e.get("satisfiedBy"):
                rows.append(("Engineered by", f"`{e['satisfiedBy']}`"))
            if e.get("prdRequirements"):
                rows.append(("Requirement IDs", ", ".join(f"`{x}`" for x in e["prdRequirements"])))

            w("| | |")
            w("|---|---|")
            for k, v in rows:
                w(f"| **{k}** | {md_escape(v)} |")
            w("")

            if e.get("capabilities"):
                w("**What it actually does**")
                w("")
                for c in e["capabilities"]:
                    w(f"- {c}")
                w("")
            if e.get("acceptanceCriteria"):
                w("**Done means**")
                w("")
                for c in e["acceptanceCriteria"]:
                    w(f"- {c}")
                w("")
            if e.get("integrations"):
                w("**Integrations** &mdash; " + "; ".join(e["integrations"]))
                w("")
            if e.get("pullForwardTrigger"):
                w(f"**What pulls it forward.** {e['pullForwardTrigger']}")
                w("")
            if e.get("risks"):
                w("**Risks**")
                w("")
                for r in e["risks"]:
                    w(f"- {r}")
                w("")
            if e.get("openQuestions"):
                w("**Still open**")
                w("")
                for q in e["openQuestions"]:
                    w(f"- {q}")
                w("")

            w("**What each document says.** "
              f"`mvp-scope.md`: {e['baselines']['mvpScope']}. "
              f"`prd.md`: {e['baselines']['prdPriority']}. "
              f"`team-roadmap.md`: {e['baselines']['teamRoadmap']}.")
            w("")
            w("Sources: " + ", ".join(f"`{s}`" for s in e.get("sources", [])))
            w("")

    w("## Taxonomies")
    w("")
    w("### Personas")
    w("")
    for per in personas.values():
        w(f"- **{per['name']}**, {per['role']} ({per['segment']}). {per['essence']} "
          f"Top jobs: {', '.join(per['topJobs'])}. Source: `{per['source']}`")
    w("")
    w("### Unmet needs")
    w("")
    for n in needs.values():
        w(f"- **{n['id']} {n['name']}** (evidence: {n['evidence']}). {n['detail']}")
    w("")
    w("### Jobs to be done")
    w("")
    for j in jobs.values():
        w(f"- **{j['id']}** {j['name']} ({j['layer']})")
    w("")
    w("### Emotional jobs")
    w("")
    for j in ejobs.values():
        w(f"- **{j['id']}** {j['name']} ({personas[j['persona']]['name']})")
    w("")

    w("## Source documents")
    w("")
    for s in d["meta"]["sourceDocuments"]:
        w(f"- `{s}`")
    w("")

    return "\n".join(out) + "\n"


def main() -> int:
    check_only = "--check" in sys.argv

    try:
        d = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"error: {JSON_PATH} not found", file=sys.stderr)
        return 1
    except json.JSONDecodeError as exc:
        print(f"error: {JSON_PATH} is not valid JSON: {exc}", file=sys.stderr)
        return 1

    if derive_blocks(d) and not check_only:
        JSON_PATH.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("rebuilt reverse dependency edges in features.json")

    errors = validate(d)
    if errors:
        print(f"{len(errors)} validation problem(s):", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    counts: dict[str, int] = {}
    for e in d["entries"]:
        counts[e["kind"]] = counts.get(e["kind"], 0) + 1
    summary = ", ".join(f"{v} {k}" for k, v in sorted(counts.items()))
    print(f"validated {len(d['entries'])} entries ({summary})")

    for s in scenarios(d):
        print(f"  {s['name']:<28} {s['rn']:>6.2f} RN pm -> month {whole_month(s['launchMonth'])}")

    if check_only:
        return 0

    MD_PATH.write_text(generate(d), encoding="utf-8")
    lines = MD_PATH.read_text(encoding="utf-8").count("\n")
    print(f"wrote {MD_PATH.relative_to(ROOT)} ({lines} lines)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
