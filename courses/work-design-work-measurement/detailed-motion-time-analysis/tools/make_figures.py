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
import dmtkit as dk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
COLS = ["#2b6cb0", "#dd6b20", "#2f855a", "#c53030"]


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_reach_move():
    d = np.arange(5, 81, 5)
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.6), sharey=True)
    for i, c in enumerate(dk.REACH):
        axs[0].plot(d, [dk.code_value(f"R{x}{c}")[0] for x in d], color=COLS[i], label=f"case {c}")
    for i, c in enumerate(dk.MOVE):
        axs[1].plot(d, [dk.code_value(f"M{x}{c}")[0] for x in d], color=COLS[i], label=f"case {c}")
    axs[1].plot(d, [dk.code_value(f"M{x}b/6")[0] for x in d], color=COLS[1], ls="--", label="case b, 6 kg")
    axs[0].set_title("Reach (teaching card)", fontsize=10)
    axs[1].set_title("Move (teaching card)", fontsize=10)
    for ax in axs:
        ax.set_xlabel("Distance (cm)")
        ax.legend(frameon=False, fontsize=8)
    axs[0].set_ylabel("cs (0.01 s)")
    save(fig, "04_reach_move.png")


def simo(ax, name, title):
    t = dk.lab_table(name)
    x = 0
    for _, r in t.iterrows():
        if r.lh_cs:
            ax.barh(1, r.lh_cs, left=x, color=COLS[0], edgecolor="white")
        if r.rh_cs:
            ax.barh(0, r.rh_cs, left=x if r.simultaneous else x + r.lh_cs, color=COLS[1], edgecolor="white")
        if r.LH == "H":
            ax.barh(1, r.hands_cs, left=x, color="#cbd5e0", edgecolor="white")
        if r.RH == "H":
            ax.barh(0, r.hands_cs, left=x, color="#cbd5e0", edgecolor="white")
        x += r.row_cs
    ax.set_yticks([0, 1], ["Right hand", "Left hand"])
    ax.set_xlim(0, 240)
    ax.set_title(f"{title}: {x:.0f} cs", fontsize=9)


def fig_simo():
    fig, axs = plt.subplots(2, 1, figsize=(9, 3.6), sharex=True)
    simo(axs[0], "L03_current", "Current (one hand holds)")
    simo(axs[1], "L03_improved", "Improved (fixture, both hands work)")
    axs[1].set_xlabel("cs (0.01 s); blue/orange = working, grey = holding, blank = idle")
    save(fig, "13_simo_chart.png")


if __name__ == "__main__":
    fig_reach_move()
    fig_simo()
    print("figures written:", sorted(os.listdir(FIG)))
