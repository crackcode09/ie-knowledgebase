# Solutions and Teaching Notes

All values come from `python tools/finkit.py all`. Dollar amounts in the statements are in $000.

## Key results

| Example | Result |
|---|---|
| Statements (02–03) | Y2 revenue 48,000; EBIT 5,100; net income 3,150; total assets 34,300 = liabilities 18,250 + equity 16,050 |
| Cash flow (04) | CFO 4,250; capex 3,100; CFF −600; cash +550; FCF 1,150 |
| Ratios (05) | ROE 21.1 % = 6.56 % × 1.466 × 2.194; CCC 92.3 days (up from 90.3); debt/EBITDA 1.71 |
| Budget (06) | Static 184,000 → actual 190,700 (+6,700 F); vs flexible −33,860 U; volume +40,560 F; price −16,800 U |
| TVM (07) | Loan payment $23,761.44/month; total interest $225,686 |
| WACC (08) | Bond $929.76; k_d after tax 5.25 %; k_e 10.6 %; WACC 9.07 % |
| Investment (09) | NPV +$398,094; IRR 16.94 %; payback 4.10 yr; discounted payback 5.37 yr; PI 1.29; accounting ROI 20.5 % |
| Lease vs buy (10) | PV cost of buying −955,132 vs leasing −1,063,733; buying cheaper by 108,600 |
| Economic analysis (11) | Break-even savings $274,289; Monte Carlo P(NPV < 0) 3.8 %; EAC X 428,455 vs Y 381,921 |
| Break-even (12) | 18,225 units; margin of safety 54.4 %; DOL 1.84; automation indifference 28,571 units |
| Valuation (13) | EV 54,578; equity 45,228; TV 75 % of EV; Kestrel walk-away price 10,839; venture peak need 2,600 |

## Teaching notes

- **Modules 02–04 are one story.** Have learners trace net income into retained earnings and the cash-flow statement into the change in cash. The code asserts that the balance sheet balances, so a learner who changes an input sees it still balance.
- **Module 05:** ask "Was Y2 a good year?" before showing the ratios. Most people say yes on profit alone; the working-capital ratios add nuance.
- **Module 06:** the "beat the budget" headline hides a $33,860 miss against the flexible budget. Learners from operations often have not seen a flexible budget before.
- **Module 09:** run the payback-rule question as a debate. Payback is 4.1 years against a 4-year rule, yet NPV is strongly positive.
- **Module 11:** the Monte Carlo mean NPV ($311k) is below the base case ($398k). Use it to show that "most likely" inputs do not give the expected value.
- **Module 13:** the new-venture NPV flips from −$290k to +$5.56M once a terminal value is included. Discuss how much faith to put in year-6-and-beyond forecasts.
- **Substitute local numbers.** The tax rate, cost of capital inputs, lease quote and cost model are illustrative. Ask learners to replace them with their company's figures.
