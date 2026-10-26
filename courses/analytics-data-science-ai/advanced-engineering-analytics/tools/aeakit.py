"""aeakit.py - data and worked examples for the Advanced Engineering Analytics course.

Running case: Corbin Packaging (fictional) heat-seals food trays on four lines (L1-L4).
Data arrives from several systems: an Excel production workbook, a quality-lab export,
a maintenance log, daily line sensors and customer orders.

    python tools/aeakit.py data          # (re)write data/ (CSV + Excel workbook, fixed seed)
    python tools/aeakit.py all           # every worked example
    python tools/aeakit.py <name>        # merge, prepare, describe, anova, regression, nonparametric,
                                         # doe, predict_failure, predict_strength, delivery

Requires numpy, pandas, scipy, statsmodels, scikit-learn, openpyxl. License: MIT
"""
from __future__ import annotations

import itertools
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
LINES = ["L1", "L2", "L3", "L4"]
SPEC_MIN_SEAL = 18.0          # N, minimum seal strength


# ---------------------------------------------------------------- data
def make_data(seed=2028):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    days = pd.bdate_range("2026-01-05", "2026-06-26")
    line_eff = {"L1": 0.0, "L2": -1.2, "L3": 0.6, "L4": -2.4}       # seal strength offset (N)
    line_down = {"L1": 25, "L2": 40, "L3": 20, "L4": 75}             # mean unplanned downtime per run (min)
    runs, lab = [], []
    rid = 1000
    for d in days:
        for line in LINES:
            for shift in ("A", "B"):
                rid += 1
                supplier = rng.choice(["FilmCo", "PolyPak"], p=[0.6, 0.4])
                product = rng.choice(["T-200", "T-350", "T-500"], p=[0.5, 0.3, 0.2])
                temp = rng.normal(165, 4)
                dwell = rng.normal(900, 60)
                pres = rng.normal(4.0, 0.3)
                down = rng.gamma(1.4, line_down[line] / 1.4)
                planned = 7.5
                run_h = max(planned - down / 60, 3.0)
                speed = {"T-200": 1500, "T-350": 1200, "T-500": 950}[product]
                units = int(run_h * speed * rng.uniform(0.88, 0.98))
                base = (24 + 0.22 * (temp - 165) + 0.006 * (dwell - 900) + 1.5 * (pres - 4.0)
                        - 0.012 * (temp - 165) ** 2 + line_eff[line] + (-1.0 if supplier == "PolyPak" else 0.0))
                scrap_rate = np.clip(0.012 + 0.004 * max(0, 21 - base) + rng.normal(0, 0.004), 0.002, 0.2)
                scrap = int(units * scrap_rate)
                runs.append(dict(run_id=f"R{rid}", date=d.date(), line=line, shift=shift, product=product,
                                 film_supplier=supplier, planned_hours=planned, run_hours=round(run_h, 2),
                                 unplanned_downtime_min=round(down, 0), units_good=units - scrap, units_scrap=scrap,
                                 seal_temp_c=round(temp, 1), dwell_ms=round(dwell, 0), pressure_bar=round(pres, 2)))
                for s in range(3):
                    lab.append(dict(run_id=f"R{rid}", sample=s + 1, seal_strength_n=round(base + rng.normal(0, 1.6), 2)))
    runs = pd.DataFrame(runs)
    lab = pd.DataFrame(lab)

    # deliberately messy features for the "preparing data" module
    runs = pd.concat([runs, runs.iloc[[37, 410]]], ignore_index=True)            # duplicate rows
    idx = rng.choice(len(runs), 6, replace=False)
    runs.loc[idx[:3], "seal_temp_c"] = (runs.loc[idx[:3], "seal_temp_c"] * 9 / 5 + 32).round(1)   # logged in F
    runs.loc[idx[3:5], "pressure_bar"] = np.nan
    runs.loc[idx[5], "line"] = "l3"
    lab.loc[rng.choice(len(lab), 4, replace=False), "seal_strength_n"] = np.nan

    with pd.ExcelWriter(os.path.join(D, "production_workbook.xlsx")) as xw:
        runs.to_excel(xw, sheet_name="runs", index=False)
        pd.DataFrame(dict(line=LINES, commissioned=[2015, 2017, 2021, 2012],
                          cost_per_run_hour=[410, 395, 430, 380])).to_excel(xw, sheet_name="lines", index=False)
    lab.to_csv(os.path.join(D, "quality_lab.csv"), index=False)

    # maintenance log
    mrows = []
    for line in LINES:
        rate = {"L1": 0.05, "L2": 0.08, "L3": 0.04, "L4": 0.16}[line]
        for d in days:
            if rng.uniform() < rate:
                mode = rng.choice(["heater element", "sealing jaw wear", "conveyor jam", "film tracking", "PLC fault"],
                                  p=[0.3, 0.25, 0.2, 0.15, 0.1])
                mrows.append(dict(date=d.date(), line=line, type="breakdown", failure_mode=mode,
                                  downtime_min=round(rng.lognormal(np.log(70 if line != "L4" else 110), 0.7)),
                                  cost=round(rng.lognormal(np.log(900), 0.6), -1)))
            if d.dayofweek == 4 and rng.uniform() < 0.5:
                mrows.append(dict(date=d.date(), line=line, type="PM", failure_mode="", downtime_min=60, cost=350))
    maint = pd.DataFrame(mrows)
    maint.to_csv(os.path.join(D, "maintenance_log.csv"), index=False)

    # daily sensor features with label: breakdown within next 7 days
    srows = []
    bd = maint[maint.type == "breakdown"][["line", "date"]].copy()
    bd["date"] = pd.to_datetime(bd["date"])
    vib_base = {"L1": 2.0, "L2": 2.9, "L3": 1.4, "L4": 3.3}      # lines differ a lot in normal vibration
    cur_base = {"L1": 12.0, "L2": 13.5, "L3": 11.0, "L4": 12.8}
    for line in LINES:
        bdl = np.sort(bd[bd.line == line].date.values)
        walk_v, walk_c = 0.0, 0.0
        for d in days:
            nxt = bdl[bdl > np.datetime64(d)]
            days_to = (nxt[0] - np.datetime64(d)).astype("timedelta64[D]").astype(int) if len(nxt) else 999
            soon = days_to <= 7
            drift = max(0, 8 - days_to) / 8 if days_to < 999 else 0
            walk_v = 0.9 * walk_v + rng.normal(0, 0.25)            # slow wander of the baseline
            walk_c = 0.9 * walk_c + rng.normal(0, 0.3)
            srows.append(dict(date=d.date(), line=line,
                              vibration_mm_s=round(vib_base[line] + walk_v + 1.1 * drift + rng.normal(0, 0.25), 2),
                              heater_current_a=round(cur_base[line] + walk_c + 0.7 * drift + rng.normal(0, 0.3), 2),
                              motor_temp_c=round(55 + 3 * drift + rng.normal(0, 2.5), 1),
                              jaw_cycles_k=round(rng.uniform(50, 400), 0),
                              ambient_c=round(rng.normal(22, 3), 1),
                              breakdown_within_7d=int(soon)))
    pd.DataFrame(srows).to_csv(os.path.join(D, "line_sensors_daily.csv"), index=False)

    # customer orders and delivery
    orows = []
    for o in range(1, 1201):
        promised = days[rng.integers(5, len(days))]
        line = rng.choice(LINES)
        delay = rng.normal(-1.0 + {"L1": 0, "L2": 0.4, "L3": -0.2, "L4": 1.3}[line], 1.4)
        orows.append(dict(order_id=f"SO{o:05d}", customer=f"CU{rng.integers(1, 41):02d}", line=line,
                          qty=int(rng.choice([5000, 10000, 20000, 40000])), promised=promised.date(),
                          shipped=(promised + pd.Timedelta(days=int(round(delay)))).date()))
    pd.DataFrame(orows).to_csv(os.path.join(D, "customer_orders.csv"), index=False)

    # 2^3 factorial DOE on seal strength, 2 replicates, randomized
    rows = []
    for rep in (1, 2):
        for t, w, p in itertools.product([-1, 1], repeat=3):
            temp, dwell, pres = 160 + 10 * (t + 1) / 2, 800 + 200 * (w + 1) / 2, 3.5 + 1.0 * (p + 1) / 2
            y = (24 + 0.22 * (temp - 165) + 0.006 * (dwell - 900) + 1.5 * (pres - 4.0) - 0.012 * (temp - 165) ** 2
                 + 0.5 * t * w + rng.normal(0, 0.8))
            rows.append(dict(rep=rep, A_temp=t, B_dwell=w, C_pressure=p, temp_c=temp, dwell_ms=dwell, pressure_bar=pres,
                             seal_strength_n=round(y, 2)))
    pd.DataFrame(rows).sample(frac=1, random_state=4).reset_index(drop=True).to_csv(os.path.join(D, "seal_doe.csv"), index=False)
    return "data written"


