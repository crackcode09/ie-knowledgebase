"""describe.py - descriptive statistics and Pareto tables for the course.

    python tools/describe.py summary data/shaft_diameter.csv mm
    python tools/describe.py pareto  data/complaints.csv category
    python tools/describe.py pareto  data/complaints.csv category --weight cost_usd
    python tools/describe.py zscore  12.725 12.702 0.010

License: MIT
"""
from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict

import numpy as np
from scipy import stats


def load(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def summary(x):
    x = np.asarray(x, float)
    q1, med, q3 = np.percentile(x, [25, 50, 75])
    mode = Counter(np.round(x, 6)).most_common(1)[0]
    return {
        "n": len(x), "mean": x.mean(), "median": med,
        "mode": mode[0] if mode[1] > 1 else None,
        "trimmed_mean_10pct": stats.trim_mean(x, 0.10),
        "min": x.min(), "max": x.max(), "range": np.ptp(x),
        "variance": x.var(ddof=1), "std_dev": x.std(ddof=1),
        "Q1": q1, "Q3": q3, "IQR": q3 - q1,
        "cv_pct": 100 * x.std(ddof=1) / x.mean(),
        "skewness": stats.skew(x),
    }


def pareto(categories, weights=None):
    tot = defaultdict(float)
    for i, c in enumerate(categories):
        tot[c] += 1 if weights is None else weights[i]
    items = sorted(tot.items(), key=lambda kv: kv[1], reverse=True)
    grand = sum(v for _, v in items)
    cum, out = 0.0, []
    for c, v in items:
        cum += v
        out.append((c, v, 100 * v / grand, 100 * cum / grand))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["summary", "pareto", "zscore"])
    ap.add_argument("args", nargs="*")
    ap.add_argument("--weight")
    ap.add_argument("--by", help="summary: group by this column")
    a = ap.parse_args()
    if a.cmd == "summary":
        rows = load(a.args[0])
        groups = {"all": rows} if not a.by else {
            g: [r for r in rows if r[a.by] == g] for g in dict.fromkeys(r[a.by] for r in rows)}
        for g, rs in groups.items():
            print(f"--- {g}")
            for k, v in summary([float(r[a.args[1]]) for r in rs]).items():
                print(f"  {k:20s} {v if v is None or isinstance(v, int) else round(float(v), 5)}")
    elif a.cmd == "pareto":
        rows = load(a.args[0])
        w = [float(r[a.weight]) for r in rows] if a.weight else None
        print(f"{'category':30s} {'value':>10s} {'%':>7s} {'cum %':>7s}")
        for c, v, p, cp in pareto([r[a.args[1]] for r in rows], w):
            print(f"{c:30s} {v:10.0f} {p:7.1f} {cp:7.1f}")
    else:
        x, mu, sd = map(float, a.args)
        z = (x - mu) / sd
        print(f"z = {z:.3f}; P(X > x) = {stats.norm.sf(z):.5f}; P(X < x) = {stats.norm.cdf(z):.5f}")


if __name__ == "__main__":
    main()
