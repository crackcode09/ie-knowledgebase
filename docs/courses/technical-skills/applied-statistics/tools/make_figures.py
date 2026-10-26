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
import statkit as st  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


ct = st.col(st.load("cycle_time.csv"), "seconds")
rt = st.col(st.load("rework_time.csv"), "minutes")
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
ax[0].hist(ct, bins=15, color=LIGHT, edgecolor="k")
ax[0].axvline(ct.mean(), color=RED, label="mean")
ax[0].axvline(np.median(ct), color=BLUE, ls="--", label="median")
ax[0].set_title("Reflow cycle time (s): symmetric")
ax[0].legend(fontsize=8)
ax[1].hist(rt, bins=15, color=LIGHT, edgecolor="k")
ax[1].axvline(rt.mean(), color=RED, label="mean")
ax[1].axvline(np.median(rt), color=BLUE, ls="--", label="median")
ax[1].set_title("Rework time (min): right-skewed")
ax[1].legend(fontsize=8)
save("histograms.png")

# Discrete distributions
fig, ax = plt.subplots(1, 2, figsize=(9, 3))
k = np.arange(0, 7)
ax[0].bar(k, stats.binom.pmf(k, 25, 0.04), color=BLUE)
ax[0].set_title("Binomial: failures in 25 boards (p = 0.04)")
ax[0].set_xlabel("failures")
d = st.col(st.load("defects_per_board.csv"), "defects")
obs = [int((d == i).sum()) for i in range(6)]
ax[1].bar(np.arange(6) - 0.2, obs, 0.4, color=LIGHT, edgecolor="k", label="observed")
ax[1].bar(np.arange(6) + 0.2, 200 * stats.poisson.pmf(np.arange(6), d.mean()), 0.4, color=RED, label="Poisson")
ax[1].set_title("Defects per board (200 boards)")
ax[1].set_xlabel("defects")
ax[1].legend(fontsize=8)
save("discrete.png")

# OC curve
K = np.arange(0, 51)
plt.figure(figsize=(6.5, 3))
for n, c, col in ((50, 1, BLUE), (80, 1, RED), (50, 0, GRAY)):
    plt.plot(K / 500 * 100, stats.hypergeom.cdf(c, 500, K, n), color=col, label=f"n = {n}, accept if ≤ {c}")
plt.xlabel("% defective in lot of 500")
plt.ylabel("P(accept)")
plt.title("Operating characteristic curves (hypergeometric)")
plt.legend(fontsize=8)
save("oc_curve.png")

# CLT
rng = np.random.default_rng(4)
fig, ax = plt.subplots(1, 3, figsize=(10, 2.8), sharey=False)
for a, n in zip(ax, (1, 5, 30)):
    m = [rng.choice(rt, n).mean() for _ in range(5000)]
    a.hist(m, bins=40, color=LIGHT, edgecolor="none")
    a.set_title(f"means of n = {n}")
    a.set_yticks([])
fig.suptitle("Central limit theorem: means of skewed rework times")
save("clt.png")

# Regression with prediction band
b = st.load("monthly_business.csv")
x, y = st.col(b, "orders"), st.col(b, "revenue_k")
res = stats.linregress(x, y)
n = len(x)
s = math.sqrt(((y - (res.intercept + res.slope * x)) ** 2).sum() / (n - 2))
xx = np.linspace(x.min() - 20, x.max() + 20, 100)
se = s * np.sqrt(1 + 1 / n + (xx - x.mean()) ** 2 / ((x - x.mean()) ** 2).sum())
t = stats.t.ppf(0.975, n - 2)
plt.figure(figsize=(6.5, 3.4))
plt.plot(x, y, "o", color=BLUE)
plt.plot(xx, res.intercept + res.slope * xx, color=RED, label="fit")
plt.fill_between(xx, res.intercept + res.slope * xx - t * se, res.intercept + res.slope * xx + t * se,
                 color=RED, alpha=0.12, label="95% prediction interval")
plt.xlabel("Orders per month")
plt.ylabel("Revenue (k$)")
plt.title(f"Revenue vs orders (R² = {res.rvalue**2:.2f})")
plt.legend(fontsize=8)
save("regression.png")

print("figures written to", os.path.abspath(FIG))
