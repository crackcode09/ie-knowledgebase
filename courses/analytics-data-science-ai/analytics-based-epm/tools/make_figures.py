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
import epmkit as ek  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_whale():
    c = ek.customer_profit().sort_values("abc_profit", ascending=False)
    cum = c.abc_profit.cumsum() / 1e6
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    ax.plot(range(1, len(c) + 1), cum, color=BLUE, marker="o", ms=3)
    ax.axhline(cum.iloc[-1], color=GREY, ls="--")
    ax.text(len(c), cum.iloc[-1] - 0.12, f"total {cum.iloc[-1]:.2f} M", ha="right", fontsize=8)
    ax.text(cum.values.argmax() + 1, cum.max() + 0.05, f"peak {cum.max():.2f} M", ha="center", fontsize=8)
    ax.set_xlabel("Customers ranked by ABC profit")
    ax.set_ylabel("Cumulative profit ($M)")
    ax.set_title("Whale curve: the most profitable customers subsidize the rest", fontsize=10)
    save(fig, "03_whale_curve.png")


def fig_cts():
    c = ek.customer_profit()
    cols = [k for k in c.columns if k.startswith("cts_")]
    g = c.groupby("channel")[cols].sum()
    g = g.div(c.groupby("channel").revenue.sum(), axis=0) * 100
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    bottom = np.zeros(len(g))
    pal = [BLUE, ORANGE, GREEN, RED, GREY, "#553c9a", "#b7791f"]
    for i, k in enumerate(cols):
        ax.bar(g.index, g[k], bottom=bottom, color=pal[i % len(pal)], label=k[4:])
        bottom += g[k].values
    for i, v in enumerate(bottom):
        ax.text(i, v + 1, f"{v:.0f} %", ha="center", fontsize=9)
    ax.set_ylabel("Cost-to-serve, % of channel revenue")
    ax.legend(frameon=False, fontsize=7, ncol=2)
    save(fig, "05_cost_to_serve.png")


def fig_rolling():
    q = ek.load("quarterly_revenue")
    r = ek.ex_rolling()["forecast"]
    fig, ax = plt.subplots(figsize=(8, 3.4))
    ax.plot(range(16), q.revenue / 1e6, color=BLUE, marker="o", ms=3, label="Actual")
    x = range(16, 21)
    ax.plot(x, [f["forecast"] / 1e6 for f in r], color=ORANGE, marker="o", ms=3, label="Rolling forecast")
    ax.fill_between(x, [f["p10"] / 1e6 for f in r], [f["p90"] / 1e6 for f in r], color=ORANGE, alpha=0.2,
                    label="80 % interval")
    ax.set_xticks(range(0, 21, 4), ["2022", "2023", "2024", "2025", "2026", "2027"][:len(range(0, 21, 4))])
    ax.set_ylabel("Revenue per quarter ($M)")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "07_rolling_forecast.png")


def fig_mc():
    rng = np.random.default_rng(11)
    res = ek.ex_montecarlo()
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    for with_r, col, lab in [(False, GREY, "Without risk events"), (True, RED, "With risk register events")]:
        r = ek.ex_montecarlo(with_risks=with_r)
        k = "op_profit_with_risks" if with_r else "op_profit_no_risk"
        ax.axvline(r[k]["p50"] / 1e6, color=col, ls="--")
    # re-simulate to draw distributions
    import numpy as _np
    for with_r, col, lab in [(False, GREY, "Without risk events"), (True, RED, "With risk register events")]:
        sims = _sim(with_r)
        ax.hist(sims / 1e6, bins=60, color=col, alpha=0.5, label=lab, density=True)
    ax.set_xlabel("Operating profit next year ($M)")
    ax.set_yticks([])
    ax.legend(frameon=False, fontsize=8)
    ax.set_title(f"P10 with risks: {res['op_profit_with_risks']['p10'] / 1e6:.2f} M", fontsize=10)
    save(fig, "07_monte_carlo.png")


def _sim(with_risks, n=20000, seed=11):
    rng = np.random.default_rng(seed)
    c = ek.customer_profit()
    rev0 = float(c.revenue.sum())
    vr = float(c.direct.sum() / c.revenue.sum())
    growth = rng.triangular(0.00, 0.06, 0.11, n)
    price = rng.triangular(-0.02, 0.01, 0.03, n)
    mat = rng.triangular(0.00, 0.03, 0.09, n)
    op = rev0 * (1 + growth) * (1 + price) - vr * rev0 * (1 + growth) * (1 + mat) - sum(ek.RESOURCES.values()) * 1.03
    if with_risks:
        for _, r in ek.load("risk_register").iterrows():
            op -= (rng.random(n) < r.probability) * r.impact * rng.triangular(0.5, 1.0, 1.5, n)
    return op


if __name__ == "__main__":
    for f in [fig_whale, fig_cts, fig_rolling, fig_mc]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
