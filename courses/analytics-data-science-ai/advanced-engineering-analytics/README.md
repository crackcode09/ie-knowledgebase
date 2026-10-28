# Advanced Engineering Analytics

Go beyond introductory analytics. You'll merge and prepare messy data from several systems, analyze it with ANOVA, regression, nonparametric methods and designed experiments, improve prediction accuracy, and communicate results with dashboards.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Prerequisites:** [Introduction to Engineering Analytics](../engineering-analytics/README.md) or equivalent. Module 00 gives a fast-track review.

## What you will be able to do

- Explain the strategic implications of data science for an organization.
- Describe key data science concepts.
- Apply advanced visualization, descriptive and predictive analysis techniques.
- Interpret and communicate data analysis results effectively.
- Improve prediction accuracy.

## Running case

**Corbin Packaging** (fictional) heat-seals food trays on four lines. Six months of data come from five sources:

- an Excel production workbook;
- a quality-lab export;
- a maintenance log;
- daily line sensors;
- customer orders.

There is also a designed experiment on seal settings. The data includes realistic problems: duplicates, values in °F, inconsistent labels and missing values. Analytics is used to:

- improve quality (seal strength);
- predict and reduce breakdowns;
- raise utilization;
- lower cost per unit;
- improve on-time delivery.

## Modules

| # | Module | Outline topic |
|---|---|---|
| 00 | [Business impact and fast-track review](modules/00-business-impact-and-review.md) | Business impact of data science; review of the introductory course |
| 01 | [Managing data](modules/01-managing-data.md) | Sources, grain, keys, data dictionary, data management practice |
| 02 | [Merging datasets](modules/02-merging-datasets.md) | Excel and other sources; join types; aggregating before joining; the fan-out trap; key validation |
| 03 | [Preparing data](modules/03-preparing-data.md) | Duplicates, units, labels, missing values, outliers, derived features |
| 04 | [Descriptive statistics](modules/04-descriptive-statistics.md) | Utilization, scrap, quality, cost and delivery by group |
| 05 | [ANOVA](modules/05-anova.md) | One-way and two-way ANOVA, Tukey HSD, effect size, assumptions |
| 06 | [Linear regression](modules/06-linear-regression.md) | Multiple regression, categorical terms, curvature and optimum, diagnostics, VIF |
| 07 | [Nonparametric analysis](modules/07-nonparametric-analysis.md) | Mann-Whitney, Kruskal-Wallis, Spearman, bootstrap |
| 08 | [Design of experiments](modules/08-design-of-experiments.md) | 2³ factorial: effects, interactions, recommendation |
| 09 | [Improving prediction accuracy](modules/09-improving-prediction-accuracy.md) | Cross-validation, baselines, feature engineering, model comparison, noise floor, thresholds, leakage |
| 10 | [Visualization and dashboards](modules/10-visualization-and-dashboards.md) | Dashboard design, interactive dashboard, BI-tool workflow, communicating results |
| 11 | [Capstone and skill check](modules/11-capstone.md) | End-to-end analysis; 10-question check |

**Suggested schedule:** Day 1 covers modules 00–05. Day 2 covers modules 06–11.

## Tools

Everything runs on free tools: Python with pandas, SciPy, statsmodels, scikit-learn, openpyxl and Plotly. The modules also describe how to do the same work in a spreadsheet and in BI tools such as Tableau or Power BI, but no BI software is required.

## Related courses

- [Introduction to Engineering Analytics](../engineering-analytics/README.md)
- [Fundamentals of Hypothesis Testing](../../lean-six-sigma/fundamentals-of-hypothesis-testing/README.md): ANOVA and nonparametric tests in depth
- [Applied Statistics](../../technical-skills/applied-statistics/README.md): regression
- [Design of Experiments](../../technical-skills/design-of-experiments/README.md)
- [Technical Communications](../../technical-skills/technical-communications/README.md): presenting results

## Getting started

```bash
pip install -r requirements.txt
python tools/aeakit.py data         # regenerate data/ (CSV + Excel workbook)
python tools/aeakit.py all          # every worked example
python tools/make_figures.py        # regenerate figures/
python tools/build_dashboard.py     # regenerate dashboard/corbin_operations_dashboard.html
```

## Folder map

```
modules/     lessons
tools/       aeakit.py (data, merge/prepare, analyses, models), make_figures.py, build_dashboard.py
data/        production_workbook.xlsx and CSV exports
dashboard/   interactive HTML dashboard
figures/     charts used in the lessons, including a dashboard screenshot
solutions/   key results + facilitator notes
reference/   cheat sheet, glossary, further reading
templates/   data dictionary, analysis plan, dashboard specification
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
