# Introduction to Engineering Analytics

A free, open course on turning data into decisions. It covers visualization, descriptive and predictive analytics, segmentation and classification, regression, forecasting, Big Data basics and optimization, with hands-on case studies.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Audience:** engineers, managers and anyone who wants to understand how data and Big Data will affect their operations.  
**Prerequisites:** basic statistics helps (see [Applied Statistics](../../technical-skills/applied-statistics/README.md)). Every example runs in free Python tools, and a spreadsheet workbook is provided for those who prefer Excel.

## What you will be able to do

- Apply data visualization techniques.
- Explain the value of segmentation and classification.
- Use basic descriptive and predictive analytics tools.
- Assess how Big Data affects decision-making.
- Describe the technology behind Big Data.
- Identify the strategic implications of analytics.

## Running case

**Ridgeway Industrial** (fictional) makes and distributes industrial fittings. All data is simulated with a fixed seed:

- a SQLite star-schema order database
- 300 customers
- 500 SKUs
- 1,200 machine-health records
- two years of daily plant energy
- 400 process batches with 10 sensors
- five years of monthly sales

## Modules

| # | Module | Body of knowledge |
|---|---|---|
| 00 | [Foundations](modules/00-foundations.md) | What engineering analytics is; descriptive, diagnostic, predictive and prescriptive analytics; the analytics process; business impact; data as a strategic asset |
| 01 | [Visualization and interaction](modules/01-visualization-and-interaction.md) | Visualization strategies, encodings, small multiples, interaction, dashboard design |
| 02 | [Descriptive analytics, data models, databases](modules/02-descriptive-analytics-and-data.md) | Data types and quality, descriptive statistics, relational models, star schema, SQL, design considerations |
| 03 | [Segmentation and classification](modules/03-segmentation-and-classification.md) | k-means clustering, silhouette, ABC inventory classification, logistic regression, decision tree, confusion matrix, precision/recall/AUC, cost-based thresholds |
| 04 | [Regression and case study](modules/04-regression-case-study.md) | Simple and multiple regression, dummy variables, residuals, prediction intervals, energy case study |
| 05 | [Predictive analytics: PCA and forecasting](modules/05-predictive-analytics-pca-forecasting.md) | Principal component analysis, principal component regression, forecasting methods, holdout MAPE |
| 06 | [Big Data](modules/06-big-data.md) | The Vs, distributed and streaming technology, enterprise data models, warehouse vs lake, governance, impact on decisions |
| 07 | [Optimization](modules/07-optimization.md) | Linear-programming product mix, binding constraints, shadow prices, families of optimization |
| 08 | [Strategy and capstone](modules/08-strategy-and-capstone.md) | Strategic implications, roadmap, capstone options, review |

**Suggested 2-day schedule:**

- Day 1: modules 00–03
- Day 2: modules 04–08

## Related courses

- [Applied Statistics](../../technical-skills/applied-statistics/README.md): regression and distributions
- [Technical Communications](../../technical-skills/technical-communications/README.md): presenting analytics results
- [Reliability Engineering Excellence](../../technical-skills/reliability-engineering-excellence/README.md): predictive maintenance context for Module 03
- [Charting Process Behavior](../../lean-six-sigma/charting-process-behavior/README.md): monitoring after deployment

## Getting started

```bash
pip install -r requirements.txt
python tools/anlkit.py data       # regenerate data/ (CSV, SQLite database, Excel workbook)
python tools/anlkit.py all        # every worked example
python tools/make_figures.py      # regenerate figures/
```

The tools are numpy, pandas, SciPy, scikit-learn, statsmodels, matplotlib, SQLite (built into Python) and openpyxl, all free and open-source. Spreadsheet users can open `data/ridgeway.xlsx` and follow the "In a spreadsheet" notes in each module.

## Folder map

```
modules/     lessons
tools/       anlkit.py (data + examples), make_figures.py
data/        CSVs, ridgeway.db (SQLite), ridgeway.xlsx
figures/     charts used in the lessons
solutions/   key results + facilitator notes
reference/   SQL cheat sheet, metrics, glossary, further reading
templates/   use-case canvas, data dictionary, model card
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
