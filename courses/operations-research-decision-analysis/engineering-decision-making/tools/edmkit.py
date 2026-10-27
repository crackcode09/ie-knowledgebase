"""edmkit.py - data and calculations for the Engineering Decision Making & Risk Management course.

Running case: Corran Motion Systems (fictional) must choose the drive technology for a new linear-axis
product, decide whether to test the market first, price against a rival, pick a supplier, and set up
warning systems for field failures.

    python tools/edmkit.py data          # (re)write data/*.csv (fixed seed)
    python tools/edmkit.py all           # every worked example
    python tools/edmkit.py <name>        # ahp, maut, voting, elicit, calibration, dominance, tree, utility,
                                         # zerosum, mixedmotive, secretary, search, voi, roc, sensitivity

Requires numpy, pandas, scipy. License: MIT
"""
from __future__ import annotations

import itertools
import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import optimize, stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")

ALTS = {"A": "Belt drive", "B": "Ball screw", "C": "Linear motor", "D": "Rack and pinion"}
# attribute data: unit cost $, accuracy um (lower better), MTBF h, time to market months
ATTR = pd.DataFrame({"unit_cost": [410, 520, 880, 450], "accuracy_um": [50, 10, 2, 30],
                     "mtbf_h": [18000, 22000, 30000, 15000], "ttm_months": [6, 8, 14, 7]},
                    index=list(ALTS))
CRITERIA = ["unit_cost", "accuracy_um", "mtbf_h", "ttm_months"]
LOWER_BETTER = {"unit_cost": True, "accuracy_um": True, "mtbf_h": False, "ttm_months": True}
# AHP pairwise judgements for criteria (Saaty 1-9 scale), row vs column
AHP_PAIRS = {("unit_cost", "accuracy_um"): 2, ("unit_cost", "mtbf_h"): 1, ("unit_cost", "ttm_months"): 3,
             ("accuracy_um", "mtbf_h"): 1 / 2, ("accuracy_um", "ttm_months"): 2, ("mtbf_h", "ttm_months"): 3}
# Saaty's random consistency index (course reference values; check the literature for your n)
RI = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32}
SWING_POINTS = {"accuracy_um": 100, "unit_cost": 80, "ttm_months": 60, "mtbf_h": 40}

# decision tree (NPV $M)
P_STRONG = 0.40
PAYOFF = {"C": {"strong": 10.5, "weak": -3.0}, "B": {"strong": 4.0, "weak": 1.0}}
STUDY = dict(cost=0.2, p_fav_given_strong=0.80, p_fav_given_weak=0.20)


def make_data(seed=2030):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)
    out = {}
    ATTR.assign(name=[ALTS[a] for a in ATTR.index]).to_csv(os.path.join(D, "alternatives.csv"), index_label="alt")

    # 7 panel members: rankings (best first) and grades for majority judgement
    rankings = [("E1", "CBDA"), ("E2", "CBDA"), ("E3", "CBDA"), ("E4", "BDAC"), ("E5", "BDAC"), ("E6", "ABDC"),
                ("E7", "ABDC")]
    grades_scale = ["Reject", "Poor", "Acceptable", "Good", "Very good", "Excellent"]
    g = {"E1": "PGEA", "E2": "PVEA", "E3": "AGVA", "E4": "GERV", "E5": "GVPG", "E6": "EVRG", "E7": "VGPA"}
    code = {"R": "Reject", "P": "Poor", "A": "Acceptable", "G": "Good", "V": "Very good", "E": "Excellent"}
    rows = []
    for (v, r) in rankings:
        rows.append(dict(voter=v, ranking=">".join(r), **{f"grade_{k}": code[c] for k, c in zip("ABCD", g[v])}))
    pd.DataFrame(rows).to_csv(os.path.join(D, "panel.csv"), index=False)
    out["panel"] = 7

    # calibration: 24 past expert 80% intervals and what actually happened
    rows = []
    for i in range(1, 25):
        true = float(rng.lognormal(np.log(100), 0.5))
        centre = true * rng.lognormal(0, 0.35)
        half = centre * rng.uniform(0.10, 0.30)        # too narrow: overconfident
        rows.append(dict(estimate=f"Q{i:02d}", low_80=round(centre - half, 1), high_80=round(centre + half, 1),
                         actual=round(true, 1)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "calibration.csv"), index=False)
    out["calibration"] = 24

    # condition-monitoring signal for ROC: vibration RMS (mm/s) for healthy vs failing actuators
    healthy = rng.normal(2.0, 0.4, 950)
    failing = rng.normal(3.0, 0.6, 50)
    pd.DataFrame(dict(rms=np.round(np.r_[healthy, failing], 3), failing=[0] * 950 + [1] * 50)).sample(
        frac=1, random_state=1).to_csv(os.path.join(D, "vibration.csv"), index=False)
    out["vibration"] = 1000
    return out


