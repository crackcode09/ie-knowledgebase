# Module 02 — Measurement and Basic Statistics

## Objectives

- Use basic statistical terms; distinguish descriptive from inferential statistics.
- Choose good measurements: data types, discrete vs continuous.
- Summarize data graphically (Pareto, histogram) and numerically (center, spread).
- Identify a distribution and clean data before analysis.

## Terms

- **Population** vs **sample**; **parameter** (μ, σ) vs **statistic** (x̄, s).
- **Descriptive statistics** summarize the data you have; **inferential statistics** draw conclusions about the population from a sample (confidence intervals, hypothesis tests).

## Measurement and data types

| Type | Example at Bayline | Information per measurement |
|---|---|---|
| Continuous (variable) | OD in mm; turnaround hours | high — shows how close to the limit |
| Discrete count | defects per insert | medium |
| Attribute (pass/fail) | thread go/no-go | low — needs large samples |
| Ordinal | burr severity 1–3 | low–medium |

**Select the best measurement:** prefer continuous data when you can get it; make sure it relates to what the customer cares about; define it operationally (how, where, with what gauge, at what temperature).

## Graphical summaries

**Pareto chart — what goes wrong most often?** (480 inserts sampled over 20 days, `data/production_sample.csv`)

| Defect | Count | % | Cumulative % |
|---|---|---|---|
| Oversize OD | 20 | 50.0 | 50.0 |
| Thread damage | 11 | 27.5 | 77.5 |
| Burr | 7 | 17.5 | 95.0 |
| Knurl incomplete | 2 | 5.0 | 100.0 |

40 defectives = **8.33 %**.

![Pareto](../figures/02_defect_pareto.png)

**Histogram — shape, center and spread against the spec:**

![Histogram](../figures/02_od_histogram.png)

The distribution sits **above target**, and its upper tail crosses the USL. Stacking by machine shows M2's parts are the larger ones — a first clue.

## Center and spread

| Statistic | OD, all 480 inserts |
|---|---|
| Mean | 6.36273 mm (target 6.350) |
| Median | 6.3623 mm |
| Standard deviation | 0.00709 mm |
| Range | 0.0463 mm (6.3379–6.3842) |
| Q1 / Q3 | 6.3580 / 6.3674 mm |
| 95 % CI for the mean | 6.36210 to 6.36337 mm |

The confidence interval is inferential: we're 95 % confident the process mean is between those values — clearly above the 6.350 target.

## The normal distribution and distribution identification

Many measurements are approximately normal (symmetric, bell-shaped): about 68 % within ±1σ, 95 % within ±2σ, 99.7 % within ±3σ. But not all.

**Quote turnaround time** (service process, 120 quotes, `data/quote_turnaround.csv`): mean 20.8 h, median 17.8 h, skewness 1.54.

| Distribution | AIC (lower = better) | KS test p |
|---|---|---|
| Normal | 935.9 | 0.048 |
| **Lognormal** | **887.3** | 0.984 |
| Gamma | 893.1 | 0.684 |
| Weibull | 905.9 | 0.387 |

![Distribution fit](../figures/02_distribution_fit.png)

Why it matters: the 95th percentile assuming normality is 40.2 h; the lognormal fit gives 43.5 h; the data's own 95th percentile is 43.4 h. Using the wrong distribution understates how long the slow quotes take — and gives wrong capability and control limits (Module 04).

## Data cleansing

Real exports contain errors. `data/dirty_export.csv` (41 rows) has:

| Issue | Count | Fix |
|---|---|---|
| Exact duplicate row | 1 | remove |
| Missing OD | 1 | find source record or exclude |
| Zero used as a placeholder | 1 | convert to missing |
| Decimal slip (63.52 instead of 6.352) | 1 | correct only after checking the source record |
| Inconsistent labels ("m2 ", "b") | 2 | standardize to M2, B |

After cleansing: 40 rows, 38 usable OD values. **Document every change**, never silently delete outliers, and fix the data-entry process that caused the errors.

## Run it

```bash
python tools/qekit.py describe
python tools/qekit.py pareto
python tools/qekit.py distribution
python tools/qekit.py cleanse
```

## Check yourself

1. Why is "% defective" a weaker measure than OD for this project?
2. Mean 20.8 h and median 17.8 h. What does that tell you about the shape?
3. An analyst deletes all OD values outside 6.33–6.38 "to remove outliers." What's wrong?

<details><summary>Answers</summary>

1. It's attribute data: it only flags parts already out of spec, needs large samples, and says nothing about how close good parts are to the limit. OD shows drift before defects occur.
2. Right-skewed (a long tail of slow quotes pulls the mean above the median).
3. Out-of-spec parts are exactly what the project is about; deleting them hides the problem. Remove only values proven to be errors, and document it.

</details>
