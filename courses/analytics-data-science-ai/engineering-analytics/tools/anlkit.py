"""anlkit.py - data and worked examples for the Introduction to Engineering Analytics course.

Running case: Ridgeway Industrial (fictional), which makes and distributes industrial fittings.

    python tools/anlkit.py data        # (re)write data/*.csv, data/ridgeway.db (SQLite) and data/ridgeway.xlsx
    python tools/anlkit.py all         # every worked example
    python tools/anlkit.py <name>      # sql, describe, segment, abc, classify, regress, pca, forecast, optimize

Requires numpy, pandas, scipy, scikit-learn, statsmodels; openpyxl for the Excel workbook. License: MIT
"""
from __future__ import annotations

import os
import sqlite3
import sys

import numpy as np
import pandas as pd

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
DB = os.path.join(D, "ridgeway.db")


# ---------------------------------------------------------------- data
def make_data(seed=2027):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)

    # 1. Customers (300): three latent segments
    seg_spec = [("Key accounts", 40, 420_000, 120, 0.010, 20), ("Regular OEMs", 140, 85_000, 40, 0.020, 35),
                ("Occasional buyers", 120, 9_000, 6, 0.045, 140)]
    rows, cid = [], 0
    for name, n, rev, orders, ret, rec in seg_spec:
        for _ in range(n):
            cid += 1
            o = max(1, int(rng.normal(orders, orders * 0.25)))
            r = max(1500.0, rng.lognormal(np.log(rev), 0.35))
            rows.append(dict(customer_id=f"C{cid:03d}", region=rng.choice(["North", "South", "East", "West"]),
                             annual_revenue=round(r, -2), orders_per_year=o, avg_order_value=round(r / o, 0),
                             return_rate=round(float(np.clip(rng.normal(ret, ret * 0.4), 0, 0.2)), 3),
                             days_since_last_order=int(max(1, rng.normal(rec, rec * 0.35))), true_segment=name))
    cust = pd.DataFrame(rows).sample(frac=1, random_state=1).reset_index(drop=True)
    cust.to_csv(os.path.join(D, "customers.csv"), index=False)

    # 2. SKUs (500) for ABC inventory classification: heavy-tailed annual usage value
    sku = pd.DataFrame(dict(sku=[f"F{i:04d}" for i in range(1, 501)],
                            annual_units=np.round(rng.lognormal(6.0, 1.3, 500)).astype(int),
                            unit_cost=np.round(rng.lognormal(2.2, 0.9, 500), 2)))
    sku.to_csv(os.path.join(D, "skus.csv"), index=False)

    # 3. Machine health snapshots (1,200) with failure within 30 days (label)
    n = 1200
    age = rng.uniform(0, 12, n)
    vib = rng.gamma(4, 0.6, n) + 0.08 * age
    temp = rng.normal(62, 6, n) + 0.9 * vib
    cur = rng.normal(18, 1.5, n)
    hrs = rng.uniform(4, 22, n)
    z = -6.3 + 0.95 * vib + 0.045 * (temp - 60) + 0.12 * age + 0.06 * hrs + rng.normal(0, 0.6, n)
    fail = (rng.uniform(size=n) < 1 / (1 + np.exp(-z))).astype(int)
    pd.DataFrame(dict(machine_id=[f"M{i:04d}" for i in range(n)], age_years=age.round(1), vibration_mm_s=vib.round(2),
                      bearing_temp_c=temp.round(1), motor_current_a=cur.round(1), hours_per_day=hrs.round(1),
                      failed_within_30d=fail)).to_csv(os.path.join(D, "machine_health.csv"), index=False)

    # 4. Daily plant energy (2 years of weekdays)
    days = pd.bdate_range("2025-01-01", "2026-12-31")
    doy = days.dayofyear.values
    out_temp = 10 - 14 * np.cos(2 * np.pi * (doy - 20) / 365) + rng.normal(0, 3, len(days))
    units = np.round(rng.normal(5200, 650, len(days))).astype(int)
    shifts = rng.choice([2, 3], len(days), p=[0.6, 0.4])
    kwh = 9_000 + 2.1 * units + 2_400 * (shifts == 3) + 85 * np.abs(out_temp - 15) + rng.normal(0, 700, len(days))
    pd.DataFrame(dict(date=days.date, units_produced=units, shifts=shifts, outdoor_temp_c=out_temp.round(1),
                      kwh=kwh.round(0).astype(int))).to_csv(os.path.join(D, "plant_energy.csv"), index=False)

    # 5. Monthly sales (60 months): trend + seasonality
    m = pd.period_range("2022-01", periods=60, freq="M")
    t = np.arange(60)
    season = np.array([0.92, 0.95, 1.05, 1.06, 1.08, 1.02, 0.90, 0.94, 1.06, 1.09, 1.03, 0.90])
    sales = (1_800 + 14 * t) * season[t % 12] + rng.normal(0, 55, 60)
    pd.DataFrame(dict(month=m.astype(str), sales_k=sales.round(1))).to_csv(os.path.join(D, "monthly_sales.csv"), index=False)

    # 6. Process data (400 batches): 10 correlated sensors driven by 3 latent factors -> yield
    nb = 400
    f = rng.normal(size=(nb, 3))
    load = np.array([[0.9, 0.1, 0.0], [0.85, 0.2, 0.1], [0.8, 0.0, 0.2], [0.1, 0.9, 0.0], [0.2, 0.85, 0.1],
                     [0.0, 0.8, 0.3], [0.1, 0.1, 0.9], [0.0, 0.2, 0.85], [0.3, 0.1, 0.8], [0.5, 0.5, 0.0]])
    X = f @ load.T + rng.normal(0, 0.35, (nb, 10))
    y = 92 + 1.6 * f[:, 0] - 1.1 * f[:, 1] + 0.4 * f[:, 2] + rng.normal(0, 0.8, nb)
    names = ["zone1_temp", "zone2_temp", "zone3_temp", "line_speed", "tension", "feed_rate", "humidity",
             "dryer_air", "coolant_flow", "power_kw"]
    proc = pd.DataFrame(X.round(3), columns=names)
    proc["yield_pct"] = y.round(2)
    proc.to_csv(os.path.join(D, "process_batches.csv"), index=False)

    # 7. Star-schema order history in SQLite
    prods = pd.DataFrame(dict(product_id=[f"P{i}" for i in range(1, 13)],
                              family=["Elbows"] * 4 + ["Tees"] * 4 + ["Valves"] * 4,
                              list_price=[4.2, 5.1, 6.8, 9.9, 5.5, 6.4, 8.2, 11.5, 22.0, 31.0, 44.0, 63.0]))
    dates = pd.DataFrame(dict(date=pd.date_range("2026-01-01", "2026-12-31").date))
    dates["month"] = pd.to_datetime(dates.date).dt.month
    dates["quarter"] = pd.to_datetime(dates.date).dt.quarter
    orders = []
    cust_w = cust.annual_revenue / cust.annual_revenue.sum()
    for oid in range(1, 4001):
        c = cust.customer_id.iloc[rng.choice(len(cust), p=cust_w)]
        p = prods.iloc[rng.integers(0, 12)]
        q = int(rng.choice([10, 25, 50, 100, 200, 500], p=[0.15, 0.2, 0.25, 0.2, 0.12, 0.08]))
        d = dates.date.iloc[rng.integers(0, len(dates))]
        orders.append(dict(order_id=oid, date=str(d), customer_id=c, product_id=p.product_id, qty=q,
                           net_price=round(p.list_price * rng.uniform(0.82, 1.0), 2)))
    orders = pd.DataFrame(orders)
    if os.path.exists(DB):
        os.remove(DB)
    with sqlite3.connect(DB) as con:
        cust.drop(columns="true_segment").to_sql("dim_customer", con, index=False)
        prods.to_sql("dim_product", con, index=False)
        dates.assign(date=dates.date.astype(str)).to_sql("dim_date", con, index=False)
        orders.to_sql("fact_orders", con, index=False)

    # 8. Excel workbook with the main datasets (for spreadsheet users)
    with pd.ExcelWriter(os.path.join(D, "ridgeway.xlsx")) as xw:
        cust.drop(columns="true_segment").to_excel(xw, sheet_name="customers", index=False)
        sku.to_excel(xw, sheet_name="skus", index=False)
        for name in ("monthly_sales", "plant_energy", "machine_health"):
            pd.read_csv(os.path.join(D, f"{name}.csv")).to_excel(xw, sheet_name=name, index=False)
    return "data written"


