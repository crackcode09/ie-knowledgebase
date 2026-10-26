# Module 10 — Capital Investment Analysis: Cash Flows, Taxes and Lease vs Buy

## Objectives

- Turn an engineering proposal into after-tax incremental cash flows.
- Handle depreciation, working capital, salvage and taxes correctly.
- Compare leasing with buying.
- Write a capital appropriation request.

## The rules for project cash flows

1. **Incremental only** — cash flows that change because of the decision. Compare "with project" to "without project".
2. **Cash, not profit** — depreciation is not a cash flow, but its **tax shield** is (depreciation × tax rate).
3. **After tax.**
4. **Ignore sunk costs** — money already spent on a study or a prototype is gone either way.
5. **Include opportunity costs** — floor space that could be rented, a machine that could be sold.
6. **Include working capital** — spares, tooling inventory, receivables from new sales; usually recovered at the end.
7. **Exclude financing costs** — interest is captured in the discount rate (Module 08).
8. **Include side effects** — savings elsewhere in the plant, or lost sales from a product it replaces.

## Building the cash flows for the 5-axis machine

**Year 0 (investment):**

| Item | $ |
|---|---|
| Machine | −1,200,000 |
| Installation and training (capitalized) | −100,000 |
| Working capital | −60,000 |
| **Total** | **−1,360,000** |

**Years 1–7 (operating cash flow):**

OCF = savings × (1 − t) + depreciation × t
= 380,000 × 0.75 + 185,714 × 0.25 = 285,000 + 46,429 = **331,429**

Equivalent form: OCF = (savings − depreciation)(1 − t) + depreciation = 145,714 + 185,714 = 331,429 ✓

**Year 7 (terminal) extras:**

| Item | $ |
|---|---|
| Salvage $150,000, book value 0, gain taxed: 150,000 × 0.75 | +112,500 |
| Working capital recovered | +60,000 |
| Year-7 total = 331,429 + 112,500 + 60,000 | **503,929** |

**Depreciation method matters.** Tax rules in many countries allow accelerated depreciation (in the US, MACRS); faster deductions move tax savings earlier and raise NPV. Book depreciation in the financial statements often differs from tax depreciation. This course uses straight-line for clarity — ask your tax staff which schedule applies.

## Lease vs buy

The vendor offers a 7-year operating lease at **$235,000 per year, paid at the start of each year**. Riverbend keeps maintenance either way, so savings are the same in both cases and drop out. Compare only the financing-related cash flows, discounted at the **after-tax cost of debt** (5.25 %), because lease payments are a debt-like fixed obligation.

| | Buy | Lease |
|---|---|---|
| Year 0 | −1,300,000 | −176,250 (235,000 × 0.75) |
| Years 1–6 | +46,429 depreciation tax shield | −176,250 |
| Year 7 | +46,429 + 112,500 after-tax salvage | 0 |
| **PV of costs at 5.25 %** | **−955,132** | **−1,063,733** |

**Buying is $108,600 cheaper** in present-value terms. Leasing can still win when the company is short of cash or borrowing capacity, the technology will be obsolete soon (the lessor takes residual risk), or the lessor can use tax benefits the company cannot. Accounting standards now put most leases on the balance sheet, so leasing no longer "hides" debt.

(Simplification: lease tax deductions are assumed to occur when the payment is made.)

## Replacement decisions

For replacing an existing machine, the incremental view includes:

- sale value of the old machine now (and tax on any gain or loss vs its book value);
- the old machine's remaining depreciation tax shield, which is **lost**;
- the difference in operating costs, reliability and capacity;
- the old machine's salvage at the end, which is **forgone**.

When lives differ, compare with equivalent annual cost (Module 11).

## The capital appropriation request

A good request (template: `templates/capital-request.md`) contains:

1. Need and alternatives considered (including "do nothing").
2. Assumptions with sources: quotes, time studies, scrap data.
3. Cash flow table, NPV, IRR, payback.
4. Sensitivity and risks (Module 11).
5. Non-financial factors: safety, quality, capacity, strategic fit.
6. A post-audit plan: how and when actual savings will be measured.

## Run it

```bash
python tools/finkit.py capital
python tools/finkit.py leasebuy
```

## Check yourself

1. Engineering spent $40,000 on a feasibility study last year. Does it belong in the cash flows?
2. The machine frees 400 ft² that can be rented to a neighbor for $12,000 a year. How is that treated?
3. Why discount the lease-vs-buy flows at 5.25 % rather than the WACC?

<details><summary>Answers</summary>

1. No. It is sunk — spent whatever is decided now.
2. As an incremental benefit of $12,000 × (1 − t) = $9,000 a year after tax (or, if the space would otherwise be rented, as an opportunity cost of not doing the project).
3. Lease payments, like loan payments, are fixed contractual obligations with debt-like risk. The operating savings, which are riskier, are common to both options and have already dropped out.

</details>
