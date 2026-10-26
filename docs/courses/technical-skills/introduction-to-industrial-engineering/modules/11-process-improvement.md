# Module 11 — Process Improvement: Lean, Six Sigma and Root Cause Analysis

**Time:** 90 min

## Learning objectives

1. Define and manage work processes using Lean, Six Sigma and root cause analysis.
2. Choose the right approach for a problem.

## 1. Three complementary approaches

| | Lean | Six Sigma | Root cause analysis |
|---|---|---|---|
| Goal | Speed and flow; remove waste | Reduce variation and defects | Find and remove causes of a specific problem |
| Core method | Value stream, takt, flow, pull, standard work | DMAIC with statistics | Problem statement → causes → verify → act |
| Typical tools | VSM, 5S, SMED, kanban, kaizen | SPC, capability, hypothesis tests, DOE, regression | Fishbone, 5-Why, Pareto, stratification |
| Duration | Days (kaizen) to months | Weeks to months | Hours to weeks |

## 2. Lean in brief

- **Value** is defined by the customer; everything else is waste.
- **Eight wastes (DOWNTIME):** Defects, Overproduction, Waiting, Non-utilized talent, Transportation, Inventory, Motion, Extra-processing.
- **Takt time** = available time ÷ demand — the pace of work. Kit packing, per shift: 450 min × 60 / 2,600 kits = **10.4 s per kit** for the department.
- **Flow, pull, standard work, 5S, kaizen.**

## 3. Six Sigma in brief

**DMAIC:** Define (problem, customer, goal) → Measure (baseline, measurement system) → Analyze (root causes with data) → Improve (solutions, pilot) → Control (standardize, monitor with control charts).

Six Sigma's focus on variation matters for IEs: a 61.5 s *average* standard hides that some kits take far longer — and variation, not the average, drives waiting and missed shipments.

## 4. Root cause analysis in brief

1. Write a clear problem statement (what, where, when, how much — no cause, no solution).
2. Pareto the data; stratify (by shift, product, person).
3. Fishbone of possible causes; 5-Why the likely ones.
4. Verify with data.
5. Fix the root cause (prefer error-proofing), verify effectiveness.

**Case — kit shortages:** Pareto of 140 shortages in a month: 62% due to a bin being empty when picked. 5-Why: bins are refilled once per shift by the material handler → there's no signal when a bin runs low → **root cause: no replenishment trigger.** Fix: two-bin kanban at the packing benches (consistent with the 11.5% waiting found by work sampling).

## 5. Go deeper

This repository has full courses on each: *Lean Methods Accelerator*, *Kaizen Leader*, *Process Mapping*, *Root Cause Analysis*, *Charting Process Behavior*, *Fundamentals of Hypothesis Testing*, *Design for Six Sigma*.

## Check yourself

Department takt is 10.4 s per kit and the standard time is 61.5 s. How many packers must be packing at the same time to keep pace?

<details><summary>Answer</summary>

61.5 / 10.4 ≈ 5.9 → about 6 packers working continuously at standard pace. Staffing 7 per shift (Module 5) allows for the 90% planned efficiency. Today's losses (waiting 11.5%, walking 7.5% from work sampling) mean 7 people still need overtime — removing those losses is the improvement opportunity.
</details>
