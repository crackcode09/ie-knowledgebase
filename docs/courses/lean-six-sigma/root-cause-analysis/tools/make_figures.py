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
import rca  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


def pareto_plot(rows, title, ylabel, fname):
    cats, vals, cum = [r[0] for r in rows], [r[1] for r in rows], [r[3] for r in rows]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.bar(range(len(cats)), vals, color=LIGHT, edgecolor="k")
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=30, ha="right", fontsize=8)
    ax.set_ylabel(ylabel)
    ax2 = ax.twinx()
    ax2.plot(range(len(cats)), cum, "o-", color=RED)
    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Cumulative %")
    ax.set_title(title)
    save(fname)


p = rca.ex_pareto()
pareto_plot(p["by count"], "Scrap by defect (count, 8 weeks)", "Parts", "pareto_count.png")
pareto_plot(p["by cost"], "Scrap by defect (cost, 8 weeks)", "USD", "pareto_cost.png")

# Leak share by machine
s = rca.load("scrap_log.csv")
fig, ax = plt.subplots(figsize=(6, 3))
for i, m in enumerate(("MC1", "MC2", "MC3")):
    leak = sum(1 for r in s if r["machine"] == m and r["defect"] == "Leak at test")
    other = sum(1 for r in s if r["machine"] == m and r["defect"] != "Leak at test")
    ax.bar(i, leak, color=RED, label="Leak at test" if i == 0 else None)
    ax.bar(i, other, bottom=leak, color=LIGHT, edgecolor="k", label="Other defects" if i == 0 else None)
ax.set_xticks(range(3))
ax.set_xticklabels(["MC1", "MC2", "MC3"])
ax.set_ylabel("Scrapped parts")
ax.legend()
ax.set_title("Scrap stratified by machine")
save("stratify_machine.png")

# Scatter + regression
t = rca.load("tool_wear.csv")
x, y = rca.col(t, "hours_since_tool_change"), rca.col(t, "seat_ra_um")
res = stats.linregress(x, y)
plt.figure(figsize=(6.5, 3.4))
plt.plot(x, y, "o", color=BLUE)
xx = np.linspace(0, 40, 50)
plt.plot(xx, res.intercept + res.slope * xx, color=RED, label=f"Ra = {res.intercept:.3f} + {res.slope:.4f} x hours")
plt.axhline(0.80, color=GRAY, ls="--", label="Ra limit 0.80 um")
plt.xlabel("Spindle hours since tool change")
plt.ylabel("Seat Ra (um)")
plt.legend(fontsize=8)
plt.title(f"Tool wear vs seat roughness (r = {np.sqrt(res.rvalue**2):.2f})")
save("scatter_tool_wear.png")

# Logistic curve
lg = rca.ex_logistic()
b0, b1, b2 = lg["coef (const, Ra, torque)"]
d = rca.load("leak_test.csv")
ra, f = rca.col(d, "seat_ra_um"), rca.col(d, "fail")
plt.figure(figsize=(6.5, 3.4))
plt.plot(ra, f + np.random.default_rng(0).uniform(-0.03, 0.03, len(f)), "o", color=BLUE, alpha=0.4, ms=4)
rr = np.linspace(0.3, 1.3, 100)
for tq, c in ((19, RED), (22, "k"), (25, GRAY)):
    plt.plot(rr, 1 / (1 + np.exp(-(b0 + b1 * rr + b2 * tq))), color=c, label=f"torque {tq} N·m")
plt.xlabel("Seat Ra (um)")
plt.ylabel("P(leak test fail)")
plt.legend(fontsize=8)
plt.title("Logistic regression: probability of leak failure")
save("logistic_curve.png")

print("figures written to", os.path.abspath(FIG))
