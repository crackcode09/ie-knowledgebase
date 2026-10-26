"""lean.py - calculation and simulation toolkit for the Lean Methods Accelerator course.

Running case: a hydraulic-manifold plant (machining, deburr, wash, leak test, assembly)
supplying three product families to equipment builders through distributors.

    python tools/lean.py all          # every worked example
    python tools/lean.py <name>       # see EX at the bottom

License: MIT
"""
from __future__ import annotations

import heapq
import math
import sys

import numpy as np

# =============================================================== Session 1
COPQ = {  # annual cost (USD) by category; sales = 24,000,000
    "Prevention": {"Training": 40_000, "FMEA / design reviews": 25_000, "Supplier quality program": 35_000},
    "Appraisal": {"Incoming inspection": 120_000, "In-process leak test": 260_000, "Final audit": 90_000,
                  "Gauge calibration": 30_000},
    "Internal failure": {"Scrap": 410_000, "Rework (re-machining, re-test)": 330_000,
                         "Expedited internal moves": 60_000, "Downtime from defects": 140_000},
    "External failure": {"Warranty returns": 280_000, "Field service": 150_000, "Customer penalties": 90_000,
                         "Lost orders (estimated)": 400_000},
}
SALES = 24_000_000


def ex_copq():
    tot = {k: sum(v.values()) for k, v in COPQ.items()}
    g = sum(tot.values())
    return {"by category (USD)": tot, "total COPQ (USD)": g, "COPQ % of sales": round(100 * g / SALES, 1),
            "failure share of COPQ": f"{100 * (tot['Internal failure'] + tot['External failure']) / g:.0f}%",
            "prevention share of COPQ": f"{100 * tot['Prevention'] / g:.1f}%"}


# =============================================================== Session 2
AVAILABLE_MIN = 2 * 8 * 60 - 2 * 40   # two 8-h shifts minus breaks/meetings = 880 min
DEMAND = 220                           # manifolds per day (all families)

VSM = [  # step, C/T (min), C/O (min), uptime, operators, inventory before (units)
    ("Saw blanks", 1.2, 15, 0.98, 1, 900),
    ("CNC machining", 6.3, 90, 0.77, 2, 640),
    ("Deburr", 3.1, 0, 1.00, 1, 300),
    ("Wash", 2.0, 10, 0.95, 1, 260),
    ("Leak test", 3.4, 20, 0.92, 1, 180),
    ("Assemble & pack", 3.6, 15, 0.97, 1, 520),
]


def takt(avail=AVAILABLE_MIN, demand=DEMAND):
    return avail / demand  # minutes


def ex_vsm():
    t = takt()
    lead = sum(r[5] for r in VSM) / DEMAND
    va = sum(r[1] for r in VSM)
    rows = []
    for name, ct, co, up, ops, inv in VSM:
        eff = ct / ops / up
        rows.append((name, ct, ops, up, round(eff, 2), "OVER TAKT" if eff > t else "", round(inv / DEMAND, 2)))
    return {"takt (min)": round(t, 2), "rows (step, C/T, operators, uptime, eff. C/T per operator, flag, inv days)": rows,
            "total inventory": sum(r[5] for r in VSM), "lead time (days)": round(lead, 2),
            "processing time (min)": round(va, 1),
            "PCE": f"{100 * va / (lead * AVAILABLE_MIN):.2f}%"}


DOWNTIME_MIN = {"Tool breakage": 1260, "Changeover overrun": 980, "Waiting for material": 720, "Coolant / chips": 510,
                "Program errors": 340, "Gauge problems": 210, "Other": 180}


def ex_pareto():
    items = sorted(DOWNTIME_MIN.items(), key=lambda kv: -kv[1])
    g = sum(DOWNTIME_MIN.values())
    cum, rows = 0, []
    for k, v in items:
        cum += v
        rows.append((k, v, round(100 * v / g, 1), round(100 * cum / g, 1)))
    return {"CNC downtime, 4 weeks (min)": rows}


BENCH = {  # metric: (us, benchmark, unit, higher_is_better)
    "On-time delivery": (82, 97, "%", True),
    "Lead time": (13.4, 4.0, "days", False),
    "First-pass yield": (91.5, 98.5, "%", True),
    "Inventory turns": (6.1, 14.0, "turns/yr", True),
    "CNC changeover": (90, 20, "min", False),
}


