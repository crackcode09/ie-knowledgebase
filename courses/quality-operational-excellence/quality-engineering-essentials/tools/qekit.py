"""qekit.py - data and worked examples for the Quality Engineering Essentials course.

Running case: Bayline Fasteners (fictional) machines brass threaded inserts. Customers report
inserts that are too large to press in and inserts with damaged threads. A quality engineer runs
a DMAIC project from charter to control plan.

    python tools/qekit.py data           # (re)write data/*.csv (fixed seed)
    python tools/qekit.py all            # every worked example
    python tools/qekit.py <name>         # yield, describe, pareto, distribution, cleanse, grr, attribute,
                                         # sample_size, baseline, spc, capability, stratify, regression,
                                         # fmea, reliability, pilot, staged

Requires numpy, scipy, pandas, statsmodels. License: MIT
"""
from __future__ import annotations

import math
import os
import sys

import numpy as np
import pandas as pd
from scipy import stats

ROOT = os.path.join(os.path.dirname(__file__), "..")
D = os.path.join(ROOT, "data")
LSL, USL, TARGET = 6.325, 6.375, 6.350          # insert outside diameter, mm


# ---------------------------------------------------------------- data
def make_data(seed=1924):
    rng = np.random.default_rng(seed)
    os.makedirs(D, exist_ok=True)

    # 1. Production sample: 480 inserts, 2 machines x 3 shifts, 20 days
    rows = []
    pid = 0
    for day in range(1, 21):
        for machine in ("M1", "M2"):
            tool_age = 0
            for shift in ("A", "B", "C"):
                for _ in range(4):
                    pid += 1
                    tool_age += int(rng.integers(150, 400))
                    if tool_age > 2400:
                        tool_age = int(rng.integers(0, 200))       # tool changed
                    coolant = rng.normal(24 if shift != "C" else 27, 1.2)
                    od = (6.351 + (0.008 if machine == "M2" else 0.0) + 0.000006 * tool_age
                          + 0.0013 * (coolant - 24) + rng.normal(0, 0.0045))
                    rows.append(dict(part=pid, day=day, machine=machine, shift=shift, tool_age_parts=tool_age,
                                     coolant_temp_c=round(coolant, 1), od_mm=round(od, 4)))
    prod = pd.DataFrame(rows)
    # attribute defect classification of the same parts (visual + gauge)
    defect = np.where(prod.od_mm > USL, "oversize OD", np.where(prod.od_mm < LSL, "undersize OD", ""))
    extra = rng.choice(["", "thread damage", "burr", "knurl incomplete", "wrong length"], len(prod),
                       p=[0.958, 0.02, 0.012, 0.006, 0.004])
    prod["defect"] = np.where(defect != "", defect, extra)
    prod.to_csv(os.path.join(D, "production_sample.csv"), index=False)

    # 2. Gauge R&R: 10 parts x 3 operators x 3 trials (micrometer on OD)
    true = np.linspace(6.333, 6.368, 10) + rng.normal(0, 0.0015, 10)
    op_bias = {"Ana": 0.0, "Ben": 0.0016, "Cai": -0.0008}
    rows = []
    for p in range(10):
        for op, b in op_bias.items():
            for t in range(3):
                rows.append(dict(part=p + 1, operator=op, trial=t + 1,
                                 od_mm=round(true[p] + b + rng.normal(0, 0.0012), 4)))
    pd.DataFrame(rows).to_csv(os.path.join(D, "gauge_rr.csv"), index=False)

    # 3. Attribute MSA: 30 inserts, 3 inspectors x 2 trials, thread go/no-go visual judgement vs expert standard
    std = rng.choice(["Pass", "Fail"], 30, p=[0.6, 0.4])
    border = rng.uniform(size=30) < 0.25
    acc = {"Dee": 0.97, "Eli": 0.88, "Fay": 0.80}
    rows = []
    for i in range(30):
        for ins, a in acc.items():
            for t in range(2):
                pa = a - (0.15 if border[i] else 0.0)
                call = std[i] if rng.uniform() < pa else ("Fail" if std[i] == "Pass" else "Pass")
                rows.append(dict(part=i + 1, inspector=ins, trial=t + 1, call=call, standard=std[i]))
    pd.DataFrame(rows).to_csv(os.path.join(D, "attribute_msa.csv"), index=False)

    # 4. Service process: quote turnaround time (hours), right-skewed
    q = rng.lognormal(np.log(18), 0.55, 120)
    pd.DataFrame(dict(quote=range(1, 121), turnaround_h=q.round(1))).to_csv(os.path.join(D, "quote_turnaround.csv"), index=False)

    # 5. "Dirty" export for data cleansing practice
    dirty = prod.sample(40, random_state=2)[["part", "machine", "shift", "od_mm"]].copy()
    dirty.loc[dirty.index[3], "od_mm"] = 63.52          # decimal slip
    dirty.loc[dirty.index[7], "machine"] = "m2 "         # inconsistent label
    dirty.loc[dirty.index[11], "od_mm"] = np.nan         # missing
    dirty.loc[dirty.index[15], "shift"] = "b"
    dirty = pd.concat([dirty, dirty.iloc[[20]]])          # duplicate row
    dirty.loc[dirty.index[25], "od_mm"] = 0.0            # placeholder zero
    dirty.to_csv(os.path.join(D, "dirty_export.csv"), index=False)

    # 6. Pilot of the corrective action on M2: before/after defectives
    # oversize OD on M2: 2 weeks before vs 2 weeks of pilot (chiller + tool-change interval + offset rule)
    pd.DataFrame(dict(phase=["before", "after"], inspected=[2400, 1800], defective=[190, 6])).to_csv(
        os.path.join(D, "pilot_results.csv"), index=False)
    # daily breakdown of the pilot for a staged p chart (10 days each phase)
    before = rng.multinomial(190, np.ones(10) / 10)
    after = np.array([1, 0, 1, 0, 1, 0, 1, 1, 0, 1])   # 6 oversize in 10 days
    pd.DataFrame(dict(day=range(1, 21), stage=["before"] * 10 + ["after"] * 10,
                      inspected=[240] * 10 + [180] * 10, oversize=np.concatenate([before, after]))).to_csv(
        os.path.join(D, "pilot_daily.csv"), index=False)
    # 7. Cost inputs for the pilot's side-effect check (module 06). Illustrative values, in US dollars.
    pd.DataFrame([
        ("tool_edge_cost_usd", 24.0, "price of one cutting-tool edge"),
        ("parts_per_edge_before", 2400, "tool-change interval before the pilot"),
        ("parts_per_edge_after", 1600, "tool-change interval during the pilot"),
        ("conversion_cost_excl_tooling_usd", 0.38, "machining cost per insert excluding tooling: labour, machine time, coolant"),
        ("scrap_cost_per_oversize_part_usd", 0.55, "material plus conversion lost when an oversize insert is scrapped"),
    ], columns=["item", "value", "meaning"]).to_csv(os.path.join(D, "tooling_cost.csv"), index=False)
    return "data written"


