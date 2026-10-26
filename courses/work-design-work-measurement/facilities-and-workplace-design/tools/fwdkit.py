"""fwdkit.py - data and calculations for the Facilities and Workplace Design course.

Running case: Corvan Enclosures (fictional) makes steel electrical enclosures in a 50 m x 40 m plant.
Flow is convoluted after years of growth; the IE team re-plans the layout and builds a wall-box cell.

    python tools/fwdkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/fwdkit.py all           # every worked example
    python tools/fwdkit.py <name>        # pq, inventory, usage, flow, space, affinities, layout, roc,
                                         # cell_capacity, staffing, balance, configs, kanban, schedule, capstone

Requires numpy, pandas. License: MIT
"""
from __future__ import annotations

import itertools
import math
import os
import sys

import numpy as np
import pandas as pd

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

DEPTS = ["RCV", "SHR", "PUN", "BRK", "WLD", "PNT", "ASM", "TST", "PKG", "WHS", "TLR", "OFF"]
NAMES = {"RCV": "Receiving", "SHR": "Shear", "PUN": "Punch", "BRK": "Press brake", "WLD": "Weld", "PNT": "Paint",
         "ASM": "Assembly", "TST": "Test", "PKG": "Pack & ship", "WHS": "Warehouse", "TLR": "Tool room",
         "OFF": "Offices"}
ROUTES = {"F1 wall box": ["RCV", "SHR", "PUN", "BRK", "WLD", "PNT", "ASM", "TST", "PKG"],
          "F2 floor cabinet": ["RCV", "SHR", "PUN", "BRK", "WLD", "PNT", "ASM", "TST", "WHS", "PKG"],
          "F3 junction box": ["RCV", "PUN", "BRK", "PNT", "ASM", "PKG"],
          "F4 custom": ["RCV", "SHR", "BRK", "WLD", "PNT", "ASM", "TST", "PKG"]}
COLS, ROWS = 4, 3
SLOT_W, SLOT_H = 50 / COLS, 40 / ROWS                # 12.5 m x 13.33 m
FIXED = {"RCV": (0, 1), "PKG": (3, 1)}               # receiving dock west wall, shipping dock east wall
AS_IS = {"RCV": (0, 1), "PKG": (3, 1), "SHR": (3, 2), "PUN": (0, 0), "BRK": (2, 2), "WLD": (1, 0), "PNT": (3, 0),
         "ASM": (0, 2), "TST": (1, 1), "WHS": (2, 0), "TLR": (2, 1), "OFF": (1, 2)}
HANDLING_COST = 0.012                                # $ per load-metre (forklift + operator, illustrative)
WEIGHTS = {"A": 4, "E": 3, "I": 2, "O": 1, "U": 0, "X": -4}
QUAL = {("WLD", "PNT"): ("X", "sparks and fumes near wet paint and solvent"),
        ("TLR", "PUN"): ("I", "turret tooling changes"), ("TLR", "BRK"): ("I", "brake tooling changes"),
        ("OFF", "TST"): ("O", "engineering support for test"), ("OFF", "RCV"): ("O", "paperwork"),
        ("ASM", "WHS"): ("I", "purchased components kitted from warehouse")}
SHIFT_S = 7.5 * 3600
DAYS = 230


