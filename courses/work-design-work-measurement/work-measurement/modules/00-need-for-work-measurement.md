# Module 00 — The Need for Work Measurement: Overview

## Objectives

- Explain what work measurement is and its role in industrial engineering.
- Recognize why organizations need work standards.
- Describe the main measurement methods and when each fits.

## What is work measurement?

**Work measurement** determines the time a qualified worker should take to perform a defined task, using a defined method, at a defined level of performance, under defined conditions — plus allowances for personal needs, fatigue and unavoidable delay. The result is a **work standard** (standard time).

Every part of that definition matters: change the method, the worker's qualification, or the conditions, and the standard is no longer valid.

It is no longer just a stopwatch exercise. Work measurement is how an organization understands the relationship between **people and processes**: how much work a process contains, where time is lost, and what capacity really is.

## Why standards are needed

Without standards, an organization cannot reliably answer:

- How many people do we need next month? (staffing, capacity)
- What does this product cost to make? (costing, quoting)
- When will this order be done? (scheduling)
- Is the line performing well today? (performance measurement)
- Is the new method better? (process improvement)
- How do we balance work across stations? (line balancing, Lean)

## Methods at a glance

| Method | How | Best for |
|---|---|---|
| Time study (stopwatch / video) | time a qualified worker, rate pace, add allowances | repetitive, existing work |
| Work sampling | random instantaneous observations | long, irregular or group work; delays and allowances |
| Standard data | element times or formulas from past studies | families of similar jobs |
| Predetermined motion time systems (PMTS) | sum standard times for basic motions | designing new work before it exists; short cycles |
| Historical data / estimates | past records, expert judgment | quick, rough planning only |

## Running case

**Marlow Pump Works** (fictional) assembles small centrifugal pumps in a cell and runs a kitting area. Its industrial engineer must set the pump-assembly standard, check how kitters spend their time, build standard data for crate pack-out, report labor performance and plan staffing.

| File | Content |
|---|---|
| `data/time_study_continuous.csv`, `data/elements.csv` | 15-cycle continuous time study, 6 elements |
| `data/rating_practice.csv` | rating-training results for 4 analysts |
| `data/labor_report.csv` | 4 weeks of labor reporting for 8 operators |
| `data/work_sampling_kitting.csv`, `data/kitting_output.csv` | 612 random observations over 20 days, with output |
| `data/packout_studies.csv` | 18 past pack-out time studies |

All data is simulated with a fixed seed.

```bash
pip install -r requirements.txt
python tools/wmkit.py all
```

The [Introduction to Industrial Engineering](../../introduction-to-industrial-engineering/README.md) course gives a one-module overview of time study and work sampling; this course goes into depth.

## Check yourself

1. A standard was set before a new fixture was installed. Is it still valid?
2. Which method fits a maintenance technician's varied day?

<details><summary>Answers</summary>

1. No — the method changed, so the standard must be re-studied (or adjusted from element data) before use.
2. Work sampling (or standard data for recurring tasks); a stopwatch study of irregular work is impractical.

</details>
