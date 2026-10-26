# Module 3 — Measurement and Data Types

**Time:** 30 min

## Learning objectives

1. Classify data by measurement scale (nominal, ordinal, interval, ratio).
2. Distinguish discrete from continuous data.
3. Pick summaries and charts that fit each data type.

## 1. Discrete vs continuous

| | Discrete (attribute) | Continuous (variable) |
|---|---|---|
| Values | Counts or categories | Any value on a scale, limited only by the instrument |
| Examples | Pass/fail; number of scratches; defect type; shift | Diameter, weight, temperature, cycle time |
| Information per observation | Low | High |
| Sample size needed | Large | Smaller |

**Prefer continuous data** when you can get it. A go/no-go gauge tells you a part failed; a micrometer tells you it's 0.004 mm over and trending up — you can act before parts fail.

## 2. Measurement scales

| Scale | What you can do | Examples | Typical summary |
|---|---|---|---|
| **Nominal** | Categories, no order | Defect type, machine, supplier | Counts, %, mode, Pareto chart |
| **Ordinal** | Ordered categories, unequal steps | Severity 1–5, satisfaction rating | Median, percentiles |
| **Interval** | Equal steps, no true zero | Temperature in °C | Mean, standard deviation |
| **Ratio** | Equal steps and a true zero | Length, weight, time, count | Mean, SD, ratios ("twice as long") |

Common mistake: averaging ordinal ratings ("average severity 2.7") as if the steps were equal.

## 3. Converting continuous to attribute loses information

Diameter (continuous) → "in spec / out of spec" (attribute) throws away everything about *how close* parts are to the limits. Record the measurement; derive pass/fail from it, never the reverse.

## Check yourself

Classify each (discrete/continuous; scale):

1. Number of customer returns per week
2. Paint color code (R, G, B)
3. Torque in N·m
4. Defect severity: minor / major / critical

<details><summary>Answers</summary>

1. Discrete, ratio (counts have a true zero). 2. Discrete, nominal. 3. Continuous, ratio. 4. Discrete, ordinal.
</details>