def make_data(seed=2028):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}
    # 1. products: 40 SKUs, Pareto-like volumes
    fam_n = {"F1 wall box": 12, "F2 floor cabinet": 8, "F3 junction box": 10, "F4 custom": 10}
    fam_scale = {"F1 wall box": 9000, "F2 floor cabinet": 1800, "F3 junction box": 4000, "F4 custom": 250}
    per_load = {"F1 wall box": 20, "F2 floor cabinet": 2, "F3 junction box": 40, "F4 custom": 4}
    rows, k = [], 0
    for fam, n in fam_n.items():
        vols = np.sort(rng.lognormal(np.log(fam_scale[fam]), 0.8, n))[::-1]
        for v in vols:
            k += 1
            rows.append(dict(sku=f"C{k:03d}", family=fam, annual_units=int(round(v, -1)), units_per_load=per_load[fam]))
    pd.DataFrame(rows).to_csv(os.path.join(D, "products.csv"), index=False)
    out["products"] = len(rows)
    pd.DataFrame([dict(family=f, step=i + 1, dept=d) for f, r in ROUTES.items() for i, d in enumerate(r)]).to_csv(
        os.path.join(D, "routings.csv"), index=False)

    # 2. inventory and usage (purchased and raw items)
    rows = []
    for i in range(1, 31):
        use = float(np.round(rng.lognormal(np.log(60), 1.0), 0)) + 1
        onhand = float(np.round(use * rng.uniform(5, 60)))
        vol = float(np.round(rng.uniform(0.0004, 0.006), 4))
        picks = int(use * DAYS / rng.choice([1, 5, 20, 50]))
        rows.append(dict(item=f"M{i:02d}", daily_usage=use, on_hand=onhand, unit_m3=vol, annual_picks=max(picks, 12)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "inventory.csv"), index=False)
    out["inventory"] = 30

    # 3. machine list for space requirements
    machines = {"SHR": [("Shear 3 m", 4.5, 2.5, 2)], "PUN": [("Turret punch", 6.0, 5.0, 2)],
                "BRK": [("Press brake 3 m", 4.0, 2.5, 3), ("Press brake 2 m", 3.0, 2.0, 1)],
                "WLD": [("Weld booth", 3.0, 3.0, 4), ("Spot welder", 1.5, 1.5, 2)],
                "PNT": [("Powder booth + cure oven (footprint)", 9.0, 6.0, 1)],
                "ASM": [("Assembly bench", 2.4, 1.2, 12)], "TST": [("Test bench", 2.0, 1.2, 4)],
                "TLR": [("Tool storage + bench", 4.0, 3.0, 2)]}
    rows = [dict(dept=d, machine=m, length_m=l, width_m=w, qty=q) for d, ms in machines.items() for m, l, w, q in ms]
    pd.DataFrame(rows).to_csv(os.path.join(D, "machines.csv"), index=False)
    out["machines"] = len(rows)

    # 4. part-machine incidence for cell formation (10 parts x 7 machines, 3 natural groups + 2 exceptions)
    mach = ["SHR", "PUN", "BRK", "SPOT", "PEM", "WLDB", "LASER"]
    groups = {"P01": ["SHR", "PUN", "BRK", "SPOT"], "P02": ["PEM", "LASER"], "P03": ["BRK", "WLDB", "SHR"],
              "P04": ["SHR", "PUN", "SPOT"], "P05": ["LASER", "PEM", "PUN"], "P06": ["WLDB", "BRK"],
              "P07": ["PUN", "SPOT", "BRK"], "P08": ["LASER", "PEM"], "P09": ["SHR", "WLDB", "BRK"],
              "P10": ["SHR", "PUN", "SPOT", "BRK"]}
    pd.DataFrame([{**{"part": p}, **{m: int(m in ms) for m in mach}} for p, ms in groups.items()]).to_csv(
        os.path.join(D, "part_machine_matrix.csv"), index=False)
    out["part_machine_matrix"] = 10

    # 5. wall-box cell: operations and manual elements
    ops = [("OP10", "Shear blank", 14, 10, 15), ("OP20", "Turret punch", 48, 14, 20), ("OP30", "Brake 4 bends", 18, 34, 12),
           ("OP40", "Spot weld corners", 22, 18, 8), ("OP50", "Press hardware (PEM)", 6, 20, 5),
           ("OP60", "Inspect, load to paint rack", 0, 24, 0)]
    pd.DataFrame([dict(op=o, description=d, machine_s=m, manual_s=h, setup_min=s) for o, d, m, h, s in ops]).to_csv(
        os.path.join(D, "cell_operations.csv"), index=False)
    out["cell_operations"] = len(ops)
    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"))


# ---------------------------------------------------------------- products, volumes (P-Q)
def ex_pq():
    p = load("products").sort_values("annual_units", ascending=False).reset_index(drop=True)
    p["cum_pct"] = (100 * p.annual_units.cumsum() / p.annual_units.sum()).round(1)
    n80 = int((p.cum_pct < 80).sum() + 1)
    fam = p.groupby("family").agg(skus=("sku", "count"), units=("annual_units", "sum")).reset_index()
    fam["share_pct"] = (100 * fam.units / fam.units.sum()).round(1)
    return {"total_units": int(p.annual_units.sum()), "skus": len(p), "skus_for_80pct": n80,
            "pct_skus_for_80pct": round(100 * n80 / len(p), 1), "families": fam.to_dict("records"),
            "top5": p.head(5)[["sku", "family", "annual_units"]].to_dict("records")}