# ---------------------------------------------------------------- managing, merging, preparing
def read_sources():
    runs = pd.read_excel(os.path.join(D, "production_workbook.xlsx"), sheet_name="runs")
    lines = pd.read_excel(os.path.join(D, "production_workbook.xlsx"), sheet_name="lines")
    lab = pd.read_csv(os.path.join(D, "quality_lab.csv"))
    maint = pd.read_csv(os.path.join(D, "maintenance_log.csv"))
    return runs, lines, lab, maint


def clean_runs(runs):
    r = runs.drop_duplicates().copy()
    r["line"] = r.line.str.strip().str.upper()
    f = r.seal_temp_c > 250                                           # Fahrenheit entries
    r.loc[f, "seal_temp_c"] = ((r.loc[f, "seal_temp_c"] - 32) * 5 / 9).round(1)
    r["date"] = pd.to_datetime(r.date)
    return r


def analysis_table():
    runs, lines, lab, maint = read_sources()
    r = clean_runs(runs)
    labm = lab.groupby("run_id").seal_strength_n.agg(seal_mean="mean", seal_min="min", n_tests="count").reset_index()
    t = r.merge(labm, on="run_id", how="left", validate="one_to_one")
    t = t.merge(lines, on="line", how="left", validate="many_to_one")
    t["units_total"] = t.units_good + t.units_scrap
    t["scrap_rate"] = t.units_scrap / t.units_total
    t["availability"] = t.run_hours / t.planned_hours
    t["cost_per_1000_good"] = 1000 * t.run_hours * t.cost_per_run_hour / t.units_good
    return t


