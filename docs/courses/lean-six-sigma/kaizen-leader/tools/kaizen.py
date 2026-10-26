"""kaizen.py - calculation toolkit for the Kaizen Leader course.

Running case: a kaizen event on the carriage assembly & pack cell (linear guide carriages).

    python tools/kaizen.py all       # every worked example
    python tools/kaizen.py <name>    # baseline, vsm, toc, spaghetti, balance, kanban, smed, oee, xmr, fivesS

License: MIT
"""
from __future__ import annotations

import math
import sys

import numpy as np

# ------------------------------------------------------------------ case data
AVAILABLE_MIN = 2 * 7.5 * 60 - 2 * 30          # two 7.5 h shifts minus two 30-min breaks/meetings = 840 min
DEMAND_PER_DAY = 560

# Current-state value stream (Day 1). Cycle time (C/T, sec/unit), changeover (C/O, min), uptime, inventory before step.
VSM = [
    # name,               C/T s, C/O min, uptime, operators, inventory_before (units)
    ("Kitting",             40,   0,   1.00, 1, 1800),
    ("Ball insert",         75,  35,   0.92, 1,  900),
    ("Preload set",         95,  50,   0.85, 1,  650),
    ("Seal & lube",         60,  10,   0.95, 1,  420),
    ("Friction test",       70,  15,   0.90, 1,  300),
    ("Pack",                45,   5,   1.00, 1,  1100),   # finished goods before shipping
]

# Spaghetti diagram: distances walked per unit (m) before and after re-layout.
SPAGHETTI_BEFORE = {"Kitting->Ball insert": 18, "Ball insert->Preload": 12, "Preload->Seal": 22,
                    "Seal->Test": 9, "Test->Pack": 25, "Fetch parts (avg/unit)": 14}
SPAGHETTI_AFTER = {"Kitting->Ball insert": 2, "Ball insert->Preload": 1.5, "Preload->Seal": 1.5,
                   "Seal->Test": 1.5, "Test->Pack": 2, "Fetch parts (avg/unit)": 3}

# Work elements for re-balancing (sec), after waste removal on Day 3.
ELEMENTS = [("Kit parts", 32), ("Insert balls", 48), ("Load fixture", 14), ("Set preload", 58),
            ("Fit seals", 22), ("Lubricate", 20), ("Friction test", 52), ("Label", 10), ("Pack", 30)]

# Quick changeover (preload station): elements in seconds and whether they can be made external.
SMED = [("Find next fixture and gauge", 540, "external"), ("Remove old fixture", 300, "internal"),
        ("Clean locating surfaces", 240, "internal"), ("Fetch shims from crib", 420, "external"),
        ("Mount new fixture (8 bolts)", 600, "internal->convert"), ("Set preload, trial parts", 900, "internal->reduce"),
        ("Paperwork", 0, "external")]
SMED_AFTER = {"Mount new fixture (8 bolts)": 120,  # quick clamps + locating pins
              "Set preload, trial parts": 360}     # preset gauge, first-part check standard

# OEE for preload station, one shift (450 min planned).
OEE = dict(planned_min=420, downtime_min=63, ideal_ct_s=95, total_units=186, good_units=178)

# Daily output (units/day) for 20 days before and 15 days after the event.
_rng = np.random.default_rng(5)
DAILY_OUTPUT = np.r_[np.round(_rng.normal(470, 28, 20)), np.round(_rng.normal(552, 18, 15))]


# ------------------------------------------------------------------ functions
def takt(available_min=AVAILABLE_MIN, demand=DEMAND_PER_DAY):
    return available_min * 60 / demand


def vsm_timeline(vsm=VSM, demand=DEMAND_PER_DAY):
    rows, lead_days, va_s = [], 0.0, 0.0
    for name, ct, co, up, ops, inv in vsm:
        days = inv / demand
        lead_days += days
        va_s += ct
        rows.append((name, ct, co, up, inv, round(days, 2)))
    lead_sec = lead_days * AVAILABLE_MIN * 60 + va_s
    return rows, lead_days, va_s, va_s / lead_sec


def bottleneck(vsm=VSM):
    eff = [(name, ct / up) for name, ct, co, up, ops, inv in vsm]  # effective C/T including downtime
    return sorted(eff, key=lambda x: -x[1])


def spaghetti():
    b, a = sum(SPAGHETTI_BEFORE.values()), sum(SPAGHETTI_AFTER.values())
    return b, a, b * DEMAND_PER_DAY / 1000, a * DEMAND_PER_DAY / 1000


def balance(elements=ELEMENTS, takt_s=None):
    takt_s = takt_s or takt()
    target = takt_s * 0.95  # 5% margin for variation
    stations, cur, load = [], [], 0
    for name, t in elements:
        if load + t > target and cur:
            stations.append((cur, load))
            cur, load = [], 0
        cur.append(name)
        load += t
    stations.append((cur, load))
    total = sum(t for _, t in elements)
    return stations, total, math.ceil(total / takt_s), total / (len(stations) * takt_s)


