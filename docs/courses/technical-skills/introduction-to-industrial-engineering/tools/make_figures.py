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
import ie  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# Time study: element observations with the abnormal reading
fig, ax = plt.subplots(figsize=(7, 3.2))
for i, (name, obs) in enumerate(ie.ELEMENTS.items()):
    ax.plot(range(1, 11), obs, "o-", label=name)
ax.annotate("dropped part (irregular)", (7, 35.0), xytext=(8, 31), arrowprops=dict(arrowstyle="->"), fontsize=8)
ax.set_xlabel("Cycle")
ax.set_ylabel("Seconds")
ax.set_title("Time study: 10 cycles of packing a service kit")
ax.legend(fontsize=7, ncol=2)
save("time_study.png")

# Learning curve
n = np.arange(1, 129)
plt.figure(figsize=(6.5, 3.2))
for r, c in ((0.80, RED), (0.85, BLUE), (0.90, GRAY)):
    plt.plot(n, [ie.learning_curve(4.0, r, k) for k in n], color=c, label=f"{int(r*100)}% curve")
plt.xlabel("Unit number")
plt.ylabel("Minutes per unit")
plt.title("Learning curves (first unit 4.0 min)")
plt.legend()
save("learning_curve.png")

# Wage line
pts = ie.job_points()
x = np.array([pts[j] for j in ie.JOBS])
y = np.array([p for _, p in ie.JOBS.values()])
res = stats.linregress(x, y)
plt.figure(figsize=(6.8, 3.6))
plt.plot(x, y, "o", color=BLUE)
for j in ie.JOBS:
    plt.annotate(j, (pts[j], ie.JOBS[j][1]), textcoords="offset points", xytext=(4, 4), fontsize=7)
xx = np.linspace(200, 430, 10)
plt.plot(xx, res.intercept + res.slope * xx, color=RED, label="wage line")
plt.plot(xx, (res.intercept + res.slope * xx) * 1.05, color=GRAY, ls=":", label="±5% band")
plt.plot(xx, (res.intercept + res.slope * xx) * 0.95, color=GRAY, ls=":")
plt.xlabel("Job evaluation points")
plt.ylabel("Hourly pay (USD)")
plt.title("Wage line from job evaluation")
plt.legend(fontsize=8)
save("wage_line.png")

# Layout before/after
def draw(ax, lay, title):
    for d, (gx, gy) in lay.items():
        ax.add_patch(plt.Rectangle((gx, 1 - gy), 0.9, 0.9, color=LIGHT, ec="k"))
        ax.text(gx + 0.45, 1 - gy + 0.45, d, ha="center", va="center", fontsize=8)
    ft = ie.FROM_TO
    for i in range(6):
        for j in range(i + 1, 6):
            if ft[i, j] >= 50:
                (x1, y1), (x2, y2) = lay[ie.DEPTS[i]], lay[ie.DEPTS[j]]
                ax.plot([x1 + 0.45, x2 + 0.45], [1 - y1 + 0.45, 1 - y2 + 0.45], color=RED, lw=ft[i, j] / 30, alpha=0.6)
    ax.set_xlim(-0.1, 3)
    ax.set_ylim(-0.1, 2)
    ax.axis("off")
    ax.set_title(title, fontsize=9)


b, lay = ie.best_layout()
fig, ax = plt.subplots(1, 2, figsize=(9, 3.2))
draw(ax[0], ie.LAYOUT_A, f"Layout A: {ie.load_distance(ie.LAYOUT_A):,.0f} trip-m/day")
draw(ax[1], lay, f"Best layout: {b:,.0f} trip-m/day")
save("layout.png")

print("figures written to", os.path.abspath(FIG))
