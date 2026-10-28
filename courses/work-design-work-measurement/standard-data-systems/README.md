# Standard Data Systems

Learn to build and use standard data for work standards in operations with many part numbers, small lots or frequent changeovers. It covers when standard data pays off, how to structure a data system, and how to turn past time studies into regression models you can trust and maintain.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Prerequisites:** time study basics (see [Work Measurement](../work-measurement/README.md)). Basic statistics helps for Modules 06–08.  
**Tools:** Excel (the Analysis ToolPak or the built-in `LINEST`), or Python. Every number in the course can be reproduced in either.

## What you will be able to do

- Define standard data systems.
- Weigh their advantages and disadvantages.
- Apply analytical tools (correlation, regression, transformations, cross-validation) to develop standard data models.
- Build a standard data model and the data sheet that goes with it.
- Evaluate models: residuals, influence, intervals, extrapolation and hold-out validation.

## Running case

**Harlan Fabrication** (fictional) is a sheet-metal job shop with about 3,000 active part numbers and lots of 5–200 pieces. The IE team builds standard data for the press brake (its bottleneck) and, in the capstone, for the turret punch. The course data includes:

- 40 press-brake run studies (with one keying error to find)
- 24 setup studies
- 26 shear handling studies with a curved relationship
- 6 jobs studied by 3 analysts
- 12 hold-out studies
- one week of jobs with clocked hours
- 36 turret-punch studies for the capstone

All data is simulated with a fixed seed.

## Modules

| # | Module | Outline topic |
|---|---|---|
| 00 | [Introduction to standard data](modules/00-introduction-to-standard-data.md) | Introduction to standard data |
| 01 | [Microscopic standard data](modules/01-microscopic-standard-data.md) | Microscopic: motion-level data, PMTS, motion builds |
| 02 | [Macroscopic standard data](modules/02-macroscopic-standard-data.md) | Macroscopic: element and operation formulas, driving variables |
| 03 | [Advantages](modules/03-advantages.md) | Advantages: speed, consistency, integration, economics |
| 04 | [Disadvantages and limits](modules/04-disadvantages.md) | Disadvantages: cost, range limits, method drift, per-job accuracy |
| 05 | [Structure](modules/05-structure.md) | Structure: element hierarchy, constants, variables, frequencies, data sheet |
| 06 | [Regression and correlation](modules/06-regression-and-correlation.md) | Regression and correlation within standard data; Excel `LINEST` and ToolPak |
| 07 | [Developing models](modules/07-developing-models.md) | Developing models: multiple regression, dummies, transformations, multicollinearity |
| 08 | [Evaluating models](modules/08-evaluating-models.md) | Evaluating models: residuals, outliers, intervals, extrapolation, validation |
| 09 | [Applying standard data](modules/09-applying-standard-data.md) | Applying standard data: quoting, capacity, performance, maintenance |
| 10 | [Capstone](modules/10-capstone.md) | Build a model end to end; skill check |

**Suggested schedule:**

- Day 1: modules 00–06
- Day 2: modules 07–10

## Related courses

- [Work Measurement](../work-measurement/README.md): time study, rating, allowances, and a one-module overview of standard data
- [Applied Statistics](../../technical-skills/applied-statistics/README.md): correlation and linear and multiple regression in more depth
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md): setup reduction (SMED) and standard work

## Getting started

```bash
pip install -r requirements.txt
python tools/sdskit.py all          # every worked example
python tools/sdskit.py data         # regenerate data/*.csv
python tools/make_figures.py        # regenerate figures/
python tools/make_workbook.py       # regenerate templates/standard-data-workbook.xlsx
```

Excel only: open `templates/standard-data-workbook.xlsx`. The model sheets use `LINEST` and recalculate live. The "ToolPak steps" sheet shows how to get the same output with the Analysis ToolPak.

## Folder map

```
modules/     lessons
tools/       sdskit.py (all calculations), make_figures.py, make_workbook.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   Excel workbook, data sheet, study log, model evaluation checklist, audit log
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
