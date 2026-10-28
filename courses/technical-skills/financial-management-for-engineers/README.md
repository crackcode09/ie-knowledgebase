# Financial Management for Engineers

Learn the financial skills an engineer needs to run a profit center: reading financial statements, budgeting, building a dashboard and judging whether a capital investment pays.

**Length:** about 2 days (14 contact hours) of self-study or classroom time.  
**Prerequisites:** none beyond algebra and a spreadsheet. Python is optional.

Well suited to engineers newly promoted into management.

## What you will be able to do

- Create a budget and track performance against it.
- Create a financial dashboard reflecting key metrics.
- Evaluate the economic viability of capital investments.
- Interpret financial statements.

## Running case

**Riverbend Motion Components, Inc.** (fictional), a $48M maker of linear-motion parts, and its **Cell 7** precision-machining profit center. All figures are illustrative. A flat 25 % tax rate is used for teaching. It is not any jurisdiction's actual rate.

## Modules

| # | Module | Body of knowledge |
|---|---|---|
| 00 | [Introduction](modules/00-introduction.md) | Finance vs accounting, the accounting equation, profit vs cash |
| 01 | [Business organization](modules/01-business-organization.md) | Legal forms; cost, revenue, profit and investment centers; transfer prices |
| 02 | [Balance sheet](modules/02-balance-sheet.md) | Assets, liabilities, equity, working capital, book vs market value |
| 03 | [Income statement](modules/03-income-statement.md) | Gross profit, EBIT, EBITDA, net income, where engineers move the numbers |
| 04 | [Cash flow](modules/04-cash-flow.md) | Indirect method, free cash flow, working capital as a lever |
| 05 | [Ratio analysis and dashboard](modules/05-ratio-analysis-dashboard.md) | Profitability, efficiency, liquidity, leverage, DuPont, dashboard design |
| 06 | [Budgets](modules/06-budgets.md) | Operating, static and flexible budgets; variance analysis |
| 07 | [Time value of money](modules/07-time-value-of-money.md) | PV, FV, annuities, effective rates, loan amortization |
| 08 | [Sources and cost of capital](modules/08-sources-and-cost-of-capital.md) | Loans, bonds, leases, stock, bond pricing, CAPM, WACC |
| 09 | [Investment analysis and ROI](modules/09-investment-analysis-roi.md) | Accounting ROI, payback, NPV, IRR, profitability index |
| 10 | [Capital investment analysis](modules/10-capital-investment-analysis.md) | After-tax incremental cash flows, depreciation tax shield, lease vs buy, replacement |
| 11 | [Economic analysis](modules/11-economic-analysis.md) | Sensitivity, break-even value, scenarios, Monte Carlo, equivalent annual cost |
| 12 | [Break-even analysis](modules/12-break-even-analysis.md) | Contribution margin, margin of safety, operating leverage, automation and make-vs-buy |
| 13 | [Valuation, mergers, new ventures](modules/13-valuation-mergers-new-ventures.md) | DCF, multiples, acquisition synergies, funding a new enterprise |
| 14 | [Capstone and skill check](modules/14-capstone.md) | Profit-center package; 10-question check |

**Suggested schedule:** Day 1 covers modules 00–06 (statements, dashboard, budget). Day 2 covers modules 07–14 (investment decisions).

## Related courses

- [Introduction to Industrial Engineering](../introduction-to-industrial-engineering/README.md): work standards and job evaluation, which feed standard costs (Module 06)
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md): cost of poor quality, and the inventory and flow levers that free cash (Module 04)
- [Design of Experiments](../design-of-experiments/README.md): choosing operating levels by cost

## Getting started

```bash
pip install -r requirements.txt
python tools/finkit.py all          # every worked example
python tools/finkit.py data         # rewrite data/*.csv
python tools/make_figures.py        # regenerate figures/
```

Every calculation also works in a spreadsheet. Each module gives the matching formulas.

## Folder map

```
modules/     lessons
tools/       finkit.py (calculations), make_figures.py
data/        statements, loan schedule, project cash flows, budget vs actual (CSV)
figures/     charts used in the lessons
solutions/   key results + teaching notes
reference/   formulas, glossary, further reading
templates/   budget, dashboard definitions, capital request
```

## Disclaimer

This course teaches general concepts with fictional data. It is not accounting, tax, legal or investment advice. Use your organization's policies and its finance staff for real decisions.

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
