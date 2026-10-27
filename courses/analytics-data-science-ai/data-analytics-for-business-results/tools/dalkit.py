"""dalkit.py - data and calculations for the Data Analytics for Business Results course.

Running case: Pinecrest Supply (fictional), a distributor of industrial maintenance, repair and operations (MRO)
supplies with five branches, wants to use its data to grow sales, keep customers and decide better.

    python tools/dalkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/dalkit.py all           # every worked example
    python tools/dalkit.py <name>        # quality, eda, apriori, abtest, regression, classify, segment, bias

Requires numpy, pandas, scipy, statsmodels, scikit-learn. License: MIT
"""
from __future__ import annotations

import itertools
import math
import os
import sys

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from scipy import stats
from sklearn.cluster import KMeans
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, roc_auc_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
BRANCHES = ["North", "South", "East", "West", "Central"]
CATS = ["Safety gloves", "Safety glasses", "Hearing protection", "Cutting tools", "Abrasives", "Fasteners",
        "Adhesives", "Tape", "Lubricants", "Batteries", "Flashlights", "Cable ties"]
STATES = ["IL", "WI", "IN", "IA", "MI"]


def make_data(seed=2033):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}

    # ---- customer master with deliberate quality problems
    n = 400
    cust = pd.DataFrame(dict(
        customer_id=[f"C{i:04d}" for i in range(1, n + 1)],
        name=[f"Company {i:03d} Inc" for i in range(1, n + 1)],
        state=rng.choice(STATES, n),
        postal_code=[f"{rng.integers(46000, 62999)}" for _ in range(n)],
        phone=[f"({rng.integers(200, 999)}) {rng.integers(200, 999)}-{rng.integers(1000, 9999)}" for _ in range(n)],
        email=[f"buyer{i}@company{i}.com" for i in range(1, n + 1)],
        region_id=rng.choice(["R1", "R2", "R3", "R4", "R5"], n),
        signup_date=(pd.Timestamp("2015-01-01") + pd.to_timedelta(rng.integers(0, 3800, n), unit="D")).astype(str),
        last_verified=(pd.Timestamp("2019-01-01") + pd.to_timedelta(rng.integers(0, 2500, n), unit="D")).astype(str),
        credit_limit=np.round(rng.lognormal(np.log(20000), 0.6, n), -2),
        industry=rng.choice(["Manufacturing", "Food", "Utilities", "Construction", "Healthcare"], n)))
    idx = lambda k: rng.choice(n, k, replace=False)
    cust.loc[idx(36), "email"] = ""
    cust.loc[idx(14), "postal_code"] = rng.choice(["ABCDE", "123", "000000"], 14)
    cust.loc[idx(22), "state"] = rng.choice(["Ill.", "illinois", "Wisc", "wi"], 22)
    cust.loc[idx(18), "phone"] = [f"{rng.integers(2000000000, 9999999999)}" for _ in range(18)]
    cust.loc[idx(5), "signup_date"] = "2027-03-01"
    cust.loc[idx(9), "region_id"] = "R9"                     # not in region table
    cust.loc[idx(7), "credit_limit"] = -1
    dups = cust.sample(12, random_state=5).copy()
    dups["customer_id"] = [f"C{i:04d}" for i in range(401, 413)]
    dups["name"] = dups.name.str.replace(" Inc", " Inc.", regex=False)
    cust = pd.concat([cust, dups], ignore_index=True)
    cust.to_csv(os.path.join(D, "customers.csv"), index=False)
    pd.DataFrame(dict(region_id=["R1", "R2", "R3", "R4", "R5"],
                      region=["Chicago", "Milwaukee", "Indianapolis", "Des Moines", "Detroit"])).to_csv(
        os.path.join(D, "regions.csv"), index=False)
    out["customers"] = len(cust)

    # ---- orders and baskets (association patterns planted)
    bundles = [(["Safety gloves", "Safety glasses", "Hearing protection"], 0.22),
               (["Cutting tools", "Abrasives"], 0.18), (["Batteries", "Flashlights"], 0.12),
               (["Adhesives", "Tape"], 0.12)]
    orders, lines = [], []
    ids = cust.customer_id.iloc[:400].values
    for o in range(1, 4001):
        c = rng.choice(ids)
        br = BRANCHES[int(c[1:]) % 5]
        date = pd.Timestamp("2025-01-01") + pd.Timedelta(days=int(rng.integers(0, 365)))
        items = set()
        for b, p in bundles:
            if rng.random() < p:
                for it in b:
                    if rng.random() < 0.85:
                        items.add(it)
        k = rng.integers(1, 4)
        items.update(rng.choice(CATS, k, replace=False))
        value = sum(rng.lognormal(np.log(90), 0.6) for _ in items) * {"North": 1.0, "South": 0.9, "East": 1.15,
                                                                        "West": 1.05, "Central": 0.95}[br]
        orders.append(dict(order_id=f"O{o:05d}", customer_id=c, branch=br, date=str(date.date()),
                           items=len(items), order_value=round(value, 2)))
        for it in sorted(items):
            lines.append(dict(order_id=f"O{o:05d}", category=it))
    pd.DataFrame(orders).to_csv(os.path.join(D, "orders.csv"), index=False)
    pd.DataFrame(lines).to_csv(os.path.join(D, "order_lines.csv"), index=False)
    out["orders"], out["order_lines"] = 4000, len(lines)

    # ---- A/B test: reorder-reminder email, control vs variant
    nA, nB = 1200, 1200
    convA = rng.binomial(1, 0.081, nA)
    convB = rng.binomial(1, 0.104, nB)
    ab = pd.DataFrame(dict(customer_group=["A control"] * nA + ["B reminder"] * nB, converted=np.r_[convA, convB]))
    ab.to_csv(os.path.join(D, "ab_test.csv"), index=False)
    out["ab_test"] = nA + nB

    # ---- branch monthly data for regression
    rows = []
    for b, base in zip(BRANCHES, [410, 360, 470, 430, 380]):
        reps = rng.integers(4, 9)
        for m in range(24):
            mkt = round(float(rng.uniform(8, 30)), 1)              # $k
            acc = int(rng.normal(300, 40))
            reps_m = int(max(3, reps + rng.integers(-1, 2)))
            season = 25 * math.sin(2 * math.pi * (m % 12 - 2) / 12)
            sales = base * 0 + 120 + 4.2 * mkt + 22 * reps_m + 0.55 * acc + season + rng.normal(0, 18)
            rows.append(dict(branch=b, month=m + 1, marketing_k=mkt, sales_reps=reps_m, active_accounts=acc,
                             sales_k=round(sales, 1)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "branch_monthly.csv"), index=False)
    out["branch_monthly"] = len(rows)

    # ---- customer churn features
    n = 1500
    tenure = rng.integers(1, 15, n)
    orders_ly = rng.poisson(14, n)
    days_since = rng.integers(1, 200, n)
    tickets = rng.poisson(1.5, n)
    disc = np.round(rng.uniform(0, 0.25, n), 3)
    z = -2.2 - 0.12 * tenure - 0.08 * orders_ly + 0.016 * days_since + 0.35 * tickets - 3 * disc
    churn = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)
    pd.DataFrame(dict(tenure_years=tenure, orders_last_year=orders_ly, days_since_last_order=days_since,
                      support_tickets=tickets, avg_discount=disc, churned=churn)).to_csv(
        os.path.join(D, "churn.csv"), index=False)
    out["churn"] = n
    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"), keep_default_na=False, na_values=[""])


