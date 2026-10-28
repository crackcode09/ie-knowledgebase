# Staffing Models & Human Capital Management

Learn to build workload-based staffing models and use them in human capital planning: budgets, hiring, training and performance measurement for mission-critical occupations.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Prerequisites:** none. Basic time study and statistics help (see [Work Measurement](../work-measurement/README.md)).  
**Tools:** Excel (workbook included) or Python.

## What you will be able to do

- Explain where staffing models fit in a human capital management framework.
- Identify and assess the seven types of data a staffing model needs.
- Explain where and how work measurement feeds staffing models.
- Use the terminology of work measurement and staffing models correctly.
- Plan and carry out the staffing model development phases, from scoping to maintenance.

## Running case

**Tri-County Building Safety** (fictional) is a public agency with 21 inspectors, 6 plan reviewers, 4 permit technicians and 4 supervisors. Builders complain about summer inspection delays, and the director needs a defensible staffing plan for 2026–2028. The course data includes:

- 60 months of workload history with staffing and service levels
- unit times from four measurement methods
- 1,200 work-sampling observations of inspectors
- leave records and a workforce roster
- separation history
- permit-counter arrivals by hour
- a 14-agency peer benchmark

All data is simulated with a fixed seed.

## Modules

| # | Module | Outline topic |
|---|---|---|
| 00 | [Staffing models in human capital management](modules/00-staffing-models-in-human-capital-management.md) | Where staffing models fit in an HCM framework |
| 01 | [Terminology](modules/01-terminology.md) | Terminology of work measurement and staffing models |
| 02 | [Seven types of required data](modules/02-seven-types-of-required-data.md) | Seven types of required data |
| 03 | [Work measurement and staffing models](modules/03-work-measurement-and-staffing-models.md) | Where and how work measurement relates to staffing models |
| 04 | [Available time and relief factors](modules/04-available-time-and-relief-factors.md) | Availability, relief factors (terminology and data in use) |
| 05 | [Types of staffing models](modules/05-staffing-model-types.md) | Workload-driven, coverage, queueing, ratio and benchmark models |
| 06 | [Forecasting workload](modules/06-forecasting-workload.md) | Demand forecasts and scenarios |
| 07 | [Workforce supply and gap analysis](modules/07-workforce-supply-and-gap-analysis.md) | Supply, attrition, hiring plans |
| 08 | [Staffing model development phases](modules/08-staffing-model-development-phases.md) | Development phases; validation, sensitivity, governance |
| 09 | [Using staffing models](modules/09-using-staffing-models.md) | Budget, hiring, performance measurement, executive communication |
| 10 | [Capstone](modules/10-capstone.md) | Plan reviewers and permit counter; skill check |

**Suggested schedule:**

- Day 1: modules 00–05
- Day 2: modules 06–10

## Related courses

- [Work Measurement](../work-measurement/README.md): time study, work sampling, allowances, staffing and takt
- [Standard Data Systems](../standard-data-systems/README.md): building unit times from past studies
- [Process Modeling and Simulation](../../technical-skills/process-modeling-and-simulation/README.md): simulation when queueing formulas are not enough
- [Technical Communications](../../technical-skills/technical-communications/README.md): presenting results to executives

## Getting started

```bash
pip install -r requirements.txt
python tools/stmkit.py all           # every worked example
python tools/stmkit.py data          # regenerate data/*.csv
python tools/make_figures.py         # regenerate figures/
python tools/make_workbook.py        # regenerate templates/staffing-model-workbook.xlsx
```

## Folder map

```
modules/     lessons
tools/       stmkit.py (all calculations), make_figures.py, make_workbook.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   Excel model, project charter, data collection plan, executive summary
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
