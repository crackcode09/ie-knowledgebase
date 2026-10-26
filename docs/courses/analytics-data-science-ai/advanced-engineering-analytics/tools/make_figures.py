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
import aeakit as ak  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"
LC = {"L1": BLUE, "L2": GREEN, "L3": GREY, "L4": ORANGE}


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_line_kpis():
    t = ak.analysis_table()
    g = t.groupby("line").agg(avail=("availability", "mean"), scrap=("scrap_rate", "mean"))
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.4))
    axes[0].bar(g.index, 100 * g.avail, color=[LC[l] for l in g.index])
    axes[0].set_ylim(70, 100)
    axes[0].set_title("Availability (run h / planned h), %", loc="left")
    axes[1].bar(g.index, 100 * g.scrap, color=[LC[l] for l in g.index])
    axes[1].set_title("Scrap rate, %", loc="left")
    fig.suptitle("L4 loses the most time; scrap differs less", x=0.01, ha="left", weight="bold")
    save(fig, "04_line_kpis.png")


def fig_seal_box():
    t = ak.analysis_table().dropna(subset=["seal_mean"])
    fig, ax = plt.subplots(figsize=(8, 3.8))
    pos, data, cols, labels = [], [], [], []
    for i, line in enumerate(ak.LINES):
        for j, sup in enumerate(["FilmCo", "PolyPak"]):
            data.append(t[(t.line == line) & (t.film_supplier == sup)].seal_mean)
            pos.append(i * 3 + j)
            cols.append(BLUE if sup == "FilmCo" else ORANGE)
    bp = ax.boxplot(data, positions=pos, patch_artist=True, widths=0.8)
    for b, c in zip(bp["boxes"], cols):
        b.set_facecolor(c)
        b.set_alpha(0.7)
    ax.set_xticks([i * 3 + 0.5 for i in range(4)])
    ax.set_xticklabels(ak.LINES)
    ax.axhline(ak.SPEC_MIN_SEAL, color=RED, ls="--")
    ax.text(10.5, ak.SPEC_MIN_SEAL + 0.2, "min 18 N", color=RED, fontsize=8)
    ax.set_ylabel("Run mean seal strength (N)")
    ax.legend([bp["boxes"][0], bp["boxes"][1]], ["FilmCo", "PolyPak"], frameon=False)
    ax.set_title("Seal strength by line and film supplier", loc="left", weight="bold")
    save(fig, "04_seal_by_line_supplier.png")


def fig_anova_means():
    t = ak.analysis_table().dropna(subset=["seal_mean"])
    g = t.groupby("line").seal_mean.agg(["mean", "std", "count"])
    ci = 1.96 * g["std"] / np.sqrt(g["count"])
    fig, ax = plt.subplots(figsize=(6, 3.4))
    ax.errorbar(g.index, g["mean"], yerr=ci, fmt="o", color=BLUE, capsize=5)
    ax.set_ylabel("Mean seal strength (N), 95% CI")
    ax.set_title("Line means differ (one-way ANOVA p < 0.001)", loc="left")
    save(fig, "05_anova_means.png")


def fig_regression():
    t = ak.analysis_table().dropna(subset=["seal_mean", "pressure_bar"])
    import statsmodels.formula.api as smf
    m = smf.ols("seal_mean ~ seal_temp_c + I(seal_temp_c**2) + dwell_ms + pressure_bar + C(film_supplier) + C(line)", data=t).fit()
    fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))
    axes[0].scatter(t.seal_temp_c, t.seal_mean, s=8, color=GREY, alpha=0.6)
    grid = np.linspace(t.seal_temp_c.min(), t.seal_temp_c.max(), 100)
    new = pd.DataFrame(dict(seal_temp_c=grid, dwell_ms=t.dwell_ms.mean(), pressure_bar=t.pressure_bar.mean(),
                            film_supplier="FilmCo", line="L1"))
    axes[0].plot(grid, m.predict(new), color=BLUE, lw=2, label="model (L1, FilmCo, mean dwell & pressure)")
    axes[0].set_xlabel("Seal temperature (°C)")
    axes[0].set_ylabel("Seal strength (N)")
    axes[0].set_title("Curved effect of temperature", loc="left")
    axes[0].legend(frameon=False, fontsize=8)
    axes[1].scatter(m.fittedvalues, m.resid, s=8, color=GREY)
    axes[1].axhline(0, color=ORANGE)
    axes[1].set_xlabel("Fitted (N)")
    axes[1].set_ylabel("Residual (N)")
    axes[1].set_title("Residuals: no pattern", loc="left")
    save(fig, "06_regression.png")