def load(name):
    return pd.read_csv(os.path.join(D, name))


# ---------------------------------------------------------------- examples
def ex_yield():
    out = {f"{n} steps at 99.9% each": round(0.999 ** n, 4) for n in (1, 10, 100, 500, 1000)}
    out["steps at 99.9% for overall yield to fall below 50%"] = math.ceil(math.log(0.5) / math.log(0.999))
    return {"rolled throughput yield": out}


def ex_describe():
    d = load("production_sample.csv").od_mm
    return {"n": len(d), "mean": round(d.mean(), 5), "median": round(d.median(), 4), "SD": round(d.std(ddof=1), 5),
            "min / max": (d.min(), d.max()), "range": round(d.max() - d.min(), 4),
            "Q1 / Q3": tuple(round(v, 4) for v in d.quantile([0.25, 0.75])), "skewness": round(float(stats.skew(d)), 3),
            "95% CI for mean": tuple(round(v, 5) for v in stats.t.interval(0.95, len(d) - 1, d.mean(), stats.sem(d)))}


def ex_pareto():
    p = load("production_sample.csv")
    c = p[p.defect.notna() & (p.defect != "")].defect.value_counts()
    tab = pd.DataFrame(dict(count=c, pct=(100 * c / c.sum()).round(1), cum_pct=(100 * c.cumsum() / c.sum()).round(1)))
    bad = p.defect.notna() & (p.defect != "")
    by_m = p.assign(bad=bad).groupby("machine").bad.agg(["sum", "size"])
    return {"parts / defective": (len(p), int(c.sum())), "% defective": round(100 * c.sum() / len(p), 2),
            "pareto": tab.reset_index().rename(columns={"index": "defect"}).to_dict("records"),
            "defective by machine": {m: f"{int(r['sum'])} of {int(r['size'])} ({100 * r['sum'] / r['size']:.1f} %)" for m, r in by_m.iterrows()}}


