# Charting Process Behavior — An Open SPC Course

Learn **Statistical Process Control (SPC)**: how to chart process behavior over time, separate routine variation from signals, and judge whether a process can meet its specifications.

No prior statistics or Lean Six Sigma knowledge is assumed. Every calculation is shown by hand, and reproduced in a small Python toolkit and in spreadsheet formulas.

## What you will be able to do

- Use process behavior (control) charts to monitor process performance
- Identify common-cause and special-cause variation on a chart
- Evaluate process performance over time with a run (trend) chart
- Use a histogram to show the relative frequency of observations
- Develop a rational sub-grouping strategy
- Construct and interpret attribute charts (p, np, c, u)
- Perform and interpret a process capability analysis

## Syllabus (≈12 hours)

| # | Module | Time |
|---|---|---|
| 0 | [Introduction: why chart process behavior?](modules/00-introduction.md) | 30 min |
| 1 | [Measurement & metrics](modules/01-measurement-and-metrics.md) | 45 min |
| 2 | [Distributions & histograms](modules/02-distributions-and-histograms.md) | 45 min |
| 3 | [Quantifying variability](modules/03-quantifying-variability.md) | 45 min |
| 4 | [Run (trend) charts](modules/04-run-charts.md) | 40 min |
| 5 | [Introduction to process behavior charts & limits](modules/05-intro-to-process-behavior-charts.md) | 45 min |
| 6 | [The XmR chart](modules/06-xmr-chart.md) | 60 min |
| 7 | [Detection rules: common vs special cause](modules/07-detection-rules.md) | 45 min |
| 8 | [Rational subgrouping & the X̄–R chart](modules/08-rational-subgrouping-xbar-r.md) | 60 min |
| 9 | [Attribute charts: p, np, c, u](modules/09-attribute-charts.md) | 60 min |
| 10 | [Tampering: Deming's funnel experiment](modules/10-tampering-deming-funnel.md) | 30 min |
| 11 | [Stratifying with stage variables](modules/11-stratification.md) | 40 min |
| 12 | [Process capability](modules/12-process-capability.md) | 60 min |
| 13 | [Non-normal data & transformations](modules/13-non-normal-data-and-transformations.md) | 45 min |
| 14 | [Advanced charts: X̄–S, EWMA, CUSUM, short-run, three-way](modules/14-advanced-charts.md) | 60 min |
| 15 | [Capstone project](modules/15-capstone.md) | 4–8 h |

Each module has learning objectives, a worked example on real numbers, an exercise, and a self-check quiz. Solutions are in [`solutions/`](solutions/README.md).

## Reference

- [Formulas & constants](reference/formulas-and-constants.md) (one page, print it)
- [Spreadsheet recipes](reference/spreadsheet-recipes.md)
- [Glossary](reference/glossary.md)
- [Further reading](reference/further-reading.md)

## Repository layout

```
modules/     course content (Markdown)
data/        synthetic practice datasets (CSV)
figures/     charts used in the modules (generated)
tools/       spc.py toolkit, data & figure generators, constants check, funnel simulation
solutions/   worked answers to every exercise
reference/   formula sheet, spreadsheet recipes, glossary, reading list
```

## Quick start

```bash
pip install -r requirements.txt
python tools/make_data.py          # regenerate datasets (fixed seeds)
python tools/make_figures.py       # regenerate figures
python tools/check_constants.py    # verify d2, d3, A2, D3, D4 numerically
python tools/spc.py xmr data/shaft_diameter.csv value --baseline 20
```

## How to teach with it

- **Self-paced:** work through modules 0–15 in order; do every exercise before opening the solution.
- **Classroom (2 days):** Day 1 modules 0–7; Day 2 modules 8–13 plus capstone kickoff. Run the funnel experiment live with a real funnel and marble, then show the simulation.
- **Lunch-and-learn series:** one module per session; module 6 and 12 deserve two.

## License

- Course content (Markdown, figures, data): [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- Code in `tools/`: MIT

See [LICENSE](../../../LICENSE). Contributions welcome — see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

