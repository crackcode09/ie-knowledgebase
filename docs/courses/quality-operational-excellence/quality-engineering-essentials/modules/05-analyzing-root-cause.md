# Module 05 — Analyzing Potential Root Causes

## Objectives

- Write an effective problem statement and follow a disciplined path to root cause.
- Use cause-and-effect diagrams, 5-Why/1-How and root cause trees.
- Verify causes with stratification, box plots, scatter plots and simple regression.
- Assess risk with FMEA and basic reliability calculations.

## The path to root cause

1. **Describe** the problem precisely (what, where, when, how big — not why).
2. **Generate** possible causes broadly (fishbone, root cause tree).
3. **Narrow** with logic and process knowledge (5-Why).
4. **Verify** with data (stratification, graphs, regression, tests).
5. **Confirm** by turning the cause on and off where safe (pilot, Module 06).

Jumping from step 1 to a solution is the most common failure.

## Effective problem statements

| Weak | Strong |
|---|---|
| "Quality is bad on the lathes." | "8.3 % of inserts sampled from M1/M2 over 20 days were defective; 50 % of defectives were OD oversize (> 6.375 mm), concentrated on M2 (19 of 20)." |

Is/is-not thinking helps: oversize **is** on M2 (19 of 20) and worse on shifts B/C; it **is not** on M1 shift A. Those contrasts point at causes.

## Generating causes

**Cause-and-effect (fishbone) diagram** for "OD oversize," by category:

- **Machine:** M2 thermal growth; spindle bearing play; offset not updated
- **Method:** tool change interval too long; no offset rule after tool change
- **Material:** bar stock diameter/hardness variation
- **Measurement:** micrometer technique (reproducibility, Module 03)
- **Environment:** coolant temperature rises in afternoon/evening; shop temperature
- **People:** offset adjustment habits differ by shift

**5-Why, 1-How** — drive one branch to a controllable cause, then ask how to fix it:

1. Why oversize? → The tool cuts less as it wears.
2. Why does wear reach oversize? → Tools run up to ~2,400 parts with no offset compensation.
3. Why no compensation? → No rule for when or how much to adjust.
4. Why no rule? → The standard work only says "check hourly."
5. Why? → Wear rate was never measured.
→ **How:** measure wear rate, set a tool-change interval and an offset-compensation rule.

**Root cause tree** — a hierarchical version of the fishbone that keeps asking "what could cause this?" level by level, with each branch marked verified, ruled out or open (`templates/root-cause-tree.md`).

## Verifying causes with data

**Stratification** — compare groups (`python tools/qekit.py stratify`):

| Machine–shift | Mean OD | % oversize |
|---|---|---|
| M1-A | 6.35556 | 0.0 |
| M1-B | 6.36134 | 0.0 |
| M1-C | 6.35957 | 1.2 |
| M2-A | 6.36319 | 3.8 |
| M2-B | 6.36926 | 13.8 |
| M2-C | 6.36747 | 6.2 |

19 of 20 oversize parts are from M2 (chi-square p = 0.0001).

**Box plots and scatter plots:**

![Box and scatter](../figures/05_box_scatter.png)

M2 runs higher on every shift; OD rises with tool age on both machines.

**Simple and multiple regression:**

- OD vs tool age alone: slope **0.0051 mm per 1,000 parts**, R² 0.23.
- OD vs tool age + coolant temperature + machine: R² **0.64**.
  - Tool age: +0.0145 mm over a 2,400-part tool life
  - Coolant: +0.0038 mm per +3 °C
  - M2 vs M1: +0.0078 mm

**Verified causes:** M2's offset (≈ 0.008 mm high), tool wear without compensation, and coolant temperature (hotter on later shifts). Together they explain about two-thirds of OD variation. Regression shows association; the pilot (Module 06) confirms cause.

## FMEA

Failure mode and effects analysis rates each failure mode for **severity (S)**, **occurrence (O)** and **detection (D)** on 1–10 scales; RPN = S × O × D.

| Step | Failure mode | S | O | D | RPN |
|---|---|---|---|---|---|
| Turn OD | OD oversize | 7 | 6 | 5 | 210 |
| Thread | Thread damage | 8 | 4 | 6 | 192 |
| Turn OD | OD undersize | 9 | 3 | 5 | 135 |
| Deburr | Burr | 4 | 4 | 4 | 64 |
| Knurl | Knurl incomplete | 8 | 2 | 4 | 64 |

Act on the highest RPNs, **and** review any severity ≥ 9 regardless of RPN (undersize inserts pull out in service). Thread damage's D = 6 reflects the unreliable visual inspection found in Module 03.

## Product and process reliability

Some causes are equipment failures. The coolant chiller that controls coolant temperature is part of a series system:

| Component | MTBF | R(720 h, one month) |
|---|---|---|
| Chiller | 3,000 h | 0.787 |
| Coolant pump | 5,000 h | 0.866 |
| Controller | 20,000 h | 0.965 |
| **Series system** | **1,714 h** | **0.657** |
| With a redundant chiller | | 0.797 |

(Exponential model, R(t) = e^(−t/MTBF); illustrative MTBFs.) A one-in-three chance of losing temperature control each month means coolant temperature — a verified cause of oversize — needs either redundancy or monitoring with an alarm.

## Run it

```bash
python tools/qekit.py stratify
python tools/qekit.py regression
python tools/qekit.py fmea
python tools/qekit.py reliability
```

## Check yourself

1. Why does a regression with R² = 0.64 not prove that coolant temperature causes oversize?
2. What does the is/is-not contrast "M2-B worst, M1-A best" suggest?
3. Compute the system MTBF of three series components with MTBFs 3,000, 5,000 and 20,000 h.

<details><summary>Answers</summary>

1. Correlation can arise from a lurking variable (e.g. later shifts have both hotter coolant and older tools). Confirm by changing the factor (a pilot or experiment).
2. Factors that differ between M2 and M1 (machine offset, thermal behavior) and between shift A and B (tool age accumulated since the morning change, coolant warming up).
3. Failure rates add: 1/3,000 + 1/5,000 + 1/20,000 = 0.000583/h → MTBF ≈ 1,714 h.

</details>
