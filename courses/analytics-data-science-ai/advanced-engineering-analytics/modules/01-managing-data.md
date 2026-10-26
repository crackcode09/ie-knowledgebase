# Module 01 — Managing Data

## Objectives

- Describe the sources, structure and ownership of operational data.
- Define grain, keys and data dictionaries.
- Set up practical data management for an analytics project.

## Inventory your data

For each source record: system, owner, refresh frequency, grain, key fields, known issues.

| Source | Owner | Refresh | Grain | Key(s) | Known issues |
|---|---|---|---|---|---|
| Production workbook | production supervisors | per shift | run | `run_id`; `line` | manual entry: typos, duplicates, unit slips |
| Quality lab | quality lab | per test | test | `run_id` + `sample` | missing results |
| Maintenance log | maintenance planner | per event | event | `line` + `date` | free-text failure modes |
| Line sensors | controls engineer | daily | line-day | `line` + `date` | gaps when PLC offline |
| Orders | customer service | per order | order | `order_id` | promised date changes |

## Grain and keys

- **Grain** — what one row represents. Mixing grains is the most common analysis error.
- **Primary key** — uniquely identifies a row (`run_id` for runs; `run_id` + `sample` for lab tests).
- **Foreign key** — links to another table (`quality_lab.run_id` → `runs.run_id`; `runs.line` → `lines.line`).
- **Check uniqueness** before trusting a key: Corbin's run sheet has **2 duplicated rows** (1,002 rows, 1,000 unique runs).

## Data dictionary

Document each field: name, meaning, unit, type, allowed range, source. Example: `seal_temp_c` — sealing-jaw set temperature, °C, numeric, expected 150–180. That entry alone would have caught **3 values logged in °F** (> 300) in Corbin's data. Template: `templates/data-dictionary.csv`.

## Practical data management

- **Keep raw data unchanged**; do cleaning in code (or in a documented BI data-prep step) so it is repeatable.
- **Version** analysis tables and code.
- **One source of truth** for definitions (availability, scrap rate, on-time) — write them down.
- **Access and privacy** — customer and employee data need controls.
- **Automate refresh** where the analysis will be repeated.

## In a BI tool

Connect each source, inspect the field types and row counts, rename fields to dictionary names, and document calculated fields. Most BI tools let you save the data source with its definitions so all reports share them.

## Check yourself

1. What is the grain of `quality_lab.csv`, and what is its primary key?
2. Why keep raw files unchanged?

<details><summary>Answers</summary>

1. One seal-strength test; key = `run_id` + `sample`.
2. So every cleaning step is visible, repeatable and reversible, and the analysis can be rerun when new data arrives.

</details>
