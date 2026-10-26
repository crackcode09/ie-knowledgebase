# Module 08 — Sources of Capital and the Cost of Capital

## Objectives

- Compare internal funds, debt (loans, bonds), leases and equity as sources of capital.
- Price a bond and read its yield.
- Estimate the cost of debt, the cost of equity (CAPM) and the weighted average cost of capital (WACC).

## Sources of capital

| Source | What it is | Cost / burden | Notes for a manager |
|---|---|---|---|
| Internal funds | retained cash flow | opportunity cost of equity | the first source; limited by free cash flow |
| Trade credit | supplier payment terms | often "free", but early-pay discounts can be expensive to skip | see Module 07 question 2 |
| Bank term loan | fixed schedule, often secured by the equipment | interest (tax-deductible); covenants (e.g. max debt/EBITDA) | common for machines |
| Revolving credit line | borrow and repay as needed | interest on drawn balance, commitment fee | funds working capital |
| Bonds | debt sold to investors, coupon + face value at maturity | interest; covenants | larger firms |
| Leases | pay to use an asset | lease payments; lessor keeps residual risk | Module 10 compares lease vs buy |
| Preferred stock | fixed dividend, ranks ahead of common | dividends not tax-deductible | hybrid |
| Common stock | ownership | highest required return; dilutes owners | new enterprises, growth, acquisitions |
| Government grants / incentives | economic-development, energy-efficiency or training programs | compliance requirements | worth checking for capital projects |

**Debt is cheaper than equity** — lenders get paid first and interest is tax-deductible — **but more debt raises financial risk**: fixed payments must be met in bad years. The mix is the firm's capital structure.

## Bond pricing

A bond's price is the present value of its coupons and face value at the market yield.

Riverbend's 10-year bond: $1,000 face, 6 % annual coupon ($60), market yield 7 %:

Price = 60 × [1 − 1.07^−10] / 0.07 + 1,000 / 1.07^10 = 421.41 + 508.35 = **$929.76**

The bond trades below face (at a discount) because its coupon is below the market rate. **When rates rise, bond prices fall.** The yield the market demands (7 %) — not the coupon — is the company's current pre-tax cost of debt.

## Cost of capital

| Component | Riverbend (illustrative inputs) |
|---|---|
| Pre-tax cost of debt k_d | 7.0 % (market yield) |
| After-tax cost of debt k_d (1 − t) | 7.0 % × 0.75 = **5.25 %** |
| Cost of equity by CAPM: k_e = r_f + β (market risk premium) | 4.0 % + 1.2 × 5.5 % = **10.6 %** |
| Market value of equity E | $30.0M |
| Market value of debt D | $12.0M |
| Weights E/V, D/V | 0.714, 0.286 |
| **WACC** = (E/V) k_e + (D/V) k_d (1 − t) | 0.714 × 10.6 % + 0.286 × 5.25 % = **9.07 %** |

The risk-free rate, beta and market risk premium above are **teaching values**, not current market data. In practice, finance staff set them (typically from current government bond yields and comparable-company betas) and publish a hurdle rate.

**Use the WACC for projects with average risk** for the company. Riskier projects (a new product, a new market) deserve a higher rate; routine cost-saving projects sometimes a lower one. Many firms set a **hurdle rate** above WACC to allow for forecast optimism.

## Financing vs investment decisions

Keep them separate. First ask whether the project earns more than the cost of capital (Modules 09–10). Then decide how to fund it. Discounting a project's cash flows at the loan rate just because "we'll borrow for it" understates risk: the loan is backed by the whole company, not the project.

## Run it

```bash
python tools/finkit.py wacc
```

## Check yourself

1. If the market yield on Riverbend's bond fell to 6 %, what would the bond price be?
2. Why is the after-tax cost of debt used in WACC?
3. Riverbend borrows heavily so D/V = 0.5. Does WACC fall to 0.5 × 10.6 % + 0.5 × 5.25 % = 7.9 %?

<details><summary>Answers</summary>

1. $1,000 — at par, because coupon equals yield.
2. Interest is deductible, so each dollar of interest costs (1 − t) after tax. Project cash flows are also after tax, so the rate must match.
3. Probably not by that much. More debt makes equity riskier (beta rises) and lenders demand more, so both k_e and k_d go up. Leverage lowers WACC only up to a point.

</details>