def ex_merge():
    runs, lines, lab, maint = read_sources()
    naive = runs.merge(lab, on="run_id", how="left")
    r = clean_runs(runs)
    t = analysis_table()
    unmatched = int(t.seal_mean.isna().sum())
    return {"rows: runs (raw), lab tests, maintenance events": (len(runs), len(lab), len(maint)),
            "naive join runs x lab tests (fan-out!)": len(naive),
            "runs after de-duplication": len(r),
            "analysis table rows (one per run)": len(t),
            "runs without lab results": unmatched,
            "join key checks": "validate='one_to_one' (runs-lab summary) and 'many_to_one' (runs-lines) passed"}


def ex_prepare():
    runs, _, lab, _ = read_sources()
    f_entries = int((runs.seal_temp_c > 250).sum())
    return {"duplicate rows": int(runs.duplicated().sum()), "seal temps logged in F (>250)": f_entries,
            "missing pressure": int(runs.pressure_bar.isna().sum()), "inconsistent line labels": sorted(set(runs.line) - set(LINES)),
            "missing lab results": int(lab.seal_strength_n.isna().sum()),
            "after cleaning: seal temp range (C)": tuple(analysis_table().seal_temp_c.agg(["min", "max"]).round(1)),
            "decision on missing pressure": "keep row; exclude from models that need pressure (2 rows)"}


