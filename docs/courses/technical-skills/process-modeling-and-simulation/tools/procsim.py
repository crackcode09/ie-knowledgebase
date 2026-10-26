"""procsim.py - a small, readable discrete-event simulator for service and production processes.

Running case: a same-day repair service center for industrial pumps and gearboxes.
Units arrive through the day, are checked in, diagnosed, repaired, tested (with a rework loop)
and released. Customers are promised same-day turnaround (8 h).

    python tools/procsim.py all          # every worked example in the course
    python tools/procsim.py <name>       # static, baseline, validate, designs, resilience, sop,
                                         # batching, fmea, business

Only numpy is needed. License: MIT
"""
from __future__ import annotations

import heapq
import math
import sys
from dataclasses import dataclass, field

import numpy as np

# ------------------------------------------------------------------ model definition
OPEN_H = 10.0                         # center open 10 h/day for arrivals (07:00-17:00)
HOURS_DAY = 14.0                      # staff work until 21:00 to finish
ARRIVALS_PER_HOUR = [3, 6, 8, 7, 5, 4, 5, 6, 4, 2]   # by hour of day (peaks mid-morning)
PROMISE_H = 8.0


@dataclass
class Design:
    name: str = "Current"
    checkin_staff: int = 1
    diag_techs: int = 2
    repair_techs: int = 4
    test_rigs: int = 1
    pooled_techs: bool = False         # one cross-trained pool does diagnosis and repair
    dispatch: str = "FIFO"             # FIFO, SPT (shortest predicted repair first), PRIORITY (contract customers first)
    test_batch: int = 1                # units tested together
    rework_p: float = 0.12             # share failing test -> back to repair
    arrival_scale: float = 1.0
    service_cv_scale: float = 1.0
    rig_breakdown_h: float = 0.0       # one breakdown of this length at a random time each day
    tech_absent: int = 0               # repair techs absent
    parts_wait_p: float = 0.25         # share of jobs that wait for a part after diagnosis
    parts_wait_h: tuple = (3.0, 0.5)   # mean and cv of the parts wait (h); no technician is busy
    seed: int = 1
    # service-time means (h) and coefficients of variation
    t_checkin: tuple = (0.10, 0.3)
    t_diag: tuple = (0.45, 0.6)
    t_repair: tuple = (0.95, 0.8)
    t_test: tuple = (0.15, 0.2)


def _draw(rng, mean, cv, scale=1.0):
    cv = cv * scale
    if cv <= 0:
        return mean
    s2 = math.log(1 + cv * cv)
    return float(rng.lognormal(math.log(mean) - s2 / 2, math.sqrt(s2)))


@dataclass(order=True)
class _Ev:
    t: float
    seq: int
    kind: str = field(compare=False)
    job: int = field(compare=False, default=-1)
    stage: str = field(compare=False, default="")