# ---------------------------------------------------------------- data quality (12 dimensions)
def ex_quality(today="2026-10-27"):
    c = load("customers")
    r = load("regions")
    n = len(c)
    t = pd.Timestamp(today)
    signup = pd.to_datetime(c.signup_date, errors="coerce")
    verified = pd.to_datetime(c.last_verified, errors="coerce")
    norm_name = c.name.str.replace(r"[.\s]+", " ", regex=True).str.strip().str.lower()
    dims = {
        "Completeness": 1 - c.email.isna().mean(),
        "Validity (postal code 5 digits)": c.postal_code.astype(str).str.fullmatch(r"\d{5}").mean(),
        "Conformity (phone format)": c.phone.str.fullmatch(r"\(\d{3}\) \d{3}-\d{4}").mean(),
        "Consistency (state code standard)": c.state.isin(STATES).mean(),
        "Uniqueness (no duplicate names)": 1 - norm_name.duplicated().mean(),
        "Integrity (region exists)": c.region_id.isin(r.region_id).mean(),
        "Accuracy / plausibility (no future signup)": (signup <= t).mean(),
        "Reasonableness (credit limit > 0)": (c.credit_limit > 0).mean(),
        "Timeliness (verified within 3 years)": (verified >= t - pd.DateOffset(years=3)).mean(),
    }
    not_measured = ["Relevance", "Accessibility", "Precision / granularity (judged, not computed here)"]
    return {"records": n, "scores_pct": {k: round(100 * float(v), 1) for k, v in dims.items()},
            "not_computed_automatically": not_measured,
            "duplicate_name_records": int(norm_name.duplicated().sum()),
            "worst": min(dims, key=dims.get)}


