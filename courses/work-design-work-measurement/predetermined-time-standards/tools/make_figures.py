"""make_figures.py - regenerate every figure in figures/.

    python tools/make_figures.py

License: MIT
"""
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(__file__))
import ptskit as pk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
COL = {"movement": "#2b6cb0", "get": "#2f855a", "put": "#dd6b20", "auxiliary": "#a0aec0", "process": "#553c9a"}


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_movements():
    mv = [(c, m) for c, k, m in pk.CARD if k == "movement"]
    labels = ["finger", "hand/wrist", "forearm", "whole arm", "extended arm", "arm + trunk"]
    vals = [int(c[1:]) for c, _ in mv]
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    ax.bar(labels, vals, color=COL["movement"])
    for i, (c, _) in enumerate(mv):
        ax.text(i, vals[i] + 0.2, c, ha="center", fontsize=9)
    ax.set_ylabel("Units (1 U = 0.1 s)")
    ax.set_title("Teaching card: movement value grows with the body member used", fontsize=10)
    save(fig, "11_movement_classes.png")


def fig_build_up():
    names = ["A_kit_current", "A_kit_improved", "C_pack_current", "C_pack_improved", "B_pin_assembly"]
    labels = ["Kit\ncurrent", "Kit\nimproved", "Pack\ncurrent", "Pack\nimproved", "Pin\nassembly"]
    fig, ax = plt.subplots(figsize=(8, 3.8))
    for i, n in enumerate(names):
        s = pk.task_summary(n)
        bottom = 0
        for k in ["movement", "get", "put", "auxiliary", "process"]:
            v = s["by_class"][k] * pk.U_SECONDS
            ax.bar(i, v, bottom=bottom, color=COL[k], label=k if i == 0 else None)
            bottom += v
        ax.text(i, bottom + 0.2, f"{bottom:.1f} s", ha="center", fontsize=9)
    ax.set_xticks(range(len(names)), labels)
    ax.set_ylabel("Normal seconds per cycle")
    ax.legend(frameon=False, fontsize=8, ncol=5, loc="upper center", bbox_to_anchor=(0.5, 1.12))
    save(fig, "20_task_build_up.png")


if __name__ == "__main__":
    fig_movements()
    fig_build_up()
    print("figures written:", sorted(os.listdir(FIG)))
