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
import kaizen as k  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6"
TAKT = k.takt()


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# Current-state cycle times vs takt (bottleneck view)
names = [r[0] for r in k.VSM]
ct = [r[1] for r in k.VSM]
eff = [r[1] / r[3] for r in k.VSM]
x = np.arange(len(names))
plt.figure(figsize=(8, 3.4))
plt.bar(x - 0.2, ct, 0.4, color=LIGHT, edgecolor="k", label="Cycle time")
plt.bar(x + 0.2, eff, 0.4, color=BLUE, label="Effective C/T (÷ uptime)")
plt.axhline(TAKT, color=RED, ls="--", label=f"Takt {TAKT:.0f} s")
plt.xticks(x, names, rotation=20)
plt.ylabel("Seconds per unit")
plt.title("Current state: preload station is the constraint")
plt.legend(fontsize=8)
save("ct_vs_takt.png")

# Yamazumi: sequential 5-station vs U-cell 4-operator
seq = [[("Kit parts", 32), ("Insert balls", 48)], [("Load fixture", 14), ("Set preload", 58)],
       [("Fit seals", 22), ("Lubricate", 20)], [("Friction test", 52), ("Label", 10)], [("Pack", 30)]]
ucell = [[("Kit parts", 32), ("Pack", 30)], [("Insert balls", 48), ("Load fixture", 14)],
         [("Set preload", 58), ("Fit seals", 22)], [("Lubricate", 20), ("Friction test", 52), ("Label", 10)]]
fig, ax = plt.subplots(1, 2, figsize=(9, 3.6), sharey=True)
palette = ["#9dc3e6", "#bdd7ee", "#deebf7", "#c5e0b4"]
for a, layout, title in ((ax[0], seq, "Straight line: 5 operators"), (ax[1], ucell, "U-cell: 4 operators")):
    for i, st in enumerate(layout):
        bottom = 0
        for j, (n, t) in enumerate(st):
            a.bar(i, t, bottom=bottom, color=palette[j % 4], edgecolor="k")
            a.text(i, bottom + t / 2, n, ha="center", va="center", fontsize=6.5)
            bottom += t
    a.axhline(TAKT, color=RED, ls="--")
    a.axhline(0.95 * TAKT, color=GRAY, ls=":")
    a.set_xticks(range(len(layout)))
    a.set_xticklabels([f"Op {i+1}" for i in range(len(layout))])
    a.set_title(title)
ax[0].set_ylabel("Seconds per unit")
save("yamazumi.png")

# Daily output before/after with XmR limits from 'before'
y = k.DAILY_OUTPUT
m, mr, lo, hi = k.xmr(y[:20])
plt.figure(figsize=(8, 3.2))
plt.plot(range(1, len(y) + 1), y, "o-", color=BLUE)
plt.hlines([m], 1, len(y), colors="k", lw=1)
plt.hlines([lo, hi], 1, len(y), colors=RED, linestyles="--", lw=1)
plt.axhline(k.DEMAND_PER_DAY, color=GRAY, ls=":", label="Demand 560/day")
plt.axvline(20.5, color=GRAY, ls=":")
plt.text(21, hi + 5, "kaizen event", color=GRAY)
plt.title("Daily output: limits from 20 days before the event, extended")
plt.xlabel("Day")
plt.ylabel("Units")
plt.legend(fontsize=8, loc="lower right")
save("output_xmr.png")

print("figures written to", os.path.abspath(FIG))