# ---------------------------------------------------------------- descriptive / EDA
def ex_eda():
    o = load("orders")
    g = o.groupby("branch").order_value
    tab = pd.DataFrame(dict(orders=g.size(), mean=g.mean(), median=g.median(), sd=g.std(),
                            iqr=g.quantile(0.75) - g.quantile(0.25)))
    tab["cv_pct"] = 100 * tab.sd / tab["mean"]
    q1, q3 = o.order_value.quantile([0.25, 0.75])
    out_hi = int((o.order_value > q3 + 1.5 * (q3 - q1)).sum())
    return {"orders": len(o), "revenue": round(float(o.order_value.sum())),
            "mean": round(float(o.order_value.mean()), 2), "median": round(float(o.order_value.median()), 2),
            "sd": round(float(o.order_value.std()), 2), "skew": round(float(o.order_value.skew()), 2),
            "outliers_1.5iqr": out_hi, "by_branch": tab.round(2).reset_index().to_dict("records")}


# ---------------------------------------------------------------- association rules (Apriori)
def apriori(min_support=0.05):
    L = load("order_lines")
    baskets = L.groupby("order_id").category.apply(frozenset)
    n = len(baskets)
    supp = {}
    level = [frozenset([c]) for c in sorted(L.category.unique())]
    k = 1
    while level:
        counts = {s: sum(1 for b in baskets if s <= b) / n for s in level}
        frequent = {s: v for s, v in counts.items() if v >= min_support}
        supp.update(frequent)
        items = sorted({i for s in frequent for i in s})
        k += 1
        cand = set()
        for a, b in itertools.combinations(list(frequent), 2):
            u = a | b
            if len(u) == k and all(frozenset(x) in frequent for x in itertools.combinations(u, k - 1)):
                cand.add(u)
        level = list(cand)
    return supp, n


def ex_apriori(min_support=0.05, min_conf=0.5):
    supp, n = apriori(min_support)
    rules = []
    for s, v in supp.items():
        if len(s) < 2:
            continue
        for r in range(1, len(s)):
            for ante in itertools.combinations(sorted(s), r):
                a = frozenset(ante)
                cons = s - a
                conf = v / supp[a]
                lift = conf / supp[cons]
                if conf >= min_conf:
                    rules.append(dict(rule=f"{' + '.join(sorted(a))} -> {' + '.join(sorted(cons))}",
                                      support=round(v, 3), confidence=round(conf, 3), lift=round(lift, 2)))
    rules.sort(key=lambda r: -r["lift"])
    pairs = []
    for s, v in supp.items():
        if len(s) == 2:
            a_, b_ = sorted(s)
            for x, y in [(a_, b_), (b_, a_)]:
                conf = v / supp[frozenset([x])]
                pairs.append(dict(rule=f"{x} -> {y}", support=round(v, 3), confidence=round(conf, 3),
                                  lift=round(conf / supp[frozenset([y])], 2)))
    pairs.sort(key=lambda r: -r["lift"])
    return {"orders": n, "frequent_itemsets": len(supp), "rules": rules[:10], "rules_total": len(rules),
            "top_pair_rules": pairs[:10],
            "support_single": {next(iter(k)): round(v, 3) for k, v in supp.items() if len(k) == 1}}


# ---------------------------------------------------------------- hypothesis testing
def ex_abtest():
    ab = load("ab_test")
    g = ab.groupby("customer_group").converted.agg(["sum", "count"])
    (xa, na), (xb, nb) = g.loc["A control"].values, g.loc["B reminder"].values
    pa, pb = xa / na, xb / nb
    p = (xa + xb) / (na + nb)
    se = math.sqrt(p * (1 - p) * (1 / na + 1 / nb))
    z = (pb - pa) / se
    pval = 2 * (1 - stats.norm.cdf(abs(z)))
    se2 = math.sqrt(pa * (1 - pa) / na + pb * (1 - pb) / nb)
    ci = (pb - pa - 1.96 * se2, pb - pa + 1.96 * se2)
    o = load("orders")
    t = stats.ttest_ind(o[o.branch == "East"].order_value, o[o.branch == "South"].order_value, equal_var=False)
    return {"conversion_A": round(pa, 4), "conversion_B": round(pb, 4), "lift_points": round(100 * (pb - pa), 2),
            "z": round(z, 2), "p_value": round(pval, 4), "ci95_diff_points": [round(100 * ci[0], 2), round(100 * ci[1], 2)],
            "east_vs_south_order_value_t": round(float(t.statistic), 2), "east_vs_south_p": float(f"{t.pvalue:.2e}")}


