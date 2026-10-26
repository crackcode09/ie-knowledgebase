"""sqckit.py - data and calculations for the Statistical Quality Control course.

Running case: Harbor Precision (fictional) turns steel pins and assembles small valve bodies.

    python tools/sqckit.py data          # (re)write data/*.csv (fixed seed)
    python tools/sqckit.py all           # every worked example
    python tools/sqckit.py <name>        # constants, describe, xbar_r, imr, p_chart, c_chart, short_run,
                                         # capability, oc, design, aoq, double

Control-chart constants are computed from the normal distribution (d2, d3 by numerical integration),
so no table is copied. Requires numpy, scipy, pandas. License: MIT
"""
from __future__ import annotations

import math
import os
import sys
from functools import lru_cache

import numpy as np
import pandas as pd
from scipy import integrate, stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")


# ---------------------------------------------------------------- control-chart constants
@lru_cache(maxsize=None)
def d2(n: int) -> float:
    """Expected range of n standard-normal values: integral of 1 - (1-Phi)^n - Phi^n."""
    f = lambda x: 1 - (1 - stats.norm.cdf(x)) ** n - stats.norm.cdf(x) ** n  # noqa: E731
    return integrate.quad(f, -np.inf, np.inf)[0]


@lru_cache(maxsize=None)
def d3(n: int) -> float:
    """Standard deviation of the range of n standard-normal values."""
    Phi = stats.norm.cdf
    g = lambda y, x: 1 - Phi(y) ** n - (1 - Phi(x)) ** n + (Phi(y) - Phi(x)) ** n  # noqa: E731
    val = integrate.dblquad(g, -8, 8, lambda x: x, lambda x: 8)[0]   # region x < y
    return math.sqrt(max(2 * val - d2(n) ** 2, 0.0))


def constants(n: int) -> dict:
    A2 = 3 / (d2(n) * math.sqrt(n))
    D3 = max(0.0, 1 - 3 * d3(n) / d2(n))
    D4 = 1 + 3 * d3(n) / d2(n)
    return dict(n=n, d2=d2(n), d3=d3(n), A2=A2, D3=D3, D4=D4)


# ---------------------------------------------------------------- data
def make_data(seed=1931):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    # 1. Pin diameter, 25 subgroups of 5 (mm): spec 12.000 +/- 0.030; shift up at subgroup 19
    rows = []
    for sg in range(1, 26):
        mu = 12.004 + (0.009 if sg >= 19 else 0.0)
        for k in range(5):
            rows.append(dict(subgroup=sg, piece=k + 1, diameter=round(mu + rng.normal(0, 0.0055), 4)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "pin_diameter_subgroups.csv"), index=False)
    # 2. Individuals: daily hardness test on a heat-treat batch (HRC), one point at day 17 off
    h = rng.normal(58.0, 0.6, 30)
    h[16] += 2.6
    pd.DataFrame(dict(day=range(1, 31), hardness_hrc=h.round(2))).to_csv(os.path.join(D, "daily_hardness.csv"), index=False)
    # 3. P chart: daily final inspection, varying n, defective valve bodies
    n = rng.integers(180, 320, 25)
    p = np.full(25, 0.035)
    p[20] = 0.085
    pd.DataFrame(dict(day=range(1, 26), inspected=n, defective=rng.binomial(n, p))).to_csv(
        os.path.join(D, "valve_final_inspection.csv"), index=False)
    # 4. C chart: surface defects per casting (constant area)
    c = rng.poisson(4.2, 30)
    c[11] = 13
    pd.DataFrame(dict(casting=range(1, 31), defects=c)).to_csv(os.path.join(D, "casting_defects.csv"), index=False)
    # 5. Short run: three pin part numbers on one lathe, different nominals, similar sigma
    parts = [("P-120", 12.000), ("P-095", 9.500), ("P-150", 15.000)]
    rows = []
    seq = rng.choice(3, 24)
    for i, j in enumerate(seq):
        pn, nom = parts[j]
        off = 0.012 if (pn == "P-095" and i >= 16) else 0.0
        meas = nom + 0.002 + off + rng.normal(0, 0.006, 3)
        for k, x in enumerate(meas):
            rows.append(dict(run=i + 1, part_number=pn, nominal=nom, piece=k + 1, diameter=round(x, 4)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "short_run_lathe.csv"), index=False)
    # 6. Capability study: 100 consecutive pins from a stable period
    pd.DataFrame(dict(piece=range(1, 101), diameter=np.round(rng.normal(12.006, 0.0058, 100), 4))).to_csv(
        os.path.join(D, "capability_study.csv"), index=False)
    return "data written"


def load(name):
    return pd.read_csv(os.path.join(D, name))