def simulate_day(d: Design, rng) -> dict:
    """Simulate one day. Returns per-job records and resource busy time."""
    # arrivals: nonhomogeneous Poisson by hour
    arr = []
    for h, lam in enumerate(ARRIVALS_PER_HOUR):
        n = rng.poisson(lam * d.arrival_scale)
        arr += list(h + np.sort(rng.uniform(0, 1, n)))
    arr = sorted(arr)
    n = len(arr)
    contract = rng.random(n) < 0.35
    repair_need = [_draw(rng, d.t_repair[0], d.t_repair[1], d.service_cv_scale) for _ in range(n)]
    diag_est = [r * float(rng.uniform(0.7, 1.3)) for r in repair_need]   # diagnosis predicts repair length

    cap = {"checkin": d.checkin_staff, "test": d.test_rigs}
    if d.pooled_techs:
        cap["tech"] = d.diag_techs + d.repair_techs - d.tech_absent
    else:
        cap["diag"] = d.diag_techs
        cap["repair"] = d.repair_techs - d.tech_absent
    busy_n = {k: 0 for k in cap}
    busy_time = {k: 0.0 for k in cap}
    queue = {k: [] for k in cap}
    done = [None] * n
    seq = [0]
    ev = []

    def push(t, kind, job=-1, stage=""):
        seq[0] += 1
        heapq.heappush(ev, _Ev(t, seq[0], kind, job, stage))

    def res_of(stage):
        if stage == "rework":
            stage = "repair"
        if d.pooled_techs and stage in ("diag", "repair"):
            return "tech"
        return stage

    rig_down = None
    if d.rig_breakdown_h > 0:
        start = float(rng.uniform(1, 8))
        rig_down = (start, start + d.rig_breakdown_h)

    for j, a in enumerate(arr):
        push(a, "arrive", j)

    def key(job, stage):
        if stage == "repair" and d.dispatch == "SPT":
            return diag_est[job]
        if d.dispatch == "PRIORITY" and stage in ("diag", "repair"):
            return 0 if contract[job] else 1
        return 0

    def try_start(t, r):
        while queue[r] and busy_n[r] < cap[r]:
            if r == "test":
                if rig_down and rig_down[0] <= t < rig_down[1]:
                    push(rig_down[1], "retry", stage="test")
                    return
                if len(queue[r]) < d.test_batch and t < HOURS_DAY - 0.5 and not _arrivals_done(t):
                    return  # wait to fill a batch
                batch = [queue[r].pop(0)[2] for _ in range(min(d.test_batch, len(queue[r])))]
                dur = _draw(rng, d.t_test[0] * (1 + 0.2 * (len(batch) - 1)), d.t_test[1])
                busy_n[r] += 1
                busy_time[r] += dur
                for jb in batch:
                    push(t + dur, "end", jb, "test")
                push(t + dur, "free", stage="test")
                continue
            queue[r].sort(key=lambda x: (x[0], x[1]))
            _, _, job, stage = queue[r].pop(0)
            if stage == "checkin":
                dur = _draw(rng, *d.t_checkin)
            elif stage == "diag":
                dur = _draw(rng, d.t_diag[0], d.t_diag[1], d.service_cv_scale)
            else:
                dur = repair_need[job] if stage == "repair" else repair_need[job] * 0.4  # rework is shorter
            busy_n[r] += 1
            busy_time[r] += dur
            push(t + dur, "end", job, stage)

    arrivals_done_at = arr[-1] if arr else 0.0

    def _arrivals_done(t):
        return t >= arrivals_done_at

    def enqueue(t, job, stage):
        r = res_of(stage)
        if r == "test":
            queue[r].append((0, t, job))
        else:
            queue[r].append((key(job, "repair" if stage == "rework" else stage), t, job, stage))
        try_start(t, r)

    rework_flag = [False] * n
    while ev:
        e = heapq.heappop(ev)
        t = e.t
        if e.kind == "arrive":
            enqueue(t, e.job, "checkin")
        elif e.kind == "parts":
            enqueue(t, e.job, "repair")
        elif e.kind == "retry":
            try_start(t, "test")
        elif e.kind == "free":
            busy_n["test"] -= 1
            try_start(t, "test")
        elif e.kind == "end":
            stg = e.stage
            if stg != "test":
                busy_n[res_of(stg)] -= 1
                try_start(t, res_of(stg))
            if stg == "checkin":
                enqueue(t, e.job, "diag")
            elif stg == "diag":
                if rng.random() < d.parts_wait_p:
                    push(t + _draw(rng, *d.parts_wait_h), "parts", e.job)
                else:
                    enqueue(t, e.job, "repair")
            elif stg in ("repair", "rework"):
                enqueue(t, e.job, "test")
            elif stg == "test":
                if (not rework_flag[e.job]) and rng.random() < d.rework_p:
                    rework_flag[e.job] = True
                    enqueue(t, e.job, "rework")
                else:
                    done[e.job] = t
    # rework uses the repair resource
    lead = np.array([done[j] - arr[j] for j in range(n) if done[j] is not None])
    return {"n": n, "lead": lead, "busy": busy_time, "cap": cap,
            "contract_lead": np.array([done[j] - arr[j] for j in range(n) if done[j] is not None and contract[j]])}


