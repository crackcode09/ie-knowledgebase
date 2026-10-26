"""statkit.py - data generator and worked examples for the Applied Statistics course.

Running case: a contract electronics assembler (printed circuit board assemblies).

    python tools/statkit.py data       # (re)generate data/*.csv (fixed seed)
    python tools/statkit.py all        # every worked example
    python tools/statkit.py <name>     # describe, hypergeom, binomial, poisson, normal, exponential,
                                    # sampling, ci, tests, nonnormal, correlation, regression, multiple

License: MIT
"""
from __future__ import annotations

import csv
import math
import os
import sys

import numpy as np
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")


def write(name, header, rows):
    os.makedirs(D, exist_ok=True)
    with open(os.path.join(D, name), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)


def load(name):
    with open(os.path.join(D, name), newline="") as f:
        return list(csv.DictReader(f))


def col(rows, k):
    return np.array([float(r[k]) for r in rows])


def make_data(seed=1662):
    rng = np.random.default_rng(seed)
    # 1. Reflow oven cycle time per board (s), 120 boards: roughly normal
    ct = rng.normal(62.0, 2.4, 120)
    write("cycle_time.csv", ["board", "seconds"], [[i + 1, f"{v:.1f}"] for i, v in enumerate(ct)])
    # 2. Rework repair time (min), 80 repairs: right-skewed
    rt = rng.lognormal(math.log(14), 0.6, 80)
    write("rework_time.csv", ["repair", "minutes"], [[i + 1, f"{v:.1f}"] for i, v in enumerate(rt)])
    # 3. Solder-joint defects per board, 200 boards: Poisson mean 0.8
    dfx = rng.poisson(0.8, 200)
    write("defects_per_board.csv", ["board", "defects"], [[i + 1, int(v)] for i, v in enumerate(dfx)])
    # 4. Time between failures of the pick-and-place machine (h), 40 failures: exponential, mean 55 h
    tbf = rng.exponential(55, 40)
    write("time_between_failures.csv", ["failure", "hours"], [[i + 1, f"{v:.1f}"] for i, v in enumerate(tbf)])
    # 5. Solder paste thickness (um), two printers, 25 each
    a = rng.normal(127, 4.0, 25)
    b = rng.normal(129, 6.5, 25)
    write("paste_thickness.csv", ["printer", "um"],
          [["P1", f"{v:.1f}"] for v in a] + [["P2", f"{v:.1f}"] for v in b])
    # 6. Monthly business data, 30 months: revenue vs orders, quoting lead time, on-time %, marketing
    orders = rng.normal(420, 60, 30)
    quote_days = rng.uniform(1, 6, 30)
    ontime = np.clip(rng.normal(92, 3, 30), 80, 99.5)
    promo = rng.uniform(0, 20, 30)          # k$ spent on trade shows/marketing
    revenue = 50 + 2.9 * orders - 18 * quote_days + 6.0 * (ontime - 92) + 0.4 * promo + rng.normal(0, 55, 30)
    write("monthly_business.csv", ["month", "orders", "quote_days", "ontime_pct", "promo_k", "revenue_k"],
          [[i + 1, f"{o:.0f}", f"{q:.1f}", f"{t:.1f}", f"{p:.1f}", f"{r:.0f}"]
           for i, (o, q, t, p, r) in enumerate(zip(orders, quote_days, ontime, promo, revenue))])
    return "data written"


# ------------------------------------------------------------ examples
def ex_describe():
    out = {}
    for name, k in (("cycle_time.csv", "seconds"), ("rework_time.csv", "minutes")):
        x = col(load(name), k)
        q1, q3 = np.percentile(x, [25, 75])
        vals, counts = np.unique(np.round(x), return_counts=True)
        out[name] = {"n": len(x), "mean": round(x.mean(), 2), "median": round(float(np.median(x)), 2),
                     "mode (rounded)": float(vals[counts.argmax()]), "sd": round(x.std(ddof=1), 2),
                     "range": round(float(np.ptp(x)), 2), "IQR": round(float(q3 - q1), 2),
                     "skewness": round(float(stats.skew(x, bias=False)), 2),
                     "excess kurtosis": round(float(stats.kurtosis(x, bias=False)), 2)}
    return out


