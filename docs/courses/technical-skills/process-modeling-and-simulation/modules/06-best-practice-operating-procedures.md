# Module 6 — Developing Best-Practice Operating Procedures

**Time:** 50 min

## Learning objectives

1. Use a model to compare operating rules (dispatching, priorities, batching).
2. Turn model results into standard operating procedures.

## 1. Rules matter as much as resources

With the same people and equipment, the **rules** — which job next, when to batch, who helps whom — change results substantially. A model can test rules that would be risky to trial live.

## 2. Dispatch rules (design F: pooled techs, parts stocked)

```bash
python tools/procsim.py sop
```

| Rule | Mean lead (h) | p90 lead (h) | On time | Contract customers on time |
|---|---|---|---|---|
| **FIFO** (first in, first out) | 4.10 | **7.06** | **94.4%** | 95.0% |
| SPT (shortest predicted repair first) | **3.54** | 7.64 | 91.1% | 90.6% |
| PRIORITY (contract customers first) | 3.89 | 7.54 | 92.1% | **99.3%** |

**Choice depends on the goal:** FIFO protects the same-day promise for everyone; PRIORITY nearly guarantees contract customers at a 2.3-point cost to everyone else; SPT optimizes an average nobody is promised.

## 3. Batching the test rig

```bash
python tools/procsim.py batching
```

| Test batch size | Mean lead (h) | p90 lead (h) | On time | Rig utilization |
|---|---|---|---|---|
| 1 (test each unit when ready) | **4.08** | 7.04 | 94.5% | 60% |
| 3 | 4.23 | 7.13 | 94.3% | 38% |
| 6 | 4.58 | 7.15 | 94.8% | 33% |

Batching saves rig time (and rig setup effort), but the rig isn't the constraint, so the saving buys nothing; units wait for the batch to fill, raising mean lead time by up to half an hour. On-time barely moves because late jobs are driven by repair and parts, not testing. **Batch only where setup time at a constraint justifies it.**

## 4. Writing the SOP

| Element | Procedure (from model) |
|---|---|
| Dispatch | FIFO for all repair work; contract jobs flagged but not jumped unless within 2 h of promise |
| Pooling | Any qualified tech takes the next job; diagnosis first in the morning peak |
| Testing | Test each unit as soon as repaired (no batching) |
| Escalation | If repair queue > 6 jobs, call flex tech; if a job reaches 6 h, supervisor reviews |
| Review | Monthly: compare actual on-time with model; update model inputs quarterly |

## Check yourself

Why might a planner prefer SPT even though on-time falls?

<details><summary>Answer</summary>

It maximizes the number of jobs finished early and lowers average WIP — attractive if the KPI is throughput or average lead time — but it fails the customer promise for long jobs. Pick the rule that matches the real goal.
</details>
