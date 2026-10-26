"""ie.py - calculation toolkit for the Introduction to Industrial Engineering course.

Running case: the kit-packing department of an industrial-parts manufacturer
(operators pick, inspect, bag and box service kits), plus a few service examples.

    python tools/ie.py all        # every worked example
    python tools/ie.py <name>     # timestudy, samplesize, worksampling, learning, staffing,
                                  # niosh, anthropometry, layout, jobeval, wagecurve, incentives

License: MIT
"""
from __future__ import annotations

import itertools
import math
import sys

import numpy as np
from scipy import stats

# ---------------------------------------------------------------- work measurement
# Time study: 4 elements of "pack a service kit", 10 observed cycles (seconds, continuous stopwatch converted).
ELEMENTS = {
    "Get bag and label":        [6.2, 5.8, 6.5, 6.0, 6.1, 5.9, 6.4, 6.3, 5.7, 6.1],
    "Pick 8 parts from bins":   [21.5, 22.8, 20.9, 23.4, 21.8, 22.1, 35.0, 21.2, 22.6, 21.9],  # cycle 7: dropped part
    "Inspect & bag parts":      [14.2, 13.8, 15.1, 14.6, 13.9, 14.4, 14.0, 14.8, 14.1, 14.3],
    "Seal, label, place in box": [9.1, 8.7, 9.4, 9.0, 8.8, 9.3, 9.2, 8.9, 9.5, 9.0],
}
RATINGS = {"Get bag and label": 1.00, "Pick 8 parts from bins": 1.10, "Inspect & bag parts": 0.95,
           "Seal, label, place in box": 1.05}
ALLOWANCE = 0.15  # personal, fatigue and delay (PF&D), as a fraction of normal time


def time_study(elements=ELEMENTS, ratings=RATINGS, allowance=ALLOWANCE, drop_abnormal=True):
    rows, normal_total = [], 0.0
    for name, obs in elements.items():
        x = np.array(obs)
        if drop_abnormal:
            med = np.median(x)
            x = x[np.abs(x - med) < 0.3 * med]   # remove irregular readings (> 30% from median)
        ot = x.mean()
        nt = ot * ratings[name]
        normal_total += nt
        rows.append((name, len(x), round(ot, 2), ratings[name], round(nt, 2), round(x.std(ddof=1), 2)))
    st = normal_total * (1 + allowance)
    return rows, normal_total, st


def ex_timestudy():
    rows, nt, st = time_study()
    return {"element, n used, observed mean, rating, normal time, sd": rows,
            "normal time per kit (s)": round(nt, 2), "allowance": f"{ALLOWANCE:.0%}",
            "standard time per kit (s)": round(st, 2), "standard time (min)": round(st / 60, 3),
            "standard output per hour": round(3600 / st, 1)}


def cycles_needed(x, accuracy=0.05, conf=0.95):
    """Number of cycles for the mean to be within +/- accuracy (fraction) at the given confidence."""
    x = np.asarray(x, float)
    z = stats.norm.ppf(1 - (1 - conf) / 2)
    return math.ceil((z * x.std(ddof=1) / (accuracy * x.mean())) ** 2)


def ex_samplesize():
    out = {}
    for name, obs in ELEMENTS.items():
        x = np.array(obs)
        med = np.median(x)
        x = x[np.abs(x - med) < 0.3 * med]
        out[name] = cycles_needed(x)
    return {"cycles needed for +/-5% at 95%": out}


def ex_worksampling():
    # 400 random observations of the 6 packers over 2 weeks
    obs = {"Packing (productive)": 284, "Waiting for parts": 46, "Searching / walking": 30,
           "Rework": 12, "Personal": 20, "Other": 8}
    n = sum(obs.values())
    p_wait = obs["Waiting for parts"] / n
    z = 1.96
    moe = z * math.sqrt(p_wait * (1 - p_wait) / n)
    # sample size needed to estimate "productive" within +/-3 points
    p_prod = obs["Packing (productive)"] / n
    n_req = math.ceil(z * z * p_prod * (1 - p_prod) / 0.03 ** 2)
    return {"observations": n, "shares": {k: round(v / n, 3) for k, v in obs.items()},
            "waiting share 95% CI": (round(p_wait - moe, 3), round(p_wait + moe, 3)),
            "obs needed for productive share +/-3 pts": n_req}


