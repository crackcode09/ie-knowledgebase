"""epmkit.py - data and calculations for the Analytics-Based Enterprise Performance Management course.

Running case: Larkfield Instruments (fictional) makes and sells industrial measuring instruments through
three channels (direct, distributors, web). Leadership wants to know which products, channels and customers
make money, to replace its annual budget with driver-based rolling forecasts, and to tie risk to performance.

    python tools/epmkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/epmkit.py all           # every worked example
    python tools/epmkit.py <name>        # abc, products, customers, chargeback, scorecard, clv, churn, unitcost,
                                         # vsc, budget, rolling, montecarlo, risk, outsource, insight

Requires numpy, pandas, statsmodels. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

RESOURCES = {"Customer service staff": 620_000, "Order processing staff": 410_000, "Warehouse labour": 540_000,
             "Sales force": 980_000, "Engineering support": 450_000, "IT": 380_000, "Facilities": 300_000,
             "Quality staff": 260_000}
# activity: (driver, level)  level = customer-level or product-level
ACTIVITIES = {"Process orders": ("orders", "customer"), "Enter order lines": ("lines", "customer"),
              "Pick and ship": ("shipments", "customer"), "Handle returns": ("returns", "customer"),
              "Support customers": ("support_calls", "customer"), "Sales visits": ("visits", "customer"),
              "Engineer specials": ("special_orders", "customer"), "Sustain products": ("product_years", "product"),
              "Inspect production runs": ("production_runs", "product")}
# resource -> share of each activity (rows sum to 1); from effort interviews (case data)
RES_DRIVERS = {
    "Customer service staff": {"Process orders": 0.25, "Handle returns": 0.10, "Support customers": 0.65},
    "Order processing staff": {"Process orders": 0.45, "Enter order lines": 0.55},
    "Warehouse labour": {"Pick and ship": 0.90, "Handle returns": 0.10},
    "Sales force": {"Sales visits": 0.80, "Engineer specials": 0.20},
    "Engineering support": {"Engineer specials": 0.45, "Sustain products": 0.40, "Support customers": 0.15},
    "IT": {"Process orders": 0.30, "Enter order lines": 0.20, "Pick and ship": 0.15, "Support customers": 0.15,
           "Sales visits": 0.10, "Sustain products": 0.10},
    "Facilities": {"Pick and ship": 0.65, "Handle returns": 0.05, "Inspect production runs": 0.20,
                   "Process orders": 0.10},
    "Quality staff": {"Inspect production runs": 0.85, "Handle returns": 0.15}}


def make_data(seed=2029):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}
    pd.DataFrame([dict(resource=r, annual_cost=c) for r, c in RESOURCES.items()]).to_csv(
        os.path.join(D, "resources.csv"), index=False)
    pd.DataFrame([dict(resource=r, activity=a, share=s) for r, m in RES_DRIVERS.items() for a, s in m.items()]).to_csv(
        os.path.join(D, "resource_drivers.csv"), index=False)

    # products
    rows = []
    for i in range(1, 13):
        price = float(np.round(rng.uniform(180, 2400), -1))
        direct = round(price * rng.uniform(0.38, 0.58), 2)
        rows.append(dict(product=f"P{i:02d}", list_price=price, direct_cost=direct,
                         production_runs=int(rng.integers(6, 80)), complexity=rng.choice(["standard", "configurable"],
                                                                                          p=[.7, .3])))
    prod = pd.DataFrame(rows)
    prod.to_csv(os.path.join(D, "products.csv"), index=False)
    out["products"] = 12

    # customers and their behaviour (cost-to-serve drivers)
    chans = rng.choice(["Direct", "Distributor", "Web"], 40, p=[.3, .3, .4])
    rows, sales = [], []
    for i, ch in enumerate(chans, 1):
        size = rng.lognormal(np.log({"Direct": 300_000, "Distributor": 300_000, "Web": 30_000}[ch]), 0.8)
        disc = {"Direct": 0.08, "Distributor": 0.22, "Web": 0.0}[ch] + rng.uniform(-0.03, 0.03)
        disc = max(disc, 0)
        avg_order = {"Direct": 2500, "Distributor": 4000, "Web": 350}[ch] * rng.uniform(0.5, 1.5)
        orders = max(1, int(size / avg_order))
        lines = int(orders * rng.uniform(1.2, {"Direct": 3, "Distributor": 5, "Web": 1.6}[ch]))
        ship = int(orders * rng.uniform(1.0, 1.6))
        rets = int(rng.binomial(ship, {"Direct": 0.04, "Distributor": 0.03, "Web": 0.08}[ch]))
        calls = int(orders * rng.uniform(0.2, 1.6) * {"Direct": 1.4, "Distributor": 0.6, "Web": 0.9}[ch])
        visits = int({"Direct": rng.integers(4, 24), "Distributor": rng.integers(4, 16), "Web": 0}[ch])
        specials = int(rng.binomial(orders, {"Direct": 0.04, "Distributor": 0.01, "Web": 0.0}[ch]))
        late = float(np.round(rng.beta(2, 18), 3))
        rows.append(dict(customer=f"C{i:02d}", channel=ch, discount=round(disc, 3), orders=orders, lines=lines,
                         shipments=ship, returns=rets, support_calls=calls, visits=visits, special_orders=specials,
                         late_delivery_rate=late, years_as_customer=int(rng.integers(1, 15))))
        # product mix
        k = rng.integers(2, 8)
        ps = rng.choice(prod["product"], k, replace=False)
        w = rng.dirichlet(np.ones(k))
        for p, wi in zip(ps, w):
            lp = float(prod.loc[prod["product"] == p, "list_price"].iloc[0])
            units = max(1, int(round(size * wi / (lp * (1 - disc)))))
            sales.append(dict(customer=f"C{i:02d}", product=p, units=units))
    cust = pd.DataFrame(rows)
    # churn label (last year) driven by service experience (for the predictive module)
    cust.to_csv(os.path.join(D, "customers.csv"), index=False)
    # customer history for the churn model: 600 past customer-years with service experience and churn outcome
    n = 600
    hist = pd.DataFrame(dict(channel=rng.choice(["Direct", "Distributor", "Web"], n, p=[.3, .3, .4]),
                             calls_per_order=np.round(rng.gamma(2.0, 0.35, n), 3),
                             return_rate=np.round(rng.beta(1.5, 40, n), 3),
                             late_delivery_rate=np.round(rng.beta(2, 18, n), 3),
                             years_as_customer=rng.integers(1, 15, n)))
    z = (-3.2 + 0.9 * hist.calls_per_order + 12 * hist.return_rate + 9 * hist.late_delivery_rate
         - 0.12 * hist.years_as_customer + hist.channel.map({"Direct": -0.3, "Distributor": -0.5, "Web": 0.4}))
    hist["churned"] = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)
    hist.to_csv(os.path.join(D, "customer_history.csv"), index=False)
    out["customer_history"] = n
    pd.DataFrame(sales).to_csv(os.path.join(D, "sales.csv"), index=False)
    out["customers"], out["sales_lines"] = 40, len(sales)

    # quarterly revenue history (16 quarters) for rolling forecasts
    q = pd.period_range("2022Q1", "2025Q4", freq="Q")
    t = np.arange(len(q))
    base = 2.92e6 * 1.015 ** t * (1 + 0.06 * np.array([-1, 0.3, 0.9, -0.2])[q.quarter - 1]) * rng.normal(1, 0.025, len(q))
    pd.DataFrame(dict(quarter=q.astype(str), revenue=np.round(base, -3))).to_csv(
        os.path.join(D, "quarterly_revenue.csv"), index=False)
    out["quarterly_revenue"] = len(q)

    # risk register
    risks = [("R1", "Key component supplier failure", 0.15, 900_000, "Supply"),
             ("R2", "Loss of top distributor", 0.08, 1_400_000, "Customer"),
             ("R3", "Copper and steel price spike", 0.30, 350_000, "Market"),
             ("R4", "Field failure of new product (recall)", 0.05, 1_800_000, "Quality"),
             ("R5", "ERP outage during peak", 0.10, 250_000, "IT"),
             ("R6", "Loss of two senior engineers", 0.20, 300_000, "People")]
    pd.DataFrame([dict(risk=a, description=b, probability=p, impact=i, category=c) for a, b, p, i, c in risks]).to_csv(
        os.path.join(D, "risk_register.csv"), index=False)
    out["risk_register"] = len(risks)

    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"))


# ---------------------------------------------------------------- ABC
def activity_costs():
    rd = load("resource_drivers")
    res = load("resources").set_index("resource").annual_cost
    rd["cost"] = rd.apply(lambda r: res[r.resource] * r.share, axis=1)
    return rd.groupby("activity").cost.sum()


def driver_totals():
    c, p = load("customers"), load("products")
    tot = {d: float(c[d].sum()) for d in ["orders", "lines", "shipments", "returns", "support_calls", "visits",
                                         "special_orders"]}
    tot["product_years"] = float(len(p))
    tot["production_runs"] = float(p.production_runs.sum())
    return tot


def activity_rates():
    ac = activity_costs()
    tot = driver_totals()
    return {a: dict(cost=round(float(ac[a])), driver=d, quantity=tot[d], rate=round(float(ac[a]) / tot[d], 2))
            for a, (d, _) in ACTIVITIES.items()}


def ex_abc():
    r = activity_rates()
    return {"total_overhead": int(sum(RESOURCES.values())),
            "activities": [dict(activity=a, **v) for a, v in r.items()]}


def product_profit():
    p, s = load("products"), load("sales")
    c = load("customers").set_index("customer")
    s = s.merge(p, on="product")
    s["revenue"] = s.units * s.list_price * (1 - s.customer.map(c.discount))
    s["direct"] = s.units * s.direct_cost
    pp = s.groupby("product").agg(units=("units", "sum"), revenue=("revenue", "sum"), direct=("direct", "sum")).join(
        p.set_index("product")[["production_runs", "complexity"]])
    r = activity_rates()
    pp["sustain"] = r["Sustain products"]["rate"]
    pp["inspect"] = pp.production_runs * r["Inspect production runs"]["rate"]
    pp["product_margin"] = pp.revenue - pp.direct - pp.sustain - pp.inspect
    return pp, s


def ex_products():
    pp, _ = product_profit()
    pp = pp.assign(margin_pct=(100 * pp.product_margin / pp.revenue).round(1))
    return {"products": pp.reset_index()[["product", "units", "revenue", "product_margin", "margin_pct",
                                          "production_runs"]].round(0).to_dict("records")}


def customer_profit():
    c = load("customers")
    pp, s = product_profit()
    # product-level overhead per unit pushed to customers by units bought
    oh_per_unit = (pp.sustain + pp.inspect) / pp.units
    s["prod_oh"] = s.units * s["product"].map(oh_per_unit)
    g = s.groupby("customer").agg(revenue=("revenue", "sum"), direct=("direct", "sum"), prod_oh=("prod_oh", "sum"))
    c = c.set_index("customer").join(g)
    r = activity_rates()
    cts = 0
    for a, (d, lvl) in ACTIVITIES.items():
        if lvl == "customer":
            c[f"cts_{d}"] = c[d] * r[a]["rate"]
            cts = cts + c[f"cts_{d}"]
    c["cost_to_serve"] = cts
    c["abc_profit"] = c.revenue - c.direct - c.prod_oh - c.cost_to_serve
    total_oh = sum(RESOURCES.values())
    c["traditional_profit"] = c.revenue - c.direct - total_oh * c.revenue / c.revenue.sum()
    return c


def ex_customers():
    c = customer_profit().sort_values("abc_profit", ascending=False)
    cum = c.abc_profit.cumsum()
    total = float(c.abc_profit.sum())
    peak = float(cum.max())
    ch = c.groupby("channel").agg(customers=("revenue", "size"), revenue=("revenue", "sum"),
                                  cost_to_serve=("cost_to_serve", "sum"), abc_profit=("abc_profit", "sum"))
    ch["cts_pct_revenue"] = (100 * ch.cost_to_serve / ch.revenue).round(1)
    flip = c[(c.abc_profit < 0) & (c.traditional_profit > 0)]
    return {"total_revenue": round(float(c.revenue.sum())), "total_profit": round(total),
            "profitable_customers": int((c.abc_profit > 0).sum()), "whale_peak": round(peak),
            "whale_peak_pct_of_total": round(100 * peak / total, 1),
            "losses_from_unprofitable": round(float(c[c.abc_profit < 0].abc_profit.sum())),
            "channels": ch.round(0).reset_index().to_dict("records"),
            "flipped_customers": flip.reset_index()[["customer", "channel", "revenue", "traditional_profit",
                                                     "abc_profit"]].round(0).to_dict("records"),
            "worst5": c.tail(5).reset_index()[["customer", "channel", "revenue", "cost_to_serve",
                                               "abc_profit"]].round(0).to_dict("records")}


def ex_chargeback():
    it = RESOURCES["IT"]
    depts = pd.DataFrame(dict(dept=["Sales", "Customer service", "Warehouse", "Engineering", "Finance"],
                              headcount=[22, 14, 18, 12, 8], tickets=[420, 1650, 380, 260, 190],
                              app_users=[22, 14, 6, 12, 8]))
    depts["by_headcount"] = it * depts.headcount / depts.headcount.sum()
    w_t, w_u = 0.6, 0.4
    depts["by_drivers"] = it * (w_t * depts.tickets / depts.tickets.sum() + w_u * depts.app_users / depts.app_users.sum())
    depts["difference"] = depts.by_drivers - depts.by_headcount
    return {"it_cost": it, "split": "60 % tickets, 40 % application users",
            "depts": depts.round(0).to_dict("records")}


# ---------------------------------------------------------------- strategy: scorecard
SCORECARD = [
    ("Financial", "Operating margin %", 18.0, None, "up", 0.15),
    ("Financial", "Revenue growth %", 6.0, 6.8, "up", 0.10),
    ("Financial", "Cost-to-serve as % of revenue", 20.0, None, "down", 0.10),
    ("Customer", "Customer retention % (predicted)", 92.0, None, "up", 0.10),
    ("Customer", "On-time delivery %", 96.0, 93.0, "up", 0.10),
    ("Customer", "Net promoter score", 40, 34, "up", 0.05),
    ("Internal process", "First-pass yield %", 97.0, 97.6, "up", 0.10),
    ("Internal process", "Order-to-ship lead time (days)", 5.0, 6.2, "down", 0.10),
    ("Internal process", "Cost of quality % of sales", 6.0, 7.1, "down", 0.05),
    ("Learning and growth", "Cross-trained employees %", 60, 52, "up", 0.05),
    ("Learning and growth", "Analytics-skilled analysts (count)", 6, 4, "up", 0.05),
    ("Learning and growth", "Improvement ideas implemented per employee", 2.0, 2.3, "up", 0.05)]


def ex_scorecard():
    c = customer_profit()
    live = {"Operating margin %": round(100 * float(c.abc_profit.sum() / c.revenue.sum()), 1),
            "Cost-to-serve as % of revenue": round(100 * float(c.cost_to_serve.sum() / c.revenue.sum()), 1),
            "Customer retention % (predicted)": round(100 * float(1 - current_churn().p_churn.mean()), 1)}
    rows, score = [], 0
    for persp, kpi, tgt, act, d, w in SCORECARD:
        act = live.get(kpi, act)
        ach = act / tgt if d == "up" else tgt / act
        ach = min(ach, 1.2)
        status = "green" if ach >= 1.0 else "amber" if ach >= 0.9 else "red"
        rows.append(dict(perspective=persp, kpi=kpi, target=tgt, actual=act, achievement_pct=round(100 * ach, 1),
                         status=status, weight=w))
        score += w * ach
    return {"kpis": rows, "weighted_score_pct": round(100 * score, 1),
            "reds": [r["kpi"] for r in rows if r["status"] == "red"]}


# ---------------------------------------------------------------- customers: churn model and CLV
def churn_model():
    h = load("customer_history")
    return smf.logit("churned ~ calls_per_order + return_rate + late_delivery_rate + years_as_customer + C(channel)",
                     data=h).fit(disp=0)


def current_churn():
    c = load("customers")
    c = c.assign(calls_per_order=c.support_calls / c.orders, return_rate=c.returns / c.shipments)
    c["p_churn"] = churn_model().predict(c)
    return c


def auc(y, score):
    """Area under the ROC curve via the rank (Mann-Whitney) formula."""
    r = pd.Series(score).rank().values
    n1 = int(y.sum())
    n0 = len(y) - n1
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0)


def ex_churn():
    h = load("customer_history")
    m = churn_model()
    p = m.predict(h)
    pred = (p >= 0.5).astype(int)
    c = current_churn()
    return {"history_n": len(h), "churn_rate_history": round(float(h.churned.mean()), 3),
            "coefficients": {k: round(v, 3) for k, v in m.params.items()},
            "pvalues": {k: round(v, 4) for k, v in m.pvalues.items()},
            "pseudo_r2": round(m.prsquared, 3), "accuracy_at_0.5": round(float((pred == h.churned).mean()), 3),
            "base_rate_accuracy": round(float(1 - h.churned.mean()), 3),
            "auc": round(auc(h.churned.values, p.values), 3),
            "top_decile_churn_rate": round(float(h.churned[p >= p.quantile(0.9)].mean()), 3),
            "predicted_churn_by_channel": c.groupby("channel").p_churn.mean().round(3).to_dict(),
            "highest_risk": c.sort_values("p_churn", ascending=False).head(5)[
                ["customer", "channel", "calls_per_order", "return_rate", "late_delivery_rate", "years_as_customer",
                 "p_churn"]].round(3).to_dict("records")}


def clv(annual_margin, retention, rate=0.10, years=10):
    return sum(annual_margin * retention ** (t - 1) / (1 + rate) ** t for t in range(1, years + 1))


def ex_clv():
    c = customer_profit()
    ch = current_churn().groupby("channel").p_churn.mean().to_dict()
    rows = []
    for k, g in c.groupby("channel"):
        m = float(g.abc_profit.mean())
        ret = 1 - ch[k]
        rows.append(dict(channel=k, avg_annual_profit=round(m), predicted_retention=round(ret, 3),
                         clv_10yr=round(clv(m, ret)), clv_if_retention_plus5=round(clv(m, min(ret + 0.05, 0.99)))))
    return {"discount_rate": 0.10, "horizon_years": 10, "segments": rows}


# ---------------------------------------------------------------- operational costing
def ex_unitcost():
    sites = pd.DataFrame(dict(site=["Larkfield", "Riverside", "Northgate"], orders=[9800, 6200, 4100],
                              order_mgmt_cost=[700_000, 380_000, 310_000], fte=[9.5, 5.0, 4.5]))
    sites["cost_per_order"] = (sites.order_mgmt_cost / sites.orders).round(2)
    sites["orders_per_fte"] = (sites.orders / sites.fte).round(0)
    best = float(sites.cost_per_order.min())
    sites["gap_to_best"] = ((sites.cost_per_order - best) * sites.orders).round(0)
    return {"sites": sites.to_dict("records")}


def ex_vsc():
    price, mat, conv_fixed = 950.0, 410.0, 3_200_000.0
    produced, sold = 10_000, 10_500
    std_fixed_per_unit = conv_fixed / 10_500           # standard set at planned (= sales) volume
    vs_profit = sold * (price - mat) - conv_fixed
    absorbed = produced * std_fixed_per_unit
    # absorption: cost of goods sold carries fixed overhead per unit sold; inventory decrease releases prior-period overhead
    abs_profit = sold * (price - mat - std_fixed_per_unit) - (conv_fixed - absorbed)   # under-absorption expensed
    return {"price": price, "material_per_unit": mat, "conversion_costs": conv_fixed, "produced": produced,
            "sold": sold, "inventory_change_units": produced - sold,
            "value_stream_profit": round(vs_profit), "absorption_profit": round(abs_profit),
            "difference": round(vs_profit - abs_profit),
            "fixed_cost_per_unit_standard": round(std_fixed_per_unit, 2)}


# ---------------------------------------------------------------- predictive accounting
CAPACITY = {"Process orders": ("orders", 60_000), "Enter order lines": ("lines", 56_000),
            "Pick and ship": ("shipments", 48_000), "Support customers": ("support_calls", 60_000)}


def ex_budget(growth=0.08, web_shift=0.20):
    """Driver-based operational budget for staff-driven activities. Today's staff cost / cost per FTE gives today's
    FTE; driver quantity / FTE gives capacity per FTE; next year's driver forecast / capacity gives FTE (step-fixed)."""
    c = load("customers")
    tot = driver_totals()
    rd = load("resource_drivers")
    res = load("resources").set_index("resource").annual_cost
    staff = {"Customer service staff", "Order processing staff", "Warehouse labour"}
    rows = []
    for a, (d, cost_fte) in CAPACITY.items():
        staff_cost = float(sum(res[r.resource] * r.share for r in rd[rd.activity == a].itertuples() if r.resource in staff))
        fte_now = staff_cost / cost_fte
        per_fte = tot[d] / fte_now
        q_next = tot[d] * (1 + growth)
        if d in ("orders", "lines", "shipments"):
            web_share = float(c[c.channel == "Web"][d].sum() / c[d].sum())
            q_next *= 1 + web_shift * web_share      # web grows faster: more, smaller orders
        fte_next = q_next / per_fte
        rows.append(dict(activity=a, driver=d, qty_now=int(tot[d]), qty_next=int(q_next),
                         capacity_per_fte=int(per_fte), fte_now=round(fte_now, 2), fte_next=round(fte_next, 2),
                         staff_next=math.ceil(fte_next), cost_now=round(staff_cost),
                         cost_next=math.ceil(fte_next) * cost_fte))
    return {"growth": growth, "web_extra_growth": web_shift, "lines": rows,
            "cost_now": sum(r["cost_now"] for r in rows), "cost_next": sum(r["cost_next"] for r in rows),
            "naive_budget_(+8%)": round(sum(r["cost_now"] for r in rows) * (1 + growth)),
            "fte_now_total": round(sum(r["fte_now"] for r in rows), 2),
            "fte_next_total": round(sum(r["fte_next"] for r in rows), 2),
            "staff_next_if_pooled": math.ceil(sum(r["fte_next"] for r in rows)),
            "staff_next_if_separate": sum(r["staff_next"] for r in rows)}


