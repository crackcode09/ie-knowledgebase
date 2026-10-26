# Module 03 — Preparing Data for Analysis

## Objectives

- Find and fix common data problems: duplicates, unit errors, inconsistent labels, missing values, outliers.
- Create derived features that match the business question.
- Document preparation so it is repeatable.

## A preparation checklist

| Check | Corbin finding | Action |
|---|---|---|
| Duplicate rows | 2 | drop exact duplicates; investigate why they occurred |
| Units | 3 seal temperatures logged in °F (> 300) | convert (°F − 32) × 5/9 after confirming with the operator log |
| Categorical labels | `l3` instead of `L3` | standardize (strip, upper-case) |
| Missing values | 2 missing pressures; 4 missing lab tests | keep rows; exclude from models that need the field; lab means use available tests |
| Range checks | after fixes, seal temperature 150.5–177.0 °C | matches the expected 150–180 |
| Types | dates as text in some exports | parse to date type |
| Outliers | none implausible after unit fix | keep real extremes; remove only proven errors |

```bash
python tools/aeakit.py prepare
```

## Missing data

Why data is missing matters more than how much:

- **Missing at random** (a sensor glitch) — dropping rows or simple imputation is usually fine.
- **Missing for a reason** (lab skipped tests on runs that were already scrapped) — dropping biases results.

Report how many rows each analysis used. Never fill missing values silently.

## Outliers

Investigate before acting. An extreme value may be an error (unit slip — fix), a real special cause (a jammed jaw — keep, and learn from it) or the natural tail of a skewed process (downtime — use methods that handle skew, Module 07).

## Derived features

Create measures that answer the business questions:

| Feature | Definition |
|---|---|
| `scrap_rate` | units_scrap / (units_good + units_scrap) |
| `availability` | run_hours / planned_hours |
| `cost_per_1000_good` | 1,000 × run_hours × cost_per_run_hour / units_good |
| `seal_min` | lowest of the run's lab tests (the customer cares about the weakest seal) |
| sensor "trend" features | today's value minus the line's average of the previous 14 days (Module 09) |

## In a spreadsheet or BI tool

Remove duplicates, use find/replace or a mapping table for labels, add calculated columns for derived features, filter on range checks. In a BI tool's data-prep step, record each step so it reruns on refresh.

## Check yourself

1. Why convert the °F values rather than delete those runs?
2. A run has 2 of 3 lab tests. Use it?
3. Downtime has a few runs with 300+ minutes. Remove them as outliers?

<details><summary>Answers</summary>

1. The runs are real and their other fields are valid; the error is a known, correctable unit slip. Deleting loses information and can bias results.
2. Yes, with `n_tests` = 2 recorded; the mean is slightly less precise. Check whether missing tests cluster on particular lines or dates.
3. No — long breakdowns are real and important. Use medians and nonparametric methods (Module 07) instead.

</details>
