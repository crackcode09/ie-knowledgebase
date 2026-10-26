"""rca.py - analysis toolkit for the Root Cause Analysis course.

    python tools/rca.py all          # every worked example
    python tools/rca.py <name>       # pareto, stratify, scatter, simple, multiple, logistic, decision

License: MIT
"""
from __future__ import annotations

import csv
import os
import sys
from collections import Counter, defaultdict

import numpy as np
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")


def load(name):
    with open(os.path.join(ROOT, "data", name), newline="") as f:
        return list(csv.DictReader(f))


def col(rows, k):
    return np.array([float(r[k]) for r in rows])


def pareto(keys, weights=None):
    tot = defaultdict(float)
    for i, k in enumerate(keys):
        tot[k] += 1 if weights is None else weights[i]
    items = sorted(tot.items(), key=lambda kv: -kv[1])
    g, cum, out = sum(v for _, v in items), 0, []
    for k, v in items:
        cum += v
        out.append((k, v, round(100 * v / g, 1), round(100 * cum / g, 1)))
    return out


def ex_pareto():
    s = load("scrap_log.csv")
    return {"by count": pareto([r["defect"] for r in s]),
            "by cost": pareto([r["defect"] for r in s], [float(r["cost_usd"]) for r in s])}


def ex_stratify():
    s = [r for r in load("scrap_log.csv") if r["defect"] == "Leak at test"]
    by_m = Counter(r["machine"] for r in s)
    by_sh = Counter(r["shift"] for r in s)
    other = [r for r in load("scrap_log.csv") if r["defect"] != "Leak at test"]
    tab = [[by_m[m], Counter(r["machine"] for r in other)[m]] for m in ("MC1", "MC2", "MC3")]
    chi = stats.chi2_contingency(tab)
    return {"leaks by machine": dict(sorted(by_m.items())), "leaks by shift": dict(by_sh),
            "machine x (leak vs other) table": tab, "chi2": round(chi.statistic, 2), "p": chi.pvalue}


def ex_scatter():
    t = load("tool_wear.csv")
    x, y = col(t, "hours_since_tool_change"), col(t, "seat_ra_um")
    r, p = stats.pearsonr(x, y)
    rho, ps = stats.spearmanr(x, y)
    return {"n": len(x), "pearson r": r, "r^2": r * r, "p": p, "spearman rho": rho}


def ex_simple():
    t = load("tool_wear.csv")
    x, y = col(t, "hours_since_tool_change"), col(t, "seat_ra_um")
    res = stats.linregress(x, y)
    tc = stats.t.ppf(0.975, len(x) - 2)
    hours_to_limit = (0.80 - res.intercept) / res.slope
    resid = y - (res.intercept + res.slope * x)
    s = np.sqrt((resid ** 2).sum() / (len(x) - 2))
    return {"intercept": res.intercept, "slope": res.slope, "slope 95% CI": (res.slope - tc * res.stderr, res.slope + tc * res.stderr),
            "r^2": res.rvalue ** 2, "p (slope)": res.pvalue, "s (residual SD)": s,
            "hours until predicted mean Ra = 0.80": hours_to_limit}


def _ols(y, X, names):
    import statsmodels.api as sm
    m = sm.OLS(y, sm.add_constant(X)).fit()
    return m, dict(zip(["const"] + names, m.params)), dict(zip(["const"] + names, m.pvalues))


