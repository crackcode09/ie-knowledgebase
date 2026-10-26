"""stmkit.py - data and calculations for the Staffing Models & Human Capital Management course.

Running case: Tri-County Building Safety (fictional) is a public agency that reviews construction
plans, issues permits and inspects construction. Inspectors and plan reviewers are mission-critical:
when there are too few, construction stops and safety suffers. The agency's IE builds a staffing model.

    python tools/stmkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/stmkit.py all           # every worked example
    python tools/stmkit.py <name>        # data_inventory, unit_times, sampling, availability, workload_model,
                                         # coverage, queueing, ratio, forecast, supply, gap, sensitivity,
                                         # validate, budget, capstone

Requires numpy, pandas, scipy, statsmodels. License: MIT
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

# ---------------------------------------------------------------- "true" values used only to simulate data
TRUE_MIN = {"inspection_res": 32, "inspection_com": 67, "reinspection": 20, "complaint": 80, "travel_per_stop": 18,
            "plan_review_res": 108, "plan_review_com": 450, "resubmittal_res": 43, "resubmittal_com": 180,
            "permit_processing": 12, "counter_service": 11}
WS_TRUE = {"on_site_inspection": 0.36, "travel": 0.21, "report_writing": 0.11, "phone_customer": 0.09,
           "meetings_admin": 0.10, "personal": 0.05, "waiting": 0.04, "other_unassigned": 0.04}
COUNTER_LAMBDA = [6, 9, 11, 10, 12, 11, 8, 5]           # mean arrivals per hour, 08:00-16:00
ROLES_NOW = {"Inspector": 21, "Plan reviewer": 6, "Permit technician": 4, "Supervisor": 4}

# ---------------------------------------------------------------- policy / planning parameters (course choices)
RESUB = {"res": 0.35, "com": 0.55}       # share of plan reviews with one resubmittal
PLAN_SHARE_RES = 0.55                    # share of residential permits that need a plan review
REINSP_RATE = 0.18                       # share of inspections that fail and need a re-inspection
INDIRECT = {"Plan reviewer": 0.20, "Permit technician": 0.15}   # SME-agreed indirect shares
SPAN = 9                                 # supervisor span of control (policy)
COUNTER_DAYS = 250
COUNTER_TARGET = (0.80, 10.0)            # 80 % of customers served within 10 minutes
LOADED_COST = {"Inspector": 112_000, "Plan reviewer": 125_000, "Permit technician": 78_000, "Supervisor": 140_000}
OT_PREMIUM = 1.5
WAGE_SHARE = 0.68                        # wage as share of loaded cost (for overtime cost)
NEW_HIRE_FACTOR = 0.65                   # average first-year productivity of a new inspector (incl. hiring lag)
RETIRE_TAKEUP = 0.35                     # share of retirement-eligible staff who retire each year


def eligible(age, svc):
    """Illustrative retirement-eligibility rule (NOT any specific plan)."""
    return (age >= 62 and svc >= 5) or (age >= 60 and svc >= 20) or (age >= 57 and svc >= 30)


def make_data(seed=2027):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}

    # 1. Monthly workload history 2021-2025
    months = pd.period_range("2021-01", "2025-12", freq="M")
    t = np.arange(len(months))
    m = months.month.values
    res = 260 * 1.025 ** (t / 12) * (1 + 0.25 * np.cos(2 * np.pi * (m - 7) / 12)) * rng.normal(1, 0.06, len(t))
    com = 35 * 1.04 ** (t / 12) * (1 + 0.10 * np.cos(2 * np.pi * (m - 7) / 12)) * rng.normal(1, 0.08, len(t))
    res, com = np.round(res), np.round(com)
    res_lag = pd.Series(res).rolling(3, min_periods=1).mean().values
    com_lag = pd.Series(com).rolling(6, min_periods=1).mean().values
    ins_res = np.round(6.0 * res_lag * rng.normal(1, 0.04, len(t)))
    ins_com = np.round(14.0 * com_lag * rng.normal(1, 0.05, len(t)))
    reins = np.round(REINSP_RATE * (ins_res + ins_com) * rng.normal(1, 0.06, len(t)))
    compl = rng.poisson(45 * 1.01 ** (t / 12))
    pr_res = np.round(PLAN_SHARE_RES * res * rng.normal(1, 0.04, len(t)))
    pr_com = np.round(com * rng.normal(1, 0.03, len(t)))
    wl = pd.DataFrame(dict(month=months.astype(str), res_permits=res.astype(int), com_permits=com.astype(int),
                           res_inspections=ins_res.astype(int), com_inspections=ins_com.astype(int),
                           reinspections=reins.astype(int), complaints=compl.astype(int),
                           res_plan_reviews=pr_res.astype(int), com_plan_reviews=pr_com.astype(int)))

    # inspector headcount on staff (declining with vacancies) and service level that responds to the gap
    fte = np.round(np.interp(t, [0, 20, 40, 59], [23, 22.5, 21.5, 21]) - rng.choice([0, 0, 0, 1], len(t)), 1)
    hrs = (ins_res * (TRUE_MIN["inspection_res"] + 18) + ins_com * (TRUE_MIN["inspection_com"] + 18)
           + reins * (TRUE_MIN["reinspection"] + 18) + compl * (TRUE_MIN["complaint"] + 18)) / 60
    req = hrs / (0.68 / 0.92) / (1730 / 12)
    ratio = req / fte
    svc = np.clip(97 - 85 * np.maximum(0, ratio - 0.92) + rng.normal(0, 1.5, len(t)), 35, 99.5)
    wl["inspectors_on_staff"] = fte
    wl["next_day_inspection_pct"] = np.round(svc, 1)
    wl.to_csv(os.path.join(D, "workload_history.csv"), index=False)
    out["workload_history"] = len(wl)

    # 2. Unit-time studies (mixed methods)
    spec = [("inspection_res", "residential inspection (on site + report)", "time study", 48, 0.25),
            ("inspection_com", "commercial inspection (on site + report)", "time study", 30, 0.30),
            ("reinspection", "re-inspection (on site + report)", "time study", 40, 0.30),
            ("complaint", "complaint investigation", "time records", 120, 0.45),
            ("travel_per_stop", "travel between stops", "vehicle GPS records", 900, 0.50),
            ("plan_review_res", "residential plan review", "time records", 200, 0.40),
            ("plan_review_com", "commercial plan review", "time records", 80, 0.45),
            ("resubmittal_res", "residential resubmittal review", "SME estimate (Delphi, 6 reviewers)", 6, 0.15),
            ("resubmittal_com", "commercial resubmittal review", "SME estimate (Delphi, 6 reviewers)", 6, 0.20),
            ("permit_processing", "permit processing (back office)", "time study", 60, 0.30),
            ("counter_service", "counter service per customer", "time study", 150, 0.80)]
    rows = []
    for key, desc, meth, n, cv in spec:
        mu = TRUE_MIN[key]
        x = rng.normal(mu, mu * cv, n) if "SME" not in meth else rng.normal(mu, mu * cv, n)
        x = np.clip(x, mu * 0.2, None)
        if key == "counter_service":
            x = rng.exponential(mu, n)
        rows.append(dict(activity=key, description=desc, method=meth, n=n, mean_min=round(float(x.mean()), 1),
                         sd_min=round(float(x.std(ddof=1)), 1)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "unit_time_studies.csv"), index=False)
    out["unit_time_studies"] = len(rows)

    # 3. Work sampling of inspectors: 1,200 random observations over 4 weeks
    cats = list(WS_TRUE)
    obs = rng.choice(cats, 1200, p=list(WS_TRUE.values()))
    day = rng.integers(1, 21, 1200)
    pd.DataFrame(dict(obs=np.arange(1, 1201), workday=day, activity=obs)).to_csv(
        os.path.join(D, "work_sampling_inspectors.csv"), index=False)
    out["work_sampling_inspectors"] = 1200

    # 4. Workforce roster (2026-01-01) and leave records (2025)
    rows, lv = [], []
    k = 0
    for role, n in ROLES_NOW.items():
        for _ in range(n):
            k += 1
            age = int(np.clip(rng.normal(47, 10), 24, 66))
            svc = int(np.clip(rng.normal((age - 23) * 0.55, 5), 0, age - 22))
            rows.append(dict(emp_id=f"E{k:03d}", role=role, age=age, service_years=svc))
            lv.append(dict(emp_id=f"E{k:03d}", role=role, paid_hours=2080, holidays=88,
                           annual_leave=round(float(np.clip(rng.normal(150, 32), 40, 240))),
                           sick_leave=round(float(np.clip(rng.normal(56, 26), 0, 200))),
                           training=round(float(np.clip(rng.normal(40, 10), 16, 80))),
                           other_leave=round(float(np.clip(rng.normal(14, 8), 0, 40)))))
    pd.DataFrame(rows).to_csv(os.path.join(D, "workforce_roster.csv"), index=False)
    pd.DataFrame(lv).to_csv(os.path.join(D, "leave_2025.csv"), index=False)
    out["workforce_roster"] = len(rows)

    # 5. Separations history (inspectors and plan reviewers)
    rows = []
    for y in range(2021, 2026):
        for role, hc, q in [("Inspector", 22.5 - 0.4 * (y - 2021), 0.075), ("Plan reviewer", 6, 0.06)]:
            rows.append(dict(year=y, role=role, avg_headcount=round(hc, 1), quits=int(rng.binomial(round(hc), q)),
                             retirements=int(rng.binomial(round(hc), 0.03))))
    pd.DataFrame(rows).to_csv(os.path.join(D, "separations_history.csv"), index=False)
    out["separations_history"] = len(rows)

    # 6. Permit counter arrivals: 60 sampled days x 8 hours
    rows = []
    for d in range(1, 61):
        for h, lam in enumerate(COUNTER_LAMBDA):
            rows.append(dict(day=d, hour_start=f"{8 + h:02d}:00", arrivals=int(rng.poisson(lam))))
    pd.DataFrame(rows).to_csv(os.path.join(D, "counter_arrivals.csv"), index=False)
    out["counter_arrivals"] = len(rows)

    # 7. Peer agencies (benchmark)
    rows = []
    for i in range(1, 15):
        ins = float(np.round(rng.uniform(8_000, 60_000), -2))
        f = (0.5 + 0.70 * ins / 1000) * rng.normal(1, 0.08)
        rows.append(dict(agency=f"Peer {i:02d}", annual_inspections=int(ins), inspector_fte=round(f, 1)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "peer_benchmark.csv"), index=False)
    out["peer_benchmark"] = 14
    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"))


def ut():
    u = load("unit_time_studies")
    return dict(zip(u.activity, u.mean_min))


# ---------------------------------------------------------------- Module 02: seven data types
def ex_data_inventory():
    inv = [
        ("1 Workload volume (demand drivers)", "workload_history.csv", "monthly counts 2021-2025", "high"),
        ("2 Work content (unit times)", "unit_time_studies.csv", "11 activities, 4 methods", "mixed: SME rows low"),
        ("3 Work activity profile (direct vs indirect)", "work_sampling_inspectors.csv", "1,200 observations", "high"),
        ("4 Availability (paid vs available hours)", "leave_2025.csv", "35 employees, 2025", "high"),
        ("5 Service and policy requirements", "this README / Module 05", "counter target, span, coverage", "policy"),
        ("6 Workforce supply (roster, separations)", "workforce_roster.csv, separations_history.csv",
         "35 staff, 5 years", "medium (small numbers)"),
        ("7 Performance and cost", "workload_history.csv (service), Module 09 costs", "next-day %, loaded cost",
         "medium"),
    ]
    w = load("workload_history")
    gaps = {"months": len(w), "missing_values": int(w.isna().sum().sum()),
            "negative_or_zero_counts": int((w.drop(columns=["month"]) <= 0).sum().sum())}
    return {"inventory": [dict(type=a, source=b, coverage=c, quality=d) for a, b, c, d in inv], "checks": gaps}


# ---------------------------------------------------------------- Module 03: work measurement for staffing
def ex_unit_times():
    u = load("unit_time_studies")
    u = u.assign(cv=(u.sd_min / u.mean_min).round(2),
                 rel_precision_95=(196 * u.sd_min / u.mean_min / np.sqrt(u.n)).round(1))
    # cycles needed for +-5 % at 95 %
    u = u.assign(n_for_5pct=np.ceil((1.96 * u.sd_min / (0.05 * u.mean_min)) ** 2).astype(int))
    return {"unit_times": u[["activity", "method", "n", "mean_min", "sd_min", "rel_precision_95", "n_for_5pct"]]
            .to_dict("records")}


def ws_shares():
    s = load("work_sampling_inspectors").activity.value_counts(normalize=True)
    return s.reindex(list(WS_TRUE)).fillna(0)


def inspector_unit_share():
    s = ws_shares()
    unit = s[["on_site_inspection", "travel", "report_writing"]].sum()
    indirect = s[["phone_customer", "meetings_admin", "personal"]].sum()
    return unit, indirect, unit / (unit + indirect)


def ex_sampling():
    s = ws_shares()
    n = 1200
    rows = [dict(activity=k, share=round(v, 3), ci95=round(1.96 * math.sqrt(v * (1 - v) / n), 3)) for k, v in s.items()]
    unit, ind, us = inspector_unit_share()
    return {"shares": rows, "unit_driven": round(unit, 3), "indirect_allowed": round(ind, 3),
            "excluded_waiting_other": round(1 - unit - ind, 3), "unit_share_for_staffing": round(us, 3),
            "staffing_multiplier": round(1 / us, 3)}


# ---------------------------------------------------------------- Module 04: availability
def available_hours():
    lv = load("leave_2025")
    lv = lv.assign(available=lv.paid_hours - lv.holidays - lv.annual_leave - lv.sick_leave - lv.training - lv.other_leave)
    return lv


def ex_availability():
    lv = available_hours()
    avg = lv[["paid_hours", "holidays", "annual_leave", "sick_leave", "training", "other_leave", "available"]].mean().round(1)
    a = float(avg["available"])
    open_h = 8 * COUNTER_DAYS
    return {"average": avg.to_dict(), "available_h_per_fte": round(a, 1), "availability_pct": round(100 * a / 2080, 1),
            "by_role": lv.groupby("role").available.mean().round(1).to_dict(),
            "counter_relief_factor": round(open_h / a, 3),
            "24x7_post_relief_factor": round(8760 / a, 2)}


def AV():
    return float(available_hours().available.mean())


# ---------------------------------------------------------------- Module 05: model types
def annual(year):
    w = load("workload_history")
    w = w[w.month.str.startswith(str(year))]
    return w.drop(columns=["month", "inspectors_on_staff", "next_day_inspection_pct"]).sum()


def inspector_req(v, u=None, av=None, unit_share=None):
    u = u or ut()
    av = av or AV()
    unit_share = unit_share or inspector_unit_share()[2]
    tr = u["travel_per_stop"]
    hrs = (v["res_inspections"] * (u["inspection_res"] + tr) + v["com_inspections"] * (u["inspection_com"] + tr)
           + v["reinspections"] * (u["reinspection"] + tr) + v["complaints"] * (u["complaint"] + tr)) / 60
    return hrs, hrs / unit_share, hrs / unit_share / av


def reviewer_req(v, u=None, av=None):
    u = u or ut()
    av = av or AV()
    hrs = (v["res_plan_reviews"] * (u["plan_review_res"] + RESUB["res"] * u["resubmittal_res"])
           + v["com_plan_reviews"] * (u["plan_review_com"] + RESUB["com"] * u["resubmittal_com"])) / 60
    return hrs, hrs / (1 - INDIRECT["Plan reviewer"]), hrs / (1 - INDIRECT["Plan reviewer"]) / av


def erlang_c(c, a):
    """Probability an arrival waits (M/M/c), offered load a = lambda/mu."""
    if c <= a:
        return 1.0
    s = sum(a ** k / math.factorial(k) for k in range(c))
    top = a ** c / math.factorial(c) * c / (c - a)
    return top / (s + top)


def service_level(c, lam, mean_min, t_min):
    mu = 60 / mean_min
    a = lam / mu
    if c <= a:
        return 0.0
    return 1 - erlang_c(c, a) * math.exp(-(c * mu - lam) * t_min / 60)


def counter_positions(lams, mean_min, target=COUNTER_TARGET):
    rows = []
    for h, lam in enumerate(lams):
        c = max(1, math.ceil(lam * mean_min / 60))
        while service_level(c, lam, mean_min, target[1]) < target[0]:
            c += 1
        rows.append(dict(hour=f"{8 + h:02d}:00", arrivals=round(lam, 2), load_erlangs=round(lam * mean_min / 60, 2),
                         positions=c, service_level=round(service_level(c, lam, mean_min, target[1]), 3),
                         utilization=round(lam * mean_min / 60 / c, 2)))
    return rows


def tech_req(v, u=None, av=None):
    u = u or ut()
    av = av or AV()
    lams = load("counter_arrivals").groupby("hour_start").arrivals.mean().values
    rows = counter_positions(lams, u["counter_service"])
    pos_h = sum(r["positions"] for r in rows) * COUNTER_DAYS
    back = (v["res_permits"] + v["com_permits"]) * u["permit_processing"] / 60 / (1 - INDIRECT["Permit technician"])
    return rows, pos_h, back, (pos_h + back) / av


def ex_workload_model(year=2025):
    v = annual(year)
    u = ut()
    hrs, gross, fte = inspector_req(v)
    us_ = inspector_unit_share()[2]
    lines = []
    tr = u["travel_per_stop"]
    for col, key in [("res_inspections", "inspection_res"), ("com_inspections", "inspection_com"),
                     ("reinspections", "reinspection"), ("complaints", "complaint")]:
        lines.append(dict(driver=col, volume=int(v[col]), unit_min=round(u[key] + tr, 1),
                          hours=round(v[col] * (u[key] + tr) / 60)))
    rh, rg, rf = reviewer_req(v)
    return {"year": year, "inspector_lines": lines, "unit_hours": round(hrs), "unit_share": round(us_, 3),
            "total_hours": round(gross), "available_h": round(AV(), 1), "inspector_fte": round(fte, 2),
            "reviewer_unit_hours": round(rh), "reviewer_fte": round(rf, 2)}


def ex_coverage():
    a = AV()
    return {"counter_open_h_per_position": 8 * COUNTER_DAYS, "relief_factor": round(8 * COUNTER_DAYS / a, 3),
            "one_post_24x7_fte": round(8760 / a, 2),
            "example_2_posts_24x7_fte": round(2 * 8760 / a, 2)}


def ex_queueing(year=2025):
    v = annual(year)
    rows, pos_h, back, fte = tech_req(v)
    lams = [r["arrivals"] for r in rows]
    naive = sum(math.ceil(l * ut()["counter_service"] / 60) for l in lams) * COUNTER_DAYS
    return {"by_hour": rows, "position_hours_per_day": sum(r["positions"] for r in rows),
            "counter_hours_per_year": pos_h, "back_office_hours": round(back), "tech_fte": round(fte, 2),
            "naive_workload_only_position_hours": naive,
            "arrivals_per_day": round(sum(lams), 1)}


def ex_ratio():
    p = load("peer_benchmark")
    m = smf.ols("inspector_fte ~ I(annual_inspections/1000)", data=p).fit()
    v = annual(2025)
    ours = float(v.res_inspections + v.com_inspections + v.reinspections)
    pred = m.get_prediction(pd.DataFrame(dict(annual_inspections=[ours]))).summary_frame(alpha=0.05)
    sup = sum(ROLES_NOW[r] for r in ["Inspector", "Plan reviewer", "Permit technician"])
    return {"fit": {k: round(v_, 3) for k, v_ in m.params.items()}, "r2": round(m.rsquared, 3),
            "our_inspections": int(ours), "peer_predicted_fte": round(float(pred["mean"].iloc[0]), 1),
            "pi95": [round(float(pred["obs_ci_lower"].iloc[0]), 1), round(float(pred["obs_ci_upper"].iloc[0]), 1)],
            "fte_per_1000_peer_median": round(float((p.inspector_fte / p.annual_inspections * 1000).median()), 3),
            "supervisors_span_rule": round(sup / SPAN, 2)}


# ---------------------------------------------------------------- Module 06: forecasting
def forecast_driver(col, years=(2026, 2027, 2028)):
    w = load("workload_history")
    w = w.assign(t=np.arange(len(w)), mo=w.month.str[5:7].astype(int))
    m = smf.ols(f"np.log({col}) ~ t + C(mo)", data=w).fit()
    out = {}
    for y in years:
        f = pd.DataFrame(dict(t=np.arange((y - 2021) * 12, (y - 2020) * 12), mo=np.arange(1, 13)))
        out[y] = float(np.exp(m.predict(f) + m.scale / 2).sum())
    growth = math.exp(12 * m.params["t"]) - 1
    return out, growth, m


DRIVERS = ["res_permits", "com_permits", "res_inspections", "com_inspections", "reinspections", "complaints",
           "res_plan_reviews", "com_plan_reviews"]


def forecast_all(scenario="base"):
    adj = {"low": -0.05, "base": 0.0, "high": 0.08}[scenario]      # level shift applied by 2028, linear from 2026
    res = {}
    for c in DRIVERS:
        f, g, _ = forecast_driver(c)
        for i, y in enumerate([2026, 2027, 2028]):
            res.setdefault(y, {})[c] = f[y] * (1 + adj * (i + 1) / 3)
    return {y: pd.Series(d) for y, d in res.items()}


def ex_forecast():
    rows = []
    for c in ["res_permits", "com_permits", "res_inspections", "com_inspections"]:
        f, g, m = forecast_driver(c)
        rows.append(dict(driver=c, actual_2025=int(annual(2025)[c]), growth_pct_yr=round(100 * g, 1),
                         f2026=round(f[2026]), f2027=round(f[2027]), f2028=round(f[2028]), r2=round(m.rsquared, 3)))
    w = load("workload_history")
    mo = w.assign(mo=w.month.str[5:7].astype(int)).groupby("mo").res_inspections.mean()
    req = {}
    for sc in ["low", "base", "high"]:
        fc = forecast_all(sc)
        req[sc] = {y: round(inspector_req(fc[y])[2], 2) for y in fc}
    return {"drivers": rows, "seasonal_peak_trough_ratio": round(float(mo.max() / mo.min()), 2),
            "inspector_fte_by_scenario": req}


# ---------------------------------------------------------------- Module 07: supply and gap
def separation_rates():
    s = load("separations_history")
    return {role: dict(quit_rate=round(g.quits.sum() / g.avg_headcount.sum(), 3),
                       retire_rate=round(g.retirements.sum() / g.avg_headcount.sum(), 3)) for role, g in s.groupby("role")}


def project_inspectors(hires=(0, 0, 0), role="Inspector"):
    """Year-by-year inspector supply. Quits at the historic rate; retirements = take-up x eligible pool.
    Hires arrive through the year: each counts as NEW_HIRE_FACTOR of an FTE in the hiring year, 1.0 after."""
    r = load("workforce_roster")
    insp = r[r.role == role]
    ages, svcs = list(insp.age), list(insp.service_years)
    q = separation_rates()[role]["quit_rate"]
    head, retired, proj = float(len(insp)), 0.0, []
    for i, (y, h) in enumerate(zip([2026, 2027, 2028], hires)):
        el = sum(eligible(a + i, v + i) for a, v in zip(ages, svcs))
        ret = RETIRE_TAKEUP * max(el - retired, 0)
        retired += ret
        quits = q * head
        end = head - ret - quits + h
        eff = (head + head - ret - quits) / 2 + h * NEW_HIRE_FACTOR
        proj.append(dict(year=y, start=round(head, 1), retirements=round(ret, 1), quits=round(quits, 1), hires=h,
                         end=round(end, 1), effective_fte=round(eff, 1)))
        head = end
    return proj


def ex_supply():
    r = load("workforce_roster")
    insp = r[r.role == "Inspector"]
    return {"rates": separation_rates(),
            "inspectors_eligible_now": int(sum(eligible(a, v) for a, v in zip(insp.age, insp.service_years))),
            "inspectors_eligible_by_2028": int(sum(eligible(a + 2, v + 2) for a, v in zip(insp.age, insp.service_years))),
            "age_profile": insp.age.describe()[["mean", "min", "max"]].round(1).to_dict(),
            "no_hire_projection": project_inspectors((0, 0, 0))}


def hiring_plan(need, cap=None):
    hires = []
    for i, y in enumerate([2026, 2027, 2028]):
        h = 0
        while True:
            p = project_inspectors(tuple(hires + [h] + [0] * (2 - i)))[i]
            if p["effective_fte"] >= need[y] or (cap is not None and h >= cap):
                break
            h += 1
        hires.append(h)
    return hires


def ex_gap(scenario="base"):
    fc = forecast_all(scenario)
    need = {y: inspector_req(fc[y])[2] for y in fc}
    nohire = project_inspectors((0, 0, 0))
    plan = hiring_plan(need)
    capped = hiring_plan(need, cap=4)
    pp, pc = project_inspectors(tuple(plan)), project_inspectors(tuple(capped))
    return {"need": {y: round(v, 2) for y, v in need.items()},
            "no_hire": [dict(year=r["year"], effective=r["effective_fte"], gap=round(r["effective_fte"] - need[r["year"]], 1))
                        for r in nohire],
            "plan_unconstrained": plan,
            "plan_rows": [dict(year=r["year"], hires=r["hires"], end_headcount=r["end"], effective=r["effective_fte"],
                               gap=round(r["effective_fte"] - need[r["year"]], 1)) for r in pp],
            "plan_capped_4": capped,
            "capped_rows": [dict(year=r["year"], hires=r["hires"], effective=r["effective_fte"],
                                 gap=round(r["effective_fte"] - need[r["year"]], 1)) for r in pc]}


# ---------------------------------------------------------------- Module 08: sensitivity
def ex_sensitivity(n=5000, seed=7):
    v = forecast_all("base")[2026]
    u = ut()
    base = inspector_req(v)[2]
    av, us = AV(), inspector_unit_share()[2]

    def run(scale_ut=1.0, scale_tr=1.0, scale_av=1.0, d_us=0.0, scale_v=1.0):
        uu = dict(u)
        for k in ["inspection_res", "inspection_com", "reinspection", "complaint"]:
            uu[k] = u[k] * scale_ut
        uu["travel_per_stop"] = u["travel_per_stop"] * scale_tr
        vv = v * scale_v
        return inspector_req(vv, uu, av * scale_av, us + d_us)[2]

    tor = [("Unit times ±10 %", run(scale_ut=0.9), run(scale_ut=1.1)),
           ("Travel per stop ±20 %", run(scale_tr=0.8), run(scale_tr=1.2)),
           ("Available hours ±5 %", run(scale_av=1.05), run(scale_av=0.95)),
           ("Unit share ±5 pts", run(d_us=0.05), run(d_us=-0.05)),
           ("Workload volume ±10 %", run(scale_v=0.9), run(scale_v=1.1))]
    tor = sorted([dict(factor=f, low=round(a, 2), high=round(b, 2), swing=round(b - a, 2)) for f, a, b in tor],
                 key=lambda r: -r["swing"])
    rng = np.random.default_rng(seed)
    sims = np.array([run(rng.triangular(0.92, 1, 1.10), rng.triangular(0.85, 1, 1.20), rng.triangular(0.96, 1, 1.03),
                         rng.triangular(-0.04, 0, 0.04), rng.triangular(0.92, 1, 1.10)) for _ in range(n)])
    return {"base_fte_2026": round(base, 2), "tornado": tor, "mc_mean": round(float(sims.mean()), 2),
            "mc_p10": round(float(np.percentile(sims, 10)), 2), "mc_p50": round(float(np.percentile(sims, 50)), 2),
            "mc_p80": round(float(np.percentile(sims, 80)), 2), "mc_p90": round(float(np.percentile(sims, 90)), 2)}


def monthly_requirement():
    w = load("workload_history")
    req = []
    for _, r in w.iterrows():
        req.append(inspector_req(r, av=AV() / 12)[2])
    return w.assign(required_fte=np.round(req, 2), ratio=np.round(np.array(req) / w.inspectors_on_staff, 3))


def ex_validate():
    w = monthly_requirement()
    r = float(np.corrcoef(w.ratio, w.next_day_inspection_pct)[0, 1])
    over = w[w.ratio > 1.0]
    under = w[w.ratio <= 0.92]
    m = smf.ols("next_day_inspection_pct ~ ratio", data=w).fit()
    by = w.assign(mo=w.month.str[5:7].astype(int)).groupby("mo")[["required_fte", "next_day_inspection_pct"]].mean().round(1)
    return {"corr_ratio_service": round(r, 3), "months_ratio_gt_1": len(over),
            "service_when_ratio_gt_1": round(float(over.next_day_inspection_pct.mean()), 1),
            "service_when_ratio_le_0.92": round(float(under.next_day_inspection_pct.mean()), 1),
            "slope_pts_per_0.1_ratio": round(float(m.params["ratio"]) / 10, 1),
            "monthly_profile": by.reset_index().to_dict("records"),
            "fte_2025_months": w[w.month.str.startswith("2025")][["month", "required_fte", "inspectors_on_staff",
                                                                    "next_day_inspection_pct"]].to_dict("records")}


# ---------------------------------------------------------------- Module 09: budget and use
def ex_budget(hires=None, scenario="base"):
    g = ex_gap(scenario)
    hires = g["plan_capped_4"] if hires is None else hires
    v26 = forecast_all(scenario)[2026]
    rows = []
    need = {"Inspector": inspector_req(v26)[2], "Plan reviewer": reviewer_req(v26)[2],
            "Permit technician": tech_req(v26)[3]}
    need["Supervisor"] = sum(need.values()) / SPAN
    for role, now in ROLES_NOW.items():
        req = need[role]
        rows.append(dict(role=role, on_staff=now, required_2026=round(req, 2), gap=round(now - req, 2),
                         loaded_cost=LOADED_COST[role], gap_cost=round((now - req) * LOADED_COST[role])))
    # inspector shortfall covered by overtime vs hiring, 2026
    short_h = max(0, need["Inspector"] - project_inspectors((0, 0, 0))[0]["effective_fte"]) * AV()
    ot_rate = LOADED_COST["Inspector"] * WAGE_SHARE / 2080 * OT_PREMIUM
    return {"roles_2026": rows, "inspector_shortfall_h_2026_no_hire": round(short_h),
            "overtime_rate_per_h": round(ot_rate, 2), "overtime_cost": round(short_h * ot_rate),
            "ot_h_per_inspector_per_week": round(short_h / ROLES_NOW["Inspector"] / 48, 1),
            "hiring_plan": hires,
            "plan_cost_2026": round(hires[0] * NEW_HIRE_FACTOR * LOADED_COST["Inspector"]),
            "plan_2026_shortfall_h": round(max(0, need["Inspector"] - project_inspectors(tuple(hires))[0]["effective_fte"]) * AV()),
            "plan_2026_bridge_ot_cost": round(max(0, need["Inspector"] - project_inspectors(tuple(hires))[0]["effective_fte"])
                                              * AV() * ot_rate),
            "plan_added_cost_3yr": round(sum(sum(hires[:i]) * LOADED_COST["Inspector"] + hires[i] * NEW_HIRE_FACTOR
                                             * LOADED_COST["Inspector"] for i in range(3)))}


# ---------------------------------------------------------------- Module 10: capstone key
def ex_capstone():
    need, need_fix = {}, {}
    for y, v in forecast_all("base").items():
        need[y] = round(reviewer_req(v)[2], 2)
        old = RESUB["com"]
        RESUB["com"] = 0.35
        need_fix[y] = round(reviewer_req(v)[2], 2)
        RESUB["com"] = old
    sup = project_inspectors((0, 0, 0), role="Plan reviewer")
    lams = load("counter_arrivals").groupby("hour_start").arrivals.mean().values
    u = ut()
    now = counter_positions(lams, u["counter_service"])
    online = counter_positions(lams * 0.7, u["counter_service"])
    v26 = forecast_all("base")[2026]
    back = (v26["res_permits"] + v26["com_permits"]) * u["permit_processing"] / 60 / (1 - INDIRECT["Permit technician"])
    f_now = (sum(r["positions"] for r in now) * COUNTER_DAYS + back) / AV()
    f_onl = (sum(r["positions"] for r in online) * COUNTER_DAYS + back) / AV()
    return {"reviewer_need": need, "reviewer_need_resub_0.35": need_fix,
            "reviewer_supply_no_hire": [dict(year=r["year"], effective=r["effective_fte"]) for r in sup],
            "reviewer_gap_no_hire": {r["year"]: round(r["effective_fte"] - need[r["year"]], 1) for r in sup},
            "counter_positions_now": [r["positions"] for r in now],
            "counter_positions_online_30pct": [r["positions"] for r in online],
            "tech_fte_2026_now": round(f_now, 2), "tech_fte_2026_online": round(f_onl, 2)}


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


EX = {"data_inventory": ex_data_inventory, "unit_times": ex_unit_times, "sampling": ex_sampling,
      "availability": ex_availability, "workload_model": ex_workload_model, "coverage": ex_coverage,
      "queueing": ex_queueing, "ratio": ex_ratio, "forecast": ex_forecast, "supply": ex_supply, "gap": ex_gap,
      "sensitivity": ex_sensitivity, "validate": ex_validate, "budget": ex_budget,
      "capstone": ex_capstone}

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
