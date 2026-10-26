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
import lean  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT, GREEN = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6", "#548235"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


# COPQ
tot = {k: sum(v.values()) / 1000 for k, v in lean.COPQ.items()}
plt.figure(figsize=(6.5, 3))
plt.barh(list(tot.keys())[::-1], list(tot.values())[::-1], color=[RED, RED, LIGHT, GREEN], edgecolor="k")
for i, v in enumerate(list(tot.values())[::-1]):
    plt.text(v + 10, i, f"${v:,.0f}k", va="center", fontsize=8)
plt.xlabel("USD thousands per year")
plt.title("Cost of poor quality: $2.46M = 10.2% of sales")
save("copq.png")

# Bullwhip
rng = np.random.default_rng(3)
weeks, lead, review, alpha = 104, 2, 1, 0.3
demand = np.clip(rng.normal(100, 10, weeks), 0, None)
streams = {"Customer demand": demand}
stream = demand
for name in ("Retailer orders", "Distributor orders", "Factory production"):
    f = stream[0]
    prev = f * (lead + review)
    out = []
    for d in stream:
        f = alpha * d + (1 - alpha) * f
        tgt = f * (lead + review)
        out.append(max(0.0, d + tgt - prev))
        prev = tgt
    stream = np.array(out)
    streams[name] = stream
plt.figure(figsize=(8, 3.4))
for (n, s), c in zip(streams.items(), (GRAY, BLUE, GREEN, RED)):
    plt.plot(range(20, weeks), s[20:], color=c, label=n, lw=1.2)
plt.xlabel("Week")
plt.ylabel("Units")
plt.title("Bullwhip effect: same end demand, amplified upstream")
plt.legend(fontsize=8, ncol=2)
save("bullwhip.png")

# CONWIP caps
caps = [3, 4, 5, 6, 8, 10, 14, 20, 30]
res = [lean.simulate_line("conwip", c, n_jobs=12000) for c in caps]
push = lean.simulate_line("push", n_jobs=12000)
fig, ax = plt.subplots(figsize=(7, 3.4))
ax.plot(caps, [r["throughput/day"] for r in res], "o-", color=BLUE, label="Throughput/day")
ax.axhline(push["throughput/day"], color=BLUE, ls=":", lw=1)
ax.set_xlabel("CONWIP cap (jobs on the floor)")
ax.set_ylabel("Throughput per day", color=BLUE)
ax2 = ax.twinx()
ax2.plot(caps, [r["avg floor flow time (min)"] for r in res], "s-", color=RED, label="Floor flow time")
ax2.set_ylabel("Floor flow time (min)", color=RED)
ax.set_title("CONWIP: a cap too low starves the bottleneck")
save("conwip.png")

# OEE six big losses waterfall
t = lean.ex_tpm()
losses = t["six big losses (min/shift)"]
labels = ["Loading time"] + list(losses) + ["Valuable time"]
vals = [440] + [-v for v in losses.values()] + [t["valuable operating time (min)"]]
fig, ax = plt.subplots(figsize=(8, 3.6))
level = 0
for i, (lab, v) in enumerate(zip(labels, vals)):
    if i == 0 or i == len(vals) - 1:
        ax.bar(i, v, color=BLUE if i == 0 else GREEN, edgecolor="k")
        level = v if i == 0 else level
    else:
        ax.bar(i, -v, bottom=level + v, color=RED, edgecolor="k")
        level += v
ax.set_xticks(range(len(labels)))
ax.set_xticklabels(labels, rotation=30, ha="right", fontsize=8)
ax.set_ylabel("Minutes per shift")
ax.set_title(f"Six big losses: OEE = {t['OEE (time-loss method)']:.0%}")
save("oee_losses.png")

# Product-process matrix before/after clustering
r, c = lean.rank_order_clustering(lean.PPM)
fig, ax = plt.subplots(1, 2, figsize=(9, 3.6))
for a, m, rows, cols, title in ((ax[0], lean.PPM, range(10), range(7), "Before (part number order)"),
                                (ax[1], lean.PPM[r][:, c], r, c, "After rank order clustering")):
    a.imshow(m, cmap="Blues", vmin=0, vmax=1.3)
    a.set_xticks(range(7))
    a.set_xticklabels([lean.MACHINES[j] for j in cols], rotation=45, fontsize=7)
    a.set_yticks(range(10))
    a.set_yticklabels([lean.PARTS[i] for i in rows], fontsize=7)
    a.set_title(title, fontsize=9)
save("product_process_matrix.png")

print("figures written to", os.path.abspath(FIG))
