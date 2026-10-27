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
import statsmodels.formula.api as smf

sys.path.insert(0, os.path.dirname(__file__))
import dalkit as dk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY = "#2b6cb0", "#dd6b20", "#a0aec0"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_quality():
    q = dk.ex_quality()["scores_pct"]
    names = list(q)[::-1]
    fig, ax = plt.subplots(figsize=(8, 3.6))
    ax.barh(names, [q[k] for k in names], color=[ORANGE if q[k] < 95 else BLUE for k in names])
    ax.set_xlim(0, 100)
    ax.set_xlabel("% of customer master records passing")
    ax.tick_params(axis="y", labelsize=8)
    save(fig, "01_data_quality.png")


def fig_hist():
    o = dk.load("orders")
    fig, ax = plt.subplots(figsize=(7, 3.2))
    ax.hist(o.order_value, bins=50, color=BLUE)
    ax.axvline(o.order_value.mean(), color=ORANGE, ls="--", label=f"mean {o.order_value.mean():.0f}")
    ax.axvline(o.order_value.median(), color="k", ls=":", label=f"median {o.order_value.median():.0f}")
    ax.set_xlabel("Order value ($)")
    ax.set_ylabel("Orders")
    ax.legend(frameon=False)
    save(fig, "02_order_value_hist.png")


def fig_regression():
    b = dk.load("branch_monthly")
    train, test = b[b.month <= 18], b[b.month > 18]
    m = smf.ols("sales_k ~ marketing_k + sales_reps + active_accounts", data=train).fit()
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    ax.scatter(test.sales_k, m.predict(test), color=BLUE)
    lim = [test.sales_k.min() - 20, test.sales_k.max() + 20]
    ax.plot(lim, lim, color=GREY, ls="--")
    ax.set_xlabel("Actual monthly sales ($k), months 19-24")
    ax.set_ylabel("Predicted ($k)")
    ax.set_title("Hold-out check of the MLR model", fontsize=10)
    save(fig, "03_regression_holdout.png")


def fig_story():
    o = dk.load("orders")
    g = o.groupby("branch").order_value.mean().sort_values()
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.6))
    ax = axs[0]
    cols = plt.cm.tab10(np.arange(len(g)))
    ax.bar(g.index, g.values, color=cols, edgecolor="k")
    ax.grid(True, axis="both")
    ax.set_title("Before: Average Order Value by Branch (FY2025)", fontsize=9)
    ax.set_ylabel("AOV")
    ax.legend(g.index, fontsize=6, loc="upper left")
    ax.spines["top"].set_visible(True)
    ax.spines["right"].set_visible(True)
    ax = axs[1]
    c = [ORANGE if b in ("East",) else GREY for b in g.index]
    ax.barh(g.index, g.values, color=c)
    for i, v in enumerate(g.values):
        ax.text(v + 3, i, f"${v:.0f}", va="center", fontsize=9)
    ax.set_xticks([])
    ax.spines["bottom"].set_visible(False)
    ax.set_title("After: East's orders are 22 % larger than South's.\nWhat is East doing that others can copy?",
                 fontsize=10, loc="left")
    save(fig, "04_storytelling_before_after.png")


if __name__ == "__main__":
    for f in [fig_quality, fig_hist, fig_regression, fig_story]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
