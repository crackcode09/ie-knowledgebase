# Root Cause Analysis & Problem Solving — An Open Course

A free, open course on finding and removing the real causes of problems — from a clear problem statement, through qualitative tools (process maps, fishbones, 5-Why, root cause trees) to statistical proof (stratification, correlation, multiple and logistic regression), and on to solutions that stick. One case runs through every module: leaking valve bodies from a three-machine cell. No prerequisites; *Measurement & Basic Statistics* helps.

## What you will be able to do

- Write effective problem statements and bound a problem with 5W2H and Is/Is-Not
- Build and interpret Pareto charts and process maps
- Identify and organize potential causes with a cause-and-effect diagram
- Find root causes with 5-Why, 1-How, and map interacting causes with a root cause tree
- Stratify data to locate causes
- Use scatter plots and correlation to examine relationships
- Use simple and multiple regression to find significant inputs and model Y = f(X)
- Use binary logistic regression when Y is pass/fail
- Error-proof, select solutions with a decision matrix, and track actions with a corrective action matrix

## Syllabus (≈14 hours)

| # | Session | Module | Time |
|---|---|---|---|
| 0 | Identify | [Introduction and the RCA framework](modules/00-introduction-and-framework.md) | 45 min |
| 1 | Identify | [Writing effective problem statements](modules/01-problem-statements.md) | 40 min |
| 2 | Identify | [Solving problems with statistics: measurement and metrics](modules/02-statistics-and-metrics.md) | 30 min |
| 3 | Identify | [Pareto charts](modules/03-pareto-charts.md) | 40 min |
| 4 | Identify | [Process flow charts and swim lanes](modules/04-process-maps-and-swim-lanes.md) | 40 min |
| 5 | Investigate | [Cause-and-effect diagram](modules/05-cause-and-effect-diagram.md) | 45 min |
| 6 | Investigate | [5-Why, 1-How](modules/06-five-why-one-how.md) | 40 min |
| 7 | Investigate | [Root cause tree and comprehensive root cause mapping](modules/07-root-cause-tree-and-mapping.md) | 75 min |
| 8 | Investigate | [Root cause stratification](modules/08-stratification.md) | 45 min |
| 9 | Statistics | [Scatter plots and correlation](modules/09-scatter-plots-and-correlation.md) | 50 min |
| 10 | Statistics | [Simple regression](modules/10-simple-regression.md) | 50 min |
| 11 | Statistics | [Multiple regression](modules/11-multiple-regression.md) | 90 min |
| 12 | Statistics | [Binary logistic regression](modules/12-logistic-regression.md) | 75 min |
| 13 | Solve | [Error-proofing](modules/13-error-proofing.md) | 40 min |
| 14 | Solve | [Prioritizing and selecting a solution](modules/14-prioritizing-and-selecting-solutions.md) | 45 min |
| 15 | Solve | [Corrective action matrix and verification](modules/15-corrective-action-matrix.md) | 45 min |
| 16 | — | [Capstone](modules/16-capstone.md) | 3–4 h |

Answers to each module's checks are in the module; capstone answers are in [`solutions/`](solutions/README.md).

## Reference

[Formulas](reference/formulas.md) · [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/make_data.py
python tools/rca.py all
python tools/make_figures.py
```

## Related courses

[Measurement & Basic Statistics](../measurement-and-basic-statistics/README.md) · [Charting Process Behavior](../charting-process-behavior/README.md) · [Fundamentals of Hypothesis Testing](../fundamentals-of-hypothesis-testing/README.md) · [Design for Six Sigma](../design-for-six-sigma/README.md)

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