def load(name):
    return pd.read_csv(os.path.join(D, name))


# ---------------------------------------------------------------- examples
def ex_sql():
    q = {
        "revenue by product family": """
            SELECT p.family, ROUND(SUM(f.qty * f.net_price), 0) AS revenue, COUNT(*) AS orders
            FROM fact_orders f JOIN dim_product p ON f.product_id = p.product_id
            GROUP BY p.family ORDER BY revenue DESC""",
        "revenue by quarter": """
            SELECT d.quarter, ROUND(SUM(f.qty * f.net_price), 0) AS revenue
            FROM fact_orders f JOIN dim_date d ON f.date = d.date
            GROUP BY d.quarter ORDER BY d.quarter""",
        "top 5 customers": """
            SELECT f.customer_id, c.region, ROUND(SUM(f.qty * f.net_price), 0) AS revenue
            FROM fact_orders f JOIN dim_customer c ON f.customer_id = c.customer_id
            GROUP BY f.customer_id ORDER BY revenue DESC LIMIT 5""",
        "average discount by region (%)": """
            SELECT c.region, ROUND(100 * (1 - AVG(f.net_price / p.list_price)), 1) AS avg_discount_pct
            FROM fact_orders f JOIN dim_customer c ON f.customer_id = c.customer_id
                               JOIN dim_product p ON f.product_id = p.product_id
            GROUP BY c.region ORDER BY c.region""",
    }
    out = {}
    with sqlite3.connect(DB) as con:
        for k, sql in q.items():
            out[k] = pd.read_sql(sql, con).to_dict("records")
    return out


