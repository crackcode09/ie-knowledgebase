"""Refresh the vendored O*NET role profiles under roles/onet/ from the official O*NET database CSV files.

Usage:  python tools/onet_refresh.py              # refresh every code listed in roles/onet/codes.txt
        python tools/onet_refresh.py 17-2112.00   # one code

Reads the current release's CSV files from the O*NET Resource Center download area (db_<ver>_csv/*.csv),
keeps the rows for the requested occupation codes, and writes one Markdown profile and one JSON file per
code with the release version and download date stamped on them. Standard library only.

Data: O*NET Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA),
used under the CC BY 4.0 licence. O*NET is a trademark of USDOL/ETA. The IE Knowledgebase is not affiliated
with or endorsed by USDOL/ETA.
"""
import csv
import io
import json
import sys
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "roles" / "onet"
VERSION = "31.0"                      # bump when O*NET publishes a new release (quarterly)
BASE = f"https://www.onetcenter.org/dl_files/database/db_{VERSION.replace('.', '_')}_csv/"
FILES = {
    "occupation": "occupation_data.csv",
    "tasks": "task_statements.csv",
    "task_ratings": "task_ratings.csv",
    "knowledge": "knowledge.csv",
    "skills_essential": "essential_skills.csv",
    "skills_transferable": "transferable_skills.csv",
    "abilities": "abilities.csv",
    "work_activities": "work_activities.csv",
    "software": "software_skills.csv",
}
ATTRIBUTION = ("This file includes information from the O*NET {v} Database by the U.S. Department of Labor, Employment and "
               "Training Administration (USDOL/ETA), used under the CC BY 4.0 licence. O*NET is a trademark of USDOL/ETA. "
               "The IE Knowledgebase is not affiliated with or endorsed by USDOL/ETA.")


def fetch(name):
    url = BASE + FILES[name]
    with urllib.request.urlopen(url, timeout=120) as r:   # noqa: S310 - fixed https host
        text = r.read().decode("utf-8-sig")
    return list(csv.DictReader(io.StringIO(text)))


def rated(rows, code):
    """Element rows for one code: importance (IM) and level (LV) on one line per element."""
    by = {}
    for r in rows:
        if r["O*NET-SOC Code"] != code or r.get("Recommend Suppress") == "Y":
            continue
        e = by.setdefault(r["Element ID"], {"id": r["Element ID"], "name": r["Element Name"], "importance": None, "level": None})
        if r["Scale ID"] == "IM":
            e["importance"] = float(r["Data Value"])
        elif r["Scale ID"] == "LV":
            e["level"] = float(r["Data Value"])
    out = [e for e in by.values() if e["importance"] is not None]
    return sorted(out, key=lambda e: -e["importance"])


def profile(code, data):
    occ = next((r for r in data["occupation"] if r["O*NET-SOC Code"] == code), None)
    if not occ:
        sys.exit(f"no occupation {code} in O*NET {VERSION}")
    imp = {}
    for r in data["task_ratings"]:
        if r["O*NET-SOC Code"] == code and r["Scale ID"] == "IM":
            imp[r["Task ID"]] = float(r["Data Value"])
    tasks = [{"id": r["Task ID"], "task": r["Task"], "type": r["Task Type"], "importance": imp.get(r["Task ID"])}
             for r in data["tasks"] if r["O*NET-SOC Code"] == code]
    tasks.sort(key=lambda t: -(t["importance"] or 0))
    software = [{"example": r["Workplace Example"], "category": r["Element Name"], "hot": r["Hot Technology"] == "Y", "in_demand": r["In Demand"] == "Y"}
                for r in data["software"] if r["O*NET-SOC Code"] == code]
    return {
        "code": code, "title": occ["Title"], "description": occ["Description"],
        "onet_version": VERSION, "downloaded": date.today().isoformat(), "attribution": ATTRIBUTION.format(v=VERSION),
        "tasks": tasks,
        "knowledge": rated(data["knowledge"], code),
        "skills_essential": rated(data["skills_essential"], code),
        "skills_transferable": rated(data["skills_transferable"], code),
        "abilities": rated(data["abilities"], code),
        "work_activities": rated(data["work_activities"], code),
        "technology": software,
    }


def markdown(p):
    def table(title, rows, idkey, namekey, extra=None):
        out = [f"\n## {title}\n", "| ID | Element | Importance (1 to 5) | Level (0 to 7) |", "|---|---|---|---|"]
        for e in rows:
            out.append(f"| {e[idkey]} | {e[namekey]} | {e['importance']:.2f} | {'' if e['level'] is None else f'{e['level']:.2f}'} |")
        return "\n".join(out)
    md = [f"# {p['title']} ({p['code']})", "",
          f"O*NET {p['onet_version']} Database, downloaded {p['downloaded']}. Refresh with `python tools/onet_refresh.py {p['code']}`. "
          "Importance is O*NET's 1 to 5 scale (5 = extremely important); Level is the 0 to 7 scale of how much of the element the job needs. "
          "Rows are sorted by importance.", "", f"> {p['attribution']}", "", "## Description", "", p["description"], "",
          "## Tasks", "", "| Task ID | Task | Type | Importance (1 to 5) |", "|---|---|---|---|"]
    for t in p["tasks"]:
        md.append(f"| {t['id']} | {t['task']} | {t['type']} | {'' if t['importance'] is None else f'{t['importance']:.2f}'} |")
    md.append(table("Knowledge", p["knowledge"], "id", "name"))
    md.append(table("Essential skills", p["skills_essential"], "id", "name"))
    md.append(table("Transferable skills", p["skills_transferable"], "id", "name"))
    md.append(table("Abilities", p["abilities"], "id", "name"))
    md.append(table("Work activities", p["work_activities"], "id", "name"))
    md += ["", "## Technology", "", "Flags come from O*NET: *hot* technologies are frequently included in employer job postings across occupations; *in demand* ones are frequently included in postings for this occupation.", "",
           "| Example | Category | Hot | In demand |", "|---|---|---|---|"]
    for s in p["technology"]:
        md.append(f"| {s['example']} | {s['category']} | {'yes' if s['hot'] else ''} | {'yes' if s['in_demand'] else ''} |")
    return "\n".join(md) + "\n"


def main(codes):
    OUT.mkdir(parents=True, exist_ok=True)
    data = {k: fetch(k) for k in FILES}
    for code in codes:
        p = profile(code, data)
        (OUT / f"{code}.json").write_text(json.dumps(p, indent=1, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
        (OUT / f"{code}.md").write_text(markdown(p), encoding="utf-8", newline="\n")
        print(f"wrote roles/onet/{code}.md: {p['title']}, {len(p['tasks'])} tasks, {len(p['knowledge'])} knowledge, "
              f"{len(p['skills_essential']) + len(p['skills_transferable'])} skills, {len(p['technology'])} technology rows")


if __name__ == "__main__":
    codes = sys.argv[1:] or [c.split("#")[0].strip() for c in (OUT / "codes.txt").read_text(encoding="utf-8").splitlines() if c.split("#")[0].strip()]
    main(codes)
