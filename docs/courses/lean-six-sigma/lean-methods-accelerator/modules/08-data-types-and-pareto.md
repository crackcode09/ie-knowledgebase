# Module 8 — Measurement and Data Types; Pareto Charts

**Time:** 45 min

## Learning objectives

1. Distinguish discrete from continuous data and choose measurements accordingly.
2. Build and interpret a Pareto chart.

## 1. Data types

| | Discrete (attribute) | Continuous (variable) |
|---|---|---|
| What | Counts, categories, pass/fail | Measurements on a scale |
| Examples | Number of leakers; downtime reason; on-time yes/no | Cycle time; changeover minutes; bore diameter; leak rate |
| Information per data point | Low | High |
| Sample size needed | Larger | Smaller |

**Prefer continuous:** "changeover minutes" tells far more than "changeover on time: yes/no"; "leak rate in cc/min" more than pass/fail. Record time-stamped data with context (machine, shift, product family) so it can be stratified later.

**Good measurement** also needs an operational definition (when does a changeover start and stop?) and a measurement system that's repeatable.

## 2. Pareto charts

Sort categories from largest to smallest; add cumulative %. Focus on the "vital few."

### Case — CNC downtime, 4 weeks

```bash
python tools/lean.py pareto
```

| Reason | Minutes | % | Cum % |
|---|---|---|---|
| Tool breakage | 1,260 | 30.0 | 30.0 |
| Changeover overrun | 980 | 23.3 | 53.3 |
| Waiting for material | 720 | 17.1 | 70.5 |
| Coolant / chips | 510 | 12.1 | 82.6 |
| Program errors | 340 | 8.1 | 90.7 |
| Gauge problems | 210 | 5.0 | 95.7 |
| Other | 180 | 4.3 | 100.0 |

Four reasons cause 83% of downtime. Tool breakage → TPM and tool-life management (Module 19); changeover overrun → SMED (Module 15); waiting for material → pull (Module 17).

Use the measure that reflects impact (minutes or cost, not just number of events), keep "Other" small, and drill down (a second-level Pareto of tool breakage by tool).

## Check yourself

The team only recorded "downtime: yes/no" per hour. What can't they do?

<details><summary>Answer</summary>

Quantify how much time each cause costs, or Pareto by minutes — they'd need the duration and reason of each stop.
</details>