# ---------------------------------------------------------------- run rules
def western_electric(x, center, sigma):
    """Return {rule: [indices]} for the four classic run rules (1-based indices)."""
    z = (np.asarray(x) - center) / sigma
    out = {"1: beyond 3 sigma": [], "2: 2 of 3 beyond 2 sigma (same side)": [],
           "3: 4 of 5 beyond 1 sigma (same side)": [], "4: 8 in a row on one side": []}
    for i in range(len(z)):
        if abs(z[i]) > 3:
            out["1: beyond 3 sigma"].append(i + 1)
        for s in (1, -1):
            if i >= 2 and sum(s * z[i - 2:i + 1] > 2) >= 2 and s * z[i] > 2:
                out["2: 2 of 3 beyond 2 sigma (same side)"].append(i + 1)
            if i >= 4 and sum(s * z[i - 4:i + 1] > 1) >= 4 and s * z[i] > 1:
                out["3: 4 of 5 beyond 1 sigma (same side)"].append(i + 1)
            if i >= 7 and all(s * z[i - 7:i + 1] > 0):
                out["4: 8 in a row on one side"].append(i + 1)
    return {k: sorted(set(v)) for k, v in out.items()}


# ---------------------------------------------------------------- examples
def ex_constants():
    rows = []
    for n in range(2, 11):
        c = constants(n)
        rows.append({k: (round(v, 4) if isinstance(v, float) else v) for k, v in c.items()})
    return {"computed constants (n = 2..10)": rows}


def ex_describe():
    d = load("capability_study.csv").diameter
    q1, q3 = d.quantile([0.25, 0.75])
    return {"n": len(d), "mean": round(d.mean(), 5), "median": round(d.median(), 4),
            "mode (rounded to 0.001)": float(d.round(3).mode().iloc[0]), "range": round(d.max() - d.min(), 4),
            "sample SD": round(d.std(ddof=1), 5), "variance": f"{d.var(ddof=1):.3e}", "IQR": round(q3 - q1, 4),
            "skewness": round(float(stats.skew(d, bias=False)), 3), "excess kurtosis": round(float(stats.kurtosis(d, bias=False)), 3),
            "Shapiro-Wilk p": round(stats.shapiro(d).pvalue, 3)}


def xbar_r_limits(df, phase_end=None):
    g = df.groupby("subgroup").diameter
    xb, r = g.mean(), g.max() - g.min()
    base = slice(None) if phase_end is None else slice(1, phase_end)
    xbb, rb = xb.loc[base].mean(), r.loc[base].mean()
    c = constants(5)
    return xb, r, dict(xbarbar=xbb, rbar=rb, UCLx=xbb + c["A2"] * rb, LCLx=xbb - c["A2"] * rb,
                       UCLr=c["D4"] * rb, LCLr=c["D3"] * rb, sigma_hat=rb / c["d2"])


def ex_xbar_r():
    df = load("pin_diameter_subgroups.csv")
    xb, r, L = xbar_r_limits(df, phase_end=18)
    sig_x = L["sigma_hat"] / math.sqrt(5)
    rules = western_electric(xb.values, L["xbarbar"], sig_x)
    out_r = [int(i) for i in r.index if r[i] > L["UCLr"] or r[i] < L["LCLr"]]
    return {"limits from subgroups 1-18 (mm)": {k: round(v, 5) for k, v in L.items()},
            "A2, D3, D4, d2 for n = 5": tuple(round(constants(5)[k], 3) for k in ("A2", "D3", "D4", "d2")),
            "R chart points out of limits": out_r,
            "X-bar run-rule signals (subgroup numbers)": {k: v for k, v in rules.items() if v},
            "mean of subgroups 19-25 vs 1-18": (round(xb.loc[19:].mean(), 4), round(xb.loc[:18].mean(), 4))}


def ex_imr():
    h = load("daily_hardness.csv").hardness_hrc.values
    mr = np.abs(np.diff(h))
    xbar, mrbar = h.mean(), mr.mean()
    L = dict(center=xbar, UCL=xbar + 2.66 * mrbar, LCL=xbar - 2.66 * mrbar, MRbar=mrbar, UCL_MR=3.267 * mrbar)
    out = [i + 1 for i, v in enumerate(h) if v > L["UCL"] or v < L["LCL"]]
    mr_out = [i + 2 for i, v in enumerate(mr) if v > L["UCL_MR"]]
    # revised limits without day 17
    keep = np.delete(h, 16)
    mr2 = np.abs(np.diff(keep))
    rev = dict(center=keep.mean(), UCL=keep.mean() + 2.66 * mr2.mean(), LCL=keep.mean() - 2.66 * mr2.mean())
    return {"limits (HRC)": {k: round(v, 3) for k, v in L.items()}, "2.66 = 3/d2(2)": round(3 / d2(2), 3),
            "3.267 = D4(2)": round(constants(2)["D4"], 3), "points beyond limits (day)": out,
            "moving ranges beyond UCL (ending day)": mr_out,
            "revised limits after removing day 17 (assignable cause found)": {k: round(v, 3) for k, v in rev.items()}}