def ex_benchmark():
    rows = []
    for k, (us, b, u, hib) in BENCH.items():
        gap = (b - us) if hib else (us - b)
        rows.append((k, us, b, u, round(gap, 1), f"{100 * gap / (b if hib else us):.0f}%"))
    return {"metric, us, benchmark, unit, gap, gap %": rows}


# Line balancing for assembly & pack (seconds) - after heijunka the mix is level
ASSY_ELEMENTS = [("Install plugs", 38), ("Install cartridge valves", 64), ("Torque", 41), ("Install seals", 29),
                 ("Functional test", 72), ("Label & serialize", 18), ("Pack", 33)]


def ex_balance():
    t = takt() * 60  # seconds
    total = sum(e[1] for e in ASSY_ELEMENTS)
    nmin = math.ceil(total / t)
    st, cur, load = [], [], 0
    for n, s in ASSY_ELEMENTS:
        if load + s > 0.95 * t and cur:
            st.append((cur, load))
            cur, load = [], 0
        cur.append(n)
        load += s
    st.append((cur, load))
    return {"takt (s)": round(t, 1), "work content (s)": total, "min operators": nmin,
            "stations": st, "efficiency": f"{100 * total / (len(st) * t):.1f}%"}


# =============================================================== Session 3
def bullwhip(weeks=104, seed=3, lead=2, alpha=0.3, review=1):
    """Retailer -> Distributor -> Factory. Each echelon forecasts with exponential smoothing
    and uses an order-up-to policy. Returns the variance of orders at each echelon."""
    rng = np.random.default_rng(seed)
    demand = np.clip(rng.normal(100, 10, weeks), 0, None)
    stream = demand
    variances = {"Customer demand": float(np.var(demand[20:]))}
    for name in ("Retailer orders", "Distributor orders", "Factory production"):
        f = stream[0]
        prev_target = f * (lead + review)
        orders = []
        for d in stream:
            f = alpha * d + (1 - alpha) * f
            target = f * (lead + review)
            o = max(0.0, d + (target - prev_target))
            prev_target = target
            orders.append(o)
        stream = np.array(orders)
        variances[name] = float(np.var(stream[20:]))
    base = variances["Customer demand"]
    return {k: (round(v, 1), round(v / base, 2)) for k, v in variances.items()}


def ex_bullwhip():
    return {"variance, ratio to customer demand": bullwhip()}


# Product-process matrix: 10 part numbers x 7 machines (1 = uses machine)
PARTS = ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10"]
MACHINES = ["Saw", "HMC-1", "VMC-2", "Lathe", "Deburr", "Hone", "Anodize"]
PPM = np.array([
    [1, 1, 0, 0, 1, 0, 0],  # P1
    [0, 0, 1, 1, 1, 0, 1],  # P2
    [1, 1, 0, 0, 1, 1, 0],  # P3
    [0, 0, 1, 1, 0, 0, 1],  # P4
    [1, 1, 0, 0, 1, 1, 0],  # P5
    [0, 0, 1, 1, 1, 0, 1],  # P6
    [1, 1, 0, 0, 0, 1, 0],  # P7
    [0, 0, 1, 1, 1, 0, 1],  # P8
    [1, 1, 0, 0, 1, 0, 0],  # P9
    [0, 1, 1, 1, 0, 0, 1],  # P10 (exceptional: needs HMC-1 too)
])


def rank_order_clustering(m, max_iter=20):
    """King's (1980) rank order clustering: reorder rows and columns by binary weight until stable."""
    rows, cols = np.arange(m.shape[0]), np.arange(m.shape[1])
    for _ in range(max_iter):
        w_r = (m[rows][:, cols] * (2 ** np.arange(len(cols))[::-1])).sum(1)
        new_rows = rows[np.argsort(-w_r, kind="stable")]
        w_c = (m[new_rows][:, cols].T * (2 ** np.arange(len(new_rows))[::-1])).sum(1)
        new_cols = cols[np.argsort(-w_c, kind="stable")]
        if (new_rows == rows).all() and (new_cols == cols).all():
            break
        rows, cols = new_rows, new_cols
    return rows, cols


