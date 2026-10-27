# Quality Engineering Essentials

A free, open course in the quality engineer's core toolkit, organized along the DMAIC improvement process:

- basic statistics
- measurement system analysis
- statistical process control
- capability and risk assessment
- root-cause investigation
- corrective actions and control

**Length:** about 39 hours of self-study, in a foundations module, six sessions and a capstone. About half of that time is hands-on practice.  
**Prerequisites:** none.  
**Roles:** 17-2112.00 (quality engineer), 17-2112.03

## What you will be able to do

- Explain what quality means, how the field developed, and the difference between quality control, assurance and improvement, including where ISO 9001 fits.
- Explain why each quality engineering tool is used, when to apply it in DMAIC, and how to use it.
- Evaluate a measurement system (gauge R&R and attribute agreement).
- Chart process behavior and assess capability.
- Find and verify root causes, and assess risk with FMEA and reliability calculations.
- Select, pilot and sustain corrective actions with control plans, visual management and standard work.

## Running case

**Bayline Fasteners** (fictional) machines brass threaded inserts. The critical characteristic is OD 6.350 ± 0.025 mm. A key customer has returned shipments for oversize and damaged-thread inserts. The course follows a quality engineer from the project charter to the control plan. The data includes:

- 480 production samples
- a gauge R&R study
- an attribute agreement study
- a service-process dataset (quote turnaround)
- a "dirty" data export for cleansing practice
- pilot results

All data is simulated with a fixed seed.

## Sessions

| # | Session | Topics |
|---|---|---|
| 00 | [Foundations of quality](modules/00-foundations-of-quality.md) | What quality means; history from Shewhart to Lean Six Sigma; quality control vs assurance vs improvement; obstacles to continuous improvement; what a process map gives you; ISO 9001:2015 in outline |
| 01 | [Introduction to quality engineering](modules/01-introduction-to-quality-engineering.md) | Y = f(X), Lean principles, 3 M's and 8 wastes, the 99.9% problem, DMAIC, project charter, using AI tools responsibly |
| 02 | [Measurement and basic statistics](modules/02-measurement-and-basic-statistics.md) | Statistical terms, data types, selecting measurements, Pareto, histogram, center and spread, normal distribution, distribution identification, data cleansing |
| 03 | [Measurement system analysis](modules/03-measurement-system-analysis.md) | Measurement as a process, cause-and-effect matrix, gauge R&R, attribute MSA, calibration, data collection, sample size, baseline (DPMO, sigma level) |
| 04 | [Process behavior and capability](modules/04-process-behavior-and-capability.md) | Trend and control charts, chart selection, rational subgrouping, I–MR, data transformation, attribute charts, X̄–R, stage variables, capability |
| 05 | [Analyzing root cause](modules/05-analyzing-root-cause.md) | Problem statements, fishbone, 5-Why/1-How, root cause tree, stratification, box plots, scatter plots, regression, FMEA, reliability |
| 06 | [Corrective actions and control](modules/06-corrective-actions.md) | Corrective action matrix, error-proofing, piloting, change management, control charts, control plan, visual management, 5S, standard work |
| 07 | [Capstone and skill check](modules/07-capstone.md) | DMAIC storyboard; 10-question check |

## Related courses

These courses in the repo go deeper on individual topics:

- [Measurement & Basic Statistics](../../lean-six-sigma/measurement-and-basic-statistics/README.md)
- [Statistical Quality Control](../statistical-quality-control/README.md)
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
modules/     the seven sessions
tools/       qekit.py (statistics, gauge R&R, attribute agreement, capability, regression, FMEA, reliability, pilot test), make_figures.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results + facilitator notes
reference/   formulas, glossary, further reading
templates/   charter, C&E matrix, data collection plan, root cause tree, FMEA, corrective action matrix, control plan
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