def load(name):
    return pd.read_csv(os.path.join(D, f"{name}.csv"))


# ---------------------------------------------------------------- AHP
def ahp_matrix():
    n = len(CRITERIA)
    M = np.ones((n, n))
    for (a, b), v in AHP_PAIRS.items():
        i, j = CRITERIA.index(a), CRITERIA.index(b)
        M[i, j], M[j, i] = v, 1 / v
    return M


def ahp_weights(M):
    vals, vecs = np.linalg.eig(M)
    k = int(np.argmax(vals.real))
    w = np.abs(vecs[:, k].real)
    w = w / w.sum()
    lam = float(vals[k].real)
    n = M.shape[0]
    ci = (lam - n) / (n - 1)
    cr = ci / RI[n] if RI[n] else 0.0
    return w, lam, ci, cr


def ratings_normalized():
    """AHP 'ratings mode' for alternatives: scores proportional to performance (inverse for lower-better)."""
    s = {}
    for c in CRITERIA:
        x = ATTR[c].astype(float)
        v = (1 / x) if LOWER_BETTER[c] else x
        s[c] = v / v.sum()
    return pd.DataFrame(s)


def ex_ahp():
    M = ahp_matrix()
    w, lam, ci, cr = ahp_weights(M)
    S = ratings_normalized()
    total = S.values @ w
    # geometric-mean approximation for comparison
    gm = np.prod(M, axis=1) ** (1 / M.shape[0])
    gm = gm / gm.sum()
    return {"weights": {c: round(float(x), 3) for c, x in zip(CRITERIA, w)},
            "weights_geometric_mean": {c: round(float(x), 3) for c, x in zip(CRITERIA, gm)},
            "lambda_max": round(lam, 3), "CI": round(ci, 4), "CR": round(cr, 4), "consistent": cr < 0.10,
            "scores": {a: round(float(t), 3) for a, t in zip(ATTR.index, total)},
            "ranking": "".join(ATTR.index[np.argsort(-total)])}


# ---------------------------------------------------------------- MAUT / swing weights
def value(c, x):
    lo, hi = ATTR[c].min(), ATTR[c].max()
    if c == "accuracy_um":                       # diminishing value: exponential, concave toward the best
        worst, best = hi, lo
        z = (worst - x) / (worst - best)
        rho = 0.35
        return (1 - math.exp(-z / rho)) / (1 - math.exp(-1 / rho))
    if LOWER_BETTER[c]:
        return (hi - x) / (hi - lo)
    return (x - lo) / (hi - lo)


def swing_weights(points=None):
    p = points or SWING_POINTS
    t = sum(p.values())
    return {c: p[c] / t for c in CRITERIA}


def ex_maut(points=None):
    w = swing_weights(points)
    rows = []
    for a in ATTR.index:
        v = {c: value(c, ATTR.loc[a, c]) for c in CRITERIA}
        rows.append(dict(alt=a, name=ALTS[a], **{f"v_{c}": round(v[c], 3) for c in CRITERIA},
                         total=round(sum(w[c] * v[c] for c in CRITERIA), 3)))
    rows.sort(key=lambda r: -r["total"])
    return {"weights": {c: round(x, 3) for c, x in w.items()}, "alternatives": rows,
            "ranking": "".join(r["alt"] for r in rows)}


