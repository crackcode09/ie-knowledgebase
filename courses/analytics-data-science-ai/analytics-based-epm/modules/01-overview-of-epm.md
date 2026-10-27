# Module 01 — Overview of and Enterprise Performance Management (EPM)

> The module title is quoted as it appears in the source outline.

## Objectives

- Define enterprise performance management (EPM) and explain why interest in it is growing.
- Describe how EPM is used in commercial and government organizations.
- Explain how enterprise risk management (ERM) and EPM fit together.

## What EPM is

**Enterprise performance management** is the set of integrated methods an organization uses to turn strategy into results and to steer toward them:

| Method | Answers | Module |
|---|---|---|
| Strategy maps and balanced scorecards | Are we executing the strategy? | 04 |
| Activity-based cost management (ABC/M) | What do our products, channels and customers really cost and earn? | 03, 05 |
| Customer profitability and value management | Which customers create value, now and over their lifetime? | 05 |
| Operational costing (unit costs, cost of quality, value-stream costing) | Where is process cost wasted? | 06 |
| Driver-based budgets, rolling forecasts, scenario planning | What resources will we need, and what could happen? | 07 |
| Enterprise risk management | What could knock us off course, and how likely is it? | 01, 07 |
| Business analytics, especially predictive analytics | What is likely to happen, and what should we do? | 02 |

EPM is not one software package or one report. Its value comes from **integrating** these methods so that they share data and assumptions. This course's view is that analytics is what makes each method more useful.

## Why interest is growing

- Strategy is often poorly executed. Measures don't connect to it, and budgets are disconnected from it.
- Margins depend on **cost-to-serve** and product mix more than on average unit costs.
- Annual budgets are out of date within months.
- Data and analytics tools have become cheap and widely available.

## Commercial and government use

| Commercial | Government |
|---|---|
| Profit by product, channel, customer | Cost per service output and per citizen served |
| Pricing, mix and channel decisions | Shared-service chargebacks between agencies |
| Driver-based budgets for sales and operations | Outcome-based scorecards and performance reporting |
| Shareholder value | Mission outcomes per unit of funding |

## ERM and EPM

**ERM** identifies, assesses and manages risks to objectives. **EPM** plans and steers performance toward those objectives. They meet in four places:

1. **The same objectives.** Risks are defined against strategic objectives, the same ones the scorecard measures.
2. **Risk-adjusted plans.** Forecasts and budgets show a range of outcomes, including risk events, not a single number (Module 07).
3. **Key risk indicators next to KPIs.** A leading signal that a risk is becoming more likely, for example the share of late deliveries from one key supplier.
4. **Shared decisions.** Investments are judged on expected return **and** the risk they add or remove.

## Running case: Larkfield Instruments

**Larkfield Instruments** (fictional) makes 12 instrument models and sells to 40 customers through three channels: direct sales, distributors and a web shop. Revenue is $14.5 M. Leadership's questions:

- Which channels and customers actually make money?
- How should next year's budget be built, now that the web channel is growing fast?
- What is the realistic range of next year's profit once risks are included?

All data is simulated with a fixed seed (2029).

## Run it

```bash
python tools/epmkit.py data
python tools/epmkit.py all
```

## Check yourself

1. Name three EPM methods and the question each answers.
2. Give one way ERM and EPM connect in a budget.

<details><summary>Answers</summary>

1. Any three from the table. For example: scorecard → are we executing the strategy?; ABC/M → what do customers really cost?; rolling forecast → what will we need next?
2. Build the budget as a range that includes the probability and impact of the main risks (a risk-adjusted forecast), rather than a single point estimate.

</details>
