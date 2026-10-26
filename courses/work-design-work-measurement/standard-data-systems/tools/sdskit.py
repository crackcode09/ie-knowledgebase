"""sdskit.py - data and calculations for the Standard Data Systems course.

Running case: Harlan Fabrication (fictional) is a sheet-metal job shop with about 3,000 active
part numbers, lots of 5-200 pieces and many changeovers a day. Time-studying every new part is
impossible, so the industrial engineer builds standard data for the press brake area.

    python tools/sdskit.py data          # (re)write data/*.csv (fixed seed)
    python tools/sdskit.py all           # every worked example
    python tools/sdskit.py <name>        # micro, macro, consistency, economics, structure, correlation,
                                         # models, transform, evaluate, validate, apply, capstone

Requires numpy, pandas, scipy, statsmodels. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.outliers_influence import variance_inflation_factor

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

PFD = 0.12                 # personal, fatigue and delay allowance, % of normal time (Harlan convention)
RATE = 68.0                # fully burdened press-brake labor + machine rate, $/standard hour (illustrative)
STEEL = 7.85e-6            # kg per mm^3

# Study-file correction found during model evaluation (Module 08): the analyst keyed 3 bends,
# the drawing and the element sheet both show 8.
CORRECTIONS = {"S27": {"bends": 8}}

# Course-made, ILLUSTRATIVE motion table (seconds). Not taken from any commercial PMTS.
MOTIONS = {
    "reach_short": 0.4,    # reach up to 30 cm
    "reach_long": 0.7,     # reach 30-80 cm
    "grasp_simple": 0.2,
    "grasp_flat_sheet": 0.6,   # slide/lift a flat blank off a stack
    "move_short": 0.5,
    "move_long": 0.9,
    "position_loose": 0.5,
    "position_backgauge": 2.5,   # push blank to two backgauge fingers, check contact
    "release": 0.1,
    "foot_pedal": 0.3,
    "turn_body": 0.8,
}


def _brake_part(rng, n, prefix):
    rows = []
    for i in range(1, n + 1):
        bends = int(rng.integers(1, 13))
        flips = int(rng.binomial(max(bends - 1, 0), 0.35))
        thick = float(rng.choice([1.5, 2.0, 3.0, 4.0, 6.0], p=[.25, .25, .25, .15, .10]))
        length = float(np.round(rng.uniform(150, 2400), -1))
        width = float(np.round(rng.uniform(80, 500), -1))
        weight = round(length * width * thick * STEEL, 2)
        true = 0.18 + 0.092 * bends + 0.11 * flips + 0.021 * weight + 0.00006 * length
        normal = true * rng.normal(1, 0.045)
        rows.append(dict(study=f"{prefix}{i:02d}", bends=bends, flips=flips, length_mm=length, width_mm=width,
                         thickness_mm=thick, weight_kg=weight, normal_min=round(normal, 3)))
    return pd.DataFrame(rows)


def make_data(seed=1946):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}

    # 1. 40 past press-brake run studies (normal minutes per piece), one keying error (S27)
    b = _brake_part(rng, 40, "S")
    b.loc[b.study == "S27", "bends"] = 8
    b.loc[b.study == "S27", "flips"] = 2
    t27 = 0.18 + 0.092 * 8 + 0.11 * 2 + 0.021 * b.loc[b.study == "S27", "weight_kg"] + 0.00006 * b.loc[b.study == "S27", "length_mm"]
    b.loc[b.study == "S27", "normal_min"] = np.round(t27 * 1.01, 3)
    b.loc[b.study == "S27", "bends"] = 3                       # keying error in the study database
    b.to_csv(os.path.join(D, "brake_run_studies.csv"), index=False)
    out["brake_run_studies"] = len(b)

    # 2. 24 press-brake setup studies (normal minutes per setup)
    rows = []
    for i in range(1, 25):
        seg = int(rng.integers(1, 11))
        newp = int(rng.random() < 0.4)
        t = 7.5 + 2.6 * seg + 9.0 * newp + rng.normal(0, 1.5)
        rows.append(dict(study=f"U{i:02d}", tool_segments=seg, new_program=newp, normal_min=round(t, 2)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "brake_setup_studies.csv"), index=False)
    out["brake_setup_studies"] = 24

    # 3. 26 shear load-and-square studies: curvilinear in blank weight
    rows = []
    for i in range(1, 27):
        w = float(np.round(np.exp(rng.uniform(np.log(0.3), np.log(28))), 2))
        t = 0.12 * w ** 0.55 * rng.normal(1, 0.06)
        rows.append(dict(study=f"H{i:02d}", blank_kg=w, normal_min=round(t, 3)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "shear_handling_studies.csv"), index=False)
    out["shear_handling_studies"] = 26

    # 4. Same 6 jobs time-studied by 3 analysts (normal min/piece); analysts differ in rating bias and noise
    jobs = _brake_part(rng, 6, "J")
    rows = []
    for _, r in jobs.iterrows():
        true = 0.18 + 0.092 * r.bends + 0.11 * r.flips + 0.021 * r.weight_kg + 0.00006 * r.length_mm
        for a, bias, sd in [("Analyst 1", 1.00, 0.04), ("Analyst 2", 0.92, 0.05), ("Analyst 3", 1.07, 0.06)]:
            rows.append(dict(job=r.study, analyst=a, bends=r.bends, flips=r.flips, length_mm=r.length_mm,
                             weight_kg=r.weight_kg, normal_min=round(true * bias * rng.normal(1, sd), 3)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "analyst_consistency.csv"), index=False)
    out["analyst_consistency"] = len(rows)

    # 5. 12 new jobs time-studied AFTER the model was built (hold-out validation)
    v = _brake_part(rng, 12, "V")
    v.to_csv(os.path.join(D, "validation_studies.csv"), index=False)
    out["validation_studies"] = 12

    # 6. One week of press-brake jobs with actual clocked hours
    rows = []
    for i in range(1, 31):
        p = _brake_part(rng, 1, "P").iloc[0]
        qty = int(rng.choice([5, 10, 12, 20, 25, 40, 50, 75, 100, 150, 200]))
        seg = int(rng.integers(1, 11))
        newp = int(rng.random() < 0.3)
        true_h = ((7.5 + 2.6 * seg + 9.0 * newp) + qty * (0.18 + 0.092 * p.bends + 0.11 * p.flips + 0.021 * p.weight_kg
                                                            + 0.00006 * p.length_mm)) * (1 + PFD) / 60
        actual = true_h / rng.normal(0.93, 0.08)
        rows.append(dict(job=f"W{i:02d}", part=f"HF-{int(rng.integers(10000, 99999))}", qty=qty, bends=int(p.bends),
                         flips=int(p.flips), length_mm=p.length_mm, weight_kg=p.weight_kg, tool_segments=seg,
                         new_program=newp, actual_h=round(actual, 2)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "week_jobs.csv"), index=False)
    out["week_jobs"] = 30

    # 7. Capstone: turret punch run studies (normal min per sheet), one study with a documented foreign element
    rows = []
    for i in range(1, 37):
        hits = int(rng.integers(20, 401))
        stations = int(rng.integers(1, 13))
        kg = float(np.round(rng.uniform(4, 40), 1))
        t = (0.55 + 0.0042 * hits + 0.16 * stations + 0.028 * kg) * rng.normal(1, 0.04)
        note = ""
        if i == 14:
            t += 1.9
            note = "tool jam cleared during study"
        rows.append(dict(study=f"T{i:02d}", hits=hits, tool_stations=stations, sheet_kg=kg, normal_min=round(t, 3),
                         note=note))
    tp = pd.DataFrame(rows)
    tp.iloc[:30].to_csv(os.path.join(D, "capstone_punch_studies.csv"), index=False)
    tp.iloc[30:].drop(columns="note").to_csv(os.path.join(D, "capstone_punch_holdout.csv"), index=False)
    out["capstone_punch_studies"] = 30
    out["capstone_punch_holdout"] = 6

    # 8. Motion table (illustrative)
    pd.DataFrame([dict(motion=k, seconds=v) for k, v in MOTIONS.items()]).to_csv(
        os.path.join(D, "motion_table_illustrative.csv"), index=False)
    out["motion_table_illustrative"] = len(MOTIONS)
    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"))


def brake(corrected=True):
    b = load("brake_run_studies")
    if corrected:
        for s, fix in CORRECTIONS.items():
            for k, v in fix.items():
                b.loc[b.study == s, k] = v
    return b


def setup_model():
    return smf.ols("normal_min ~ tool_segments + new_program", data=load("brake_setup_studies")).fit()


def run_model(corrected=True):
    return smf.ols("normal_min ~ bends + flips + weight_kg + length_mm", data=brake(corrected)).fit()


RAM_S = 4.5               # press-brake ram approach-form-return per bend, s (machine time; illustrative)


# ---------------------------------------------------------------- Module 01: microscopic
def ex_micro():
    m = MOTIONS
    load_blank = [("reach_long", 1), ("grasp_flat_sheet", 1), ("move_long", 1), ("position_backgauge", 1),
                  ("release", 1), ("foot_pedal", 1)]
    per_bend = [("reach_short", 1), ("grasp_simple", 1), ("move_short", 1), ("position_backgauge", 1),
                ("release", 1), ("foot_pedal", 1)]
    flip = [("grasp_simple", 1), ("turn_body", 1), ("move_short", 1), ("position_loose", 1)]
    s = lambda seq: round(sum(m[k] * n for k, n in seq), 2)
    lb, pb, fl = s(load_blank), s(per_bend), s(flip)
    # a 4-bend, 1-flip part: load + first bend uses load_blank, 3 re-positions, 1 flip, unload (reach+grasp+move+release)
    unload = s([("reach_short", 1), ("grasp_simple", 1), ("turn_body", 1), ("move_long", 1), ("release", 1)])
    check = s([("reach_short", 1), ("grasp_simple", 1), ("position_loose", 1), ("release", 1)])
    part = lb + 3 * pb + fl + unload + check
    return {"load_blank_s": lb, "reposition_per_bend_s": pb, "flip_s": fl, "unload_s": unload, "angle_check_s": check,
            "manual_4bend_1flip_s": round(part, 2),
            "ram_cycle_note": "machine ram time per bend must be added (from the machine, not motions)",
            "ram_s_per_bend_assumed": RAM_S,
            "total_4bend_1flip_min": round((part + 4 * RAM_S) / 60, 3)}


# ---------------------------------------------------------------- Module 02: macroscopic
def ex_macro():
    rm, su = run_model(), setup_model()
    job = dict(bends=4, flips=1, weight_kg=1.2, length_mm=400, tool_segments=3, new_program=0, qty=50)
    run = float(rm.predict(pd.DataFrame([job]))[0])
    setup = float(su.predict(pd.DataFrame([job]))[0])
    std_h = (setup + job["qty"] * run) * (1 + PFD) / 60
    return {"run_formula": {k: round(v, 6) for k, v in rm.params.items()},
            "setup_formula": {k: round(v, 3) for k, v in su.params.items()},
            "job": job, "run_normal_min_pc": round(run, 3), "setup_normal_min": round(setup, 2),
            "job_standard_h": round(std_h, 3), "micro_vs_macro_note": "compare with ex_micro total"}


# ---------------------------------------------------------------- Module 03: advantages
def ex_consistency():
    a = load("analyst_consistency")
    rm = run_model()
    rows = []
    for j, g in a.groupby("job"):
        r = g.iloc[0]
        f = float(rm.predict(pd.DataFrame([dict(bends=r.bends, flips=r.flips, weight_kg=r.weight_kg, length_mm=r.length_mm)]))[0])
        lo, hi = g.normal_min.min(), g.normal_min.max()
        rows.append(dict(job=j, analysts_min=round(lo, 3), analysts_max=round(hi, 3),
                         spread_pct=round(100 * (hi - lo) / g.normal_min.mean(), 1), formula=round(f, 3)))
    t = pd.DataFrame(rows)
    by = a.groupby("analyst").normal_min.mean().round(3).to_dict()
    return {"jobs": t.to_dict("records"), "mean_spread_pct": round(t.spread_pct.mean(), 1),
            "analyst_means": by}


def ex_economics(new_parts=600, ts_h=2.5, sd_h=0.2, dev_h=320, maint_h=60, analyst_rate=55.0, years=3):
    ts_cost = new_parts * ts_h * analyst_rate
    sd_cost_yr = (new_parts * sd_h + maint_h) * analyst_rate
    saving_yr = ts_cost - sd_cost_yr
    payback_months = dev_h * analyst_rate / saving_yr * 12
    return {"time_study_h_per_yr": new_parts * ts_h, "standard_data_h_per_yr": new_parts * sd_h + maint_h,
            "development_h": dev_h, "analyst_hours_saved_per_yr": new_parts * ts_h - (new_parts * sd_h + maint_h),
            "saving_per_yr_$": round(saving_yr), "payback_months": round(payback_months, 1),
            f"net_{years}yr_$": round(years * saving_yr - dev_h * analyst_rate),
            "breakeven_new_parts_per_yr": math.ceil((dev_h / years + maint_h) / (ts_h - sd_h))}


# ---------------------------------------------------------------- Module 05: structure
def ex_structure():
    rm, su = run_model(), setup_model()
    p = {k: round(v, 3) for k, v in rm.params.items()}
    s = {k: round(v, 2) for k, v in su.params.items()}
    sheet = [
        dict(code="PB-10", element="Setup: base (clear, load program, first-piece check)", type="constant", frequency="per lot",
             normal_min=s["Intercept"]),
        dict(code="PB-11", element="Setup: change tooling", type="variable", frequency="per lot",
             normal_min=f"{s['tool_segments']} x tool segments"),
        dict(code="PB-12", element="Setup: write and prove new backgauge program", type="constant", frequency="per lot, if new",
             normal_min=s["new_program"]),
        dict(code="PB-20", element="Run: get blank, load, unload, aside", type="constant", frequency="per piece",
             normal_min=p["Intercept"]),
        dict(code="PB-21", element="Run: position and form one bend", type="variable", frequency="per bend",
             normal_min=p["bends"]),
        dict(code="PB-22", element="Run: flip part between bends", type="variable", frequency="per flip",
             normal_min=p["flips"]),
        dict(code="PB-23", element="Run: handling increment for weight", type="variable", frequency="per kg per piece",
             normal_min=p["weight_kg"]),
        dict(code="PB-24", element="Run: handling increment for part length", type="variable", frequency="per metre per piece",
             normal_min=round(1000 * rm.params["length_mm"], 3)),
    ]
    return {"data_sheet": sheet, "allowance": PFD,
            "job_standard": "standard_h = (setup + qty x run) x (1 + PFD) / 60"}


# ---------------------------------------------------------------- Module 06: regression & correlation
def ex_correlation():
    b = brake()
    cols = ["normal_min", "bends", "flips", "length_mm", "thickness_mm", "weight_kg"]
    r = b[cols].corr().round(3)
    m = smf.ols("normal_min ~ bends", data=b).fit()
    ci = m.conf_int().round(4)
    return {"r_with_time": r["normal_min"].drop("normal_min").to_dict(),
            "r_length_weight": float(r.loc["length_mm", "weight_kg"]),
            "simple_fit": {k: round(v, 4) for k, v in m.params.items()},
            "slope_95ci": [float(ci.loc["bends", 0]), float(ci.loc["bends", 1])],
            "r2": round(m.rsquared, 3), "se_min": round(math.sqrt(m.scale), 3),
            "slope_t": round(m.tvalues["bends"], 1), "n": int(m.nobs)}


# ---------------------------------------------------------------- Module 07: developing models
def _vif(df, cols):
    X = sm.add_constant(df[cols])
    return {c: round(variance_inflation_factor(X.values, i + 1), 2) for i, c in enumerate(cols)}


def ex_models():
    b = brake()
    specs = {"M1 bends": "bends", "M2 +flips": "bends + flips", "M3 +weight": "bends + flips + weight_kg",
             "M4 +length": "bends + flips + weight_kg + length_mm",
             "M5 +thickness": "bends + flips + weight_kg + length_mm + thickness_mm"}
    rows = []
    for name, rhs in specs.items():
        m = smf.ols(f"normal_min ~ {rhs}", data=b).fit()
        # leave-one-out prediction error
        e = []
        for i in b.index:
            mi = smf.ols(f"normal_min ~ {rhs}", data=b.drop(i)).fit()
            e.append(b.loc[i, "normal_min"] - float(mi.predict(b.loc[[i]]).iloc[0]))
        rows.append(dict(model=name, k=len(m.params) - 1, r2=round(m.rsquared, 4), adj_r2=round(m.rsquared_adj, 4),
                         se_min=round(math.sqrt(m.scale), 4), aic=round(m.aic, 1),
                         loocv_rmse=round(float(np.sqrt(np.mean(np.square(e)))), 4),
                         worst_p=round(float(m.pvalues.drop("Intercept").max()), 4)))
    m4 = smf.ols("normal_min ~ bends + flips + weight_kg + length_mm", data=b).fit()
    return {"comparison": rows, "chosen": "M4 +length",
            "M4_length_coef": round(m4.params["length_mm"], 6), "M4_length_p": round(m4.pvalues["length_mm"], 3),
            "vif_M4": _vif(b, ["bends", "flips", "weight_kg", "length_mm"]),
            "vif_M3": _vif(b, ["bends", "flips", "weight_kg"]),
            "setup": {k: round(v, 3) for k, v in setup_model().params.items()},
            "setup_r2": round(setup_model().rsquared, 3), "setup_se": round(math.sqrt(setup_model().scale), 2)}


def ex_transform():
    h = load("shear_handling_studies")
    lin = smf.ols("normal_min ~ blank_kg", data=h).fit()
    h = h.assign(lt=np.log(h.normal_min), lw=np.log(h.blank_kg))
    log = smf.ols("lt ~ lw", data=h).fit()
    a, b = math.exp(log.params["Intercept"]), log.params["lw"]
    pred_log = a * h.blank_kg ** b
    rmse = lambda e: float(np.sqrt(np.mean(np.square(e))))
    # relative error is what matters for light blanks
    light = h.blank_kg < 2
    return {"linear": {k: round(v, 4) for k, v in lin.params.items()}, "linear_r2": round(lin.rsquared, 3),
            "power_a": round(a, 4), "power_b": round(b, 3), "loglog_r2": round(log.rsquared, 3),
            "rmse_linear": round(rmse(h.normal_min - lin.fittedvalues), 4),
            "rmse_power": round(rmse(h.normal_min - pred_log), 4),
            "mean_abs_pct_err_light_linear": round(float(100 * np.mean(np.abs((h.normal_min - lin.fittedvalues) / h.normal_min)[light])), 1),
            "mean_abs_pct_err_light_power": round(float(100 * np.mean(np.abs((h.normal_min - pred_log) / h.normal_min)[light])), 1),
            "predict_0.5kg": {"linear": round(float(lin.params.iloc[0] + lin.params.iloc[1] * 0.5), 3),
                              "power": round(a * 0.5 ** b, 3)},
            "predict_15kg": {"linear": round(float(lin.params.iloc[0] + lin.params.iloc[1] * 15), 3),
                             "power": round(a * 15 ** b, 3)}, "max_kg": float(h.blank_kg.max())}


# ---------------------------------------------------------------- Module 08: evaluating models
def ex_evaluate():
    raw = smf.ols("normal_min ~ bends + flips + weight_kg + length_mm", data=brake(corrected=False)).fit()
    infl = raw.get_influence()
    cook = infl.cooks_distance[0]
    sres = infl.resid_studentized_external
    b0 = brake(corrected=False)
    i = int(np.argmax(cook))
    fixed = run_model()
    resid = fixed.resid
    from scipy import stats
    sw = stats.shapiro(resid)
    bp = sm.stats.het_breuschpagan(resid, fixed.model.exog)
    # prediction interval for a typical new job
    new = pd.DataFrame([dict(bends=4, flips=1, weight_kg=1.2, length_mm=400)])
    pr = fixed.get_prediction(new).summary_frame(alpha=0.05)
    return {"before_fix": {"r2": round(raw.rsquared, 3), "se": round(math.sqrt(raw.scale), 3),
                           "max_cooks_study": b0.study.iloc[i], "max_cooks_d": round(float(cook[i]), 2),
                           "studentized_resid": round(float(sres[i]), 1)},
            "after_fix": {"r2": round(fixed.rsquared, 4), "se": round(math.sqrt(fixed.scale), 4),
                          "params": {k: round(v, 6) for k, v in fixed.params.items()},
                          "max_cooks_d": round(float(fixed.get_influence().cooks_distance[0].max()), 3)},
            "shapiro_p": round(sw.pvalue, 3), "breusch_pagan_p": round(bp[1], 3),
            "pi_4bend": [round(float(pr["obs_ci_lower"].iloc[0]), 3), round(float(pr["obs_ci_upper"].iloc[0]), 3)],
            "fit_4bend": round(float(pr["mean"].iloc[0]), 3),
            "range": {c: [float(brake()[c].min()), float(brake()[c].max())] for c in ["bends", "flips", "weight_kg", "length_mm"]}}


def ex_validate():
    v = load("validation_studies")
    m = run_model()
    v = v.assign(pred=m.predict(v).round(3))
    v = v.assign(err_pct=(100 * (v.pred - v.normal_min) / v.normal_min).round(1))
    tot = 100 * (v.pred.sum() - v.normal_min.sum()) / v.normal_min.sum()
    return {"jobs": v[["study", "bends", "flips", "weight_kg", "length_mm", "normal_min", "pred", "err_pct"]].to_dict("records"),
            "mean_abs_pct_err": round(float(v.err_pct.abs().mean()), 1),
            "max_abs_pct_err": round(float(v.err_pct.abs().max()), 1),
            "within_10pct": int((v.err_pct.abs() <= 10).sum()), "within_5pct": int((v.err_pct.abs() <= 5).sum()),
            "aggregate_err_pct": round(float(tot), 2), "n": len(v)}


# ---------------------------------------------------------------- Module 09: applying
def job_standard(df):
    rm, su = run_model(), setup_model()
    run = rm.predict(df)
    setup = su.predict(df)
    return setup, run, (setup + df.qty * run) * (1 + PFD) / 60


def ex_apply(machines=2, shifts=1, h_per_shift=7.5, utilization=0.85):
    w = load("week_jobs")
    setup, run, std = job_standard(w)
    w = w.assign(setup_min=setup.round(2), run_min=run.round(3), std_h=std.round(3))
    w = w.assign(eff_pct=(100 * w.std_h / w.actual_h).round(1))
    cap = machines * shifts * h_per_shift * 5 * utilization
    big = w.sort_values("std_h", ascending=False).head(3)
    quote = w[w.job == "W01"].iloc[0]
    b = brake()
    out_rng = w[(w.bends > b.bends.max()) | (w.flips > b.flips.max()) | (w.weight_kg > b.weight_kg.max())
                | (w.weight_kg < b.weight_kg.min()) | (w.length_mm > b.length_mm.max()) | (w.length_mm < b.length_mm.min())
                | (w.tool_segments > load("brake_setup_studies").tool_segments.max())]
    setup_share = float((w.setup_min * (1 + PFD) / 60).sum() / w.std_h.sum())
    return {"total_std_h": round(float(w.std_h.sum()), 2), "total_actual_h": round(float(w.actual_h.sum()), 2),
            "dept_eff_pct": round(float(100 * w.std_h.sum() / w.actual_h.sum()), 1),
            "setup_share_pct": round(100 * setup_share, 1),
            "capacity_h": cap, "load_pct": round(float(100 * w.std_h.sum() / cap), 1),
            "low_eff_jobs": w[w.eff_pct < 80][["job", "qty", "std_h", "actual_h", "eff_pct"]].to_dict("records"),
            "biggest": big[["job", "qty", "std_h"]].to_dict("records"),
            "outside_data_range": out_rng[["job", "bends", "flips", "weight_kg", "length_mm"]].to_dict("records"),
            "W01": {k: (float(quote[k]) if k != "part" else quote[k]) for k in ["part", "bends", "flips", "weight_kg", "length_mm", "tool_segments", "new_program", "setup_min", "run_min"]},
            "quote_W01": {"qty": int(quote.qty), "std_h": float(quote.std_h),
                          "labor_$": round(float(quote.std_h) * RATE, 2),
                          "per_piece_$": round(float(quote.std_h) * RATE / int(quote.qty), 2)},
            "lot_size_curve": [dict(qty=q, std_min_per_pc=round(float(
                (setup.iloc[0] + q * run.iloc[0]) * (1 + PFD) / q), 3)) for q in (5, 10, 25, 50, 100, 200)]}


# ---------------------------------------------------------------- Module 10: capstone key
def ex_capstone():
    t = load("capstone_punch_studies")
    t["note"] = t["note"].fillna("")
    raw = smf.ols("normal_min ~ hits + tool_stations + sheet_kg", data=t).fit()
    sr = raw.get_influence().resid_studentized_external
    flag = t.study[np.abs(sr) > 3].tolist()
    good = t[t.note == ""]
    m = smf.ols("normal_min ~ hits + tool_stations + sheet_kg", data=good).fit()
    h = load("capstone_punch_holdout")
    h = h.assign(pred=m.predict(h).round(3))
    h = h.assign(err_pct=(100 * (h.pred - h.normal_min) / h.normal_min).round(1))
    job = pd.DataFrame([dict(hits=180, tool_stations=6, sheet_kg=22.0)])
    run = float(m.predict(job).iloc[0])
    return {"flagged": flag, "max_abs_studentized": round(float(np.abs(sr).max()), 1),
            "raw_r2": round(raw.rsquared, 3), "raw_se": round(math.sqrt(raw.scale), 3),
            "params": {k: round(v, 5) for k, v in m.params.items()}, "r2": round(m.rsquared, 4),
            "se": round(math.sqrt(m.scale), 3), "pvalues": {k: round(v, 4) for k, v in m.pvalues.items()},
            "vif": _vif(good, ["hits", "tool_stations", "sheet_kg"]),
            "holdout": h.to_dict("records"), "holdout_mae_pct": round(float(h.err_pct.abs().mean()), 1),
            "holdout_aggregate_pct": round(float(100 * (h.pred.sum() - h.normal_min.sum()) / h.normal_min.sum()), 2),
            "job_180hits_6st_22kg_normal": round(run, 3),
            "job_40_sheets_std_h": round(40 * run * (1 + PFD) / 60, 3),
            "range": {c: [float(good[c].min()), float(good[c].max())] for c in ["hits", "tool_stations", "sheet_kg"]}}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, (np.floating,)):
        return round(float(o), 4)
    if isinstance(o, (np.integer,)):
        return int(o)
    return o


EX = {"micro": ex_micro, "macro": ex_macro, "consistency": ex_consistency, "economics": ex_economics,
      "structure": ex_structure, "correlation": ex_correlation, "models": ex_models, "transform": ex_transform,
      "evaluate": ex_evaluate, "validate": ex_validate, "apply": ex_apply, "capstone": ex_capstone}

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
