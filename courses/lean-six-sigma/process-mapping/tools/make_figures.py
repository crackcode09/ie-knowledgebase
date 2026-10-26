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

sys.path.insert(0, os.path.dirname(__file__))
import pmap  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT, GREEN = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6", "#548235"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


def draw_path(ax, path, loc, title):
    for name, (x, y) in loc.items():
        ax.add_patch(plt.Rectangle((x - 5, y - 2.5), 10, 5, color=LIGHT, ec="k", zorder=3))
        ax.text(x, y, name, ha="center", va="center", fontsize=6, zorder=4)
    for i, (a, b) in enumerate(zip(path, path[1:])):
        (x1, y1), (x2, y2) = loc[a], loc[b]
        off = (i % 3 - 1) * 1.2
        ax.plot([x1 + off, x2 + off], [y1 + off, y1 + off], color=RED, lw=1.2)
        ax.plot([x2 + off, x2 + off], [y1 + off, y2 + off], color=RED, lw=1.2)
    ax.set_xlim(-10, 80)
    ax.set_ylim(-12, 80)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)


fig, ax = plt.subplots(1, 2, figsize=(10, 5))
draw_path(ax[0], pmap.PATH_BEFORE, pmap.LOC, f"Before: {pmap.path_length(pmap.PATH_BEFORE, pmap.LOC):.0f} m")
draw_path(ax[1], pmap.PATH_AFTER, pmap.LOC_AFTER,
          f"After: {pmap.path_length(pmap.PATH_AFTER, pmap.LOC_AFTER):.0f} m")
save("spaghetti.png")

# Time profile: waiting vs work
work, count, tw, wait, lead = pmap.va_analysis()
plt.figure(figsize=(7, 2.6))
parts = [("Waiting", wait, GRAY), ("NVA work", work["NVA"] / 60, RED), ("BVA work", work["BVA"] / 60, LIGHT),
         ("VA work", work["VA"] / 60, GREEN)]
left = 0
for lab, v, c in parts:
    plt.barh(0, v, left=left, color=c, edgecolor="k", label=f"{lab}: {v:.1f} h")
    left += v
plt.yticks([])
plt.xlabel("Hours from first contact to close-out")
plt.title("Where an RMA's 278 hours go")
plt.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.35), ncol=4)
save("time_profile.png")

# VOC distribution
x = pmap.MAX_ACCEPTABLE_DAYS
plt.figure(figsize=(7, 3))
plt.hist(x, bins=np.arange(2.5, 25.5, 1), color=LIGHT, edgecolor="k")
for p, c in ((10, BLUE), (50, "k")):
    v = np.percentile(x, p)
    plt.axvline(v, color=c, ls="--", label=f"{p}th percentile: {v:.0f} days")
plt.axvline(lead / 24, color=RED, label=f"current lead time: {lead/24:.1f} days")
plt.xlabel("Longest acceptable RMA turnaround (days)")
plt.ylabel("Customers")
plt.legend(fontsize=8)
plt.title("Voice of the customer: 120 survey responses")
save("voc_turnaround.png")

print("figures written to", os.path.abspath(FIG))