def ex_p_chart():
    d = load("valve_final_inspection.csv")
    pbar = d.defective.sum() / d.inspected.sum()
    d["p"] = d.defective / d.inspected
    d["UCL"] = pbar + 3 * np.sqrt(pbar * (1 - pbar) / d.inspected)
    d["LCL"] = (pbar - 3 * np.sqrt(pbar * (1 - pbar) / d.inspected)).clip(lower=0)
    sig = d[(d.p > d.UCL) | (d.p < d.LCL)]
    return {"total inspected / defective": (int(d.inspected.sum()), int(d.defective.sum())),
            "p-bar %": round(100 * pbar, 3),
            "limits for n = 180 and n = 320 (%)": tuple(round(100 * (pbar + 3 * math.sqrt(pbar * (1 - pbar) / n)), 2) for n in (180, 320)),
            "LCL (all days)": "0 (negative limit truncated)" if (d.LCL == 0).all() else "varies",
            "days beyond UCL": sig[["day", "inspected", "defective"]].assign(p_pct=(100 * sig.p).round(2),
                                                                         UCL_pct=(100 * sig.UCL).round(2)).to_dict("records")}


def ex_c_chart():
    d = load("casting_defects.csv").defects.values
    cbar = d.mean()
    ucl, lcl = cbar + 3 * math.sqrt(cbar), max(0.0, cbar - 3 * math.sqrt(cbar))
    out = [i + 1 for i, v in enumerate(d) if v > ucl]
    keep = np.delete(d, [i - 1 for i in out])
    c2 = keep.mean()
    return {"c-bar": round(cbar, 3), "UCL / LCL": (round(ucl, 2), round(lcl, 2)), "castings beyond UCL": out,
            "revised c-bar, UCL after removing them": (round(c2, 3), round(c2 + 3 * math.sqrt(c2), 2))}


def ex_short_run():
    d = load("short_run_lathe.csv")
    d["dev"] = d.diameter - d.nominal
    g = d.groupby("run").agg(part=("part_number", "first"), xbar_dev=("dev", "mean"),
                             r=("dev", lambda s: s.max() - s.min()))
    c = constants(3)
    xbb, rb = g.xbar_dev.mean(), g.r.mean()
    UCL, LCL = xbb + c["A2"] * rb, xbb - c["A2"] * rb
    sig = g[(g.xbar_dev > UCL) | (g.xbar_dev < LCL)]
    # standardized (Z) version uses each part's own target and sigma estimate
    sd_by_part = d.groupby(["part_number", "run"]).dev.apply(lambda s: s.max() - s.min()).groupby("part_number").mean() / c["d2"]
    return {"runs / parts": (len(g), sorted(d.part_number.unique())),
            "DNOM chart: center, UCL, LCL (mm from nominal)": (round(xbb, 5), round(UCL, 5), round(LCL, 5)),
            "Rbar, UCL_R": (round(rb, 5), round(c["D4"] * rb, 5)),
            "runs beyond limits": sig.reset_index().round(5).to_dict("records"),
            "sigma estimate by part (Rbar/d2), similar?": sd_by_part.round(5).to_dict()}


def capability(x, lsl, usl, sigma_within):
    mu, s_overall = x.mean(), x.std(ddof=1)
    cp = (usl - lsl) / (6 * sigma_within)
    cpk = min(usl - mu, mu - lsl) / (3 * sigma_within)
    pp = (usl - lsl) / (6 * s_overall)
    ppk = min(usl - mu, mu - lsl) / (3 * s_overall)
    ppm = 1e6 * (stats.norm.sf((usl - mu) / s_overall) + stats.norm.cdf((lsl - mu) / s_overall))
    return dict(mean=mu, sigma_within=sigma_within, sigma_overall=s_overall, Cp=cp, Cpk=cpk, Pp=pp, Ppk=ppk,
                ppm_expected=ppm)


def ex_capability():
    x = load("capability_study.csv").diameter
    mr = np.abs(np.diff(x.values)).mean()
    sw = mr / d2(2)
    c = capability(x, 11.970, 12.030, sw)
    centered_ppm = 1e6 * 2 * stats.norm.sf(0.030 / c["sigma_overall"])
    obs_out = int(((x < 11.970) | (x > 12.030)).sum())
    return {"spec": "12.000 +/- 0.030 mm", **{k: round(v, 5) if k.startswith(("mean", "sigma")) else round(v, 3)
                                              for k, v in c.items()},
            "observed out of spec (of 100)": obs_out,
            "ppm if centred at 12.000": round(centered_ppm, 1),
            "Cpk if 12-pin shift (+0.009) persists, same sigma": round(min(12.030 - (c["mean"] + 0.009), (c["mean"] + 0.009) - 11.970) / (3 * sw), 3)}


