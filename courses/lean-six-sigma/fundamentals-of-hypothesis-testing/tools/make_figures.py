"""Draw every figure used in modules/ into figures/.

    python tools/make_figures.py

License: MIT
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import htest as h  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY = "#1f4e79", "#c00000", "#7f7f7f"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# 1. Rejection region for the one-sample t example (df = 19)
x = np.linspace(-6, 6, 600)
tc = stats.t.ppf(0.975, 19)
plt.figure(figsize=(7, 3))
plt.plot(x, stats.t.pdf(x, 19), color=BLUE)
for side in (x > tc, x < -tc):
    plt.fill_between(x[side], stats.t.pdf(x[side], 19), color=RED, alpha=0.4)
plt.axvline(5.309, color="k", ls="--")
plt.text(5.35, 0.3, "observed t = 5.31", rotation=90, va="top")
plt.title(f"t distribution, df = 19: reject H0 if |t| > {tc:.3f} (alpha = 0.05)")
plt.yticks([])
save("t_rejection_region.png")

# 2. Power curves for a one-sample t-test
plt.figure(figsize=(7, 3.4))
ns = np.arange(3, 61)
for d, c in ((0.25, GRAY), (0.5, BLUE), (1.0, RED)):
    plt.plot(ns, [h.power_one_mean(n, d, 1.0) for n in ns], color=c, label=f"shift = {d} sigma")
plt.axhline(0.8, color="k", lw=0.8, ls=":")
plt.xlabel("Sample size n")
plt.ylabel("Power")
plt.title("Power of a two-sided one-sample t-test (alpha = 0.05)")
plt.legend()
save("power_curves.png")

# 3. Treatment comparison on a process behavior chart
s = h.load("daily_scrap.csv")
y = h.col(s, "scrap_pct")
b = y[:20]
mr = np.abs(np.diff(b)).mean()
cl, u, l = b.mean(), b.mean() + 2.66 * mr, b.mean() - 2.66 * mr
plt.figure(figsize=(8, 3.2))
plt.plot(range(1, 36), y, "o-", color=BLUE)
for v, ls in ((cl, "-"), (u, "--"), (l, "--")):
    plt.hlines(v, 1, 35, colors="k" if ls == "-" else RED, linestyles=ls, lw=1)
plt.axvline(20.5, color=GRAY, ls=":")
plt.text(21, u, "change made", color=GRAY, va="top")
plt.title("Daily scrap %: limits from days 1-20, extended")
plt.xlabel("Day")
plt.ylabel("Scrap %")
save("scrap_before_after.png")

# 4. Skewed data: repair turnaround
rt = h.load("repair_turnaround.csv")
bf = h.col(rt, "hours", lambda r: r["period"] == "before")
af = h.col(rt, "hours", lambda r: r["period"] == "after")
plt.figure(figsize=(7, 3))
plt.boxplot([bf, af], vert=False)
plt.yticks([1, 2], ["before", "after"])
plt.xlabel("Hours")
plt.title("Repair turnaround (right-skewed)")
save("repair_boxplot.png")

# 5. Coating thickness by line
c = h.load("coating_thickness.csv")
groups = [h.col(c, "um", lambda r, L=L: r["line"] == L) for L in ("L1", "L2", "L3")]
plt.figure(figsize=(6, 3))
for i, g in enumerate(groups, 1):
    plt.plot(np.full(len(g), i) + np.linspace(-0.08, 0.08, len(g)), g, "o", color=BLUE, alpha=0.7)
    plt.hlines(g.mean(), i - 0.25, i + 0.25, color=RED)
plt.xticks([1, 2, 3], ["L1", "L2", "L3"])
plt.ylabel("um")
plt.title("Coating thickness by line (red = mean)")
save("coating_by_line.png")

print("figures written to", os.path.abspath(FIG))