def learning_curve(t1, rate, n):
    b = math.log(rate) / math.log(2)
    return t1 * n ** b


def ex_learning():
    t1 = 4.0  # minutes for the first kit of a new, complex kit type
    rate = 0.85
    pts = {n: round(learning_curve(t1, rate, n), 2) for n in (1, 2, 4, 8, 16, 32, 64, 128)}
    cum100 = sum(learning_curve(t1, rate, n) for n in range(1, 101))
    return {"unit time (min) at n, 85% curve, first unit 4.0 min": pts,
            "total time for first 100 kits (min)": round(cum100, 1), "average per kit, first 100": round(cum100 / 100, 2)}


def ex_staffing():
    rows, nt, st = time_study()
    demand_day = 5200     # kits per day, two shifts
    per_shift = demand_day / 2
    avail = 450 * 60      # seconds per shift
    eff = 0.90            # planned efficiency (training, absenteeism buffer)
    n = per_shift * st / (avail * eff)  # operators per shift
    return {"standard time (s)": round(st, 2), "demand/day": demand_day, "demand/shift": per_shift,
            "takt per shift (s)": round(avail / per_shift, 2),
            "operators needed per shift": round(n, 2), "staff per shift (rounded up)": math.ceil(n)}


# ---------------------------------------------------------------- workplace design
def niosh_rwl(H, V, D, A, FM, CM, LC=23.0):
    """Revised NIOSH lifting equation (metric). H, V, D in cm; A in degrees."""
    HM = min(1.0, 25 / H)
    VM = 1 - 0.003 * abs(V - 75)
    DM = min(1.0, 0.82 + 4.5 / D)
    AM = 1 - 0.0032 * A
    rwl = LC * HM * VM * DM * AM * FM * CM
    return rwl, dict(HM=round(HM, 3), VM=round(VM, 3), DM=round(DM, 3), AM=round(AM, 3), FM=FM, CM=CM)


def ex_niosh():
    load = 14.0  # kg: full box of kits
    # Before: box lifted from floor pallet (V=15 cm) to conveyor at 95 cm, reaching 50 cm, 45 deg twist
    rwl_b, m_b = niosh_rwl(H=50, V=15, D=80, A=45, FM=0.85, CM=0.95)
    # After: pallet on a spring-loaded leveler (V=70), box pulled close (H=30), no twist, small travel
    rwl_a, m_a = niosh_rwl(H=30, V=70, D=25, A=0, FM=0.85, CM=0.95)
    return {"load (kg)": load,
            "before: multipliers": m_b, "before: RWL (kg)": round(rwl_b, 2), "before: lifting index": round(load / rwl_b, 2),
            "after: multipliers": m_a, "after: RWL (kg)": round(rwl_a, 2), "after: lifting index": round(load / rwl_a, 2)}


def ex_anthropometry():
    # Illustrative standing elbow height (cm) for the workforce: assume normal, mean and sd per group
    groups = {"Female": (101.0, 4.5), "Male": (109.0, 5.0)}
    out = {}
    for g, (m, s) in groups.items():
        out[g] = {p: round(m + stats.norm.ppf(p / 100) * s, 1) for p in (5, 50, 95)}
    lo = out["Female"][5]
    hi = out["Male"][95]
    return {"elbow height percentiles (cm)": out,
            "light assembly surface ~5-10 cm below elbow -> adjustable range (cm)": (round(lo - 10), round(hi - 5))}


# ---------------------------------------------------------------- facility layout
DEPTS = ["Receiving", "Stores", "Kitting", "Packing", "QC", "Shipping"]
FROM_TO = np.array([  # trips per day between departments (symmetric flow intensity)
    [0, 60, 0, 0, 8, 0],
    [60, 0, 90, 10, 0, 0],
    [0, 90, 0, 120, 15, 0],
    [0, 10, 120, 0, 25, 110],
    [8, 0, 15, 25, 0, 5],
    [0, 0, 0, 110, 5, 0],
])
LAYOUT_A = {"Receiving": (0, 0), "Stores": (2, 1), "Kitting": (0, 1), "Packing": (2, 0), "QC": (1, 1), "Shipping": (1, 0)}