def ex_distribution():
    q = load("quote_turnaround.csv").turnaround_h.values
    fits = {}
    for name, dist, kw in (("normal", stats.norm, {}), ("lognormal", stats.lognorm, dict(floc=0)),
                           ("Weibull", stats.weibull_min, dict(floc=0)), ("gamma", stats.gamma, dict(floc=0))):
        params = dist.fit(q, **kw)
        ll = np.sum(dist.logpdf(q, *params))
        k = len(params) - (1 if "floc" in kw else 0)
        fits[name] = dict(AIC=round(2 * k - 2 * ll, 1), KS_p_rough=round(stats.kstest(q, dist.cdf, args=params).pvalue, 3))
    best = min(fits, key=lambda k: fits[k]["AIC"])
    lnq = np.log(q)
    return {"n": len(q), "mean / median (h)": (round(q.mean(), 1), round(np.median(q), 1)), "skewness": round(float(stats.skew(q)), 2),
            "fits (lower AIC = better; KS p is a rough guide only, the parameters were fitted to the same data)": fits, "best by AIC": best,
            "Shapiro p: raw / log": (float(f"{stats.shapiro(q).pvalue:.2g}"), round(stats.shapiro(lnq).pvalue, 3)),
            "95th percentile: normal assumption vs lognormal fit (h)": (round(q.mean() + 1.645 * q.std(ddof=1), 1),
                                                                         round(float(np.exp(lnq.mean() + 1.645 * lnq.std(ddof=1))), 1)),
            "empirical 95th percentile (h)": round(float(np.percentile(q, 95)), 1)}


def ex_cleanse():
    d = load("dirty_export.csv")
    issues = {"rows": len(d), "exact duplicate rows": int(d.duplicated().sum()), "missing od_mm": int(d.od_mm.isna().sum()),
              "zeros (placeholder) in od_mm": int((d.od_mm == 0).sum()),
              "out of physical range (not 6.0-6.7 mm)": int(((d.od_mm > 6.7) | ((d.od_mm < 6.0) & (d.od_mm > 0))).sum()),
              "non-standard machine labels": sorted(set(d.machine) - {"M1", "M2"}),
              "non-standard shift labels": sorted(set(d["shift"]) - {"A", "B", "C"})}
    c = d.drop_duplicates().copy()
    c["machine"] = c.machine.str.strip().str.upper()
    c["shift"] = c["shift"].str.strip().str.upper()
    c.loc[c.od_mm == 0, "od_mm"] = np.nan
    c.loc[c.od_mm > 6.7, "od_mm"] = c.od_mm / 10          # decimal slip, confirmed against source record
    issues["rows after cleansing / usable od values"] = (len(c), int(c.od_mm.notna().sum()))
    return issues


