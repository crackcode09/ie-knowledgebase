"""dfss.py - calculation toolkit for the Design for Six Sigma course.

    python tools/dfss.py all        # run every worked example in the course
    python tools/dfss.py <name>     # one example: qfd, pugh, survey, capability, fmea,
                                    # scorecard, doe, stackup, queue, sim, balance, reliability

All examples use synthetic data built in this file (fixed seeds). License: MIT
"""
from __future__ import annotations

import heapq
import itertools
import math
import sys

import numpy as np
from scipy import stats

# --------------------------------------------------------------------- Define
def survey_sample_size(margin, p=0.5, conf=0.95, population=None):
    """n for estimating a proportion within +/- margin; optional finite-population correction."""
    z = stats.norm.ppf(1 - (1 - conf) / 2)
    n0 = z ** 2 * p * (1 - p) / margin ** 2
    if population:
        n0 = n0 / (1 + (n0 - 1) / population)
    return math.ceil(n0)


# ------------------------------------------------------------------------ QFD
def qfd(importance, relationships):
    """House of Quality: technical importance = sum(customer importance x relationship)."""
    imp = np.asarray(importance, float)
    rel = np.asarray(relationships, float)
    raw = imp @ rel
    return raw, 100 * raw / raw.sum()


# ----------------------------------------------------------------------- Pugh
def pugh(scores, weights=None):
    """scores: concepts x criteria in {+1, 0, -1} vs the datum."""
    s = np.asarray(scores)
    w = np.ones(s.shape[1]) if weights is None else np.asarray(weights, float)
    return {"plus": (s > 0).sum(1), "minus": (s < 0).sum(1), "same": (s == 0).sum(1),
            "net": s.sum(1), "weighted": s @ w}


# ------------------------------------------------------------------ Capability
def capability(mu, sigma, lsl, usl):
    cp = (usl - lsl) / (6 * sigma)
    cpk = min(usl - mu, mu - lsl) / (3 * sigma)
    p_out = stats.norm.cdf((lsl - mu) / sigma) + stats.norm.sf((usl - mu) / sigma)
    dpmo = p_out * 1e6
    z_bench = stats.norm.isf(p_out)
    return dict(Cp=cp, Cpk=cpk, dpmo=dpmo, z_bench=z_bench, sigma_level_with_1_5_shift=z_bench + 1.5)


# ----------------------------------------------------------------------- FMEA
def rpn(rows):
    out = [(name, s, o, d, s * o * d) for name, s, o, d in rows]
    return sorted(out, key=lambda r: r[4], reverse=True)


# ------------------------------------------------------------------ Scorecard
def scorecard(steps):
    """steps: list of (name, opportunities, dpmo). Returns per-step yield and rolled throughput yield."""
    res, rty = [], 1.0
    for name, opp, dpmo in steps:
        dpu = opp * dpmo / 1e6
        y = math.exp(-dpu)  # Poisson: P(zero defects)
        rty *= y
        res.append((name, opp, dpmo, dpu, y))
    return res, rty


# ------------------------------------------------------------------------ DOE
def doe_2k(y, k=3):
    """Full 2^k factorial in standard order; returns effects and coded regression coefficients."""
    X = np.array(list(itertools.product([-1, 1], repeat=k)))[:, ::-1]  # standard (Yates) order
    y = np.asarray(y, float)
    terms = {}
    names = "ABCDEFG"[:k]
    for r in range(1, k + 1):
        for combo in itertools.combinations(range(k), r):
            col = np.prod(X[:, combo], axis=1)
            terms["".join(names[c] for c in combo)] = col
    effects = {t: (y[c > 0].mean() - y[c < 0].mean()) for t, c in terms.items()}
    return X, y.mean(), effects


# ---------------------------------------------------------------- Tolerances
def stackup(nominals, tols, signs, n=200_000, seed=1):
    """Linear stack: gap = sum(sign * dim). Tolerances are symmetric +/- and treated as 3 sigma."""
    nom = np.asarray(nominals, float)
    tol = np.asarray(tols, float)
    sg = np.asarray(signs, float)
    gap_nom = (sg * nom).sum()
    worst = tol.sum()
    rss = math.sqrt((tol ** 2).sum())
    rng = np.random.default_rng(seed)
    sims = (sg * (nom + rng.normal(0, tol / 3, (n, len(nom))))).sum(1)
    return dict(nominal=gap_nom, worst_case=(gap_nom - worst, gap_nom + worst),
                rss=(gap_nom - rss, gap_nom + rss), mc_mean=sims.mean(), mc_sd=sims.std(),
                mc_p_below_zero=(sims < 0).mean(), sims=sims)


