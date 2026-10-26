"""htest.py - readable hypothesis tests for the Fundamentals of Hypothesis Testing course.

Thin wrappers around scipy.stats that print the hypotheses, the statistic,
the p-value, a confidence interval and a plain-language conclusion.

    python tools/htest.py all          # run every worked example in the course
    python tools/htest.py one-mean     # or one example by name

License: MIT
"""
from __future__ import annotations

import csv
import math
import os
import sys

import numpy as np
from scipy import stats

DATA = os.path.join(os.path.dirname(__file__), "..", "data")


def load(name):
    with open(os.path.join(DATA, name), newline="") as f:
        return list(csv.DictReader(f))


def col(rows, key, where=None):
    return np.array([float(r[key]) for r in rows if where is None or where(r)])


def verdict(p, alpha=0.05):
    return (f"p = {p:.4g} < {alpha} -> reject H0" if p < alpha
            else f"p = {p:.4g} >= {alpha} -> fail to reject H0")


def banner(title, h0, ha):
    print("\n" + "=" * 70 + f"\n{title}\n  H0: {h0}\n  Ha: {ha}")


# ------------------------------------------------------------------ means
def one_mean(x, mu0, alpha=0.05):
    n, m, s = len(x), x.mean(), x.std(ddof=1)
    t, p = stats.ttest_1samp(x, mu0)
    tc = stats.t.ppf(1 - alpha / 2, n - 1)
    ci = (m - tc * s / math.sqrt(n), m + tc * s / math.sqrt(n))
    return dict(n=n, mean=m, sd=s, t=t, df=n - 1, p=p, ci=ci)


def two_means(x, y, alpha=0.05):
    r = stats.ttest_ind(x, y, equal_var=False)  # Welch
    ci = r.confidence_interval(1 - alpha)
    return dict(mean_x=x.mean(), mean_y=y.mean(), sd_x=x.std(ddof=1), sd_y=y.std(ddof=1),
                diff=x.mean() - y.mean(), t=r.statistic, df=r.df, p=r.pvalue, ci=(ci.low, ci.high))


def paired(x, y, alpha=0.05):
    d = y - x
    r = stats.ttest_rel(y, x)
    ci = r.confidence_interval(1 - alpha)
    return dict(n=len(d), mean_d=d.mean(), sd_d=d.std(ddof=1), t=r.statistic, df=r.df, p=r.pvalue,
                ci=(ci.low, ci.high))


def anova(groups: dict):
    f, p = stats.f_oneway(*groups.values())
    allv = np.concatenate(list(groups.values()))
    gm = allv.mean()
    ssb = sum(len(v) * (v.mean() - gm) ** 2 for v in groups.values())
    ssw = sum(((v - v.mean()) ** 2).sum() for v in groups.values())
    k, N = len(groups), len(allv)
    return dict(means={g: v.mean() for g, v in groups.items()}, ssb=ssb, ssw=ssw,
                dfb=k - 1, dfw=N - k, msb=ssb / (k - 1), msw=ssw / (N - k), F=f, p=p,
                eta2=ssb / (ssb + ssw))


# ------------------------------------------------------------ proportions
def one_prop(d, n, p0, alt="greater"):
    ph = d / n
    z = (ph - p0) / math.sqrt(p0 * (1 - p0) / n)
    exact = stats.binomtest(d, n, p0, alternative=alt)
    ci = exact.proportion_ci(0.95, method="exact")
    pz = stats.norm.sf(z) if alt == "greater" else 2 * stats.norm.sf(abs(z))
    return dict(phat=ph, z=z, p_normal=pz, p_exact=exact.pvalue, ci=(ci.low, ci.high))


def two_prop(d1, n1, d2, n2):
    p1, p2 = d1 / n1, d2 / n2
    pp = (d1 + d2) / (n1 + n2)
    z = (p1 - p2) / math.sqrt(pp * (1 - pp) * (1 / n1 + 1 / n2))
    p = 2 * stats.norm.sf(abs(z))
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)
    ci = (p1 - p2 - 1.96 * se, p1 - p2 + 1.96 * se)
    fisher = stats.fisher_exact([[d1, n1 - d1], [d2, n2 - d2]]).pvalue
    return dict(p1=p1, p2=p2, pooled=pp, z=z, p=p, ci=ci, p_fisher=fisher)


