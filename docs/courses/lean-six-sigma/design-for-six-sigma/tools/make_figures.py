"""Draw every figure used in modules/ into figures/.

    python tools/make_figures.py

License: MIT
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import dfss  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# Tolerance stack-up
r = dfss.stackup([30.00, 15.00, 12.00, 2.70], [0.10, 0.06, 0.05, 0.04], [1, -1, -1, -1])
plt.figure(figsize=(7, 3.2))
plt.hist(r["sims"], bins=80, color=LIGHT, edgecolor="none", density=True)
for x in r["worst_case"]:
    plt.axvline(x, color=RED, ls="--")
for x in r["rss"]:
    plt.axvline(x, color=BLUE, ls=":")
plt.text(r["worst_case"][0], plt.ylim()[1] * 0.9, " worst case", color=RED)
plt.text(r["rss"][0], plt.ylim()[1] * 0.75, " RSS", color=BLUE)
plt.title("Gap: 200,000 Monte Carlo assemblies")
plt.xlabel("Gap (mm)")
plt.yticks([])
save("stackup.png")

# DOE main effects
X, mean, eff = dfss.doe_2k(dfss.DOE_Y)
y = np.array(dfss.DOE_Y)
fig, ax = plt.subplots(1, 3, figsize=(8, 2.8), sharey=True)
for i, (name, lab) in enumerate((("A", "Preload"), ("B", "Lube viscosity"), ("C", "Seal type"))):
    lo, hi = y[X[:, i] < 0].mean(), y[X[:, i] > 0].mean()
    ax[i].plot([-1, 1], [lo, hi], "o-", color=BLUE)
    ax[i].axhline(mean, color=GRAY, lw=0.8, ls=":")
    ax[i].set_xticks([-1, 1])
    ax[i].set_xticklabels(["low", "high"])
    ax[i].set_title(f"{name}: {lab}")
ax[0].set_ylabel("Friction (N)")
save("doe_main_effects.png")

# Queue wait vs utilization
u = np.linspace(0.3, 0.97, 200)
plt.figure(figsize=(7, 3.2))
for ce, c in ((0.5, BLUE), (1.0, GRAY), (1.5, RED)):
    te = 8.0
    w = (1 + ce ** 2) / 2 * (u / (1 - u)) * te
    plt.plot(u, w, color=c, label=f"service cv = {ce}")
plt.ylim(0, 200)
plt.xlabel("Utilization")
plt.ylabel("Mean wait (min)")
plt.title("Kingman approximation: wait explodes near 100% utilization (te = 8 min, ca = 1)")
plt.legend()
save("queue_wait.png")

# Weibull probability plot
rel = dfss.ex_reliability()
f = np.array(rel["failures (km)"])
n = len(f)
F = (np.arange(1, n + 1) - 0.3) / (n + 0.4)  # Bernard's median rank
plt.figure(figsize=(6, 3.4))
plt.plot(np.log(f), np.log(-np.log(1 - F)), "o", color=BLUE, label="failures (median ranks)")
xx = np.linspace(np.log(f.min() * 0.8), np.log(f.max() * 1.2), 50)
k, lam = rel["shape beta"], rel["scale eta"]
plt.plot(xx, k * (xx - math.log(lam)), color=RED, label=f"fit: beta {k:.2f}, eta {lam:.0f}")
plt.xlabel("ln(km)")
plt.ylabel("ln(-ln(1-F))")
plt.title("Weibull plot: 12 carriage wear-out failures")
plt.legend()
save("weibull.png")

print("figures written to", os.path.abspath(FIG))
