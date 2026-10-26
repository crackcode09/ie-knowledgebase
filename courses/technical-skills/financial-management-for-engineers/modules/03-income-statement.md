# Module 03 — The Income Statement

## Objectives

- Read the income statement from revenue to net income.
- Separate cost of goods sold (COGS) from operating expenses, and EBIT from EBITDA.
- Know which lines a manufacturing engineer can move.

## Concept

The income statement covers a **period** (a month, quarter or year). It answers "did we make money?" on an accrual basis.

```
Revenue
− Cost of goods sold (material, direct labor, manufacturing overhead)
= Gross profit
− Selling, general & administrative (SG&A)
− Depreciation (sometimes inside COGS and SG&A)
= Operating income, EBIT (earnings before interest and taxes)
− Interest expense
= Earnings before tax (EBT)
− Income tax
= Net income
```

**EBITDA** = EBIT + depreciation and amortization. It is a rough proxy for operating cash generation and is used in lending covenants and valuation multiples. It ignores the capital spending needed to keep machines running, so treat it with care.

## Worked example: Riverbend ($000)

| Line | Y1 | Y2 | % of revenue (Y2) |
|---|---|---|---|
| Revenue | 44,000 | 48,000 | 100.0 |
| Cost of goods sold | 31,240 | 33,600 | 70.0 |
| **Gross profit** | **12,760** | **14,400** | **30.0** |
| SG&A | 6,900 | 7,200 | 15.0 |
| Depreciation | 1,900 | 2,100 | 4.4 |
| **EBIT** | **3,960** | **5,100** | **10.6** |
| Interest | 980 | 900 | 1.9 |
| **EBT** | **2,980** | **4,200** | 8.8 |
| Tax (25 %, illustrative) | 745 | 1,050 | |
| **Net income** | **2,235** | **3,150** | **6.6** |

EBITDA (Y2) = 5,100 + 2,100 = **7,200**.

What changed from Y1 to Y2?

- Revenue grew 9.1 %.
- COGS fell from 71 % to 70 % of revenue — a one-point gain worth 480 on Y2 revenue.
- SG&A grew only 4.3 %, slower than sales (**operating leverage**).
- EBIT rose 28.8 % on 9.1 % revenue growth.

## Where engineers move the income statement

| Engineering action | Line affected |
|---|---|
| Scrap and rework reduction | COGS (material, labor) |
| Cycle-time reduction | COGS (labor, overhead absorption); can enable more revenue |
| Setup reduction (SMED) | COGS; smaller batches cut inventory (balance sheet) |
| New capital equipment | Depreciation (up), COGS (down if it saves labor) |
| Design-to-cost | COGS |
| Warranty and returns reduction | COGS or SG&A, depending on how the company books it |

A $1 saving in COGS falls straight to EBIT and adds $0.75 to net income after tax. To earn the same $0.75 from growth at Riverbend's 6.56 % net margin takes 0.75 / 0.0656 ≈ **$11 of new revenue**. Cost reduction is powerful.

## Absorption costing caution

Manufacturing overhead is assigned (absorbed) into inventory. Building more units than you sell parks overhead in inventory and makes the period's profit look better — while cash gets worse. Lean plants that cut inventory may see a temporary profit dip for the same reason. Read inventory changes alongside the income statement.

## Run it

```bash
python tools/finkit.py statements
```

## Check yourself

1. Compute the Y1 gross margin and EBIT margin.
2. Why is EBITDA higher than EBIT, and why is it not cash?
3. A scrap project saves $200k a year in material. Holding all else equal, how much does net income rise?

<details><summary>Answers</summary>

1. Gross margin 12,760 / 44,000 = 29.0 %; EBIT margin 3,960 / 44,000 = 9.0 %.
2. It adds back depreciation, a non-cash expense. It is not cash because it ignores working-capital changes, capital spending, interest and taxes.
3. 200 × (1 − 0.25) = $150k.

</details>