def ex_rolling():
    q = load("quarterly_revenue")
    q = q.assign(t=np.arange(len(q)), qtr=q.quarter.str[-1])
    m = smf.ols("np.log(revenue) ~ t + C(qtr)", data=q).fit()
    fut = pd.DataFrame(dict(t=np.arange(16, 21), qtr=["1", "2", "3", "4", "1"]))
    pr = m.get_prediction(fut).summary_frame(alpha=0.2)
    fut["forecast"] = np.exp(pr["mean"] + m.scale / 2).round(-3)
    fut["p10"] = np.exp(pr["obs_ci_lower"]).round(-3)
    fut["p90"] = np.exp(pr["obs_ci_upper"]).round(-3)
    fut["quarter"] = ["2026Q1", "2026Q2", "2026Q3", "2026Q4", "2027Q1"]
    static = float(q[q.quarter.str.startswith("2025")].revenue.sum()) * 1.06
    return {"growth_per_quarter_pct": round(100 * (math.exp(m.params["t"]) - 1), 2), "r2": round(m.rsquared, 3),
            "forecast": fut[["quarter", "forecast", "p10", "p90"]].to_dict("records"),
            "fy2026_forecast": round(float(fut.forecast[:4].sum())),
            "static_budget_fy2026_(2025+6%)": round(static)}


