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
import aikit as ak  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
COL = {"Implement": "#2f855a", "Possible": "#2b6cb0", "Challenge": "#dd6b20", "Kill/park": "#a0aec0",
       "Fix process first (not AI)": "#c53030"}


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def fig_portfolio():
    u = ak.portfolio()
    fig, ax = plt.subplots(figsize=(8, 4.6))
    for k, g in u.groupby("pick"):
        ax.scatter(g.feasibility, g.annual_value_usd / 1000, s=70, color=COL[k], label=k, zorder=3)
    for i, r in u.iterrows():
        ax.annotate(f"#{i + 1}", (r.feasibility, r.annual_value_usd / 1000), xytext=(6, -3 + 6 * (i % 2)),
                    textcoords="offset points", fontsize=8)
    ax.axvline(3.0, color="#cbd5e0", ls="--")
    ax.axhline(u.annual_value_usd.median() / 1000, color="#cbd5e0", ls="--")
    ax.set_xlabel("Feasibility (data readiness, simplicity, low risk; 1-5)")
    ax.set_ylabel("Estimated annual value ($k)")
    ax.legend(frameon=False, fontsize=8, loc="upper left")
    ax.set_xlim(1.4, 5.2)
    ax.set_title("Idea numbers as in data/use_cases.csv (row order)", fontsize=9)
    save(fig, "04_pick_chart.png")


def fig_readiness():
    r = ak.ex_readiness()["dimension_scores_pct"]
    fig, ax = plt.subplots(figsize=(8, 3.4))
    names = list(r)[::-1]
    vals = [r[k] for k in names]
    ax.barh(names, vals, color=["#c53030" if v < 90 else "#2b6cb0" for v in vals])
    ax.axvline(95, color="#a0aec0", ls="--")
    ax.set_xlim(50, 100)
    ax.set_xlabel("% of records passing (dashed line: 95 % example target)")
    ax.tick_params(axis="y", labelsize=8)
    save(fig, "06_data_readiness.png")


def fig_threshold():
    p = ak.ex_predict()
    th = [r["threshold"] for r in p["thresholds"]]
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    ax.plot(th, [r["net_value_usd"] / 1000 for r in p["thresholds"]], marker="o", color="#2b6cb0", label="ML model")
    ax.axhline(p["rule_baseline"]["net_value_usd"] / 1000, color="#dd6b20", ls="--", label="Simple rule")
    ax.set_xlabel("Alert threshold (predicted probability of late)")
    ax.set_ylabel("Net value on 600 test shipments ($k)")
    ax.legend(frameon=False)
    save(fig, "03_threshold_value.png")


def fig_roi():
    r = ak.ex_roi()
    rows = r["tornado"][::-1]
    fig, ax = plt.subplots(figsize=(7.5, 3.2))
    for i, x in enumerate(rows):
        lo, hi = sorted([x["npv_low"], x["npv_high"]])
        ax.barh(i, (hi - lo) / 1000, left=lo / 1000, color="#2b6cb0")
    ax.axvline(0, color="k", lw=1)
    ax.axvline(r["npv_3yr_usd"] / 1000, color="#dd6b20", ls="--")
    ax.set_yticks(range(len(rows)), [x["factor"] for x in rows], fontsize=8)
    ax.set_xlabel("3-year NPV of invoice-matching pilot ($k)")
    save(fig, "07_roi_tornado.png")


if __name__ == "__main__":
    for f in [fig_portfolio, fig_readiness, fig_threshold, fig_roi]:
        f()
    print("figures written:", sorted(os.listdir(FIG)))