# ---------------------------------------------------------------- group decision making
def rankings():
    p = load("panel")
    return [r.split(">") for r in p.ranking]


def ex_voting():
    R = rankings()
    alts = list("ABCD")
    plural = {a: sum(r[0] == a for r in R) for a in alts}
    borda = {a: sum(len(alts) - 1 - r.index(a) for r in R) for a in alts}
    # pairwise preference counts
    pref = {(x, y): sum(r.index(x) < r.index(y) for r in R) for x in alts for y in alts if x != y}
    condorcet = [x for x in alts if all(pref[(x, y)] > len(R) / 2 for y in alts if y != x)]
    best, best_score = None, -1
    scores = {}
    for perm in itertools.permutations(alts):
        s = sum(pref[(perm[i], perm[j])] for i in range(4) for j in range(i + 1, 4))
        scores["".join(perm)] = s
        if s > best_score:
            best, best_score = "".join(perm), s
    # majority judgement: median grade; tie-break by removing median grades one at a time
    order = ["Reject", "Poor", "Acceptable", "Good", "Very good", "Excellent"]
    p = load("panel")
    mj = {}
    for a in alts:
        gs = sorted(order.index(x) for x in p[f"grade_{a}"])
        mj[a] = gs
    def mj_key(gs):
        gs = list(gs)
        key = []
        while gs:
            m = (len(gs) - 1) // 2          # lower median
            key.append(gs[m])
            gs.pop(m)
        return key
    mj_rank = sorted(alts, key=lambda a: mj_key(mj[a]), reverse=True)
    return {"plurality": plural, "plurality_winner": max(plural, key=plural.get), "borda": borda,
            "borda_winner": max(borda, key=borda.get), "condorcet_winner": condorcet[0] if condorcet else None,
            "pairwise_wins": {f"{x}>{y}": pref[(x, y)] for x in alts for y in alts if x < y},
            "kemeny_young_ranking": best, "kemeny_score": best_score,
            "majority_judgement_medians": {a: order[mj_key(mj[a])[0]] for a in alts},
            "majority_judgement_ranking": "".join(mj_rank)}


# ---------------------------------------------------------------- subjective probability
def ex_elicit(p10=3000, p50=5000, p90=9000):
    mu = math.log(p50)
    s_lo = (mu - math.log(p10)) / 1.2816
    s_hi = (math.log(p90) - mu) / 1.2816
    s = (s_lo + s_hi) / 2
    d = stats.lognorm(s=s, scale=math.exp(mu))
    return {"p10": p10, "p50": p50, "p90": p90, "sigma_log": round(s, 3), "sigma_lo": round(s_lo, 3),
            "sigma_hi": round(s_hi, 3), "mean": round(float(d.mean())), "P(demand<4000)": round(float(d.cdf(4000)), 3),
            "fitted_p10": round(float(d.ppf(0.1))), "fitted_p90": round(float(d.ppf(0.9)))}


def ex_calibration():
    c = load("calibration")
    hit = ((c.actual >= c.low_80) & (c.actual <= c.high_80))
    n, k = len(c), int(hit.sum())
    p = stats.binomtest(k, n, 0.8).pvalue
    return {"intervals": n, "hits": k, "hit_rate": round(k / n, 3), "expected": 0.8,
            "binomial_p_value": round(float(p), 5), "verdict": "overconfident" if k / n < 0.8 else "ok"}


# ---------------------------------------------------------------- stochastic dominance
def npv_samples(n=20000, seed=5):
    rng = np.random.default_rng(seed)
    e = ex_elicit()
    demand = rng.lognormal(math.log(e["p50"]), e["sigma_log"], n)
    years, r = 5, 0.10
    af = sum(1 / (1 + r) ** t for t in range(1, years + 1))
    # price, unit cost, up-front investment, Corran's share of the market demand
    spec = {"A": (980, 410, 0.30e6, 0.18), "B": (1150, 520, 0.42e6, 0.20), "C": (1900, 880, 3.96e6, 0.30),
            "D": (1000, 450, 0.35e6, 0.17)}
    out = {}
    for a, (price, cost, inv, share) in spec.items():
        out[a] = (demand * share * (price - cost) * af - inv) / 1e6
    return out


