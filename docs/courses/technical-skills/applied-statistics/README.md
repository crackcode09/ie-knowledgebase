# Applied Statistics — An Open Course

A free, open, two-day course on summarizing data graphically and mathematically, using probability distributions to forecast process performance, estimating population characteristics from samples, analyzing data that don't follow a standard distribution, and building models that predict business results — plus how to design a data collection system that delivers useful insight. One running case throughout: a contract electronics (PCB) assembler, with six synthetic datasets. No prerequisites.

## What you will be able to do

- Design an effective data collection system
- Analyze and summarize sample data: histograms, mean, median, mode, standard deviation, skewness, kurtosis
- Forecast process performance with the hypergeometric, binomial, Poisson, normal and exponential distributions
- Use the t, chi-square and F distributions for inference
- Build confidence intervals and run hypothesis tests for means, proportions and standard deviations
- Analyze non-normal data (transformations, other distributions, bootstrap, nonparametric tests)
- Measure correlation and build linear and multiple regression models to predict business results

## Syllabus (2 days ≈ 14 hours)

| # | Day | Module | Time |
|---|---|---|---|
| 0 | 1 | [Introduction and data collection systems](modules/00-introduction-and-data-collection.md) | 75 min |
| 1 | 1 | [Descriptive statistics](modules/01-descriptive-statistics.md) | 75 min |
| 2 | 1 | [Discrete distributions: hypergeometric, binomial, Poisson](modules/02-discrete-distributions.md) | 90 min |
| 3 | 1 | [Continuous distributions: normal, exponential](modules/03-continuous-distributions.md) | 75 min |
| 4 | 2 | [Sampling distributions: CLT, t, chi-square, F](modules/04-sampling-distributions.md) | 60 min |
| 5 | 2 | [Confidence, risk and confidence intervals](modules/05-confidence-intervals.md) | 75 min |
| 6 | 2 | [Hypothesis tests for means, proportions, standard deviations](modules/06-hypothesis-tests.md) | 90 min |
| 7 | 2 | [Non-normal data](modules/07-non-normal-data.md) | 60 min |
| 8 | 2 | [Correlation analysis](modules/08-correlation.md) | 50 min |
| 9 | 2 | [Simple linear regression](modules/09-linear-regression.md) | 60 min |
| 10 | 2 | [Multiple regression: predicting business results](modules/10-multiple-regression.md) | 75 min |
| 11 | — | [Capstone and skill check](modules/11-capstone.md) | 2 h |

Templates: [`templates/statistics-worksheets.md`](templates/statistics-worksheets.md). Answers and instructor notes: [`solutions/`](solutions/README.md). Reference: [Formulas](reference/formulas.md) · [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/statkit.py data      # generate data/*.csv (fixed seed)
python tools/statkit.py all       # every worked example
python tools/make_figures.py
```

## Related courses

[Measurement & Basic Statistics](../../lean-six-sigma/measurement-and-basic-statistics/README.md) (gentler start) · [Fundamentals of Hypothesis Testing](../../lean-six-sigma/fundamentals-of-hypothesis-testing/README.md) (tests and power in depth) · [Root Cause Analysis](../../lean-six-sigma/root-cause-analysis/README.md) (regression and logistic regression for root causes) · [Charting Process Behavior](../../lean-six-sigma/charting-process-behavior/README.md) (variation over time)

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
