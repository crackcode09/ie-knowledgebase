"""pmap.py - calculation toolkit for the Process Mapping course.

Running case: the RMA (return, repair and ship-back) process for linear guide carriages.

    python tools/pmap.py all       # every worked example
    python tools/pmap.py <name>    # va, spaghetti, vsm, spec

License: MIT
"""
from __future__ import annotations

import math
import sys

import numpy as np

# ---------------------------------------------------------------- case data
# Current RMA process: step, owner, work time (min), elapsed wait before the step (h), VA class
# VA = customer would pay / changes form-fit-function / right first time
# BVA = business-required non-value-added; NVA = waste
STEPS = [
    ("Customer emails return request", "Customer", 5, 0, "NVA"),
    ("Log request in spreadsheet", "Customer service", 6, 6, "NVA"),
    ("Ask customer for missing info", "Customer service", 8, 4, "NVA"),
    ("Issue RMA number", "Customer service", 4, 20, "BVA"),
    ("Customer ships part", "Customer", 15, 72, "NVA"),
    ("Receive and log part", "Receiving", 6, 10, "BVA"),
    ("Move to quality lab", "Receiving", 4, 16, "NVA"),
    ("Inspect and diagnose failure", "Quality", 45, 30, "VA"),
    ("Write failure report", "Quality", 25, 4, "BVA"),
    ("Approve repair vs replace", "Engineering", 10, 40, "BVA"),
    ("Repair carriage", "Repair", 60, 24, "VA"),
    ("Re-test", "Quality", 20, 8, "BVA"),
    ("Pack and ship back", "Shipping", 12, 16, "VA"),
    ("Send credit/close-out email", "Customer service", 5, 24, "NVA"),
]

# Layout coordinates (m) of locations in the building, for the spaghetti diagram.
LOC = {"Dock": (-4, 2), "Receiving": (8, 2), "Quality lab": (60, 35), "Repair bench": (15, 40),
       "Engineering office": (70, 70), "Shipping": (20, -6), "Parts crib": (40, 10)}
# Path of one returned part (current) and proposed (repair bench moved next to the lab, triage at receiving).
PATH_BEFORE = ["Dock", "Receiving", "Quality lab", "Engineering office", "Quality lab", "Repair bench",
               "Parts crib", "Repair bench", "Quality lab", "Shipping"]
LOC_AFTER = dict(LOC, **{"Repair bench": (60, 22), "Parts crib": (46, 22)})
PATH_AFTER = ["Dock", "Receiving", "Quality lab", "Repair bench", "Parts crib", "Repair bench",
              "Quality lab", "Shipping"]  # engineering approval done electronically

# VOC: survey of 120 customers - "the longest RMA turnaround (days, door to door) you would accept".
_rng = np.random.default_rng(42)
MAX_ACCEPTABLE_DAYS = np.clip(np.round(_rng.lognormal(math.log(9), 0.35, 120)), 3, 30)


# ---------------------------------------------------------------- functions
def va_analysis(steps=STEPS):
    work = {"VA": 0, "BVA": 0, "NVA": 0}
    count = {"VA": 0, "BVA": 0, "NVA": 0}
    wait_h = 0
    for _, _, w, wt, c in steps:
        work[c] += w
        count[c] += 1
        wait_h += wt
    total_work = sum(work.values())
    lead_h = wait_h + total_work / 60
    return work, count, total_work, wait_h, lead_h


def handoffs(steps=STEPS):
    return sum(1 for a, b in zip(steps, steps[1:]) if a[1] != b[1])


def path_length(path, loc):
    d = 0.0
    for a, b in zip(path, path[1:]):
        (x1, y1), (x2, y2) = loc[a], loc[b]
        d += abs(x1 - x2) + abs(y1 - y2)  # rectilinear (aisles)
    return d


# ---------------------------------------------------------------- examples
def ex_va():
    work, count, tw, wait, lead = va_analysis()
    return {"steps": len(STEPS), "steps by class": count, "work minutes by class": work,
            "total work (min)": tw, "total waiting (h)": wait, "lead time (h)": round(lead, 1),
            "lead time (calendar days)": round(lead / 24, 1),
            "VA share of work": f"{100 * work['VA'] / tw:.1f}%",
            "VA time / lead time (PCE)": f"{100 * (work['VA'] / 60) / lead:.2f}%",
            "handoffs between owners": handoffs()}


def ex_spaghetti():
    b = path_length(PATH_BEFORE, LOC)
    a = path_length(PATH_AFTER, LOC_AFTER)
    return {"distance before (m)": b, "distance after (m)": a, "reduction": f"{100 * (1 - a / b):.0f}%",
            "moves before": len(PATH_BEFORE) - 1, "moves after": len(PATH_AFTER) - 1}


def ex_vsm():
    # Rolled %C&A: share of work passed downstream that is complete & accurate.
    ca = {"Log request": 0.55, "Issue RMA": 0.95, "Receive": 0.90, "Diagnose": 0.92, "Approve": 0.85,
          "Repair": 0.97, "Ship": 0.99}
    rolled = float(np.prod(list(ca.values())))
    work, count, tw, wait, lead = va_analysis()
    return {"%C&A by step": ca, "rolled %C&A": f"{100 * rolled:.1f}%",
            "lead time (calendar days)": round(lead / 24, 1), "process time (h)": round(tw / 60, 1)}


def ex_spec():
    x = MAX_ACCEPTABLE_DAYS
    pct = {p: float(np.percentile(x, p)) for p in (5, 10, 25, 50)}
    work, count, tw, wait, lead = va_analysis()
    current = lead / 24
    share_ok_now = float((x >= current).mean())
    return {"n": len(x), "median acceptable (days)": pct[50], "10th percentile": pct[10],
            "5th percentile": pct[5], "25th percentile": pct[25],
            "current lead time (days)": round(current, 1),
            "share of customers satisfied by current lead time": f"{100 * share_ok_now:.0f}%",
            "share satisfied at 7 days": f"{100 * float((x >= 7).mean()):.0f}%",
            "share satisfied at 5 days": f"{100 * float((x >= 5).mean()):.0f}%"}


EX = {"va": ex_va, "spaghetti": ex_spaghetti, "vsm": ex_vsm, "spec": ex_spec}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                print(f"  {a}: {b}")