def ex_describe():
    e = load("plant_energy.csv")
    c = load("customers.csv")
    return {"energy: rows, date range": (len(e), e.date.min(), e.date.max()),
            "kWh mean / median / SD": (round(e.kwh.mean()), round(e.kwh.median()), round(e.kwh.std())),
            "kWh per unit (mean)": round((e.kwh / e.units_produced).mean(), 2),
            "customer revenue mean / median": (round(c.annual_revenue.mean()), round(c.annual_revenue.median())),
            "customer revenue skew": round(float(c.annual_revenue.skew()), 2),
            "share of revenue from top 20% of customers %": round(
                100 * c.annual_revenue.nlargest(int(0.2 * len(c))).sum() / c.annual_revenue.sum(), 1),
            "missing values (all customer fields)": int(c.isna().sum().sum())}


def ex_segment():
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import silhouette_score, adjusted_rand_score
    c = load("customers.csv")
    feats = ["annual_revenue", "orders_per_year", "return_rate", "days_since_last_order"]
    X = c[feats].copy()
    X["annual_revenue"] = np.log10(X["annual_revenue"])          # tame the skew before clustering
    Z = StandardScaler().fit_transform(X)
    sil = {}
    for k in range(2, 7):
        km = KMeans(n_clusters=k, n_init=20, random_state=0).fit(Z)
        sil[k] = round(silhouette_score(Z, km.labels_), 3)
    km = KMeans(n_clusters=3, n_init=20, random_state=0).fit(Z)
    c["cluster"] = km.labels_
    prof = c.groupby("cluster").agg(customers=("customer_id", "count"), median_revenue=("annual_revenue", "median"),
                                    median_orders=("orders_per_year", "median"), median_return=("return_rate", "median"),
                                    median_recency=("days_since_last_order", "median"),
                                    revenue_share=("annual_revenue", "sum"))
    prof["revenue_share"] = (100 * prof.revenue_share / prof.revenue_share.sum()).round(1)
    prof = prof.sort_values("median_revenue", ascending=False)
    return {"silhouette by k": sil, "cluster profiles (k=3)": prof.reset_index().round(3).to_dict("records"),
            "agreement with hidden true segments (adjusted Rand index)": round(adjusted_rand_score(c.true_segment, c.cluster), 3)}


