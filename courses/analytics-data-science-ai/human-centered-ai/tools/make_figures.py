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
import pandas as pd

sys.path.insert(0, os.path.dirname(__file__))
import hcdkit as hk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_theme_matrix():
    n = hk.load("interview_notes").merge(hk.load("theme_key"), on="note_id")
    m = pd.crosstab(n.theme, n.person).reindex(index=list(hk.THEMES), columns=list(hk.PEOPLE), fill_value=0)
    fig, ax = plt.subplots(figsize=(10, 4.2))
    ax.imshow(m.values, cmap="Blues", vmin=0, vmax=3)
    for i in range(m.shape[0]):
        for j in range(m.shape[1]):
            if m.values[i, j]:
                ax.text(j, i, m.values[i, j], ha="center", va="center", fontsize=9)
    ax.set_xticks(range(m.shape[1]), [hk.PEOPLE[p].split(" (")[0] for p in m.columns], rotation=30, ha="right",
                  fontsize=8)
    ax.set_yticks(range(m.shape[0]), [f"{t} {hk.THEMES[t]}" for t in m.index], fontsize=8)
    ax.set_title("Notes per theme and role (breadth across roles = signal)", fontsize=10)
    save(fig, "03_theme_matrix.png")


def fig_assumptions():
    a = hk.load("assumptions")
    fig, ax = plt.subplots(figsize=(6.5, 4.4))
    ax.scatter(a.evidence, a.importance, s=120, color="#2b6cb0", zorder=3)
    for _, r in a.iterrows():
        ax.annotate(r.id, (r.evidence, r.importance), xytext=(7, 4), textcoords="offset points")
    ax.axvline(2.5, color="#cbd5e0", ls="--")
    ax.axhline(3.5, color="#cbd5e0", ls="--")
    ax.text(1.1, 5.3, "TEST FIRST", color="#c53030", fontsize=9)
    ax.text(3.6, 5.3, "proceed, monitor", color="#718096", fontsize=9)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(1, 5.6)
    ax.invert_xaxis()
    ax.set_xlabel("Evidence (5 = strong ... 1 = none)")
    ax.set_ylabel("Importance if wrong")
    save(fig, "05_assumption_map.png")


def fig_prototype():
    w = hk.load("wizard_of_oz_test")
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    data = [w[w.method == "current"].seconds, w[w.method == "prototype"].seconds]
    ax.boxplot(data, vert=False, widths=0.5)
    ax.set_yticks([1, 2], ["Current way", "Prototype (Wizard of Oz)"])
    ax.set_xlabel("Seconds to find the information (36 tasks)")
    save(fig, "05_prototype_times.png")


if __name__ == "__main__":
    for f in [fig_theme_matrix, fig_assumptions, fig_prototype]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