def ex_grr():
    import statsmodels.formula.api as smf
    import statsmodels.api as sm
    g = load("gauge_rr.csv")
    p, o, r = g.part.nunique(), g.operator.nunique(), g.trial.nunique()
    m = smf.ols("od_mm ~ C(part) * C(operator)", data=g).fit()
    a = sm.stats.anova_lm(m, typ=2)
    ms = a.sum_sq / a.df
    msp, mso, mspo, mse = ms["C(part)"], ms["C(operator)"], ms["C(part):C(operator)"], ms["Residual"]
    p_int = a.loc["C(part):C(operator)", "PR(>F)"]
    var_rep = mse
    var_int = max(0.0, (mspo - mse) / r)
    var_op = max(0.0, (mso - mspo) / (p * r))
    var_part = max(0.0, (msp - mspo) / (o * r))
    grr = var_rep + var_op + var_int
    total = grr + var_part
    sv = lambda v: 100 * math.sqrt(v / total)  # noqa: E731
    tol = USL - LSL
    ndc = int(math.floor(1.41 * math.sqrt(var_part / grr)))
    return {"design": f"{p} parts x {o} operators x {r} trials", "interaction p-value": round(p_int, 3),
            "variance components (mm^2)": {k: f"{v:.3e}" for k, v in dict(repeatability=var_rep, operator=var_op,
                                                                          interaction=var_int, part=var_part).items()},
            "% study variation": {"repeatability": round(sv(var_rep), 1), "reproducibility": round(sv(var_op + var_int), 1),
                                  "total gauge R&R": round(sv(grr), 1), "part-to-part": round(sv(var_part), 1)},
            "% tolerance (6 sigma GRR / tolerance)": round(100 * 6 * math.sqrt(grr) / tol, 1),
            "number of distinct categories": ndc,
            "operator means (mm)": g.groupby("operator").od_mm.mean().round(5).to_dict()}


def _kappa(a, b):
    a, b = np.asarray(a), np.asarray(b)
    po = np.mean(a == b)
    cats = np.union1d(a, b)
    pe = sum(np.mean(a == c) * np.mean(b == c) for c in cats)
    return (po - pe) / (1 - pe)


def ex_attribute():
    d = load("attribute_msa.csv")
    out = {}
    for ins, g in d.groupby("inspector"):
        w = g.pivot(index="part", columns="trial", values="call")
        std = g.groupby("part").standard.first()
        within = (w[1] == w[2]).mean()
        vs_std = ((w[1] == std) & (w[2] == std)).mean()
        out[ins] = {"within-inspector agreement %": round(100 * within, 1), "agrees with standard (both trials) %": round(100 * vs_std, 1),
                    "kappa vs standard (all calls)": round(_kappa(g.call, g.standard), 3)}
    allc = d.pivot_table(index="part", columns=["inspector", "trial"], values="call", aggfunc="first")
    std = d.groupby("part").standard.first()
    all_agree = allc.nunique(axis=1).eq(1)
    all_std = all_agree & allc.iloc[:, 0].eq(std)
    return {"by inspector": out, "all inspectors agree with each other %": round(100 * all_agree.mean(), 1),
            "all inspectors agree with standard %": round(100 * all_std.mean(), 1)}


def ex_sample_size():
    z = stats.norm.ppf(0.975)
    sigma = load("production_sample.csv").od_mm.std(ddof=1)
    out = {}
    for e in (0.002, 0.001):
        out[f"n to estimate mean OD within +/-{e} mm (95%)"] = math.ceil((z * sigma / e) ** 2)
    for p, e in ((0.05, 0.02), (0.05, 0.01)):
        out[f"n to estimate a ~{int(100*p)}% defect rate within +/-{int(100*e)} pts (95%)"] = math.ceil(z ** 2 * p * (1 - p) / e ** 2)
    out["sigma used (mm)"] = round(sigma, 5)
    return out


def ex_baseline():
    p = load("production_sample.csv")
    n = len(p)
    defective = int((p.defect.notna() & (p.defect != "")).sum())
    opportunities = 5          # OD, thread, burr, knurl, length
    dpmo = 1e6 * defective / (n * opportunities)
    dpu = defective / n
    od = p.od_mm
    ppk = min(USL - od.mean(), od.mean() - LSL) / (3 * od.std(ddof=1))
    return {"units / defective units": (n, defective), "% defective": round(100 * defective / n, 2), "DPU": round(dpu, 4),
            "DPMO (5 opportunities per unit)": round(dpmo), "first-pass yield %": round(100 * (1 - defective / n), 2),
            "sigma level (short-term, with 1.5 shift convention)": round(stats.norm.ppf(1 - dpmo / 1e6) + 1.5, 2),
            "OD Ppk (overall)": round(ppk, 3)}