def chi_square(table):
    r = stats.chi2_contingency(np.asarray(table))
    return dict(chi2=r.statistic, df=r.dof, p=r.pvalue, expected=r.expected_freq)


# -------------------------------------------------------------- variances
def one_var(x, sigma0):
    n, s = len(x), x.std(ddof=1)
    chi2 = (n - 1) * s ** 2 / sigma0 ** 2
    p = stats.chi2.sf(chi2, n - 1)  # Ha: sigma > sigma0
    lo = math.sqrt((n - 1) * s ** 2 / stats.chi2.ppf(0.975, n - 1))
    hi = math.sqrt((n - 1) * s ** 2 / stats.chi2.ppf(0.025, n - 1))
    return dict(n=n, s=s, chi2=chi2, df=n - 1, p=p, ci_sigma=(lo, hi))


def two_var(x, y):
    F = x.var(ddof=1) / y.var(ddof=1)
    d1, d2 = len(x) - 1, len(y) - 1
    p = 2 * min(stats.f.sf(F, d1, d2), stats.f.cdf(F, d1, d2))
    lev = stats.levene(x, y, center="median")
    return dict(s_x=x.std(ddof=1), s_y=y.std(ddof=1), F=F, df=(d1, d2), p=p,
                levene_W=lev.statistic, levene_p=lev.pvalue)


# ---------------------------------------------------------- nonparametric
def mann_whitney(x, y):
    r = stats.mannwhitneyu(x, y, alternative="two-sided")
    return dict(med_x=np.median(x), med_y=np.median(y), U=r.statistic, p=r.pvalue)


def wilcoxon_paired(x, y):
    r = stats.wilcoxon(x, y, zero_method="wilcox")
    return dict(med_d=np.median(y - x), W=r.statistic, p=r.pvalue, n_nonzero=int(np.sum(y != x)))


def sign_test(x, y):
    d = y - x
    pos, neg = int(np.sum(d > 0)), int(np.sum(d < 0))
    return dict(pos=pos, neg=neg, p=stats.binomtest(pos, pos + neg, 0.5).pvalue)


def kruskal(groups: dict):
    r = stats.kruskal(*groups.values())
    return dict(medians={g: np.median(v) for g, v in groups.items()}, H=r.statistic, p=r.pvalue)


# --------------------------------------------------------- power / n
def n_for_mean(delta, sigma, alpha=0.05, power=0.80, two_sided=True):
    """Normal-approximation sample size for a one-sample (or paired) t-test, then
    iterate on the noncentral t to get the exact n."""
    za = stats.norm.ppf(1 - alpha / (2 if two_sided else 1))
    zb = stats.norm.ppf(power)
    n = max(2, math.ceil(((za + zb) * sigma / delta) ** 2))
    while power_one_mean(n, delta, sigma, alpha) < power:
        n += 1
    return n


def power_one_mean(n, delta, sigma, alpha=0.05):
    df = n - 1
    tc = stats.t.ppf(1 - alpha / 2, df)
    nc = delta / (sigma / math.sqrt(n))
    return stats.nct.sf(tc, df, nc) + stats.nct.cdf(-tc, df, nc)


def n_per_group_two_means(delta, sigma, alpha=0.05, power=0.80):
    n = 2
    while True:
        df = 2 * n - 2
        tc = stats.t.ppf(1 - alpha / 2, df)
        nc = delta / (sigma * math.sqrt(2 / n))
        if stats.nct.sf(tc, df, nc) + stats.nct.cdf(-tc, df, nc) >= power:
            return n
        n += 1


