"""finkit.py - data and calculations for the Financial Management for Engineers course.

Running case: Riverbend Motion Components, Inc. (fictional), a maker of linear-motion
parts, and its Cell 7 precision-machining profit center. Every number is illustrative.

    python tools/finkit.py data        # (re)write data/*.csv
    python tools/finkit.py all         # every worked example
    python tools/finkit.py <name>      # statements, cashflow, ratios, budget, tvm, loan, capital,
                                       # wacc, invest, leasebuy, sensitivity, eac, breakeven, valuation,
                                       # merger, startup

Requires numpy, scipy, pandas. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
from scipy.optimize import brentq

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
TAX = 0.25  # illustrative combined income-tax rate; use your own jurisdiction's rate


# ---------------------------------------------------------------- core finance functions
def fv(pv, r, n):
    return pv * (1 + r) ** n


def pv(fv_, r, n):
    return fv_ / (1 + r) ** n


def pv_annuity(pmt, r, n):
    return pmt * (1 - (1 + r) ** -n) / r


def fv_annuity(pmt, r, n):
    return pmt * ((1 + r) ** n - 1) / r


def payment(principal, r, n):
    return principal * r / (1 - (1 + r) ** -n)


def npv(rate, cfs):
    """cfs[0] at time 0."""
    return sum(cf / (1 + rate) ** t for t, cf in enumerate(cfs))


def irr(cfs, lo=-0.99, hi=1.0):
    return brentq(lambda r: npv(r, cfs), lo, hi)


def payback(cfs, rate=None):
    cum = 0.0
    for t, cf in enumerate(cfs):
        c = cf if rate is None else cf / (1 + rate) ** t
        if t > 0 and cum < 0 <= cum + c:
            return t - 1 + (-cum) / c
        cum += c
    return float("nan")


def eac(npv_cost, r, n):
    """Equivalent annual cost of a present-value cost over n years."""
    return npv_cost * r / (1 - (1 + r) ** -n)


# ---------------------------------------------------------------- financial statements
def statements():
    """Two years of statements built so the balance sheet and cash flow reconcile exactly ($000)."""
    inc = {}
    for y, (rev, cogs_pct, sga, dep, interest) in {"Y1": (44000, 0.71, 6900, 1900, 980),
                                                   "Y2": (48000, 0.70, 7200, 2100, 900)}.items():
        cogs = round(rev * cogs_pct)
        gross = rev - cogs
        ebit = gross - sga - dep
        ebt = ebit - interest
        tax = round(ebt * TAX)
        inc[y] = dict(revenue=rev, cogs=cogs, gross_profit=gross, sga=sga, depreciation=dep, ebit=ebit,
                      interest=interest, ebt=ebt, tax=tax, net_income=ebt - tax)
    bs1 = dict(cash=2400, receivables=6100, inventory=7300, prepaid=400,
               ppe_gross=26000, acc_dep=11000,
               payables=3900, accrued=1500, current_debt=1200, long_term_debt=10800,
               common_stock=5000)
    bs1["ppe_net"] = bs1["ppe_gross"] - bs1["acc_dep"]
    bs1["total_current_assets"] = bs1["cash"] + bs1["receivables"] + bs1["inventory"] + bs1["prepaid"]
    bs1["total_assets"] = bs1["total_current_assets"] + bs1["ppe_net"]
    bs1["total_current_liabilities"] = bs1["payables"] + bs1["accrued"] + bs1["current_debt"]
    bs1["total_liabilities"] = bs1["total_current_liabilities"] + bs1["long_term_debt"]
    bs1["retained_earnings"] = bs1["total_assets"] - bs1["total_liabilities"] - bs1["common_stock"]
    bs1["total_equity"] = bs1["common_stock"] + bs1["retained_earnings"]

    # Year-2 operating and financing decisions
    ni2, dep2 = inc["Y2"]["net_income"], inc["Y2"]["depreciation"]
    capex, dividends, new_debt, repaid = 3100, 900, 1500, 1200
    bs2 = dict(receivables=7000, inventory=7900, prepaid=450, payables=4300, accrued=1650,
               current_debt=1300, common_stock=5000)
    bs2["ppe_gross"] = bs1["ppe_gross"] + capex
    bs2["acc_dep"] = bs1["acc_dep"] + dep2
    bs2["ppe_net"] = bs2["ppe_gross"] - bs2["acc_dep"]
    total_debt2 = bs1["current_debt"] + bs1["long_term_debt"] + new_debt - repaid
    bs2["long_term_debt"] = total_debt2 - bs2["current_debt"]
    d = lambda k: bs2[k] - bs1[k]  # noqa: E731
    cfo_items = {"net income": ni2, "depreciation": dep2, "increase in receivables": -d("receivables"),
                 "increase in inventory": -d("inventory"), "increase in prepaid": -d("prepaid"),
                 "increase in payables": d("payables"), "increase in accrued": d("accrued")}
    cfo = sum(cfo_items.values())
    cfi = -capex
    cff = new_debt - repaid - dividends
    bs2["cash"] = bs1["cash"] + cfo + cfi + cff
    bs2["total_current_assets"] = bs2["cash"] + bs2["receivables"] + bs2["inventory"] + bs2["prepaid"]
    bs2["total_assets"] = bs2["total_current_assets"] + bs2["ppe_net"]
    bs2["total_current_liabilities"] = bs2["payables"] + bs2["accrued"] + bs2["current_debt"]
    bs2["total_liabilities"] = bs2["total_current_liabilities"] + bs2["long_term_debt"]
    bs2["retained_earnings"] = bs1["retained_earnings"] + ni2 - dividends
    bs2["total_equity"] = bs2["common_stock"] + bs2["retained_earnings"]
    assert bs2["total_assets"] == bs2["total_liabilities"] + bs2["total_equity"], "balance sheet does not balance"
    cash_flow = dict(cfo_items=cfo_items, CFO=cfo, CFI=cfi, CFF=cff,
                     cff_items={"new borrowing": new_debt, "debt repaid": -repaid, "dividends": -dividends},
                     net_change=cfo + cfi + cff, free_cash_flow=cfo - capex)
    return inc, {"Y1": bs1, "Y2": bs2}, cash_flow


def ratios(inc, bs, y="Y2"):
    i, b = inc[y], bs[y]
    days = 365
    avg = lambda k: (bs["Y1"][k] + bs["Y2"][k]) / 2 if y == "Y2" else b[k]  # noqa: E731
    dso = b["receivables"] / i["revenue"] * days
    dio = b["inventory"] / i["cogs"] * days
    dpo = b["payables"] / i["cogs"] * days
    debt = b["current_debt"] + b["long_term_debt"]
    ebitda = i["ebit"] + i["depreciation"]
    return {
        "gross margin %": 100 * i["gross_profit"] / i["revenue"],
        "operating (EBIT) margin %": 100 * i["ebit"] / i["revenue"],
        "net margin %": 100 * i["net_income"] / i["revenue"],
        "ROA % (NI / avg assets)": 100 * i["net_income"] / avg("total_assets"),
        "ROE % (NI / avg equity)": 100 * i["net_income"] / avg("total_equity"),
        "asset turnover": i["revenue"] / avg("total_assets"),
        "current ratio": b["total_current_assets"] / b["total_current_liabilities"],
        "quick ratio": (b["cash"] + b["receivables"]) / b["total_current_liabilities"],
        "DSO (days)": dso, "DIO (days)": dio, "DPO (days)": dpo,
        "cash conversion cycle (days)": dso + dio - dpo,
        "debt / equity": debt / b["total_equity"],
        "debt / EBITDA": debt / ebitda,
        "interest coverage (EBIT / interest)": i["ebit"] / i["interest"],
    }


# ---------------------------------------------------------------- examples
def ex_statements():
    inc, bs, cf = statements()
    return {"income statement ($000)": inc, "balance sheet Y1 ($000)": bs["Y1"], "balance sheet Y2 ($000)": bs["Y2"],
            "check Y2 assets = liabilities + equity": (bs["Y2"]["total_assets"],
                                                       bs["Y2"]["total_liabilities"] + bs["Y2"]["total_equity"])}


def ex_cashflow():
    inc, bs, cf = statements()
    return {"operating items": cf["cfo_items"], "CFO": cf["CFO"], "CFI": cf["CFI"], "financing items": cf["cff_items"],
            "CFF": cf["CFF"], "net change in cash": cf["net_change"],
            "cash Y1 -> Y2": (bs["Y1"]["cash"], bs["Y2"]["cash"]), "free cash flow (CFO - capex)": cf["free_cash_flow"]}


def ex_ratios():
    inc, bs, _ = statements()
    r1, r2 = ratios(inc, bs, "Y1"), ratios(inc, bs, "Y2")
    return {k: (round(r1[k], 2), round(r2[k], 2)) for k in r2}


def budget_data():
    """Cell 7 quarterly budget vs actual. Static budget at 10,000 units; actual 11,200 units."""
    b_units, a_units = 10000, 11200
    budget = dict(price=62.0, mat_per_unit=14.0, labor_hr_per_unit=0.30, labor_rate=34.0,
                  var_oh_per_unit=4.0, fixed_oh=118000.0, cell_sga=36000.0)
    actual = dict(revenue=11200 * 60.5, material=11200 * 14.9, labor_hours=3250, labor_cost=3250 * 35.2,
                  var_oh=11200 * 4.1, fixed_oh=124500.0, cell_sga=35200.0)
    return b_units, a_units, budget, actual


def ex_budget():
    b_units, a_units, b, a = budget_data()

    def plan(units):
        rev = units * b["price"]
        mat = units * b["mat_per_unit"]
        lab = units * b["labor_hr_per_unit"] * b["labor_rate"]
        voh = units * b["var_oh_per_unit"]
        cm = rev - mat - lab - voh
        op = cm - b["fixed_oh"] - b["cell_sga"]
        return dict(revenue=rev, material=mat, labor=lab, var_oh=voh, contribution=cm,
                    fixed_oh=b["fixed_oh"], cell_sga=b["cell_sga"], operating_profit=op)

    static, flex = plan(b_units), plan(a_units)
    act = dict(revenue=a["revenue"], material=a["material"], labor=a["labor_cost"], var_oh=a["var_oh"])
    act["contribution"] = act["revenue"] - act["material"] - act["labor"] - act["var_oh"]
    act["fixed_oh"], act["cell_sga"] = a["fixed_oh"], a["cell_sga"]
    act["operating_profit"] = act["contribution"] - act["fixed_oh"] - act["cell_sga"]
    std_hours = a_units * b["labor_hr_per_unit"]
    detail = {
        "sales volume variance (flex - static op profit)": flex["operating_profit"] - static["operating_profit"],
        "selling price variance": a["revenue"] - a_units * b["price"],
        "material spending variance": -(a["material"] - flex["material"]),
        "labor rate variance": -(a["labor_hours"] * (a["labor_cost"] / a["labor_hours"] - b["labor_rate"])),
        "labor efficiency variance": -((a["labor_hours"] - std_hours) * b["labor_rate"]),
        "variable overhead spending variance": -(a["var_oh"] - flex["var_oh"]),
        "fixed overhead spending variance": -(a["fixed_oh"] - b["fixed_oh"]),
        "cell SG&A variance": -(a["cell_sga"] - b["cell_sga"]),
    }
    total = act["operating_profit"] - static["operating_profit"]
    assert abs(sum(detail.values()) - total) < 1e-6
    rnd = lambda dct: {k: round(v) for k, v in dct.items()}  # noqa: E731
    return {"static budget (10,000 units)": rnd(static), "flexible budget (11,200 units)": rnd(flex),
            "actual": rnd(act), "variances (+ = favorable)": rnd(detail), "total variance vs static": round(total)}


def ex_tvm():
    return {
        "FV of $100,000 at 6% for 10 yr": round(fv(100000, 0.06, 10), 2),
        "PV of $250,000 in 5 yr at 8%": round(pv(250000, 0.08, 5), 2),
        "PV of $40,000/yr for 7 yr at 9%": round(pv_annuity(40000, 0.09, 7), 2),
        "FV of $5,000/quarter for 3 yr at 6% APR (1.5%/qtr)": round(fv_annuity(5000, 0.015, 12), 2),
        "effective annual rate of 7% APR compounded monthly %": round(100 * ((1 + 0.07 / 12) ** 12 - 1), 3),
        "rule of 72 vs exact doubling time at 8% (yr)": (round(72 / 8, 2), round(math.log(2) / math.log(1.08), 2)),
        "PV of a $30,000/yr perpetuity at 10%": 300000.0,
    }


def loan_schedule(principal=1_200_000, apr=0.07, years=5):
    r, n = apr / 12, years * 12
    pmt = payment(principal, r, n)
    bal, rows = principal, []
    for m in range(1, n + 1):
        intr = bal * r
        prin = pmt - intr
        bal -= prin
        rows.append(dict(month=m, payment=pmt, interest=intr, principal=prin, balance=max(bal, 0.0)))
    return pmt, pd.DataFrame(rows)


def ex_loan():
    pmt, s = loan_schedule()
    yr = s.groupby((s.month - 1) // 12 + 1)[["interest", "principal"]].sum().round(0)
    return {"monthly payment": round(pmt, 2), "month 1 interest / principal": (round(s.interest[0], 2), round(s.principal[0], 2)),
            "total interest over 5 yr": round(s.interest.sum(), 0), "interest and principal by year": yr.to_dict("index")}


def wacc_inputs():
    """Illustrative capital-cost inputs for Riverbend. Returns (WACC, details)."""
    price = pv_annuity(60, 0.07, 10) + pv(1000, 0.07, 10)
    kd = 0.07 * (1 - TAX)
    rf, beta, mrp = 0.04, 1.2, 0.055
    ke = rf + beta * mrp
    E, Dm = 30000, 12000
    return (E * ke + Dm * kd) / (E + Dm), dict(price=price, kd=kd, ke=ke, E=E, D=Dm)


def wacc():
    """WACC rounded to 0.01 % so hand calculations match: 9.07 %."""
    return round(wacc_inputs()[0], 4)


def ex_wacc():
    # bond: 10-yr, 6% annual coupon, $1,000 face, market yield 7%
    price = pv_annuity(60, 0.07, 10) + pv(1000, 0.07, 10)
    kd_pre = 0.07
    kd = kd_pre * (1 - TAX)
    rf, beta, mrp = 0.04, 1.2, 0.055          # illustrative inputs
    ke = rf + beta * mrp
    E, Dm = 30000, 12000                       # market values $000 (illustrative)
    w = (E * ke + Dm * kd) / (E + Dm)
    return {"bond price at 7% yield (6% coupon)": round(price, 2), "pre-tax cost of debt %": 7.0,
            "after-tax cost of debt %": round(100 * kd, 2), "cost of equity (CAPM) %": round(100 * ke, 2),
            "weights E / D": (round(E / (E + Dm), 3), round(Dm / (E + Dm), 3)), "WACC %": round(100 * w, 2)}


def project_cash_flows(cost=1_200_000, install=100_000, savings=380_000, life=7, salvage=150_000,
                       nwc=60_000, tax=TAX):
    """After-tax cash flows of the 5-axis machining-center project (straight-line depreciation to zero)."""
    basis = cost + install
    dep = basis / life
    cfs = [-(basis + nwc)]
    for t in range(1, life + 1):
        ocf = savings * (1 - tax) + dep * tax          # operating cash flow incl. depreciation tax shield
        cf = ocf
        if t == life:
            cf += salvage * (1 - tax) + nwc            # salvage taxed as gain (book value 0) + recover working capital
        cfs.append(cf)
    return cfs, dep


def ex_capital():
    cfs, dep = project_cash_flows()
    return {"annual depreciation": round(dep, 2), "cash flows": [round(c) for c in cfs]}


def ex_invest():
    cfs, dep = project_cash_flows()
    r = wacc()
    basis = 1_300_000
    avg_ni = 380_000 * (1 - TAX) - dep * (1 - TAX)  # accounting income per year
    return {"NPV at WACC 9.07%": round(npv(r, cfs)), "IRR %": round(100 * irr(cfs), 2),
            "simple payback (yr)": round(payback(cfs), 2), "discounted payback (yr)": round(payback(cfs, r), 2),
            "profitability index": round(1 + npv(r, cfs) / -cfs[0], 3),
            "accounting ROI % (avg net income / avg investment)": round(100 * avg_ni / ((basis + 0) / 2 + 60_000), 2)}


def ex_leasebuy():
    """Lease vs buy-with-loan for the same machine; compare after-tax PV of costs at the after-tax cost of debt."""
    kd_at = 0.07 * (1 - TAX)
    life, basis, salvage = 7, 1_300_000, 150_000
    dep = basis / life
    lease_pmt = 235_000                       # annual, paid at start of each year (illustrative quote)
    lease = [-(lease_pmt * (1 - TAX))] * life + [0]                  # years 0..6 payments, year 7 nothing
    buy = [-basis] + [dep * TAX] * life
    buy[-1] += salvage * (1 - TAX)
    pv_lease, pv_buy = npv(kd_at, lease), npv(kd_at, buy)
    return {"after-tax discount rate %": round(100 * kd_at, 2), "PV cost of leasing": round(pv_lease),
            "PV cost of buying": round(pv_buy), "advantage of buying (+ = buy cheaper)": round(pv_buy - pv_lease)}


def ex_sensitivity():
    r = wacc()
    base = npv(r, project_cash_flows()[0])
    swings = {
        "annual savings -20% / +20%": (dict(savings=304_000), dict(savings=456_000)),
        "machine cost +10% / -10%": (dict(cost=1_320_000), dict(cost=1_080_000)),
        "life 5 / 9 years": (dict(life=5), dict(life=9)),
        "salvage 0 / 300k": (dict(salvage=0), dict(salvage=300_000)),
    }
    out = {}
    for k, (lo, hi) in swings.items():
        out[k] = (round(npv(r, project_cash_flows(**lo)[0])), round(npv(r, project_cash_flows(**hi)[0])))
    rate = (round(npv(0.07, project_cash_flows()[0])), round(npv(0.12, project_cash_flows()[0])))
    # break-even savings (NPV = 0)
    be = brentq(lambda s: npv(r, project_cash_flows(savings=s)[0]), 1, 1_000_000)
    # Monte Carlo
    rng = np.random.default_rng(2026)
    n = 10000
    sav = rng.triangular(280_000, 380_000, 440_000, n)
    cost = rng.normal(1_200_000, 60_000, n)
    lifes = rng.choice([5, 6, 7, 8], n, p=[0.1, 0.25, 0.45, 0.2])
    sims = np.array([npv(r, project_cash_flows(cost=c, savings=s, life=int(L))[0]) for c, s, L in zip(cost, sav, lifes)])
    return {"base NPV": round(base), "NPV low / high by driver": out, "discount rate 7% / 12%": rate,
            "break-even annual savings": round(be),
            "Monte Carlo (10,000 runs)": {"mean NPV": round(sims.mean()), "P(NPV < 0)": round(float((sims < 0).mean()), 3),
                                          "5th / 95th percentile": (round(np.percentile(sims, 5)), round(np.percentile(sims, 95)))}}


def ex_eac():
    """Two machines with different lives; compare by equivalent annual cost (pre-tax, at WACC)."""
    r = wacc()
    m1 = dict(name="Machine X", price=900_000, op_cost=210_000, life=5, salvage=80_000)
    m2 = dict(name="Machine Y", price=1_300_000, op_cost=160_000, life=8, salvage=150_000)
    out = {}
    for m in (m1, m2):
        pvc = m["price"] + pv_annuity(m["op_cost"], r, m["life"]) - pv(m["salvage"], r, m["life"])
        out[m["name"]] = {"PV of costs": round(pvc), "EAC": round(eac(pvc, r, m["life"]))}
    return out


def ex_breakeven():
    """Annual view of Cell 7, consistent with the quarterly budget (4 x 10,000 units; fixed 4 x 154,000)."""
    price, vc, fixed = 62.0, 28.2, 616_000.0
    cm = price - vc
    be_units = fixed / cm
    plan = 40_000
    op = plan * cm - fixed
    target = 800_000
    auto_vc, auto_fixed = 24.0, fixed + 120_000      # automation cell: lower variable cost, higher fixed cost
    op_auto = plan * (price - auto_vc) - auto_fixed
    return {"contribution margin per unit": round(cm, 2), "CM ratio %": round(100 * cm / price, 2),
            "break-even units": round(be_units), "break-even revenue": round(be_units * price),
            "plan units": plan, "operating profit at plan": round(op),
            "margin of safety %": round(100 * (plan - be_units) / plan, 1),
            "degree of operating leverage at plan": round(plan * cm / op, 2),
            "units for $800k operating profit": round((fixed + target) / cm),
            "automated: break-even units": round(auto_fixed / (price - auto_vc)),
            "automated: operating profit at plan": round(op_auto),
            "automated: DOL at plan": round(plan * (price - auto_vc) / op_auto, 2),
            "indifference volume (current = automated)": round((auto_fixed - fixed) / (vc - auto_vc))}


def ex_valuation():
    inc, bs, cf = statements()
    # 5-year forecast of unlevered free cash flow ($000)
    rev0, g = inc["Y2"]["revenue"], [0.06, 0.06, 0.05, 0.04, 0.03]
    ebit_m, dep_pct, capex_pct, nwc_pct = 0.11, 0.045, 0.055, 0.20
    rows, rev, nwc_prev = [], rev0, rev0 * nwc_pct
    for t, gt in enumerate(g, start=1):
        rev = rev * (1 + gt)
        ebit = rev * ebit_m
        nopat = ebit * (1 - TAX)
        dep = rev * dep_pct
        capex = rev * capex_pct
        nwc = rev * nwc_pct
        fcf = nopat + dep - capex - (nwc - nwc_prev)
        nwc_prev = nwc
        rows.append(dict(year=t, revenue=round(rev), nopat=round(nopat), fcf=round(fcf)))
    w, gT = wacc(), 0.025
    pv_fcf = sum(r["fcf"] / (1 + w) ** r["year"] for r in rows)
    tv = rows[-1]["fcf"] * (1 + gT) / (w - gT)
    pv_tv = tv / (1 + w) ** 5
    ev = pv_fcf + pv_tv
    b = bs["Y2"]
    net_debt = b["current_debt"] + b["long_term_debt"] - b["cash"]
    ebitda = inc["Y2"]["ebit"] + inc["Y2"]["depreciation"]
    return {"forecast": rows, "PV of 5-yr FCF": round(pv_fcf), "terminal value (yr 5)": round(tv),
            "PV of terminal value": round(pv_tv), "enterprise value": round(ev),
            "terminal value share of EV %": round(100 * pv_tv / ev, 1),
            "net debt": net_debt, "equity value": round(ev - net_debt),
            "implied EV / EBITDA": round(ev / ebitda, 2),
            "EV at 6x-8x EBITDA (multiples cross-check)": (6 * ebitda, 8 * ebitda)}


def ex_merger():
    """Acquire Kestrel Bearings (fictional): value standalone, value synergies, set a walk-away price ($000)."""
    w, g = wacc(), 0.02
    fcf_next = 600.0                                   # Kestrel next-year free cash flow
    standalone = fcf_next / (w - g)                    # growing perpetuity
    syn_pre_tax = 250.0                                # purchasing and overhead savings per year
    syn_cost = 400.0                                   # one-time integration cost (year 0, pre-tax)
    synergy = syn_pre_tax * (1 - TAX) / (w - g) - syn_cost * (1 - TAX)
    asking = 9500.0
    return {"standalone value (FCF 600 growing 2%)": round(standalone), "PV of synergies net of integration": round(synergy),
            "maximum (walk-away) price": round(standalone + synergy), "seller asking price": asking,
            "value left for Riverbend at asking price": round(standalone + synergy - asking),
            "premium over standalone at asking %": round(100 * (asking / standalone - 1), 1)}


def ex_startup():
    """New linear-actuator venture: how much financing is needed? ($000, yearly)"""
    cfs = [-2000, -600, 200, 900, 1300, 1500]
    cum = np.cumsum(cfs)
    peak = -cum.min()
    r = 0.15                                           # higher rate for a riskier new venture (illustrative)
    tv = cfs[-1] * 1.02 / (r - 0.02)
    return {"cash flows yr 0-5": cfs, "cumulative": cum.tolist(), "peak funding need": int(peak),
            "funding with 25% contingency": round(peak * 1.25), "year cumulative cash turns positive": int(np.argmax(cum > 0)),
            "NPV at 15% incl. terminal value": round(npv(r, cfs) + tv / (1 + r) ** 5),
            "NPV at 15% without terminal value": round(npv(r, cfs))}


# ---------------------------------------------------------------- data files
def make_data():
    os.makedirs(D, exist_ok=True)
    inc, bs, cf = statements()
    pd.DataFrame(inc).to_csv(os.path.join(D, "income_statement.csv"), index_label="line_item")
    pd.DataFrame(bs).to_csv(os.path.join(D, "balance_sheet.csv"), index_label="line_item")
    pd.DataFrame({"amount": {**cf["cfo_items"], "CFO": cf["CFO"], "capital expenditure": cf["CFI"],
                             **cf["cff_items"], "CFF": cf["CFF"], "net change in cash": cf["net_change"]}}
                 ).to_csv(os.path.join(D, "cash_flow_statement.csv"), index_label="line_item")
    _, s = loan_schedule()
    s.round(2).to_csv(os.path.join(D, "loan_schedule.csv"), index=False)
    cfs, _ = project_cash_flows()
    pd.DataFrame({"year": range(len(cfs)), "cash_flow": [round(c, 2) for c in cfs]}).to_csv(
        os.path.join(D, "machining_center_cash_flows.csv"), index=False)
    b = ex_budget()
    pd.DataFrame({k: b[k] for k in ("static budget (10,000 units)", "flexible budget (11,200 units)", "actual")}
                 ).to_csv(os.path.join(D, "cell7_budget_vs_actual.csv"), index_label="line_item")
    return "data written"


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"statements": ex_statements, "cashflow": ex_cashflow, "ratios": ex_ratios, "budget": ex_budget, "tvm": ex_tvm,
      "loan": ex_loan, "capital": ex_capital, "wacc": ex_wacc, "invest": ex_invest, "leasebuy": ex_leasebuy,
      "sensitivity": ex_sensitivity, "eac": ex_eac, "breakeven": ex_breakeven, "valuation": ex_valuation,
      "merger": ex_merger, "startup": ex_startup}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                print(f"  {a}: {_clean(b)}")