def ex_spc():
    q = load("quote_turnaround.csv").turnaround_h.values
    out = {}
    for name, x in (("raw hours", q), ("log(hours)", np.log(q))):
        mr = np.abs(np.diff(x)).mean()
        ucl, lcl = x.mean() + 2.66 * mr, x.mean() - 2.66 * mr
        n_out = int(((x > ucl) | (x < lcl)).sum())
        out[name] = {"center": round(float(x.mean()), 3), "UCL": round(float(ucl), 3), "LCL": round(float(lcl), 3),
                     "points outside": n_out}
    out["log-scale limits back-transformed to hours"] = (round(float(np.exp(out["log(hours)"]["LCL"])), 1),
                                                        round(float(np.exp(out["log(hours)"]["UCL"])), 1))
    # stage variable: X-bar by day for M2 before/after a coolant chiller fix would go here (see pilot)
    return out


def ex_capability():
    p = load("production_sample.csv")
    out = {}
    for m, g in p.groupby("machine"):
        x = g.od_mm
        s = x.std(ddof=1)
        out[m] = {"mean": round(x.mean(), 5), "SD": round(s, 5), "Pp": round((USL - LSL) / (6 * s), 3),
                  "Ppk": round(min(USL - x.mean(), x.mean() - LSL) / (3 * s), 3),
                  "expected % out of spec": round(100 * (stats.norm.sf((USL - x.mean()) / s) + stats.norm.cdf((LSL - x.mean()) / s)), 2)}
    return out


def ex_stratify():
    p = load("production_sample.csv")
    p["oversize"] = (p.od_mm > USL).astype(int)
    t = p.groupby(["machine", "shift"]).agg(n=("part", "count"), mean_od=("od_mm", "mean"), pct_oversize=("oversize", "mean"))
    t["mean_od"] = t.mean_od.round(5)
    t["pct_oversize"] = (100 * t.pct_oversize).round(1)
    k = pd.crosstab(p.machine, p.oversize)
    chi = stats.chi2_contingency(k)
    return {"by machine and shift": t.reset_index().to_dict("records"),
            "oversize by machine (count)": k.to_dict("index"), "chi-square p (machine vs oversize)": float(f"{chi[1]:.2g}")}


def ex_regression():
    import statsmodels.formula.api as smf
    p = load("production_sample.csv")
    m1 = smf.ols("od_mm ~ tool_age_parts", data=p).fit()
    m2 = smf.ols("od_mm ~ tool_age_parts + coolant_temp_c + C(machine)", data=p).fit()
    return {"simple: OD vs tool age": {"slope (mm per 1,000 parts)": round(1000 * m1.params.tool_age_parts, 5),
                                      "R2": round(m1.rsquared, 3), "p": float(f"{m1.pvalues.tool_age_parts:.2g}")},
            "multiple: tool age + coolant temp + machine": {k: round(v, 6) for k, v in m2.params.items()},
            "multiple R2": round(m2.rsquared, 3),
            "OD gain from 0 to 2,400 parts of tool life (mm)": round(2400 * m2.params.tool_age_parts, 4),
            "OD gain per +3 C coolant (mm)": round(3 * m2.params.coolant_temp_c, 4)}


def ex_fmea():
    rows = [("Turn OD", "OD oversize", "customer can't press insert; line stop", 7, "tool wear; coolant temperature drift", 6,
             "hourly micrometer check", 5),
            ("Turn OD", "OD undersize", "insert pulls out in service", 9, "offset over-correction", 3, "hourly micrometer check", 5),
            ("Thread", "Thread damage", "screw won't start; field return", 8, "chip packing in tap", 4, "visual go/no-go 1 in 50", 6),
            ("Deburr", "Burr", "assembly scratch", 4, "worn deburr brush", 4, "visual 1 in 50", 4),
            ("Knurl", "Knurl incomplete", "low retention torque", 8, "knurl tool misaligned", 2, "first-piece check", 4)]
    f = pd.DataFrame(rows, columns=["step", "failure_mode", "effect", "S", "cause", "O", "current_control", "D"])
    f["RPN"] = f.S * f.O * f.D
    return {"FMEA ranked by RPN": f.sort_values("RPN", ascending=False)[["step", "failure_mode", "S", "O", "D", "RPN"]].to_dict("records"),
            "note": "review any S >= 9 regardless of RPN (undersize: S = 9)"}


