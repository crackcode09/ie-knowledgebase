"""make_figures.py - regenerate every figure in figures/.

    python tools/make_figures.py

License: MIT
"""
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import qekit as qk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_pareto():
    r = qk.ex_pareto()["pareto"]
    names = [x["defect"] for x in r]
    cnt = [x["count"] for x in r]
    cum = [x["cum_pct"] for x in r]
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.bar(names, cnt, color=[BLUE, BLUE] + [GREY] * (len(names) - 2))
    ax.set_ylabel("Defective inserts (of 480)")
    ax2 = ax.twinx()
    ax2.plot(names, cum, color=ORANGE, marker="o")
    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Cumulative %")
    ax2.spines["top"].set_visible(False)
    ax.set_title("Oversize OD and thread damage: 77.5% of defectives", loc="left", weight="bold")
    save(fig, "02_defect_pareto.png")


def fig_histogram():
    p = qk.load("production_sample.csv")
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.hist([p[p.machine == "M1"].od_mm, p[p.machine == "M2"].od_mm], bins=20, stacked=True, color=[GREY, BLUE],
            label=["M1", "M2"], edgecolor="white")
    for v, lab in ((qk.LSL, "LSL"), (qk.USL, "USL"), (qk.TARGET, "target")):
        ax.axvline(v, color=RED if lab != "target" else "black", ls="--" if lab != "target" else ":")
        ax.text(v, ax.get_ylim()[1] * 0.92, f" {lab}", fontsize=8)
    ax.set_xlabel("Insert OD (mm)")
    ax.set_ylabel("Inserts")
    ax.set_title("OD histogram, stacked by machine: M2 runs large", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "02_od_histogram.png")


def fig_distribution():
    q = qk.load("quote_turnaround.csv").turnaround_h.values
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.hist(q, bins=20, density=True, color=GREY, edgecolor="white")
    t = np.linspace(0.1, q.max() * 1.1, 300)
    ax.plot(t, stats.norm.pdf(t, q.mean(), q.std(ddof=1)), color=RED, ls="--", label="normal fit")
    s, loc, sc = stats.lognorm.fit(q, floc=0)
    ax.plot(t, stats.lognorm.pdf(t, s, loc, sc), color=BLUE, lw=2, label="lognormal fit (best AIC)")
    ax.set_xlabel("Quote turnaround (hours)")
    ax.set_yticks([])
    ax.set_title("Distribution identification: skewed data, lognormal fits", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "02_distribution_fit.png")


def fig_grr():
    g = qk.load("gauge_rr.csv")
    r = qk.ex_grr()["% study variation"]
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    keys = ["total gauge R&R", "repeatability", "reproducibility", "part-to-part"]
    axes[0].bar(keys, [r[k] for k in keys], color=[RED, ORANGE, ORANGE, BLUE])
    axes[0].axhline(10, color=GREY, ls=":")
    axes[0].axhline(30, color=GREY, ls=":")
    axes[0].set_ylabel("% study variation")
    axes[0].set_title("Components of variation", loc="left")
    axes[0].tick_params(axis="x", labelsize=8)
    for op, c in zip(["Ana", "Ben", "Cai"], (BLUE, ORANGE, GREEN)):
        m = g[g.operator == op].groupby("part").od_mm.mean()
        axes[1].plot(m.index, m.values, marker="o", color=c, label=op)
    axes[1].set_xlabel("Part")
    axes[1].set_ylabel("Average OD (mm)")
    axes[1].set_title("Operator by part: Ben reads high on every part", loc="left")
    axes[1].legend(frameon=False)
    save(fig, "03_gauge_rr.png")


