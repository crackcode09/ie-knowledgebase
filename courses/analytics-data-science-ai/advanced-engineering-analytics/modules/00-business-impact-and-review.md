# Module 00 — Business Impact of Data Science and a Fast-Track Review

## Objectives

- Explain the strategic implications of data science for an operation.
- Review the foundations from the introductory course.
- Meet the running case, its data sources and its business questions.

## Why data science matters to operations

Data science combines statistics, computing and domain knowledge to turn data into decisions. In operations it pays off where it changes a decision that is made often or costs a lot:

| Business goal | Analytics question | Module |
|---|---|---|
| Improve quality | Which factors drive seal strength? | 05, 06, 08 |
| Predict and reduce equipment failures | Which line will break down in the next week? | 07, 09 |
| Improve machine utilization | Where is availability lost, and why? | 04 |
| Lower production costs | What drives cost per 1,000 good units? | 04 |
| Improve customer service | Which lines cause late deliveries? | 04, 10 |

**Strategic implications:** decisions move from opinion to evidence; data becomes a shared asset (with owners, definitions and quality rules); people need both domain and data skills; and models must be monitored, because processes change.

## Fast-track review (Introduction to Engineering Analytics)

- **Four types of analytics:** descriptive (what happened), diagnostic (why), predictive (what will happen), prescriptive (what to do).
- **Process:** business question → understand data → prepare → model → evaluate on unseen data → deploy and monitor.
- **Visualization:** one message per chart; position and length for numbers; color for highlighting.
- **Data models:** tables, keys, star schemas.
- **Techniques:** segmentation, classification (precision/recall/AUC), regression, PCA, forecasting, optimization.

See the [Introduction to Engineering Analytics](../../engineering-analytics/README.md) course for the full treatment.

## Running case: Corbin Packaging

**Corbin Packaging** (fictional) heat-seals food trays on four lines (L1–L4), two shifts a day, January–June 2026. Data comes from five systems — typical of real plants:

| Source | File | Grain (one row = …) |
|---|---|---|
| Production workbook (Excel), sheets `runs` and `lines` | `data/production_workbook.xlsx` | one production run; one line |
| Quality lab export | `data/quality_lab.csv` | one seal-strength test (3 per run) |
| Maintenance system | `data/maintenance_log.csv` | one maintenance event |
| Line sensors | `data/line_sensors_daily.csv` | one line-day |
| Order system | `data/customer_orders.csv` | one customer order |
| Designed experiment | `data/seal_doe.csv` | one experimental run |

The data contains realistic problems — duplicates, mixed units, missing values, inconsistent labels — that Modules 01–03 deal with. Minimum seal strength (customer requirement): **18 N**.

## Tools

Everything runs in free tools (Python: pandas, SciPy, statsmodels, scikit-learn, Plotly). The same work can be done in a BI tool such as Tableau or Power BI plus a spreadsheet; each module notes the BI-tool equivalent where it helps.

```bash
pip install -r requirements.txt
python tools/aeakit.py all
python tools/build_dashboard.py
```

## Check yourself

1. Name one decision at your workplace that is made often and could be improved with data.
2. Why does the grain of each source matter before combining them?

<details><summary>Answers</summary>

1. Examples: which machine to maintain next; how much stock to hold; which supplier lot to use; whether to release a batch.
2. Combining tables of different grain (runs vs tests vs events) without aggregating first duplicates rows and inflates totals — Module 02.

</details>
