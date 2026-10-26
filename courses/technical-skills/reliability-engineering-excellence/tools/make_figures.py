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
from scipy import stats

sys.path.insert(0, os.path.dirname(__file__))
import relkit as rk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, GREEN, RED = "#2b6cb0", "#dd6b20", "#a0aec0", "#2f855a", "#c53030"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_bathtub():
    t = np.linspace(0.01, 10, 400)
    h = 0.75 * np.exp(-t / 0.7) + 0.15 + 0.03 * np.clip(t - 6.5, 0, None) ** 2
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    ax.plot(t, h, color=BLUE, lw=2)
    ax.set_ylim(0, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("Age")
    ax.set_ylabel("Failure rate (hazard)")
    for x, txt in ((0.6, "Infant mortality\n(β < 1)"), (4.0, "Random failures\n(β ≈ 1)"), (8.6, "Wear-out\n(β > 1)")):
        ax.text(x, 1.0, txt, ha="center", fontsize=9)
    ax.set_title("The classic 'bathtub' curve: one of several real failure patterns", loc="left")
    save(fig, "00_bathtub.png")


def fig_pareto():
    w = rk.load("work_orders.csv")
    s = w.groupby("asset").downtime_h.sum().sort_values(ascending=False)
    cum = 100 * s.cumsum() / s.sum()
    fig, ax = plt.subplots(figsize=(7.5, 3.8))
    ax.bar(range(len(s)), s.values, color=[BLUE, BLUE] + [GREY] * (len(s) - 2))
    ax.set_xticks(range(len(s)))
    ax.set_xticklabels([n.replace(" ", "\n") for n in s.index], fontsize=9)
    ax.set_ylabel("Downtime (h), 12 months")
    ax2 = ax.twinx()
    ax2.plot(range(len(s)), cum.values, color=ORANGE, marker="o")
    ax2.set_ylim(0, 105)
    ax2.set_ylabel("Cumulative %")
    ax2.spines["top"].set_visible(False)
    ax.set_title("Line A downtime: spindle and press make 74%", loc="left", weight="bold")
    save(fig, "05_downtime_pareto.png")


def fig_hazards():
    t = np.linspace(1, 15000, 400)
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    for b, c in ((0.6, GREEN), (1.0, GREY), (1.81, BLUE), (3.5, RED)):
        e = 8000
        h = (b / e) * (t / e) ** (b - 1) * 1000
        ax.plot(t, h, color=c, label=f"β = {b}")
    ax.set_ylim(0, 0.6)
    ax.set_xlabel("Operating hours")
    ax.set_ylabel("Hazard (failures per 1,000 h)")
    ax.set_title("Weibull shape β sets the failure pattern (η = 8,000 h)", loc="left")
    ax.legend(frameon=False)
    save(fig, "06_weibull_hazards.png")


def fig_weibull_plot():
    d = rk.load("spindle_bearing_life.csv")
    f = (d.status == "F").values
    b, e = rk.weibull_mle(d.hours.values, f)
    mr = rk.median_ranks(d.hours.values, f)
    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    ax.scatter(np.log(mr[:, 0]), np.log(-np.log(1 - mr[:, 1])), color=BLUE, zorder=3, label="failures (adjusted median ranks)")
    tt = np.linspace(800, 20000, 100)
    ax.plot(np.log(tt), b * (np.log(tt) - np.log(e)), color=ORANGE, label=f"MLE fit: β = {b:.2f}, η = {e:,.0f} h")
    for t_s in d.hours[~f]:
        ax.axvline(np.log(t_s), ymin=0, ymax=0.04, color=GREY)
    yt = [0.01, 0.05, 0.1, 0.2, 0.5, 0.632, 0.9, 0.99]
    ax.set_yticks([np.log(-np.log(1 - p)) for p in yt])
    ax.set_yticklabels([f"{100*p:g}%" for p in yt])
    xt = [1000, 2000, 5000, 10000, 20000]
    ax.set_xticks(np.log(xt))
    ax.set_xticklabels([f"{x:,}" for x in xt])
    ax.axhline(np.log(-np.log(0.9)), color=GREY, ls=":", lw=0.8)
    b10 = e * (-math.log(0.9)) ** (1 / b)
    ax.annotate(f"B10 ≈ {b10:,.0f} h", (np.log(b10), np.log(-np.log(0.9))), xytext=(-90, 12), textcoords="offset points")
    ax.set_xlabel("Operating hours (log scale); grey ticks = suspensions")
    ax.set_ylabel("Unreliability F(t)")
    ax.set_title("Weibull plot: spindle bearings (12 failures, 12 suspensions)", loc="left")
    ax.legend(frameon=False, loc="lower right", fontsize=8)
    save(fig, "06_weibull_plot.png")


def fig_normal():
    w = rk.load("grinding_wheel_life.csv")
    mu, sd = w.parts.mean(), w.parts.std(ddof=1)
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    ax.hist(w.parts, bins=10, density=True, color=GREY, edgecolor="white")
    x = np.linspace(mu - 4 * sd, mu + 4 * sd, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sd), color=BLUE)
    cp = stats.norm.ppf(0.01, mu, sd)
    ax.axvline(cp, color=RED, ls="--")
    ax.text(cp, ax.get_ylim()[1] * 0.9, f" change at {cp:,.0f} parts\n (1% risk)", color=RED, fontsize=8)
    ax.set_yticks([])
    ax.set_xlabel("Grinding-wheel life (parts)")
    ax.set_title("Normal wear-out: set the change point from the left tail", loc="left")
    save(fig, "05_wheel_life_normal.png")


