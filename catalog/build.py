#!/usr/bin/env python3
"""Validate catalog/features.json and regenerate everything derived from it.

Run after every edit to features.json:

    python catalog/build.py            # validate, then write all outputs
    python catalog/build.py --check    # validate only, non-zero exit on failure

Three outputs, all generated and never hand-edited, because the JSON is the
source of truth (DEC-020):

  catalog/FEATURES.md        full mirror, so agents and humans without a
                             browser get the same catalog the page shows
  blueprint/index.html       the condensed features section 05, injected
  blueprint/blueprint.md     the same section in the citable markdown

The blueprint outputs are injected between marker comments and carry no
timestamp, so a rebuild that changes nothing produces no diff in the investor
document. FEATURES.md does carry a timestamp and therefore always diffs.

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
BP_HTML_PATH = ROOT / "blueprint" / "index.html"
BP_MD_PATH = ROOT / "blueprint" / "blueprint.md"

MARK_START = "<!-- CATALOG:START"
MARK_END = "<!-- CATALOG:END -->"

VALID_KINDS = {"feature", "compliance", "nonfunctional", "excluded"}
VALID_RELEASES = {"mvp", "v1.x", "v2", "never"}

# How each release reads to an investor, who does not know what "v1.x" means.
RELEASE_WORD = {"mvp": "launch", "v1.x": "fast-follow", "v2": "later"}
RELEASE_BADGE = {"mvp": "b-green", "v1.x": "b-amber", "v2": "b-gray"}


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
                       if e["kind"] == "feature" and e.get("historicalAssigned", e["assigned"]) == "mvp")
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
        {"name": "Recut v1 (approved)", "note": "skeleton plus compliance minimum plus launch hardening",
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
    w("Recut v1 is the approved first-release baseline (DEC-014). Its projection reproduces "
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


# --------------------------------------------------------------------------- #
# blueprint section 05, condensed
# --------------------------------------------------------------------------- #
#
# The blueprint is the investor-facing document, so this view is deliberately
# thinner than FEATURES.md: name, one-line purpose, when it ships, who it is
# for. Per-feature person-months and RICE ranks are internal planning detail
# and section 12 already owns the schedule, so they are left out on purpose.

def html_escape(s: str) -> str:
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def features_by_module(d: dict) -> list[tuple[dict, list[dict]]]:
    """Modules in display order, each with its shippable features.

    Excluded entries are left out because they are shown once in the
    never-build card rather than scattered through the module tables, and
    compliance and non-functional entries are summarised as counts.
    """
    rel_rank = {"mvp": 0, "v1.x": 1, "v2": 2}
    out = []
    for m in sorted(d["modules"], key=lambda x: x["order"]):
        items = [e for e in d["entries"]
                 if e["module"] == m["id"] and e["kind"] == "feature"]
        items.sort(key=lambda e: (rel_rank.get(e["assigned"], 9),
                                  e["rice"]["rank"] if e.get("rice") else 900))
        out.append((m, items))
    return out


def catalog_counts(d: dict) -> dict:
    e = d["entries"]
    feats = [x for x in e if x["kind"] == "feature"]
    return {
        "features": len(feats),
        "modules": len(d["modules"]),
        "mvp": len([x for x in feats if x["assigned"] == "mvp"]),
        "fast": len([x for x in feats if x["assigned"] == "v1.x"]),
        "later": len([x for x in feats if x["assigned"] == "v2"]),
        "never": len([x for x in e if x["kind"] == "excluded"]),
        "compliance": len([x for x in e if x["kind"] == "compliance"]),
        "nonfunctional": len([x for x in e if x["kind"] == "nonfunctional"]),
        "obligations": len([x for x in e
                            if x["kind"] in ("compliance", "nonfunctional")]),
        "skeleton": len([x for x in e if x.get("skeletonEffort")]),
    }


def nfr_groups(d: dict) -> str:
    """"6 accessibility, 6 language, 4 performance, 3 offline" and so on."""
    groups: dict[str, int] = {}
    for e in d["entries"]:
        if e["kind"] == "nonfunctional":
            g = (e.get("group") or "other").lower()
            groups[g] = groups.get(g, 0) + 1
    parts = sorted(groups.items(), key=lambda kv: (-kv[1], kv[0]))
    return ", ".join(f"{n} {g}" for g, n in parts)


def persona_cell(e: dict, personas: dict, bold: str, plain: str) -> str:
    """Primary personas emphasised, secondary plain. Empty renders as a dash."""
    bits = []
    for ref in e.get("personas") or []:
        p = personas.get(ref["id"])
        if not p:
            continue
        name = p["name"]
        bits.append(bold.format(name) if ref.get("weight") == "primary"
                    else plain.format(name))
    return ", ".join(bits) if bits else "&mdash;"


def render_blueprint_html(d: dict) -> str:
    c = catalog_counts(d)
    personas = {p["id"]: p for p in d["personas"]}
    out: list[str] = []
    w = out.append

    w('<div class="stats">')
    for k, v, sub in [
        ("Features", c["features"],
         f"Across {c['modules']} functional modules"),
        ("Approved for v1", c["mvp"],
         f"Plus {c['obligations']} compliance and platform obligations"),
        ("Fast-follow", c["fast"],
         "Deferred planning bucket; timing requires validation"),
        ("Ruled out", c["never"],
         "Locked by DEC-006 and not revisitable"),
    ]:
        w('  <div class="stat">')
        w(f'    <div class="k">{k}</div>')
        w(f'    <div class="v">{v}</div>')
        w(f'    <div class="d">{sub}</div>')
        w('  </div>')
    w('</div>')
    w('')

    w('<h3>What the platform does, and when each part ships</h3>')
    w(f'<p>{c["features"]} features across {c["modules"]} modules. '
      f'{c["mvp"]} are approved for the v1 launch, {c["fast"]} are deferred to v1.x after launch '
      f'and {c["later"]} wait on evidence or on a predecessor. Release phase for every '
      f'one of them, plus the {c["compliance"]} compliance requirements and '
      f'{c["nonfunctional"]} platform requirements that ship alongside, is decided in '
      f'<span class="kbd">catalog/features.json</span> under DEC-020 &mdash; not in this '
      f'document, and not in the three research documents that used to disagree about it. '
      f'Primary personas are shown in bold.</p>')
    w('')

    for m, items in features_by_module(d):
        w(f'<h4>{html_escape(m["name"])}</h4>')
        w(f'<p class="sec-sub" style="font-size:14.6px;margin:0 0 2px">'
          f'{html_escape(m["tagline"])}</p>')

        if items:
            w('<div class="tw"><table>')
            w('  <thead><tr><th style="width:27%">Feature</th><th>What it is for</th>'
              '<th>Ships</th><th>For</th></tr></thead>')
            w('  <tbody>')
            for e in items:
                rel = e["assigned"]
                badge = (f'<span class="badge {RELEASE_BADGE.get(rel, "b-gray")}">'
                         f'{RELEASE_WORD.get(rel, rel)}</span>')
                who = persona_cell(e, personas, "<strong>{}</strong>", "{}")
                w(f'    <tr><td><strong>{e["id"]}</strong> {html_escape(e["name"])}</td>'
                  f'<td>{html_escape(e.get("skeletonScope") if e.get("releaseScope") == "reduced-slice" else e["summary"])}</td>'
                  f'<td>{badge}</td><td>{who}</td></tr>')
            w('  </tbody>')
            w('</table></div>')

        if m["id"] == "trust":
            w(f'<p>Behind that one feature sit <strong>{c["compliance"]} compliance '
              f'requirements</strong> &mdash; privacy zones, layered consent, the deletion '
              f'pipeline, data subject rights, AI transparency, age gating, breach '
              f'readiness. They are not optional and not deferrable, so the catalog locks '
              f'them into v1 and counts their cost. '
              f'<a class="ref" href="#s15">Section 15</a> covers the legal basis.</p>')
        if m["id"] == "quality":
            w(f'<p>No user-facing features live here. It holds the '
              f'<strong>{c["nonfunctional"]} platform requirements</strong> that a public '
              f'launch requires ({nfr_groups(d)}), each with its own target and its own '
              f'cost. Naming them individually is what corrected the scope estimate: the '
              f'planning documents had absorbed all {c["obligations"]} obligations into a '
              f'single two-person-month line.</p>')
        w('')

    w('<div class="callout warn">')
    w('  <span class="lbl">What "approved for v1" does and does not mean</span>')
    w(f'  <p>DEC-014 approves Recut v1: reduced slices of {c["mvp"]} features plus {c["obligations"]} obligations. The accepted model is 13.38 React Native person-months, projecting iOS around month 13 under the current capacity and unmeasured 1.8x AI assumption. The historical full MVP is 32.52 person-months. Deferred work is not a fixed post-launch promise. Five founder decisions remain open. See section 12 for planning context.</p>')
    w('</div>')
    w('')

    excluded = [e for e in d["entries"] if e["kind"] == "excluded"]
    w('<h3>What we will never build</h3>')
    w(f'<p>Locked by DEC-006 and carried in the catalog as {c["never"]} explicit entries, '
      f'so nobody re-proposes them in six months.</p>')
    w('<div class="tw"><table>')
    w('  <tbody>')
    for e in excluded:
        w(f'    <tr><td style="width:34%"><strong>{html_escape(e["name"])}</strong></td>'
          f'<td>{html_escape(e.get("skeletonScope") if e.get("releaseScope") == "reduced-slice" else e["summary"])}</td></tr>')
    w('  </tbody>')
    w('</table></div>')
    w('<p>The NOT list is doing real work. It is what keeps a part-time team\'s v1 small '
      'instead of sprawling, and it is what makes the paid tier nameable.</p>')
    w('')

    w('<p style="color:var(--dim);font-size:13.5px">'
      'This section is generated from the catalog. The full detail behind every entry '
      '&mdash; capabilities, acceptance criteria, dependencies, effort, RICE score, the '
      'unmet need it answers &mdash; is filterable at '
      '<a class="ref" href="../catalog/">/catalog/</a>, where changing a release '
      'assignment recomputes the projected launch month live.</p>')

    return "\n".join(out)


def render_blueprint_md(d: dict) -> str:
    c = catalog_counts(d)
    personas = {p["id"]: p for p in d["personas"]}
    out: list[str] = []
    w = out.append

    w("### What the platform does, and when each part ships")
    w("")
    w(f"{c['features']} features across {c['modules']} modules: **{c['mvp']} approved for the "
      f"v1 launch**, {c['fast']} deferred to v1.x, {c['later']} waiting on "
      f"evidence or on a predecessor, and {c['never']} ruled out permanently. Release phase "
      f"for every one of them, plus the {c['compliance']} compliance requirements and "
      f"{c['nonfunctional']} platform requirements that ship alongside, is decided in "
      f"`catalog/features.json` under DEC-020 rather than in this document. Primary personas "
      f"in bold.")
    w("")

    for m, items in features_by_module(d):
        w(f"#### {m['name']}")
        w("")
        w(f"*{m['tagline']}*")
        w("")
        if items:
            w("| Feature | What it is for | Ships | For |")
            w("|---|---|---|---|")
            for e in items:
                rel = RELEASE_WORD.get(e["assigned"], e["assigned"])
                who = persona_cell(e, personas, "**{}**", "{}")
                w(f"| **{e['id']}** {md_escape(e['name'])} | {md_escape(e.get('skeletonScope') if e.get('releaseScope') == 'reduced-slice' else e['summary'])} "
                  f"| {rel} | {who} |")
            w("")
        if m["id"] == "trust":
            w(f"Behind that one feature sit **{c['compliance']} compliance requirements**: "
              f"privacy zones, layered consent, the deletion pipeline, data subject rights, "
              f"AI transparency, age gating, breach readiness. Not optional and not "
              f"deferrable, so the catalog locks them into v1 and counts their cost. "
              f"Section 15 covers the legal basis.")
            w("")
        if m["id"] == "quality":
            w(f"No user-facing features here. It holds the **{c['nonfunctional']} platform "
              f"requirements** a public launch requires ({nfr_groups(d)}), each with its own "
              f"target and cost. Naming them individually is what corrected the scope "
              f"estimate: the planning documents had absorbed all {c['obligations']} "
              f"obligations into a single two-person-month line.")
            w("")

    w("### What \"approved for v1\" does and does not mean")
    w("")
    w(f"DEC-014 approves Recut v1: reduced slices of {c['mvp']} features plus {c['obligations']} obligations. The accepted model is 13.38 React Native person-months, projecting iOS around month 13 under current capacity and the unmeasured 1.8x AI assumption. Historical full MVP: 32.52 person-months. Deferred work has no fixed post-launch date. Five founder decisions remain open.")
    w("")

    w("### What we will never build")
    w("")
    w(f"Locked by DEC-006 and carried in the catalog as {c['never']} explicit entries, so "
      f"nobody re-proposes them in six months.")
    w("")
    w("| Ruled out | Why |")
    w("|---|---|")
    for e in d["entries"]:
        if e["kind"] == "excluded":
            w(f"| **{md_escape(e['name'])}** | {md_escape(e.get('skeletonScope') if e.get('releaseScope') == 'reduced-slice' else e['summary'])} |")
    w("")
    w("The NOT list is doing real work. It is what keeps a part-time team's v1 small instead "
      "of sprawling, and it is what makes the paid tier nameable.")
    w("")
    w("Full detail behind every entry (capabilities, acceptance criteria, dependencies, "
      "effort, RICE score, the unmet need it answers) is in `catalog/FEATURES.md`, or "
      "filterable at `catalog/index.html`.")

    return "\n".join(out)


def inject(path: Path, body: str, check: bool = False) -> bool:
    """Replace the text between the CATALOG markers. True when the file changed.

    Refuses to guess: a missing, duplicated or inverted marker pair raises
    rather than silently appending or overwriting the wrong span.
    """
    text = path.read_text(encoding="utf-8")

    if text.count(MARK_START) != 1 or text.count(MARK_END) != 1:
        raise ValueError(
            f"{path.relative_to(ROOT)}: expected exactly one "
            f"'{MARK_START}' and one '{MARK_END}' "
            f"(found {text.count(MARK_START)} and {text.count(MARK_END)})"
        )

    start = text.index(MARK_START)
    open_end = text.index("-->", start) + len("-->")
    end = text.index(MARK_END)
    if end < open_end:
        raise ValueError(f"{path.relative_to(ROOT)}: CATALOG:END precedes CATALOG:START")

    # Match the marker's own indentation so the generated block does not sit at
    # column zero inside an indented <section>.
    line_start = text.rfind("\n", 0, start) + 1
    indent = text[line_start:start]
    if indent.strip():
        indent = ""
    if indent:
        body = "\n".join(indent + ln if ln else ln for ln in body.split("\n"))

    updated = text[:open_end] + "\n" + body + "\n" + indent + text[end:]
    if updated == text:
        return False
    if check:
        raise ValueError(f"{path.relative_to(ROOT)}: stale generated catalog block; run python catalog/build.py")
    path.write_text(updated, encoding="utf-8", newline="")
    return True


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
        import re
        normalize = lambda text: re.sub(r"> Version-Timestamp: [^\n]+", "> Version-Timestamp: ignored", text).replace("\r\n", "\n")
        try:
            if normalize(MD_PATH.read_text(encoding="utf-8")) != normalize(generate(d)):
                raise ValueError("catalog/FEATURES.md: stale; run python catalog/build.py")
            inject(BP_HTML_PATH, render_blueprint_html(d), check=True)
            inject(BP_MD_PATH, render_blueprint_md(d), check=True)
        except (OSError, ValueError) as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        return 0

    MD_PATH.write_text(generate(d), encoding="utf-8")
    lines = MD_PATH.read_text(encoding="utf-8").count("\n")
    print(f"wrote {MD_PATH.relative_to(ROOT)} ({lines} lines)")

    for path, body in ((BP_HTML_PATH, render_blueprint_html(d)),
                       (BP_MD_PATH, render_blueprint_md(d))):
        try:
            changed = inject(path, body)
        except (FileNotFoundError, ValueError) as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        rel = path.relative_to(ROOT)
        print(f"{'updated' if changed else 'unchanged'} {rel} catalog section")

    return 0


if __name__ == "__main__":
    sys.exit(main())