def ex_montecarlo(n=20000, seed=11, with_risks=True):
    rng = np.random.default_rng(seed)
    c = customer_profit()
    rev0 = float(c.revenue.sum())
    vr = float(c.direct.sum() / c.revenue.sum())          # direct cost ratio
    growth = rng.triangular(0.00, 0.06, 0.11, n)
    price = rng.triangular(-0.02, 0.01, 0.03, n)
    mat_infl = rng.triangular(0.00, 0.03, 0.09, n)
    rev = rev0 * (1 + growth) * (1 + price)
    direct = vr * rev0 * (1 + growth) * (1 + mat_infl)
    fixed = sum(RESOURCES.values()) * 1.03
    op = rev - direct - fixed
    loss = np.zeros(n)
    if with_risks:
        for _, r in load("risk_register").iterrows():
            hit = rng.random(n) < r.probability
            loss += hit * r.impact * rng.triangular(0.5, 1.0, 1.5, n)
    op_r = op - loss
    pct = lambda x, p: round(float(np.percentile(x, p)))
    return {"revenue_2025": round(rev0), "direct_cost_ratio": round(vr, 3), "profit_2025": round(float(c.abc_profit.sum())),
            "op_profit_no_risk": {"p10": pct(op, 10), "p50": pct(op, 50), "p90": pct(op, 90)},
            "op_profit_with_risks": {"p10": pct(op_r, 10), "p50": pct(op_r, 50), "p90": pct(op_r, 90)},
            "expected_risk_loss": round(float(loss.mean())),
            "prob_op_below_1M": round(float((op_r < 1e6).mean()), 3),
            "prob_loss": round(float((op_r < 0).mean()), 3)}


