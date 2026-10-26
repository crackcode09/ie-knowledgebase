# Module 7 — Detection Rules: Common vs Special Cause

**Time:** 45 min · **Data:** `data/shaft_diameter.csv`

## Learning objectives

1. Apply the four Western Electric zone tests.
2. Choose how many rules to use and understand the false-alarm trade-off.
3. Write a reaction plan for signals.

## 1. Zones

Divide the space between center line and each limit into three equal zones (each one σ̂ wide):

```
UCL  ───────────────────────
      Zone A   (2σ to 3σ)
     ───────────────────────
      Zone B   (1σ to 2σ)
     ───────────────────────
      Zone C   (0 to 1σ)
CL   ═══════════════════════
      Zone C
     ───────────────────────
      Zone B
     ───────────────────────
      Zone A
LCL  ───────────────────────
```

## 2. The four rules

These are the zone tests published in the Western Electric *Statistical Quality Control Handbook* (1956), and the set Wheeler recommends.

| Rule | Signal | Detects |
|---|---|---|
| **1** | One point beyond a 3σ limit | Large, sudden change |
| **2** | 2 of 3 successive points beyond 2σ, same side | Moderate shift |
| **3** | 4 of 5 successive points beyond 1σ, same side | Small sustained shift |
| **4** | 8 successive points on the same side of the center line | Small sustained shift |

Other rule sets exist (e.g., the eight Nelson rules, which add trend and stratification tests). More rules = more sensitivity and more false alarms.

**Practical guidance:**

- Rule 1 always.
- Add Rules 2–4 when you need sensitivity to small shifts and the chart is reviewed by someone who can investigate.
- For a busy floor chart, Rule 1 + Rule 4 is a common, workable pair.
- Rules 2–4 assume roughly symmetric zones; use them cautiously on attribute charts with asymmetric limits.

## 3. Worked example

Shaft diameter, baseline limits from hours 1–20: CL 12.6992, σ̂ 0.00570.
Zone boundaries above the center: 1σ = 12.7049, 2σ = 12.7106, 3σ = 12.7163.

```bash
python tools/spc.py xmr data/shaft_diameter.csv value --baseline 20
```

Applying the baseline limits to hours 1–30 (indices reported 1-based):

| Rule | Hours where the signal completes |
|---|---|
| 1 | 22, 25, 26, 28, 30 |
| 2 | 22, 23, 24, 25, 26, 28, 30 |
| 3 | 24–30 |
| 4 | 28, 29, 30 |

All four rules agree: the shift started around hour 21. Rule 2 caught it at hour 22 — as early as Rule 1. In smaller shifts, Rules 2–4 typically fire before Rule 1.

## 4. Responding to a signal: the reaction plan

A chart without a reaction plan is wallpaper. A minimal plan, posted with the chart:

1. **Stop and confirm.** Re-measure the part. Check the gauge.
2. **Contain.** Quarantine parts made since the last good point if the signal threatens spec.
3. **Look for the cause.** Ask *what changed?* — material lot, tool, setup, operator, program, environment. Note it on the chart.
4. **Act.** Remove a harmful cause; if a cause improves things, make it permanent.
5. **Don't adjust on noise.** No signal → no adjustment (Module 10).

## Exercise 7.1

Using limits from hours 1–20, check each of hours 21–25 against all four rules by hand. Which rule fires first?

<details><summary>Answer</summary>

Hour 22: Rule 1 (12.7203 > 12.7163) and Rule 2 (hours 21 and 22 both > 12.7106). Hour 21 itself (12.7112) is only just above 2σ and fires nothing on its own.
</details>

## Check yourself

1. Points 11–18 are all slightly above the center line, none beyond 1σ. Is this a signal?
2. Why not use all eight Nelson rules everywhere?

<details><summary>Answers</summary>

1. Yes — Rule 4 (8 in a row on one side).
2. Every added rule increases the false-alarm rate; operators stop trusting a chart that cries wolf.
</details>