def dominance(x, y, grid=400):
    lo, hi = min(x.min(), y.min()), max(x.max(), y.max())
    t = np.linspace(lo, hi, grid)
    Fx = np.searchsorted(np.sort(x), t, side="right") / len(x)
    Fy = np.searchsorted(np.sort(y), t, side="right") / len(y)
    fsd = bool(np.all(Fx <= Fy + 1e-3))
    dt = t[1] - t[0]
    ssd = bool(np.all(np.cumsum(Fx - Fy) * dt <= 1e-3))
    return fsd, ssd


def ex_dominance():
    s = npv_samples()
    stats_ = {a: dict(mean=round(float(v.mean()), 2), p10=round(float(np.percentile(v, 10)), 2),
                      p90=round(float(np.percentile(v, 90)), 2), p_loss=round(float((v < 0).mean()), 3))
              for a, v in s.items()}
    pairs = []
    for x, y in itertools.permutations(s, 2):
        f, ss = dominance(s[x], s[y])
        if f or ss:
            pairs.append(dict(dominant=x, dominated=y, first_order=f, second_order=ss))
    return {"npv_$M": stats_, "dominance": pairs}


# ---------------------------------------------------------------- decision tree, utility, VOI
def emv(alt, p=P_STRONG):
    return p * PAYOFF[alt]["strong"] + (1 - p) * PAYOFF[alt]["weak"]


def ex_tree():
    e = {a: round(emv(a), 3) for a in PAYOFF}
    return {"p_strong": P_STRONG, "payoffs_$M": PAYOFF, "EMV": e, "best": max(e, key=e.get)}


def u(x, R):
    return 1 - math.exp(-x / R)


def ce(alt, R, p=P_STRONG):
    eu = p * u(PAYOFF[alt]["strong"], R) + (1 - p) * u(PAYOFF[alt]["weak"], R)
    return -R * math.log(1 - eu)


def ex_utility():
    rows = []
    for R in [2.0, 3.0, 5.0, 10.0, 50.0, 200.0]:
        rows.append(dict(risk_tolerance_M=R, CE_C=round(ce("C", R), 3), CE_B=round(ce("B", R), 3),
                         choice="C" if ce("C", R) > ce("B", R) else "B",
                         risk_premium_C=round(emv("C") - ce("C", R), 3)))
    Rs = optimize.brentq(lambda R: ce("C", R) - ce("B", R), 2, 1000)
    return {"utility": "u(x) = 1 - exp(-x / R)", "table": rows, "switch_R_$M": round(Rs, 2)}


def ex_voi():
    p = P_STRONG
    perfect = p * max(PAYOFF[a]["strong"] for a in PAYOFF) + (1 - p) * max(PAYOFF[a]["weak"] for a in PAYOFF)
    best_prior = max(emv(a) for a in PAYOFF)
    evpi = perfect - best_prior
    ps, pw = STUDY["p_fav_given_strong"], STUDY["p_fav_given_weak"]
    p_fav = p * ps + (1 - p) * pw
    post_fav = p * ps / p_fav
    post_unf = p * (1 - ps) / (1 - p_fav)
    v_fav = max(emv(a, post_fav) for a in PAYOFF)
    v_unf = max(emv(a, post_unf) for a in PAYOFF)
    with_info = p_fav * v_fav + (1 - p_fav) * v_unf
    evii = with_info - best_prior
    return {"EMV_without_info": round(best_prior, 3), "EV_with_perfect_info": round(perfect, 3),
            "EVPI": round(evpi, 3), "P(favourable)": round(p_fav, 3), "P(strong|fav)": round(post_fav, 3),
            "P(strong|unfav)": round(post_unf, 3),
            "best_if_fav": max(PAYOFF, key=lambda a: emv(a, post_fav)),
            "best_if_unfav": max(PAYOFF, key=lambda a: emv(a, post_unf)),
            "EV_with_study": round(with_info, 3), "EVII": round(evii, 3), "study_cost": STUDY["cost"],
            "net_value_of_study": round(evii - STUDY["cost"], 3)}