def ex_cells():
    r, c = rank_order_clustering(PPM)
    mat = PPM[r][:, c]
    lines = ["      " + " ".join(f"{MACHINES[j][:6]:>6}" for j in c)]
    for i, ri in enumerate(r):
        lines.append(f"{PARTS[ri]:>5} " + " ".join(f"{'X' if v else '.':>6}" for v in mat[i]))
    return {"clustered matrix": lines}


SMED_EL = [("Find program, tools, fixture", 18, "E"), ("Remove fixture", 9, "I"), ("Clean table", 6, "I"),
           ("Fetch and preset tools at machine", 22, "E->"), ("Mount fixture, indicate (dial in)", 17, "I"),
           ("Touch-off tools", 8, "I"), ("First-part run and inspection", 10, "I")]
SMED_AFTER = {"Mount fixture, indicate (dial in)": 4, "Touch-off tools": 2, "First-part run and inspection": 6,
              "Remove fixture": 4, "Clean table": 4}


def ex_smed():
    before = sum(t for _, t, _ in SMED_EL)
    internal_sep = sum(t for _, t, k in SMED_EL if k == "I")
    after = sum(SMED_AFTER.get(n, t) for n, t, k in SMED_EL if k == "I")
    # EPEI: every-part-every-interval with 3 families at the CNC
    avail = AVAILABLE_MIN * 2 * 0.92  # 2 CNCs, 8% breakdown loss (changeovers counted separately)
    run = DEMAND * 6.3
    spare = avail - run
    epei_before = 3 * 90 / spare
    epei_after = 3 * after / spare
    return {"breakdown-adjusted CNC time (min/day)": round(avail), "run time needed (min/day)": round(run),
            "changeover as practised (min)": before, "internal after separating (min)": internal_sep,
            "internal after converting/streamlining (min)": after,
            "spare CNC min/day for changeovers": round(spare), "EPEI before (days)": round(epei_before, 2),
            "EPEI after (days)": round(epei_after, 2)}


def ex_toc():
    t = takt()
    eff = [(n, round(ct / ops / up, 2)) for n, ct, co, up, ops, inv in VSM]
    eff.sort(key=lambda x: -x[1])
    cap = AVAILABLE_MIN / eff[0][1]
    return {"effective C/T per operator (min)": eff, "takt": round(t, 2), "constraint capacity/day": round(cap),
            "drum-buffer-rope": "drum = CNC pace; buffer = ~4 h of work before CNC; rope = release blanks at CNC pace"}


def simulate_line(policy, wip_cap=None, n_jobs=20000, seed=11, interarrival=4.3):
    """Event-driven simulation of a 3-station serial line (single server each, FIFO).
    Orders arrive at random (exponential, mean `interarrival` min). Push: every order is released
    to the floor on arrival. CONWIP: an order is released only when WIP on the floor < wip_cap;
    otherwise it waits in the order backlog (not on the floor). Service times gamma, cv 0.7.
    Returns floor WIP, floor flow time (release->finish) and total order lead time (arrival->finish)."""
    rng = np.random.default_rng(seed)
    means = [3.5, 3.9, 3.3]  # minutes; station 2 is the bottleneck (u = 3.9/4.3 = 0.91)
    shape = 1 / 0.7 ** 2
    arrivals = np.cumsum(rng.exponential(interarrival, n_jobs))
    svc = np.array([rng.gamma(shape, m / shape, n_jobs) for m in means])
    free = [0.0, 0.0, 0.0]
    release = np.empty(n_jobs)
    finish = np.empty(n_jobs)
    done_heap = []  # finish times of jobs on the floor (for CONWIP release)
    for j in range(n_jobs):
        r = arrivals[j]
        if policy == "conwip":
            # remove jobs already finished by time r; if floor is full, wait for the earliest finish
            while done_heap and done_heap[0] <= r:
                heapq.heappop(done_heap)
            if len(done_heap) >= wip_cap:
                r = max(r, heapq.heappop(done_heap))
                while done_heap and done_heap[0] <= r:
                    heapq.heappop(done_heap)
        release[j] = r
        t = r
        for i in range(3):
            start = max(t, free[i])
            free[i] = start + svc[i, j]
            t = free[i]
        finish[j] = t
        if policy == "conwip":
            heapq.heappush(done_heap, t)
    w = n_jobs // 10
    floor_ft = finish[w:] - release[w:]
    lead = finish[w:] - arrivals[w:]
    span_min = finish[-1] - finish[w]
    th_per_min = (n_jobs - w) / span_min
    return {"throughput/day": round(th_per_min * AVAILABLE_MIN, 1),
            "avg floor WIP": round(float(th_per_min * floor_ft.mean()), 1),
            "avg floor flow time (min)": round(float(floor_ft.mean()), 0),
            "avg order lead time incl. backlog (min)": round(float(lead.mean()), 0)}


