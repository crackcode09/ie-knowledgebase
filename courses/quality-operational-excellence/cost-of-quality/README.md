# Cost of Quality

Learn to use cost of quality (CoQ) to choose and manage improvement projects, not just to account for quality costs.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Prerequisites:** none. A spreadsheet program is needed for the tracker; Python is optional.

## What you will be able to do

- Identify the direct costs of quality.
- Identify the hidden costs of quality.
- Define the main categories of quality costs.
- Prepare a cost of quality summary report.
- Use quality cost data to guide process improvement.

## Running case

**Ellison Hydraulics** (fictional) builds about 24,400 hydraulic cylinders a year on $40.3M in sales. It launches a CoQ program in month 7. The course data includes:

- a 12-month ledger of 20 cost elements;
- monthly operations data;
- 700 failure events that reconcile to the ledger;
- hidden-cost estimates.

All data is simulated with a fixed seed.

## The tracker

`templates/coq-tracker.xlsx` is an Excel workbook with live formulas. It has three sheets: a ledger by element and month, a summary by category with CoQ % of sales and mix ratios, and instructions. It comes pre-filled with the case data; clear the month columns to track your own costs.

I checked the tracker by recalculating it in LibreOffice. Its totals match the Python toolkit.

## Modules

| # | Module | Outline topic |
|---|---|---|
| 00 | [Introduction](modules/00-introduction.md) | CoQ as a management tool; the course journey; the tracker |
| 01 | [Cost models](modules/01-cost-models.md) | Prevention–appraisal–failure model, process cost model, activity-based CoQ, classic vs modern optimum |
| 02 | [Cost categories](modules/02-cost-categories.md) | Category rules, element list, gray areas, first summary |
| 03 | [Prevention](modules/03-prevention-costs.md) | Prevention activities, leverage, judging effectiveness |
| 04 | [Detection](modules/04-detection-appraisal-costs.md) | Appraisal activities, limits of inspection, reducing appraisal safely |
| 05 | [Internal failure](modules/05-internal-failure-costs.md) | Scrap, rework and their valuation; failure-element Pareto |
| 06 | [External failure](modules/06-external-failure-costs.md) | Warranty, returns, field service; cost per escaped defect |
| 07 | [Hidden costs](modules/07-hidden-costs.md) | The iceberg, estimation methods, quadratic quality loss |
| 08 | [Cost assessments](modules/08-cost-assessments.md) | Data sources, work sampling, reconciliation, ongoing tracking |
| 09 | [Cost drivers](modules/09-cost-drivers.md) | Linking cost to failure types; cost vs count Pareto |
| 10 | [Project management](modules/10-project-management.md) | Project portfolio, payback and ROI, hard vs soft savings, verification |
| 11 | [Reports](modules/11-reports.md) | Measurement bases, before/after, summary report, presenting to management |
| 12 | [Capstone and skill check](modules/12-capstone.md) | Build a CoQ picture; 10-question check |

**Suggested schedule:**

- **Day 1:** modules 00–07 (models, categories, hidden costs)
- **Day 2:** modules 08–12 (assessment, drivers, projects, reports)

## Related courses

- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md): cost of poor quality in a Lean program
- [Financial Management for Engineers](../../technical-skills/financial-management-for-engineers/README.md): payback, ROI and NPV
- [Root Cause Analysis & Problem Solving](../../lean-six-sigma/root-cause-analysis/README.md): acting on the top cost drivers
- [Quality Engineering Essentials](../quality-engineering-essentials/README.md): running the improvement projects

## Getting started

```bash
pip install -r requirements.txt
python tools/coqkit.py all          # every worked example
python tools/coqkit.py tracker      # rebuild templates/coq-tracker.xlsx
python tools/coqkit.py report       # write solutions/coq-summary-report.md
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons
tools/       coqkit.py (data, analysis, tracker builder, report generator), make_figures.py
data/        ledger, operations, failure events, hidden-cost estimates (CSV)
figures/     charts used in the lessons
solutions/   key results, facilitator notes, generated summary report
reference/   formulas, glossary, further reading
templates/   coq-tracker.xlsx, element checklist, report template
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