def load_distance(layout, ft=FROM_TO, cell=15.0):
    tot = 0.0
    for i, j in itertools.combinations(range(len(DEPTS)), 2):
        (x1, y1), (x2, y2) = layout[DEPTS[i]], layout[DEPTS[j]]
        tot += ft[i, j] * (abs(x1 - x2) + abs(y1 - y2)) * cell
    return tot


def best_layout():
    spots = [(x, y) for y in (0, 1) for x in (0, 1, 2)]
    best = None
    for perm in itertools.permutations(spots):
        lay = dict(zip(DEPTS, perm))
        ld = load_distance(lay)
        if best is None or ld < best[0]:
            best = (ld, lay)
    return best


def ex_layout():
    a = load_distance(LAYOUT_A)
    b, lay = best_layout()
    grid = [[None] * 3 for _ in range(2)]
    for d, (x, y) in lay.items():
        grid[y][x] = d
    return {"layout A load-distance (trip-m/day)": round(a), "best layout load-distance": round(b),
            "reduction": f"{100 * (1 - b / a):.0f}%", "best layout grid (row 0, row 1)": grid}


# ---------------------------------------------------------------- jobs and pay
FACTORS = {  # factor weight in %; points = sum(weight x degree), degrees 1-5 -> 100-500 points
    "Knowledge & skill": 35, "Responsibility": 25, "Effort (mental & physical)": 20, "Working conditions": 20}
JOBS = {  # degrees 1-5 per factor; current hourly pay (USD)
    "Kit packer":            ([2, 2, 3, 2], 18.50),
    "Material handler":      ([2, 2, 4, 3], 19.75),
    "Inspector":             ([3, 3, 2, 2], 21.00),
    "Machine operator":      ([3, 3, 3, 3], 23.25),
    "Setup technician":      ([4, 4, 3, 3], 27.00),
    "Maintenance technician": ([5, 4, 3, 4], 31.50),
    "Team leader":           ([4, 5, 3, 2], 25.00),   # under-paid relative to points
}


def job_points():
    w = np.array(list(FACTORS.values()))
    return {j: int((w * np.array(d)).sum()) for j, (d, _) in JOBS.items()}


def ex_jobeval():
    pts = job_points()
    return {"points (100-500 scale)": dict(sorted(pts.items(), key=lambda kv: kv[1]))}


def ex_wagecurve():
    pts = job_points()
    x = np.array([pts[j] for j in JOBS])
    y = np.array([p for _, p in JOBS.values()])
    res = stats.linregress(x, y)
    out = {}
    for j, (d, pay) in JOBS.items():
        pred = res.intercept + res.slope * pts[j]
        out[j] = (pts[j], pay, round(pred, 2), f"{100 * (pay - pred) / pred:+.1f}%")
    return {"wage line": f"pay = {res.intercept:.2f} + {res.slope:.4f} x points (R^2 = {res.rvalue**2:.2f})",
            "job: points, pay, line, deviation": out}


def ex_incentives():
    base_rate = 18.50       # $/h
    std_min = 0.81          # standard minutes per kit (from the time study, rounded)
    hours = 8
    kits = 680              # produced in the shift
    std_hours = kits * std_min / 60
    eff = std_hours / hours
    out = {"standard hours earned": round(std_hours, 2), "efficiency": f"{eff:.0%}"}
    out["day rate"] = round(base_rate * hours, 2)
    out["100% premium (standard hour plan)"] = round(base_rate * max(hours, std_hours), 2)
    saved = max(0.0, std_hours - hours)
    out["Halsey 50% plan"] = round(base_rate * hours + 0.5 * saved * base_rate, 2)
    out["Rowan plan"] = round(base_rate * hours * (1 + saved / std_hours) if std_hours > 0 else 0, 2)
    return out


EX = {"timestudy": ex_timestudy, "samplesize": ex_samplesize, "worksampling": ex_worksampling,
      "learning": ex_learning, "staffing": ex_staffing, "niosh": ex_niosh, "anthropometry": ex_anthropometry,
      "layout": ex_layout, "jobeval": ex_jobeval, "wagecurve": ex_wagecurve, "incentives": ex_incentives}

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