# ---------------------------------------------------------------- acceptance sampling
def pa_single(p, n, c, N=None):
    if N is None:
        return stats.binom.cdf(c, n, p)
    D = int(round(p * N))
    return stats.hypergeom.cdf(c, N, D, n)


def ex_oc():
    n, c, N = 80, 2, 2000
    ps = [0.005, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.08, 0.10]
    return {"plan": f"N = {N}, n = {n}, c = {c}",
            "P(accept) by lot % defective (binomial)": {f"{100*p:g}%": round(pa_single(p, n, c), 4) for p in ps},
            "hypergeometric check at 2% and 6%": (round(pa_single(0.02, n, c, N), 4), round(pa_single(0.06, n, c, N), 4)),
            "producer's risk at AQL 1%": round(1 - pa_single(0.01, n, c), 4),
            "consumer's risk at LTPD 6%": round(pa_single(0.06, n, c), 4)}


def design_single(aql, alpha, ltpd, beta, nmax=1000):
    """Smallest n (and its c) with P(acc | AQL) >= 1-alpha and P(acc | LTPD) <= beta (binomial)."""
    for n in range(1, nmax + 1):
        for c in range(0, n):
            if stats.binom.cdf(c, n, ltpd) > beta:
                break
            if stats.binom.cdf(c, n, aql) >= 1 - alpha:
                return n, c
    return None


def ex_design():
    n, c = design_single(0.01, 0.05, 0.06, 0.10)
    return {"requirement": "AQL 1% with alpha 5%; LTPD 6% with beta 10%", "smallest plan (n, c)": (n, c),
            "achieved P(accept) at AQL / LTPD": (round(pa_single(0.01, n, c), 4), round(pa_single(0.06, n, c), 4)),
            "tighter: LTPD 4%, beta 10%": design_single(0.01, 0.05, 0.04, 0.10)}


def ex_aoq():
    n, c, N = 80, 2, 2000
    ps = np.linspace(0.0005, 0.12, 2400)
    pa = stats.binom.cdf(c, n, ps)
    aoq = pa * ps * (N - n) / N
    i = int(np.argmax(aoq))
    ati = lambda p: n + (1 - pa_single(p, n, c)) * (N - n)  # noqa: E731
    return {"plan": f"N = {N}, n = {n}, c = {c}, rejected lots 100% inspected (rectifying)",
            "AOQ at 1%, 2%, 4% (%)": tuple(round(100 * pa_single(p, n, c) * p * (N - n) / N, 3) for p in (0.01, 0.02, 0.04)),
            "AOQL (%)": round(100 * aoq[i], 3), "at incoming quality (%)": round(100 * ps[i], 2),
            "ATI at 1%, 2%, 4%": tuple(round(ati(p)) for p in (0.01, 0.02, 0.04))}


def double_plan_pa_asn(p, n1=40, c1=0, r1=2, n2=80, c2=4):
    """Double sampling: accept if d1<=c1; reject if d1>=r1; else take n2 and accept if d1+d2<=c2."""
    b1 = stats.binom.pmf
    pa1 = stats.binom.cdf(c1, n1, p)
    pa2 = sum(b1(d1, n1, p) * stats.binom.cdf(c2 - d1, n2, p) for d1 in range(c1 + 1, r1))
    p_second = sum(b1(d1, n1, p) for d1 in range(c1 + 1, r1))
    return pa1 + pa2, n1 + n2 * p_second


def ex_double():
    out = {}
    for p in (0.005, 0.01, 0.02, 0.04, 0.06, 0.10):
        pa, asn = double_plan_pa_asn(p)
        out[f"{100*p:g}%"] = {"P(accept) double": round(pa, 4), "ASN double": round(asn, 1),
                              "P(accept) single n=80,c=2": round(pa_single(p, 80, 2), 4)}
    return {"double plan": "n1 = 40, c1 = 0, r1 = 2; n2 = 80, c2 = 4 (chosen to match the single plan's OC curve)",
            "comparison": out}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"constants": ex_constants, "describe": ex_describe, "xbar_r": ex_xbar_r, "imr": ex_imr, "p_chart": ex_p_chart,
      "c_chart": ex_c_chart, "short_run": ex_short_run, "capability": ex_capability, "oc": ex_oc, "design": ex_design,
      "aoq": ex_aoq, "double": ex_double}

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
