"""make_figures.py - regenerate every figure in figures/.

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
import coqkit as ck  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
COL = {"Prevention": "#2f855a", "Appraisal": "#2b6cb0", "Internal failure": "#dd6b20", "External failure": "#c53030"}
GREY = "#a0aec0"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_models():
    q = np.linspace(0.90, 0.9999, 500)
    nonconf = 2_000_000 * (1 - q)
    classic = 20_000 / (1 - q) ** 0.5 - 20_000 / 0.1 ** 0.5
    modern = 90_000 * (q - 0.90) / 0.0999
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
    for ax, conf, title in ((axes[0], classic, "Classic view: an 'optimum' below 100%"),
                            (axes[1], modern, "Modern view: total cost keeps falling")):
        ax.plot(100 * q, nonconf / 1000, color=COL["Internal failure"], label="cost of nonconformance (failures)")
        ax.plot(100 * q, conf / 1000, color=COL["Prevention"], label="cost of conformance (prevention + appraisal)")
        tot = (conf + nonconf) / 1000
        ax.plot(100 * q, tot, color="black", lw=2, label="total")
        i = int(np.argmin(tot))
        ax.scatter(100 * q[i], tot[i], color="black", zorder=3)
        ax.set_ylim(0, 250)
        ax.set_xlabel("Conformance level (%)")
        ax.set_title(title, loc="left", fontsize=10)
    axes[0].set_ylabel("$000 per period (illustrative)")
    axes[1].legend(frameon=False, fontsize=8)
    save(fig, "01_coq_models.png")


def fig_monthly():
    led = ck.load("coq_ledger.csv")
    ops = ck.load("monthly_operations.csv").set_index("month")
    m = led.pivot_table(index="month", columns="category", values="cost", aggfunc="sum")[ck.CATS] / 1000
    fig, ax = plt.subplots(figsize=(9, 4))
    bottom = np.zeros(len(m))
    x = np.arange(len(m))
    for c in ck.CATS:
        ax.bar(x, m[c], bottom=bottom, color=COL[c], label=c)
        bottom += m[c].values
    ax.set_xticks(x)
    ax.set_xticklabels([s[5:] for s in m.index])
    ax.set_xlabel("Month (2026)")
    ax.set_ylabel("Cost of quality ($000)")
    ax.axvline(5.5, color="black", ls=":", lw=1)
    ax.text(5.6, bottom.max() * 1.02, "program starts", fontsize=8)
    ax.set_ylim(0, bottom.max() * 1.1)
    ax2 = ax.twinx()
    ax2.plot(x, 100 * m.sum(axis=1) * 1000 / ops.sales.values, color="black", marker="o", label="CoQ % of sales")
    ax2.set_ylim(0, 9)
    ax2.set_ylabel("CoQ % of sales")
    ax2.spines["top"].set_visible(False)
    ax.legend(frameon=False, fontsize=8, loc="upper center", bbox_to_anchor=(0.5, -0.14), ncol=4)
    ax.set_title("Monthly cost of quality: prevention up, failures down", loc="left", weight="bold")
    save(fig, "02_monthly_coq.png")


def fig_failure_pareto():
    r = ck.ex_failures()["failure-cost elements (annual)"]
    fig, ax = plt.subplots(figsize=(8, 4))
    names = [x["element"] for x in r]
    ax.barh(names[::-1], [x["cost"] / 1000 for x in r][::-1],
            color=[COL[x["category"]] for x in r][::-1])
    ax.set_xlabel("Annual cost ($000)")
    ax.set_title("Failure-cost elements: scrap, rework and warranty lead", loc="left", weight="bold")
    save(fig, "05_failure_elements.png")


def fig_drivers():
    d = ck.ex_drivers()["drivers ranked by cost"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    names = [x["failure_type"] for x in d]
    axes[0].barh(names[::-1], [x["cost"] / 1000 for x in d][::-1], color=COL["Internal failure"])
    axes[0].set_xlabel("Failure cost, 6 months ($000)")
    axes[0].set_title("Ranked by cost", loc="left")
    by_n = sorted(d, key=lambda x: x["events"], reverse=True)
    axes[1].barh([x["failure_type"] for x in by_n][::-1], [x["events"] for x in by_n][::-1], color=GREY)
    axes[1].set_xlabel("Events, 6 months")
    axes[1].set_title("Ranked by count: a different order", loc="left")
    save(fig, "09_drivers_cost_vs_count.png")


def fig_iceberg():
    h = ck.ex_hidden()
    fig, ax = plt.subplots(figsize=(7, 4))
    vis = h["visible failure cost, annualized from months 1-6 ($/yr)"] / 1000
    items = ck.load("hidden_costs.csv").sort_values("annual_estimate")
    ax.bar(0, vis, color=COL["Internal failure"], width=0.6)
    ax.text(0, vis / 2, f"booked failure\ncosts\n${vis:,.0f}k", ha="center", va="center", color="white", fontsize=9)
    bottom = 0
    for _, r in items.iterrows():
        v = r.annual_estimate / 1000
        ax.bar(1, v, bottom=bottom, color=GREY, edgecolor="white", width=0.6)
        if v > 60:
            short = {"Sales lost": "lost sales", "Lost capacity": "lost bottleneck capacity",
                     "Engineering time": "engineering firefighting", "Expediting and": "expediting / premium freight"}
            lab = next((v2 for k2, v2 in short.items() if r.hidden_cost.startswith(k2)), "")
            ax.text(1, bottom + v / 2, f"{lab} ${v:,.0f}k", ha="center", va="center", fontsize=7)
        bottom += v
    ax.text(1, bottom + 30, f"hidden (estimated)\n${bottom:,.0f}k", ha="center", fontsize=9)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Visible (booked)", "Hidden (estimated)"])
    ax.set_ylabel("$000 per year")
    ax.set_title("The iceberg: costs that never reach the quality ledger", loc="left", weight="bold")
    save(fig, "07_hidden_costs.png")


def fig_loss():
    x = np.linspace(49.96, 50.04, 300)
    k = 180 / 0.025 ** 2
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.plot(x, k * (x - 50) ** 2, color="black", lw=2, label="quadratic loss k(y − T)²")
    ax.plot(x, np.where(np.abs(x - 50) > 0.025, 180, 0), color=COL["External failure"], ls="--", label="'goalpost' view")
    ax.axvline(49.975, color=GREY, ls=":")
    ax.axvline(50.025, color=GREY, ls=":")
    ax.set_ylim(0, 450)
    ax.set_xlabel("Bore diameter (mm), target 50.000")
    ax.set_ylabel("Loss per cylinder ($)")
    ax.set_title("Loss grows with distance from target, not only outside spec", loc="left")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "07_quality_loss.png")


def fig_before_after():
    mth = ck.ex_monthly()
    b, a = mth["months 1-6 (before)"], mth["months 10-12 (after)"]
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    x = np.arange(4)
    ax.bar(x - 0.2, [b[f"{c} / month"] / 1000 for c in ck.CATS], 0.4, color=GREY, label="months 1–6")
    ax.bar(x + 0.2, [a[f"{c} / month"] / 1000 for c in ck.CATS], 0.4, color=[COL[c] for c in ck.CATS], label="months 10–12")
    ax.set_xticks(x)
    ax.set_xticklabels([c.replace(" ", "\n") for c in ck.CATS])
    ax.set_ylabel("$000 per month")
    ax.set_title(f"Net monthly CoQ down ${mth['monthly reduction ($)']:,}", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "11_before_after.png")


if __name__ == "__main__":
    for f in (fig_models, fig_monthly, fig_failure_pareto, fig_drivers, fig_iceberg, fig_loss, fig_before_after):
        f()
    print("figures written to", os.path.abspath(FIG))