def ex_risk():
    r = load("risk_register")
    r["expected_loss"] = r.probability * r.impact
    r = r.sort_values("expected_loss", ascending=False)
    return {"risks": r.to_dict("records"), "total_expected_loss": round(float(r.expected_loss.sum()))}


def ex_outsource(price_per_shipment=58.0, variable_share_labour=0.85, facilities_avoidable=0.5):
    r = activity_rates()
    ship = r["Pick and ship"]["quantity"]
    rd = load("resource_drivers")
    a = rd[rd.activity == "Pick and ship"].set_index("resource").share
    res = load("resources").set_index("resource").annual_cost
    labour = res["Warehouse labour"] * a["Warehouse labour"]
    it = res["IT"] * a["IT"]
    fac = res["Facilities"] * a["Facilities"]
    avoid = labour * variable_share_labour + fac * facilities_avoidable
    third = ship * price_per_shipment
    full = r["Pick and ship"]["cost"]
    return {"shipments": int(ship), "abc_full_cost": full, "full_cost_per_shipment": r["Pick and ship"]["rate"],
            "avoidable_cost": round(avoid), "avoidable_per_shipment": round(avoid / ship, 2),
            "3pl_cost": round(third), "net_saving_if_outsourced": round(avoid - third),
            "it_cost_not_avoided": round(it), "breakeven_price": round(avoid / ship, 2)}