def ex_sensitivity():
    base = emv("C") - emv("B")
    p_star = (PAYOFF["B"]["weak"] - PAYOFF["C"]["weak"]) / (
        (PAYOFF["C"]["strong"] - PAYOFF["C"]["weak"]) - (PAYOFF["B"]["strong"] - PAYOFF["B"]["weak"]))
    rows = []
    def diff(p=P_STRONG, cs=None, cw=None, bs=None, bw=None):
        cs = PAYOFF["C"]["strong"] if cs is None else cs
        cw = PAYOFF["C"]["weak"] if cw is None else cw
        bs = PAYOFF["B"]["strong"] if bs is None else bs
        bw = PAYOFF["B"]["weak"] if bw is None else bw
        return p * cs + (1 - p) * cw - (p * bs + (1 - p) * bw)
    for name, lo, hi in [("P(strong) 0.30-0.50", diff(p=0.30), diff(p=0.50)),
                         ("C strong payoff 8-13", diff(cs=8), diff(cs=13)),
                         ("C weak payoff -5 to -1", diff(cw=-5), diff(cw=-1)),
                         ("B strong payoff 3-5", diff(bs=5), diff(bs=3)),
                         ("B weak payoff 0-2", diff(bw=2), diff(bw=0))]:
        rows.append(dict(input=name, low=round(lo, 3), high=round(hi, 3), swing=round(abs(hi - lo), 3),
                         crosses_zero=bool(lo < 0 < hi or hi < 0 < lo)))
    rows.sort(key=lambda r: -r["swing"])
    return {"EMV_C_minus_B": round(base, 3), "breakeven_p_strong": round(p_star, 4), "tornado": rows}


# ---------------------------------------------------------------- game theory
ZERO_SUM = pd.DataFrame([[3, -1, 2], [-2, 4, 1], [1, 0, -1]],
                        index=["Price cut", "Feature push", "Service bundle"],
                        columns=["Rival: price cut", "Rival: new model", "Rival: hold"])


def ex_zerosum():
    A = ZERO_SUM.values.astype(float)
    rowmin = A.min(axis=1)
    colmax = A.max(axis=0)
    maximin, minimax = rowmin.max(), colmax.min()
    # LP: maximize v s.t. sum_i x_i A_ij >= v for all j, sum x = 1
    m, n = A.shape
    c = np.r_[np.zeros(m), -1]
    A_ub = np.c_[-A.T, np.ones(n)]
    res = optimize.linprog(c, A_ub=A_ub, b_ub=np.zeros(n), A_eq=[np.r_[np.ones(m), 0]], b_eq=[1],
                           bounds=[(0, None)] * m + [(None, None)])
    x, v = res.x[:m], res.x[m]
    c2 = np.r_[np.zeros(n), 1]
    res2 = optimize.linprog(c2, A_ub=np.c_[A, -np.ones(m)], b_ub=np.zeros(m), A_eq=[np.r_[np.ones(n), 0]],
                            b_eq=[1], bounds=[(0, None)] * n + [(None, None)])
    y = res2.x[:n]
    return {"payoff_to_Corran": ZERO_SUM.to_dict(), "maximin": float(maximin), "minimax": float(minimax),
            "saddle_point": bool(maximin == minimax), "corran_mix": {k: round(float(p), 3) for k, p in zip(ZERO_SUM.index, x)},
            "rival_mix": {k: round(float(p), 3) for k, p in zip(ZERO_SUM.columns, y)}, "game_value": round(float(v), 3)}


MIXED = {("High", "High"): (6, 6), ("High", "Low"): (1, 8), ("Low", "High"): (8, 1), ("Low", "Low"): (3, 3)}


def ex_mixedmotive():
    acts = ["High", "Low"]
    nash = []
    for a, b in itertools.product(acts, acts):
        ua, ub = MIXED[(a, b)]
        best_a = all(ua >= MIXED[(x, b)][0] for x in acts)
        best_b = all(ub >= MIXED[(a, y)][1] for y in acts)
        if best_a and best_b:
            nash.append(f"{a}/{b}")
    return {"payoffs_(Corran,Rival)_$M": {f"{a}/{b}": v for (a, b), v in MIXED.items()}, "nash_equilibria": nash,
            "pareto_better": "High/High (6,6) beats the equilibrium (3,3) for both",
            "dominant_strategy": "Low for both (8>6 and 3>1)"}