def fig_downtime():
    m = pd.read_csv(os.path.join(ak.D, "maintenance_log.csv"))
    b = m[m.type == "breakdown"]
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    for i, line in enumerate(ak.LINES):
        y = b[b.line == line].downtime_min
        ax.scatter(np.full(len(y), i) + np.random.default_rng(i).uniform(-0.15, 0.15, len(y)), y, color=LC[line], s=18)
        ax.plot([i - 0.25, i + 0.25], [y.median()] * 2, color="black", lw=2)
    ax.set_yscale("log")
    ax.set_xticks(range(4))
    ax.set_xticklabels(ak.LINES)
    ax.set_ylabel("Breakdown downtime (min, log)")
    ax.set_title("Skewed downtime: compare medians (bars), not means", loc="left")
    save(fig, "07_downtime_by_line.png")


def fig_doe():
    d = pd.read_csv(os.path.join(ak.D, "seal_doe.csv"))
    g = d.groupby(["B_dwell", "A_temp"]).seal_strength_n.mean().unstack()
    fig, axes = plt.subplots(1, 2, figsize=(9, 3.4))
    for f, ax_i in (("A_temp", 0), ("B_dwell", 0), ("C_pressure", 0)):
        mm = d.groupby(f).seal_strength_n.mean()
        axes[0].plot([-1, 1], mm.values, marker="o", label=f)
    axes[0].set_xticks([-1, 1])
    axes[0].set_title("Main effects", loc="left")
    axes[0].set_ylabel("Mean seal strength (N)")
    axes[0].legend(frameon=False, fontsize=8)
    axes[1].plot([-1, 1], g.loc[-1].values, marker="o", color=GREY, label="dwell low (800 ms)")
    axes[1].plot([-1, 1], g.loc[1].values, marker="o", color=BLUE, label="dwell high (1000 ms)")
    axes[1].set_xticks([-1, 1])
    axes[1].set_xticklabels(["temp 160 °C", "temp 170 °C"])
    axes[1].set_title("Temp × dwell interaction", loc="left")
    axes[1].legend(frameon=False, fontsize=8)
    save(fig, "08_doe_effects.png")


def fig_prediction():
    r = ak.ex_predict_strength()
    keys = [k for k in r if k.endswith("CV RMSE (N)")]
    fig, ax = plt.subplots(figsize=(7.5, 3.6))
    vals = [r[k] for k in keys]
    ax.barh([k.replace(": CV RMSE (N)", "") for k in keys][::-1], vals[::-1], color=[BLUE] * len(keys))
    ax.axvline(r["noise floor: lab SD / sqrt(3)"], color=RED, ls="--", label="measurement noise floor")
    ax.set_xlabel("Cross-validated RMSE (N), lower is better")
    ax.set_title("Improving prediction accuracy: seal strength", loc="left", weight="bold")
    ax.legend(frameon=False)
    save(fig, "09_prediction_ladder.png")


if __name__ == "__main__":
    for f in (fig_line_kpis, fig_seal_box, fig_anova_means, fig_regression, fig_downtime, fig_doe, fig_prediction):
        f()
    print("figures written to", os.path.abspath(FIG))
