# Module 03 — Fact-based Data with Managerial Accounting (Activity Based Cost Management [ABC/M])

## Objectives

- Assign resource costs to activities and activities to cost objects (products, channels, customers).
- Use ABC/M for shared-service chargebacks.
- Compare ABC/M with other costing methods.

## How ABC/M assigns costs

```
Resources (general ledger)  ──resource drivers──►  Activities  ──activity drivers──►  Cost objects
salaries, IT, facilities      (% of effort, m²)      process orders,       (# orders,        products, channels,
                                                     pick and ship, …        # shipments, …)   customers, services
```

Larkfield's **$3.94 M** of indirect and selling costs (`data/resources.csv`) are split into nine activities using effort interviews (`data/resource_drivers.csv`). Each activity is then charged to cost objects by its driver:

| Activity | Cost | Driver | Quantity | Rate |
|---|---|---|---|---|
| Process orders | $483,500 | orders | 6,201 | **$77.97 per order** |
| Enter order lines | $301,500 | lines | 19,337 | $15.59 per line |
| Pick and ship | $738,000 | shipments | 8,201 | $89.99 per shipment |
| Handle returns | $170,000 | returns | 308 | $551.95 per return |
| Support customers | $527,500 | support calls | 4,364 | $120.88 per call |
| Sales visits | $822,000 | visits | 282 | $2,914.89 per visit |
| Engineer specials | $398,500 | special orders | 119 | $3,348.74 per special |
| Sustain products | $218,000 | product-years | 12 | $18,166.67 per product |
| Inspect production runs | $281,000 | production runs | 572 | $491.26 per run |

**Customer-level** activities (orders through specials) are driven by how customers buy. **Product-level** activities (sustaining, inspection runs) are driven by the product line.

## Profitability

**Products** (revenue net of discounts − direct cost − product-level activities): margins run from **31 % (P03)** to **48 % (P01)**. P03 is hurt by **66 production runs** for only 914 units. Short runs cost $491 each for inspection alone.

**Customers:** customer-level activities are added on top. A worked example, customer C10 (web):

| Item | $ |
|---|---|
| Revenue | 107,066 |
| − Direct cost | 51,679 |
| − Product-level overhead | 6,077 |
| − Orders 252 × 77.97 | 19,648 |
| − Lines 372 × 15.59 | 5,799 |
| − Shipments 362 × 89.99 | 32,576 |
| − Returns 20 × 551.95 | 11,039 |
| − Support calls 155 × 120.88 | 18,736 |
| **ABC profit** | **−38,489** |
| Traditional view (overhead spread by revenue) | +26,365 |

**17 of 40 customers** look profitable under the traditional revenue-based allocation but **lose money** under ABC/M. Module 05 continues the analysis.

## Shared-service chargebacks

IT costs $380,000. Charging it by **headcount** is simple but unfair: the warehouse has many people and few IT needs. Charging by **drivers** (60 % tickets, 40 % application users) changes the picture:

| Department | By headcount | By drivers | Difference |
|---|---|---|---|
| Sales | $112,973 | $86,956 | −$26,017 |
| Customer service | $71,892 | **$164,047** | **+$92,155** |
| Warehouse | $92,432 | $44,586 | −$47,847 |
| Engineering | $61,622 | $49,861 | −$11,761 |
| Finance | $41,081 | $34,551 | −$6,530 |

Driver-based chargebacks tell users what their demand costs, and they encourage behaviour that cuts cost. Customer service raises 1,650 tickets. Fixing the top ticket causes cuts IT demand.

## ABC/M vs other costing methods

| Method | Overhead assigned by | Best for | Weakness |
|---|---|---|---|
| Traditional absorption | Labour hours, machine hours or revenue | Inventory valuation, external reporting | Distorts product and customer cost when overhead is driven by complexity |
| Standard costing | Pre-set rates; variances | Control of stable, repetitive work | Volume-based rates; can reward overproduction (Module 06) |
| **ABC/M** | Activity drivers | Product, channel and customer profitability; process improvement | Effort to build and maintain |
| Time-driven ABC | Time per transaction × capacity cost rate | Simpler maintenance; shows unused capacity | Needs time estimates |
| Lean / value-stream costing | Direct to value streams | Lean organizations | Less product-level detail |
| Throughput accounting | Only truly variable cost (materials) | Constraint decisions | Ignores cost-to-serve |

## Run it

```bash
python tools/epmkit.py abc
python tools/epmkit.py products
python tools/epmkit.py chargeback
```

## Check yourself

1. Customer C38 (direct) has 80 orders, 167 lines, 97 shipments, 4 returns, 97 support calls, 20 visits and 3 specials. Compute its cost-to-serve.
2. Why does charging overhead by revenue hide unprofitable customers?

<details><summary>Answers</summary>

1. 80 × 77.97 + 167 × 15.59 + 97 × 89.99 + 4 × 551.95 + 97 × 120.88 + 20 × 2,914.89 + 3 × 3,348.74 ≈ 6,238 + 2,604 + 8,729 + 2,208 + 11,725 + 58,298 + 10,046 = **$99,847** (to rounding).
2. It assumes cost is proportional to revenue. Small, frequent, service-heavy buyers generate far more activity per dollar of revenue, so they receive too little cost, and large, simple buyers receive too much.

</details>