def ex_reliability():
    mtbf_chiller = 3000.0
    t = 720.0                       # one month of 24/7 operation, h
    r_ch = math.exp(-t / mtbf_chiller)
    r_pump = math.exp(-t / 5000.0)
    r_ctrl = math.exp(-t / 20000.0)
    series = r_ch * r_pump * r_ctrl
    return {"chiller R(720 h), MTBF 3,000 h": round(r_ch, 4), "coolant pump R(720 h), MTBF 5,000 h": round(r_pump, 4),
            "controller R(720 h), MTBF 20,000 h": round(r_ctrl, 4), "series system R(720 h)": round(series, 4),
            "system failure rate per 1,000 h": round(1000 * (1 / 3000 + 1 / 5000 + 1 / 20000), 3),
            "system MTBF (h)": round(1 / (1 / 3000 + 1 / 5000 + 1 / 20000)),
            "with a redundant chiller (1-of-2)": round((1 - (1 - r_ch) ** 2) * r_pump * r_ctrl, 4)}


def ex_pilot():
    from statsmodels.stats.proportion import proportions_ztest, confint_proportions_2indep
    d = load("pilot_results.csv").set_index("phase")
    x = [d.loc["before", "defective"], d.loc["after", "defective"]]
    n = [d.loc["before", "inspected"], d.loc["after", "inspected"]]
    z, p = proportions_ztest(x, n)
    lo, hi = confint_proportions_2indep(x[0], n[0], x[1], n[1])
    c = load("tooling_cost.csv").set_index("item").value
    tool_before = c.tool_edge_cost_usd / c.parts_per_edge_before
    tool_after = c.tool_edge_cost_usd / c.parts_per_edge_after
    cost_before = c.conversion_cost_excl_tooling_usd + tool_before
    cost_after = c.conversion_cost_excl_tooling_usd + tool_after
    scrap_saved = (x[0] / n[0] - x[1] / n[1]) * c.scrap_cost_per_oversize_part_usd
    return {"before / after % defective": (round(100 * x[0] / n[0], 2), round(100 * x[1] / n[1], 2)),
            "two-proportion z, p": (round(z, 2), float(f"{p:.2g}")),
            "95% CI for reduction (percentage points)": (round(100 * lo, 2), round(100 * hi, 2)),
            "tooling cost per part before / after (USD)": (round(tool_before, 4), round(tool_after, 4)),
            "tooling cost per part change %": round(100 * (tool_after / tool_before - 1), 1),
            "cost per part before / after (USD)": (round(cost_before, 4), round(cost_after, 4)),
            "cost per part change %": round(100 * (cost_after / cost_before - 1), 2),
            "scrap avoided per part made (USD)": round(scrap_saved, 4),
            "net saving per part made (USD)": round(scrap_saved - (tool_after - tool_before), 4)}


def ex_staged():
    d = load("pilot_daily.csv")
    out = {}
    for st, g in d.groupby("stage", sort=False):
        pbar = g.oversize.sum() / g.inspected.sum()
        n = g.inspected.iloc[0]
        ucl = pbar + 3 * math.sqrt(pbar * (1 - pbar) / n)
        lcl = max(0.0, pbar - 3 * math.sqrt(pbar * (1 - pbar) / n))
        p = g.oversize / g.inspected
        out[st] = {"p-bar %": round(100 * pbar, 2), "UCL %": round(100 * ucl, 2), "LCL %": round(100 * lcl, 2),
                   "days outside": int(((p > ucl) | (p < lcl)).sum())}
    return {"staged p chart (separate limits per stage)": out}


def _clean(o):
    if isinstance(o, dict):
        return {k: _clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return type(o)(_clean(v) for v in o)
    if isinstance(o, np.generic):
        return o.item()
    return o


EX = {"yield": ex_yield, "describe": ex_describe, "pareto": ex_pareto, "distribution": ex_distribution, "cleanse": ex_cleanse,
      "grr": ex_grr, "attribute": ex_attribute, "sample_size": ex_sample_size, "baseline": ex_baseline, "spc": ex_spc,
      "capability": ex_capability, "stratify": ex_stratify, "regression": ex_regression, "fmea": ex_fmea,
      "reliability": ex_reliability, "pilot": ex_pilot, "staged": ex_staged}

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
