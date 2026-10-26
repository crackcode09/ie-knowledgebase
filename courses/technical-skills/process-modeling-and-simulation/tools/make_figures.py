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
import procsim as ps  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
BLUE, RED, GRAY, LIGHT, GREEN = "#1f4e79", "#c00000", "#7f7f7f", "#9dc3e6", "#548235"


def save(name):
    plt.tight_layout()
    plt.savefig(os.path.join(FIG, name), dpi=110)
    plt.close()


def leads(d, days=150):
    rng = np.random.default_rng(d.seed)
    return np.concatenate([ps.simulate_day(d, rng)["lead"] for _ in range(days)])


# Static vs simulated lead time
L = leads(ps.Design())
plt.figure(figsize=(7, 3.2))
plt.hist(L, bins=np.arange(0, 16, 0.5), color=LIGHT, edgecolor="k")
plt.axvline(1.71, color=GREEN, lw=2, label="static map: sum of work = 1.7 h")
plt.axvline(L.mean(), color=BLUE, ls="--", label=f"simulated mean = {L.mean():.1f} h")
plt.axvline(8, color=RED, label="promise = 8 h")
plt.xlabel("Lead time (h)")
plt.ylabel("Jobs (150 days)")
plt.title("Same process, static vs dynamic view")
plt.legend(fontsize=8)
save("static_vs_dynamic.png")

# Hourly arrivals
plt.figure(figsize=(6.5, 2.8))
plt.bar([f"{7+h:02d}:00" for h in range(10)], ps.ARRIVALS_PER_HOUR, color=LIGHT, edgecolor="k")
plt.ylabel("Units per hour (avg)")
plt.title("Arrival pattern: peak mid-morning")
plt.xticks(rotation=45, fontsize=8)
save("arrivals.png")

# Design comparison
designs = [ps.Design(name="A Current"), ps.Design(name="B +1 tech", repair_techs=5),
           ps.Design(name="C Pool", pooled_techs=True),
           ps.Design(name="D Pool+SPT", pooled_techs=True, dispatch="SPT"),
           ps.Design(name="E Parts", parts_wait_p=0.08),
           ps.Design(name="F Pool+parts", pooled_techs=True, parts_wait_p=0.08)]
res = [ps.run(d, days=150) for d in designs]
fig, ax = plt.subplots(figsize=(7.5, 3.2))
x = np.arange(len(res))
ax.bar(x, [r["on time (<= 8 h)"] * 100 for r in res], color=BLUE)
for i, r in enumerate(res):
    ax.text(i, r["on time (<= 8 h)"] * 100 + 0.3, f"{r['on time (<= 8 h)']*100:.1f}%", ha="center", fontsize=8)
ax.set_xticks(x)
ax.set_xticklabels([d.name for d in designs], fontsize=8)
ax.set_ylim(80, 100)
ax.set_ylabel("% jobs within 8 h")
ax.set_title("Exploring the design space")
save("designs.png")

# Resilience curves
scales = [0.9, 1.0, 1.1, 1.2, 1.3]
plt.figure(figsize=(6.5, 3.2))
for d, c in ((ps.Design(name="A Current"), RED), (ps.Design(name="F Pool + parts", pooled_techs=True, parts_wait_p=0.08), BLUE)):
    vals = []
    for s in scales:
        dd = ps.Design(**{**d.__dict__, "arrival_scale": s})
        vals.append(ps.run(dd, days=100)["on time (<= 8 h)"] * 100)
    plt.plot([s * 100 for s in scales], vals, "o-", color=c, label=d.name)
plt.axhline(90, color=GRAY, ls=":")
plt.xlabel("Demand (% of today)")
plt.ylabel("% within 8 h")
plt.title("Resilience to demand growth")
plt.legend(fontsize=8)
save("resilience.png")

# FMEA impact
f = ps.ex_fmea()
rows = f["failure mode, on time, drop"]
plt.figure(figsize=(7, 3))
plt.barh([r[0] for r in rows][::-1], [r[2] * 100 for r in rows][::-1], color=RED)
plt.xlabel("Drop in on-time % (points)")
plt.title("Simulated impact of failure modes")
save("fmea_impact.png")

print("figures written to", os.path.abspath(FIG))
