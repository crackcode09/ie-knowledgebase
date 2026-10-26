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
import finkit as fk  # noqa: E402

FIG = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG, exist_ok=True)
plt.rcParams.update({"figure.dpi": 110, "axes.spines.top": False, "axes.spines.right": False, "font.size": 10})
BLUE, ORANGE, GREY, GREEN, RED = "#2b6cb0", "#dd6b20", "#a0aec0", "#2f855a", "#c53030"


def save(fig, name):
    fig.tight_layout()
    fig.savefig(os.path.join(FIG, name))
    plt.close(fig)


def waterfall(ax, labels, values, start_label=None, start=None, end_label=None):
    x, cum = 0, 0.0
    names = []
    if start is not None:
        ax.bar(x, start, color=BLUE)
        names.append(start_label)
        cum, x = start, 1
    for lab, v in zip(labels, values):
        ax.bar(x, v, bottom=cum if v >= 0 else cum + v, color=GREEN if v >= 0 else RED)
        ax.text(x, max(cum, cum + v), f"{v:+,.0f}", ha="center", va="bottom", fontsize=8)
        cum += v
        names.append(lab)
        x += 1
    if end_label:
        ax.bar(x, cum, color=BLUE)
        ax.text(x, cum, f"{cum:,.0f}", ha="center", va="bottom", fontsize=8)
        names.append(end_label)
    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, rotation=35, ha="right", fontsize=8)
    ax.axhline(0, color="black", lw=0.6)


def fig_balance_sheet():
    _, bs, _ = fk.statements()
    b = bs["Y2"]
    fig, ax = plt.subplots(figsize=(6, 4))
    assets = [("Cash", b["cash"]), ("Receivables", b["receivables"]), ("Inventory", b["inventory"]),
              ("Prepaid", b["prepaid"]), ("Net PP&E", b["ppe_net"])]
    claims = [("Payables + accrued", b["payables"] + b["accrued"]), ("Current debt", b["current_debt"]),
              ("Long-term debt", b["long_term_debt"]), ("Common stock", b["common_stock"]),
              ("Retained earnings", b["retained_earnings"])]
    cols = ["#90cdf4", "#63b3ed", "#4299e1", "#bee3f8", "#2b6cb0"]
    cols2 = ["#fbd38d", "#f6ad55", "#dd6b20", "#9ae6b4", "#2f855a"]
    for x, items, cs in ((0, assets, cols), (1, claims, cols2)):
        bottom = 0
        for (lab, v), c in zip(items, cs):
            ax.bar(x, v, bottom=bottom, color=c, width=0.6)
            ax.text(x, bottom + v / 2, f"{lab}\n{v:,}", ha="center", va="center", fontsize=7.5)
            bottom += v
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Assets", "Liabilities + equity"])
    ax.set_ylabel("$000")
    ax.set_title(f"Balance sheet, end of Y2: both sides = {b['total_assets']:,}")
    save(fig, "02_balance_sheet.png")


def fig_cash_flow():
    _, bs, cf = fk.statements()
    labels = list(cf["cfo_items"].keys()) + ["capital expenditure"] + list(cf["cff_items"].keys())
    values = list(cf["cfo_items"].values()) + [cf["CFI"]] + list(cf["cff_items"].values())
    fig, ax = plt.subplots(figsize=(8, 4))
    waterfall(ax, labels, values, "cash Y1", bs["Y1"]["cash"], "cash Y2")
    ax.set_ylabel("$000")
    ax.set_title("Where the cash went in Y2 (indirect method)")
    save(fig, "04_cash_flow_waterfall.png")


def fig_dashboard():
    inc, bs, _ = fk.statements()
    r1, r2 = fk.ratios(inc, bs, "Y1"), fk.ratios(inc, bs, "Y2")
    tiles = [("Gross margin", "gross margin %", "%"), ("EBIT margin", "operating (EBIT) margin %", "%"),
             ("ROE", "ROE % (NI / avg equity)", "%"), ("Current ratio", "current ratio", "x"),
             ("Cash conversion cycle", "cash conversion cycle (days)", " d"), ("Debt / EBITDA", "debt / EBITDA", "x"),
             ("Interest coverage", "interest coverage (EBIT / interest)", "x"), ("DSO", "DSO (days)", " d")]
    better_low = {"cash conversion cycle (days)", "debt / EBITDA", "DSO (days)"}
    fig, axes = plt.subplots(2, 4, figsize=(10, 4))
    for ax, (title, k, unit) in zip(axes.flat, tiles):
        ax.axis("off")
        v1, v2 = r1[k], r2[k]
        good = (v2 < v1) if k in better_low else (v2 > v1)
        ax.text(0.5, 0.72, title, ha="center", fontsize=10, color="#4a5568")
        ax.text(0.5, 0.38, f"{v2:,.1f}{unit}", ha="center", fontsize=18, weight="bold")
        ax.text(0.5, 0.1, f"Y1 {v1:,.1f}{unit}  {'▲' if v2 > v1 else '▼'}", ha="center", fontsize=9,
                color=GREEN if good else RED)
        ax.add_patch(plt.Rectangle((0.02, 0.0), 0.96, 0.95, fill=False, ec="#e2e8f0", transform=ax.transAxes))
    fig.suptitle("Riverbend financial dashboard, Y2 vs Y1 (green = improving)")
    save(fig, "05_dashboard.png")


