# Module 02 — Merging Datasets (Excel and Other Sources)

## Objectives

- Combine data from an Excel workbook and other sources with the right join.
- Aggregate to a common grain before joining.
- Detect and prevent join errors.

## Join types

| Join | Keeps | Use when |
|---|---|---|
| Inner | rows matched in both | you only want complete records |
| Left | all rows from the left table, matches from the right | the left table defines the population (e.g. all runs) |
| Full outer | all rows from both | reconciling two systems |
| Union / append | stacks rows with the same columns | combining monthly files or sheets |

## The fan-out trap

Joining runs (1,002 rows) directly to lab tests (3,000 rows, 3 per run) gives **3,006 rows** — every run repeated three times (plus the duplicates). Any sum over that table (units, hours, cost) is **tripled**. This is the most common merge error in practice.

**Fix: aggregate the many-side to the target grain first**, then join:

```python
runs = pd.read_excel("data/production_workbook.xlsx", sheet_name="runs")
lines = pd.read_excel("data/production_workbook.xlsx", sheet_name="lines")
lab = pd.read_csv("data/quality_lab.csv")

lab_run = lab.groupby("run_id").seal_strength_n.agg(seal_mean="mean", seal_min="min", n_tests="count").reset_index()
table = (clean_runs(runs)
         .merge(lab_run, on="run_id", how="left", validate="one_to_one")
         .merge(lines, on="line", how="left", validate="many_to_one"))
```

`validate=` makes pandas **raise an error** if a key is not unique as expected — a cheap guard against silent fan-out.

## Corbin's merge

| Step | Rows |
|---|---|
| Runs (raw Excel sheet) | 1,002 |
| Lab tests | 3,000 |
| Naive runs × tests join | 3,006 (wrong grain) |
| Runs after de-duplication | 1,000 |
| **Analysis table (one row per run)** | **1,000** |
| Runs without a lab result | 0 |

The analysis table adds `seal_mean`, `seal_min`, the line's `cost_per_run_hour`, and derived measures: scrap rate, availability (run hours / planned hours) and cost per 1,000 good units.

## Joining on dates and lines

Maintenance events and sensor readings join on **line + date**. Decide what "match" means: a breakdown on 3 March affects runs on 3 March; for prediction we look **forward** ("breakdown within the next 7 days"), which must use only information available **before** the event (Module 09).

## In a BI tool

BI tools offer joins (physical merges at a fixed grain), relationships (tables kept separate and combined at the grain of each visualization) and blending (combining aggregated results from separate sources). The same principle applies: know the grain of each table and how they relate, and check row counts and totals after combining.

## Run it

```bash
python tools/aeakit.py merge
```

## Check yourself

1. You join orders (one per order) to customers (one per customer). Which `validate` setting?
2. Total units in a merged table is 3× the production report. What happened?
3. Why use a left join from runs to lab results?

<details><summary>Answers</summary>

1. `many_to_one` — many orders per customer, each customer once.
2. Fan-out: a one-to-many join (e.g. to lab tests or maintenance events) duplicated each run.
3. The runs define the population; a run without a lab result should stay in the table (with missing seal values) rather than disappear silently.

</details>
