# Work Measurement

Learn work measurement. It explains why work standards matter, then shows how to set them with time study, work sampling and standard data, and how to use them in management information systems, process improvement and Lean.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Prerequisites:** none. Basic statistics helps for Modules 05, 11 and 12.

## What you will be able to do

- Explain work measurement and its role in industrial engineering.
- Recognize why work standards are needed.
- Calculate a standard using time study.
- Apply work measurement data: labor reporting, staffing, takt and learning curves.
- Explain related methods: work sampling, standard data and predetermined time systems.

## Running case

**Marlow Pump Works** (fictional) assembles small pumps in a cell and runs a kitting area. The course data includes:

- a 15-cycle continuous time study with a foreign element
- rating-practice results for four analysts
- four weeks of labor reports
- 612 work-sampling observations
- 18 past pack-out studies used to build standard data

All data is simulated with a fixed seed.

## Modules

| # | Module | Outline topic |
|---|---|---|
| 00 | [Need for work measurement: overview](modules/00-need-for-work-measurement.md) | Need for work measurement; overview of methods |
| 01 | [Impact of standards and standard practice](modules/01-impact-of-standards-and-standard-practice.md) | Impact of standards; standard practice |
| 02 | [Documentation and charting](modules/02-documentation-and-charting.md) | Process charts, worker–machine chart, the study file |
| 03 | [Methods analysis and work design](modules/03-methods-analysis-and-work-design.md) | Method first, ECRS, motion economy, work design |
| 04 | [Defining work](modules/04-defining-work.md) | Work units, elements, breakpoints, element types |
| 05 | [Classical time study and elemental analysis](modules/05-classical-time-study-and-elemental-analysis.md) | Procedure, continuous timing, foreign elements, number of cycles |
| 06 | [Rating](modules/06-rating.md) | Pace rating, leveling, rating training and calibration |
| 07 | [Allowances](modules/07-allowances.md) | Personal, fatigue and delay allowances; conventions; common errors |
| 08 | [Computations and time study practice](modules/08-computations-and-time-study-practice.md) | Normal and standard time, units, practices and ethics, maintaining standards |
| 09 | [Labor reporting](modules/09-labor-reporting.md) | Earned hours, efficiency, utilization, productivity, off-standard analysis |
| 10 | [Job analysis](modules/10-job-analysis.md) | Job descriptions and specifications, data collection, links to standards |
| 11 | [Work sampling](modules/11-work-sampling.md) | Planning, confidence intervals, sample size, stability, standards from sampling |
| 12 | [Standard data and related methods](modules/12-standard-data.md) | Element tables and formulas, regression, PMTS, other methods |
| 13 | [Applying work measurement, and capstone](modules/13-applying-work-measurement-and-capstone.md) | Staffing, takt, learning curves, capstone, skill check |

**Suggested schedule:**

- Day 1: modules 00–07
- Day 2: modules 08–13

## Related courses

- [Introduction to Industrial Engineering](../../technical-skills/introduction-to-industrial-engineering/README.md): a one-module overview of time study and work sampling, plus job evaluation and pay
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md) and [Kaizen Leader](../../lean-six-sigma/kaizen-leader/README.md): takt time, line balancing and standard work
- [Process Mapping](../../lean-six-sigma/process-mapping/README.md): process-level charts

## Getting started

```bash
pip install -r requirements.txt
python tools/wmkit.py all         # every worked example
python tools/wmkit.py data        # regenerate data/*.csv
python tools/make_figures.py      # regenerate figures/
```

## Folder map

```
modules/     lessons
tools/       wmkit.py (time study, cycles, rating, allowances, labor reporting, work sampling, standard data, learning, staffing), make_figures.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   time study form, study-file checklist, standard-practice outline, work sampling sheet, job analysis worksheet
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
