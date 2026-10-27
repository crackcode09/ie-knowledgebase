# Quality Engineering Essentials

Learn to run a quality improvement project end to end: measure a process you can trust, find what is really causing defects, fix it, and keep it fixed.

**Length:** about 39 hours of self-study, half of it hands-on with the course data.  
**Prerequisites:** none.  
**Roles:** 17-2112.00 (quality engineer), 17-2112.03

## What you will be able to do

- Evaluate a measurement system with gauge R&R and attribute agreement.
- Chart process behavior and assess capability.
- Find and verify root causes, and assess risk with FMEA and reliability calculations.
- Select, pilot and sustain corrective actions with control plans, visual management and standard work.
- Explain what quality means, the difference between quality control, assurance and improvement, and where ISO 9001 and the other standards a quality engineer meets fit.

## Running case

**Bayline Fasteners** (fictional) machines brass threaded inserts. The critical characteristic is OD 6.350 ± 0.025 mm. A key customer has returned shipments for oversize and damaged-thread inserts. The course follows one improvement project from charter to control plan, using these datasets:

| File | What it is | Used in |
|---|---|---|
| `data/production_sample.csv` | 480 inserts over 20 days, 2 machines, 3 shifts: OD, tool age, coolant temperature, defect call | 02, 03, 04, 05 |
| `data/gauge_rr.csv` | Gauge R&R study: 10 parts, 3 operators, 3 trials | 03 |
| `data/attribute_msa.csv` | Attribute agreement study: 30 inserts, 3 inspectors, 2 trials, expert standard | 03 |
| `data/quote_turnaround.csv` | Service process: 120 quote turnaround times in hours | 02, 04 |
| `data/dirty_export.csv` | A deliberately flawed export for cleansing practice | 02 |
| `data/pilot_results.csv`, `data/pilot_daily.csv` | Pilot of the corrective action on M2: before and after totals, and the daily counts | 04, 06 |
| `data/tooling_cost.csv` | Cost inputs for the pilot's side-effect check | 06 |

All data is simulated with a fixed seed (1924) by `tools/qekit.py data`. Bayline Fasteners, its customer and every person named in the course are fictional.

## Sessions

| # | Session | Time | Topics |
|---|---|---|---|
| 00 | [Foundations of quality](modules/00-foundations-of-quality.md) | 75 min | What quality means; history from Shewhart to Lean Six Sigma; quality control vs assurance vs improvement; obstacles to continuous improvement; the standards a quality engineer meets; ISO 9001 in outline; what a process map gives you |
| 01 | [Introduction to quality engineering](modules/01-introduction-to-quality-engineering.md) | 3 h | Y = f(X), Lean principles, 3 M's and 8 wastes, the 99.9% problem, DMAIC, project charter, using AI tools responsibly |
| 02 | [Measurement and basic statistics](modules/02-measurement-and-basic-statistics.md) | 6 h | Statistical terms, data types, selecting measurements, Pareto, histogram, center and spread, normal distribution, distribution identification, data cleansing |
| 03 | [Measurement system analysis](modules/03-measurement-system-analysis.md) | 6 h | Measurement as a process, cause-and-effect matrix, gauge R&R, attribute MSA, calibration, data collection, sample size, baseline (DPMO, sigma level) |
| 04 | [Process behavior and capability](modules/04-process-behavior-and-capability.md) | 6 h | Trend and control charts, chart selection, rational subgrouping, I–MR, data transformation, attribute charts, X̄–R, stage variables, capability |
| 05 | [Analyzing root cause](modules/05-analyzing-root-cause.md) | 6 h | Problem statements, fishbone, 5-Why/1-How, root cause tree, stratification, box plots, scatter plots, regression, FMEA, reliability |
| 06 | [Corrective actions and control](modules/06-corrective-actions.md) | 6 h | Corrective action matrix, error-proofing, piloting, change management, control charts, control plan, visual management, 5S, standard work |
| 07 | [Capstone and skill check](modules/07-capstone.md) | 5 h | DMAIC storyboard; 10-question check |

Each session has objectives, the concept, a worked example on the Bayline data (which file, which steps, which command, what the result means), an exercise with answers in `solutions/README.md`, and a check-yourself section.

## Related courses

These courses in the repo go deeper on individual topics:

- [Measurement & Basic Statistics](../../lean-six-sigma/measurement-and-basic-statistics/README.md)
- [Statistical Quality Control](../../quality-operational-excellence/statistical-quality-control/README.md)
- [Charting Process Behavior](../../lean-six-sigma/charting-process-behavior/README.md)
- [Root Cause Analysis & Problem Solving](../../lean-six-sigma/root-cause-analysis/README.md)
- [Reliability Engineering Excellence](../../technical-skills/reliability-engineering-excellence/README.md)
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md)
- [Fundamentals of Hypothesis Testing](../../lean-six-sigma/fundamentals-of-hypothesis-testing/README.md)

## Getting started

```bash
pip install -r requirements.txt
python tools/qekit.py all          # every worked example
python tools/qekit.py data         # regenerate data/*.csv
python tools/make_figures.py       # regenerate figures/
```

## Folder map

```
modules/     the eight sessions
tools/       qekit.py (statistics, gauge R&R, attribute agreement, capability, regression, FMEA, reliability, pilot test and cost), make_figures.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results, exercise answers, facilitator notes
reference/   formula sheet with symbol definitions, glossary, sources
templates/   charter, C&E matrix, data collection plan, root cause tree, FMEA, corrective action matrix, control plan
```

## About this course

It follows the public IISE catalog's course title and topic list for Quality Engineering Essentials, and module 00 covers the topics the catalog lists as a separate "Quality 101" course. Only those public titles and topic lists were used; every lesson, dataset, figure and exercise here is original, and the course is not affiliated with or endorsed by IISE. See the repository's [NOTICE](../../../NOTICE.md).

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