def abc_table():
    s = load("skus.csv")
    s["annual_value"] = s.annual_units * s.unit_cost
    s = s.sort_values("annual_value", ascending=False).reset_index(drop=True)
    s["cum_value_pct"] = 100 * s.annual_value.cumsum() / s.annual_value.sum()
    s["cum_sku_pct"] = 100 * (np.arange(len(s)) + 1) / len(s)
    s["class"] = np.where(s.cum_value_pct <= 80, "A", np.where(s.cum_value_pct <= 95, "B", "C"))
    return s


def ex_abc():
    s = abc_table()
    g = s.groupby("class").agg(skus=("sku", "count"), value=("annual_value", "sum"))
    g["% of SKUs"] = (100 * g.skus / g.skus.sum()).round(1)
    g["% of value"] = (100 * g.value / g.value.sum()).round(1)
    return {"total annual usage value": round(s.annual_value.sum()), "classes": g.assign(value=g.value.round(0)).reset_index().to_dict("records"),
            "rule": "A = top 80% of value, B = next 15%, C = last 5%"}


def ex_classify():
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    from sklearn.pipeline import make_pipeline
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import confusion_matrix, roc_auc_score, precision_score, recall_score, accuracy_score
    m = load("machine_health.csv")
    feats = ["age_years", "vibration_mm_s", "bearing_temp_c", "motor_current_a", "hours_per_day"]
    Xtr, Xte, ytr, yte = train_test_split(m[feats], m.failed_within_30d, test_size=0.3, random_state=7,
                                          stratify=m.failed_within_30d)
    out = {"failure rate (all data) %": round(100 * m.failed_within_30d.mean(), 1), "train / test rows": (len(Xtr), len(Xte)),
           "naive 'never fails' accuracy on test %": round(100 * (1 - yte.mean()), 1)}
    lr = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)).fit(Xtr, ytr)
    p = lr.predict_proba(Xte)[:, 1]
    for thr in (0.5, 0.25):
        pred = (p >= thr).astype(int)
        tn, fp, fn, tp = confusion_matrix(yte, pred).ravel()
        out[f"logistic, threshold {thr}"] = {"TP": int(tp), "FP": int(fp), "FN": int(fn), "TN": int(tn),
                                             "accuracy %": round(100 * accuracy_score(yte, pred), 1),
                                             "precision %": round(100 * precision_score(yte, pred), 1),
                                             "recall %": round(100 * recall_score(yte, pred), 1)}
    out["logistic AUC"] = round(roc_auc_score(yte, p), 3)
    coefs = dict(zip(feats, lr[-1].coef_[0].round(2)))
    out["standardized coefficients (bigger = stronger)"] = coefs
    tree = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)
    out["decision tree (depth 3) AUC"] = round(roc_auc_score(yte, tree.predict_proba(Xte)[:, 1]), 3)
    return out


def ex_regress():
    import statsmodels.formula.api as smf
    e = load("plant_energy.csv")
    e["temp_dev"] = (e.outdoor_temp_c - 15).abs()
    e["third_shift"] = (e.shifts == 3).astype(int)
    m1 = smf.ols("kwh ~ units_produced", data=e).fit()
    m2 = smf.ols("kwh ~ units_produced + third_shift + temp_dev", data=e).fit()
    new = pd.DataFrame(dict(units_produced=[6000], third_shift=[1], temp_dev=[20.0]))
    pr = m2.get_prediction(new).summary_frame(alpha=0.05)
    return {"simple model": {"coef units": round(m1.params.units_produced, 3), "R2": round(m1.rsquared, 3),
                             "residual SD (kWh)": round(m1.mse_resid ** 0.5)},
            "multiple model coefficients": m2.params.round(2).to_dict(),
            "multiple model p-values": m2.pvalues.map(lambda v: float(f"{v:.2g}")).to_dict(),
            "multiple model R2 / adj R2": (round(m2.rsquared, 3), round(m2.rsquared_adj, 3)),
            "residual SD (kWh)": round(m2.mse_resid ** 0.5),
            "prediction: 6,000 units, 3 shifts, 20 C from 15 C": {"mean": round(pr["mean"].iloc[0]),
                                                                   "95% prediction interval": (round(pr["obs_ci_lower"].iloc[0]),
                                                                                               round(pr["obs_ci_upper"].iloc[0]))}}


