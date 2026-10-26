# Fundamentals of Hypothesis Testing — An Open Course

A free, open course on using hypothesis tests to make decisions from data: what a test is, when and how to run one, and how to read the result without fooling yourself. No prerequisites. Every test is worked by hand, then reproduced with a small Python toolkit and spreadsheet formulas.

## What you will be able to do

- Formulate a hypothesis statement
- Differentiate between null and alternative hypotheses
- Distinguish statistical from practical significance
- Determine an appropriate sample size and significance level
- Assign the correct type of error given the outcome of a test
- Use confidence intervals to judge statistical significance
- Given a situation, choose the right test, perform it, and interpret the results
- Explain the difference between parametric and nonparametric tests

## Syllabus (≈14 hours)

| # | Module | Time |
|---|---|---|
| 0 | [Introduction: deciding with data](modules/00-introduction.md) | 30 min |
| 1 | [Hypotheses: the process on trial](modules/01-hypotheses.md) | 45 min |
| 2 | [Decisions and the two types of error](modules/02-errors.md) | 40 min |
| 3 | [Power and sample size](modules/03-power-and-sample-size.md) | 60 min |
| 4 | [Test procedure, p-values, statistical vs practical significance](modules/04-test-procedure-and-p-values.md) | 60 min |
| 5 | [Confidence intervals](modules/05-confidence-intervals.md) | 45 min |
| 6 | [Treatment comparisons with process behavior charts](modules/06-treatment-comparisons-with-charts.md) | 40 min |
| 7 | [One proportion vs a standard](modules/07-one-proportion.md) | 40 min |
| 8 | [Two proportions](modules/08-two-proportions.md) | 40 min |
| 9 | [Several proportions: chi-square](modules/09-chi-square-multiple-proportions.md) | 50 min |
| 10 | [One mean vs a standard: one-sample t](modules/10-one-sample-t.md) | 45 min |
| 11 | [Two means: two-sample and paired t](modules/11-two-means-and-paired-t.md) | 60 min |
| 12 | [Several means: one-way ANOVA](modules/12-anova.md) | 60 min |
| 13 | [One variance vs a standard](modules/13-one-variance.md) | 35 min |
| 14 | [Two variances: F and Levene](modules/14-two-variances.md) | 40 min |
| 15 | [Parametric vs nonparametric tests](modules/15-parametric-vs-nonparametric.md) | 35 min |
| 16 | [Nonparametric toolset](modules/16-nonparametric-toolset.md) | 60 min |
| 17 | [Choosing the right test](modules/17-choosing-the-right-test.md) | 30 min |
| 18 | [Capstone: four case files](modules/18-capstone-case-files.md) | 2–3 h |

Solutions: [`solutions/`](solutions/README.md).

## Reference

- [Formulas & test selection sheet](reference/formulas.md)
- [Spreadsheet recipes](reference/spreadsheet-recipes.md)
- [Glossary](reference/glossary.md)
- [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/make_data.py       # regenerate datasets (fixed seed)
python tools/make_figures.py    # regenerate figures
python tools/htest.py all       # run every worked example
```

## Related course

[Charting Process Behavior](../charting-process-behavior/README.md) — process behavior charts are used in Module 6 and are the recommended first look at any before/after data.

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