# ------------------------------------------------------------ Process models
def kingman_wait(ta, ca, te, ce):
    """Kingman (VUT) approximation for mean queue wait at a single station."""
    u = te / ta
    return (ca ** 2 + ce ** 2) / 2 * (u / (1 - u)) * te, u


def simulate_line(arrival_mean, stations, n_jobs=20000, seed=7, cv_service=None):
    """Discrete-event simulation of a serial line with single servers and unlimited buffers.
    stations: list of (name, mean_service_time, cv). Exponential arrivals.
    Service times are gamma with the given mean and cv. Returns throughput, WIP, flow time."""
    rng = np.random.default_rng(seed)
    arrivals = np.cumsum(rng.exponential(arrival_mean, n_jobs))
    t_ready = arrivals.copy()
    for _, mean, cv in stations:
        shape = 1 / cv ** 2
        svc = rng.gamma(shape, mean / shape, n_jobs)
        free = 0.0
        done = np.empty(n_jobs)
        for i in range(n_jobs):
            start = max(t_ready[i], free)
            free = start + svc[i]
            done[i] = free
        t_ready = done
    flow = t_ready - arrivals
    warm = n_jobs // 10
    span = t_ready[-1] - arrivals[warm]
    th = (n_jobs - warm) / span
    return dict(throughput=th, flow_time=flow[warm:].mean(), wip=th * flow[warm:].mean(),
                flow_p90=np.percentile(flow[warm:], 90))


def balance(tasks, takt):
    """Largest-candidate rule line balancing. tasks: dict name -> (time, [predecessors])."""
    done, stations = set(), []
    remaining = dict(tasks)
    while remaining:
        load, st = 0.0, []
        while True:
            cands = [(t, n) for n, (t, pre) in remaining.items()
                     if all(p in done for p in pre) and load + t <= takt + 1e-9]
            if not cands:
                break
            t, n = max(cands)
            st.append(n)
            load += t
            done.add(n)
            del remaining[n]
        stations.append((st, load))
    total = sum(t for t, _ in tasks.values())
    return stations, total / (len(stations) * takt), math.ceil(total / takt)


# ---------------------------------------------------------------- Reliability
def success_run_n(reliability, confidence):
    return math.ceil(math.log(1 - confidence) / math.log(reliability))


def weibull_fit(failures):
    shape, loc, scale = stats.weibull_min.fit(failures, floc=0)
    return shape, scale


# ------------------------------------------------------------------- Examples
def ex_survey():
    return {"n for +/-5%, 95%": survey_sample_size(0.05),
            "n for +/-5%, 95%, population 800": survey_sample_size(0.05, population=800),
            "n for +/-3%, 95%": survey_sample_size(0.03)}


QFD_NEEDS = ["Slides smoothly", "Holds position under load", "Low maintenance", "Quiet", "Affordable"]
QFD_IMP = [5, 4, 3, 2, 4]
QFD_TECH = ["Friction force (N)", "Static stiffness (N/um)", "Lube interval (km)", "Noise (dBA)", "Unit cost ($)"]
QFD_REL = [[9, 1, 3, 3, 0],
           [1, 9, 0, 0, 1],
           [3, 0, 9, 1, 0],
           [3, 1, 1, 9, 0],
           [1, 3, 3, 1, 9]]


def ex_qfd():
    raw, pct = qfd(QFD_IMP, QFD_REL)
    return {t: (int(r), round(p, 1)) for t, r, p in zip(QFD_TECH, raw, pct)}


PUGH_CRIT = ["Friction", "Stiffness", "Maintenance", "Noise", "Cost", "Ease of assembly"]
PUGH_CONCEPTS = {"B: polymer bushing": [1, -1, 1, 1, 1, 1],
                 "C: recirculating ball": [1, 1, 0, -1, -1, -1],
                 "D: roller + wiper seal": [1, 1, 1, 0, -1, 0]}
PUGH_W = [5, 4, 3, 2, 4, 2]


def ex_pugh():
    r = pugh(list(PUGH_CONCEPTS.values()), PUGH_W)
    return {c: {k: int(v[i]) for k, v in r.items()} for i, c in enumerate(PUGH_CONCEPTS)}


def ex_capability():
    return {"bore, mu 20.004 sd 0.004, 20.000 +/- 0.015": capability(20.004, 0.004, 19.985, 20.015),
            "bore after recenter, mu 20.000": capability(20.000, 0.004, 19.985, 20.015)}


FMEA_ROWS = [("Rail mounting holes mislocated", 8, 3, 4),
             ("Wiper seal omitted", 6, 4, 7),
             ("Wrong lubricant applied", 7, 2, 8),
             ("Carriage scratched in handling", 4, 6, 3),
             ("Preload too high", 7, 5, 5)]