def ex_describe():
    t = analysis_table()
    g = t.groupby("line").agg(runs=("run_id", "count"), availability=("availability", "mean"), scrap_rate=("scrap_rate", "mean"),
                              seal_mean=("seal_mean", "mean"), cost_per_1000=("cost_per_1000_good", "median"),
                              downtime_min=("unplanned_downtime_min", "mean"))
    g["availability"] = (100 * g.availability).round(1)
    g["scrap_rate"] = (100 * g.scrap_rate).round(2)
    below = (t.seal_min < SPEC_MIN_SEAL).mean()
    return {"runs analysed": len(t), "by line": g.round(2).reset_index().to_dict("records"),
            "runs with any seal test below 18 N %": round(100 * below, 1),
            "seal strength mean / SD (run means)": (round(t.seal_mean.mean(), 2), round(t.seal_mean.std(), 2))}


def ex_anova():
    import statsmodels.formula.api as smf
    import statsmodels.api as sm
    from statsmodels.stats.multicomp import pairwise_tukeyhsd
    t = analysis_table().dropna(subset=["seal_mean"])
    m1 = smf.ols("seal_mean ~ C(line)", data=t).fit()
    a1 = sm.stats.anova_lm(m1, typ=2)
    m2 = smf.ols("seal_mean ~ C(line) * C(film_supplier)", data=t).fit()
    a2 = sm.stats.anova_lm(m2, typ=2)
    tk = pairwise_tukeyhsd(t.seal_mean, t.line)
    pairs = [(f"{r[0]}-{r[1]}", round(float(r[2]), 3), float(f"{r[3]:.2g}"), bool(r[6])) for r in tk._results_table.data[1:]]
    lev = stats.levene(*[g.seal_mean.values for _, g in t.groupby("line")]).pvalue
    return {"one-way: F, p": (round(a1.F.iloc[0], 1), float(f"{a1['PR(>F)'].iloc[0]:.2g}")),
            "eta-squared (share of variation explained by line)": round(a1.sum_sq.iloc[0] / a1.sum_sq.sum(), 3),
            "two-way (line x supplier) p-values": {k: float(f"{v:.2g}") for k, v in a2["PR(>F)"].dropna().items()},
            "supplier effect (PolyPak - FilmCo, N)": round(t[t.film_supplier == "PolyPak"].seal_mean.mean() - t[t.film_supplier == "FilmCo"].seal_mean.mean(), 2),
            "Tukey pairs (diff, p-adj, reject)": pairs, "Levene p": round(lev, 3)}


def ex_regression():
    import statsmodels.formula.api as smf
    t = analysis_table().dropna(subset=["seal_mean", "pressure_bar"])
    m = smf.ols("seal_mean ~ seal_temp_c + I(seal_temp_c**2) + dwell_ms + pressure_bar + C(film_supplier) + C(line)", data=t).fit()
    m_lin = smf.ols("seal_mean ~ seal_temp_c + dwell_ms + pressure_bar + C(film_supplier) + C(line)", data=t).fit()
    b1, b2 = m.params["seal_temp_c"], m.params["I(seal_temp_c ** 2)"]
    best_t = -b1 / (2 * b2)
    from statsmodels.stats.outliers_influence import variance_inflation_factor
    X = t[["seal_temp_c", "dwell_ms", "pressure_bar"]].assign(const=1.0)
    vif = {c: round(variance_inflation_factor(X.values, i), 2) for i, c in enumerate(X.columns) if c != "const"}
    return {"R2 linear-in-temp / with temp^2": (round(m_lin.rsquared, 3), round(m.rsquared, 3)),
            "coefficients": {k: round(v, 4) for k, v in m.params.items()},
            "p (temp^2)": float(f"{m.pvalues['I(seal_temp_c ** 2)']:.2g}"),
            "temperature giving maximum strength (C)": round(best_t, 1),
            "residual SD (N)": round(m.mse_resid ** 0.5, 3), "VIF (process settings)": vif}


