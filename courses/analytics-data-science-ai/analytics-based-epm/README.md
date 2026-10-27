# Analytics-Based Enterprise Performance Management

A free, open course on combining performance-management methods (balanced scorecards, activity-based cost management, customer profitability, operational costing, driver-based budgets, rolling forecasts and risk) with analytics, especially predictive analytics. It follows the nine-module outline of a one-day workshop, in the same order and with the same module titles.

**Length:** 1 day (7 h) as a workshop, or self-paced (about 2 days with the exercises).  
**Prerequisites:** none. Basic accounting and statistics help.

## What you will be able to do

- Distinguish strategic KPIs in a balanced scorecard from operational performance indicators in dashboards.
- Use "predictive accounting": driver-based budgets, rolling forecasts, what-if analysis and outsourcing decisions.
- Integrate enterprise risk management (ERM) with enterprise performance management (EPM).
- Apply statistics and analytics to product, channel and customer profitability.
- Address implementation barriers, including resistance to change and fear of accountability.

## Running case

**Larkfield Instruments** (fictional) sells 12 instrument models to 40 customers through direct, distributor and web channels ($14.5 M revenue).

- ABC/M shows 17 customers that look profitable under a revenue-based allocation are actually losing money.
- The web channel's cost-to-serve is 83 % of its revenue.
- A churn model (AUC 0.79) feeds customer lifetime value.
- A driver-based budget replaces "+8 %".
- A risk-adjusted Monte Carlo puts next year's P10 profit at $0.71 M.

All data is simulated with a fixed seed.

## Modules (source outline titles)

| # | Module |
|---|---|
| 01 | [Overview of and Enterprise Performance Management (EPM)](modules/01-overview-of-epm.md) |
| 02 | [The Rise of Business Intelligence (BI) and Business Analytics (BA)](modules/02-bi-and-business-analytics.md) |
| 03 | [Fact-based Data with Managerial Accounting (Activity Based Cost Management [ABC/M])](modules/03-fact-based-data-abc-m.md) |
| 04 | [Strategy Formulation and Strategy Management](modules/04-strategy-formulation-and-management.md) |
| 05 | [Customer Profitability and Value Management](modules/05-customer-profitability-and-value-management.md) |
| 06 | [Operational Costing to Optimize Process Costs](modules/06-operational-costing.md) |
| 07 | [The shift to "predictive accounting" for Decision Making and Budgeting](modules/07-predictive-accounting.md) |
| 08 | [The Shift in ROI's Source from Tangible to Intangible Assets](modules/08-roi-from-tangible-to-intangible-assets.md) |
| 09 | [Accelerating the Rate of Adoption for Implementing FP&A and EPM](modules/09-accelerating-adoption.md) |
| 10 | [Capstone](modules/10-capstone.md) (added) |

**Suggested one-day agenda:**

- Morning: modules 01–05
- Afternoon: modules 06–09
- Capstone as follow-up work

## Related courses

- [Financial Management for Engineers](../../technical-skills/financial-management-for-engineers/README.md): statements, budgets, NPV and IRR
- [Cost of Quality](../../quality-operational-excellence/cost-of-quality/README.md): quality costs in depth
- [Introduction to Engineering Analytics](../engineering-analytics/README.md) and [Advanced Engineering Analytics](../advanced-engineering-analytics/README.md): models and dashboards
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md): value streams

## Getting started

```bash
pip install -r requirements.txt
python tools/epmkit.py all          # every worked example
python tools/epmkit.py data         # regenerate data/*.csv
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons (source outline titles)
tools/       epmkit.py (ABC/M, profitability, chargebacks, scorecard, churn, CLV, unit costs, value-stream costing, driver budget, rolling forecast, Monte Carlo with risk register, outsourcing, decision value), make_figures.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   KPI definition sheet, ABC model workbook layout, risk register, EPM roadmap
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