def kanban(daily_demand, replenish_days, safety_pct, container_qty):
    n = daily_demand * replenish_days * (1 + safety_pct) / container_qty
    return math.ceil(n), n


def smed():
    before_internal = sum(t for _, t, k in SMED if k.startswith("internal"))
    before_total = sum(t for _, t, _ in SMED)
    after_internal = sum(SMED_AFTER.get(n, t) for n, t, k in SMED if k.startswith("internal"))
    return before_total / 60, before_internal / 60, after_internal / 60


def oee(planned_min, downtime_min, ideal_ct_s, total_units, good_units):
    run = planned_min - downtime_min
    a = run / planned_min
    p = (ideal_ct_s * total_units / 60) / run
    q = good_units / total_units
    return a, p, q, a * p * q


def xmr(x):
    x = np.asarray(x, float)
    mr = np.abs(np.diff(x)).mean()
    return x.mean(), mr, x.mean() - 2.66 * mr, x.mean() + 2.66 * mr


FIVE_S_AUDIT = {"Sort": (2, 4), "Set in order": (1, 4), "Shine": (2, 3), "Standardize": (1, 3), "Sustain": (1, 3)}


# ------------------------------------------------------------------ examples
def ex_baseline():
    t = takt()
    rows, lead_days, va, pce = vsm_timeline()
    return {"available min/day": AVAILABLE_MIN, "demand/day": DEMAND_PER_DAY, "takt (s)": round(t, 1),
            "total WIP (units)": sum(r[5] for r in VSM), "lead time (days)": round(lead_days, 2),
            "value-added time (s)": va, "process cycle efficiency (%)": round(100 * pce, 3)}


def ex_vsm():
    rows, lead_days, va, pce = vsm_timeline()
    return {"rows (name, C/T s, C/O min, uptime, inventory, days)": rows}


def ex_toc():
    t = takt()
    b = bottleneck()
    return {"takt (s)": round(t, 1),
            "effective C/T = C/T / uptime (s)": [(n, round(v, 1), "OVER TAKT" if v > t else "") for n, v in b],
            "capacity of bottleneck (units/day)": round(AVAILABLE_MIN * 60 / b[0][1])}


def ex_spaghetti():
    b, a, kb, ka = spaghetti()
    return {"m per unit before": b, "m per unit after": a, "km/day before": round(kb, 1),
            "km/day after": round(ka, 1), "reduction (%)": round(100 * (1 - a / b), 1)}


def ex_balance():
    st, total, nmin, eff = balance()
    t = takt()
    return {"takt (s)": round(t, 1), "planning target 95% of takt (s)": round(0.95 * t, 1),
            "total work content (s)": total, "theoretical min operators": nmin,
            "stations": [(s, l) for s, l in st], "balance efficiency (%)": round(100 * eff, 1)}


def ex_kanban():
    n, raw = kanban(DEMAND_PER_DAY, 0.5, 0.20, 40)
    return {"daily demand": DEMAND_PER_DAY, "replenishment (days)": 0.5, "safety": "20%", "container qty": 40,
            "kanban cards (raw)": round(raw, 2), "kanban cards": n, "max inventory (units)": n * 40}


def ex_smed():
    total, internal, after = smed()
    return {"total C/O work (min)": total, "internal (machine stopped) before (min)": internal,
            "internal after separating, converting, reducing (min)": after,
            "reduction in downtime per C/O (%)": round(100 * (1 - after / internal), 1)}


def ex_oee():
    a, p, q, o = oee(**OEE)
    return {"availability": round(a, 3), "performance": round(p, 3), "quality": round(q, 3), "OEE": round(o, 3)}


def ex_xmr():
    b, a = DAILY_OUTPUT[:20], DAILY_OUTPUT[20:]
    m, mr, lo, hi = xmr(b)
    above = int((a > m).sum())
    beyond = int((a > hi).sum())
    m2, mr2, lo2, hi2 = xmr(a)
    return {"before: mean, mR, LNPL, UNPL": tuple(round(v, 1) for v in (m, mr, lo, hi)),
            "after days above before-mean": f"{above} of {len(a)}", "after days above UNPL": beyond,
            "after: mean, mR, LNPL, UNPL": tuple(round(v, 1) for v in (m2, mr2, lo2, hi2)),
            "after values": a.astype(int).tolist()}


def ex_fives():
    tot_b = sum(v[0] for v in FIVE_S_AUDIT.values())
    tot_a = sum(v[1] for v in FIVE_S_AUDIT.values())
    return {"scores (before, after) out of 5": FIVE_S_AUDIT, "total before /25": tot_b, "total after /25": tot_a}


EX = {"baseline": ex_baseline, "vsm": ex_vsm, "toc": ex_toc, "spaghetti": ex_spaghetti, "balance": ex_balance,
      "kanban": ex_kanban, "smed": ex_smed, "oee": ex_oee, "xmr": ex_xmr, "fives": ex_fives}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list):
                    print(f"  {a}:")
                    for r in b:
                        print("    ", r)
                else:
                    print(f"  {a}: {b}")