def ex_fmea():
    return rpn(FMEA_ROWS)


SCORE_STEPS = [("Machine rail", 12, 300), ("Grind raceway", 4, 1500),
               ("Assemble carriage", 20, 150), ("Lubricate & seal", 6, 800), ("Final inspect & pack", 8, 100)]


def ex_scorecard():
    rows, rty = scorecard(SCORE_STEPS)
    return {"steps": [(n, o, d, round(dpu, 4), round(y, 4)) for n, o, d, dpu, y in rows], "RTY": rty}


# 2^3 DOE on carriage friction force (N): A = preload (low/high), B = lube viscosity, C = seal type.
DOE_Y = [12.1, 17.9, 11.4, 17.2, 14.0, 20.3, 13.1, 19.6]


def ex_doe():
    X, mean, eff = doe_2k(DOE_Y)
    return {"grand mean": mean, "effects": {k: round(v, 3) for k, v in eff.items()},
            "coded model": f"y = {mean:.3f} + {eff['A']/2:.3f}A + {eff['B']/2:.3f}B + {eff['C']/2:.3f}C"}


def ex_stackup():
    # Gap = housing bore depth - (bearing width + spacer + retaining ring)
    r = stackup(nominals=[30.00, 15.00, 12.00, 2.70], tols=[0.10, 0.06, 0.05, 0.04], signs=[1, -1, -1, -1])
    r.pop("sims")
    return r


def ex_queue():
    w, u = kingman_wait(ta=10.0, ca=1.0, te=8.0, ce=0.5)
    w2, u2 = kingman_wait(ta=10.0, ca=1.0, te=9.0, ce=0.5)
    w3, _ = kingman_wait(ta=10.0, ca=1.0, te=8.0, ce=1.5)
    return {"u=0.80 ce=0.5": (u, w), "u=0.90 ce=0.5": (u2, w2), "u=0.80 ce=1.5": (u, w3)}


def ex_sim():
    base = simulate_line(10.0, [("Cut", 6.0, 0.5), ("Drill", 8.0, 0.5), ("Assemble", 7.0, 0.5)])
    var = simulate_line(10.0, [("Cut", 6.0, 0.5), ("Drill", 8.0, 1.2), ("Assemble", 7.0, 0.5)])
    fast = simulate_line(10.0, [("Cut", 6.0, 0.5), ("Drill", 7.0, 0.5), ("Assemble", 7.0, 0.5)])
    return {"baseline": base, "drill cv 1.2": var, "drill 7.0 min": fast}


BAL_TASKS = {"A": (0.6, []), "B": (0.9, ["A"]), "C": (0.4, ["A"]), "D": (1.1, ["B"]),
             "E": (0.5, ["C"]), "F": (0.8, ["D", "E"]), "G": (0.7, ["F"]), "H": (0.3, ["G"])}


def ex_balance():
    demand_per_shift, avail_min = 400, 450
    takt = avail_min / demand_per_shift
    st, eff, nmin = balance(BAL_TASKS, takt)
    return {"takt (min)": takt, "theoretical min stations": nmin,
            "stations": [(s, round(l, 2)) for s, l in st], "balance efficiency": eff}


def ex_reliability():
    rng = np.random.default_rng(3)
    fails = np.round(stats.weibull_min.rvs(2.2, scale=8000, size=12, random_state=rng), 0)
    k, lam = weibull_fit(fails)
    b10 = lam * (-math.log(0.9)) ** (1 / k)
    return {"failures (km)": sorted(fails.tolist()), "shape beta": k, "scale eta": lam, "B10 life": b10,
            "success-run n for R=0.90, C=0.90": success_run_n(0.90, 0.90),
            "success-run n for R=0.95, C=0.90": success_run_n(0.95, 0.90),
            "success-run n for R=0.99, C=0.95": success_run_n(0.99, 0.95)}


EXAMPLES = {"survey": ex_survey, "qfd": ex_qfd, "pugh": ex_pugh, "capability": ex_capability, "fmea": ex_fmea,
            "scorecard": ex_scorecard, "doe": ex_doe, "stackup": ex_stackup, "queue": ex_queue, "sim": ex_sim,
            "balance": ex_balance, "reliability": ex_reliability}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for name, fn in EXAMPLES.items():
        if which in ("all", name):
            print(f"\n=== {name}")
            r = fn()
            if isinstance(r, dict):
                for k, v in r.items():
                    print(f"  {k}: {v}")
            else:
                for row in r:
                    print("  ", row)