def fig_imr_log():
    q = qk.load("quote_turnaround.csv").turnaround_h.values
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.6))
    for ax, x, lab in ((axes[0], q, "hours (raw)"), (axes[1], np.log(q), "ln(hours)")):
        mr = np.abs(np.diff(x)).mean()
        u, l = x.mean() + 2.66 * mr, x.mean() - 2.66 * mr
        ax.plot(range(1, len(x) + 1), x, color=BLUE, marker="o", ms=2, lw=0.8)
        ax.axhline(x.mean(), color="black", lw=1)
        ax.axhline(u, color=RED, ls="--")
        ax.axhline(l, color=RED, ls="--")
        out = (x > u) | (x < l)
        ax.scatter(np.arange(1, len(x) + 1)[out], x[out], color=RED, zorder=3)
        ax.set_xlabel("Quote")
        ax.set_ylabel(lab)
    axes[0].set_title("Raw: negative LCL, 2 false-looking signals", loc="left")
    axes[1].set_title("Log-transformed: symmetric, no signals", loc="left")
    save(fig, "04_individuals_transform.png")


def fig_staged():
    d = qk.load("pilot_daily.csv")
    fig, ax = plt.subplots(figsize=(8, 3.6))
    for st, g in d.groupby("stage", sort=False):
        pbar = g.oversize.sum() / g.inspected.sum()
        n = g.inspected.iloc[0]
        u = pbar + 3 * math.sqrt(pbar * (1 - pbar) / n)
        lo = max(0.0, pbar - 3 * math.sqrt(pbar * (1 - pbar) / n))
        x = g.day.values
        ax.plot(x, 100 * g.oversize / g.inspected, color=BLUE, marker="o")
        ax.hlines(100 * pbar, x[0] - 0.4, x[-1] + 0.4, color="black")
        ax.hlines([100 * u, 100 * lo], x[0] - 0.4, x[-1] + 0.4, color=RED, ls="--")
        ax.text(x[0], 100 * u + 0.4, f"{st}: p̄ = {100*pbar:.2f}%", fontsize=9)
    ax.axvline(10.5, color=GREY, ls=":")
    ax.set_xlabel("Day")
    ax.set_ylabel("% oversize (M2)")
    ax.set_title("Staged p chart: new limits after the pilot change", loc="left", weight="bold")
    save(fig, "04_staged_p_chart.png")


def fig_box_scatter():
    p = qk.load("production_sample.csv")
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    groups = [(m, s) for m in ("M1", "M2") for s in ("A", "B", "C")]
    data = [p[(p.machine == m) & (p["shift"] == s)].od_mm for m, s in groups]
    bp = axes[0].boxplot(data, patch_artist=True)
    for patch, (m, _) in zip(bp["boxes"], groups):
        patch.set_facecolor(BLUE if m == "M2" else GREY)
    axes[0].set_xticks(range(1, 7))
    axes[0].set_xticklabels([f"{m}-{s}" for m, s in groups])
    axes[0].axhline(qk.USL, color=RED, ls="--")
    axes[0].set_ylabel("OD (mm)")
    axes[0].set_title("Box plots by machine-shift", loc="left")
    for m, c in (("M1", GREY), ("M2", BLUE)):
        g = p[p.machine == m]
        axes[1].scatter(g.tool_age_parts, g.od_mm, s=8, color=c, alpha=0.6, label=m)
        b = np.polyfit(g.tool_age_parts, g.od_mm, 1)
        xx = np.array([0, 2400])
        axes[1].plot(xx, np.polyval(b, xx), color=c, lw=2)
    axes[1].axhline(qk.USL, color=RED, ls="--")
    axes[1].set_xlabel("Tool age (parts since tool change)")
    axes[1].set_ylabel("OD (mm)")
    axes[1].set_title("OD grows with tool wear; M2 starts higher", loc="left")
    axes[1].legend(frameon=False)
    save(fig, "05_box_scatter.png")


if __name__ == "__main__":
    for f in (fig_pareto, fig_histogram, fig_distribution, fig_grr, fig_imr_log, fig_staged, fig_box_scatter):
        f()
    print("figures written to", os.path.abspath(FIG))
