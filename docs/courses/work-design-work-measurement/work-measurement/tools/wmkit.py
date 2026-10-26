"""wmkit.py - data and calculations for the Work Measurement course.

Running case: Marlow Pump Works (fictional) assembles small centrifugal pumps in a cell
and runs a kitting area. An industrial engineer sets and maintains labor standards.

    python tools/wmkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/wmkit.py all           # every worked example
    python tools/wmkit.py <name>        # timestudy, cycles, rating, allowances, labor, sampling,
                                        # sampling_std, standard_data, learning, staffing

Requires numpy, pandas, scipy, statsmodels. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

# assemble pump: elements (name, type, mean s, sd s, true performance rating of the observed operator)
ELEMENTS = [
    ("E1 Get housing, place in fixture", "manual", 6.0, 0.5),
    ("E2 Insert impeller and shaft", "manual", 14.0, 1.2),
    ("E3 Fit seal and cover, run 6 screws (power driver)", "manual", 31.0, 2.4),
    ("E4 Leak test (machine-controlled)", "machine", 45.0, 0.3),
    ("E5 Attach label, inspect visually", "manual", 9.0, 0.9),
    ("E6 Place in tote", "manual", 4.0, 0.4),
]
OPERATOR_PACE = 1.10        # observed operator works at 110% of normal pace on manual elements


def make_data(seed=1911):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)

    # 1. Continuous time study: cumulative watch readings (s) for 15 cycles, with one foreign element
    rows, clock = [], 0.0
    for cyc in range(1, 16):
        for name, kind, mu, sd in ELEMENTS:
            t = rng.normal(mu, sd)
            if kind == "manual":
                t = t / OPERATOR_PACE
            if cyc == 9 and name.startswith("E3"):
                t += 22.0                                   # driver bit dropped and replaced: foreign element
            clock += t
            rows.append(dict(cycle=cyc, element=name.split()[0], cumulative_s=round(clock, 1),
                             note="dropped bit, replaced (foreign)" if (cyc == 9 and name.startswith("E3")) else ""))
    pd.DataFrame(rows).to_csv(os.path.join(D, "time_study_continuous.csv"), index=False)
    pd.DataFrame([dict(element=n.split()[0], description=n.split(" ", 1)[1], type=k) for n, k, _, _ in ELEMENTS]).to_csv(
        os.path.join(D, "elements.csv"), index=False)

    # 2. Rating practice: 10 clips with known benchmark pace, 4 trainee analysts
    bench = np.array([80, 90, 95, 100, 100, 105, 110, 115, 120, 130])
    bias = {"Analyst A": 0, "Analyst B": -8, "Analyst C": 5, "Analyst D": 0}
    spread = {"Analyst A": 3, "Analyst B": 4, "Analyst C": 4, "Analyst D": 10}
    rows = []
    for a in bias:
        for i, b in enumerate(bench):
            rows.append(dict(clip=i + 1, analyst=a, benchmark_pct=int(b),
                             rating_pct=int(5 * round((b + bias[a] + rng.normal(0, spread[a])) / 5))))
    pd.DataFrame(rows).to_csv(os.path.join(D, "rating_practice.csv"), index=False)

    # 3. Labor reporting: 4 weeks x 8 operators: units by job, hours on standard / off standard
    ops = [f"OP{i}" for i in range(1, 9)]
    std_min = {"Pump assembly": 1.95, "Kitting": 0.80, "Packing": 0.45}
    rows = []
    for wk in range(1, 5):
        for o in ops:
            perf = rng.normal(1.0, 0.08) * (0.85 if o == "OP7" else 1.0)
            hours_on = round(rng.uniform(30, 36), 1)
            off = round(40 - hours_on, 1)
            job = rng.choice(list(std_min), p=[0.6, 0.25, 0.15])
            units = int(hours_on * 60 / std_min[job] * perf)
            rows.append(dict(week=wk, operator=o, job=job, units=units, hours_on_standard=hours_on,
                             hours_off_standard=off, off_standard_reason=rng.choice(["waiting for parts", "meeting", "training",
                                                                                      "rework", "machine down"])))
    pd.DataFrame(rows).to_csv(os.path.join(D, "labor_report.csv"), index=False)

    # 4. Work sampling of the kitting area: 3 kitters, 20 days, random observations
    cats = ["picking", "walking", "searching", "waiting for system", "paperwork", "idle", "personal"]
    p = [0.46, 0.17, 0.09, 0.08, 0.08, 0.07, 0.05]
    rows = []
    for day in range(1, 21):
        n = int(rng.integers(25, 36))
        for _ in range(n):
            rows.append(dict(day=day, minute_of_shift=int(rng.integers(0, 480)), kitter=f"K{rng.integers(1, 4)}",
                             activity=rng.choice(cats, p=p)))
    pd.DataFrame(rows).sort_values(["day", "minute_of_shift"]).to_csv(os.path.join(D, "work_sampling_kitting.csv"), index=False)
    pd.DataFrame(dict(day=range(1, 21), kits_completed=rng.integers(560, 640, 20), kitters_present=3,
                      shift_minutes=480)).to_csv(os.path.join(D, "kitting_output.csv"), index=False)

    # 5. Standard data: pack-out time for crate sizes, from 18 past time studies
    rows = []
    for i in range(18):
        items = int(rng.integers(4, 40))
        heavy = int(rng.integers(0, 2))
        t = 0.60 + 0.085 * items + 0.70 * heavy + rng.normal(0, 0.12)
        rows.append(dict(study=f"TS-{100+i}", items_per_crate=items, heavy_items=heavy, normal_minutes=round(t, 2)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "packout_studies.csv"), index=False)
    return "data written"


def load(name):
    return pd.read_csv(os.path.join(D, name))


# ---------------------------------------------------------------- time study
def element_times():
    c = load("time_study_continuous.csv")
    c["note"] = c.note.fillna("")
    c["observed_s"] = c.cumulative_s.diff().fillna(c.cumulative_s.iloc[0]).round(1)
    return c


def ex_timestudy(pfd=0.15):
    c = element_times()
    el = load("elements.csv").set_index("element")
    good = c[c.note == ""]
    ratings = {e: (100 if el.loc[e, "type"] == "machine" else 110) for e in el.index}
    rows = []
    for e, g in good.groupby("element"):
        mean = g.observed_s.mean()
        r = ratings[e]
        normal = mean * r / 100
        rows.append(dict(element=e, type=el.loc[e, "type"], cycles_used=len(g), mean_observed_s=round(mean, 2),
                         sd_s=round(g.observed_s.std(), 2), rating_pct=r, normal_s=round(normal, 2)))
    t = pd.DataFrame(rows)
    nt = t.normal_s.sum()
    manual_nt = t[t.type == "manual"].normal_s.sum()
    std = nt * (1 + pfd)
    std_manual_only_allowance = manual_nt * (1 + pfd) + t[t.type == "machine"].normal_s.sum()
    return {"elements": t.to_dict("records"), "foreign element removed": "cycle 9, E3 (+22 s dropped bit)",
            "normal time per pump (s)": round(nt, 2), "standard time, PF&D 15% on all elements (s)": round(std, 2),
            "standard time, allowance on manual elements only (s)": round(std_manual_only_allowance, 2),
            "standard minutes per pump (allowance on manual only)": round(std_manual_only_allowance / 60, 3),
            "pumps per hour at standard": round(3600 / std_manual_only_allowance, 1),
            "pumps per 7.5 h shift at standard": int(7.5 * 3600 / std_manual_only_allowance)}


def ex_cycles(k=0.05, conf=0.95):
    c = element_times()
    good = c[c.note == ""]
    z = stats.norm.ppf(0.5 + conf / 2)
    out = {}
    for e, g in good.groupby("element"):
        x, s, n = g.observed_s.mean(), g.observed_s.std(ddof=1), len(g)
        need = math.ceil((z * s / (k * x)) ** 2)
        t = stats.t.ppf(0.5 + conf / 2, n - 1)
        need_t = math.ceil((t * s / (k * x)) ** 2)
        out[e] = {"mean": round(x, 2), "sd": round(s, 2), "cycles needed (z)": need, "cycles needed (t, n-1 df)": need_t,
                  "taken": n}
    return {"accuracy +/-5%, 95% confidence": out}


def ex_rating():
    r = load("rating_practice.csv")
    r["error"] = r.rating_pct - r.benchmark_pct
    g = r.groupby("analyst").agg(mean_error=("error", "mean"), sd_error=("error", "std"),
                                 within_5=("error", lambda e: (e.abs() <= 5).mean()))
    g["within_5"] = (100 * g.within_5).round(0)
    out = {"by analyst": g.round(1).reset_index().to_dict("records")}
    # leveling example (illustrative factor values)
    lev = {"skill (good)": 0.06, "effort (good)": 0.05, "conditions (average)": 0.0, "consistency (good)": 0.01}
    out["leveling example factors"] = lev
    out["leveling factor"] = round(1 + sum(lev.values()), 2)
    return out


def ex_allowances():
    personal, basic_fatigue, variable, delay = 0.05, 0.04, 0.03, 0.03
    total = personal + basic_fatigue + variable + delay
    nt = 60.0
    return {"allowance components (% of normal time)": {"personal": 5, "basic fatigue": 4, "variable fatigue (standing, light lifts)": 3,
                                                        "unavoidable delay (from work sampling)": 3},
            "total allowance %": round(100 * total, 1),
            "standard for 60 s normal time, allowance as % of normal time": round(nt * (1 + total), 2),
            "standard if allowance is % of the workday (NT / (1 - A))": round(nt / (1 - total), 2),
            "same 15% expressed as % of workday -> % of normal time": round(100 * (total / (1 - total)), 2)}


def ex_labor():
    l = load("labor_report.csv")
    std_min = {"Pump assembly": 1.95, "Kitting": 0.80, "Packing": 0.45}
    l["earned_hours"] = l.units * l.job.map(std_min) / 60
    l["paid_hours"] = l.hours_on_standard + l.hours_off_standard
    g = l.groupby("operator").agg(earned=("earned_hours", "sum"), on=("hours_on_standard", "sum"), paid=("paid_hours", "sum"))
    g["efficiency_% (earned/on-std)"] = (100 * g.earned / g.on).round(1)
    g["utilization_% (on-std/paid)"] = (100 * g.on / g.paid).round(1)
    g["productivity_% (earned/paid)"] = (100 * g.earned / g.paid).round(1)
    tot = l[["earned_hours", "hours_on_standard", "paid_hours"]].sum()
    off = l.groupby("off_standard_reason").hours_off_standard.sum().sort_values(ascending=False)
    return {"by operator (4 weeks)": g.round(1).reset_index().to_dict("records"),
            "department efficiency / utilization / productivity %": (round(100 * tot.earned_hours / tot.hours_on_standard, 1),
                                                                     round(100 * tot.hours_on_standard / tot.paid_hours, 1),
                                                                     round(100 * tot.earned_hours / tot.paid_hours, 1)),
            "off-standard hours by reason": off.round(1).to_dict()}


def ex_sampling():
    w = load("work_sampling_kitting.csv")
    n = len(w)
    share = w.activity.value_counts(normalize=True)
    z = 1.96
    out = {}
    for a, p in share.items():
        h = z * math.sqrt(p * (1 - p) / n)
        out[a] = {"share %": round(100 * p, 1), "95% CI %": (round(100 * (p - h), 1), round(100 * (p + h), 1))}
    pick = share["picking"]
    need = math.ceil(z ** 2 * pick * (1 - pick) / 0.03 ** 2)
    daily = w.assign(pick=w.activity.eq("picking")).groupby("day").agg(n=("pick", "size"), p=("pick", "mean"))
    pbar = w.activity.eq("picking").mean()
    daily["UCL"] = pbar + 3 * np.sqrt(pbar * (1 - pbar) / daily.n)
    daily["LCL"] = pbar - 3 * np.sqrt(pbar * (1 - pbar) / daily.n)
    out_days = daily[(daily.p > daily.UCL) | (daily.p < daily.LCL)].index.tolist()
    return {"observations": n, "by activity": out,
            "observations needed for picking share within +/-3 points": need,
            "control chart of daily picking share: days outside limits": out_days}


def ex_sampling_std(rating=1.0, allowance=0.12):
    w = load("work_sampling_kitting.csv")
    o = load("kitting_output.csv")
    productive = w.activity.isin(["picking", "walking", "searching", "paperwork"]).mean()   # work content incl. method waste
    picking = w.activity.eq("picking").mean()
    total_min = (o.kitters_present * o.shift_minutes).sum()
    kits = o.kits_completed.sum()
    def std(p):
        return total_min * p * rating / kits * (1 + allowance)
    return {"total kitter-minutes (20 days)": int(total_min), "kits completed": int(kits),
            "share of time on kit work (picking + walking + searching + paperwork) %": round(100 * productive, 1),
            "standard min per kit, current method": round(std(productive), 3),
            "share of time actually picking %": round(100 * picking, 1),
            "standard min per kit if walking and searching were removed (picking + paperwork)": round(
                std(w.activity.isin(["picking", "paperwork"]).mean()), 3),
            "assumptions": "rating 100%, allowance 12%; method waste stays in the standard until the method is fixed"}


def ex_standard_data():
    import statsmodels.formula.api as smf
    s = load("packout_studies.csv")
    m = smf.ols("normal_minutes ~ items_per_crate + heavy_items", data=s).fit()
    new = pd.DataFrame(dict(items_per_crate=[24], heavy_items=[1]))
    pr = m.get_prediction(new).summary_frame(alpha=0.05)
    return {"studies": len(s), "formula (normal minutes)": {k: round(v, 3) for k, v in m.params.items()},
            "R2": round(m.rsquared, 3), "residual SD (min)": round(m.mse_resid ** 0.5, 3),
            "new crate: 24 items incl. heavy ones -> normal min": round(pr["mean"].iloc[0], 2),
            "95% prediction interval": (round(pr["obs_ci_lower"].iloc[0], 2), round(pr["obs_ci_upper"].iloc[0], 2)),
            "standard min with 15% allowance": round(pr["mean"].iloc[0] * 1.15, 2),
            "valid range": f"{s.items_per_crate.min()}-{s.items_per_crate.max()} items"}


def ex_learning(first=4.20, rate=0.85):
    b = math.log(rate) / math.log(2)
    out = {"learning exponent b": round(b, 4)}
    for n in (1, 2, 4, 8, 16, 32, 64, 100, 200):
        out[f"unit {n} (min)"] = round(first * n ** b, 3)
    cum100 = sum(first * k ** b for k in range(1, 101))
    out["cumulative minutes for first 100 units (pure curve)"] = round(cum100, 1)
    std = ex_timestudy()["standard minutes per pump (allowance on manual only)"]
    n_reach = math.ceil((std / first) ** (1 / b))
    out[f"unit at which time reaches the {std} min standard"] = n_reach
    out["after that unit"] = "plan at the standard; the curve is not extrapolated below it"
    cum_plan = sum(max(first * k ** b, std) for k in range(1, 101))
    out["planning minutes for first 100 units (curve until standard, then standard)"] = round(cum_plan, 1)
    return out


def ex_staffing():
    std_min = ex_timestudy()["standard minutes per pump (allowance on manual only)"]
    demand_week = 4200
    avail_min = 5 * 2 * 450            # 5 days x 2 shifts x 450 productive minutes
    eff = 0.95
    operators = demand_week * std_min / (avail_min / 2 * eff)   # per operator: 5 days x 450 min
    takt = (5 * 2 * 450 * 60) / demand_week
    return {"weekly demand": demand_week, "standard min per pump": std_min,
            "operator-minutes needed per week": round(demand_week * std_min, 0),
            "minutes available per operator per week (5 x 450)": 2250, "planned efficiency": eff,
            "operators needed (both shifts)": round(operators, 2), "round up to": math.ceil(operators),
            "takt time (s) over 2 shifts": round(takt, 1),
            "note": "cycle includes a 45 s machine leak test; if one tester, check it against takt"}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"timestudy": ex_timestudy, "cycles": ex_cycles, "rating": ex_rating, "allowances": ex_allowances, "labor": ex_labor,
      "sampling": ex_sampling, "sampling_std": ex_sampling_std, "standard_data": ex_standard_data, "learning": ex_learning,
      "staffing": ex_staffing}

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
