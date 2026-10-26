# Module 03 — The Reliability Program, Change Management and Metrics

## Objectives

- Identify the essential elements of a successful reliability program.
- Use management of change to protect reliability.
- Calculate and interpret MTBF, MTTR and availability, and choose a balanced set of leading and lagging metrics.
- Find ways to optimize the program.

## Essential program elements

1. **Leadership and policy** — a sponsor, goals tied to business results, and resources.
2. **Asset register and criticality** (Module 01).
3. **Maintenance strategy per asset** — PM, PdM, run-to-failure, redesign — chosen by RCM-style logic (Module 04).
4. **Work management** — identify, plan, schedule, execute, close out with good failure data.
5. **Failure reporting and RCA** (Module 08).
6. **Spare parts and stores** — critical spares stocked, stored correctly (e.g. motor shafts rotated, bearings kept clean and dry).
7. **Precision maintenance skills** — alignment, balancing, lubrication, torque.
8. **Lifecycle management** — design, purchase, installation and disposal decisions (Module 02).
9. **Management of change** (below).
10. **Metrics and continuous improvement.**

A program is only as strong as its weakest element: excellent Weibull analysis is useless if work orders record "fixed it" as the failure description.

## Management of change (MOC)

Many failures follow an undocumented change: a different lubricant, a "temporary" bypass, a new supplier's seal, a higher production rate. MOC requires that changes to equipment, materials, procedures or operating limits are:

1. proposed and described;
2. reviewed for risk (safety, reliability, quality) by the right people;
3. approved;
4. implemented with updated drawings, PM plans, spares and training;
5. verified after implementation.

Like-for-like replacement usually doesn't need MOC; anything else does.

## Core metrics

From the coolant pump history (`data/coolant_pump_failures.csv`, 14 failures):

| Metric | Formula | Value |
|---|---|---|
| MTBF | total operating time / number of failures | **1,949 h** |
| MTTR | total repair time / number of repairs | **3.29 h** |
| Inherent availability A_i | MTBF / (MTBF + MTTR) | **99.83 %** |
| Operational availability A_o (adding a 6-h average delay for parts and call-out, illustrative) | MTBF / (MTBF + MTTR + delay) | **99.53 %** |
| Downtime per 6,000 operating hours | 6,000 / MTBF × (MTTR + delay) | **28.6 h** |

The pump's repair is quick; the **waiting** is the bigger loss — a stores and planning problem, not a repair-skill problem. That insight comes from splitting the metric.

**Availability percentages look deceptively high.** 99.5 % sounds excellent, but 28.6 h of unplanned downtime a year on a bottleneck can cost far more than the pump. Report hours and dollars alongside percentages.

## A balanced scorecard

| Leading (predict results) | Lagging (record results) |
|---|---|
| PM schedule compliance | MTBF by critical asset |
| % of work that is planned | Unplanned downtime hours |
| % of PdM-detected faults acted on before failure | Maintenance cost per unit produced |
| Backlog in weeks | Availability; OEE |
| RCA actions completed on time | Repeat failures |
| Training hours on precision skills | Safety incidents linked to equipment |

Track a few of each. Lagging metrics tell you if you've arrived; leading metrics tell you if you're on the road.

## Optimizing the program

- **Benchmark** against your own history and, where available, industry data — carefully, since definitions differ.
- **Assess** the program against the element list above (a self-assessment scored 1–5 per element is a good start; `templates/program-assessment.md`).
- **Pareto** the losses (Module 05) and fix the vital few.
- **Remove** PM tasks that add no value (Module 09) and move effort to condition monitoring where it pays.
- **Feed back** failure data into design and purchasing.

## Run it

```bash
python tools/relkit.py metrics
```

## Check yourself

1. MTBF rose from 1,949 h to 3,000 h. Recalculate A_o with the same MTTR and delay.
2. Why is "PM compliance 98 %" not proof of a good program?
3. Give an example of a change that would need MOC on Line A.

<details><summary>Answers</summary>

1. 3,000 / (3,000 + 3.29 + 6) = 99.69 %.
2. The PMs might be the wrong tasks at the wrong intervals. Compliance measures execution, not effectiveness — pair it with failure rates on the assets.
3. Switching the hydraulic press to a different oil grade, changing the coolant concentrate brand, raising press tonnage for a new product, or bypassing a level switch.

</details>
