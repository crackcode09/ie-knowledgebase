"""doekit.py - data generator and analysis toolkit for the Design of Experiments course.

Running case: injection molding of a glass-filled nylon bearing cage.

    python tools/doekit.py data       # (re)generate data/*.csv (fixed seed)
    python tools/doekit.py all        # every worked example
    python tools/doekit.py <name>     # crd, rbd, latin, twofactor, unbalanced, reps, full, fractional, optimize

Requires numpy, scipy, pandas, statsmodels. License: MIT
"""
from __future__ import annotations

import itertools
import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")


def _save(df, name):
    os.makedirs(D, exist_ok=True)
    df.to_csv(os.path.join(D, name), index=False)


def load(name):
    return pd.read_csv(os.path.join(D, name))


def make_data(seed=1935):
    rng = np.random.default_rng(seed)
    # 1. CRD: tensile strength (MPa) of cages from 4 resin suppliers, 6 cages each, run in random order
    means = {"S1": 182.0, "S2": 186.5, "S3": 179.0, "S4": 187.5}
    rows = [(s, round(m + rng.normal(0, 3.2), 1)) for s, m in means.items() for _ in range(6)]
    order = rng.permutation(len(rows))
    _save(pd.DataFrame([dict(run=i + 1, supplier=rows[j][0], strength=rows[j][1]) for i, j in enumerate(order)]),
          "crd_suppliers.csv")
    # 2. RBD: ejection force (N) with 4 mold-release agents, blocked by 5 molds
    agent = {"R1": 0.0, "R2": -6.0, "R3": -2.0, "R4": -9.0}
    mold = {"M1": 0, "M2": 12, "M3": -8, "M4": 20, "M5": 5}
    rows = [dict(mold=m, agent=a, force=round(140 + agent[a] + mold[m] + rng.normal(0, 3.0), 1))
            for m in mold for a in agent]
    _save(pd.DataFrame(rows), "rbd_release_agent.csv")
    # 3. Latin square: cycle time (s), 4 cooling programs (A-D), rows = machines, columns = days
    square = [["A", "B", "C", "D"], ["B", "C", "D", "A"], ["C", "D", "A", "B"], ["D", "A", "B", "C"]]
    prog = {"A": 0.0, "B": -1.4, "C": -2.6, "D": -0.6}
    mach = [0.0, 1.2, -0.8, 2.0]
    day = [0.0, 0.5, -0.4, 0.9]
    rows = [dict(machine=f"Mc{i+1}", day=f"Day{j+1}", program=square[i][j],
                 cycle=round(32 + prog[square[i][j]] + mach[i] + day[j] + rng.normal(0, 0.5), 2))
            for i in range(4) for j in range(4)]
    _save(pd.DataFrame(rows), "latin_cooling.csv")
    # 4. Two-factor with interaction: shrinkage (%) melt temp (3) x hold pressure (3), 3 replicates
    rows = []
    for ti, T in enumerate((260, 275, 290)):
        for pi, P in enumerate((60, 75, 90)):
            mu = 1.40 + 0.06 * ti - 0.10 * pi + (0.05 if (ti == 2 and pi == 0) else 0) - (0.04 if (ti == 0 and pi == 2) else 0)
            for r in range(3):
                rows.append(dict(melt_temp=T, hold_pressure=P, rep=r + 1, shrinkage=round(mu + rng.normal(0, 0.025), 3)))
    df = pd.DataFrame(rows)
    _save(df.sample(frac=1, random_state=3).reset_index(drop=True), "twofactor_shrinkage.csv")
    # 5. 2^4 full factorial, single replicate + 4 center points: warpage (um)
    #    A melt temp (270/290), B mold temp (70/90), C hold pressure (60/90), D cooling time (12/20 s)
    rows = []
    for d_, c_, b_, a_ in itertools.product([-1, 1], repeat=4):
        y = 120 + 6 * a_ - 14 * b_ - 11 * c_ - 9 * d_ + 7 * b_ * c_ + 1.5 * a_ * d_ + rng.normal(0, 2.5)
        rows.append(dict(A=a_, B=b_, C=c_, D=d_, warpage=round(y, 1)))
    rows.sort(key=lambda r: (r["D"], r["C"], r["B"], r["A"]))
    for _ in range(4):
        rows.append(dict(A=0, B=0, C=0, D=0, warpage=round(120 + 3.5 + rng.normal(0, 2.5), 1)))  # mild curvature
    _save(pd.DataFrame(rows), "full_factorial_warpage.csv")
    # 6. 2^(5-1) resolution V screening: E = ABCD; factors A-D as above plus E injection speed; response flash defects/1000
    rows = []
    for d_, c_, b_, a_ in itertools.product([-1, 1], repeat=4):
        e_ = a_ * b_ * c_ * d_
        y = 30 + 2 * a_ + 1 * b_ + 9 * c_ + 0.5 * d_ + 6 * e_ + 4 * c_ * e_ + rng.normal(0, 1.5)
        rows.append(dict(A=a_, B=b_, C=c_, D=d_, E=e_, flash=round(y, 1)))
    _save(pd.DataFrame(rows), "fractional_flash.csv")
    return "data written"