def ex_hypergeom():
    # Lot of 500 boards with 10 defective; sample 50, accept if 0 or 1 defective
    N, K, n, c = 500, 10, 50, 1
    p_accept = stats.hypergeom.cdf(c, N, K, n)
    p0 = stats.hypergeom.pmf(0, N, K, n)
    binom_approx = stats.binom.cdf(c, n, K / N)
    oc = {k: round(float(stats.hypergeom.cdf(c, N, k, n)), 3) for k in (0, 5, 10, 20, 30)}
    return {"P(0 defective in sample)": round(p0, 4), "P(accept, c=1)": round(p_accept, 4),
            "binomial approximation": round(binom_approx, 4),
            "OC curve: defectives in lot -> P(accept)": oc}


def ex_binomial():
    # First-pass yield 96%: in a batch of 25 boards, how many fail?
    n, p = 25, 0.04
    pmf = {k: round(float(stats.binom.pmf(k, n, p)), 4) for k in range(5)}
    return {"P(k failures in 25), p=0.04": pmf, "P(0)": round(float(stats.binom.pmf(0, n, p)), 4),
            "P(>=3)": round(float(stats.binom.sf(2, n, p)), 4), "mean": n * p,
            "sd": round(math.sqrt(n * p * (1 - p)), 3)}


def ex_poisson():
    x = col(load("defects_per_board.csv"), "defects")
    lam = x.mean()
    obs = {k: int((x == k).sum()) for k in range(5)}
    obs[">=5"] = int((x >= 5).sum())
    exp = {k: round(200 * float(stats.poisson.pmf(k, lam)), 1) for k in range(5)}
    exp[">=5"] = round(200 * float(stats.poisson.sf(4, lam)), 1)
    return {"mean defects/board": round(lam, 3), "variance": round(x.var(ddof=1), 3),
            "observed counts": obs, "Poisson expected": exp,
            "P(board defect-free)": round(math.exp(-lam), 3),
            "P(>=3 defects)": round(float(stats.poisson.sf(2, lam)), 4),
            "DPU": round(lam, 3), "rolled yield e^-DPU": round(math.exp(-lam), 3)}


def ex_normal():
    x = col(load("cycle_time.csv"), "seconds")
    m, s = x.mean(), x.std(ddof=1)
    usl = 68.0
    z = (usl - m) / s
    p_over = stats.norm.sf(z)
    obs_over = int((x > usl).sum())
    return {"mean": round(m, 2), "sd": round(s, 2), "USL (s)": usl, "z": round(z, 2),
            "P(cycle > 68 s)": round(p_over, 4), "ppm": round(p_over * 1e6),
            "observed > 68 s": f"{obs_over} of {len(x)}", "95th percentile": round(stats.norm.ppf(0.95, m, s), 2),
            "Shapiro-Wilk p": round(stats.shapiro(x).pvalue, 3)}


def ex_exponential():
    x = col(load("time_between_failures.csv"), "hours")
    mtbf = x.mean()
    lam = 1 / mtbf
    r8 = math.exp(-8 / mtbf)
    r40 = math.exp(-40 / mtbf)
    chi_lo = stats.chi2.ppf(0.025, 2 * len(x))
    chi_hi = stats.chi2.ppf(0.975, 2 * len(x))
    ci = (2 * x.sum() / chi_hi, 2 * x.sum() / chi_lo)
    return {"MTBF (h)": round(mtbf, 1), "failure rate (/h)": round(lam, 4),
            "P(no failure in an 8-h shift)": round(r8, 3), "P(no failure in a 40-h week)": round(r40, 3),
            "MTBF 95% CI (chi-square)": tuple(round(v, 1) for v in ci),
            "sd / mean (exponential -> ~1)": round(x.std(ddof=1) / mtbf, 2)}


def ex_sampling(seed=4):
    rng = np.random.default_rng(seed)
    pop = col(load("rework_time.csv"), "minutes")  # skewed "population"
    means = {n: [rng.choice(pop, n).mean() for _ in range(5000)] for n in (2, 5, 30)}
    out = {f"n={n}": {"sd of means": round(float(np.std(v)), 2), "theory s/sqrt(n)": round(pop.std() / math.sqrt(n), 2),
                      "skewness of means": round(float(stats.skew(v)), 2)} for n, v in means.items()}
    out["t critical (95%, df 4, 9, 29, inf)"] = tuple(round(float(stats.t.ppf(0.975, d)), 3) for d in (4, 9, 29, 10**6))
    out["chi-square 2.5% / 97.5% (df 24)"] = (round(float(stats.chi2.ppf(0.025, 24)), 2), round(float(stats.chi2.ppf(0.975, 24)), 2))
    out["F 97.5% (24, 24)"] = round(float(stats.f.ppf(0.975, 24, 24)), 3)
    return out


