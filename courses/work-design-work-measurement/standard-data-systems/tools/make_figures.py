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
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import sdskit as sk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_micro_macro():
    mi, ma = sk.ex_micro(), sk.ex_macro()
    parts = [("Load blank", mi["load_blank_s"]), ("3 re-positions", 3 * mi["reposition_per_bend_s"]),
             ("Flip", mi["flip_s"]), ("Angle check", mi["angle_check_s"]), ("Unload, aside", mi["unload_s"]),
             ("Ram, 4 bends", 4 * mi["ram_s_per_bend_assumed"])]
    fig, ax = plt.subplots(figsize=(8, 2.8))
    left = 0
    colors = [BLUE, BLUE, BLUE, BLUE, BLUE, GREY]
    for (lab, v), c in zip(parts, colors):
        ax.barh(1, v, left=left, color=c, edgecolor="white")
        if v >= 4:
            ax.text(left + v / 2, 1, f"{lab}\n{v:.1f}s", ha="center", va="center", fontsize=7, color="white")
        left += v
    ax.barh(0, ma["run_normal_min_pc"] * 60, color=ORANGE)
    ax.text(ma["run_normal_min_pc"] * 60 / 2, 0, f"Macro formula: {ma['run_normal_min_pc'] * 60:.1f} s", ha="center",
            va="center", color="white")
    ax.set_yticks([0, 1], ["Macroscopic\n(regression)", "Microscopic\n(motion build)"])
    small = ", ".join(f"{lab} {v:.1f}s" for lab, v in parts if v < 4)
    ax.set_xlabel(f"Normal seconds per piece (4 bends, 1 flip, 1.2 kg, 400 mm)\nUnlabelled segments: {small}")
    ax.set_title(f"Micro build {left:.1f} s vs macro {ma['run_normal_min_pc'] * 60:.1f} s")
    save(fig, "01_micro_vs_macro.png")


def fig_consistency():
    a = sk.load("analyst_consistency")
    c = sk.ex_consistency()["jobs"]
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    marks = {"Analyst 1": "o", "Analyst 2": "s", "Analyst 3": "^"}
    for an, g in a.groupby("analyst"):
        x = np.arange(len(g))
        ax.scatter(x, g.normal_min, marker=marks[an], label=an, color=GREY, edgecolor="k", zorder=3)
    ax.scatter(np.arange(len(c)), [r["formula"] for r in c], marker="_", s=600, color=ORANGE, lw=3,
               label="Standard-data formula", zorder=4)
    ax.set_xticks(np.arange(len(c)), [r["job"] for r in c])
    ax.set_ylabel("Normal min / piece")
    ax.set_title("Same jobs, three time studies vs one formula")
    ax.legend(fontsize=8, frameon=False)
    save(fig, "03_analyst_consistency.png")


def fig_economics():
    e = sk.ex_economics()
    yrs = np.linspace(0, 3, 37)
    ts = e["time_study_h_per_yr"] * yrs
    sd = e["development_h"] + e["standard_data_h_per_yr"] * yrs
    fig, ax = plt.subplots(figsize=(7, 3.4))
    ax.plot(yrs * 12, ts, color=GREY, lw=2, label="Time-study every new part")
    ax.plot(yrs * 12, sd, color=BLUE, lw=2, label="Build + use standard data")
    ax.axvline(e["payback_months"], color=ORANGE, ls="--")
    ax.text(e["payback_months"] + 0.5, ts[-1] * 0.8, f"payback ≈ {e['payback_months']} months", color=ORANGE)
    ax.set_xlabel("Months")
    ax.set_ylabel("Cumulative analyst hours")
    ax.legend(frameon=False)
    save(fig, "04_economics.png")


def fig_scatter():
    b = sk.brake()
    fig, axs = plt.subplots(1, 4, figsize=(11, 3), sharey=True)
    for ax, c in zip(axs, ["bends", "flips", "weight_kg", "length_mm"]):
        r = np.corrcoef(b[c], b.normal_min)[0, 1]
        ax.scatter(b[c], b.normal_min, s=14, color=BLUE)
        ax.set_xlabel(c)
        ax.set_title(f"r = {r:.2f}", fontsize=9)
    axs[0].set_ylabel("Normal min / piece")
    save(fig, "06_scatter_panels.png")


def fig_models():
    rows = sk.ex_models()["comparison"]
    fig, ax = plt.subplots(figsize=(7, 3.2))
    x = np.arange(len(rows))
    ax.bar(x - 0.18, [r["se_min"] for r in rows], 0.36, color=GREY, label="Std error (fit)")
    ax.bar(x + 0.18, [r["loocv_rmse"] for r in rows], 0.36, color=BLUE, label="Leave-one-out RMSE")
    ax.set_xticks(x, [r["model"] for r in rows], fontsize=8)
    ax.set_ylabel("Normal min")
    ax.set_title("Each added variable must earn its place (M5 does not)")
    ax.legend(frameon=False)
    save(fig, "07_model_ladder.png")


