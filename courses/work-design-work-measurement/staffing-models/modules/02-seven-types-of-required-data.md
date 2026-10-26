# Module 02 — Seven Types of Required Data

## Objectives

- List the seven types of data a staffing model needs and where each comes from.
- Judge the quality and fitness of each data source.
- Plan data collection before building the model.

> **Note.** This course groups the data into seven types to match its outline topic. The grouping is the course author's. The original course's list of seven was not published, so this one may differ from it.

## The seven types

| # | Type | Question it answers | Typical sources | Tri-County file |
|---|---|---|---|---|
| 1 | **Workload volume** (demand drivers) | How much work arrives, and when? | Case management, permit, ticketing and ERP systems | `workload_history.csv` |
| 2 | **Work content** (unit times) | How long does one unit take? | Time study, time records, standard data, SME estimates | `unit_time_studies.csv` |
| 3 | **Activity profile** (direct vs indirect) | What share of the day goes to units, indirect work, allowances, waste? | Work sampling, activity logs | `work_sampling_inspectors.csv` |
| 4 | **Availability** | How many hours does an FTE actually work? | Payroll, leave and training records | `leave_2025.csv` |
| 5 | **Service and policy requirements** | What service level, coverage and span of control are required? | Laws, service agreements, policies, leadership decisions | Course parameters (Module 05) |
| 6 | **Workforce supply** | Who is on staff, and who will leave? | HR roster, separations, retirement eligibility, hiring lead times | `workforce_roster.csv`, `separations_history.csv` |
| 7 | **Performance and cost** | Is staffing linked to results, and what does it cost? | KPIs, quality and backlog data, loaded cost per FTE | `workload_history.csv` (service %), Module 09 costs |

Types 1–5 build **demand**, type 6 builds **supply**, and type 7 **validates** the model and **prices** it.

## Data quality questions

For every source, ask these questions:

| Question | Why it matters |
|---|---|
| **Definition**: does a "unit" mean the same thing everywhere and every year? | Counting rules change; a re-inspection may be counted as an inspection in some years |
| **Completeness**: are any months, sites or work types missing? | Gaps understate demand |
| **Demand vs output**: does it record work requested or work done? | Backlogs and refusals hide demand |
| **Accuracy**: how was it measured, and what is its precision? | SME estimates and self-reported time can be biased |
| **Representativeness**: does the sample cover seasons, sites and staff? | A June-only study misses winter work |
| **Timeliness**: is it recent enough to reflect current methods? | Method changes make old unit times wrong |
| **Ownership**: who maintains it, and will it exist next year? | The model must be refreshed |

## Tri-County data review

| Type | Coverage | Quality | Note |
|---|---|---|---|
| 1 Workload | 60 months, 8 drivers, no gaps | High | Counts are requests, so backlog is included |
| 2 Unit times | 11 activities, 4 methods | Mixed | Two resubmittal rows are SME estimates from only 6 reviewers |
| 3 Activity profile | 1,200 observations, 4 weeks | High for the sample | Taken in one season only; repeat in winter |
| 4 Availability | 35 employees, 2025 | High | 2025 only; check whether one year is typical |
| 5 Policy | Counter target, span 1:9 | Decision | Leadership must confirm the targets |
| 6 Supply | 35 staff; 5 years of separations | Medium | Small numbers make rates unstable |
| 7 Performance and cost | Monthly next-day inspection %; loaded costs | Medium | The service measure is automated and reliable; costs are budget figures |

A data plan lists each type, its source, its owner, the collection method and dates, and the known weaknesses. Use the template `templates/data-collection-plan.md`.

## Run it

```bash
python tools/stmkit.py data_inventory
```

## Check yourself

1. Which data type is a leadership decision rather than a measurement?
2. The permit system counts "inspections completed". During a summer backlog, what bias does that create?
3. Why does supply data (type 6) need several years of history even though it describes people now?

<details><summary>Answers</summary>

1. Type 5, service and policy requirements (service levels, coverage, span of control).
2. Completed counts lag requests. In a backlog they understate demand in peak months and push work into later months, which flattens the seasonal pattern.
3. Separation rates come from history. One year of a small group (21 inspectors) can easily show 0 or 3 quits by chance. Pool several years.

</details>
