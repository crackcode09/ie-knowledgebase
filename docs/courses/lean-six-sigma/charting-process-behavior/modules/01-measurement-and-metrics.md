# Module 1 — Measurement & Metrics

**Time:** 45 min

## Learning objectives

1. Classify data as continuous (variables) or discrete (attributes) and know which charts each one feeds.
2. Write an operational definition for a metric.
3. Recognize when the measurement system, not the process, is the source of variation.

## 1. Data types decide the chart

| Type | Examples | Typical charts |
|---|---|---|
| **Continuous / variables** — measured on a scale | Diameter, weight, cycle time, temperature | XmR, X̄–R, X̄–S |
| **Count of defectives** — each unit is good/bad | Rejected parts per lot | p, np |
| **Count of defects** — many defects possible per unit | Scratches per panel, errors per invoice | c, u |

Continuous data carry far more information per observation. A pass/fail gauge tells you a part is bad; a micrometer tells you it is 0.012 mm from nominal and drifting. Prefer continuous measures whenever you can get them.

## 2. Operational definitions

Deming's point: a metric does not exist until you define *how* to get the number. An operational definition states:

- **What** is measured (characteristic, units, resolution)
- **How** (instrument, method, fixture, location on the part)
- **When/where** (sampling point, frequency)
- **Decision rule** for attributes (what counts as a defect, with examples or limit samples)

> **Weak:** "Measure shaft diameter."
> **Operational:** "Measure diameter at 10 mm from the shoulder with the 0–25 mm digital micrometer (0.001 mm resolution), two readings 90° apart, record the average, first part off each hour."

Two people following the second definition should get the same number on the same part.

## 3. Is the measurement system good enough?

Every recorded value = true value + measurement error. If measurement error is large relative to the process variation, your chart is mostly charting the gauge.

Checks to know (full method in any Measurement Systems Analysis reference):

| Property | Question | Quick check |
|---|---|---|
| **Resolution** | Can the gauge see the variation? | At least ~10 distinct values across the process spread; if the mR chart shows mostly zeros and one or two values, resolution is too coarse |
| **Bias** | Does it read high/low on average? | Measure a reference standard repeatedly |
| **Repeatability** | Same person, same part, same gauge — how much scatter? | Gauge R&R study |
| **Reproducibility** | Different people — do they agree? | Gauge R&R study |
| **Stability** | Does the gauge drift over time? | Chart repeated measurements of a master part (an XmR chart works) |

A common rule of thumb (from automotive MSA practice) is that gauge R&R below 10% of process variation is acceptable, 10–30% may be acceptable depending on the application, and above 30% is not. Treat these as conventions, not laws.

## 4. Good metrics for charting

- **Time-ordered.** Record the date/time or sequence number. A chart without time order is just a histogram.
- **Context-rich.** Record machine, shift, operator, material lot, cavity — you will need these for stratification (Module 11).
- **Raw, not summarized.** Store individual readings; you can always compute averages later, never the reverse.
- **Not ratios of ratios.** Monthly "% on-time" hides the counts; keep numerator and denominator.

## Exercise 1.1

Write an operational definition for one metric you deal with at work (or: "time to answer a customer email"). Include what, how, when, and the decision rule.

## Check yourself

1. "Number of invoices with at least one error" is (a) defects, (b) defectives, (c) continuous.
2. Your mR chart is almost all zeros with occasional values of 0.01. What is the likely problem?
3. Why record machine and shift with each reading?

<details><summary>Answers</summary>

1. (b) defectives — each invoice is classified good/bad. "Number of errors" would be defects.
2. Inadequate measurement resolution (data rounded too coarsely).
3. So you can stratify later and find which factor drives variation.
</details>
