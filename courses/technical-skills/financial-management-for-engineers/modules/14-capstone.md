# Module 14 — Capstone and Skill Check

## Part A — Build your profit-center package

Pick a cell, line or department you know (or use Cell 7). Produce:

1. **Budget** for one quarter from volume and standard costs (`templates/budget-template.csv`), plus a flexible budget at a different volume.
2. **Dashboard** of 6–10 metrics with written definitions (`templates/dashboard-definitions.md`): at least three financial and three operational.
3. **Capital request** for one real improvement (`templates/capital-request.md`): incremental after-tax cash flows, NPV, IRR, payback, a tornado or break-even value for the two biggest drivers, and a post-audit plan.
4. **Break-even** analysis for the area, including what happens if volume falls 20 %.

**Review criteria:** a finance colleague can reproduce every number from your assumptions; assumptions have sources; the recommendation follows from NPV and risk, not from payback alone.

## Part B — Skill check (answers below)

1. Net income $500k, depreciation $200k, receivables up $150k, payables up $50k, capex $300k. What are CFO and free cash flow?
2. Revenue $10M, COGS $7M, inventory $1.4M. Compute DIO.
3. What is the present value of $20,000 a year for 10 years at 8 %?
4. A $500,000 loan at 6 % APR over 4 years, monthly payments. What is the payment?
5. After-tax cost of debt 4.5 %, cost of equity 12 %, 40 % debt / 60 % equity. WACC?
6. A project costs $200,000 and returns $60,000 a year for 5 years. NPV at 10 %? IRR roughly?
7. Name two flaws of simple payback.
8. Price $40, variable cost $25, fixed cost $300,000. Break-even units? Units for $150,000 profit?
9. Static budget profit $50,000 at 5,000 units; flexible budget at 5,500 units $58,000; actual $54,000. Split the variance.
10. Target FCF next year $2M, growing 3 %, WACC 10 %, net debt $5M. Equity value?

<details><summary>Answers</summary>

1. CFO = 500 + 200 − 150 + 50 = **$600k**; FCF = 600 − 300 = **$300k**.
2. 1.4 / 7 × 365 = **73 days**.
3. 20,000 × [1 − 1.08^−10] / 0.08 = **$134,202**.
4. r = 0.005, n = 48: 500,000 × 0.005 / (1 − 1.005^−48) = **$11,742.51**.
5. 0.4 × 4.5 % + 0.6 × 12 % = **9.0 %**.
6. NPV = −200,000 + 60,000 × 3.7908 = **+$27,447**; IRR ≈ **15.2 %**.
7. Ignores the time value of money; ignores cash flows after the payback date (and has no objective cutoff).
8. CM = 15; break-even = 300,000 / 15 = **20,000 units**; for $150k profit: 450,000 / 15 = **30,000 units**.
9. Volume variance 58,000 − 50,000 = **+$8,000 F**; performance (flexible vs actual) 54,000 − 58,000 = **−$4,000 U**; total **+$4,000 F**.
10. EV = 2 / (0.10 − 0.03) = $28.57M; equity = 28.57 − 5 = **$23.57M**.

</details>