# ------------------------------------------------------------------ helpers
def anova_oneway_table(df, factor, y):
    g = df.groupby(factor)[y]
    grand = df[y].mean()
    sst = ((df[y] - grand) ** 2).sum()
    ssb = (g.count() * (g.mean() - grand) ** 2).sum()
    ssw = sst - ssb
    k, N = g.ngroups, len(df)
    msb, msw = ssb / (k - 1), ssw / (N - k)
    F = msb / msw
    return dict(SS_between=round(ssb, 2), SS_within=round(ssw, 2), SS_total=round(sst, 2), df=(k - 1, N - k),
                MS_between=round(msb, 2), MS_within=round(msw, 2), F=round(F, 2), p=round(stats.f.sf(F, k - 1, N - k), 5))


def ols_anova(formula, df, typ=2):
    import statsmodels.formula.api as smf
    import statsmodels.api as sm
    m = smf.ols(formula, data=df).fit()
    t = sm.stats.anova_lm(m, typ=typ)
    return m, t.round(4)


def effects_2k(df, y, factors):
    out = {}
    for r in range(1, len(factors) + 1):
        for combo in itertools.combinations(factors, r):
            col = np.prod(df[list(combo)].values, axis=1)
            out["".join(combo)] = df[y][col > 0].mean() - df[y][col < 0].mean()
    return out


def lenth_pse(effects):
    e = np.abs(np.array(list(effects.values())))
    s0 = 1.5 * np.median(e)
    pse = 1.5 * np.median(e[e < 2.5 * s0])
    m = len(e)
    me = stats.t.ppf(0.975, m / 3) * pse
    return pse, me


# ------------------------------------------------------------------ examples
def ex_crd():
    df = load("crd_suppliers.csv")
    t = anova_oneway_table(df, "supplier", "strength")
    means = df.groupby("supplier")["strength"].mean().round(2).to_dict()
    tk = stats.tukey_hsd(*[df[df.supplier == s]["strength"].values for s in sorted(means)])
    pairs = []
    names = sorted(means)
    for i, j in itertools.combinations(range(4), 2):
        pairs.append((f"{names[j]}-{names[i]}", round(means[names[j]] - means[names[i]], 2), round(float(tk.pvalue[i, j]), 4)))
    lev = stats.levene(*[df[df.supplier == s]["strength"].values for s in names]).pvalue
    return {"means": means, "ANOVA": t, "Tukey (pair, diff, p)": pairs, "Levene p": round(lev, 3)}


def ex_rbd():
    df = load("rbd_release_agent.csv")
    m, t = ols_anova("force ~ C(agent) + C(mold)", df)
    m2, t2 = ols_anova("force ~ C(agent)", df)
    return {"agent means": df.groupby("agent")["force"].mean().round(2).to_dict(),
            "RBD ANOVA": t.to_dict("index"), "same data, ignoring blocks": t2.to_dict("index")}


def ex_latin():
    df = load("latin_cooling.csv")
    m, t = ols_anova("cycle ~ C(program) + C(machine) + C(day)", df)
    return {"program means": df.groupby("program")["cycle"].mean().round(2).to_dict(),
            "Latin square ANOVA": t.to_dict("index")}


def ex_twofactor():
    df = load("twofactor_shrinkage.csv")
    m, t = ols_anova("shrinkage ~ C(melt_temp) * C(hold_pressure)", df)
    cell = df.groupby(["melt_temp", "hold_pressure"])["shrinkage"].mean().unstack().round(3)
    # hand calculation of sums of squares
    a, b, n = 3, 3, 3
    grand = df.shrinkage.mean()
    ssa = b * n * ((df.groupby("melt_temp").shrinkage.mean() - grand) ** 2).sum()
    ssb = a * n * ((df.groupby("hold_pressure").shrinkage.mean() - grand) ** 2).sum()
    sscell = n * ((df.groupby(["melt_temp", "hold_pressure"]).shrinkage.mean() - grand) ** 2).sum()
    ssab = sscell - ssa - ssb
    sst = ((df.shrinkage - grand) ** 2).sum()
    sse = sst - sscell
    return {"cell means": cell.to_dict("index"), "row means": df.groupby("melt_temp").shrinkage.mean().round(4).to_dict(),
            "column means": df.groupby("hold_pressure").shrinkage.mean().round(4).to_dict(),
            "grand mean": round(grand, 4),
            "hand SS (A, B, AB, E, T)": tuple(round(v, 5) for v in (ssa, ssb, ssab, sse, sst)),
            "ANOVA": t.to_dict("index")}