def ex_insight(min_order=2500):
    """Value of information: act on the ABC view for unprofitable web customers with a minimum order value."""
    c = customer_profit()
    w = c[(c.channel == "Web") & (c.abc_profit < 0)].copy()
    avg_order = w.revenue / w.orders
    new_orders = np.maximum(1, np.ceil(w.revenue / np.maximum(avg_order, min_order)))
    scale = new_orders / w.orders
    order_drivers = {"orders": "Process orders", "lines": "Enter order lines", "shipments": "Pick and ship"}
    r = activity_rates()
    saving = sum(((1 - scale) * w[d] * r[a]["rate"]).sum() for d, a in order_drivers.items())
    return {"web_loss_customers": len(w), "their_profit_now": round(float(w.abc_profit.sum())),
            "cost_to_serve_saving_if_consolidated": round(float(saving)),
            "their_profit_after": round(float(w.abc_profit.sum() + saving)),
            "note": "assumes the same revenue in fewer, larger orders; activity savings need capacity to be removed"}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, np.floating):
        return round(float(o), 4)
    if isinstance(o, np.integer):
        return int(o)
    return o


EX = {"abc": ex_abc, "products": ex_products, "customers": ex_customers, "chargeback": ex_chargeback,
      "scorecard": ex_scorecard, "churn": ex_churn, "clv": ex_clv, "unitcost": ex_unitcost, "vsc": ex_vsc,
      "budget": ex_budget, "rolling": ex_rolling, "montecarlo": ex_montecarlo, "risk": ex_risk,
      "outsource": ex_outsource, "insight": ex_insight}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print(make_data())
        sys.exit()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list) and b and isinstance(b[0], dict):
                    print(f"  {a}:")
                    for row in b:
                        print(f"    {_clean(row)}")
                else:
                    print(f"  {a}: {_clean(b)}")
