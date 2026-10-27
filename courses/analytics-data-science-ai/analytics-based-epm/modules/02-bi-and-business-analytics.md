# Module 02 — The Rise of Business Intelligence (BI) and Business Analytics (BA)

## Objectives

- Distinguish business intelligence from business analytics.
- Place big data in EPM.
- Distinguish forecasting from predictive analytics, and know when each fits.

## BI vs BA

| | Business intelligence (BI) | Business analytics (BA) |
|---|---|---|
| Question | What happened? Where? How much? | Why did it happen? What will happen? What should we do? |
| Output | Reports, dashboards, drill-down | Models, predictions, optimized decisions |
| Methods | Queries, aggregation, visualization | Statistics, regression, classification, simulation, optimization |
| Users | Many people, routine monitoring | Analysts and decision makers, specific decisions |

BI shows that web-channel profit fell. BA explains **why** (cost-to-serve per order) and **predicts** which customers will leave (this module) or what next year will look like (Module 07).

## Big data

High volume, velocity and variety of data, such as clickstreams, sensors and transactions. For EPM, the useful point is that **more detailed drivers** become measurable at low cost: order lines, support calls, delivery times. These are exactly the drivers ABC/M and predictive models need. Big data is not a goal in itself. Start from the decision and work back to the data.

## Forecasting vs predictive analytics

| | Forecasting | Predictive analytics |
|---|---|---|
| Predicts | An aggregate over time (revenue next quarter) | An outcome for an individual (will this customer leave?) |
| Typical methods | Trend and seasonality, smoothing, regression on time | Classification and regression on attributes (logistic regression, trees) |
| Used for | Budgets, capacity, cash | Retention, pricing, risk scoring, targeting |

## Example: predicting customer churn

`data/customer_history.csv` holds 600 past customer-years: service experience and whether the customer left. A logistic regression gives:

| Predictor | Coefficient | p | Effect |
|---|---|---|---|
| Support calls per order | +1.08 | < 0.001 | More problems → more likely to leave |
| Return rate | +8.56 | 0.033 | |
| Late-delivery rate | +11.51 | < 0.001 | Strongest service driver |
| Years as customer | −0.16 | < 0.001 | Loyalty builds over time |
| Web channel (vs direct) | +0.89 | 0.005 | |

- Base churn rate: **14.7 %**.
- **AUC 0.79**: the model ranks churners above stayers 79 % of the time.
- The 10 % of customers the model scores highest churn at **40 %**, nearly three times the average.

**Accuracy can mislead.** The model is 85.5 % accurate at a 0.5 cut-off, but predicting "nobody leaves" scores 85.3 %. For rare outcomes, use ranking measures (AUC, top-decile rate) and act on the ranking.

Applied to Larkfield's current 40 customers, the predicted churn is 26 % for direct, 12 % for distributors and 21 % for web customers. These figures feed customer lifetime value (Module 05). The [Engineering Analytics](../../engineering-analytics/README.md) and [Advanced Engineering Analytics](../../advanced-engineering-analytics/README.md) courses cover modelling in depth.

## Run it

```bash
python tools/epmkit.py churn
```

## Check yourself

1. Is "next quarter's revenue" a forecasting or a predictive-analytics problem? And "which distributor will leave"?
2. Why is the model's 85.5 % accuracy unimpressive here?

<details><summary>Answers</summary>

1. Revenue: forecasting (an aggregate over time). Distributor churn: predictive analytics (an individual outcome from attributes).
2. Only 14.7 % of customers churn, so predicting "no churn" for everyone already scores 85.3 %. The model's value is in ranking (AUC 0.79; 40 % churn in the top decile).

</details>
