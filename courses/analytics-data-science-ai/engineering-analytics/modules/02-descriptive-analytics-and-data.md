# Module 02 — Descriptive Analytics: Data Models, Data Properties and Databases

## Objectives

- Describe data types and data-quality properties.
- Explain relational data models, keys and the star schema.
- Query a database with SQL to produce descriptive summaries.
- Apply design considerations for analytics data.

## Data properties

**Types**

| Type | Examples | Summaries |
|---|---|---|
| Continuous | kWh, temperature, revenue | mean, median, SD, percentiles, histogram |
| Discrete count | orders per year, defects | mean, distribution |
| Categorical (nominal) | region, product family | counts, proportions |
| Ordinal | criticality A/B/C, rating 1–5 | counts, median |
| Date/time | order date | trends, seasonality, lags |
| Text, image, signal | comments, photos, vibration waveforms | need extraction first |

**Quality dimensions** — check before analyzing: completeness (missing values), accuracy (correct values), consistency (same definition everywhere — is "revenue" net or gross?), timeliness, uniqueness (no duplicate records) and validity (values in allowed ranges).

**Shape**: analytics tools work best with **tidy** data — one row per observation, one column per variable, one table per kind of thing.

## Descriptive statistics on Ridgeway data

| Measure | Value |
|---|---|
| Plant energy: workdays | 522 (2025–2026) |
| kWh per day: mean / median / SD | 21,688 / 21,614 / 1,962 |
| kWh per unit (mean) | 4.20 |
| Customer annual revenue: mean / median | $103,368 / $67,150 |
| Skewness of customer revenue | 2.38 (long right tail) |
| Share of revenue from the top 20 % of customers | 65.2 % |
| Missing values in customer table | 0 |

Mean ≫ median and positive skew mean a few large customers dominate: **report the median and percentiles**, not just the mean, and expect segmentation (Module 03) to matter.

## Data models and databases

A **relational database** stores data in tables linked by **keys**:

- **primary key** — uniquely identifies a row (`order_id`, `customer_id`);
- **foreign key** — refers to another table's primary key (`fact_orders.customer_id` → `dim_customer.customer_id`).

**Transactional (OLTP)** systems such as ERP and MES are designed for fast, consistent updates (normalized: each fact stored once). **Analytical** stores are designed for fast summarizing, often as a **star schema**:

```
                 dim_date (date, month, quarter)
                        │
dim_customer ── fact_orders (order_id, date, customer_id, product_id, qty, net_price) ── dim_product
(customer_id, region, …)                                                             (product_id, family, list_price)
```

- **Fact table**: one row per event (order line), with measures (qty, price).
- **Dimension tables**: descriptive attributes to slice by (customer, product, date).

## SQL on the Ridgeway database

`data/ridgeway.db` holds the distributor channel's 4,000 order lines for 2026 ($6.84 million).

```sql
SELECT p.family, ROUND(SUM(f.qty * f.net_price), 0) AS revenue, COUNT(*) AS orders
FROM fact_orders f JOIN dim_product p ON f.product_id = p.product_id
GROUP BY p.family ORDER BY revenue DESC;
```

| Family | Revenue | Order lines |
|---|---|---|
| Valves | $5,058,496 | 1,314 |
| Tees | $984,414 | 1,339 |
| Elbows | $797,630 | 1,347 |

Order counts are almost equal, but valves bring **74 %** of revenue — order count is the wrong measure of importance here.

Other queries in `tools/anlkit.py sql`: revenue by quarter (Q1 $1.79M down to Q3 $1.64M); top five customers ($145k–$187k each); average discount by region (8.8 %–9.2 %, essentially uniform).

You can open the database with any SQLite client, or from Python:

```python
import sqlite3, pandas as pd
con = sqlite3.connect("data/ridgeway.db")
pd.read_sql("SELECT * FROM dim_product", con)
```

In a spreadsheet, the same summaries come from a **pivot table** on the order lines with the product and customer attributes looked up (XLOOKUP/VLOOKUP) or joined with the data-model feature.

## Design considerations

- **Define the grain** of each table (one row = one order line? one day? one machine-hour?).
- **Agree definitions** (net vs gross, calendar vs fiscal) and document them in a data dictionary.
- **Keep history** — slowly changing attributes (a customer's region) need effective dates.
- **Avoid duplicating logic** in many spreadsheets; calculate once, upstream.
- **Security and privacy** — restrict personal and commercially sensitive fields.
- **Automate refresh**; a manual monthly copy-paste process will break.

## Check yourself

1. Why would an analyst prefer a star schema over the ERP's normalized tables for monthly reporting?
2. Average customer revenue is $103k. Why is that a misleading "typical customer" figure?
3. Write SQL for the number of distinct customers ordering valves.

<details><summary>Answers</summary>

1. Fewer, simpler joins; tables designed for grouping and filtering; faster queries; consistent definitions in one place.
2. The distribution is right-skewed; the median ($67k) is typical, and a few very large customers pull the mean up.
3. `SELECT COUNT(DISTINCT f.customer_id) FROM fact_orders f JOIN dim_product p ON f.product_id = p.product_id WHERE p.family = 'Valves';`

</details>
