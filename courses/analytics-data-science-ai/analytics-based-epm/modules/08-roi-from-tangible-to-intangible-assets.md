# Module 08 — The Shift in ROI's Source from Tangible to Intangible Assets

## Objectives

- Explain why returns increasingly come from intangible assets such as information, skills, relationships and processes.
- Show how integrated FP&A and EPM act as a value multiplier, by turning information into better decisions.

## Where returns come from

Traditional ROI thinking focuses on **tangible** assets: machines, buildings, inventory. More and more of a company's value now rests on **intangibles**:

- customer relationships and brand
- know-how and skilled people
- processes, data and models
- intellectual property

Many observers argue that intangibles now make up most of the market value of large listed companies. Treat specific percentages you see quoted as claims to check. This course doesn't verify them.

The practical consequence for EPM: information and analytics capability are **assets that earn a return** when they change decisions.

## Information as a value multiplier

Information has value only if it **changes a decision**. Two Larkfield examples from this course:

| Decision | Without integrated EPM | With it | Value |
|---|---|---|---|
| Web customers | Look profitable under the revenue-based allocation | ABC shows 13 web accounts losing $149,321. A minimum order value of $2,500 per order (same revenue in fewer orders) cuts their order, line and shipment costs by **$184,485**, turning them to **+$35,164** | ≈ $184k/yr (if capacity is actually removed) |
| Outsourcing pick and ship | Full-cost comparison suggests a $262k saving | Avoidable-cost analysis shows $35k, so decide on service and risk | Avoids a poor decision |
| Budget | +8 % incremental: $1.57 M | Driver-based: $1.76 M, with the levers visible | Prevents under-staffing and service failure |

**FP&A** (financial planning and analysis) integrated with **EPM** turns the finance function from scorekeeper into decision support:

- one set of drivers and assumptions
- one data model
- scenario and risk ranges instead of single numbers

## Measuring the return on analytics

Return on an analytics or EPM investment = (value of better decisions − cost) ÷ cost. Value is measured decision by decision:

- profit improved by actions (re-pricing, minimum orders, retention programs)
- costs avoided (poor outsourcing, over- or under-staffing)
- risk losses reduced

Track the decisions and their outcomes, not the number of reports produced.

## Run it

```bash
python tools/epmkit.py insight
```

## Check yourself

1. Why does the minimum-order saving only become real "if capacity is actually removed"?
2. An analytics team costs $250,000 a year and its documented decisions add $600,000 a year. What is the ROI?

<details><summary>Answers</summary>

1. ABC rates spread existing costs, mostly people. Fewer orders only save money if staff hours are redeployed or reduced. Otherwise the cost stays as unused capacity.
2. (600,000 − 250,000) / 250,000 = **140 %**.

</details>