def ex_nonparametric():
    m = pd.read_csv(os.path.join(D, "maintenance_log.csv"))
    b = m[m.type == "breakdown"]
    kw = stats.kruskal(*[g.downtime_min.values for _, g in b.groupby("line")])
    med = b.groupby("line").downtime_min.median().to_dict()
    t = analysis_table()
    mw = stats.mannwhitneyu(t[t.film_supplier == "FilmCo"].scrap_rate, t[t.film_supplier == "PolyPak"].scrap_rate)
    s = pd.read_csv(os.path.join(D, "line_sensors_daily.csv"))
    rho = stats.spearmanr(s.vibration_mm_s, s.breakdown_within_7d)
    rng = np.random.default_rng(7)
    l4 = b[b.line == "L4"].downtime_min.values
    boots = [np.median(rng.choice(l4, len(l4))) for _ in range(5000)]
    sk = stats.skew(b.downtime_min)
    return {"breakdown downtime skewness": round(float(sk), 2), "median breakdown minutes by line": med,
            "Kruskal-Wallis (downtime by line) H, p": (round(kw.statistic, 2), float(f"{kw.pvalue:.2g}")),
            "Mann-Whitney scrap rate FilmCo vs PolyPak: U, p": (float(mw.statistic), float(f"{mw.pvalue:.2g}")),
            "median scrap % FilmCo / PolyPak": (round(100 * t[t.film_supplier == "FilmCo"].scrap_rate.median(), 3),
                                                 round(100 * t[t.film_supplier == "PolyPak"].scrap_rate.median(), 3)),
            "Spearman rho vibration vs breakdown-within-7d": (round(rho.statistic, 3), float(f"{rho.pvalue:.2g}")),
            "L4 median breakdown minutes, bootstrap 95% CI": (float(np.median(l4)), tuple(np.percentile(boots, [2.5, 97.5]).round(1)))}


def ex_doe():
    import statsmodels.formula.api as smf
    d = pd.read_csv(os.path.join(D, "seal_doe.csv"))
    eff = {}
    for combo in ["A_temp", "B_dwell", "C_pressure", "A_temp:B_dwell", "A_temp:C_pressure", "B_dwell:C_pressure",
                  "A_temp:B_dwell:C_pressure"]:
        col = np.prod([d[c] for c in combo.split(":")], axis=0)
        eff[combo] = round(d.seal_strength_n[col > 0].mean() - d.seal_strength_n[col < 0].mean(), 3)
    m = smf.ols("seal_strength_n ~ A_temp * B_dwell * C_pressure", data=d).fit()
    sig = {k: float(f"{v:.2g}") for k, v in m.pvalues.items() if k != "Intercept"}
    cells = d.groupby(["A_temp", "B_dwell", "C_pressure"]).seal_strength_n.mean().sort_values(ascending=False)
    return {"runs": len(d), "effects (high - low, N)": eff, "p-values": sig,
            "best cell (A, B, C) and mean": (cells.index[0], round(cells.iloc[0], 2)), "R2": round(m.rsquared, 3)}


def ex_predict_failure():
    from sklearn.model_selection import StratifiedKFold, cross_val_score, cross_val_predict
    from sklearn.linear_model import LogisticRegression
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import precision_score, recall_score
    s = pd.read_csv(os.path.join(D, "line_sensors_daily.csv"))
    s["L4"] = (s.line == "L4").astype(int)
    s = s.sort_values(["line", "date"])
    for c in ("vibration_mm_s", "heater_current_a", "motor_temp_c"):
        # change versus the line's own recent normal (mean of the previous 14 days)
        s[c + "_7d_trend"] = s.groupby("line")[c].transform(lambda x: x - x.rolling(14, min_periods=3).mean().shift(1))
    s = s.dropna()
    y = s.breakdown_within_7d
    base = ["vibration_mm_s", "heater_current_a", "motor_temp_c", "jaw_cycles_k", "ambient_c"]
    eng = base + ["vibration_mm_s_7d_trend", "heater_current_a_7d_trend", "motor_temp_c_7d_trend"]
    cv = StratifiedKFold(5, shuffle=True, random_state=1)
    models = {"logistic, raw features": (make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)), base),
              "logistic, + trend features": (make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000)), eng),
              "random forest, + trend features": (RandomForestClassifier(300, min_samples_leaf=5, random_state=1), eng),
              "gradient boosting, + trend features": (GradientBoostingClassifier(random_state=1), eng)}
    out = {"days x lines": len(s), "positive rate %": round(100 * y.mean(), 1)}
    for name, (mdl, feats) in models.items():
        auc = cross_val_score(mdl, s[feats], y, cv=cv, scoring="roc_auc")
        out[f"{name}: CV AUC mean (sd)"] = (round(auc.mean(), 3), round(auc.std(), 3))
    best = make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000))
    p = cross_val_predict(best, s[eng], y, cv=cv, method="predict_proba")[:, 1]
    for thr in (0.5, 0.3):
        pred = (p >= thr).astype(int)
        out[f"logistic + trends, threshold {thr}: precision / recall %"] = (round(100 * precision_score(y, pred), 1),
                                                                            round(100 * recall_score(y, pred), 1))
    return out


