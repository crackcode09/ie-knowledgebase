"""make_figures.py - regenerate every figure in figures/ from data/*.csv.

    python tools/make_figures.py

License: MIT
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import doekit as dk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY = "#2b6cb0", "#dd6b20", "#718096"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_crd():
    df = dk.load("crd_suppliers.csv")
    names = sorted(df.supplier.unique())
    fig, ax = plt.subplots(figsize=(6, 3.6))
    for i, s in enumerate(names):
        y = df[df.supplier == s].strength
        ax.scatter(np.full(len(y), i) + np.linspace(-0.08, 0.08, len(y)), y, color=GREY, s=18)
        ax.plot([i - 0.25, i + 0.25], [y.mean()] * 2, color=BLUE, lw=2.5)
    ax.axhline(df.strength.mean(), color=ORANGE, ls="--", lw=1, label="grand mean")
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names)
    ax.set_xlabel("Resin supplier")
    ax.set_ylabel("Tensile strength (MPa)")
    ax.set_title("CRD: 6 cages per supplier, bars = supplier means")
    ax.legend(frameon=False)
    save(fig, "01_crd_suppliers.png")


def fig_rbd():
    df = dk.load("rbd_release_agent.csv")
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.6), sharey=True)
    agents = sorted(df.agent.unique())
    for i, a in enumerate(agents):
        y = df[df.agent == a].force
        axes[0].scatter([i] * len(y), y, color=GREY, s=18)
        axes[0].plot([i - 0.25, i + 0.25], [y.mean()] * 2, color=BLUE, lw=2.5)
    axes[0].set_title("Ignoring molds: agents look alike")
    for m, g in df.groupby("mold"):
        g = g.set_index("agent").loc[agents]
        axes[1].plot(range(4), g.force, marker="o", label=m)
    axes[1].set_title("Each line is one mold (block)")
    axes[1].legend(frameon=False, fontsize=8, loc="center left", bbox_to_anchor=(1.0, 0.5))
    for ax in axes:
        ax.set_xticks(range(4))
        ax.set_xticklabels(agents)
        ax.set_xlabel("Release agent")
    axes[0].set_ylabel("Ejection force (N)")
    save(fig, "02_rbd_blocks.png")


def fig_interaction():
    df = dk.load("twofactor_shrinkage.csv")
    cell = df.groupby(["hold_pressure", "melt_temp"]).shrinkage.mean().unstack()
    fig, ax = plt.subplots(figsize=(6, 3.6))
    for T, c in zip(cell.columns, (BLUE, GREY, ORANGE)):
        ax.plot(cell.index, cell[T], marker="o", color=c, label=f"melt {T} °C")
    ax.set_xlabel("Hold pressure (MPa)")
    ax.set_ylabel("Mean shrinkage (%)")
    ax.set_title("Two-factor interaction plot (near-parallel lines = weak interaction)")
    ax.legend(frameon=False)
    save(fig, "04_twofactor_interaction.png")


def fig_effects():
    df = dk.load("full_factorial_warpage.csv")
    fact = df[df.A != 0]
    eff = dk.effects_2k(fact, "warpage", ["A", "B", "C", "D"])
    pse, me = dk.lenth_pse(eff)
    items = sorted(eff.items(), key=lambda kv: abs(kv[1]))
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    names = [k for k, _ in items]
    vals = [abs(v) for _, v in items]
    axes[0].barh(names, vals, color=[BLUE if v > me else GREY for v in vals])
    axes[0].axvline(me, color=ORANGE, ls="--", label=f"Lenth ME = {me:.2f}")
    axes[0].set_xlabel("|effect| on warpage (µm)")
    axes[0].set_title("Pareto of effects, 2^4 full factorial")
    axes[0].legend(frameon=False)
    m = len(vals)
    q = stats.halfnorm.ppf((np.arange(1, m + 1) - 0.5) / m)
    axes[1].scatter(q, vals, color=GREY)
    for x, y, n in zip(q, vals, names):
        if y > me:
            axes[1].annotate(n, (x, y), xytext=(4, 0), textcoords="offset points", color=BLUE)
    axes[1].plot([0, q.max()], [0, q.max() * pse], color=ORANGE, ls="--", lw=1, label="slope = PSE")
    axes[1].set_xlabel("Half-normal quantile")
    axes[1].set_ylabel("|effect|")
    axes[1].set_title("Half-normal plot: active effects fall off the line")
    axes[1].legend(frameon=False)
    save(fig, "07_full_factorial_effects.png")


def fig_bc():
    df = dk.load("full_factorial_warpage.csv")
    fact = df[df.A != 0]
    g = fact.groupby(["C", "B"]).warpage.mean().unstack()
    fig, ax = plt.subplots(figsize=(6, 3.6))
    ax.plot([-1, 1], g[-1], marker="o", color=GREY, label="B (mold temp) low, 70 °C")
    ax.plot([-1, 1], g[1], marker="o", color=BLUE, label="B (mold temp) high, 90 °C")
    ax.set_xticks([-1, 1])
    ax.set_xticklabels(["C low (60 MPa)", "C high (90 MPa)"])
    ax.set_ylabel("Mean warpage (µm)")
    ax.set_title("BC interaction: hold pressure helps less when the mold is hot")
    ax.legend(frameon=False)
    save(fig, "07_bc_interaction.png")


def fig_fractional():
    df = dk.load("fractional_flash.csv")
    eff = dk.effects_2k(df, "flash", ["A", "B", "C", "D", "E"])
    eff = {k: v for k, v in eff.items() if len(k) <= 2}
    pse, me = dk.lenth_pse(eff)
    items = sorted(eff.items(), key=lambda kv: abs(kv[1]))
    fig, ax = plt.subplots(figsize=(6, 4))
    vals = [abs(v) for _, v in items]
    ax.barh([k for k, _ in items], vals, color=[BLUE if v > me else GREY for v in vals])
    ax.axvline(me, color=ORANGE, ls="--", label=f"Lenth ME = {me:.2f}")
    ax.set_xlabel("|effect| on flash (defects per 1000)")
    ax.set_title("2^(5-1) resolution V screen: 16 runs, 5 factors")
    ax.legend(frameon=False)
    save(fig, "08_fractional_effects.png")


def fig_power():
    ns = np.arange(2, 9)
    pw = []
    for n in ns:
        df_e = 9 * (n - 1)
        se = 0.025 * np.sqrt(2 / n)
        tc = stats.t.ppf(0.975, df_e)
        nc = 0.05 / se
        pw.append(stats.nct.sf(tc, df_e, nc) + stats.nct.cdf(-tc, df_e, nc))
    fig, ax = plt.subplots(figsize=(6, 3.4))
    ax.plot(ns, pw, marker="o", color=BLUE)
    ax.axhline(0.8, color=ORANGE, ls="--", lw=1, label="80 % target")
    ax.set_xlabel("Replicates per cell (n)")
    ax.set_ylabel("Power")
    ax.set_ylim(0, 1)
    ax.set_title("Power to detect a 0.05 % gap between two cells (σ = 0.025)")
    ax.legend(frameon=False)
    save(fig, "06_power_vs_replicates.png")


if __name__ == "__main__":
    for f in (fig_crd, fig_rbd, fig_interaction, fig_power, fig_effects, fig_bc, fig_fractional):
        f()
    print("figures written to", os.path.abspath(FIG))