def run(d: Design, days=200) -> dict:
    rng = np.random.default_rng(d.seed)
    leads, units, busy, ontime_days, cl = [], 0, None, [], []
    for _ in range(days):
        r = simulate_day(d, rng)
        leads.append(r["lead"])
        cl.append(r["contract_lead"])
        units += r["n"]
        ontime_days.append(float((r["lead"] <= PROMISE_H).mean()) if len(r["lead"]) else 1.0)
        if busy is None:
            busy = {k: 0.0 for k in r["busy"]}
        for k, v in r["busy"].items():
            busy[k] += v
    L = np.concatenate(leads)
    C = np.concatenate(cl)
    cap = r["cap"]
    util = {k: round(busy[k] / (cap[k] * HOURS_DAY * days), 2) if cap[k] else None for k in busy}
    od = np.array(ontime_days)
    half = 1.96 * od.std(ddof=1) / math.sqrt(days)
    return {"design": d.name, "units/day": round(units / days, 1), "mean lead (h)": round(float(L.mean()), 2),
            "p90 lead (h)": round(float(np.percentile(L, 90)), 2),
            "on time (<= 8 h)": round(float((L <= PROMISE_H).mean()), 3),
            "on-time 95% CI (daily mean)": (round(float(od.mean() - half), 3), round(float(od.mean() + half), 3)),
            "contract on time": round(float((C <= PROMISE_H).mean()), 3) if len(C) else None,
            "utilization (14 staffed h)": util}


# ------------------------------------------------------------------ examples
def ex_static():
    lam = sum(ARRIVALS_PER_HOUR) / OPEN_H
    day = sum(ARRIVALS_PER_HOUR)
    d = Design()
    load = {"checkin": day * d.t_checkin[0] / (d.checkin_staff * HOURS_DAY),
            "diag": day * d.t_diag[0] / (d.diag_techs * HOURS_DAY),
            "repair": day * d.t_repair[0] * (1 + d.rework_p * 0.4) / (d.repair_techs * HOURS_DAY),
            "test": day * d.t_test[0] * (1 + d.rework_p) / (d.test_rigs * HOURS_DAY)}
    work = d.t_checkin[0] + d.t_diag[0] + d.t_repair[0] * (1 + d.rework_p * 0.4) + d.t_test[0] * (1 + d.rework_p)
    det = run(Design(name="Deterministic (no variation)", service_cv_scale=0.0, seed=1), days=60)
    return {"average arrival rate (/h)": lam, "static utilization (daily work / staffed hours)": {k: round(v, 2) for k, v in load.items()},
            "static 'lead time' = sum of work (h)": round(work, 2),
            "simulation without service-time variation": det}


def ex_baseline():
    return run(Design())


HISTORY = {"mean lead (h)": 4.9, "p90 lead (h)": 8.4, "on time (<= 8 h)": 0.88, "units/day": 50}


def ex_validate():
    keys = ("units/day", "mean lead (h)", "p90 lead (h)", "on time (<= 8 h)")
    v1 = run(Design(name="v1 no parts waits", parts_wait_p=0.0))
    v2 = run(Design(name="v2 with parts waits"))
    return {"model v1 (no parts waits)": {k: v1[k] for k in keys},
            "model v2 (25% of jobs wait ~3 h for parts)": {k: v2[k] for k in keys},
            "history (last 3 months, illustrative)": HISTORY}


def ex_designs():
    out = []
    for d in (Design(name="A Current"),
              Design(name="B +1 repair tech", repair_techs=5),
              Design(name="C Cross-trained pool (6 techs)", pooled_techs=True),
              Design(name="D Pool + SPT dispatch", pooled_techs=True, dispatch="SPT"),
              Design(name="E Stock fast-moving parts (parts waits 25% -> 8%)", parts_wait_p=0.08),
              Design(name="F Pool + stock parts", pooled_techs=True, parts_wait_p=0.08)):
        r = run(d)
        out.append((r["design"], r["mean lead (h)"], r["p90 lead (h)"], r["on time (<= 8 h)"]))
    return {"design, mean lead, p90 lead, on time": out}


