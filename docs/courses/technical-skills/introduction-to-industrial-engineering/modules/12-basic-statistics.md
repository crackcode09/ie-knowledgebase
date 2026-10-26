# Module 12 — Basic Statistics for Industrial Engineers

**Time:** 75 min

## Learning objectives

1. Summarize data with measures of center and spread.
2. Use the normal distribution and confidence intervals in IE work.
3. Recognize when to use run charts and control charts.

## 1. Describing data

| Measure | Formula / meaning | Use in IE |
|---|---|---|
| Mean | Σx / n | Average element time |
| Median | Middle value | Typical time when data are skewed (e.g., delays) |
| Range | max − min | Quick check of spread |
| Standard deviation s | √[Σ(x − x̄)² / (n − 1)] | Variation of cycle times; sample-size formula |
| Coefficient of variation | s / x̄ | Comparing variability of different elements |

**Example — "Inspect & bag" element (10 cycles):** mean 14.32 s, s = 0.41 s, CV = 2.9%. "Pick 8 parts" (9 cycles after removing the irregular reading): mean 22.02 s, s = 0.80 s, CV = 3.6%.

**Always plot first:** a histogram or dot plot shows outliers (like the 35.0 s dropped-part cycle) and skew that averages hide.

## 2. The normal distribution and confidence intervals

Many measured times are roughly normal: about 68% of values lie within ±1 s of the mean, 95% within ±2 s, 99.7% within ±3 s. Delays and repair times are usually right-skewed — use the median and percentiles.

**Confidence interval for a mean:** x̄ ± t × s/√n. For "Inspect & bag": 14.32 ± 2.262 × 0.41/√10 = **14.32 ± 0.29 s** (95%). The time-study sample-size formula (Module 4) is this idea rearranged.

**Confidence interval for a proportion:** p̂ ± 1.96 √[p̂(1 − p̂)/n] — the work-sampling margin (Module 5).

## 3. Variation over time

A standard time is a single number, but the process varies. Plot data in time order:

- **Run chart:** values in time order with a median line — shows trends and shifts.
- **Control (process behavior) chart:** adds limits computed from the data to separate routine variation from signals (e.g., kits per hour by day).

Use them to check that a new method's gains are real and sustained, and before setting standards (a process that's drifting gives an unreliable standard).

## 4. Go deeper

*Measurement & Basic Statistics*, *Charting Process Behavior* and *Fundamentals of Hypothesis Testing* in this repository.

## Check yourself

Repair times for a sealer: 4, 5, 5, 6, 7, 9, 45 minutes. Mean or median for "typical repair"?

<details><summary>Answer</summary>

Median (6 min). The mean (11.6 min) is pulled up by one 45-minute repair; use the mean for total downtime planning.
</details>
