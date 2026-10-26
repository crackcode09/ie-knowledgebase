# Module 5 — Statistical Process Control for New Processes

**Time:** 2 h · **Phase:** Design

## Learning objectives

1. Plan which characteristics get process behavior charts in a new process.
2. Choose chart types and subgroups during design, not after launch.

## 1. Why plan SPC during design?

A capability prediction (Module 4) only holds if the process stays predictable. Designing the monitoring at the same time as the process means the right measurements, gauges, data fields and sampling points exist on day one.

## 2. What to chart

| Chart | Use for |
|---|---|
| Key **output** CTQs (from QFD/scorecard) | Verifying the process delivers what the design predicted |
| Key **input** variables (from DOE transfer functions, Module 9) | Catching changes before they affect output — often better than charting outputs |
| High-RPN failure modes (Module 6) | Where detection is weak and occurrence uncertain |

## 3. Choosing charts at design time

| Data | Sampling | Chart |
|---|---|---|
| Continuous, one value per period (e.g., bath temperature) | Hourly | XmR |
| Continuous, small subgroups of consecutive parts | 3–5 parts every 2 h | X̄–R |
| Many part numbers on one machine | Every part/lot | Deviation-from-nominal or Z–MR |
| Defectives / defects | Per lot or shift | p / u chart, or XmR on the rates |

Design the **rational subgroups** around the variation sources you want to detect (spindles, cavities, shifts — separate them, don't mix them).

## 4. Early production

- New processes rarely have 20–30 points of history. Compute **provisional limits** from the first 8–10 points, revise at 20–25.
- Short-run charts let you chart the machine, not the part number.
- Use the chart in pilots (Module 14) as evidence that the process is stable before you trust its capability.

The full method — limits, detection rules, subgrouping — is in *Charting Process Behavior* in this repository.

## Check yourself

1. Why chart an input like coolant temperature instead of only the output dimension?
2. A new 4-cavity mold: how should subgroups be formed?

<details><summary>Answers</summary>

1. Inputs change before outputs drift; charting the input gives earlier warning and points directly at the cause.
2. Chart each cavity separately (or subgroup within cavity); mixing cavities inflates the within-subgroup range and hides shifts.
</details>