# ---------------------------------------------------------------- search, secretary problem
def ex_secretary(n=20, trials=20000, seed=3):
    rng = np.random.default_rng(seed)
    k_opt = round(n / math.e)
    res = {}
    for k in [1, 3, 5, k_opt, 10, 15]:
        wins = 0
        for _ in range(trials):
            perm = rng.permutation(n)            # 0 = best
            best_seen = perm[:k].min() if k > 0 else n
            pick = next((x for x in perm[k:] if x < best_seen), perm[-1])
            wins += pick == 0
        res[k] = round(wins / trials, 3)
    return {"n": n, "k_opt_n_over_e": k_opt, "P(best)_by_k": res, "theory_limit": round(1 / math.e, 3)}


def ex_search(a=80.0, b=120.0, cost=1.5):
    r = a + math.sqrt(2 * cost * (b - a))
    p_accept = (r - a) / (b - a)
    exp_quotes = 1 / p_accept
    exp_price = (a + r) / 2
    return {"quote_range_$k": [a, b], "cost_per_quote_$k": cost, "reservation_price_$k": round(r, 2),
            "P(quote acceptable)": round(p_accept, 3), "expected_quotes": round(exp_quotes, 2),
            "expected_price_paid_$k": round(exp_price, 2),
            "expected_total_$k": round(exp_price + cost * exp_quotes, 2)}


# ---------------------------------------------------------------- ROC
def ex_roc(c_false_alarm=800.0, c_miss=20000.0):
    v = load("vibration")
    th = np.round(np.arange(1.5, 4.01, 0.05), 2)
    rows = []
    for t in th:
        alarm = v.rms >= t
        tp = int((alarm & (v.failing == 1)).sum())
        fp = int((alarm & (v.failing == 0)).sum())
        fn = int((~alarm & (v.failing == 1)).sum())
        tn = int((~alarm & (v.failing == 0)).sum())
        rows.append(dict(threshold=float(t), TPR=round(tp / (tp + fn), 3), FPR=round(fp / (fp + tn), 4), tp=tp, fp=fp,
                         fn=fn, cost=fp * c_false_alarm + fn * c_miss))
    r = pd.DataFrame(rows)
    best = r.loc[r.cost.idxmin()]
    pos, neg = v.rms[v.failing == 1].values, v.rms[v.failing == 0].values
    auc = float((pos[:, None] > neg[None, :]).mean() + 0.5 * (pos[:, None] == neg[None, :]).mean())
    ppv = best.tp / (best.tp + best.fp) if (best.tp + best.fp) else 0
    return {"auc": round(auc, 3), "best_threshold": float(best.threshold), "TPR": float(best.TPR), "FPR": float(best.FPR),
            "tp": int(best.tp), "fp": int(best.fp), "fn": int(best.fn), "expected_cost": float(best.cost),
            "cost_alarm_at_2.5": float(r[r.threshold == 2.5].cost.iloc[0]),
            "PPV_at_best": round(float(ppv), 3), "prevalence": round(float(v.failing.mean()), 3)}


def _clean(o):
    if isinstance(o, dict):
        return {str(k): _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [_clean(v) for v in o]
    if isinstance(o, np.floating):
        return round(float(o), 4)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.bool_):
        return bool(o)
    return o


EX = {"ahp": ex_ahp, "maut": ex_maut, "voting": ex_voting, "elicit": ex_elicit, "calibration": ex_calibration,
      "dominance": ex_dominance, "tree": ex_tree, "utility": ex_utility, "zerosum": ex_zerosum,
      "mixedmotive": ex_mixedmotive, "secretary": ex_secretary, "search": ex_search, "voi": ex_voi, "roc": ex_roc,
      "sensitivity": ex_sensitivity}

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
