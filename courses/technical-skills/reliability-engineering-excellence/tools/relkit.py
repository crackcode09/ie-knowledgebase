"""relkit.py - data and analysis toolkit for the Reliability Engineering Excellence course.

Running case: Lakeshore Components (fictional), a machining and assembly plant. Line A has a
hydraulic press, a grinder with a high-speed spindle, a coolant system and a transfer conveyor.

    python tools/relkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/relkit.py all           # every worked example
    python tools/relkit.py <name>        # pareto, metrics, exponential, normal, weibull, rbd,
                                         # criticality, pm, pf, lcc, optimum, growth

Requires numpy, scipy, pandas. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import optimize, stats, integrate

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")


# ---------------------------------------------------------------- data
def make_data(seed=4242):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)

    # 1. 12 months of corrective work orders on Line A
    modes = {
        "Grinder spindle": [("bearing failure", 5, 22, 9000), ("drawbar / tool clamp", 4, 3, 900), ("encoder fault", 3, 2, 1200)],
        "Hydraulic press": [("seal leak", 9, 4, 1100), ("valve stuck", 6, 3, 1500), ("pump wear", 2, 16, 7000)],
        "Coolant system": [("pump failure", 7, 3, 1300), ("filter clogged", 14, 1, 150), ("level sensor", 5, 1, 200)],
        "Transfer conveyor": [("belt tracking", 11, 1.5, 120), ("gearmotor", 2, 8, 3200), ("photo-eye", 8, 0.5, 90)],
        "Robot loader": [("gripper", 6, 1, 300), ("collision / crash", 2, 6, 4500), ("teach drift", 4, 1, 100)],
    }
    rows, wo = [], 1000
    for asset, ms in modes.items():
        for mode, n, mean_h, mean_cost in ms:
            for _ in range(n):
                dt = round(float(rng.gamma(4, mean_h / 4)), 1)
                cost = round(float(mean_cost * rng.lognormal(0, 0.3)), -1)
                wo += 1
                rows.append(dict(work_order=wo, month=int(rng.integers(1, 13)), asset=asset, failure_mode=mode,
                                 downtime_h=dt, repair_cost=cost))
    pd.DataFrame(rows).sort_values(["month", "work_order"]).to_csv(os.path.join(D, "work_orders.csv"), index=False)

    # 2. Spindle bearing life (operating hours): Weibull beta 2.3, eta 9,000 h; some removed early (suspensions)
    life = stats.weibull_min.rvs(2.3, scale=9000, size=24, random_state=rng)
    removal = rng.uniform(3000, 12000, size=24)        # planned rebuilds / still running at data cut-off
    t = np.minimum(life, removal)
    status = np.where(life <= removal, "F", "S")
    pd.DataFrame(dict(unit=[f"SB{i+1:02d}" for i in range(24)], hours=np.round(t, 0).astype(int), status=status)) \
        .to_csv(os.path.join(D, "spindle_bearing_life.csv"), index=False)

    # 3. Coolant pump times between failures (h): exponential, MTBF 2,200 h; repair times lognormal
    tbf = rng.exponential(2200, size=14)
    ttr = rng.lognormal(np.log(2.6), 0.45, size=14)
    pd.DataFrame(dict(failure=range(1, 15), hours_since_last=np.round(tbf, 0).astype(int),
                      repair_h=np.round(ttr, 1))).to_csv(os.path.join(D, "coolant_pump_failures.csv"), index=False)

    # 4. Grinding-wheel life (parts): normal wear-out
    pd.DataFrame(dict(wheel=range(1, 31), parts=np.round(rng.normal(5200, 420, 30), 0).astype(int))) \
        .to_csv(os.path.join(D, "grinding_wheel_life.csv"), index=False)

    # 5. Asset register for criticality ranking (scores 1-5)
    reg = [
        ("Grinder spindle", 5, 4, 4, 3, 2), ("Hydraulic press", 5, 4, 3, 4, 4), ("Coolant system", 3, 3, 2, 4, 1),
        ("Transfer conveyor", 4, 2, 1, 4, 1), ("Robot loader", 4, 3, 2, 2, 3), ("Air compressor", 5, 2, 1, 2, 1),
        ("Parts washer", 2, 2, 2, 3, 2), ("Chip conveyor", 3, 2, 1, 3, 1),
    ]
    pd.DataFrame(reg, columns=["asset", "production_impact", "quality_impact", "repair_cost", "failure_frequency",
                               "safety_environment"]).to_csv(os.path.join(D, "asset_register.csv"), index=False)

    # 6. Reliability-growth test of a redesigned gearmotor: cumulative failure times (h)
    beta_g, lam = 0.55, 0.35
    cum, t_, times = 0, 0.0, []
    while True:
        cum += 1
        t_ = (cum / lam) ** (1 / beta_g) * rng.uniform(0.85, 1.15)
        if t_ > 2000:
            break
        times.append(round(t_, 0))
    times = sorted(set(times))
    pd.DataFrame(dict(failure=range(1, len(times) + 1), cumulative_hours=times)).to_csv(
        os.path.join(D, "gearmotor_growth_test.csv"), index=False)
    return "data written"


def load(name):
    return pd.read_csv(os.path.join(D, name))


# ---------------------------------------------------------------- core functions
def weibull_mle(t, failed):
    """MLE of Weibull (beta, eta) with right-censoring. failed: boolean array."""
    t = np.asarray(t, float)
    f = np.asarray(failed, bool)

    def nll(p):
        b, e = np.exp(p)
        z = t / e
        return -(np.sum(np.log(b / e) + (b - 1) * np.log(z[f])) - np.sum(z ** b))

    res = optimize.minimize(nll, x0=[np.log(1.5), np.log(np.mean(t))], method="Nelder-Mead",
                            options=dict(xatol=1e-8, fatol=1e-10, maxiter=5000))
    return tuple(np.exp(res.x))


def median_ranks(t, failed):
    """Johnson's adjusted ranks + Benard's approximation for plotting with suspensions."""
    order = np.argsort(t)
    t, failed = np.asarray(t)[order], np.asarray(failed)[order]
    n, prev, out = len(t), 0.0, []
    for i, (ti, fi) in enumerate(zip(t, failed)):
        if fi:
            reverse_rank = n - i
            prev = prev + (n + 1 - prev) / (1 + reverse_rank)
            out.append((ti, (prev - 0.3) / (n + 0.4)))
    return np.array(out)


def weib_R(t, b, e):
    return np.exp(-(np.asarray(t) / e) ** b)


def age_replacement_cost_rate(T, b, e, cp, cf):
    """Long-run cost per operating hour when replacing at age T or at failure."""
    R = weib_R(T, b, e)
    denom, _ = integrate.quad(lambda x: weib_R(x, b, e), 0, T)
    return (cp * R + cf * (1 - R)) / denom


def npv(rate, cfs):
    return sum(c / (1 + rate) ** k for k, c in enumerate(cfs))


# ---------------------------------------------------------------- examples
def ex_pareto():
    w = load("work_orders.csv")
    by_asset = w.groupby("asset").agg(failures=("work_order", "count"), downtime_h=("downtime_h", "sum"),
                                      cost=("repair_cost", "sum")).sort_values("downtime_h", ascending=False)
    share = 100 * by_asset.downtime_h / by_asset.downtime_h.sum()
    by_asset["downtime %"] = share.round(1)
    by_asset["cum %"] = share.cumsum().round(1)
    by_mode = w.groupby(["asset", "failure_mode"]).downtime_h.sum().sort_values(ascending=False)
    top = by_mode.head(5)
    return {"work orders": len(w), "total downtime h": round(w.downtime_h.sum(), 1), "total repair cost": int(w.repair_cost.sum()),
            "by asset (sorted by downtime)": by_asset.round(1).reset_index().to_dict("records"),
            "top 5 failure modes by downtime": {f"{a} / {m}": round(v, 1) for (a, m), v in top.items()},
            "top-5 share of downtime %": round(100 * top.sum() / w.downtime_h.sum(), 1),
            "most frequent modes (count)": {f"{a} / {m}": int(v) for (a, m), v in
                                            w.groupby(["asset", "failure_mode"]).size().sort_values(ascending=False).head(3).items()}}


def ex_metrics():
    p = load("coolant_pump_failures.csv")
    mtbf = p.hours_since_last.mean()
    mttr = p.repair_h.mean()
    ai = mtbf / (mtbf + mttr)
    mldt = 6.0  # mean logistics delay (parts, call-out) per failure, h - illustrative
    ao = mtbf / (mtbf + mttr + mldt)
    return {"failures": len(p), "MTBF (h)": round(mtbf), "MTTR (h)": round(mttr, 2), "inherent availability %": round(100 * ai, 3),
            "operational availability incl. 6 h logistics delay %": round(100 * ao, 3),
            "downtime per 6,000 operating h (h)": round(6000 / mtbf * (mttr + mldt), 1)}


def ex_exponential():
    p = load("coolant_pump_failures.csv")
    T, r = p.hours_since_last.sum(), len(p)
    mtbf = T / r
    lo = 2 * T / stats.chi2.ppf(0.95, 2 * r)          # 90% two-sided interval (failure-terminated)
    hi = 2 * T / stats.chi2.ppf(0.05, 2 * r)
    lam = 1 / mtbf
    month = 500                                         # operating hours per month
    return {"total operating time (h)": int(T), "failures": r, "MTBF (h)": round(mtbf),
            "90% CI for MTBF (h)": (round(lo), round(hi)), "failure rate per 1,000 h": round(1000 * lam, 3),
            "R(500 h) = exp(-500/MTBF)": round(math.exp(-month * lam), 3),
            "P(0, 1, 2+ failures in a 500-h month)": tuple(round(x, 3) for x in (
                stats.poisson.pmf(0, month * lam), stats.poisson.pmf(1, month * lam), stats.poisson.sf(1, month * lam))),
            "note": "exponential => constant hazard: a preventive replacement does not lower the risk"}


def ex_normal():
    w = load("grinding_wheel_life.csv")
    mu, sd = w.parts.mean(), w.parts.std(ddof=1)
    out = {"mean life (parts)": round(mu), "SD (parts)": round(sd)}
    for change_at in (4800, 4500, 4200):
        out[f"P(fail before planned change at {change_at})"] = round(stats.norm.cdf((change_at - mu) / sd), 4)
    out["change point for 1% risk"] = round(stats.norm.ppf(0.01, mu, sd))
    out["Shapiro-Wilk p (normality)"] = round(stats.shapiro(w.parts).pvalue, 3)
    return out


def ex_weibull():
    d = load("spindle_bearing_life.csv")
    f = (d.status == "F").values
    b, e = weibull_mle(d.hours.values, f)
    b10 = e * (-math.log(0.9)) ** (1 / b)
    mttf = e * math.gamma(1 + 1 / b)
    mr = median_ranks(d.hours.values, f)
    x, y = np.log(mr[:, 0]), np.log(-np.log(1 - mr[:, 1]))
    slope, intercept = np.polyfit(x, y, 1)
    return {"units": len(d), "failures / suspensions": (int(f.sum()), int((~f).sum())),
            "MLE beta (shape)": round(b, 2), "MLE eta (scale, h)": round(e), "B10 life (h)": round(b10),
            "mean life (h)": round(mttf), "R(4,000 h)": round(float(weib_R(4000, b, e)), 3),
            "hazard rising? (beta > 1)": bool(b > 1),
            "rank-regression beta, eta (check)": (round(slope, 2), round(math.exp(-intercept / slope)))}


def ex_rbd():
    r = dict(press=0.95, grinder=0.92, pump=0.90, conveyor=0.97, robot=0.94)   # 1-month reliabilities (illustrative)
    series = np.prod(list(r.values()))
    pump_pair = 1 - (1 - r["pump"]) ** 2
    with_redundant_pump = series / r["pump"] * pump_pair
    k_of_n = sum(math.comb(3, k) * 0.90 ** k * 0.10 ** (3 - k) for k in (2, 3))   # 2-out-of-3 sensors
    return {"subsystem R (1 month)": r, "line in series": round(series, 4),
            "with a redundant (1-of-2) coolant pump": round(with_redundant_pump, 4),
            "two pumps in parallel": round(pump_pair, 4),
            "2-out-of-3 level sensors at R=0.90 each": round(k_of_n, 4),
            "weakest link": min(r, key=r.get)}


def ex_criticality():
    a = load("asset_register.csv")
    a["consequence"] = a[["production_impact", "quality_impact", "repair_cost", "safety_environment"]].max(axis=1)
    a["risk (consequence x frequency)"] = a.consequence * a.failure_frequency
    a["weighted score"] = (0.35 * a.production_impact + 0.20 * a.quality_impact + 0.10 * a.repair_cost +
                           0.35 * a.safety_environment) * a.failure_frequency
    a = a.sort_values("weighted score", ascending=False)
    a["class"] = pd.cut(a["weighted score"], [0, 6, 10, 100], labels=["C", "B", "A"])   # A > 10, B > 6, C <= 6
    return {"ranking": a[["asset", "consequence", "failure_frequency", "risk (consequence x frequency)",
                          "weighted score", "class"]].round(2).astype({"class": str}).to_dict("records")}


def ex_pm():
    d = load("spindle_bearing_life.csv")
    b, e = weibull_mle(d.hours.values, (d.status == "F").values)
    cp, cf = 4_000.0, 22_000.0          # planned rebuild vs in-service failure (incl. downtime, scrap)
    rtf = cf / (e * math.gamma(1 + 1 / b))
    res = optimize.minimize_scalar(lambda T: age_replacement_cost_rate(T, b, e, cp, cf), bounds=(500, 20000),
                                   method="bounded")
    T = res.x
    table = {int(Tx): round(age_replacement_cost_rate(Tx, b, e, cp, cf), 3) for Tx in (2000, 3000, 4000, 5000, 6000, 8000)}
    return {"Weibull (beta, eta)": (round(b, 2), round(e)), "planned / failure cost": (cp, cf),
            "run-to-failure cost per h": round(rtf, 3), "optimum replacement age (h)": round(T, -1),
            "cost per h at optimum": round(res.fun, 3), "saving vs run-to-failure %": round(100 * (1 - res.fun / rtf), 1),
            "R at optimum age": round(float(weib_R(T, b, e)), 3), "cost per h by age": table,
            "annual saving at 6,000 h/yr": round((rtf - res.fun) * 6000, -2)}


def ex_pf():
    pf = 1200.0          # P-F interval for spindle bearing (h): vibration detectable to functional failure (illustrative)
    out = {"P-F interval (h)": pf}
    for k in (1, 2, 3):
        interval = pf / k
        out[f"inspect every {interval:.0f} h -> inspections inside the P-F window"] = k
    out["common rule: inspect at P-F / 2"] = pf / 2
    out["net warning time at P-F/2 (worst case, h)"] = pf - pf / 2
    out["online monitoring: inspections per 6,000 h at P-F/2"] = int(6000 / (pf / 2))
    return out


def ex_lcc():
    """Two coolant-pump options over 10 years at 9 %; 6,000 operating h/yr."""
    rate, years, hours = 0.09, 10, 6000
    opts = {"A standard": dict(price=18_000, install=2_000, mtbf=2_200, cost_per_failure=6_500, energy=5_400, pm=900),
            "B premium sealed": dict(price=31_000, install=2_500, mtbf=6_000, cost_per_failure=6_500, energy=4_600, pm=600)}
    out, flows = {}, {}
    for k, o in opts.items():
        annual = hours / o["mtbf"] * o["cost_per_failure"] + o["energy"] + o["pm"]
        cfs = [-(o["price"] + o["install"])] + [-annual] * years
        flows[k] = cfs
        out[k] = {"initial": o["price"] + o["install"], "annual failures": round(hours / o["mtbf"], 2),
                  "annual operating cost": round(annual), "LCC (PV of costs)": round(-npv(rate, cfs))}
    inc = [b - a for a, b in zip(flows["A standard"], flows["B premium sealed"])]
    annual_saving = inc[1]
    pv_benefit = npv(rate, [0] + inc[1:])
    out["incremental (B - A)"] = {"extra investment": -inc[0], "annual saving": round(annual_saving),
                                  "simple payback (yr)": round(-inc[0] / annual_saving, 2),
                                  "ROI % (annual saving / extra investment)": round(100 * annual_saving / -inc[0], 1),
                                  "benefit-cost ratio (PV savings / extra investment)": round(pv_benefit / -inc[0], 2),
                                  "net return (NPV)": round(npv(rate, inc))}
    return out


def ex_optimum():
    """Total cost = cost of reliability effort + expected failure cost, as a function of target reliability."""
    R = np.linspace(0.80, 0.995, 400)
    prevention = 4_000 / (1 - R) ** 0.6 - 4_000          # effort rises steeply near R = 1 (illustrative)
    failure = 900_000 * (1 - R)                          # expected annual failure cost
    total = prevention + failure
    i = int(np.argmin(total))
    return {"optimum target reliability": round(float(R[i]), 3), "total annual cost at optimum": round(float(total[i]), -2),
            "cost at R = 0.85": round(float(np.interp(0.85, R, total)), -2),
            "cost at R = 0.99": round(float(np.interp(0.99, R, total)), -2)}


def ex_growth():
    """Crow-AMSAA (power-law NHPP) for a reliability-growth test, time-terminated at T = 2,000 h."""
    g = load("gearmotor_growth_test.csv")
    t = g.cumulative_hours.values.astype(float)
    T, n = 2000.0, len(t)
    beta = n / np.sum(np.log(T / t))
    lam = n / T ** beta
    inst_mtbf = 1 / (lam * beta * T ** (beta - 1))
    return {"failures in test": n, "beta (growth if < 1)": round(beta, 3), "lambda": round(lam, 4),
            "cumulative MTBF at 2,000 h": round(T / n, 1), "instantaneous MTBF at 2,000 h": round(inst_mtbf, 1)}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"pareto": ex_pareto, "metrics": ex_metrics, "exponential": ex_exponential, "normal": ex_normal,
      "weibull": ex_weibull, "rbd": ex_rbd, "criticality": ex_criticality, "pm": ex_pm, "pf": ex_pf, "lcc": ex_lcc,
      "optimum": ex_optimum, "growth": ex_growth}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list):
                    print(f"  {a}:")
                    for row in b:
                        print(f"    {_clean(row)}")
                else:
                    print(f"  {a}: {_clean(b)}")
