# Measurement & Basic Statistics — An Open Course

Learn the measurement and statistics toolkit used in process improvement: how to get trustworthy data, summarize it honestly, and avoid the traps averages set. No prerequisites. Every calculation is shown by hand and reproduced with a small Python toolkit and spreadsheet formulas.

## What you will be able to do

- Communicate using core statistical and Lean Six Sigma terminology
- Create histograms showing the relative frequency of observations in each category
- Locate the center of a process
- Measure and assess process variability
- Decide when to use a Pareto chart, then build and interpret one correctly
- Explain variation, why averages can mislead, and the difference between accuracy and precision

## Syllabus (≈6 hours)

| # | Module | Time |
|---|---|---|
| 0 | [Introduction: solving problems with statistics](modules/00-introduction.md) | 25 min |
| 1 | [Basic statistical and Lean Six Sigma terms](modules/01-basic-terms.md) | 30 min |
| 2 | [Descriptive vs inferential statistics](modules/02-descriptive-vs-inferential.md) | 20 min |
| 3 | [Measurement and data types](modules/03-measurement-and-data-types.md) | 30 min |
| 4 | [Selecting the best measurement: accuracy vs precision](modules/04-selecting-the-best-measurement.md) | 35 min |
| 5 | [Graphical summaries](modules/05-graphical-summaries.md) | 25 min |
| 6 | [Pareto charts](modules/06-pareto-charts.md) | 35 min |
| 7 | [Histograms](modules/07-histograms.md) | 35 min |
| 8 | [Understanding variation: why averages mislead](modules/08-understanding-variation.md) | 35 min |
| 9 | [Measuring central tendency](modules/09-central-tendency.md) | 30 min |
| 10 | [Quantifying process variability](modules/10-quantifying-variability.md) | 35 min |
| 11 | [The normal distribution](modules/11-normal-distribution.md) | 35 min |
| 12 | [Wrap-up and skill check](modules/12-skill-check.md) | 30 min |

Answers to the in-module checks are in each module; exercise notes are in [`solutions/`](solutions/README.md).

## Reference

- [Formulas](reference/formulas.md) · [Spreadsheet recipes](reference/spreadsheet-recipes.md) · [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/make_data.py
python tools/make_figures.py
python tools/describe.py pareto data/complaints.csv category --weight cost_usd
```

## Where next

This is the entry course in the repository. Continue with [Charting Process Behavior](../charting-process-behavior/README.md), then [Fundamentals of Hypothesis Testing](../fundamentals-of-hypothesis-testing/README.md).

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