def ex_ci():
    x = col(load("cycle_time.csv"), "seconds")
    n, m, s = len(x), x.mean(), x.std(ddof=1)
    t = stats.t.ppf(0.975, n - 1)
    ci_mean = (m - t * s / math.sqrt(n), m + t * s / math.sqrt(n))
    lo = math.sqrt((n - 1) * s * s / stats.chi2.ppf(0.975, n - 1))
    hi = math.sqrt((n - 1) * s * s / stats.chi2.ppf(0.025, n - 1))
    d = col(load("defects_per_board.csv"), "defects")
    k, nb = int((d > 0).sum()), len(d)
    p = k / nb
    z = 1.96
    wald = (p - z * math.sqrt(p * (1 - p) / nb), p + z * math.sqrt(p * (1 - p) / nb))
    wil = stats.binomtest(k, nb).proportion_ci(0.95, method="wilson")
    return {"cycle time mean 95% CI": tuple(round(v, 2) for v in ci_mean),
            "cycle time sd 95% CI": (round(lo, 2), round(hi, 2)),
            "boards with >=1 defect": f"{k}/{nb} = {p:.3f}",
            "proportion 95% CI (normal approx)": tuple(round(v, 3) for v in wald),
            "proportion 95% CI (Wilson)": (round(wil.low, 3), round(wil.high, 3))}


def ex_tests():
    x = col(load("cycle_time.csv"), "seconds")
    t1 = stats.ttest_1samp(x, 61.0)
    d = col(load("defects_per_board.csv"), "defects")
    k, n = int((d > 0).sum()), len(d)
    pt = stats.binomtest(k, n, 0.50, alternative="greater")
    pa = load("paste_thickness.csv")
    p1 = np.array([float(r["um"]) for r in pa if r["printer"] == "P1"])
    p2 = np.array([float(r["um"]) for r in pa if r["printer"] == "P2"])
    chi = (len(p1) - 1) * p1.var(ddof=1) / 5.0 ** 2
    p_var1 = stats.chi2.sf(chi, len(p1) - 1)  # H1: sigma > 5
    chi2v = (len(p2) - 1) * p2.var(ddof=1) / 5.0 ** 2
    p_var2 = stats.chi2.sf(chi2v, len(p2) - 1)
    F = p2.var(ddof=1) / p1.var(ddof=1)
    pF = 2 * min(stats.f.sf(F, 24, 24), stats.f.cdf(F, 24, 24))
    lev = stats.levene(p1, p2, center="median")
    welch = stats.ttest_ind(p1, p2, equal_var=False)
    return {"mean cycle time vs 61.0 s: t, p": (round(t1.statistic, 2), round(t1.pvalue, 4)),
            "share of boards with a defect vs 50% (H1 >): p": round(pt.pvalue, 4),
            "printer sd": (round(p1.std(ddof=1), 2), round(p2.std(ddof=1), 2)),
            "P1 sigma > 5 um: chi2, p": (round(chi, 1), round(p_var1, 3)),
            "P2 sigma > 5 um: chi2, p": (round(chi2v, 1), round(p_var2, 3)),
            "P2 vs P1 variance: F, p": (round(F, 2), round(pF, 4)), "Levene p": round(lev.pvalue, 4),
            "means: Welch t, p": (round(welch.statistic, 2), round(welch.pvalue, 3)),
            "printer means": (round(p1.mean(), 1), round(p2.mean(), 1))}