# ---------------------------------------------------------------- inventory, usage
def ex_inventory(target_days=10, pallet_m3=1.2, pallet_m2=1.44, fill=0.75):
    inv = load("inventory")
    inv["days_on_hand"] = (inv.on_hand / inv.daily_usage).round(1)
    inv["target_qty"] = inv.daily_usage * target_days
    now_m3 = float((inv.on_hand * inv.unit_m3).sum())
    tgt_m3 = float((inv.target_qty * inv.unit_m3).sum())
    pal = lambda m3: math.ceil(m3 / (pallet_m3 * fill))
    return {"items": len(inv), "median_days_on_hand": float(inv.days_on_hand.median()),
            "items_over_30_days": int((inv.days_on_hand > 30).sum()),
            "inventory_m3_now": round(now_m3, 1), "inventory_m3_at_target": round(tgt_m3, 1),
            "pallet_positions_now": pal(now_m3), "pallet_positions_target": pal(tgt_m3),
            "floor_m2_now_single_stack": round(pal(now_m3) * pallet_m2, 1),
            "floor_m2_target_single_stack": round(pal(tgt_m3) * pallet_m2, 1)}


def ex_usage():
    inv = load("inventory").sort_values("annual_picks", ascending=False).reset_index(drop=True)
    inv["cum_pct"] = 100 * inv.annual_picks.cumsum() / inv.annual_picks.sum()
    inv["class"] = np.where(inv.cum_pct <= 70, "A", np.where(inv.cum_pct <= 90, "B", "C"))
    inv.loc[0, "class"] = "A"
    s = inv.groupby("class").agg(items=("item", "count"), picks=("annual_picks", "sum")).reset_index()
    s["pick_share_pct"] = (100 * s.picks / s.picks.sum()).round(1)
    return {"classes": s.to_dict("records"), "top_items": inv.head(5)[["item", "annual_picks"]].to_dict("records")}


# ---------------------------------------------------------------- flow
def flow_matrix():
    p = load("products")
    F = pd.DataFrame(0.0, index=DEPTS, columns=DEPTS)
    for fam, r in ROUTES.items():
        loads = float((p[p.family == fam].annual_units / p[p.family == fam].units_per_load).sum())
        for a, b in zip(r[:-1], r[1:]):
            F.loc[a, b] += loads
    return F.round(0)


def ex_flow():
    F = flow_matrix()
    pairs = []
    for a, b in itertools.combinations(DEPTS, 2):
        f = F.loc[a, b] + F.loc[b, a]
        if f > 0:
            pairs.append(dict(pair=f"{a}-{b}", loads_per_yr=int(f)))
    pairs.sort(key=lambda r: -r["loads_per_yr"])
    loads = {fam: int((load("products").query("family == @fam").annual_units /
                       load("products").query("family == @fam").units_per_load).sum()) for fam in ROUTES}
    back = backtracks(AS_IS)
    return {"loads_by_family": loads, "pairs": pairs, "as_is_backtrack_moves": back}


def backtracks(layout):
    """Count route steps that move west (against the receiving-to-shipping direction)."""
    n = 0
    for fam, r in ROUTES.items():
        for a, b in zip(r[:-1], r[1:]):
            if layout[b][0] < layout[a][0]:
                n += 1
    return n


# ---------------------------------------------------------------- space
def ex_space(op_allow=1.5, aisle=0.25):
    m = load("machines")
    m["area"] = m.length_m * m.width_m * m.qty
    mach = m.groupby("dept").area.sum()
    fixed = {"RCV": 110, "PKG": 140, "WHS": 0, "OFF": 120}       # m2 from dock/office standards (case values)
    whs = ex_inventory()["floor_m2_target_single_stack"] / 3 * (1 + 1.0)   # 3-high racking, 100 % aisles
    rows = []
    for d in DEPTS:
        if d in mach.index:
            a = mach[d] * (1 + op_allow) * (1 + aisle)
            basis = f"machines {mach[d]:.1f} m2 x {(1 + op_allow):.1f} x {(1 + aisle):.2f}"
        elif d == "WHS":
            a, basis = whs, "pallet positions at target days, 3-high racks, x 2 for aisles"
        else:
            a, basis = fixed[d], "standard"
        rows.append(dict(dept=d, name=NAMES[d], m2=round(a, 1), basis=basis))
    total = sum(r["m2"] for r in rows)
    return {"planning_units": rows, "total_m2": round(total, 1), "building_m2": 2000,
            "slot_m2": round(SLOT_W * SLOT_H, 1), "fits": total <= 2000}


