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
import edmkit as ek  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
COL = {"A": "#a0aec0", "B": "#2b6cb0", "C": "#dd6b20", "D": "#2f855a"}


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_cdf():
    s = ek.npv_samples()
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    for a, v in s.items():
        x = np.sort(v)
        ax.plot(x, np.arange(1, len(x) + 1) / len(x), color=COL[a], lw=2, label=f"{a} {ek.ALTS[a]}")
    ax.axvline(0, color="k", lw=0.8)
    ax.set_xlabel("NPV ($M)")
    ax.set_ylabel("Cumulative probability")
    ax.set_title("A curve that stays to the right dominates (first order)", fontsize=10)
    ax.legend(frameon=False, fontsize=8)
    save(fig, "04_npv_cdfs.png")


def fig_utility():
    R = np.geomspace(1, 400, 120)
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot(R, [ek.ce("C", r) for r in R], color=COL["C"], label="C linear motor")
    ax.plot(R, [ek.ce("B", r) for r in R], color=COL["B"], label="B ball screw")
    ax.axhline(ek.emv("C"), color=COL["C"], ls=":", lw=1)
    ax.axhline(ek.emv("B"), color=COL["B"], ls=":", lw=1)
    ax.set_xscale("log")
    ax.set_xlabel("Risk tolerance R ($M)")
    ax.set_ylabel("Certainty equivalent ($M)")
    ax.legend(frameon=False, fontsize=8)
    ax.set_title(f"C is preferred only above R = ${ek.ex_utility()['switch_R_$M']} M", fontsize=10)
    save(fig, "04_certainty_equivalents.png")


def fig_roc():
    v = ek.load("vibration")
    th = np.linspace(0.5, 5.5, 300)
    tpr = [((v.rms >= t) & (v.failing == 1)).sum() / (v.failing == 1).sum() for t in th]
    fpr = [((v.rms >= t) & (v.failing == 0)).sum() / (v.failing == 0).sum() for t in th]
    r = ek.ex_roc()
    fig, ax = plt.subplots(figsize=(4.6, 4.4))
    ax.plot(fpr, tpr, color=COL["B"])
    ax.plot([0, 1], [0, 1], color="#cbd5e0", ls="--")
    ax.scatter([r["FPR"]], [r["TPR"]], color=COL["C"], zorder=3)
    ax.annotate(f"threshold {r['best_threshold']} mm/s\n(lowest expected cost)", (r["FPR"], r["TPR"]),
                xytext=(0.3, 0.55), fontsize=8, arrowprops=dict(arrowstyle="->"))
    ax.set_xlabel("False alarm rate (FPR)")
    ax.set_ylabel("Detection rate (TPR)")
    ax.set_title(f"ROC curve, AUC = {r['auc']}", fontsize=10)
    save(fig, "08_roc_curve.png")


def fig_tornado():
    t = ek.ex_sensitivity()
    rows = t["tornado"][::-1]
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    for i, r in enumerate(rows):
        lo, hi = sorted([r["low"], r["high"]])
        ax.barh(i, hi - lo, left=lo, color=COL["B"])
    ax.axvline(0, color="k", lw=1)
    ax.axvline(t["EMV_C_minus_B"], color=COL["C"], ls="--")
    ax.set_yticks(range(len(rows)), [r["input"] for r in rows], fontsize=8)
    ax.set_xlabel("EMV(C) - EMV(B), $M  (left of 0: choose B)")
    save(fig, "09_tornado.png")


def fig_secretary():
    n = 20
    k = np.arange(1, n)
    # exact probability of choosing the best with cutoff k (reject first k)
    p = [k_ / n * sum(1 / (i - 1) for i in range(k_ + 1, n + 1)) for k_ in k]
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot(k, p, marker="o", ms=3, color=COL["B"])
    ax.axvline(n / np.e, color=COL["C"], ls="--")
    ax.set_xlabel("Candidates observed and rejected first (k)")
    ax.set_ylabel("P(choose the best)")
    ax.set_title("Secretary problem, n = 20", fontsize=10)
    save(fig, "06_secretary.png")


if __name__ == "__main__":
    for f in [fig_cdf, fig_utility, fig_roc, fig_tornado, fig_secretary]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
