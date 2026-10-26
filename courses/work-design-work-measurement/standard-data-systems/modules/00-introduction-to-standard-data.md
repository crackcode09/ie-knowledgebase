# Module 00 — Introduction to Standard Data

## Objectives

- Define a standard data system.
- Recognize operations where standard data beats a time study for every job.
- Describe the course case and the path from past studies to a job standard.

## What standard data is

A **work standard** is the time a qualified worker needs to do a defined task at normal pace using the prescribed method, plus allowances. The usual way to set one is a **time study**: time the job, rate the pace, add allowances. (The [Work Measurement](../../work-measurement/README.md) course covers time study in detail.)

A **standard data system** is a catalogue of element times and formulas built from many past studies. To set a standard for a new job, you describe the job by its **variables** (bends, length, weight, number of holes, tool changes and so on) and add up the matching element times. You don't need a stopwatch, and the job doesn't need to exist yet.

```
past time studies ──► element times & formulas ──► data sheet / calculator ──► standard for any new job
   (many jobs)          (regression, tables)        (codes, frequencies)        (in seconds, before production)
```

## When standard data pays off

Standard data is worth building when **the same kinds of elements recur in many different jobs**:

| Situation | Why time study struggles | Why standard data helps |
|---|---|---|
| High part-number count (job shops, made-to-order) | Too many jobs to study | One model covers the whole family |
| Small lots | The job is finished before a study is done | Standards are set from the drawing |
| Frequent changeovers | Setup varies with tooling and program | Setup formula driven by tool count, program status |
| Quoting and planning before production | No job to time yet | Standard comes from the part's features |
| Many analysts | Analysts rate pace differently | One formula gives the same answer every time |

It is a poor fit when work is unique and never repeats, when the method is unstable, or when a few long-running jobs account for most of the hours. In those cases, time-study those few jobs directly.

## Running case: Harlan Fabrication

**Harlan Fabrication** (fictional) is a sheet-metal job shop:

- about 3,000 active part numbers, with 600 new ones a year
- lot sizes from 5 to 200 pieces
- shear, turret punch, **press brake**, weld and assembly areas

The press brake is the bottleneck, and quoting and scheduling it from guesses has failed. The IE team will build standard data for **press-brake setup and run**, using:

| File | Content |
|---|---|
| `data/brake_run_studies.csv` | 40 past run studies: bends, flips, length, width, thickness, weight, normal min/piece |
| `data/brake_setup_studies.csv` | 24 setup studies: tool segments changed, new program (yes/no), normal min |
| `data/shear_handling_studies.csv` | 26 studies of the shear "load and square blank" element vs blank weight |
| `data/analyst_consistency.csv` | 6 jobs, each time-studied by 3 analysts |
| `data/validation_studies.csv` | 12 new jobs studied after the model was built (hold-out) |
| `data/week_jobs.csv` | one week of press-brake jobs with clocked hours |
| `data/motion_table_illustrative.csv` | a course-made motion table for Module 01 |

All data is simulated with a fixed seed (1946). Harlan's allowance convention is **12 % PF&D on normal time**.

## The course path

| Module | Question it answers |
|---|---|
| 01–02 | At what level of detail do we build the data: motions or whole operations? |
| 03–04 | Is it worth it, and what can go wrong? |
| 05 | How is a data system organised? |
| 06–08 | How do we turn past studies into a formula we can trust? |
| 09 | How do we use and maintain it? |
| 10 | Capstone |

## Tools

- **Excel** with the Analysis ToolPak, or the built-in `LINEST` function. The workbook `templates/standard-data-workbook.xlsx` contains the full model and a job calculator.
- **Python** (optional): `tools/sdskit.py` reproduces every number in the modules.

## Run it

```bash
python tools/sdskit.py data    # regenerate the datasets
python tools/sdskit.py all     # every worked example
```

## Check yourself

1. In your own words, what is the difference between a time-study standard and a standard-data standard?
2. Which of these suit standard data? (a) A paint line running one product 24/7. (b) A machine shop quoting 40 new parts a week. (c) A maintenance crew doing one-off repairs. (d) A kitting area picking 2–60 items per kit.
3. Why does Harlan start with the press brake?

<details><summary>Answers</summary>

1. A time study measures one job directly. Standard data predicts the time for any job in a family from its features, using element times built from many earlier studies.
2. (b) and (d). Both have many different jobs made of the same elements. (a) is one job, so study it directly. (c) has little repetition, although a coarse "slotting" of standard repair jobs is sometimes used.
3. It is the bottleneck, so errors in its standards hurt quoting and scheduling the most. It also has many part numbers with the same elements (load, bend, flip, unload, setup).

</details>
