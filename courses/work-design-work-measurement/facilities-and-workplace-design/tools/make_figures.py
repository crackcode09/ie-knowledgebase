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
import fwdkit as fk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"
RCOL = {"A": RED, "E": ORANGE, "I": GREEN, "O": BLUE, "X": "k"}
RW = {"A": 4, "E": 3, "I": 2, "O": 1, "X": 1.5}


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_pq():
    p = fk.load("products").sort_values("annual_units", ascending=False).reset_index(drop=True)
    fig, ax = plt.subplots(figsize=(8.5, 3.4))
    cols = {"F1 wall box": BLUE, "F2 floor cabinet": ORANGE, "F3 junction box": GREEN, "F4 custom": GREY}
    ax.bar(range(len(p)), p.annual_units, color=[cols[f] for f in p.family])
    ax2 = ax.twinx()
    ax2.plot(range(len(p)), 100 * p.annual_units.cumsum() / p.annual_units.sum(), color="k", lw=1)
    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Cumulative %")
    ax.set_xticks([])
    ax.set_xlabel("40 SKUs, highest volume first")
    ax.set_ylabel("Units per year")
    for f, c in cols.items():
        ax.bar([0], [0], color=c, label=f)
    ax.legend(frameon=False, fontsize=8)
    save(fig, "03_pq_curve.png")


def draw_layout(ax, L, title):
    F = fk.flow_matrix()
    for d, (c, r) in L.items():
        ax.add_patch(plt.Rectangle((c * fk.SLOT_W, r * fk.SLOT_H), fk.SLOT_W, fk.SLOT_H, fill=False, lw=1))
        x, y = fk.centre((c, r))
        ax.text(x, y + 3.5, d, ha="center", fontsize=9, weight="bold")
    mx = F.values.max()
    for a in fk.DEPTS:
        for b in fk.DEPTS:
            f = F.loc[a, b]
            if f > 0:
                (x1, y1), (x2, y2) = fk.centre(L[a]), fk.centre(L[b])
                ax.annotate("", (x2, y2), (x1, y1), arrowprops=dict(arrowstyle="->", lw=0.5 + 4 * f / mx,
                                                                      color=BLUE, alpha=0.6))
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 40)
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title, fontsize=9)
    ax.text(-1, 20, "receiving dock", rotation=90, va="center", ha="right", fontsize=7)
    ax.text(51, 20, "shipping dock", rotation=90, va="center", ha="left", fontsize=7)


def fig_layouts():
    lay = fk.ex_layout()
    new, _ = fk.improve(fk.AS_IS)
    fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
    draw_layout(axs[0], fk.AS_IS, f"As-is: {lay['as_is_load_m']:,} load-m/yr, {lay['as_is_backtracks']} backtracks")
    draw_layout(axs[1], new, f"Improved: {lay['improved_load_m']:,} load-m/yr, {lay['improved_backtracks']} backtracks")
    save(fig, "08_layouts.png")


def fig_affinity():
    rating, _ = fk.closeness()
    n = len(fk.DEPTS)
    pos = {d: (math.cos(2 * math.pi * i / n), math.sin(2 * math.pi * i / n)) for i, d in enumerate(fk.DEPTS)}
    fig, ax = plt.subplots(figsize=(6, 6))
    for (a, b), r in rating.items():
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.plot([x1, x2], [y1, y2], color=RCOL[r], lw=RW[r], ls="--" if r == "X" else "-", alpha=0.8)
    for d, (x, y) in pos.items():
        ax.scatter([x], [y], s=900, color="white", edgecolor="k", zorder=3)
        ax.text(x, y, d, ha="center", va="center", fontsize=8, zorder=4)
    for r in ["A", "E", "I", "O", "X"]:
        ax.plot([], [], color=RCOL[r], lw=RW[r], ls="--" if r == "X" else "-", label=r)
    ax.legend(frameon=False, title="Closeness", loc="lower right", fontsize=8)
    ax.set_aspect("equal")
    ax.axis("off")
    save(fig, "07_relationship_diagram.png")


def fig_roc():
    M = fk.load("part_machine_matrix").set_index("part")
    R = fk.roc(M)
    fig, axs = plt.subplots(1, 2, figsize=(9, 3.8))
    for ax, X, t in [(axs[0], M, "Before (as listed)"), (axs[1], R, "After rank order clustering")]:
        ax.imshow(X.values, cmap="Blues", vmin=0, vmax=1.3)
        ax.set_xticks(range(X.shape[1]), X.columns, fontsize=8, rotation=45)
        ax.set_yticks(range(X.shape[0]), X.index, fontsize=8)
        ax.set_title(t, fontsize=9)
    save(fig, "09_rank_order_clustering.png")


def fig_cell():
    c = fk.ex_cell_capacity()
    b = fk.ex_balance()
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.6))
    ops = [o for o in c["ops"] if o["capacity_per_yr"]]
    axs[0].bar([o["op"] for o in ops], [o["s_per_pc"] for o in ops], color=BLUE)
    axs[0].axhline(c["takt_s"], color=RED, ls="--")
    axs[0].text(0, c["takt_s"] + 2, f"takt {c['takt_s']} s", color=RED, fontsize=8)
    axs[0].set_ylabel("Machine-occupied s / piece")
    axs[0].set_title("Machine capacity vs takt (2 shifts)", fontsize=9)
    axs[1].bar([f"Operator {i + 1}\n{', '.join(a)}" for i, a in enumerate(b["assignment"])], b["loads_s"], color=GREEN)
    axs[1].axhline(b["takt_s"], color=RED, ls="--")
    axs[1].set_ylabel("Manual + walking s / cycle")
    axs[1].set_title(f"Operator balance ({b['balance_efficiency_pct']} % efficiency)", fontsize=9)
    save(fig, "11_cell_capacity_balance.png")


if __name__ == "__main__":
    for f in [fig_pq, fig_layouts, fig_affinity, fig_roc, fig_cell]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