# ---------------------------------------------------------------- affinities
def closeness():
    F = flow_matrix()
    pairs = []
    for a, b in itertools.combinations(DEPTS, 2):
        pairs.append(((a, b), F.loc[a, b] + F.loc[b, a]))
    flows = sorted([p for p in pairs if p[1] > 0], key=lambda x: -x[1])
    top = flows[0][1]
    rating = {}
    for pr, f in flows:            # flow-intensity bands relative to the largest flow (course convention)
        r = f / top
        rating[pr] = "A" if r >= 0.90 else "E" if r >= 0.75 else "I" if r >= 0.40 else "O"
    reasons = {pr: f"flow {int(f)} loads/yr" for pr, f in flows}
    for (a, b), (r, why) in QUAL.items():
        key = (a, b) if (a, b) in dict(pairs) else (b, a)
        rating[key] = r if r == "X" or WEIGHTS[r] > WEIGHTS.get(rating.get(key, "U"), 0) else rating[key]
        reasons[key] = why if rating[key] == r else reasons.get(key, "")
    return rating, reasons


def ex_affinities():
    rating, reasons = closeness()
    rows = [dict(pair=f"{a}-{b}", rating=r, reason=reasons.get((a, b), "")) for (a, b), r in
            sorted(rating.items(), key=lambda kv: -WEIGHTS[kv[1]])]
    cnt = pd.Series([r for r in rating.values()]).value_counts().to_dict()
    return {"ratings": rows, "counts": cnt, "unrated_pairs_are_U": 66 - len(rating)}


# ---------------------------------------------------------------- layout evaluation and improvement
def centre(slot):
    c, r = slot
    return ((c + 0.5) * SLOT_W, (r + 0.5) * SLOT_H)


def dist(a, b):
    (x1, y1), (x2, y2) = centre(a), centre(b)
    return abs(x1 - x2) + abs(y1 - y2)


def flow_cost(layout):
    F = flow_matrix()
    return float(sum(F.loc[a, b] * dist(layout[a], layout[b]) for a in DEPTS for b in DEPTS if F.loc[a, b] > 0))


def adjacency_score(layout):
    rating, _ = closeness()
    s = 0
    for (a, b), r in rating.items():
        if dist(layout[a], layout[b]) <= max(SLOT_W, SLOT_H) + 1e-6 and (
                layout[a][0] == layout[b][0] or layout[a][1] == layout[b][1]):
            s += WEIGHTS[r]
    return s


def x_violations(layout):
    rating, _ = closeness()
    return [f"{a}-{b}" for (a, b), r in rating.items() if r == "X" and
            dist(layout[a], layout[b]) <= max(SLOT_W, SLOT_H) + 1e-6 and
            (layout[a][0] == layout[b][0] or layout[a][1] == layout[b][1])]


def improve(layout, x_penalty=1e6, also_fixed=()):
    lay = dict(layout)
    fixed = set(FIXED) | set(also_fixed)
    cost = lambda L: flow_cost(L) + x_penalty * len(x_violations(L))
    best, it = cost(lay), 0
    while True:
        cand = None
        for a, b in itertools.combinations([d for d in DEPTS if d not in fixed], 2):
            L = dict(lay)
            L[a], L[b] = L[b], L[a]
            c = cost(L)
            if c < best - 1e-6 and (cand is None or c < cand[0]):
                cand = (c, L, (a, b))
        if cand is None:
            return lay, it
        best, lay, it = cand[0], cand[1], it + 1


def ex_layout():
    new, iters = improve(AS_IS)
    c0, c1 = flow_cost(AS_IS), flow_cost(new)
    grid = lambda L: [[next(d for d, s in L.items() if s == (c, r)) for c in range(COLS)] for r in range(ROWS)]
    keep, _ = improve(AS_IS, also_fixed=("PNT",))
    c2 = flow_cost(keep)
    return {"alt_B_paint_stays_load_m": round(c2), "alt_B_cost_$": round(c2 * HANDLING_COST),
            "alt_B_adjacency": adjacency_score(keep), "alt_B_backtracks": backtracks(keep),
            "alt_B_saving_pct": round(100 * (1 - c2 / c0), 1), "alt_B_grid_row0_to_2": grid(keep),
            "as_is_load_m": round(c0), "as_is_cost_$": round(c0 * HANDLING_COST),
            "as_is_adjacency": adjacency_score(AS_IS), "as_is_X_violations": x_violations(AS_IS),
            "as_is_backtracks": backtracks(AS_IS),
            "improved_load_m": round(c1), "improved_cost_$": round(c1 * HANDLING_COST),
            "improved_adjacency": adjacency_score(new), "improved_X_violations": x_violations(new),
            "improved_backtracks": backtracks(new), "saving_pct": round(100 * (1 - c1 / c0), 1),
            "exchanges": iters, "as_is_grid_row0_to_2": grid(AS_IS), "improved_grid_row0_to_2": grid(new)}


