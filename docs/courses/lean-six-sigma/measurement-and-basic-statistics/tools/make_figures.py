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
import describe as d  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
FIG = os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6"


def data(name):
    return d.load(os.path.join(ROOT, "data", name))


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


def pareto_plot(rows, title, ylabel, fname):
    cats = [r[0] for r in rows]
    vals = [r[1] for r in rows]
    cum = [r[3] for r in rows]
    fig, ax = plt.subplots(figsize=(8, 3.8))
    ax.bar(range(len(cats)), vals, color=LIGHT, edgecolor="k")
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, rotation=35, ha="right", fontsize=8)
    ax.set_ylabel(ylabel)
    ax2 = ax.twinx()
    ax2.plot(range(len(cats)), cum, "o-", color=RED)
    ax2.set_ylim(0, 105)
    ax2.axhline(80, color=GRAY, ls=":", lw=1)
    ax2.set_ylabel("Cumulative %")
    ax.set_title(title)
    save(fname)


c = data("complaints.csv")
cats = [r["category"] for r in c]
pareto_plot(d.pareto(cats), "Complaints by category (count)", "Complaints", "pareto_count.png")
pareto_plot(d.pareto(cats, [float(r["cost_usd"]) for r in c]), "Complaints by category (cost)", "USD",
            "pareto_cost.png")

# Histograms
x = np.array([float(r["mm"]) for r in data("shaft_diameter.csv")])
plt.figure(figsize=(6.5, 3.2))
plt.hist(x, bins=np.arange(12.665, 12.736, 0.005), color=LIGHT, edgecolor="k")
plt.axvline(x.mean(), color=RED, label=f"mean {x.mean():.4f}")
plt.legend()
plt.title("Shaft diameter, 100 parts")
plt.xlabel("mm")
save("hist_shaft.png")

lt = np.array([float(r["days"]) for r in data("lead_time.csv")])
plt.figure(figsize=(6.5, 3.2))
plt.hist(lt, bins=np.arange(0, 17, 1), color=LIGHT, edgecolor="k")
plt.axvline(lt.mean(), color=RED, label=f"mean {lt.mean():.2f}")
plt.axvline(np.median(lt), color=BLUE, ls="--", label=f"median {np.median(lt):.2f}")
plt.legend()
plt.title("Order lead time, 60 orders (right-skewed)")
plt.xlabel("days")
save("hist_lead_time.png")

fw = data("fill_weight.csv")
g = np.array([float(r["g"]) for r in fw])
plt.figure(figsize=(6.5, 3.2))
plt.hist(g, bins=np.arange(494, 507, 1), color=LIGHT, edgecolor="k")
plt.axvline(g.mean(), color=RED, label=f"mean {g.mean():.1f}")
plt.legend()
plt.title("Fill weight, two heads mixed (bimodal)")
plt.xlabel("g")
save("hist_fill_bimodal.png")

# Same mean, different spread
s = data("supplier_thickness.csv")
fig, ax = plt.subplots(figsize=(7, 2.8))
for i, sup in enumerate(("A", "B")):
    v = [float(r["mm"]) for r in s if r["supplier"] == sup]
    ax.plot(v, np.full(len(v), i) + np.linspace(-0.12, 0.12, len(v)), "o", color=BLUE, alpha=0.7)
for lim in (9.70, 10.30):
    ax.axvline(lim, color=RED, ls="--")
ax.axvline(10.0, color="k", lw=0.8)
ax.set_yticks([0, 1])
ax.set_yticklabels(["Supplier A", "Supplier B"])
ax.set_xlabel("mm (spec 10.00 +/- 0.30)")
ax.set_title("Same average (10.00 mm), different variation")
save("same_mean_different_spread.png")

# Accuracy vs precision
gr = data("gauge_reference.csv")
fig, ax = plt.subplots(figsize=(7, 3))
labels = {"G1": "G1 accurate + precise", "G2": "G2 accurate, imprecise",
          "G3": "G3 precise, biased", "G4": "G4 biased + less precise"}
for i, k in enumerate(labels):
    v = [float(r["mm"]) for r in gr if r["gauge"] == k]
    ax.plot(v, np.full(len(v), i), "o", color=BLUE, alpha=0.6)
ax.axvline(25.000, color=RED, label="true value 25.000")
ax.set_yticks(range(4))
ax.set_yticklabels(labels.values())
ax.legend(loc="lower right", fontsize=8)
ax.set_xlabel("mm")
ax.set_title("Four gauges, 10 readings each of a 25.000 mm reference block")
save("accuracy_precision.png")

# Normal curve
z = np.linspace(-4, 4, 400)
plt.figure(figsize=(7, 3))
plt.plot(z, stats.norm.pdf(z), color=BLUE)
for k, a in ((3, 0.15), (2, 0.25), (1, 0.4)):
    m = (z >= -k) & (z <= k)
    plt.fill_between(z[m], stats.norm.pdf(z[m]), color=BLUE, alpha=a)
for k, p in ((1, "68.3%"), (2, "95.4%"), (3, "99.73%")):
    plt.text(0, stats.norm.pdf(k) * 0.4 + 0.02 * (4 - k), p, ha="center")
plt.xticks(range(-3, 4), ["-3σ", "-2σ", "-1σ", "μ", "+1σ", "+2σ", "+3σ"])
plt.yticks([])
plt.title("The normal distribution")
save("normal_curve.png")

print("figures written to", os.path.abspath(FIG))