def ex_pca():
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    from sklearn.linear_model import LinearRegression
    from sklearn.model_selection import cross_val_score
    d = load("process_batches.csv")
    X, y = d.drop(columns="yield_pct"), d.yield_pct
    Z = StandardScaler().fit_transform(X)
    pca = PCA().fit(Z)
    ev = pca.explained_variance_ratio_
    load3 = pd.DataFrame(pca.components_[:3].T, index=X.columns, columns=["PC1", "PC2", "PC3"]).round(2)
    corr = np.corrcoef(Z, rowvar=False)
    hi = int(((np.abs(corr) > 0.7) & ~np.eye(10, dtype=bool)).sum() / 2)
    cv = {}
    for k in (1, 2, 3, 5, 10):
        Zk = PCA(n_components=k).fit_transform(Z)
        cv[k] = round(cross_val_score(LinearRegression(), Zk, y, cv=5, scoring="r2").mean(), 3)
    return {"sensor pairs with |r| > 0.7": hi, "variance explained by PC1..PC4 %": (100 * ev[:4]).round(1).tolist(),
            "cumulative, 3 PCs %": round(100 * ev[:3].sum(), 1), "loadings (first 3 PCs)": load3.to_dict("index"),
            "cross-validated R2 of yield model by # of PCs": cv}


def ex_forecast():
    from statsmodels.tsa.holtwinters import ExponentialSmoothing
    s = load("monthly_sales.csv")
    y = s.sales_k.values
    train, test = y[:48], y[48:]

    def mape(a, f):
        return round(100 * float(np.mean(np.abs((a - f) / a))), 2)

    naive = np.repeat(train[-1], 12)
    snaive = train[-12:]
    ma3 = np.repeat(train[-3:].mean(), 12)
    ses = ExponentialSmoothing(train, trend=None, seasonal=None).fit()
    hw = ExponentialSmoothing(train, trend="add", seasonal="mul", seasonal_periods=12).fit()
    f_ses, f_hw = ses.forecast(12), hw.forecast(12)
    hw_all = ExponentialSmoothing(y, trend="add", seasonal="mul", seasonal_periods=12).fit()
    return {"test period": f"{s.month.iloc[48]} to {s.month.iloc[59]}",
            "MAPE % on 12-month holdout": {"naive (last value)": mape(test, naive), "seasonal naive": mape(test, snaive),
                                           "3-month moving average": mape(test, ma3),
                                           "simple exponential smoothing": mape(test, f_ses),
                                           "Holt-Winters (trend + seasonality)": mape(test, f_hw)},
            "Holt-Winters next 3 months (all data, $k)": [round(v, 0) for v in hw_all.forecast(3)]}


def ex_optimize():
    """Weekly product mix: maximize contribution subject to machine-hour and material limits."""
    from scipy.optimize import linprog
    prods = ["Elbow kit", "Tee kit", "Valve kit"]
    margin = np.array([18.0, 22.0, 41.0])                 # $ contribution per kit
    A = np.array([[0.10, 0.12, 0.30],                     # CNC hours per kit
                  [0.05, 0.08, 0.10],                     # assembly hours per kit
                  [1.2, 1.5, 2.6]])                       # brass kg per kit
    b = np.array([160.0, 90.0, 2_200.0])                  # weekly capacity / supply
    bounds = [(0, 700), (0, 600), (0, 300)]               # demand limits
    res = linprog(-margin, A_ub=A, b_ub=b, bounds=bounds, method="highs")
    x = res.x
    use = A @ x
    duals = -res.ineqlin.marginals
    return {"optimal kits per week": dict(zip(prods, np.round(x, 1).tolist())),
            "weekly contribution $": round(-res.fun, 2),
            "resource use / capacity": {r: (round(u, 1), cap) for r, u, cap in zip(["CNC h", "assembly h", "brass kg"], use, b)},
            "shadow prices ($ per extra unit of resource)": dict(zip(["CNC h", "assembly h", "brass kg"], np.round(duals, 2).tolist())),
            "upper-bound (demand) multipliers": dict(zip(prods, np.round(-res.upper.marginals, 2).tolist()))}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"sql": ex_sql, "describe": ex_describe, "segment": ex_segment, "abc": ex_abc, "classify": ex_classify,
      "regress": ex_regress, "pca": ex_pca, "forecast": ex_forecast, "optimize": ex_optimize}

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
