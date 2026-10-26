# Module 00 — Introduction: Cost of Quality as a Management Tool

## Objectives

- Define the cost of quality (CoQ) and explain why it matters.
- Distinguish using CoQ to **select and manage improvement** from using it only as an accounting report.
- Meet the running case and the tracker tool.

## What is the cost of quality?

The **cost of quality** is the total cost of ensuring that products and services conform to requirements **plus** the cost of failing to conform. It translates quality problems into the language of management — money — so they can be compared with other uses of resources.

Two halves:

| Cost of good quality (conformance) | Cost of poor quality (nonconformance) |
|---|---|
| Prevention: stopping defects from happening | Internal failure: defects found before the customer |
| Appraisal (detection): checking whether requirements are met | External failure: defects found by the customer |

Commonly quoted ranges put total CoQ at several percent to over 20 % of sales in many organizations — with most of it in failure costs. Treat such figures as order-of-magnitude, not benchmarks; your own number is what counts.

## Accounting system or improvement tool?

| CoQ as accounting | CoQ as an improvement tool |
|---|---|
| a quarterly report of totals | a way to **find** where money is lost |
| precision of every dollar matters | **direction and relative size** matter |
| owned by finance | owned by operations + quality, validated by finance |
| ends with the report | ends with **projects** that reduce failure cost |

This course follows the second approach: build a CoQ picture good enough to **choose** the right improvement projects, track their results, and report progress in business terms.

## The typical journey

1. Define categories and elements (Modules 01–06).
2. Assess current costs from accounts, estimates and studies (Module 08).
3. Add hidden costs, reported separately (Module 07).
4. Analyze cost drivers (Module 09).
5. Select and manage projects (Module 10).
6. Report and track (Module 11).

## Running case

**Ellison Hydraulics** (fictional) builds hydraulic cylinders: about $40.3M sales and 24,400 cylinders a year. In month 7 it launches a CoQ program — more prevention (planning, training, supplier development, FMEA), with appraisal and failure costs expected to fall.

| File | Content |
|---|---|
| `data/coq_ledger.csv` | 12 months × 20 cost elements, categorized |
| `data/monthly_operations.csv` | sales, units, direct labor hours |
| `data/failure_events.csv` | 700 failure events (months 1–6) with driver and cost; reconciles to the ledger |
| `data/hidden_costs.csv` | estimated hidden costs and their basis |

All data is simulated with a fixed seed.

## The tracker (the course "software")

`templates/coq-tracker.xlsx` is an Excel workbook with live formulas: a **Ledger** sheet (one row per cost element, one column per month) and a **Summary** sheet (category totals, CoQ % of sales, failure and prevention shares). It is pre-filled with the case data; clear the month columns to use it for your own organization.

`tools/coqkit.py` does the same analysis in Python and can regenerate the tracker and a summary report:

```bash
pip install -r requirements.txt
python tools/coqkit.py all        # every worked example
python tools/coqkit.py tracker    # rebuild templates/coq-tracker.xlsx
python tools/coqkit.py report     # write solutions/coq-summary-report.md
```

## Check yourself

1. Why might a plant manager respond more to "$1.2M a year in scrap and rework" than to "first-pass yield is 92 %"?
2. Your CoQ total is off by ±10 %. Is that a problem for selecting projects?

<details><summary>Answers</summary>

1. Money is the common language of management; it can be compared directly with budgets, investments and profit.
2. Usually not — project selection depends on relative size and direction (which drivers cost most). Reported figures should still be reconciled with finance before they are used for official results.

</details>