def ex_multiple():
    import statsmodels.api as sm
    from statsmodels.stats.outliers_influence import variance_inflation_factor as vif
    d = load("leak_rate.csv")
    names = ["seat_ra_um", "torque_nm", "ambient_c", "humidity_pct", "gasket_mm"]
    X = np.column_stack([col(d, k) for k in names])
    y = col(d, "leak_ccm")
    m, b, p = _ols(y, X, names)
    Xc = sm.add_constant(X)
    vifs = {n: vif(Xc, i + 1) for i, n in enumerate(names)}
    keep = ["seat_ra_um", "torque_nm"]
    m2, b2, p2 = _ols(y, np.column_stack([col(d, k) for k in keep]), keep)
    r_th = stats.pearsonr(col(d, "ambient_c"), col(d, "humidity_pct"))[0]
    r_hl = stats.pearsonr(col(d, "humidity_pct"), y)
    return {"full model coef": {k: round(v, 4) for k, v in b.items()},
            "full model p": {k: round(v, 4) for k, v in p.items()},
            "full R^2 / adj R^2": (round(m.rsquared, 3), round(m.rsquared_adj, 3)),
            "VIF": {k: round(v, 2) for k, v in vifs.items()},
            "r(ambient, humidity)": round(r_th, 3),
            "humidity alone vs leak: r, p": (round(r_hl[0], 3), round(r_hl[1], 4)),
            "reduced model coef": {k: round(v, 4) for k, v in b2.items()},
            "reduced model p": {k: round(v, 6) for k, v in p2.items()},
            "reduced R^2 / adj R^2": (round(m2.rsquared, 3), round(m2.rsquared_adj, 3)),
            "reduced residual SD": round(np.sqrt(m2.scale), 3)}


def ex_logistic():
    import statsmodels.api as sm
    d = load("leak_test.csv")
    X = np.column_stack([col(d, "seat_ra_um"), col(d, "torque_nm")])
    y = col(d, "fail")
    m = sm.Logit(y, sm.add_constant(X)).fit(disp=0)
    b0, b1, b2 = m.params
    def prob(ra, tq):
        return 1 / (1 + np.exp(-(b0 + b1 * ra + b2 * tq)))
    pred = (m.predict(sm.add_constant(X)) >= 0.5).astype(int)
    return {"n / failures": (len(y), int(y.sum())),
            "coef (const, Ra, torque)": tuple(round(v, 3) for v in m.params),
            "p-values": tuple(round(v, 5) for v in m.pvalues),
            "odds ratio per +0.1 um Ra": round(float(np.exp(b1 * 0.1)), 3),
            "odds ratio per +1 N*m torque": round(float(np.exp(b2)), 3),
            "P(fail) Ra 0.4, 22 N*m": round(float(prob(0.4, 22)), 4),
            "P(fail) Ra 0.8, 22 N*m": round(float(prob(0.8, 22)), 4),
            "P(fail) Ra 1.2, 22 N*m": round(float(prob(1.2, 22)), 4),
            "Ra for P(fail)=5% at 22 N*m": round(float((np.log(0.05 / 0.95) - b0 - b2 * 22) / b1), 3),
            "classification accuracy (0.5 cut)": round(float((pred == y).mean()), 3),
            "McFadden pseudo R^2": round(m.prsquared, 3)}


DEC_CRIT = {"Effectiveness": 5, "Cost": 3, "Time to implement": 2, "Risk of side effects": 3, "Sustainability": 4}
DEC_OPTS = {"Change tool every 16 h": [4, 3, 5, 4, 3],
            "In-process Ra gauge + auto tool change": [5, 2, 3, 4, 5],
            "Increase clamp torque to 25 N*m": [2, 5, 5, 2, 3],
            "100% leak retest": [1, 3, 4, 5, 1]}


def ex_decision():
    w = np.array(list(DEC_CRIT.values()))
    return {k: int(np.dot(w, v)) for k, v in sorted(DEC_OPTS.items(), key=lambda kv: -np.dot(w, kv[1]))}


EX = {"pareto": ex_pareto, "stratify": ex_stratify, "scatter": ex_scatter, "simple": ex_simple,
      "multiple": ex_multiple, "logistic": ex_logistic, "decision": ex_decision}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list):
                    print(f"  {a}:")
                    for row in b:
                        print("    ", row)
                else:
                    print(f"  {a}: {b}")