# ---------------------------------------------------------------- cell formation (rank order clustering)
def roc(M):
    M = M.copy()
    for _ in range(10):
        rw = M.apply(lambda r: int("".join(str(int(v)) for v in r), 2), axis=1)
        M = M.loc[rw.sort_values(ascending=False, kind="stable").index]
        cw = M.apply(lambda c: int("".join(str(int(v)) for v in c), 2), axis=0)
        new = M[cw.sort_values(ascending=False, kind="stable").index]
        if list(new.columns) == list(M.columns) and _ > 0:
            break
        M = new
    return M


def ex_roc():
    M = load("part_machine_matrix").set_index("part")
    R = roc(M)
    cells = {"Cell 1 (fabricate boxes)": ["SHR", "PUN", "SPOT"], "Cell 2 (laser + hardware)": ["LASER", "PEM"],
             "Cell 3 (welded frames)": ["BRK", "WLDB"]}
    part_cell = {}
    exc = []
    for p, row in M.iterrows():
        used = [m for m in M.columns if row[m]]
        best = max(cells, key=lambda c: sum(m in cells[c] for m in used))
        part_cell[p] = best
        exc += [f"{p}:{m}" for m in used if m not in cells[best]]
    return {"ordered_parts": list(R.index), "ordered_machines": list(R.columns),
            "matrix": R.astype(int).values.tolist(), "cells": cells, "part_cell": part_cell,
            "exceptional_elements": exc}


# ---------------------------------------------------------------- the wall-box cell
def cell_demand():
    p = load("products")
    return int(p[p.family == "F1 wall box"].annual_units.sum())


def ex_cell_capacity(shifts=2, oee_avail=0.90, lot=150):
    ops = load("cell_operations")
    demand = cell_demand()
    avail_s = DAYS * shifts * SHIFT_S
    takt = avail_s / demand
    rows = []
    for _, o in ops.iterrows():
        if o.machine_s == 0:
            rows.append(dict(op=o.op, description=o.description, s_per_pc=float(o.manual_s), capacity_per_yr=None,
                             utilization_pct=0.0, machines_needed=0))
            continue
        per_pc = o.machine_s + o.manual_s + o.setup_min * 60 / lot     # machine idle while loading/unloading
        cap = avail_s * oee_avail / per_pc
        rows.append(dict(op=o.op, description=o.description, s_per_pc=round(per_pc, 1),
                         capacity_per_yr=int(cap), utilization_pct=round(100 * demand / cap, 1),
                         machines_needed=math.ceil(demand / cap)))
    return {"demand_per_yr": demand, "available_s": avail_s, "takt_s": round(takt, 1), "ops": rows,
            "bottleneck": max(rows, key=lambda r: r["utilization_pct"])["op"]}


def ex_staffing(shifts=2):
    ops = load("cell_operations")
    takt = ex_cell_capacity(shifts)["takt_s"]
    manual = float(ops.manual_s.sum())
    walk = 6 * 2.0                       # ~6 station moves x 2 s
    ops_needed = (manual + walk) / takt
    return {"manual_s": manual, "walk_s": walk, "takt_s": takt, "operators_theoretical": round(ops_needed, 2),
            "operators": math.ceil(ops_needed), "per_shift_note": f"{math.ceil(ops_needed)} operators per shift"}


def ex_balance(n_ops=None):
    ops = load("cell_operations")
    st = ex_staffing()
    takt = st["takt_s"]
    n = n_ops or st["operators"]
    # operators take consecutive operations (U-cell lets an operator take ops from both ends)
    elems = list(zip(ops.op, ops.manual_s))
    best = None
    for split in itertools.combinations(range(1, len(elems)), n - 1):
        b = [0] + list(split) + [len(elems)]
        loads = [sum(e[1] for e in elems[b[i]:b[i + 1]]) + 2 * 2.0 * (b[i + 1] - b[i]) for i in range(n)]
        if best is None or max(loads) < max(best[1]):
            best = ([[e[0] for e in elems[b[i]:b[i + 1]]] for i in range(n)], loads)
    eff = sum(best[1]) / (n * max(best[1]))
    return {"takt_s": takt, "operators": n, "assignment": best[0], "loads_s": [round(x, 1) for x in best[1]],
            "max_load_s": round(max(best[1]), 1), "meets_takt": max(best[1]) <= takt,
            "balance_efficiency_pct": round(100 * eff, 1)}


