"""Draw every figure used in modules/ into figures/.

    python tools/make_figures.py

License: MIT
"""
import csv
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

sys.path.insert(0, os.path.dirname(__file__))
import funnel  # noqa: E402
import spc  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
FIG = os.path.join(ROOT, "figures")
os.makedirs(FIG, exist_ok=True)


def col(name, key):
    with open(os.path.join(ROOT, "data", name)) as f:
        return [r[key] for r in csv.DictReader(f)]


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# Run chart - cycle time
ct = np.array(col("cycle_time.csv", "days"), float)
med = np.median(ct[:25])
plt.figure(figsize=(8, 3.2))
plt.plot(range(1, 41), ct, "o-", color="#1f4e79")
plt.axhline(med, color="k", lw=1)
plt.axvline(25.5, color="gray", ls=":")
plt.text(26, ct.max(), "change made", color="gray", va="top")
plt.title(f"Run chart: order-to-ship cycle time (median of orders 1-25 = {med})")
plt.xlabel("Order")
plt.ylabel("Days")
save("run_chart_cycle_time.png")

# Histogram - shaft baseline
x = np.array(col("shaft_diameter.csv", "value"), float)
plt.figure(figsize=(6, 3.2))
plt.hist(x[:20], bins=np.arange(12.684, 12.716, 0.004), color="#9dc3e6", edgecolor="k")
plt.axvline(12.66, color="#c00000", ls="--")
plt.axvline(12.74, color="#c00000", ls="--")
plt.title("Shaft diameter, hours 1-20 (spec 12.66-12.74)")
plt.xlabel("mm")
save("hist_shaft.png")

# XmR - baseline and extended
xl, ml = spc.xmr_limits(x[:20])
fig, ax = plt.subplots(2, 1, figsize=(8, 5.5), sharex=True)
spc.plot_chart(x, xl, "X chart: shaft diameter (limits from hours 1-20)", "mm", ax[0], spc.detect(x, xl))
ax[0].axvline(20.5, color="gray", ls=":")
spc.plot_chart(np.r_[np.nan, spc.moving_ranges(x)], ml, "mR chart", "mm", ax[1])
save("xmr_shaft.png")

# Xbar-R
keys = ["x1", "x2", "x3", "x4", "x5"]
with open(os.path.join(ROOT, "data", "bore_subgroups.csv")) as f:
    s = np.array([[float(r[k]) for k in keys] for r in csv.DictReader(f)])
xb, rb = spc.xbar_r_limits(s)
fig, ax = plt.subplots(2, 1, figsize=(8, 5.5), sharex=True)
spc.plot_chart(xb.extra["means"], xb, "X-bar chart: bore diameter (n = 5)", "mm", ax[0])
spc.plot_chart(rb.extra["ranges"], rb, "R chart", "mm", ax[1])
save("xbar_r_bore.png")

# p chart
d = np.array(col("daily_defectives.csv", "defective"), float)
n = np.array(col("daily_defectives.csv", "inspected"), float)
pl = spc.p_limits(d, n)
plt.figure(figsize=(8, 3.2))
spc.plot_chart(pl.extra["p"], pl, "p chart: daily proportion defective", "proportion")
save("p_chart.png")

# c chart
c = np.array(col("panel_blemishes.csv", "defects"), float)
cl = spc.c_limits(c)
plt.figure(figsize=(8, 3.2))
spc.plot_chart(c, cl, "c chart: blemishes per panel", "count", signals=spc.detect(c, cl))
save("c_chart.png")

# Stratification
v = np.array(col("fill_weight.csv", "value"), float)
h = np.array(col("fill_weight.csv", "head"))
plt.figure(figsize=(8, 3.2))
for head, color in (("A", "#1f4e79"), ("B", "#ed7d31")):
    m = h == head
    plt.plot(np.where(m)[0] + 1, v[m], "o", color=color, label=f"Head {head}")
plt.plot(range(1, 41), v, color="gray", lw=0.6)
plt.legend()
plt.title("Fill weight, colored by filler head")
plt.ylabel("g")
save("stratified_fill.png")

# Funnel
fig, ax = plt.subplots(1, 4, figsize=(10, 2.8))
for i, r in enumerate((1, 2, 3, 4)):
    z = funnel.run(r, 200)
    ax[i].plot(z, lw=0.8)
    ax[i].set_title(f"Rule {r}")
save("funnel.png")

# Skewed data histogram
ra = np.array(col("roughness_ra.csv", "value"), float)
fig, ax = plt.subplots(1, 2, figsize=(8, 3))
ax[0].hist(ra, bins=15, color="#9dc3e6", edgecolor="k")
ax[0].axvline(1.6, color="#c00000", ls="--")
ax[0].set_title("Ra (um), raw")
ax[1].hist(np.log(ra), bins=15, color="#c5e0b4", edgecolor="k")
ax[1].axvline(np.log(1.6), color="#c00000", ls="--")
ax[1].set_title("ln(Ra)")
save("roughness_transform.png")

print("figures written to", os.path.abspath(FIG))