# ---------------------------------------------------------- examples
def examples():
    out = {}
    od = col(load("bearing_od.csv"), "od_mm")
    out["one-mean"] = ("Bearing OD vs nominal 25.000 mm", "mu = 25.000", "mu != 25.000", one_mean(od, 25.000))

    h = load("supplier_hardness.csv")
    A, B = col(h, "hrc", lambda r: r["supplier"] == "A"), col(h, "hrc", lambda r: r["supplier"] == "B")
    out["two-means"] = ("Hardness supplier A vs B (Welch t)", "muA = muB", "muA != muB", two_means(A, B))

    g = load("gauge_paired.csv")
    out["paired"] = ("New vs old gauge, same parts (paired t)", "mean difference = 0", "mean difference != 0",
                     paired(col(g, "old_mm"), col(g, "new_mm")))

    c = load("coating_thickness.csv")
    lines = {L: col(c, "um", lambda r, L=L: r["line"] == L) for L in ("L1", "L2", "L3")}
    out["anova"] = ("Coating thickness, 3 lines (one-way ANOVA)", "all line means equal",
                    "at least one differs", anova(lines))

    out["one-prop"] = ("Incoming defect rate vs claimed 3%", "p <= 0.03", "p > 0.03", one_prop(21, 400, 0.03))
    out["two-prop"] = ("Day vs night shift defect rate", "p_day = p_night", "p_day != p_night",
                       two_prop(17, 500, 35, 520))
    t = load("defects_by_machine.csv")
    tab = [[int(r[k]) for k in ("burr", "scratch", "dimension", "other")] for r in t]
    out["chi-square"] = ("Defect type vs machine (chi-square)", "type and machine independent",
                         "not independent", chi_square(tab))

    tq = col(load("torque.csv"), "nm")
    out["one-var"] = ("Torque sigma vs requirement 0.50", "sigma <= 0.50", "sigma > 0.50", one_var(tq, 0.50))

    sw = load("saw_length.csv")
    o, n = col(sw, "mm", lambda r: r["saw"] == "old"), col(sw, "mm", lambda r: r["saw"] == "new")
    out["two-var"] = ("Old vs new saw variation (F and Levene)", "sigma_old = sigma_new",
                      "sigma_old != sigma_new", two_var(o, n))

    rt = load("repair_turnaround.csv")
    bf, af = col(rt, "hours", lambda r: r["period"] == "before"), col(rt, "hours", lambda r: r["period"] == "after")
    out["mann-whitney"] = ("Repair turnaround before vs after (Mann-Whitney)", "same distribution",
                           "one tends to be larger", mann_whitney(bf, af))
    out["welch-on-skewed"] = ("Same data, Welch t for comparison", "muB = muA", "muB != muA", two_means(bf, af))

    ds = load("discomfort_scores.csv")
    pre, post = col(ds, "before"), col(ds, "after")
    out["wilcoxon"] = ("Discomfort before vs after (Wilcoxon signed-rank)", "median difference = 0",
                       "median difference != 0", wilcoxon_paired(pre, post))
    out["sign"] = ("Same data, sign test", "P(+) = P(-)", "P(+) != P(-)", sign_test(pre, post))
    out["kruskal"] = ("Coating thickness, 3 lines (Kruskal-Wallis)", "same distribution",
                      "at least one differs", kruskal(lines))
    return out


def fmt(v):
    if isinstance(v, float) or isinstance(v, np.floating):
        return f"{v:.4g}"
    if isinstance(v, tuple):
        return "(" + ", ".join(fmt(x) for x in v) + ")"
    if isinstance(v, dict):
        return "{" + ", ".join(f"{k}: {fmt(x)}" for k, x in v.items()) + "}"
    if isinstance(v, np.ndarray):
        return np.array2string(v, precision=2)
    return str(v)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    ex = examples()
    for name, (title, h0, ha, res) in ex.items():
        if which in ("all", name):
            banner(f"[{name}] {title}", h0, ha)
            for k, v in res.items():
                print(f"  {k:10s} {fmt(v)}")
            if "p" in res:
                print("  ->", verdict(res["p"]))
