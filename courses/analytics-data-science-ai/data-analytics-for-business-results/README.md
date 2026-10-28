# Data Analytics for Business Results

Learn to use data and analytics to get measurable business results. It covers finding opportunities and use cases, working with business, IT and data teams, mapping processes to find where value is added, and making data-driven decisions by weighing trade-offs. The four modules follow the source course outline: each outline topic is a section heading, with the same wording and in the same order.

**Length:** 8 hours, as four 2-hour sessions (one per module), plus an optional capstone project.  
**Prerequisites:** comfortable with spreadsheets and basic business metrics. Python is optional: every result is printed in the lessons, and the scripts reproduce it.

## What you will be able to do

- Identify business opportunities and use cases for data and analytics.
- Drive adoption by collaborating with business, IT and data teams.
- Map process flows and identify value-adding activities and the data they create.
- Improve technical competency (EDA, association rules, hypothesis tests, regression, machine learning) and make data-driven decisions by weighing trade-offs.

## Running case

**Pinecrest Supply** (fictional) is an industrial MRO distributor with five branches. All data is simulated with a fixed seed. The course follows it through:

- a data-quality scorecard on 12 dimensions: timeliness is worst at 28.9 %
- EDA of 4,000 orders: East's average order is 22 % larger than South's, and the difference is real (Welch *t* = 6.21)
- Apriori on 12,318 order lines: a PPE trio rule with lift 2.52
- an A/B test of a reminder e-mail: +2.4 points, *p* = 0.046
- a sales regression: R² 0.75; holdout RMSE $24.8k vs $54.8k for a naive mean
- a churn model: AUC 0.81; the threshold is chosen by expected value
- RFM segments, and a survivorship-bias trap

## Modules (source outline)

| # | Module | Outline topics (section headings) |
|---|---|---|
| 01 | [Foundations of Data Analytics](modules/01-foundations-of-data-analytics.md) (the source gives no module title) | Introduction to Data Analytics · Types of Analytics and Data Science Techniques Taxonomy · Phases of the Data Analytics Lifecycle · MAD Framework and Types of Business Insights · Types of Business Data and Data Types · 3 types of IT Systems · Data Quality and its 12 key dimensions |
| 02 | [Descriptive Analytics](modules/02-descriptive-analytics.md) | Measuring Business Performance with Exploratory Data Analytics · Measures of Central Tendency and Variation · Introduction to Associative Data Analytics · Apriori Techniques · Hypothesis Testing |
| 03 | [Predictive Analytics](modules/03-predictive-analytics.md) | Fundamentals of Predictive Analytics · Regression Models – Simple Linear Regression and Multiple Linear Regression · Evaluating Analytics Models · Fundamentals of ML (Machine Learning) and key characteristics of ML Models · Supervised & Unsupervised ML Algorithms |
| 04 | [Data Story Telling and Decision Science](modules/04-data-storytelling-and-decision-science.md) | Data Storytelling including Data Visualization · Introduction to Decision Making · Decision Making Models · Biases in Decision Making · Managing your careers in Data Analytics · Summary and Wrap-up |
| 05 | [Capstone: from question to decision](modules/05-capstone.md) (added) | — |

**Suggested schedule (4 × 2 h):**

| Session | Content |
|---|---|
| 1 | Module 01: process map and data-quality exercise |
| 2 | Module 02: EDA, Apriori, A/B test |
| 3 | Module 03: regression, model evaluation, churn and segments |
| 4 | Module 04: story rewrite, expected-value decision, bias, careers, wrap-up |

## Related courses

- [Engineering Analytics](../engineering-analytics/README.md) and [Advanced Engineering Analytics](../advanced-engineering-analytics/README.md): deeper statistical and ML methods
- [Fundamentals of Hypothesis Testing](../../lean-six-sigma/fundamentals-of-hypothesis-testing/README.md)
- [Process Mapping](../../lean-six-sigma/process-mapping/README.md)
- [Engineering Decision Making](../../operations-research-decision-analysis/engineering-decision-making/README.md)
- [Technical Communications](../../technical-skills/technical-communications/README.md)

## Getting started

```bash
pip install -r requirements.txt
python tools/dalkit.py all          # every worked example
python tools/dalkit.py data         # regenerate data/*.csv (fixed seed)
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons (source outline topics as section headings)
tools/       dalkit.py (data quality, EDA, Apriori, A/B and t-tests, regression, churn classification, RFM segmentation, bias), make_figures.py
data/        simulated customer master, orders, order lines, A/B test, branch-month panel, churn
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   use-case canvas, data-quality scorecard, model checklist, one-page story
```

## Notes on sources

The outline names three things without defining them. The course's interpretations are flagged in the lessons and in [further reading](reference/further-reading.md):

- the "MAD framework" is taken as Monitor–Analyze–Drill to detail
- the "12 key dimensions" of data quality are a compiled list, since published lists vary
- the "3 types of IT systems" are taken as systems of record, engagement and insight

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
