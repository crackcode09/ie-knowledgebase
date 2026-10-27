"""hcdkit.py - data and calculations for the Human-Centered AI course.

Running case: Halvorsen Components (fictional, also used in the Efficient AI course). Before building any AI,
the team interviews and observes eight frontline, operational and knowledge workers, synthesizes themes,
frames opportunities, maps assumptions and runs a quick prototype test.

All interview notes are SIMULATED for teaching; no real people were interviewed.

    python tools/hcdkit.py data          # (re)write data/*.csv
    python tools/hcdkit.py all           # every worked example
    python tools/hcdkit.py <name>        # themes, machine_clusters, opportunities, assumptions, prototype

Requires numpy, pandas, scipy, scikit-learn. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import adjusted_rand_score

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

PEOPLE = {"P1": "CNC operator (2nd shift)", "P2": "Maintenance technician", "P3": "Production planner",
          "P4": "Customer service agent", "P5": "Accounts payable clerk", "P6": "Quality engineer",
          "P7": "Shift supervisor", "P8": "Warehouse picker"}
THEMES = {"T1": "Finding the right information takes too long",
          "T2": "Know-how lives in a few experts' heads",
          "T3": "Systems don't connect, so people re-key and reconcile",
          "T4": "People don't trust numbers they can't trace",
          "T5": "Firefighting crowds out planned work",
          "T6": "Floor conditions limit what tools can work (gloves, noise, time)"}
# (person, note type, observation or paraphrased statement, theme)
NOTES = [
    ("P1", "pain", "Walks to the office PC to look up the latest work instruction revision several times a shift", "T1"),
    ("P1", "workaround", "Keeps a personal notebook of offsets and tricks for difficult part numbers", "T2"),
    ("P1", "constraint", "Wears gloves and cannot use a touchscreen without taking them off", "T6"),
    ("P1", "need", "Wants to know quickly whether a drawing note applies to this revision", "T1"),
    ("P1", "pain", "When the setup expert is off shift, waits or guesses on unfamiliar jobs", "T2"),
    ("P1", "constraint", "Machine area is loud; voice input would be hard to hear", "T6"),
    ("P2", "pain", "Searches three places for the last repair history of a machine", "T1"),
    ("P2", "goal", "Wants to fix a breakdown right the first time instead of trial and error", "T2"),
    ("P2", "workaround", "Texts photos of faults to a retired colleague who knows the old machines", "T2"),
    ("P2", "pain", "Planned maintenance is skipped whenever there is a breakdown elsewhere", "T5"),
    ("P2", "need", "Needs the fault code, the manual page and past fixes together in one place", "T1"),
    ("P2", "constraint", "Hands are often oily; phone stays in the pocket during repairs", "T6"),
    ("P3", "pain", "Copies orders from the ERP into a spreadsheet every morning to build the schedule", "T3"),
    ("P3", "pain", "Does not trust the system lead times so adds own buffer to every order", "T4"),
    ("P3", "goal", "Wants to see the impact of a rush order on other customers before saying yes", "T5"),
    ("P3", "workaround", "Calls the floor to check machine status because the system is not up to date", "T3"),
    ("P3", "pain", "Half the day goes to expediting instead of planning ahead", "T5"),
    ("P3", "need", "Needs to know why a forecast changed before acting on it", "T4"),
    ("P4", "pain", "Toggles between four screens to answer one order status question", "T3"),
    ("P4", "need", "Wants a quick answer on technical questions without waiting for engineering", "T2"),
    ("P4", "pain", "Spends a long time finding the right spec sheet for a customer question", "T1"),
    ("P4", "goal", "Wants to give customers a delivery date she can stand behind", "T4"),
    ("P4", "workaround", "Keeps a shared document of answers to common technical questions", "T2"),
    ("P4", "constraint", "Must answer phone calls within a few minutes; no time for long searches", "T6"),
    ("P5", "pain", "Re-keys invoice lines from PDF into the ERP by hand", "T3"),
    ("P5", "pain", "Reconciles price differences between PO and invoice line by line", "T3"),
    ("P5", "need", "Wants exceptions flagged with the reason so she can act quickly", "T4"),
    ("P5", "goal", "Wants to stop month-end overtime", "T5"),
    ("P5", "workaround", "Keeps a personal list of suppliers whose invoices always have unit-of-measure problems", "T2"),
    ("P5", "pain", "Would not approve a payment suggested by a system without seeing why it matched", "T4"),
    ("P6", "pain", "Writing an 8D report means hunting through emails for the complaint history", "T1"),
    ("P6", "need", "Wants to see all similar past complaints and their root causes in one view", "T1"),
    ("P6", "pain", "Investigations are interrupted by daily containment firefights", "T5"),
    ("P6", "goal", "Wants to spot recurring problems before the customer does", "T5"),
    ("P6", "workaround", "Exports data from three systems and joins them in a spreadsheet", "T3"),
    ("P6", "pain", "Does not trust a defect rate unless she can see the raw inspection records", "T4"),
    ("P7", "pain", "Spends the first hour of the shift chasing what happened on the previous shift", "T5"),
    ("P7", "need", "Wants handover notes that are complete and quick to read", "T1"),
    ("P7", "pain", "Only two people can set up the new machine; absences stop production", "T2"),
    ("P7", "goal", "Wants the team to solve problems without escalating everything", "T2"),
    ("P7", "workaround", "Uses a whiteboard because the system board is never current", "T3"),
    ("P7", "constraint", "No time during the shift for training on new software", "T6"),
    ("P8", "pain", "Walks back to the desk when a pick location is wrong in the system", "T3"),
    ("P8", "constraint", "Scanner gun is the only device carried; screen is small", "T6"),
    ("P8", "workaround", "Remembers where fast movers really are instead of trusting the system", "T4"),
    ("P8", "pain", "Rush orders interrupt planned picking waves", "T5"),
    ("P8", "need", "Wants to know about a shortage before walking to the location", "T1"),
    ("P8", "goal", "Wants fewer wasted trips across the warehouse", "T5"),
]

OPPORTUNITIES = [
    # id, how-might-we statement, theme, desirability, feasibility, viability, AI fit (1-5)
    ("O1", "How might we help technicians get the right information for this job, at the machine, in seconds?",
     "T1", 5, 3, 4, 4),
    ("O2", "How might we capture and share experts' know-how so that anyone on shift can handle unfamiliar jobs?",
     "T2", 5, 3, 4, 3),
    ("O3", "How might we stop people re-keying the same data between systems?", "T3", 4, 4, 4, 2),
    ("O4", "How might we show the reasons behind system numbers so people can trust and act on them?", "T4", 4, 3, 3, 4),
    ("O5", "How might we protect planned work from daily firefighting?", "T5", 4, 2, 3, 2),
    ("O6", "How might we design tools that work with gloves, noise and seconds to spare?", "T6", 3, 3, 3, 2),
]

ASSUMPTIONS = [
    # id, assumption, importance 1-5, evidence 1-5 (5 = strong evidence)
    ("A1", "Technicians will use a question-answering tool at the machine during a job", 5, 1),
    ("A2", "Answers can be drawn from current, approved work instructions and repair records", 5, 2),
    ("A3", "A small rugged tablet at each cell can be used with gloves", 4, 2),
    ("A4", "Experts will review and correct the tool's answers in the first months", 4, 1),
    ("A5", "Faster information access reduces setup and repair time", 5, 4),
    ("A6", "IT can connect the document system and the maintenance system", 3, 4),
    ("A7", "Supervisors will allow time for a 20-minute introduction", 2, 4),
]

PROTOTYPE_TESTS = [
    # assumption, cheapest test
    ("A1", "Wizard-of-Oz: technician asks questions on a tablet; an engineer answers live from the documents"),
    ("A2", "Audit 30 recent technician questions: can each be answered from current approved documents?"),
    ("A3", "Paper / cardboard mock-up and a borrowed rugged tablet used for one shift"),
    ("A4", "Ask two experts to review 20 answers; time and willingness"),
]


def make_data(seed=2032):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    notes = pd.DataFrame(NOTES, columns=["person", "type", "note", "theme"])
    notes.insert(1, "role", notes.person.map(PEOPLE))
    notes.insert(0, "note_id", [f"N{i:02d}" for i in range(1, len(notes) + 1)])
    notes.drop(columns="theme").to_csv(os.path.join(D, "interview_notes.csv"), index=False)
    notes[["note_id", "theme"]].to_csv(os.path.join(D, "theme_key.csv"), index=False)
    pd.DataFrame([dict(theme=k, name=v) for k, v in THEMES.items()]).to_csv(os.path.join(D, "themes.csv"), index=False)
    pd.DataFrame(OPPORTUNITIES, columns=["id", "statement", "theme", "desirability", "feasibility", "viability",
                                         "ai_fit"]).to_csv(os.path.join(D, "opportunities.csv"), index=False)
    pd.DataFrame(ASSUMPTIONS, columns=["id", "assumption", "importance", "evidence"]).to_csv(
        os.path.join(D, "assumptions.csv"), index=False)

    # Wizard-of-Oz test (A1): 12 technicians, 3 lookup tasks each, current way vs prototype
    rows = []
    for t in range(1, 13):
        for task in range(1, 4):
            base = rng.lognormal(np.log(310), 0.35)          # seconds, current way (walk to PC, search)
            proto = rng.lognormal(np.log(95), 0.45)
            ok_base = rng.random() < 0.83
            ok_proto = rng.random() < 0.89
            rows.append(dict(tech=f"Tech{t:02d}", task=task, method="current", seconds=round(base), success=int(ok_base)))
            rows.append(dict(tech=f"Tech{t:02d}", task=task, method="prototype", seconds=round(proto),
                             success=int(ok_proto)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "wizard_of_oz_test.csv"), index=False)
    trust = pd.DataFrame(dict(tech=[f"Tech{t:02d}" for t in range(1, 13)],
                              would_use_daily=rng.choice([1, 2, 3, 4, 5], 12, p=[.05, .1, .2, .4, .25]),
                              trust_answers=rng.choice([1, 2, 3, 4, 5], 12, p=[.1, .2, .35, .25, .1]),
                              wants_source_shown=rng.choice([0, 1], 12, p=[.17, .83])))
    trust.to_csv(os.path.join(D, "prototype_survey.csv"), index=False)
    # role-play cards for simulated interviews
    lines = ["# Role-play Cards for Simulated Interviews", "",
             "Simulated roles for practice. Interviewees: stay in role; reveal an item only when a question invites it "
             "(open questions about real recent events). Do not volunteer solutions.", ""]
    for pid, role in PEOPLE.items():
        lines += [f"## {pid}: {role}", ""]
        for _, r in notes[notes.person == pid].iterrows():
            lines.append(f"- ({r.type}) {r.note}")
        lines.append("")
    with open(os.path.join(D, "roleplay_cards.md"), "w") as f:
        f.write("\n".join(lines))
    return {"interview_notes": len(notes), "opportunities": len(OPPORTUNITIES), "assumptions": len(ASSUMPTIONS),
            "wizard_of_oz_rows": len(rows), "survey": 12}


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"))


def ex_themes():
    n = load("interview_notes").merge(load("theme_key"), on="note_id")
    m = pd.crosstab(n.theme, n.person)
    breadth = (m > 0).sum(axis=1)
    rows = []
    for t in THEMES:
        rows.append(dict(theme=t, name=THEMES[t], notes=int(m.loc[t].sum()), roles=int(breadth[t]),
                         pains=int(((n.theme == t) & (n.type == "pain")).sum()),
                         workarounds=int(((n.theme == t) & (n.type == "workaround")).sum())))
    rows.sort(key=lambda r: (-r["roles"], -r["notes"]))
    return {"notes": len(n), "people": n.person.nunique(), "types": n.type.value_counts().to_dict(), "themes": rows}


def ex_machine_clusters(k=6, seed=0):
    n = load("interview_notes").merge(load("theme_key"), on="note_id")
    X = TfidfVectorizer(stop_words="english").fit_transform(n.note)
    km = KMeans(n_clusters=k, n_init=20, random_state=seed).fit(X)
    ari = adjusted_rand_score(n.theme, km.labels_)
    ct = pd.crosstab(km.labels_, n.theme)
    purity = float(ct.max(axis=1).sum() / len(n))
    return {"adjusted_rand_index": round(float(ari), 3), "purity": round(purity, 3),
            "cluster_sizes": pd.Series(km.labels_).value_counts().sort_index().to_dict(),
            "note": "word-based clusters match human themes only partly; meaning, not vocabulary, defines themes"}


def ex_opportunities(weights=(0.35, 0.25, 0.2, 0.2)):
    o = load("opportunities")
    wd, wf, wv, wa = weights
    o["score"] = (wd * o.desirability + wf * o.feasibility + wv * o.viability + wa * o.ai_fit).round(2)
    o = o.sort_values("score", ascending=False)
    return {"weights": dict(desirability=wd, feasibility=wf, viability=wv, ai_fit=wa),
            "ranked": o[["id", "theme", "desirability", "feasibility", "viability", "ai_fit", "score"]].to_dict("records"),
            "top": o.iloc[0].statement}


def ex_assumptions():
    a = load("assumptions")
    a["risk"] = a.importance * (6 - a.evidence)
    a["quadrant"] = np.where(a.importance >= 4, np.where(a.evidence <= 2, "Test first", "Proceed (monitor)"),
                             np.where(a.evidence <= 2, "Learn later", "Ignore for now"))
    tests = dict((k, v) for k, v in PROTOTYPE_TESTS)
    a["cheapest_test"] = a.id.map(tests).fillna("")
    return {"assumptions": a.sort_values("risk", ascending=False)[["id", "importance", "evidence", "risk", "quadrant",
                                                                  "cheapest_test"]].to_dict("records")}


def ex_prototype():
    w = load("wizard_of_oz_test")
    cur, pro = w[w.method == "current"], w[w.method == "prototype"]
    # paired per tech-task
    m = cur.merge(pro, on=["tech", "task"], suffixes=("_cur", "_pro"))
    ratio = np.log(m.seconds_pro) - np.log(m.seconds_cur)
    t = stats.ttest_1samp(ratio, 0)
    s = load("prototype_survey")
    return {"tasks": len(m), "median_seconds_current": float(cur.seconds.median()),
            "median_seconds_prototype": float(pro.seconds.median()),
            "geometric_mean_time_ratio": round(float(np.exp(ratio.mean())), 3),
            "paired_t_p_value": float(f"{t.pvalue:.2e}"),
            "success_current": round(float(cur.success.mean()), 3), "success_prototype": round(float(pro.success.mean()), 3),
            "would_use_daily_4or5": int((s.would_use_daily >= 4).sum()), "trust_4or5": int((s.trust_answers >= 4).sum()),
            "want_source_shown": int(s.wants_source_shown.sum()), "n_survey": len(s)}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, np.floating):
        return round(float(o), 4)
    if isinstance(o, np.integer):
        return int(o)
    return o


EX = {"themes": ex_themes, "machine_clusters": ex_machine_clusters, "opportunities": ex_opportunities,
      "assumptions": ex_assumptions, "prototype": ex_prototype}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list) and b and isinstance(b[0], dict):
                    print(f"  {a}:")
                    for row in b:
                        print(f"    {_clean(row)}")
                else:
                    print(f"  {a}: {_clean(b)}")