# ---------------------------------------------------------------- regression and model evaluation
def ex_regression():
    b = load("branch_monthly")
    slr = smf.ols("sales_k ~ marketing_k", data=b).fit()
    mlr = smf.ols("sales_k ~ marketing_k + sales_reps + active_accounts", data=b).fit()
    train, test = b[b.month <= 18], b[b.month > 18]
    m = smf.ols("sales_k ~ marketing_k + sales_reps + active_accounts", data=train).fit()
    pred = m.predict(test)
    err = test.sales_k - pred
    naive = train.sales_k.mean()
    X = b[["marketing_k", "sales_reps", "active_accounts"]].values
    y = b.sales_k.values
    cv = cross_val_score(LinearRegression(), X, y, cv=KFold(5, shuffle=True, random_state=1),
                         scoring="neg_root_mean_squared_error")
    return {"slr": {k: round(v, 3) for k, v in slr.params.items()}, "slr_r2": round(slr.rsquared, 3),
            "mlr": {k: round(v, 3) for k, v in mlr.params.items()}, "mlr_r2": round(mlr.rsquared, 3),
            "mlr_adj_r2": round(mlr.rsquared_adj, 3), "mlr_pvalues": {k: round(v, 4) for k, v in mlr.pvalues.items()},
            "holdout_months": "19-24", "holdout_rmse": round(float(np.sqrt((err ** 2).mean())), 1),
            "holdout_mae": round(float(err.abs().mean()), 1),
            "holdout_mape_pct": round(float(100 * (err.abs() / test.sales_k).mean()), 1),
            "naive_mean_rmse": round(float(np.sqrt(((test.sales_k - naive) ** 2).mean())), 1),
            "cv5_rmse": round(float(-cv.mean()), 1)}


def ex_classify(threshold=0.15):
    c = load("churn")
    X = c.drop(columns="churned")
    y = c.churned.values
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=3, stratify=y)
    sc = StandardScaler().fit(Xtr)
    lr = LogisticRegression(max_iter=1000).fit(sc.transform(Xtr), ytr)
    p = lr.predict_proba(sc.transform(Xte))[:, 1]
    tree = DecisionTreeClassifier(max_depth=3, random_state=0).fit(Xtr, ytr)
    pt = tree.predict_proba(Xte)[:, 1]

    def metrics(pred):
        tn, fp, fn, tp = confusion_matrix(yte, pred).ravel()
        return dict(tp=int(tp), fp=int(fp), fn=int(fn), tn=int(tn), accuracy=round((tp + tn) / len(yte), 3),
                    precision=round(tp / max(tp + fp, 1), 3), recall=round(tp / max(tp + fn, 1), 3),
                    f1=round(2 * tp / max(2 * tp + fp + fn, 1), 3))
    return {"churn_rate": round(float(y.mean()), 3), "test_n": len(yte),
            "logistic_auc": round(float(roc_auc_score(yte, p)), 3), "tree_auc": round(float(roc_auc_score(yte, pt)), 3),
            "logistic_at_0.5": metrics((p >= 0.5).astype(int)), f"logistic_at_{threshold}": metrics((p >= threshold).astype(int)),
            "baseline_all_stay": metrics(np.zeros(len(yte), dtype=int)),
            "coefficients_standardized": {k: round(float(v), 3) for k, v in zip(X.columns, lr.coef_[0])}}


def ex_segment(k=4):
    o = load("orders")
    o["date"] = pd.to_datetime(o.date)
    end = o.date.max() + pd.Timedelta(days=1)
    rfm = o.groupby("customer_id").agg(recency=("date", lambda d: (end - d.max()).days),
                                       frequency=("order_id", "count"), monetary=("order_value", "sum"))
    Z = StandardScaler().fit_transform(np.c_[rfm.recency, np.log1p(rfm.frequency), np.log1p(rfm.monetary)])
    km = KMeans(n_clusters=k, n_init=20, random_state=0).fit(Z)
    rfm["segment"] = km.labels_
    prof = rfm.groupby("segment").agg(customers=("recency", "size"), recency_days=("recency", "median"),
                                      orders=("frequency", "median"), revenue=("monetary", "median")).round(0)
    share = (rfm.groupby("segment").monetary.sum() / rfm.monetary.sum() * 100).round(1)
    prof["revenue_share_pct"] = share
    return {"customers": len(rfm), "segments": prof.sort_values("revenue", ascending=False).reset_index().to_dict("records")}


def ex_bias():
    """Survivorship bias: average tenure looks high if you only look at customers who stayed."""
    c = load("churn")
    return {"avg_tenure_all": round(float(c.tenure_years.mean()), 2),
            "avg_tenure_survivors": round(float(c[c.churned == 0].tenure_years.mean()), 2),
            "avg_tickets_survivors": round(float(c[c.churned == 0].support_tickets.mean()), 2),
            "avg_tickets_churned": round(float(c[c.churned == 1].support_tickets.mean()), 2)}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, np.floating):
        return round(float(o), 4)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


EX = {"quality": ex_quality, "eda": ex_eda, "apriori": ex_apriori, "abtest": ex_abtest, "regression": ex_regression,
      "classify": ex_classify, "segment": ex_segment, "bias": ex_bias}

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
