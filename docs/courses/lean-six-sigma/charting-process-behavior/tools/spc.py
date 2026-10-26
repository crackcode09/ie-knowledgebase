"""
spc.py - a small, dependency-light toolkit for process behavior charts.

Used by every module in the Open SPC Course. Requires numpy; plotting
functions also need matplotlib.

    python tools/spc.py xmr data/shaft_diameter.csv value
    python tools/spc.py xbar data/bore_subgroups.csv
    python tools/spc.py p data/daily_defectives.csv
    python tools/spc.py capability data/shaft_diameter.csv value 12.66 12.74 --first 20

License: MIT
"""
from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass, field

import numpy as np

# ---------------------------------------------------------------------------
# Bias-correction constants for subgroup ranges (n = 2..10).
# d2 = E[R]/sigma, d3 = SD[R]/sigma for samples from a normal distribution.
# A2 = 3/(d2*sqrt(n)), D3 = max(0, 1-3*d3/d2), D4 = 1+3*d3/d2.
# tests/check_constants.py recomputes d2 and d3 by numerical integration.
# ---------------------------------------------------------------------------
D2 = {2: 1.128, 3: 1.693, 4: 2.059, 5: 2.326, 6: 2.534, 7: 2.704, 8: 2.847, 9: 2.970, 10: 3.078}
D3_SD = {2: 0.853, 3: 0.888, 4: 0.880, 5: 0.864, 6: 0.848, 7: 0.833, 8: 0.820, 9: 0.808, 10: 0.797}
A2 = {2: 1.880, 3: 1.023, 4: 0.729, 5: 0.577, 6: 0.483, 7: 0.419, 8: 0.373, 9: 0.337, 10: 0.308}
D3 = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0.076, 8: 0.136, 9: 0.184, 10: 0.223}
D4 = {2: 3.267, 3: 2.574, 4: 2.282, 5: 2.114, 6: 2.004, 7: 1.924, 8: 1.864, 9: 1.816, 10: 1.777}


@dataclass
class Limits:
    center: float
    lower: float | np.ndarray
    upper: float | np.ndarray
    sigma: float | np.ndarray  # one-sigma width used for zone rules
    extra: dict = field(default_factory=dict)


# ----------------------------- variables charts ---------------------------
def moving_ranges(x):
    x = np.asarray(x, dtype=float)
    return np.abs(np.diff(x))


def xmr_limits(x):
    """Individuals (X) and moving range (mR) limits, Wheeler-style.

    Natural process limits: mean +/- 2.66 * mean(mR)   (2.66 = 3 / 1.128)
    Upper range limit:      3.268 * mean(mR)          (3.268 = D4 for n=2)
    """
    x = np.asarray(x, dtype=float)
    mr = moving_ranges(x)
    xbar, mrbar = x.mean(), mr.mean()
    sigma = mrbar / D2[2]
    x_lim = Limits(xbar, xbar - 3 * sigma, xbar + 3 * sigma, sigma)
    mr_lim = Limits(mrbar, 0.0, 3.268 * mrbar, None)
    return x_lim, mr_lim


def xbar_r_limits(subgroups):
    """subgroups: 2-D array (k subgroups x n)."""
    s = np.asarray(subgroups, dtype=float)
    n = s.shape[1]
    means, ranges = s.mean(axis=1), np.ptp(s, axis=1)
    grand, rbar = means.mean(), ranges.mean()
    sigma_x = rbar / D2[n]
    xl = Limits(grand, grand - A2[n] * rbar, grand + A2[n] * rbar, A2[n] * rbar / 3,
                extra={"means": means, "sigma_within": sigma_x})
    rl = Limits(rbar, D3[n] * rbar, D4[n] * rbar, None, extra={"ranges": ranges})
    return xl, rl


# ----------------------------- attribute charts ---------------------------
def p_limits(defectives, inspected):
    d, n = np.asarray(defectives, float), np.asarray(inspected, float)
    pbar = d.sum() / n.sum()
    sig = np.sqrt(pbar * (1 - pbar) / n)
    return Limits(pbar, np.clip(pbar - 3 * sig, 0, None), pbar + 3 * sig, sig,
                  extra={"p": d / n})


def np_limits(defectives, n):
    d = np.asarray(defectives, float)
    npbar = d.mean()
    pbar = npbar / n
    sig = math.sqrt(npbar * (1 - pbar))
    return Limits(npbar, max(0.0, npbar - 3 * sig), npbar + 3 * sig, sig)


def c_limits(counts):
    c = np.asarray(counts, float)
    cbar = c.mean()
    sig = math.sqrt(cbar)
    return Limits(cbar, max(0.0, cbar - 3 * sig), cbar + 3 * sig, sig)


def u_limits(counts, area):
    c, a = np.asarray(counts, float), np.asarray(area, float)
    ubar = c.sum() / a.sum()
    sig = np.sqrt(ubar / a)
    return Limits(ubar, np.clip(ubar - 3 * sig, 0, None), ubar + 3 * sig, sig,
                  extra={"u": c / a})


# ----------------------------- detection rules ----------------------------
def detect(x, lim: Limits):
    """Western Electric zone tests. Returns {rule: [indices that complete a signal]}.

    Rule 1: one point beyond a 3-sigma limit
    Rule 2: 2 of 3 successive points beyond 2 sigma, same side
    Rule 3: 4 of 5 successive points beyond 1 sigma, same side
    Rule 4: 8 successive points on the same side of the center line
    """
    x = np.asarray(x, float)
    z = (x - lim.center) / lim.sigma
    out = {1: [], 2: [], 3: [], 4: []}
    for i in range(len(x)):
        if abs(z[i]) > 3:
            out[1].append(i)
        for rule, win, need, thr in ((2, 3, 2, 2), (3, 5, 4, 1)):
            if i >= win - 1:
                w = z[i - win + 1:i + 1]
                for side in (1, -1):
                    if np.sum(side * w > thr) >= need and side * z[i] > thr:
                        out[rule].append(i)
        if i >= 7:
            w = z[i - 7:i + 1]
            if np.all(w > 0) or np.all(w < 0):
                out[4].append(i)
    return {k: sorted(set(v)) for k, v in out.items()}


