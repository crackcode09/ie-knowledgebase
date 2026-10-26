# Module 13 — Business Valuation, Mergers and Financing a New Enterprise

## Objectives

- Value a business by discounted free cash flow and check it against market multiples.
- Value an acquisition including synergies, and set a walk-away price.
- Estimate how much funding a new venture needs.

## 1. Discounted cash flow (DCF) valuation

Enterprise value (EV) = PV of future **unlevered free cash flow** (cash from operations after tax and investment, before any financing), discounted at the WACC.

FCF = EBIT × (1 − t) + depreciation − capital expenditure − increase in working capital

Steps:

1. Forecast 5–10 years of FCF.
2. Add a **terminal value** at the end: TV = FCF_{n+1} / (WACC − g), with g a long-run growth rate no higher than the economy's.
3. Discount to today; that is EV.
4. **Equity value = EV − net debt** (debt − cash).

**Riverbend ($000).** Assumptions (illustrative): revenue growth 6 %, 6 %, 5 %, 4 %, 3 %; EBIT margin 11 %; depreciation 4.5 % and capex 5.5 % of revenue; working capital 20 % of revenue; WACC 9.07 %; terminal growth 2.5 %.

| Year | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| Revenue | 50,880 | 53,933 | 56,629 | 58,895 | 60,661 |
| NOPAT (EBIT × 0.75) | 4,198 | 4,449 | 4,672 | 4,859 | 5,005 |
| Free cash flow | 3,113 | 3,300 | 3,566 | 3,817 | 4,045 |

| Result | $000 |
|---|---|
| PV of 5-year FCF | 13,694 |
| Terminal value at year 5 = 4,045 × 1.025 / (0.0907 − 0.025) | 63,107 |
| PV of terminal value | 40,884 |
| **Enterprise value** | **54,578** |
| Net debt (12,300 − 2,950) | 9,350 |
| **Equity value** | **45,228** |

**75 % of the value is in the terminal value.** DCF results are very sensitive to WACC and terminal growth — always show a range.

## 2. Multiples cross-check

Comparable companies or recent deals are often quoted at a multiple of EBITDA. Our DCF implies **EV / EBITDA = 54,578 / 7,200 = 7.6×**. If comparable deals traded at 6–8× (an illustrative range), EV would be $43.2M–$57.6M — the DCF sits inside it. Multiples are quick but hide every assumption; DCF makes them explicit. Use both.

Other approaches: **asset-based** (adjusted book value — relevant for asset-heavy or liquidating businesses) and **comparable transactions**.

## 3. Mergers and acquisitions

Riverbend considers buying **Kestrel Bearings** (fictional), a small competitor.

| Item | $000 |
|---|---|
| Kestrel standalone: next-year FCF 600, growing 2 % → 600 / (0.0907 − 0.02) | 8,487 |
| Synergies: 250 a year pre-tax purchasing and overhead savings, after tax, as a growing perpetuity, less 400 one-time integration cost after tax | 2,352 |
| **Maximum (walk-away) price** | **10,839** |
| Seller asking price | 9,500 |
| Value retained by Riverbend at the asking price | 1,339 |

Paying more than standalone value means **giving the seller part of the synergies**. Synergy estimates tend to be optimistic and integration costs underestimated, so a buyer that pays close to the walk-away price has little room for error. Engineers are often asked to validate operational synergies (shared machines, consolidated plants, combined purchasing) — be the realist in the room.

Financing the deal: cash on hand, new debt (watch debt/EBITDA covenants) or new shares (dilution of existing owners).

## 4. Financing a new enterprise

Riverbend's engineers propose a **linear-actuator venture**. Forecast cash flows ($000):

| Year | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Cash flow | −2,000 | −600 | 200 | 900 | 1,300 | 1,500 |
| Cumulative | −2,000 | −2,600 | −2,400 | −1,500 | −200 | +1,300 |

- **Peak funding need: $2.6M** (end of year 1). With a 25 % contingency for delays: **$3.25M**. Running out of cash, not lack of profit, is what kills most new ventures.
- At a 15 % risk-adjusted rate, the five forecast years alone give NPV −$290k; including a terminal value (growth 2 %) gives +$5.56M. **The venture's value is almost all beyond year 5** — exactly where forecasts are weakest.

Funding options: parent-company capital, a bank loan (hard without assets or history), equipment financing, outside equity (angel or venture investors, strategic partners), grants. Stage the funding: release money in tranches tied to milestones (prototype, first customer, break-even month).

## Run it

```bash
python tools/finkit.py valuation
python tools/finkit.py merger
python tools/finkit.py startup
```

## Check yourself

1. If terminal growth is 3.5 % instead of 2.5 %, will EV go up or down, and why so much?
2. Why subtract net debt to get equity value?
3. Kestrel's owner raises the price to $11.5M. What should Riverbend do?

<details><summary>Answers</summary>

1. Up, sharply: the denominator (WACC − g) shrinks from 6.57 % to 5.57 %, raising the terminal value by about 19 %.
2. EV is the value of the whole operating business to all capital providers. Lenders are paid first; what's left after net debt belongs to shareholders.
3. Walk away (or renegotiate): $11.5M exceeds the $10.84M maximum, so the deal would destroy value even if every synergy is delivered.

</details>