def ex_configs(pitch=2.5, across=2.0, speed=1.2):
    """One operator running all 6 stations once per cycle and returning to the start.
    Straight line: 6 stations in a row. L-shape: 4 + 2 stations. U-shape: 3 + 3 stations facing, `across` m apart."""
    straight = 2 * 5 * pitch
    l_out = 3 * pitch + 2 * pitch
    l_back = math.hypot(3 * pitch, 2 * pitch)
    lshape = l_out + l_back
    ushape = 2 * (2 * pitch) + 2 * across
    rows = [dict(config="Straight line", walk_m=round(straight, 1)), dict(config="L-shape", walk_m=round(lshape, 1)),
            dict(config="U-shape", walk_m=round(ushape, 1))]
    for r in rows:
        r["walk_s"] = round(r["walk_m"] / speed, 1)
    return {"configs": rows, "speed_m_s": speed,
            "note": "U-shape: first and last operations side by side, so one person controls input and output"}


def ex_kanban(lead_days=1.0, safety=0.15, container=20):
    d = cell_demand() / DAYS
    n = d * lead_days * (1 + safety) / container
    return {"daily_demand": round(d, 1), "container_qty": container, "lead_time_days": lead_days,
            "safety": safety, "kanbans": math.ceil(n), "kanbans_exact": round(n, 2)}


def ex_schedule(shifts=2):
    p = load("products")
    f1 = p[p.family == "F1 wall box"]
    ops = load("cell_operations")
    setup = float(ops.setup_min.sum()) * 60           # one changeover of the whole cell (s), sequential worst case
    bottleneck_setup = float(ops.setup_min.max()) * 60
    avail = shifts * SHIFT_S
    o = ops[ops.op == "OP20"].iloc[0]
    run_day = float(o.machine_s + o.manual_s) * f1.annual_units.sum() / DAYS     # punch run time, no setups
    spare = avail * 0.9 - run_day
    skus = len(f1)
    epei_days = skus * bottleneck_setup / spare
    return {"skus": skus, "bottleneck_setup_min": bottleneck_setup / 60, "punch_run_s_per_day": round(run_day),
            "punch_spare_s_per_day": round(spare), "EPEI_days": round(epei_days, 2),
            "changeovers_possible_per_day": int(spare // bottleneck_setup)}


CAPSTONE_OPS = [("OP10", "Turret punch", 30, 10, 20), ("OP20", "Brake 2 bends", 10, 16, 10),
                ("OP30", "Press hardware", 5, 14, 5), ("OP40", "Inspect, load to paint rack", 0, 12, 0)]


def ex_capstone(shifts=1, oee_avail=0.90, lot=150, walk_per_op=2.0, container=40, safety=0.15):
    p = load("products")
    demand = int(p[p.family == "F3 junction box"].annual_units.sum())
    avail = DAYS * shifts * SHIFT_S
    takt = avail / demand
    rows, manual = [], 0.0
    for op, d, m, h, su in CAPSTONE_OPS:
        manual += h
        if m == 0:
            continue
        per = m + h + su * 60 / lot
        cap = avail * oee_avail / per
        rows.append(dict(op=op, description=d, s_per_pc=round(per, 1), capacity=int(cap),
                         utilization_pct=round(100 * demand / cap, 1)))
    work = manual + walk_per_op * len(CAPSTONE_OPS)
    kb = demand / DAYS * 1.0 * (1 + safety) / container
    return {"demand": demand, "shifts": shifts, "takt_s": round(takt, 1), "machines": rows,
            "manual_s": manual, "work_with_walk_s": work, "operators_theoretical": round(work / takt, 2),
            "operators": math.ceil(work / takt), "kanbans": math.ceil(kb), "kanbans_exact": round(kb, 2)}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating,)):
        return round(float(o), 4)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


EX = {"pq": ex_pq, "inventory": ex_inventory, "usage": ex_usage, "flow": ex_flow, "space": ex_space,
      "affinities": ex_affinities, "layout": ex_layout, "roc": ex_roc, "cell_capacity": ex_cell_capacity,
      "staffing": ex_staffing, "balance": ex_balance, "configs": ex_configs, "kanban": ex_kanban,
      "schedule": ex_schedule, "capstone": ex_capstone}

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
