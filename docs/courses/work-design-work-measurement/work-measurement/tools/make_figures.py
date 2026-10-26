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

sys.path.insert(0, os.path.dirname(__file__))
import wmkit as wk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_element_cycles():
    c = wk.element_times()
    fig, ax = plt.subplots(figsize=(8, 3.8))
    for e, g in c.groupby("element"):
        ax.plot(g.cycle, g.observed_s, marker="o", ms=3, label=e)
    f = c[c.note != ""]
    ax.scatter(f.cycle, f.observed_s, s=120, facecolors="none", edgecolors=RED, linewidths=2, zorder=3)
    ax.annotate("foreign element:\ndropped bit", (f.cycle.iloc[0], f.observed_s.iloc[0]), xytext=(15, -10),
                textcoords="offset points", color=RED, fontsize=8)
    ax.set_xlabel("Cycle")
    ax.set_ylabel("Element time (s)")
    ax.set_title("Element times by cycle: screen for foreign elements before averaging", loc="left")
    ax.legend(frameon=False, fontsize=7, ncol=6, loc="upper center", bbox_to_anchor=(0.5, -0.18))
    save(fig, "05_element_times_by_cycle.png")


def fig_build_up():
    r = wk.ex_timestudy()
    el = r["elements"]
    obs = sum(x["mean_observed_s"] for x in el)
    nt = r["normal time per pump (s)"]
    std = r["standard time, allowance on manual elements only (s)"]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.bar(["Observed\n(average)", "Normal\n(× rating)", "Standard\n(+ allowances)"], [obs, nt, std],
           color=[GREY, BLUE, ORANGE])
    for i, v in enumerate([obs, nt, std]):
        ax.text(i, v + 1.5, f"{v:.1f} s", ha="center")
    ax.set_ylabel("Seconds per pump")
    ax.set_ylim(0, std * 1.15)
    ax.set_title("From observed time to standard time (pump assembly)", loc="left", weight="bold")
    save(fig, "08_time_build_up.png")


def fig_rating():
    r = wk.load("rating_practice.csv")
    fig, ax = plt.subplots(figsize=(6.5, 4))
    for a, c in zip(sorted(r.analyst.unique()), (BLUE, GREEN, ORANGE, RED)):
        g = r[r.analyst == a]
        ax.scatter(g.benchmark_pct, g.rating_pct, color=c, label=a, s=25)
    ax.plot([75, 135], [75, 135], color="black", lw=1)
    ax.fill_between([75, 135], [70, 130], [80, 140], color=GREY, alpha=0.25, label="±5 points")
    ax.set_xlabel("Benchmark pace (%)")
    ax.set_ylabel("Analyst rating (%)")
    ax.set_title("Rating practice: bias (B, C) and inconsistency (D)", loc="left")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "06_rating_practice.png")


def fig_labor():
    r = wk.ex_labor()["by operator (4 weeks)"]
    ops = [x["operator"] for x in r]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    x = np.arange(len(ops))
    ax.bar(x - 0.2, [x_["efficiency_% (earned/on-std)"] for x_ in r], 0.4, color=BLUE, label="efficiency (earned / on-standard)")
    ax.bar(x + 0.2, [x_["utilization_% (on-std/paid)"] for x_ in r], 0.4, color=GREY, label="utilization (on-standard / paid)")
    ax.axhline(100, color="black", lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(ops)
    ax.set_ylim(60, 125)
    ax.set_ylabel("%")
    ax.set_title("Labor report, 4 weeks: one operator below standard; utilization is the bigger loss", loc="left")
    ax.legend(frameon=False, fontsize=8, loc="upper right", ncol=2)
    save(fig, "09_labor_report.png")


def fig_sampling():
    w = wk.load("work_sampling_kitting.csv")
    share = w.activity.value_counts(normalize=True)
    n = len(w)
    ci = 1.96 * np.sqrt(share * (1 - share) / n)
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    axes[0].barh(share.index[::-1], 100 * share.values[::-1], xerr=100 * ci.values[::-1], color=BLUE, capsize=3)
    axes[0].set_xlabel("% of observations (95% CI)")
    axes[0].set_title(f"Kitting work sampling, {n} observations", loc="left")
    d = w.assign(pick=w.activity.eq("picking")).groupby("day").agg(n=("pick", "size"), p=("pick", "mean"))
    pbar = w.activity.eq("picking").mean()
    ucl = pbar + 3 * np.sqrt(pbar * (1 - pbar) / d.n)
    lcl = pbar - 3 * np.sqrt(pbar * (1 - pbar) / d.n)
    axes[1].plot(d.index, 100 * d.p, marker="o", color=BLUE)
    axes[1].step(d.index, 100 * ucl, where="mid", color=RED, ls="--")
    axes[1].step(d.index, 100 * lcl, where="mid", color=RED, ls="--")
    axes[1].axhline(100 * pbar, color="black", lw=1)
    axes[1].set_xlabel("Day")
    axes[1].set_ylabel("% picking")
    axes[1].set_title("Daily p chart: is the study stable?", loc="left")
    save(fig, "11_work_sampling.png")


def fig_standard_data():
    s = wk.load("packout_studies.csv")
    r = wk.ex_standard_data()["formula (normal minutes)"]
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    for h, c, lab in ((0, BLUE, "no heavy items"), (1, ORANGE, "with heavy items")):
        g = s[s.heavy_items == h]
        ax.scatter(g.items_per_crate, g.normal_minutes, color=c, label=lab)
        xx = np.array([4, 40])
        ax.plot(xx, r["Intercept"] + r["items_per_crate"] * xx + r["heavy_items"] * h, color=c)
    ax.set_xlabel("Items per crate")
    ax.set_ylabel("Normal minutes (from time studies)")
    ax.set_title("Standard data: one formula replaces many studies", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "12_standard_data.png")


def fig_learning():
    first, rate = 4.20, 0.85
    b = math.log(rate) / math.log(2)
    std = wk.ex_timestudy()["standard minutes per pump (allowance on manual only)"]
    n = np.arange(1, 201)
    t = first * n ** b
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.plot(n, t, color=GREY, ls="--", label="85% learning curve")
    ax.plot(n, np.maximum(t, std), color=BLUE, lw=2, label="planning curve (floors at standard)")
    ax.axhline(std, color=ORANGE, ls=":", label=f"standard {std} min")
    ax.set_xlabel("Unit number (new operator)")
    ax.set_ylabel("Minutes per pump")
    ax.set_title("Learning: when a new operator reaches standard", loc="left")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "13_learning_curve.png")


if __name__ == "__main__":
    for f in (fig_element_cycles, fig_build_up, fig_rating, fig_labor, fig_sampling, fig_standard_data, fig_learning):
        f()
    print("figures written to", os.path.abspath(FIG))