# ----------------------------- capability ---------------------------------
def capability(x, lsl=None, usl=None, sigma_within=None):
    """Cp/Cpk use within-subgroup sigma (default: mR-bar/1.128).
    Pp/Ppk use the overall sample standard deviation."""
    x = np.asarray(x, float)
    mu = x.mean()
    sw = sigma_within if sigma_within is not None else moving_ranges(x).mean() / D2[2]
    so = x.std(ddof=1)
    res = {"mean": mu, "sigma_within": sw, "sigma_overall": so}
    for tag, s in (("C", sw), ("P", so)):
        if lsl is not None and usl is not None:
            res[f"{tag}p"] = (usl - lsl) / (6 * s)
        sides = []
        if usl is not None:
            sides.append((usl - mu) / (3 * s))
        if lsl is not None:
            sides.append((mu - lsl) / (3 * s))
        res[f"{tag}pk"] = min(sides)
    return res


# ----------------------------- plotting -----------------------------------
def plot_chart(values, lim: Limits, title="", ylabel="", ax=None, signals=None):
    import matplotlib.pyplot as plt
    ax = ax or plt.gca()
    idx = np.arange(1, len(values) + 1)
    ax.plot(idx, values, marker="o", color="#1f4e79", lw=1)
    ax.axhline(lim.center, color="k", lw=1)
    for b in (lim.lower, lim.upper):
        if np.ndim(b) == 0:
            ax.axhline(b, color="#c00000", ls="--", lw=1)
        else:
            ax.step(idx, b, where="mid", color="#c00000", ls="--", lw=1)
    if signals:
        bad = sorted({i for v in signals.values() for i in v})
        ax.plot(idx[bad], np.asarray(values)[bad], "o", color="#c00000", ms=9, mfc="none")
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel("Observation")
    return ax


# ----------------------------- CLI ----------------------------------------
def _read(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chart", choices=["xmr", "xbar", "p", "c", "u", "capability"])
    ap.add_argument("csv")
    ap.add_argument("column", nargs="?", default="value")
    ap.add_argument("lsl", nargs="?", type=float)
    ap.add_argument("usl", nargs="?", type=float)
    ap.add_argument("--first", type=int, help="use only the first N rows (drop the rest)")
    ap.add_argument("--baseline", type=int,
                    help="xmr: compute limits from the first N rows, then test ALL rows against them")
    a = ap.parse_args()
    rows = _read(a.csv)
    if a.first:
        rows = rows[: a.first]
    f = lambda k: np.array([float(r[k]) for r in rows])
    if a.chart == "xmr":
        x = f(a.column)
        xl, ml = xmr_limits(x[: a.baseline] if a.baseline else x)
        print(f"X:  CL={xl.center:.4f}  LNPL={xl.lower:.4f}  UNPL={xl.upper:.4f}  sigma={xl.sigma:.4f}")
        print(f"mR: CL={ml.center:.4f}  URL={ml.upper:.4f}")
        sig = {k: [i + 1 for i in v] for k, v in detect(x, xl).items()}
        print("signals by rule (1-based points):", sig)
        print("mR above URL at points:", [i + 2 for i, m in enumerate(moving_ranges(x)) if m > ml.upper])
    elif a.chart == "xbar":
        cols = [k for k in rows[0] if k.startswith("x")]
        s = np.array([[float(r[c]) for c in cols] for r in rows])
        xl, rl = xbar_r_limits(s)
        print(f"Xbar: CL={xl.center:.4f}  LCL={xl.lower:.4f}  UCL={xl.upper:.4f}")
        print(f"R:    CL={rl.center:.4f}  LCL={rl.lower:.4f}  UCL={rl.upper:.4f}")
        print("Xbar signals (1-based):", {k: [i + 1 for i in v] for k, v in detect(xl.extra["means"], xl).items()})
        print("R beyond UCL (subgroup #):", [int(i) + 1 for i in np.where(rl.extra["ranges"] > rl.upper)[0]])
    elif a.chart == "p":
        lim = p_limits(f("defective"), f("inspected"))
        print(f"p-bar={lim.center:.4f}")
        for i, (p, lo, hi) in enumerate(zip(lim.extra["p"], lim.lower, lim.upper), 1):
            flag = "  <-- signal" if p > hi or p < lo else ""
            print(f"{i:3d} p={p:.4f}  LCL={lo:.4f}  UCL={hi:.4f}{flag}")
    elif a.chart == "c":
        c = f("defects")
        lim = c_limits(c)
        print(f"c-bar={lim.center:.3f} LCL={lim.lower:.3f} UCL={lim.upper:.3f}")
        print("signals (1-based):", {k: [i + 1 for i in v] for k, v in detect(c, lim).items()})
    elif a.chart == "u":
        lim = u_limits(f("defects"), f("area_m2"))
        print(f"u-bar={lim.center:.4f}")
        for i, (u, hi) in enumerate(zip(lim.extra["u"], lim.upper), 1):
            print(f"{i:3d} u={u:.3f} UCL={hi:.3f}{'  <-- signal' if u > hi else ''}")
    elif a.chart == "capability":
        for k, v in capability(f(a.column), a.lsl, a.usl).items():
            print(f"{k:14s} {v:.4f}")


if __name__ == "__main__":
    main()