def fig_transform():
    h = sk.load("shear_handling_studies")
    t = sk.ex_transform()
    w = np.linspace(0.25, h.blank_kg.max() * 1.05, 200)
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.4))
    axs[0].scatter(h.blank_kg, h.normal_min, color=BLUE, s=16)
    axs[0].plot(w, t["linear"]["Intercept"] + t["linear"]["blank_kg"] * w, color=GREY, label="linear")
    axs[0].plot(w, t["power_a"] * w ** t["power_b"], color=ORANGE, label=f"power: {t['power_a']}·kg^{t['power_b']}")
    axs[0].set_xlabel("Blank weight (kg)")
    axs[0].set_ylabel("Normal min")
    axs[0].legend(frameon=False, fontsize=8)
    axs[1].scatter(np.log(h.blank_kg), np.log(h.normal_min), color=BLUE, s=16)
    m = smf.ols("np.log(normal_min) ~ np.log(blank_kg)", data=h).fit()
    lw = np.log(w)
    axs[1].plot(lw, m.params.iloc[0] + m.params.iloc[1] * lw, color=ORANGE)
    axs[1].set_xlabel("ln(weight)")
    axs[1].set_ylabel("ln(normal min)")
    axs[1].set_title("Straight line after log-log transform", fontsize=9)
    save(fig, "07_transform.png")


def fig_residuals():
    raw = smf.ols("normal_min ~ bends + flips + weight_kg + length_mm", data=sk.brake(corrected=False)).fit()
    fix = sk.run_model()
    b0 = sk.brake(corrected=False)
    fig, axs = plt.subplots(1, 3, figsize=(11, 3.3))
    sr = raw.get_influence().resid_studentized_external
    axs[0].scatter(raw.fittedvalues, sr, s=14, color=BLUE)
    i = int(np.argmax(np.abs(sr)))
    axs[0].scatter(raw.fittedvalues.iloc[i], sr[i], s=120, facecolors="none", edgecolors=RED, lw=2)
    axs[0].annotate(b0.study.iloc[i], (raw.fittedvalues.iloc[i], sr[i]), xytext=(8, -4), textcoords="offset points",
                    color=RED)
    axs[0].axhline(3, color=GREY, ls="--")
    axs[0].axhline(-3, color=GREY, ls="--")
    axs[0].set_title("Before: studentized residuals", fontsize=9)
    axs[0].set_xlabel("Fitted")
    sr2 = fix.get_influence().resid_studentized_external
    axs[1].scatter(fix.fittedvalues, sr2, s=14, color=GREEN)
    axs[1].axhline(0, color=GREY)
    axs[1].axhline(3, color=GREY, ls="--")
    axs[1].axhline(-3, color=GREY, ls="--")
    axs[1].set_title("After correcting S27", fontsize=9)
    axs[1].set_xlabel("Fitted")
    (osm, osr), (sl, ic, _) = stats.probplot(fix.resid, dist="norm")
    axs[2].scatter(osm, osr, s=14, color=GREEN)
    axs[2].plot(osm, sl * osm + ic, color=GREY)
    axs[2].set_title("Normal probability plot (after)", fontsize=9)
    axs[2].set_xlabel("Theoretical quantile")
    save(fig, "08_residuals.png")


def fig_validation():
    v = sk.ex_validate()["jobs"]
    a = np.array([r["normal_min"] for r in v])
    p = np.array([r["pred"] for r in v])
    fig, ax = plt.subplots(figsize=(4.8, 4.4))
    lim = np.array([0.3, 2.2])
    ax.fill_between(lim, lim * 0.9, lim * 1.1, color=GREY, alpha=0.3, label="±10%")
    ax.plot(lim, lim, color=GREY)
    ax.scatter(a, p, color=BLUE, zorder=3)
    for r in v:
        if abs(r["err_pct"]) > 8:
            ax.annotate(f"{r['study']} {r['err_pct']:+.0f}%", (r["normal_min"], r["pred"]), xytext=(6, -4),
                        textcoords="offset points", fontsize=8, color=RED)
    ax.set_xlabel("Hold-out time study (normal min)")
    ax.set_ylabel("Formula (normal min)")
    ax.set_title("Validation on 12 new jobs", fontsize=10)
    ax.legend(frameon=False, loc="upper left")
    save(fig, "08_validation.png")


def fig_lot_size():
    c = sk.ex_apply()["lot_size_curve"]
    fig, ax = plt.subplots(figsize=(6.5, 3.2))
    ax.plot([r["qty"] for r in c], [r["std_min_per_pc"] for r in c], marker="o", color=BLUE)
    ax.set_xscale("log")
    ax.set_xticks([5, 10, 25, 50, 100, 200], ["5", "10", "25", "50", "100", "200"])
    ax.set_xlabel("Lot quantity")
    ax.set_ylabel("Standard min / piece")
    ax.set_title("Job W01: setup share falls as the lot grows", fontsize=10)
    save(fig, "09_lot_size.png")


if __name__ == "__main__":
    for f in [fig_micro_macro, fig_consistency, fig_economics, fig_scatter, fig_models, fig_transform, fig_residuals,
              fig_validation, fig_lot_size]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
