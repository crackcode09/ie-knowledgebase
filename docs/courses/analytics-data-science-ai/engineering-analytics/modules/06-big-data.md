# Module 06 — Big Data: Technology, Enterprise Modeling and Impact on Decisions

## Objectives

- Describe what makes data "big" and the technologies built to handle it.
- Explain enterprise data models, data warehouses, data lakes and their role.
- Assess how Big Data affects decision-making, and its risks.

## What makes data "big"

Often described by the "Vs":

| V | Meaning | Manufacturing example |
|---|---|---|
| Volume | too much for one machine or a spreadsheet | 1 kHz vibration from 200 machines ≈ billions of readings a month |
| Velocity | arrives fast; may need real-time response | sensor streams, machine alarms |
| Variety | many formats | ERP tables, MES logs, images from vision systems, text in work orders |
| Veracity | uncertain quality | sensor drift, manual entries |
| Value | worth extracting | only if it changes decisions |

Scale check: 200 sensors × 1,000 readings/s × 86,400 s/day ≈ 17 billion readings a day. A spreadsheet holds about a million rows.

## The technology underneath

| Need | Technology idea | Examples (categories, not endorsements) |
|---|---|---|
| Store huge volumes cheaply | distributed file systems and cloud object storage | HDFS; cloud object stores |
| Process in parallel | split data across many machines, process pieces, combine (MapReduce idea) | Hadoop MapReduce, Apache Spark |
| Fast analytics on tables | columnar storage and compression; massively parallel query engines | Parquet files; cloud data warehouses |
| Real-time streams | message queues and stream processors | Kafka-style event streaming; stream processing engines |
| Flexible / non-tabular data | NoSQL stores (document, key-value, time-series, graph) | time-series databases for sensor data |
| Edge computing | process near the machine, send summaries | edge gateways computing vibration features |
| Scalable compute on demand | cloud infrastructure | pay per use |

Key principle: **move computation to the data** and **process in parallel**, rather than pulling everything onto one computer.

Not every problem is Big Data. Ridgeway's order history (4,000 lines a year) fits easily in SQLite or a spreadsheet; its vibration streams do not.

## Enterprise modeling and data models

An **enterprise data model** defines the organization's key entities (customer, product, order, asset, work order, supplier), their attributes and relationships — consistently across systems. It answers "what is a customer?" once.

| Store | Holds | Structure | Typical users |
|---|---|---|---|
| Operational systems (ERP, MES, CMMS) | current transactions | normalized, application-specific | operations |
| **Data warehouse** | cleaned, integrated history | modeled (often star schemas, Module 02) | reporting, BI |
| **Data lake** | raw data of any type | schema applied when read | data scientists |
| Lakehouse (hybrid) | raw + curated layers in one platform | both | both |

**Master data management** keeps core entities (customer, product, asset) consistent across systems. **Data governance** sets ownership, definitions, quality rules, access and retention. Without governance, a data lake becomes a "data swamp."

## How Big Data changes decisions

| Before | With Big Data |
|---|---|
| decide from monthly reports | decide from near-real-time data |
| sample-based inspection | 100 % sensor-based monitoring |
| judgment on maintenance timing | condition-based and predictive maintenance |
| average customer | segment-of-one personalization |
| periodic forecasts | continuous re-forecasting |

**Risks and limits:**

- **More data ≠ better decisions.** Bias, poor quality and spurious correlations scale too.
- **Many variables, many false discoveries** — with thousands of signals, some correlate by chance. Validate on new data.
- **Privacy, security and ownership** — of customer and employee data, and of machine data shared with equipment suppliers.
- **Cost and skills** — infrastructure and people are expensive; start from a valuable use case.
- **Organizational change** — decisions must actually move to the people and processes that use the data.

## Check yourself

1. Is Ridgeway's monthly sales history "Big Data"? Is a vision system capturing 30 images/s on 10 lines?
2. Give one reason a data lake might fail to deliver value.
3. Why does an enterprise data model matter even for small companies?

<details><summary>Answers</summary>

1. Sales: no — 60 rows. Vision images: yes on volume and velocity (about 26 million images a day across 10 lines) and variety (unstructured).
2. No governance: undocumented, inconsistent data that analysts can't find or trust; or no business question driving its use.
3. Consistent definitions of customer, product and asset let every report and model agree; integration between systems gets much easier.

</details>
