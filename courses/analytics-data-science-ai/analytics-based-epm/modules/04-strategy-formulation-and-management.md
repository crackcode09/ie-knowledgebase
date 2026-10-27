# Module 04 — Strategy Formulation and Strategy Management

## Objectives

- Communicate strategy with mission, vision, a strategy map and a balanced scorecard.
- Distinguish strategic KPIs (scorecard) from operational performance indicators (dashboards).
- Select KPIs and set targets and weights.

## From mission to measures

| Element | Larkfield |
|---|---|
| **Mission** (why we exist) | Accurate measurement that keeps our customers' processes safe and efficient |
| **Vision** (where we are going) | The preferred instrument partner for mid-size process plants, with service as good as our products |
| **Strategy** (how we will win) | Grow profitable distributor and direct accounts; make web self-service cheap to serve; cut order-to-ship lead time |

## Strategy map

A strategy map shows cause and effect between objectives in four perspectives, read from the bottom up:

```
Financial        Grow operating margin  ◄──  Grow profitable revenue      Lower cost-to-serve
                         ▲                          ▲                            ▲
Customer         Retain key accounts  ◄────  Deliver on time  ◄────  Easy, low-touch web ordering
                         ▲                          ▲                            ▲
Internal         Shorter order-to-ship  ◄──  Right first time (quality)   Cost-to-serve visible to sales
                         ▲                          ▲                            ▲
Learning &       Cross-trained teams          Analytics skills            Improvement culture
growth
```

## Balanced scorecard

Each objective gets one or two **strategic KPIs**, with a target and a weight (`python tools/epmkit.py scorecard`). The financial and retention figures are computed live from the ABC and churn models:

| Perspective | KPI | Target | Actual | Status |
|---|---|---|---|---|
| Financial | Operating margin % | 18.0 | 15.6 | red |
| Financial | Revenue growth % | 6.0 | 6.8 | green |
| Financial | Cost-to-serve, % of revenue | 20.0 | 23.7 | red |
| Customer | Customer retention % (predicted) | 92.0 | 81.9 | red |
| Customer | On-time delivery % | 96.0 | 93.0 | amber |
| Customer | Net promoter score | 40 | 34 | red |
| Internal | First-pass yield % | 97.0 | 97.6 | green |
| Internal | Order-to-ship lead time (days) | 5.0 | 6.2 | red |
| Internal | Cost of quality, % of sales | 6.0 | 7.1 | red |
| Learning | Cross-trained employees % | 60 | 52 | red |
| Learning | Analytics-skilled analysts | 6 | 4 | red |
| Learning | Ideas implemented per employee | 2.0 | 2.3 | green |

- Achievement = actual ÷ target (target ÷ actual where lower is better), capped at 120 %.
- Status: green ≥ 100 %, amber ≥ 90 %, red below 90 %.
- **Weighted score: 91.4 %.** Read the reds, though, not just the score.

The story the map tells: margin is held back by **cost-to-serve** and **retention**. Both connect to **on-time delivery** and **lead time**, which connect to **cross-training** and **analytics skills**.

## Strategic KPIs vs operational performance indicators

| | Strategic KPI (scorecard) | Operational PI (dashboard) |
|---|---|---|
| Purpose | Is the strategy working? | Is the process running right now? |
| Audience | Executives, monthly or quarterly | Teams and managers, daily or weekly |
| Number | Few (10–20) | Many |
| Example | On-time delivery %, by quarter | Orders shipped today vs plan; pick errors this shift |
| Link | Each one traces to a strategy-map objective | Drives a KPI |

A common mistake is to fill the scorecard with operational indicators, which turns it into a dashboard with no strategy.

## Selecting KPIs

- **Trace** each KPI to one objective on the map.
- Prefer **leading** indicators (on-time delivery) alongside **lagging** ones (retention, margin).
- Measures must be **defined** (formula, data source, owner, frequency) and **affordable** to collect.
- Set targets from strategy and benchmarks, not from last year plus a few percent.
- Weight KPIs according to how important they are to the strategy.

## Run it

```bash
python tools/epmkit.py scorecard
```

## Check yourself

1. Is "number of support calls answered within 2 minutes today" a KPI or a PI?
2. Compute the achievement for order-to-ship lead time (target 5.0, actual 6.2 days).

<details><summary>Answers</summary>

1. An operational **PI** (daily, process-level). It may drive the retention KPI.
2. Lower is better, so 5.0 / 6.2 = **80.6 %**: red.

</details>