def ex_predict_strength():
    from sklearn.model_selection import KFold, cross_val_score
    from sklearn.linear_model import LinearRegression
    from sklearn.preprocessing import PolynomialFeatures, OneHotEncoder, StandardScaler
    from sklearn.compose import ColumnTransformer
    from sklearn.pipeline import make_pipeline
    from sklearn.ensemble import GradientBoostingRegressor
    t = analysis_table().dropna(subset=["seal_mean", "pressure_bar"])
    num = ["seal_temp_c", "dwell_ms", "pressure_bar"]
    cat = ["line", "film_supplier"]
    X, y = t[num + cat], t.seal_mean
    cv = KFold(5, shuffle=True, random_state=2)
    pre_lin = ColumnTransformer([("num", StandardScaler(), num), ("cat", OneHotEncoder(drop="first"), cat)])
    pre_quad = ColumnTransformer([("num", make_pipeline(StandardScaler(), PolynomialFeatures(2, include_bias=False)), num),
                                  ("cat", OneHotEncoder(drop="first"), cat)])
    models = {"mean only (baseline)": None, "settings only, linear": make_pipeline(
        ColumnTransformer([("num", StandardScaler(), num)]), LinearRegression()),
        "settings + line + supplier, linear": make_pipeline(pre_lin, LinearRegression()),
        "+ quadratic and interaction terms": make_pipeline(pre_quad, LinearRegression()),
        "gradient boosting": make_pipeline(pre_lin, GradientBoostingRegressor(random_state=2))}
    out = {"runs": len(t)}
    for name, mdl in models.items():
        if mdl is None:
            rmse = float(np.sqrt(np.mean([((y.iloc[te] - y.iloc[tr].mean()) ** 2).mean() for tr, te in cv.split(X)])))
        else:
            rmse = float(np.sqrt(-cross_val_score(mdl, X, y, cv=cv, scoring="neg_mean_squared_error").mean()))
        out[f"{name}: CV RMSE (N)"] = round(rmse, 3)
    out["noise floor: lab SD / sqrt(3)"] = round(1.6 / np.sqrt(3), 3)
    return out


def ex_delivery():
    o = pd.read_csv(os.path.join(D, "customer_orders.csv"), parse_dates=["promised", "shipped"])
    o["late_days"] = (o.shipped - o.promised).dt.days
    o["on_time"] = o.late_days <= 0
    g = o.groupby("line").agg(orders=("order_id", "count"), on_time_pct=("on_time", "mean"), mean_late=("late_days", "mean"))
    g["on_time_pct"] = (100 * g.on_time_pct).round(1)
    chi = stats.chi2_contingency(pd.crosstab(o.line, o.on_time))
    return {"overall on-time %": round(100 * o.on_time.mean(), 1), "by line": g.round(2).reset_index().to_dict("records"),
            "chi-square p (line vs on-time)": float(f"{chi[1]:.2g}")}


def _clean(o):
    if isinstance(o, dict):
        return {(k if isinstance(k, str) else str(k)): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"merge": ex_merge, "prepare": ex_prepare, "describe": ex_describe, "anova": ex_anova, "regression": ex_regression,
      "nonparametric": ex_nonparametric, "doe": ex_doe, "predict_failure": ex_predict_failure,
      "predict_strength": ex_predict_strength, "delivery": ex_delivery}

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
