# Module 06 — Operational Costing to Optimize Process Costs

## Objectives

- Benchmark processes with unit costs.
- Judge activities by value and importance.
- Cost quality (Six Sigma) and value streams (lean).

## Unit costing for benchmarking

Divide an activity's cost by its output to compare sites, periods or competitors. Order management at three sites:

| Site | Orders | Cost | FTE | Cost per order | Orders per FTE | Excess cost vs best |
|---|---|---|---|---|---|---|
| Larkfield | 9,800 | $700,000 | 9.5 | $71.43 | 1,032 | $99,372 |
| **Riverside** | 6,200 | $380,000 | 5.0 | **$61.29** | 1,240 | — |
| Northgate | 4,100 | $310,000 | 4.5 | $75.61 | 911 | $58,712 |

Excess vs best = (site cost per order − best) × site orders. Before using it as a target, check that the sites define "an order" the same way and have a similar mix. Benchmarks that compare unlike things start arguments rather than improvements.

## Value and importance

Classify each activity before trying to cut its cost:

| | High importance to the customer or strategy | Low importance |
|---|---|---|
| **Value-adding** | Protect and improve (engineering specials priced right) | Simplify |
| **Non-value-adding** | Required (compliance, inspection): make it cheaper | **Eliminate** (rework, re-entry, chasing) |

Larkfield examples:

- **Handle returns** ($170,000): non-value-adding. Remove the causes.
- **Enter order lines** ($301,500): required but automatable (EDI and web).
- **Sales visits** ($822,000): value-adding for key accounts, wasteful for small ones.

## Cost of quality in Six Sigma

Quality costs are prevention, appraisal, internal failure and external failure. They are often 5–15 % of sales or more; that range comes from the course author's general knowledge and is unverified. Larkfield's scorecard shows **7.1 %** against a 6 % target. In ABC terms, "Handle returns" and part of "Support customers" and "Inspect production runs" are quality costs. DMAIC projects should be selected on these costs. See the [Cost of Quality](../../../quality-operational-excellence/cost-of-quality/README.md) course for the full method.

## Costing value-stream maps (lean)

**Value-stream costing** assigns costs directly to a value stream: the people, machines and space that serve one product family. It replaces detailed standard costs with a simple value-stream profit and loss statement. A key reason lean organizations use it: under absorption costing, **cutting inventory lowers reported profit** in the short term.

Instrument value stream, one year:

- price $950 per unit; material $410 per unit
- conversion costs $3.2 M (fixed)
- **produced 10,000, sold 10,500**: inventory reduced by 500 units
- the standard fixed cost of $304.76 per unit was set at the planned 10,500 units

| | Value-stream view | Absorption (standard cost) view |
|---|---|---|
| Revenue − material | 10,500 × 540 = $5,670,000 | $5,670,000 |
| Conversion cost charged | $3,200,000 (the period's actual) | 10,500 × 304.76 in cost of sales + $152,381 under-absorbed = $3,352,381 |
| **Profit** | **$2,470,000** | **$2,317,619** |

The absorption view charges an extra **$152,381**: the prior period's overhead that was sitting in the 500 units of inventory now consumed. Lean improvement (less inventory) looks worse on the old reports. That is a classic cause of resistance (Module 09).

## Run it

```bash
python tools/epmkit.py unitcost
python tools/epmkit.py vsc
```

## Check yourself

1. If Northgate reached Riverside's cost per order, what would it save?
2. Why might a plant manager resist reducing inventory if bonuses depend on absorption-cost profit?

<details><summary>Answers</summary>

1. (75.61 − 61.29) × 4,100 ≈ **$58,700** a year (shown as $58,712).
2. Reducing inventory releases overhead from the balance sheet into the period's costs, so reported profit falls even though cash and flow improve.

</details>
