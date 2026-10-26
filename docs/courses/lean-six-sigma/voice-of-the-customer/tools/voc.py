"""voc.py - data generator and analysis toolkit for the Voice of the Customer course.

Running case: a bearing and linear-motion manufacturer's spare-parts ordering service
for industrial maintenance customers.

    python tools/voc.py data        # (re)generate data/survey.csv
    python tools/voc.py all         # every worked example
    python tools/voc.py <name>      # segments, importance, kano, moe, sim, spec, targets, cematrix

License: MIT
"""
from __future__ import annotations

import csv
import math
import os
import sys
from collections import Counter

import numpy as np
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
DATA = os.path.join(ROOT, "data", "survey.csv")

NEEDS = ["fast_delivery", "right_part_first_time", "order_status_visibility", "easy_part_identification",
         "price", "technical_support"]
KANO_FEATURES = ["order_tracking", "same_day_shipping", "part_finder_by_photo", "consignment_stock"]
SEGMENTS = {"End-user plant (MRO)": 150, "Distributor": 90, "OEM machine builder": 60}


# ------------------------------------------------------------------ data
def make_data(seed=2024):
    rng = np.random.default_rng(seed)
    # mean importance (1-5) by segment for each need
    imp_mu = {"End-user plant (MRO)": [4.7, 4.6, 4.1, 4.3, 3.3, 3.6],
              "Distributor": [4.2, 4.5, 4.4, 3.6, 4.5, 2.9],
              "OEM machine builder": [3.6, 4.4, 3.5, 3.1, 4.4, 4.3]}
    sat_mu = [3.0, 3.9, 2.6, 3.1, 3.4, 3.8]  # current satisfaction 1-5
    # Kano: answer pairs functional (if present) / dysfunctional (if absent)
    # 1 like, 2 must-be, 3 neutral, 4 live-with, 5 dislike
    kano_profiles = {  # probabilities of (functional, dysfunctional) answer pairs per feature
        "order_tracking": {(1, 5): 0.30, (3, 5): 0.12, (2, 5): 0.25, (4, 5): 0.08, (1, 3): 0.12, (1, 4): 0.08, (3, 3): 0.05},
        "same_day_shipping": {(1, 5): 0.42, (1, 4): 0.12, (1, 3): 0.14, (2, 5): 0.12, (3, 3): 0.10, (3, 5): 0.05, (4, 5): 0.05},
        "part_finder_by_photo": {(1, 3): 0.38, (1, 4): 0.20, (3, 3): 0.22, (1, 5): 0.10, (2, 5): 0.04, (3, 4): 0.06},
        "consignment_stock": {(3, 3): 0.40, (1, 3): 0.18, (3, 4): 0.14, (1, 5): 0.08, (5, 1): 0.08, (2, 3): 0.06, (4, 4): 0.06},
    }
    rows = []
    rid = 0
    for seg, n in SEGMENTS.items():
        for _ in range(n):
            rid += 1
            imp = np.clip(np.round(rng.normal(imp_mu[seg], 0.7)), 1, 5).astype(int)
            sat = np.clip(np.round(rng.normal(sat_mu, 0.9)), 1, 5).astype(int)
            base = {"End-user plant (MRO)": 3.5, "Distributor": 5.5, "OEM machine builder": 9.0}[seg]
            max_days = int(np.clip(round(rng.lognormal(math.log(base), 0.4)), 1, 30))
            recommend = int(np.clip(round(rng.normal(6.6 if seg != "OEM machine builder" else 7.4, 2.0)), 0, 10))
            row = {"id": rid, "segment": seg, "max_acceptable_days": max_days, "likely_to_recommend": recommend}
            for k, v in zip(NEEDS, imp):
                row[f"imp_{k}"] = int(v)
            for k, v in zip(NEEDS, sat):
                row[f"sat_{k}"] = int(v)
            for f in KANO_FEATURES:
                pairs, probs = zip(*kano_profiles[f].items())
                fa, da = pairs[rng.choice(len(pairs), p=np.array(probs) / sum(probs))]
                row[f"kano_{f}_func"], row[f"kano_{f}_dysf"] = fa, da
            rows.append(row)
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    with open(DATA, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    return len(rows)


def load():
    with open(DATA, newline="") as fh:
        return list(csv.DictReader(fh))


# ------------------------------------------------------------------ analysis
KANO_TABLE = {  # rows: functional answer 1..5, cols: dysfunctional answer 1..5
    1: ["Q", "A", "A", "A", "O"],
    2: ["R", "I", "I", "I", "M"],
    3: ["R", "I", "I", "I", "M"],
    4: ["R", "I", "I", "I", "M"],
    5: ["R", "R", "R", "R", "Q"],
}
KANO_NAMES = {"M": "Must-be", "O": "One-dimensional", "A": "Attractive", "I": "Indifferent",
              "R": "Reverse", "Q": "Questionable"}


def kano_classify(func, dysf):
    return KANO_TABLE[int(func)][int(dysf) - 1]


def margin_of_error(p, n, conf=0.95, N=None):
    z = stats.norm.ppf(1 - (1 - conf) / 2)
    moe = z * math.sqrt(p * (1 - p) / n)
    if N:
        moe *= math.sqrt((N - n) / (N - 1))
    return moe


def sample_size(moe, p=0.5, conf=0.95, N=None):
    z = stats.norm.ppf(1 - (1 - conf) / 2)
    n0 = z * z * p * (1 - p) / moe ** 2
    return math.ceil(n0 / (1 + (n0 - 1) / N)) if N else math.ceil(n0)


def ex_segments():
    r = load()
    out = {}
    for seg in SEGMENTS:
        s = [x for x in r if x["segment"] == seg]
        out[seg] = {k: round(np.mean([int(x[f"imp_{k}"]) for x in s]), 2) for k in NEEDS}
    # target-market scoring (weights x 1-5 scores), from market data + survey
    criteria = {"Size": 3, "Growth": 2, "Fit with our strengths": 3, "Margin": 2, "Unmet need (gap)": 3}
    scores = {"End-user plant (MRO)": [5, 3, 3, 4, 5], "Distributor": [4, 2, 4, 2, 3],
              "OEM machine builder": [2, 4, 4, 3, 2]}
    w = np.array(list(criteria.values()))
    attract = {k: int(w @ np.array(v)) for k, v in scores.items()}
    return {"mean importance by segment": out, "segment attractiveness (weighted)": attract}


def ex_importance():
    r = load()
    rows = []
    for k in NEEDS:
        imp = np.mean([int(x[f"imp_{k}"]) for x in r])
        sat = np.mean([int(x[f"sat_{k}"]) for x in r])
        rows.append((k, round(imp, 2), round(sat, 2), round(imp - sat, 2)))
    rows.sort(key=lambda t: -t[3])
    return {"need, importance, satisfaction, gap (sorted by gap)": rows}


def ex_kano():
    r = load()
    out = {}
    for f in KANO_FEATURES:
        c = Counter(kano_classify(x[f"kano_{f}_func"], x[f"kano_{f}_dysf"]) for x in r)
        n = sum(c.values())
        a, o, m, i = c["A"], c["O"], c["M"], c["I"]
        better = (a + o) / (a + o + m + i)
        worse = -(o + m) / (a + o + m + i)
        top = c.most_common(1)[0]
        out[f] = {"counts": {KANO_NAMES[k]: v for k, v in sorted(c.items())},
                  "category": KANO_NAMES[top[0]], "share": round(top[1] / n, 2),
                  "better": round(better, 2), "worse": round(worse, 2)}
    return out


def ex_moe():
    r = load()
    out = {}
    for seg in list(SEGMENTS) + ["All"]:
        s = r if seg == "All" else [x for x in r if x["segment"] == seg]
        p = np.mean([int(x["sat_order_status_visibility"]) >= 4 for x in s])
        out[seg] = {"n": len(s), "satisfied with status visibility (4-5)": round(p, 3),
                    "95% margin of error": round(margin_of_error(p, len(s)), 3)}
    out["sample size for +/-5% (p=0.5)"] = sample_size(0.05)
    out["sample size for +/-5% from a customer base of 1,200"] = sample_size(0.05, N=1200)
    out["sample size for +/-10%"] = sample_size(0.10)
    return out


def ex_sim(true_p=0.30, n=150, reps=10_000, seed=1):
    rng = np.random.default_rng(seed)
    ph = rng.binomial(n, true_p, reps) / n
    moe = margin_of_error(true_p, n)
    lo, hi = ph - 1.96 * np.sqrt(ph * (1 - ph) / n), ph + 1.96 * np.sqrt(ph * (1 - ph) / n)
    return {"true p": true_p, "n": n, "sd of sample p": round(ph.std(), 4),
            "theoretical SE": round(math.sqrt(true_p * (1 - true_p) / n), 4),
            "95% MOE": round(moe, 3), "range of sample p (2.5%-97.5%)": tuple(np.round(np.percentile(ph, [2.5, 97.5]), 3)),
            "CI coverage": round(float(((lo <= true_p) & (true_p <= hi)).mean()), 3)}


def ex_spec():
    r = load()
    out = {}
    for seg in SEGMENTS:
        d = np.array([int(x["max_acceptable_days"]) for x in r if x["segment"] == seg])
        out[seg] = {"median": float(np.median(d)), "10th pct": float(np.percentile(d, 10)),
                    "satisfied by 2-day delivery": f"{100 * (d >= 2).mean():.0f}%",
                    "satisfied by 3-day delivery": f"{100 * (d >= 3).mean():.0f}%",
                    "satisfied by current 5-day": f"{100 * (d >= 5).mean():.0f}%"}
    return out


def ex_targets():
    r = load()
    rec = np.array([int(x["likely_to_recommend"]) for x in r])
    prom, det = (rec >= 9).mean(), (rec <= 6).mean()
    return {"promoters (9-10)": round(prom, 3), "detractors (0-6)": round(det, 3),
            "net promoter score": round(100 * (prom - det), 1)}


# Cause & effect matrix: outputs (CTQs) weighted by customer importance; inputs scored 0/1/3/9.
CE_OUTPUTS = {"Delivered within promised days": 9, "Right part first time": 9, "Status visible without asking": 7,
              "Order placed in < 5 min": 5}
CE_INPUTS = {
    "Stock availability (fill rate)":        [9, 0, 1, 0],
    "Part-number cross-reference accuracy":  [1, 9, 0, 3],
    "Order entry method (web vs email)":     [3, 3, 3, 9],
    "Carrier selection and cut-off time":    [9, 0, 3, 0],
    "ERP-to-customer status integration":    [1, 0, 9, 1],
    "Picker training / pick verification":   [1, 9, 0, 0],
    "Credit hold process":                   [3, 0, 3, 1],
}


def ex_cematrix():
    w = np.array(list(CE_OUTPUTS.values()))
    tot = {k: int(w @ np.array(v)) for k, v in CE_INPUTS.items()}
    ranked = sorted(tot.items(), key=lambda kv: -kv[1])
    g = sum(tot.values())
    cum, rows = 0, []
    for k, v in ranked:
        cum += v
        rows.append((k, v, round(100 * cum / g, 1)))
    return {"input, score, cumulative %": rows}


EX = {"segments": ex_segments, "importance": ex_importance, "kano": ex_kano, "moe": ex_moe, "sim": ex_sim,
      "spec": ex_spec, "targets": ex_targets, "cematrix": ex_cematrix}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "data":
        print("rows written:", make_data())
        sys.exit()
    if not os.path.exists(DATA):
        make_data()
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list):
                    print(f"  {a}:")
                    for t in b:
                        print("    ", t)
                else:
                    print(f"  {a}: {b}")
