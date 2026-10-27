"""aikit.py - data and calculations for the Efficient AI course.

Running case: Halvorsen Components (fictional), a 600-person manufacturer, has a long list of "AI ideas"
from every department. The continuous-improvement team must decide where AI fits, check the data,
run small pilots, and build a roadmap.

    python tools/aikit.py data           # (re)write data/*.csv (fixed seed)
    python tools/aikit.py all            # every worked example
    python tools/aikit.py <name>         # portfolio, readiness, predict, genai_eval, roi, roadmap

Requires numpy, pandas, scikit-learn, scipy. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
LABOUR_RATE = 48.0          # $ per loaded hour (illustrative)

# function, idea, proposed AI type, annual volume, minutes per item, expected % time saved, annual waste $ avoidable,
# data readiness 1-5, complexity 1-5, risk 1-5, simpler non-AI fix?
IDEAS = [
    ("Finance", "Match supplier invoices to POs and receipts", "ML + rules", 42000, 4.0, 0.60, 15000, 4, 2, 2, ""),
    ("Finance", "Flag unusual expense claims", "ML anomaly detection", 9000, 3.0, 0.30, 20000, 3, 3, 3, ""),
    ("Finance", "AI to chase late approvals", "GenAI agent", 6000, 6.0, 0.50, 0, 3, 3, 2,
     "Fix the approval workflow: approval limits and an escalation rule"),
    ("Customer service", "Triage and route incoming tickets", "ML classification", 24000, 3.0, 0.50, 10000, 3, 2, 2, ""),
    ("Customer service", "Draft replies to common questions", "GenAI with human review", 24000, 8.0, 0.35, 0, 3, 3, 3, ""),
    ("Operations", "Predict unplanned stops on CNC cells", "ML predictive maintenance", 1200, 30.0, 0.25, 180000, 2, 4, 3, ""),
    ("Operations", "Visual inspection of machined surfaces", "Computer vision", 300000, 0.15, 0.70, 60000, 2, 5, 4, ""),
    ("Operations", "Reduce changeover time with AI scheduling", "Optimization", 4000, 25.0, 0.10, 30000, 3, 4, 3,
     "SMED first: separate internal and external setup"),
    ("Supply chain", "Forecast demand for 2,000 SKUs", "ML forecasting", 24000, 5.0, 0.40, 90000, 4, 3, 2, ""),
    ("Supply chain", "Predict late supplier deliveries", "ML classification", 20000, 2.0, 0.30, 70000, 4, 2, 2, ""),
    ("Knowledge", "Search work instructions and specs by question", "GenAI retrieval (RAG)", 30000, 6.0, 0.50, 0, 3, 3, 3, ""),
    ("Knowledge", "Summarize customer complaints for 8D reports", "GenAI summarization", 900, 45.0, 0.40, 0, 3, 2, 3, ""),
    ("HR", "Screen job applicants automatically", "ML ranking", 5000, 10.0, 0.60, 0, 2, 3, 5,
     "Structured screening checklist; high bias and legal risk"),
    ("Sales", "Generate quotes for standard configurations", "Rules engine", 8000, 20.0, 0.70, 25000, 5, 2, 1,
     "Rules-based configurator, not AI"),
]


def make_data(seed=2031):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}
    cols = ["function", "idea", "ai_type", "annual_volume", "minutes_per_item", "time_saved_pct", "waste_avoidable_usd",
            "data_readiness_1to5", "complexity_1to5", "risk_1to5", "simpler_fix"]
    pd.DataFrame(IDEAS, columns=cols).to_csv(os.path.join(D, "use_cases.csv"), index=False)
    out["use_cases"] = len(IDEAS)

    # customer-service ticket extract with typical quality problems
    n = 600
    cats = rng.choice(["Billing", "Delivery", "Technical", "Returns", "Order change"], n, p=[.2, .3, .25, .1, .15])
    variants = {"Billing": ["Billing", "billing", "Invoice"], "Delivery": ["Delivery", "Shipping", "delivery "],
                "Technical": ["Technical", "Tech"], "Returns": ["Returns", "RMA"], "Order change": ["Order change"]}
    cat_raw = [rng.choice(variants[c], p=None) if rng.random() < 0.18 else c for c in cats]
    created = pd.Timestamp("2026-01-05") + pd.to_timedelta(rng.integers(0, 260, n), unit="D")
    created = created.astype(str).tolist()
    for i in rng.choice(n, 9, replace=False):
        created[i] = rng.choice(["2026-13-02", "", "02/30/2026"])
    cust = [f"K{int(x):04d}" for x in rng.integers(1, 900, n)]
    for i in rng.choice(n, 66, replace=False):
        cust[i] = ""
    res = np.round(rng.lognormal(np.log(35), 0.7, n), 0)
    res[rng.choice(n, 30, replace=False)] = np.nan
    res[rng.choice(n, 4, replace=False)] = -1
    resolved_cat = [c if rng.random() > 0.35 else "" for c in cats]     # 35 % never labelled at closure
    ids = [f"T{i:05d}" for i in range(1, n + 1)]
    df = pd.DataFrame(dict(ticket_id=ids, created=created, channel=rng.choice(["email", "phone", "web"], n),
                           customer_id=cust, category_raw=cat_raw, resolution_minutes=res, final_category=resolved_cat))
    dup = df.sample(18, random_state=3)
    df = pd.concat([df, dup]).sample(frac=1, random_state=4).reset_index(drop=True)
    df.to_csv(os.path.join(D, "tickets.csv"), index=False)
    out["tickets"] = len(df)

    # shipment history for late-delivery prediction
    n = 2000
    carrier = rng.choice(["Carrier A", "Carrier B", "Carrier C"], n, p=[.5, .3, .2])
    dist = rng.uniform(50, 2500, n)
    lines = rng.integers(1, 30, n)
    sup = np.round(rng.uniform(60, 100, n), 1)
    friday = (rng.random(n) < 0.2).astype(int)
    z = (-3.3 + 0.0009 * dist + 0.9 * (carrier == "Carrier C") + 0.3 * (carrier == "Carrier B") + 0.03 * lines
         - 0.04 * (sup - 80) + 0.6 * friday)
    late = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(int)
    pd.DataFrame(dict(distance_km=np.round(dist), carrier=carrier, order_lines=lines, supplier_score=sup,
                      friday_dispatch=friday, late=late)).to_csv(os.path.join(D, "shipments.csv"), index=False)
    out["shipments"] = n

    # knowledge-assistant pilot: 60 test questions graded by two reviewers
    # 52 questions answerable from the document set, 8 not answerable
    g_in = ["correct"] * 42 + ["partly correct"] * 7 + ["incorrect"] * 3
    g_out = ["said it did not know"] * 3 + ["fabricated source"] * 2 + ["incorrect"] * 1 + ["correct"] * 2
    grades = np.array(g_in + g_out)
    in_docs = np.array([True] * 52 + [False] * 8)
    order = rng.permutation(60)
    grades, in_docs = grades[order], in_docs[order]
    pd.DataFrame(dict(question=[f"Q{i:02d}" for i in range(1, 61)], answer_in_documents=in_docs, grade=grades)).to_csv(
        os.path.join(D, "assistant_pilot_eval.csv"), index=False)
    out["assistant_pilot_eval"] = 60
    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"), keep_default_na=False, na_values=[""])


# ---------------------------------------------------------------- portfolio (problem first + Lean prioritization)
def portfolio():
    u = load("use_cases")
    u["simpler_fix"] = u.simpler_fix.fillna("")
    u["annual_value_usd"] = (u.annual_volume * u.minutes_per_item / 60 * u.time_saved_pct * LABOUR_RATE
                             + u.waste_avoidable_usd).round(-2)
    u["feasibility"] = ((u.data_readiness_1to5 + (6 - u.complexity_1to5) + (6 - u.risk_1to5)) / 3).round(2)
    vmed = u.annual_value_usd.median()
    u["pick"] = np.where(u.annual_value_usd >= vmed,
                         np.where(u.feasibility >= 3.0, "Implement", "Challenge"),
                         np.where(u.feasibility >= 3.0, "Possible", "Kill/park"))
    u.loc[u.simpler_fix != "", "pick"] = "Fix process first (not AI)"
    return u


def ex_portfolio():
    u = portfolio().sort_values("annual_value_usd", ascending=False)
    return {"value_median_usd": float(u.annual_value_usd.median()),
            "ideas": u[["function", "idea", "ai_type", "annual_value_usd", "feasibility", "pick"]].to_dict("records"),
            "counts": u.pick.value_counts().to_dict()}


# ---------------------------------------------------------------- data readiness audit
def ex_readiness():
    t = load("tickets")
    n = len(t)
    dup = int(t.duplicated().sum())
    dup_ids = int(t.ticket_id.duplicated().sum())
    dates = pd.to_datetime(t.created, format="%Y-%m-%d", errors="coerce")
    invalid_dates = int(dates.isna().sum())
    labels = t.category_raw.str.strip().str.lower()
    canon = {"billing": "billing", "invoice": "billing", "delivery": "delivery", "shipping": "delivery",
             "technical": "technical", "tech": "technical", "returns": "returns", "rma": "returns",
             "order change": "order change"}
    distinct_raw = int(t.category_raw.nunique())
    distinct_clean = int(labels.map(canon).nunique())
    nonstandard = int((~t.category_raw.isin(["Billing", "Delivery", "Technical", "Returns", "Order change"])).sum())
    res = pd.to_numeric(t.resolution_minutes, errors="coerce")
    res_missing = int(res.isna().sum())
    res_invalid = int((res < 0).sum())
    cust_missing = int(t.customer_id.isna().sum())
    labelled = int(t.final_category.notna().sum())
    dims = {
        "Completeness (customer_id present)": 1 - cust_missing / n,
        "Completeness (resolution time present)": 1 - res_missing / n,
        "Validity (dates parse)": 1 - invalid_dates / n,
        "Validity (resolution time >= 0)": 1 - res_invalid / n,
        "Consistency (standard category label)": 1 - nonstandard / n,
        "Uniqueness (no duplicate rows)": 1 - dup / n,
        "Label availability (final category, for ML)": labelled / n,
    }
    score = {k: round(100 * v, 1) for k, v in dims.items()}
    latest = dates.max()
    return {"rows": n, "duplicate_rows": dup, "duplicate_ids": dup_ids, "invalid_dates": invalid_dates,
            "category_labels_raw": distinct_raw, "category_labels_after_mapping": distinct_clean,
            "nonstandard_labels": nonstandard, "resolution_missing": res_missing, "resolution_negative": res_invalid,
            "customer_id_missing": cust_missing, "labelled_for_training": labelled,
            "latest_record": str(latest.date()), "dimension_scores_pct": score,
            "lowest_dimension": min(score, key=score.get)}


# ---------------------------------------------------------------- ML: predicting late shipments
def ex_predict(cost_intervene=40.0, cost_late=400.0, effect=0.6):
    s = load("shipments")
    X = pd.get_dummies(s.drop(columns="late"), columns=["carrier"], drop_first=True).astype(float)
    y = s.late.values
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=7, stratify=y)
    m = LogisticRegression(max_iter=2000).fit(Xtr, ytr)
    p = m.predict_proba(Xte)[:, 1]
    auc = roc_auc_score(yte, p)
    base_rate = float(yte.mean())
    rows = []
    for th in [0.1, 0.15, 0.2, 0.3, 0.4, 0.5]:
        flag = p >= th
        tp = int((flag & (yte == 1)).sum())
        fp = int((flag & (yte == 0)).sum())
        fn = int((~flag & (yte == 1)).sum())
        # value: intervening on a flagged late shipment avoids `effect` of the late cost
        value = tp * effect * cost_late - (tp + fp) * cost_intervene
        rows.append(dict(threshold=th, flagged=int(flag.sum()), caught_late=tp, missed_late=fn,
                         precision=round(tp / max(tp + fp, 1), 3), recall=round(tp / max(tp + fn, 1), 3),
                         net_value_usd=round(value)))
    # simple rule baseline: flag Carrier C or distance > 1500 km
    te = s.loc[Xte.index]
    rule = ((te.carrier == "Carrier C") | (te.distance_km > 1500)).values
    tp = int((rule & (yte == 1)).sum())
    fp = int((rule & (yte == 0)).sum())
    rule_value = tp * effect * cost_late - (tp + fp) * cost_intervene
    best = max(rows, key=lambda r: r["net_value_usd"])
    return {"test_shipments": len(yte), "late_rate": round(base_rate, 3), "auc": round(float(auc), 3),
            "accuracy_if_predict_all_on_time": round(1 - base_rate, 3), "thresholds": rows,
            "rule_baseline": dict(flagged=int(rule.sum()), caught_late=tp, precision=round(tp / max(tp + fp, 1), 3),
                                  recall=round(tp / max(int(yte.sum()), 1), 3), net_value_usd=round(rule_value)),
            "best_threshold": best["threshold"], "model_gain_over_rule_usd": round(best["net_value_usd"] - rule_value)}


# ---------------------------------------------------------------- GenAI pilot evaluation
def wilson(k, n, z=1.96):
    if n == 0:
        return (0, 0)
    p = k / n
    d = 1 + z ** 2 / n
    c = (p + z ** 2 / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z ** 2 / (4 * n ** 2)) / d
    return (round(c - h, 3), round(c + h, 3))


def ex_genai_eval(target_correct=0.85, max_fabricated=0.02):
    e = load("assistant_pilot_eval")
    n = len(e)
    counts = e.grade.value_counts().to_dict()
    k_ok = counts.get("correct", 0)
    k_fab = counts.get("fabricated source", 0)
    in_docs = e[e.answer_in_documents]
    not_docs = e[~e.answer_in_documents]
    return {"questions": n, "counts": counts, "correct_rate": round(k_ok / n, 3), "correct_ci95": wilson(k_ok, n),
            "fabricated_rate": round(k_fab / n, 3), "fabricated_ci95": wilson(k_fab, n),
            "meets_correct_target": k_ok / n >= target_correct, "meets_fabrication_limit": k_fab / n <= max_fabricated,
            "correct_when_answer_in_docs": round(float((in_docs.grade == "correct").mean()), 3),
            "correct_when_not_in_docs": round(float((not_docs.grade == "correct").mean()), 3) if len(not_docs) else None,
            "questions_not_in_docs": int(len(not_docs))}


# ---------------------------------------------------------------- ROI of a pilot (invoice matching)
def roi(volume=42000, minutes=4.0, saved=0.60, adoption=(0.5, 0.85, 0.9), waste=15000, licence=24000,
        integration=60000, run_support=12000, rate=0.10):
    flows = [-integration]
    for a in adoption:
        benefit = volume * minutes / 60 * saved * LABOUR_RATE * a + waste * a
        flows.append(benefit - licence - run_support)
    npv = sum(f / (1 + rate) ** t for t, f in enumerate(flows))
    cum = np.cumsum(flows)
    payback = next((t for t, c in enumerate(cum) if c >= 0), None)
    return flows, npv, payback


def ex_roi():
    flows, npv, pb = roi()
    base = npv
    rows = []
    for name, lo, hi in [("Time saved 40-75 %", dict(saved=0.40), dict(saved=0.75)),
                         ("Adoption -/+ 20 %", dict(adoption=(0.4, 0.68, 0.72)), dict(adoption=(0.6, 1.0, 1.0))),
                         ("Integration cost 90k-40k", dict(integration=90000), dict(integration=40000)),
                         ("Licence 40k-15k/yr", dict(licence=40000), dict(licence=15000)),
                         ("Volume 32k-50k", dict(volume=32000), dict(volume=50000))]:
        rows.append(dict(factor=name, npv_low=round(roi(**lo)[1]), npv_high=round(roi(**hi)[1]),
                         swing=round(abs(roi(**hi)[1] - roi(**lo)[1]))))
    rows.sort(key=lambda r: -r["swing"])
    return {"cash_flows_usd": [round(f) for f in flows], "npv_3yr_usd": round(base), "payback_year": pb,
            "tornado": rows}


# ---------------------------------------------------------------- roadmap
def ex_roadmap():
    u = portfolio()
    phase = {"Implement": "Phase 1 (0-3 months): pilot", "Possible": "Phase 1-2: low-cost quick win",
             "Challenge": "Phase 2-3 (3-18 months): build data and capability first",
             "Kill/park": "Park: revisit yearly", "Fix process first (not AI)": "Now: Lean / automation fix, no AI"}
    u["phase"] = u.pick.map(phase)
    return {"roadmap": u.sort_values(["phase", "annual_value_usd"], ascending=[True, False])[
        ["phase", "idea", "annual_value_usd", "feasibility"]].to_dict("records")}


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


EX = {"portfolio": ex_portfolio, "readiness": ex_readiness, "predict": ex_predict, "genai_eval": ex_genai_eval,
      "roi": ex_roi, "roadmap": ex_roadmap}

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