def fig_pm():
    d = rk.load("spindle_bearing_life.csv")
    b, e = rk.weibull_mle(d.hours.values, (d.status == "F").values)
    T = np.linspace(800, 14000, 200)
    c = [rk.age_replacement_cost_rate(t, b, e, 4000, 22000) for t in T]
    rtf = 22000 / (e * math.gamma(1 + 1 / b))
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.plot(T, c, color=BLUE, label="replace at age T or at failure")
    ax.axhline(rtf, color=RED, ls="--", label=f"run to failure: ${rtf:.2f}/h")
    opt = rk.ex_pm()
    To, co = opt["optimum replacement age (h)"], opt["cost per h at optimum"]
    ax.scatter(To, co, color=ORANGE, zorder=3)
    ax.annotate(f"optimum ≈ {To:,.0f} h, ${co:.2f}/h", (To, co), xytext=(10, -25), textcoords="offset points")
    ax.set_ylim(1.5, 4)
    ax.set_xlabel("Planned replacement age T (operating hours)")
    ax.set_ylabel("Cost per operating hour ($)")
    ax.set_title("Spindle bearing: age-replacement cost curve", loc="left")
    ax.legend(frameon=False)
    save(fig, "09_pm_cost_curve.png")


def fig_pf():
    t = np.linspace(0, 10, 200)
    cond = 1 - 0.012 * np.clip(t - 4, 0, None) ** 2.6
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.plot(t, cond, color=BLUE, lw=2)
    p_t, f_t = 4.6, 9.0
    ax.scatter([p_t, f_t], [np.interp(p_t, t, cond), np.interp(f_t, t, cond)], color=[ORANGE, RED], zorder=3)
    ax.annotate("P: potential failure\ndetectable (vibration)", (p_t, np.interp(p_t, t, cond)), xytext=(-110, -40),
                textcoords="offset points", fontsize=8)
    ax.annotate("F: functional failure", (f_t, np.interp(f_t, t, cond)), xytext=(-130, 15), textcoords="offset points", fontsize=8)
    ax.annotate("", (f_t, 1.06), (p_t, 1.06), arrowprops=dict(arrowstyle="<->"))
    ax.text((p_t + f_t) / 2, 1.08, "P-F interval", ha="center", fontsize=9)
    ax.set_ylim(0.2, 1.2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("Time")
    ax.set_ylabel("Equipment condition")
    ax.set_title("The P-F curve: inspect often enough to catch P before F", loc="left")
    save(fig, "10_pf_curve.png")


def fig_lcc():
    rate, years = 0.09, 10
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    for name, init, annual, c in (("A standard", 20000, 24027, GREY), ("B premium sealed", 33500, 11700, BLUE)):
        cum = [init]
        for y in range(1, years + 1):
            cum.append(cum[-1] + annual / (1 + rate) ** y)
        ax.plot(range(years + 1), np.array(cum) / 1000, marker="o", ms=3, color=c, label=name)
    ax.set_xlabel("Year")
    ax.set_ylabel("Cumulative PV of cost ($000)")
    ax.set_title("Coolant pump life-cycle cost: the cheaper pump costs more", loc="left")
    ax.legend(frameon=False)
    save(fig, "07_lcc.png")


def fig_optimum():
    R = np.linspace(0.80, 0.995, 400)
    prev = 4000 / (1 - R) ** 0.6 - 4000
    fail = 900000 * (1 - R)
    tot = prev + fail
    i = int(np.argmin(tot))
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.plot(R, prev / 1000, color=GREEN, label="reliability effort")
    ax.plot(R, fail / 1000, color=RED, label="expected failure cost")
    ax.plot(R, tot / 1000, color=BLUE, lw=2, label="total")
    ax.axvline(R[i], color=GREY, ls=":")
    ax.text(R[i], tot[i] / 1000 + 20, f"optimum R ≈ {R[i]:.3f}", ha="center", fontsize=9)
    ax.set_ylim(0, 200)
    ax.set_xlabel("Target reliability (annual, illustrative)")
    ax.set_ylabel("$000 per year")
    ax.set_title("Optimum reliability cost (illustrative model)", loc="left")
    ax.legend(frameon=False)
    save(fig, "07_optimum_reliability.png")


def fig_growth():
    g = rk.load("gearmotor_growth_test.csv")
    t = g.cumulative_hours.values.astype(float)
    n = np.arange(1, len(t) + 1)
    r = rk.ex_growth()
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.loglog(t, n, "o", color=BLUE, ms=4, label="cumulative failures")
    tt = np.linspace(t.min(), 2000, 100)
    ax.loglog(tt, r["lambda"] * tt ** r["beta (growth if < 1)"], color=ORANGE,
              label=f"Crow-AMSAA fit, β = {r['beta (growth if < 1)']:.2f}")
    ax.set_xlabel("Cumulative test hours")
    ax.set_ylabel("Cumulative failures")
    ax.set_title("Reliability growth: slope < 1 means failures are coming less often", loc="left")
    ax.legend(frameon=False)
    save(fig, "02_reliability_growth.png")


def fig_risk_matrix():
    a = rk.load("asset_register.csv")
    a["consequence"] = a[["production_impact", "quality_impact", "repair_cost", "safety_environment"]].max(axis=1)
    fig, ax = plt.subplots(figsize=(6.5, 4.6))
    for i in range(1, 6):
        for j in range(1, 6):
            s = i * j
            col = "#c6f6d5" if s <= 6 else "#fefcbf" if s <= 12 else "#fed7d7"
            ax.add_patch(plt.Rectangle((i - 0.5, j - 0.5), 1, 1, color=col, ec="white"))
    offsets = {}
    for _, r in a.iterrows():
        key = (r.failure_frequency, r.consequence)
        k = offsets.get(key, 0)
        offsets[key] = k + 1
        ax.text(r.failure_frequency, r.consequence + 0.25 - 0.22 * k, r.asset, ha="center", fontsize=7)
    ax.set_xlim(0.5, 5.5)
    ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Failure frequency (1 = rare, 5 = frequent)")
    ax.set_ylabel("Worst consequence (1-5)")
    ax.set_title("Line A risk matrix (green low, yellow medium, red high)", loc="left")
    save(fig, "01_risk_matrix.png")


if __name__ == "__main__":
    for f in (fig_bathtub, fig_risk_matrix, fig_growth, fig_pareto, fig_normal, fig_hazards, fig_weibull_plot,
              fig_lcc, fig_optimum, fig_pm, fig_pf):
        f()
    print("figures written to", os.path.abspath(FIG))
