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
import statsmodels.formula.api as smf

sys.path.insert(0, os.path.dirname(__file__))
import stmkit as sk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, RED, GREEN = "#2b6cb0", "#dd6b20", "#a0aec0", "#c53030", "#2f855a"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_sampling():
    s = sk.ex_sampling()["shares"]
    col = {"on_site_inspection": BLUE, "travel": BLUE, "report_writing": BLUE, "phone_customer": GREEN,
           "meetings_admin": GREEN, "personal": GREEN, "waiting": RED, "other_unassigned": RED}
    fig, ax = plt.subplots(figsize=(8, 3.4))
    y = np.arange(len(s))[::-1]
    ax.barh(y, [r["share"] for r in s], xerr=[r["ci95"] for r in s], color=[col[r["activity"]] for r in s],
            capsize=3)
    ax.set_yticks(y, [r["activity"] for r in s])
    ax.set_xlabel("Share of observations (±95 % CI)")
    ax.set_title("Inspector work sampling: blue = unit-driven, green = allowed indirect, red = excluded", fontsize=9)
    save(fig, "03_work_sampling.png")


def fig_availability():
    a = sk.ex_availability()["average"]
    steps = [("Paid", a["paid_hours"]), ("Holidays", -a["holidays"]), ("Annual leave", -a["annual_leave"]),
             ("Sick leave", -a["sick_leave"]), ("Training", -a["training"]), ("Other leave", -a["other_leave"])]
    fig, ax = plt.subplots(figsize=(8, 3.4))
    level = 0
    for i, (lab, v) in enumerate(steps):
        if i == 0:
            ax.bar(i, v, color=GREY)
            level = v
        else:
            ax.bar(i, -v, bottom=level + v, color=ORANGE)
            level += v
        ax.text(i, level + 20, f"{abs(v):.0f}", ha="center", fontsize=8)
    ax.bar(len(steps), level, color=BLUE)
    ax.text(len(steps), level + 20, f"{level:.0f}", ha="center", fontsize=8, color=BLUE)
    ax.set_xticks(range(len(steps) + 1), [s[0] for s in steps] + ["Available"], fontsize=8)
    ax.set_ylabel("Hours per FTE per year")
    ax.set_ylim(0, 2250)
    save(fig, "04_availability.png")


def fig_counter():
    q = sk.ex_queueing()["by_hour"]
    fig, ax = plt.subplots(figsize=(7.5, 3.4))
    x = np.arange(len(q))
    ax.bar(x, [r["load_erlangs"] for r in q], color=GREY, label="Workload (busy servers needed on average)")
    ax.step(np.append(x, x[-1] + 1) - 0.5, [r["positions"] for r in q] + [q[-1]["positions"]], where="post",
            color=BLUE, lw=2, label="Positions for 80 % served within 10 min")
    ax.set_xticks(x, [r["hour"] for r in q])
    ax.set_ylabel("Counter staff")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.set_ylim(0, 5)
    save(fig, "05_counter_positions.png")


def fig_peers():
    p = sk.load("peer_benchmark")
    r = sk.ex_ratio()
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.scatter(p.annual_inspections / 1000, p.inspector_fte, color=GREY, label="Peer agencies")
    x = np.linspace(5, 62, 50)
    ax.plot(x, r["fit"]["Intercept"] + r["fit"]["I(annual_inspections / 1000)"] * x, color=GREY)
    ours = r["our_inspections"] / 1000
    ax.errorbar(ours, r["peer_predicted_fte"], yerr=[[r["peer_predicted_fte"] - r["pi95"][0]],
                [r["pi95"][1] - r["peer_predicted_fte"]]], fmt="o", color=ORANGE, capsize=4, label="Peer-based estimate")
    ax.scatter([ours], [sk.ex_workload_model()["inspector_fte"]], marker="*", s=180, color=BLUE, zorder=4,
               label="Workload model (2025)")
    ax.scatter([ours], [21], marker="x", s=80, color=RED, zorder=4, label="On staff")
    ax.set_xlabel("Annual inspections (thousands)")
    ax.set_ylabel("Inspector FTE")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "05_peer_benchmark.png")


def fig_forecast():
    w = sk.load("workload_history")
    w = w.assign(t=np.arange(len(w)), mo=w.month.str[5:7].astype(int))
    m = smf.ols("np.log(res_inspections) ~ t + C(mo)", data=w).fit()
    f = pd.DataFrame(dict(t=np.arange(60, 96), mo=np.tile(np.arange(1, 13), 3)))
    fig, ax = plt.subplots(figsize=(9, 3.4))
    ax.plot(w.t, w.res_inspections, color=BLUE, label="Actual")
    ax.plot(w.t, np.exp(m.fittedvalues), color=GREY, ls="--", lw=1, label="Fit")
    ax.plot(f.t, np.exp(m.predict(f) + m.scale / 2), color=ORANGE, label="Forecast (base)")
    ax.set_xticks(np.arange(0, 96, 12), [str(y) for y in range(2021, 2029)])
    ax.set_ylabel("Residential inspections / month")
    ax.legend(frameon=False, fontsize=8)
    save(fig, "06_forecast.png")


def fig_supply():
    g = sk.ex_gap()
    yrs = [2026, 2027, 2028]
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.plot(yrs, [g["need"][y] for y in yrs], marker="o", color=BLUE, lw=2, label="Required (base forecast)")
    ax.plot(yrs, [r["effective"] for r in g["no_hire"]], marker="o", color=RED, label="Supply, no hiring")
    ax.plot(yrs, [r["effective"] for r in g["capped_rows"]], marker="o", color=GREEN,
            label=f"Supply, hire {g['plan_capped_4']}")
    ax.set_xticks(yrs)
    ax.set_ylabel("Effective inspector FTE")
    ax.legend(frameon=False, fontsize=8)
    ax.set_ylim(15, 30)
    save(fig, "07_supply_demand.png")


def fig_tornado():
    t = sk.ex_sensitivity()
    rows = t["tornado"][::-1]
    base = t["base_fte_2026"]
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    for i, r in enumerate(rows):
        ax.barh(i, r["high"] - base, left=base, color=ORANGE)
        ax.barh(i, r["low"] - base, left=base, color=BLUE)
    ax.axvline(base, color="k", lw=1)
    ax.set_yticks(range(len(rows)), [r["factor"] for r in rows], fontsize=8)
    ax.set_xlabel(f"Inspector FTE 2026 (base {base})")
    save(fig, "08_tornado.png")


def fig_validation():
    w = sk.monthly_requirement()
    fig, axs = plt.subplots(1, 2, figsize=(11, 3.6))
    axs[0].plot(range(60), w.required_fte, color=BLUE, label="Model: required FTE")
    axs[0].plot(range(60), w.inspectors_on_staff, color=GREY, label="On staff")
    axs[0].set_xticks(np.arange(0, 60, 12), [str(y) for y in range(2021, 2026)])
    axs[0].set_ylabel("Inspector FTE")
    axs[0].legend(frameon=False, fontsize=8)
    axs[1].scatter(w.ratio, w.next_day_inspection_pct, color=BLUE, s=16)
    axs[1].axvline(1.0, color=GREY, ls="--")
    axs[1].set_xlabel("Required ÷ on staff")
    axs[1].set_ylabel("Next-day inspection %")
    axs[1].set_title(f"r = {sk.ex_validate()['corr_ratio_service']}", fontsize=9)
    save(fig, "08_validation.png")


if __name__ == "__main__":
    for f in [fig_sampling, fig_availability, fig_counter, fig_peers, fig_forecast, fig_supply, fig_tornado,
              fig_validation]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