def fig_budget():
    b = fk.ex_budget()
    v = b["variances (+ = favorable)"]
    short = ["sales volume", "selling price", "material", "labor rate", "labor efficiency", "var. overhead",
             "fixed overhead", "cell SG&A"]
    fig, ax = plt.subplots(figsize=(8, 4))
    waterfall(ax, short, list(v.values()), "static budget", b["static budget (10,000 units)"]["operating_profit"],
              "actual")
    ax.set_ylabel("Operating profit ($)")
    ax.set_title("Cell 7 quarter: static budget to actual operating profit")
    save(fig, "06_budget_variance_bridge.png")


def fig_loan():
    _, s = fk.loan_schedule()
    fig, ax = plt.subplots(figsize=(7, 3.6))
    ax.stackplot(s.month, s.interest, s.principal, labels=["interest", "principal"], colors=[ORANGE, BLUE])
    ax.set_xlabel("Month")
    ax.set_ylabel("$ per month")
    ax.set_title("$1.2M machine loan, 7% APR, 60 months: each payment's split")
    ax.legend(frameon=False, loc="center right")
    save(fig, "07_loan_amortization.png")


def fig_npv_profile():
    cfs, _ = fk.project_cash_flows()
    rates = np.linspace(0, 0.25, 101)
    fig, ax = plt.subplots(figsize=(6.5, 3.8))
    ax.plot(100 * rates, [fk.npv(r, cfs) / 1000 for r in rates], color=BLUE)
    ax.axhline(0, color="black", lw=0.6)
    w, i = fk.wacc(), fk.irr(cfs)
    ax.axvline(100 * w, color=GREY, ls="--")
    ax.annotate(f"WACC {100*w:.2f}%\nNPV ${fk.npv(w, cfs)/1000:,.0f}k", (100 * w, fk.npv(w, cfs) / 1000),
                xytext=(10, 10), textcoords="offset points")
    ax.annotate(f"IRR {100*i:.2f}%", (100 * i, 0), xytext=(8, 15), textcoords="offset points", color=ORANGE)
    ax.set_xlabel("Discount rate (%)")
    ax.set_ylabel("NPV ($000)")
    ax.set_title("NPV profile: 5-axis machining center")
    save(fig, "09_npv_profile.png")


def fig_tornado():
    s = fk.ex_sensitivity()
    base = s["base NPV"] / 1000
    items = dict(s["NPV low / high by driver"])
    items["discount rate 12% / 7%"] = (s["discount rate 7% / 12%"][1], s["discount rate 7% / 12%"][0])
    items = sorted(items.items(), key=lambda kv: abs(kv[1][1] - kv[1][0]))
    fig, ax = plt.subplots(figsize=(7, 3.6))
    for y, (k, (lo, hi)) in enumerate(items):
        lo, hi = lo / 1000, hi / 1000
        ax.barh(y, lo - base, left=base, color=RED)
        ax.barh(y, hi - base, left=base, color=GREEN)
    ax.axvline(base, color="black", lw=0.8)
    ax.set_yticks(range(len(items)))
    ax.set_yticklabels([k for k, _ in items])
    ax.set_xlabel("NPV ($000)")
    ax.set_title(f"Tornado: NPV swing by driver (base ${base:,.0f}k)")
    save(fig, "11_tornado.png")


def fig_monte_carlo():
    r = fk.wacc()
    rng = np.random.default_rng(2026)
    n = 10000
    sav = rng.triangular(280_000, 380_000, 440_000, n)
    cost = rng.normal(1_200_000, 60_000, n)
    lifes = rng.choice([5, 6, 7, 8], n, p=[0.1, 0.25, 0.45, 0.2])
    sims = np.array([fk.npv(r, fk.project_cash_flows(cost=c, savings=s, life=int(L))[0])
                     for c, s, L in zip(cost, sav, lifes)]) / 1000
    fig, ax = plt.subplots(figsize=(6.5, 3.6))
    ax.hist(sims, bins=60, color=BLUE, alpha=0.8)
    ax.axvline(0, color=RED, lw=1.2)
    ax.set_xlabel("NPV ($000)")
    ax.set_ylabel("Simulations")
    ax.set_title(f"Monte Carlo, 10,000 runs: P(NPV < 0) = {(sims < 0).mean():.1%}")
    save(fig, "11_monte_carlo.png")


def fig_breakeven():
    price, vc, fixed = 62.0, 28.2, 616_000
    q = np.linspace(0, 50_000, 101)
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.plot(q / 1000, price * q / 1000, color=BLUE, label="revenue")
    ax.plot(q / 1000, (fixed + vc * q) / 1000, color=ORANGE, label="total cost (current)")
    ax.plot(q / 1000, (fixed + 120_000 + 24.0 * q) / 1000, color=GREY, ls="--", label="total cost (automated)")
    be = fixed / (price - vc)
    ax.axvline(be / 1000, color=ORANGE, lw=0.8, ls=":")
    ax.axvline(40, color=GREEN, lw=0.8, ls=":")
    ax.text(be / 1000, 50, f" break-even\n {be:,.0f} units", fontsize=8)
    ax.text(40, 50, " plan\n 40,000", fontsize=8)
    ax.set_xlabel("Annual units (000)")
    ax.set_ylabel("$000")
    ax.set_title("Cell 7 break-even chart")
    ax.legend(frameon=False)
    save(fig, "12_break_even.png")


if __name__ == "__main__":
    for f in (fig_balance_sheet, fig_cash_flow, fig_dashboard, fig_budget, fig_loan, fig_npv_profile, fig_tornado,
              fig_monte_carlo, fig_breakeven):
        f()
    print("figures written to", os.path.abspath(FIG))
