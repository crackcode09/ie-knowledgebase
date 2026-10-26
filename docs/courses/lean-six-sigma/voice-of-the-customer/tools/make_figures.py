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
import voc  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT, GREEN = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6", "#548235"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# Importance vs satisfaction
rows = voc.ex_importance()["need, importance, satisfaction, gap (sorted by gap)"]
plt.figure(figsize=(6.5, 4.2))
for k, imp, sat, gap in rows:
    plt.plot(sat, imp, "o", color=RED if gap > 1 else BLUE, ms=9)
    plt.annotate(k.replace("_", " "), (sat, imp), textcoords="offset points", xytext=(6, 4), fontsize=8)
plt.axhline(np.mean([r[1] for r in rows]), color=GRAY, ls=":")
plt.axvline(np.mean([r[2] for r in rows]), color=GRAY, ls=":")
plt.xlabel("Satisfaction with us (1-5)")
plt.ylabel("Importance to customer (1-5)")
plt.title("Importance vs satisfaction (n = 300): fix top-left first")
plt.xlim(2.3, 4.3)
plt.ylim(3.2, 4.7)
save("importance_satisfaction.png")

# Kano better/worse
k = voc.ex_kano()
plt.figure(figsize=(6.2, 4.2))
for f, d in k.items():
    plt.plot(-d["worse"], d["better"], "o", color=BLUE, ms=9)
    plt.annotate(f"{f.replace('_', ' ')}\n({d['category']})", (-d["worse"], d["better"]),
                 textcoords="offset points", xytext=(6, -10), fontsize=8)
plt.axhline(0.5, color=GRAY, ls=":")
plt.axvline(0.5, color=GRAY, ls=":")
plt.text(0.02, 0.95, "Attractive", color=GRAY)
plt.text(0.78, 0.95, "One-dimensional", color=GRAY)
plt.text(0.78, 0.02, "Must-be", color=GRAY)
plt.text(0.02, 0.02, "Indifferent", color=GRAY)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Dissatisfaction if absent (|worse| coefficient)")
plt.ylabel("Satisfaction if present (better coefficient)")
plt.title("Kano better-worse diagram, 4 candidate features")
save("kano_better_worse.png")

# Sampling distribution
rng = np.random.default_rng(1)
ph = rng.binomial(150, 0.30, 10000) / 150
plt.figure(figsize=(6.5, 3.2))
plt.hist(ph, bins=np.arange(0.15, 0.46, 1 / 150), color=LIGHT, edgecolor="none")
plt.axvline(0.30, color="k", label="true proportion 30%")
for v in (0.30 - 0.073, 0.30 + 0.073):
    plt.axvline(v, color=RED, ls="--")
plt.text(0.30 + 0.075, plt.ylim()[1] * 0.8, "±7.3 points\n(95% margin)", color=RED, fontsize=8)
plt.xlabel("Sample proportion")
plt.yticks([])
plt.title("10,000 surveys of 150 customers each")
plt.legend(fontsize=8, loc="upper left")
save("sampling_distribution.png")

# Acceptance curves by segment
r = voc.load()
days = np.arange(1, 15)
plt.figure(figsize=(6.5, 3.4))
for seg, c in zip(voc.SEGMENTS, (RED, BLUE, GREEN)):
    d = np.array([int(x["max_acceptable_days"]) for x in r if x["segment"] == seg])
    plt.plot(days, [(d >= t).mean() * 100 for t in days], "o-", color=c, label=seg, ms=4)
plt.axvline(5, color=GRAY, ls=":")
plt.text(5.1, 5, "current 5 days", color=GRAY, fontsize=8)
plt.xlabel("Delivery lead time (days)")
plt.ylabel("% of customers who accept it")
plt.title("Delivery time customers will accept, by segment")
plt.legend(fontsize=8)
save("acceptance_by_segment.png")

print("figures written to", os.path.abspath(FIG))