def ex_conwip():
    return {"push": simulate_line("push"), "CONWIP cap 20": simulate_line("conwip", 20),
            "CONWIP cap 10": simulate_line("conwip", 10), "CONWIP cap 4": simulate_line("conwip", 4)}


def kanban_cards(daily, lead_days, safety, qty):
    return math.ceil(daily * lead_days * (1 + safety) / qty)


def ex_pull():
    # family mix per day and heijunka pattern (pitch = pack qty x takt)
    mix = {"A (compact)": 110, "B (standard)": 77, "C (heavy)": 33}
    pack = 11
    pitch = pack * takt()
    slots = int(AVAILABLE_MIN // pitch)
    seq = []
    counts = {k: 0 for k in mix}
    targets = {k: v / pack for k, v in mix.items()}
    for s in range(1, slots + 1):  # goal-chasing: pick family furthest behind its ideal pace
        best = max(mix, key=lambda k: targets[k] * s / slots - counts[k])
        counts[best] += 1
        seq.append(best[0])
    return {"takt (min)": round(takt(), 2), "pitch (min, pack of 11)": round(pitch, 1), "slots/day": slots,
            "heijunka sequence": "".join(seq), "containers by family": counts,
            "kanban cards (supermarket, family A)": kanban_cards(110, 1.0, 0.25, pack)}


def ex_tpm():
    # CNC-1, 4 weeks
    planned_h, failures, repair_h = 320.0, 14, 31.5
    run_h = planned_h - repair_h
    mtbf, mttr = run_h / failures, repair_h / failures
    avail = mtbf / (mtbf + mttr)
    # six big losses for one shift (480 min planned, 440 after planned stops)
    losses = {"Breakdowns": 38, "Setup & adjustment": 52, "Minor stops & idling": 27, "Reduced speed": 31,
              "Process defects (scrap/rework)": 14, "Startup losses": 9}
    loading = 440
    oee = (loading - sum(losses.values())) / loading
    return {"MTBF (h)": round(mtbf, 1), "MTTR (h)": round(mttr, 2), "inherent availability": round(avail, 3),
            "six big losses (min/shift)": losses, "valuable operating time (min)": loading - sum(losses.values()),
            "OEE (time-loss method)": round(oee, 3)}


def ex_standard_work():
    t = takt() * 60
    steps = [("Unload/load CNC", 35, 0), ("Walk to deburr", 0, 6), ("Deburr ports", 110, 0), ("Walk to wash", 0, 5),
             ("Load wash", 20, 0), ("Walk to leak test", 0, 6), ("Leak test load/unload", 40, 0), ("Walk back to CNC", 0, 8)]
    manual = sum(s[1] for s in steps)
    walk = sum(s[2] for s in steps)
    return {"takt (s)": round(t), "manual (s)": manual, "walk (s)": walk, "operator cycle (s)": manual + walk,
            "margin to takt (s)": round(t - manual - walk)}


EX = {"copq": ex_copq, "vsm": ex_vsm, "pareto": ex_pareto, "benchmark": ex_benchmark, "balance": ex_balance,
      "bullwhip": ex_bullwhip, "cells": ex_cells, "smed": ex_smed, "toc": ex_toc, "conwip": ex_conwip,
      "pull": ex_pull, "tpm": ex_tpm, "standardwork": ex_standard_work}

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
