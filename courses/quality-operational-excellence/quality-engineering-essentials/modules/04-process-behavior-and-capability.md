# Module 04 — Charting Process Behavior and Capability Analysis

## Objectives

- Use trend charts and control charts to understand process behavior.
- Select the right control chart; apply rational subgrouping.
- Handle skewed data with a transformation; use stage variables for before/after limits.
- Assess process capability.

This module covers the essentials. For more depth, see [Statistical Quality Control](../../statistical-quality-control/README.md) and [Charting Process Behavior](../../charting-process-behavior/README.md).

## Trend charts and control charts

A **trend (run) chart** plots data in time order with a median line — the minimum for seeing shifts, trends and cycles. A **control chart** adds limits based on common-cause variation (center ± 3σ, with σ estimated from short-term variation), so you can tell signals from noise:

- point outside a limit; runs of 8 on one side; trends; other run rules.
- **Common cause** → improve the system; **special cause** → find and remove it. Don't adjust a stable process for noise.

## Chart selection

| Data | Subgroup | Chart |
|---|---|---|
| Continuous | 1 per period | **X and moving range (I–MR)** |
| Continuous | 2–9 | **X̄–R** |
| Continuous | ≥ 10 | X̄–S |
| Defectives (pass/fail) | any n | **p** (np if n constant) |
| Defects (counts) | equal area/opportunity | c; unequal → **u** |

**Rational subgrouping:** subgroups should contain only common-cause variation (e.g. 5 consecutive inserts from one machine), so that differences **between** subgroups reveal special causes. Don't mix M1 and M2 in one subgroup.

## X and moving range with a transformation

Quote turnaround (Module 02) is lognormal. Charted raw:

| | Center | UCL | LCL | Points outside |
|---|---|---|---|---|
| Raw hours | 20.8 h | 56.3 h | −14.7 h (impossible) | 2 |
| ln(hours) | 2.894 | 4.634 | 1.154 | 0 |

Back-transformed, the log-scale limits are **3.2 to 102.9 hours**.

![Transformation](../figures/04_individuals_transform.png)

On the raw scale the chart flags two slow quotes that are simply the normal long tail of a skewed process — false alarms — and shows an impossible negative LCL. After a log transform the process is stable. I–MR charts are sensitive to non-normality; X̄ charts are much less so (averages tend toward normal).

## X̄–R on OD

For OD, Bayline charts 5 consecutive inserts per hour **per machine**. (Construction is covered in detail in the Statistical Quality Control course; the constants for n = 5 are A₂ = 0.577, D₃ = 0, D₄ = 2.114.) Because OD grows with tool wear and resets at each tool change (Module 05), expect a saw-tooth pattern on each machine's chart — OD climbing between tool changes. That is a predictable, assignable pattern, not random noise, and the chart should be annotated with tool changes.

## Stage variables

When a process is deliberately changed, compute **separate limits for each stage** instead of one set across the change. Bayline's pilot on M2 (Module 06) — daily % oversize on a p chart:

| Stage | p̄ | UCL | LCL | Points outside |
|---|---|---|---|---|
| Before (n = 240/day) | 7.92 % | 13.15 % | 2.69 % | 0 |
| After (n = 180/day) | 0.33 % | 1.62 % | 0 | 0 |

![Staged p chart](../figures/04_staged_p_chart.png)

Both stages are stable — at very different levels. The staged chart shows the change was real and the new level is holding.

## Process capability

Capability compares the voice of the process with the voice of the customer. Indices (for a **stable** process): Cp = tolerance / 6σ (potential); Cpk = distance from mean to nearest limit / 3σ (actual). Pp and Ppk use the overall standard deviation.

**Baseline OD capability by machine** (spec 6.325–6.375 mm):

| | Mean | SD | Pp | Ppk | Expected out of spec |
|---|---|---|---|---|---|
| M1 | 6.35882 | 0.00586 | 1.42 | 0.92 | 0.29 % |
| M2 | 6.36664 | 0.00597 | 1.40 | **0.47** | **8.09 %** |

Both machines have similar spread (Pp ≈ 1.4: the variation would fit the tolerance). The problem is **centering**: M2 runs 0.017 mm above target, M1 0.009 mm. Centering plus controlling the drift (Module 05) is the opportunity — not a new machine.

## Run it

```bash
python tools/qekit.py spc
python tools/qekit.py staged
python tools/qekit.py capability
```

## Check yourself

1. Why chart M1 and M2 separately?
2. Why is a negative LCL a warning sign on an individuals chart of times?
3. M2's Pp is 1.40 but Ppk is 0.47. What single action would have the biggest effect?

<details><summary>Answers</summary>

1. They're different process streams with different centers; mixing them inflates variation, widens limits and hides machine-specific signals.
2. Times can't be negative; it indicates skewed data being treated as symmetric, so limits (and signals) are unreliable — consider a transformation or a distribution-specific chart.
3. Re-center M2 (and control what drives it high — offset, tool wear, coolant temperature); spread is already adequate.

</details>