def ex_unbalanced():
    df = load("twofactor_shrinkage.csv")
    drop = df[(df.melt_temp == 290) & (df.hold_pressure == 60)].index[:2].tolist() + \
           df[(df.melt_temp == 260) & (df.hold_pressure == 90)].index[:1].tolist()
    u = df.drop(drop)
    m1, t1 = ols_anova("shrinkage ~ C(melt_temp) + C(hold_pressure) + C(melt_temp):C(hold_pressure)", u, typ=1)
    m1b, t1b = ols_anova("shrinkage ~ C(hold_pressure) + C(melt_temp) + C(melt_temp):C(hold_pressure)", u, typ=1)
    m3, t3 = ols_anova("shrinkage ~ C(melt_temp, Sum) * C(hold_pressure, Sum)", u, typ=3)
    return {"runs": f"{len(u)} of {len(df)}", "Type I SS, temp first": t1["sum_sq"].round(5).to_dict(),
            "Type I SS, pressure first": t1b["sum_sq"].round(5).to_dict(),
            "Type III": t3[["sum_sq", "F", "PR(>F)"]].to_dict("index")}


def ex_reps():
    # power to detect a 0.05 % shrinkage difference between two cell means, sigma 0.025
    out = {}
    for n in (2, 3, 4, 6):
        df_e = 9 * (n - 1)
        se = 0.025 * math.sqrt(2 / n)
        tc = stats.t.ppf(0.975, df_e)
        nc = 0.05 / se
        pw = stats.nct.sf(tc, df_e, nc) + stats.nct.cdf(-tc, df_e, nc)
        out[f"n={n}"] = {"error df": df_e, "power": round(pw, 3)}
    return {"3x3 design, power to detect 0.05% between two cells (sigma 0.025)": out}


def ex_full():
    df = load("full_factorial_warpage.csv")
    fact = df[df.A != 0]
    eff = effects_2k(fact, "warpage", ["A", "B", "C", "D"])
    pse, me = lenth_pse(eff)
    sig = {k: round(v, 2) for k, v in eff.items() if abs(v) > me}
    centers = df[df.A == 0].warpage
    curv = centers.mean() - fact.warpage.mean()
    s_c = centers.std(ddof=1)
    t_curv = curv / (s_c * math.sqrt(1 / 16 + 1 / 4))
    p_curv = 2 * stats.t.sf(abs(t_curv), 3)
    import statsmodels.formula.api as smf
    m = smf.ols("warpage ~ A + B + C + D + B:C", data=fact).fit()
    return {"effects": {k: round(v, 2) for k, v in sorted(eff.items(), key=lambda kv: -abs(kv[1]))},
            "Lenth PSE, margin of error": (round(pse, 2), round(me, 2)), "active effects": sig,
            "model (coded)": {k: round(v, 3) for k, v in m.params.items()}, "R^2": round(m.rsquared, 3),
            "center-point mean vs factorial mean (curvature)": round(curv, 2), "curvature p": round(p_curv, 3)}


def ex_fractional():
    df = load("fractional_flash.csv")
    eff = effects_2k(df, "flash", ["A", "B", "C", "D", "E"])
    # in a 2^(5-1) with I = ABCDE, main effects aliased with 4-factor, 2fi with 3fi
    main_2fi = {k: round(v, 2) for k, v in eff.items() if len(k) <= 2}
    pse, me = lenth_pse(main_2fi)
    # resolution III example: 2^(7-4), show alias of A
    return {"defining relation": "I = ABCDE (resolution V)",
            "main effects and 2-factor interactions": dict(sorted(main_2fi.items(), key=lambda kv: -abs(kv[1]))),
            "Lenth margin of error": round(me, 2),
            "active": {k: v for k, v in main_2fi.items() if abs(v) > me},
            "alias examples": {"A": "A = BCDE", "CE": "CE = ABD"}}


def ex_optimize():
    df = load("full_factorial_warpage.csv")
    fact = df[df.A != 0]
    import statsmodels.formula.api as smf
    m = smf.ols("warpage ~ A + B + C + D + B:C", data=fact).fit()
    rows = []
    for a_, b_, c_, d_ in itertools.product([-1, 1], repeat=4):
        w = float(m.predict(pd.DataFrame(dict(A=[a_], B=[b_], C=[c_], D=[d_])))[0])
        cycle = 30 + 4 * d_ + 1.5 * b_          # cooling time and mold temp lengthen the cycle (s)
        cost = cycle * 0.012 + (0.30 if w > 110 else 0.0)  # $ machine time + scrap risk above 110 um
        rows.append(((a_, b_, c_, d_), round(w, 1), cycle, round(cost, 3)))
    ok = [r for r in rows if r[1] <= 110]
    best = min(ok, key=lambda r: r[3])
    lowest = min(rows, key=lambda r: r[1])
    return {"lowest warpage setting (A,B,C,D)": lowest, "cheapest setting meeting warpage <= 110 um": best,
            "settings meeting spec": len(ok)}


def _clean(o):
    """Convert numpy scalars to plain Python numbers so printed output is readable."""
    if isinstance(o, dict):
        return {(_clean(k) if not isinstance(k, str) else k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"crd": ex_crd, "rbd": ex_rbd, "latin": ex_latin, "twofactor": ex_twofactor, "unbalanced": ex_unbalanced,
      "reps": ex_reps, "full": ex_full, "fractional": ex_fractional, "optimize": ex_optimize}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data" or not os.path.exists(os.path.join(D, "crd_suppliers.csv")):
        print(make_data())
        if which == "data":
            sys.exit()
    pd.set_option("display.width", 160)
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                print(f"  {a}: {_clean(b)}")