def ex_nonnormal(seed=7):
    x = col(load("rework_time.csv"), "minutes")
    lx = np.log(x)
    rng = np.random.default_rng(seed)
    boots = np.array([np.median(rng.choice(x, len(x))) for _ in range(5000)])
    bc = stats.boxcox(x)
    return {"raw: skew, Shapiro p": (round(stats.skew(x), 2), round(stats.shapiro(x).pvalue, 4)),
            "log: skew, Shapiro p": (round(stats.skew(lx), 2), round(stats.shapiro(lx).pvalue, 3)),
            "Box-Cox lambda": round(bc[1], 2),
            "mean, median (min)": (round(x.mean(), 1), round(float(np.median(x)), 1)),
            "90th pct: empirical / normal model / lognormal model": (
                round(float(np.percentile(x, 90)), 1), round(stats.norm.ppf(0.9, x.mean(), x.std(ddof=1)), 1),
                round(math.exp(lx.mean() + stats.norm.ppf(0.9) * lx.std(ddof=1)), 1)),
            "median 95% CI (bootstrap)": tuple(np.round(np.percentile(boots, [2.5, 97.5]), 1)),
            "sign test median vs 12 min: p": round(stats.binomtest(int((x > 12).sum()), int((x != 12).sum())).pvalue, 4)}


def ex_correlation():
    b = load("monthly_business.csv")
    keys = ["orders", "quote_days", "ontime_pct", "promo_k", "revenue_k"]
    M = np.array([col(b, k) for k in keys])
    r = np.corrcoef(M)
    out = {f"r(revenue, {k})": round(r[4, i], 3) for i, k in enumerate(keys[:4])}
    for i, k in enumerate(keys[:4]):
        out[f"p(revenue, {k})"] = round(stats.pearsonr(M[4], M[i]).pvalue, 4)
    return out


def ex_regression():
    b = load("monthly_business.csv")
    x, y = col(b, "orders"), col(b, "revenue_k")
    res = stats.linregress(x, y)
    n = len(x)
    yhat = res.intercept + res.slope * x
    s = math.sqrt(((y - yhat) ** 2).sum() / (n - 2))
    x0 = 500
    se_pred = s * math.sqrt(1 + 1 / n + (x0 - x.mean()) ** 2 / ((x - x.mean()) ** 2).sum())
    t = stats.t.ppf(0.975, n - 2)
    pred = res.intercept + res.slope * x0
    return {"revenue_k = b0 + b1 x orders": (round(res.intercept, 1), round(res.slope, 3)),
            "R^2": round(res.rvalue ** 2, 3), "slope p": round(res.pvalue, 6), "s (k$)": round(s, 1),
            "prediction at 500 orders (k$)": round(pred, 0),
            "95% prediction interval": (round(pred - t * se_pred, 0), round(pred + t * se_pred, 0))}


def ex_multiple():
    import statsmodels.api as sm
    b = load("monthly_business.csv")
    names = ["orders", "quote_days", "ontime_pct", "promo_k"]
    X = np.column_stack([col(b, k) for k in names])
    y = col(b, "revenue_k")
    m = sm.OLS(y, sm.add_constant(X)).fit()
    keep = ["orders", "quote_days", "ontime_pct"]
    X2 = np.column_stack([col(b, k) for k in keep])
    m2 = sm.OLS(y, sm.add_constant(X2)).fit()
    new = np.array([[1, 480, 2.0, 95.0]])
    pr = m2.get_prediction(new).summary_frame(alpha=0.05)
    return {"full coefficients": dict(zip(["const"] + names, np.round(m.params, 3))),
            "full p-values": dict(zip(["const"] + names, np.round(m.pvalues, 4))),
            "full R^2 / adj": (round(m.rsquared, 3), round(m.rsquared_adj, 3)),
            "reduced coefficients": dict(zip(["const"] + keep, np.round(m2.params, 3))),
            "reduced p-values": dict(zip(["const"] + keep, np.round(m2.pvalues, 4))),
            "reduced R^2 / adj": (round(m2.rsquared, 3), round(m2.rsquared_adj, 3)),
            "prediction: 480 orders, 2-day quotes, 95% on time (k$)": round(float(pr["mean"].iloc[0]), 0),
            "95% prediction interval": (round(float(pr["obs_ci_lower"].iloc[0]), 0), round(float(pr["obs_ci_upper"].iloc[0]), 0))}


EX = {"describe": ex_describe, "hypergeom": ex_hypergeom, "binomial": ex_binomial, "poisson": ex_poisson,
      "normal": ex_normal, "exponential": ex_exponential, "sampling": ex_sampling, "ci": ex_ci, "tests": ex_tests,
      "nonnormal": ex_nonnormal, "correlation": ex_correlation, "regression": ex_regression, "multiple": ex_multiple}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data" or not os.path.exists(os.path.join(D, "cycle_time.csv")):
        print(make_data())
        if which == "data":
            sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                print(f"  {a}: {b}")
