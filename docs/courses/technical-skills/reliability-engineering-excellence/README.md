# Reliability Engineering Excellence

A free, open course on the reliability engineer's role. It covers keeping equipment doing its job, cutting the cost and risk of failure, and building a reliability program that the rest of the plant supports.

**Length:** about 5 days (35 contact hours) of classroom time or self-study.  
**Prerequisites:** basic statistics (mean, standard deviation, probability). See [Applied Statistics](../applied-statistics/README.md).

## What you will be able to do

- Define the reliability engineer's role.
- Identify the essential elements of a successful reliability program.
- Use reliability tools and problem-solving methods.
- Apply reliability economics, statistics and probability to decisions.
- Analyze data with reliability models (exponential, normal, Weibull, block diagrams, reliability growth).
- Find ways to optimize a reliability program.
- Describe design-for-reliability elements.
- Optimize preventive maintenance.
- Explain five predictive maintenance technologies and where each applies.

## Running case

**Lakeshore Components** (fictional) runs **Line A**: a hydraulic press, a grinder with a high-speed spindle, a coolant system, a transfer conveyor and a robot loader. The data includes 12 months of work orders (88 failures, 364 h of downtime), spindle-bearing life data with suspensions, coolant-pump failure history, grinding-wheel life, an asset register and a reliability-growth test. All of it is simulated with fixed seeds.

## Modules

| # | Module | Body of knowledge |
|---|---|---|
| 00 | [Introduction and foundations](modules/00-introduction-and-foundations.md) | Reliability terms, failure patterns, the reliability engineer's role, partnerships across departments |
| 01 | [Risk and asset management](modules/01-risk-and-asset-management.md) | Risk management basics, criticality ranking, risk matrix, risk-based asset management |
| 02 | [Design and asset lifecycle](modules/02-design-and-asset-lifecycle.md) | Design for reliability; purchase, installation and commissioning; block diagrams; reliability growth |
| 03 | [Reliability program and metrics](modules/03-reliability-program-and-metrics.md) | Program elements, management of change, MTBF, MTTR, availability, leading and lagging metrics, optimization |
| 04 | [RCM and TPM](modules/04-rcm-and-tpm.md) | The seven RCM questions, task-selection logic, TPM pillars, autonomous maintenance |
| 05 | [Reliability statistics](modules/05-reliability-statistics.md) | Pareto, exponential (MTBF and its confidence interval, Poisson), normal wear-out |
| 06 | [Weibull analysis](modules/06-weibull-analysis.md) | β and η, suspensions, MLE and rank regression, B-lives |
| 07 | [Reliability economics](modules/07-reliability-economics.md) | Life-cycle cost, ROI, payback, benefit–cost ratio, net return, optimum reliability cost |
| 08 | [RCA, failure reporting and criticality](modules/08-rca-failure-reporting-criticality.md) | FRACAS, physical, human and latent roots, FMECA, RPN |
| 09 | [PM optimization](modules/09-pm-optimization.md) | PM review process, optimum age replacement, time-based to condition-based |
| 10 | [Predictive maintenance](modules/10-predictive-maintenance.md) | P-F interval; vibration, thermography, oil analysis, ultrasound, motor circuit analysis |
| 11 | [Action plan and capstone](modules/11-action-plan-and-capstone.md) | Team action plan, report-out, review questions |

**Suggested 5-day schedule:**

| Day | Modules |
|---|---|
| 1 | 00–02 |
| 2 | 03–04 |
| 3 | 05–07 |
| 4 | 08–10 |
| 5 | 11 (exercises, report-out, review) |

## Related courses

- [Root Cause Analysis & Problem Solving](../../lean-six-sigma/root-cause-analysis/README.md) (Module 08)
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md) (TPM, OEE)
- [Financial Management for Engineers](../financial-management-for-engineers/README.md) (Module 07)
- [Design for Six Sigma](../../lean-six-sigma/design-for-six-sigma/README.md) (design reliability)
- [Technical Communications](../technical-communications/README.md) (report-out)

## Getting started

```bash
pip install -r requirements.txt
python tools/relkit.py all          # every worked example
python tools/relkit.py data         # regenerate data/*.csv
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons
tools/       relkit.py (Weibull MLE with suspensions, age replacement, RBD, LCC, Crow-AMSAA), make_figures.py
data/        work orders, life data, failure histories, asset register (CSV)
figures/     charts used in the lessons
solutions/   key results + facilitator notes
reference/   formulas, glossary, further reading
templates/   criticality, RCA report, FMECA, PM review, PdM route, program assessment, action plan
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