def ex_resilience():
    rows = []
    for name, base in (("A Current", {}), ("F Pool + parts", {"pooled_techs": True, "parts_wait_p": 0.08})):
        for s in (1.0, 1.1, 1.2):
            r = run(Design(name=name, arrival_scale=s, **base), days=150)
            rows.append((name, f"demand x{s}", r["on time (<= 8 h)"], r["p90 lead (h)"]))
        for cv in (1.5,):
            r = run(Design(name=name, service_cv_scale=cv, **base), days=150)
            rows.append((name, f"service variability x{cv}", r["on time (<= 8 h)"], r["p90 lead (h)"]))
    return {"design, stress, on time, p90 lead": rows}


def ex_sop():
    rows = []
    for disp in ("FIFO", "SPT", "PRIORITY"):
        r = run(Design(name=disp, pooled_techs=True, parts_wait_p=0.08, dispatch=disp))
        rows.append((disp, r["mean lead (h)"], r["p90 lead (h)"], r["on time (<= 8 h)"], r["contract on time"]))
    return {"rule, mean lead, p90 lead, on time, contract on time": rows}


def ex_batching():
    rows = []
    for b in (1, 3, 6):
        r = run(Design(name=f"test batch {b}", pooled_techs=True, parts_wait_p=0.08, test_batch=b), days=150)
        rows.append((b, r["mean lead (h)"], r["p90 lead (h)"], r["on time (<= 8 h)"], r["utilization (14 staffed h)"]["test"]))
    return {"batch size, mean lead, p90 lead, on time, rig utilization": rows}


def ex_fmea():
    base = run(Design(name="F baseline", pooled_techs=True, parts_wait_p=0.08), days=150)["on time (<= 8 h)"]
    modes = [("Test rig down 2 h", {"rig_breakdown_h": 2.0}),
             ("One tech absent", {"tech_absent": 1}),
             ("Rework rate doubles (24%)", {"rework_p": 0.24}),
             ("Demand +20% (seasonal)", {"arrival_scale": 1.2}),
             ("Parts supplier late (waits back to 25%)", {"parts_wait_p": 0.25})]
    rows = []
    for name, kw in modes:
        kw2 = {"pooled_techs": True, "parts_wait_p": 0.08}
        kw2.update(kw)
        r = run(Design(name=name, **kw2), days=150)
        rows.append((name, r["on time (<= 8 h)"], round(base - r["on time (<= 8 h)"], 3)))
    return {"baseline on time": base, "failure mode, on time, drop": rows}


def ex_business():
    """Annual cost-benefit of design options vs current (illustrative costs)."""
    units_year = 50 * 250
    late_cost = 180.0  # $ per late job: courier upgrade, customer credit
    options = {
        "B +1 repair tech": (Design(repair_techs=5), 0, 65_000),
        "C Cross-trained pool": (Design(pooled_techs=True), 6 * 6_000 + 15_000, 6 * 1.50 * 2_000),
        "E Stock fast-moving parts": (Design(parts_wait_p=0.08), 40_000, 0.25 * 40_000),
        "F Pool + stock parts": (Design(pooled_techs=True, parts_wait_p=0.08), 6 * 6_000 + 15_000 + 40_000,
                                 6 * 1.50 * 2_000 + 0.25 * 40_000),
    }
    base_late = (1 - run(Design())["on time (<= 8 h)"]) * units_year
    rows = []
    for name, (d, one_time, annual) in options.items():
        late = (1 - run(d)["on time (<= 8 h)"]) * units_year
        saving = (base_late - late) * late_cost
        net = saving - annual
        payback = round(12 * one_time / net, 1) if net > 0 and one_time else ("n/a" if net <= 0 else 0)
        rows.append((name, round(late), round(saving), round(annual), one_time, round(net), payback))
    return {"late jobs/yr, current": round(base_late),
            "option, late/yr, late-cost saving, annual cost, one-time cost, net/yr, payback (months)": rows}


EX = {"static": ex_static, "baseline": ex_baseline, "validate": ex_validate, "designs": ex_designs,
      "resilience": ex_resilience, "sop": ex_sop, "batching": ex_batching, "fmea": ex_fmea, "business": ex_business}

if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    for k, fn in EX.items():
        if which in ("all", k):
            print(f"\n=== {k}")
            for a, b in fn().items():
                if isinstance(b, list):
                    print(f"  {a}:")
                    for r in b:
                        print("    ", r)
                else:
                    print(f"  {a}: {b}")
