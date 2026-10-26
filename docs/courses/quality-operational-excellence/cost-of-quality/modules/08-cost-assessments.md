# Module 08 — Cost Assessments: Collecting the Data

## Objectives

- Plan a first cost-of-quality assessment.
- Collect cost data from accounts, estimates and studies.
- Reconcile, validate and set up ongoing tracking.

## Plan the assessment

1. **Sponsor and partner with finance** from the start — their credibility makes the result usable.
2. **Choose scope** — one plant, one product line or one process first.
3. **Choose the period** — typically the last 6–12 months.
4. **Agree the element list and category rules** (Module 02).
5. **Identify sources** for each element.

## Sources of cost data

| Source | Elements typically found | Notes |
|---|---|---|
| General ledger accounts | scrap (if booked), warranty, calibration contracts, training | easiest; often incomplete |
| Labor reporting / time tracking | rework, inspection, MRB | depends on coding discipline |
| Quality records (NCRs, MRB logs, complaints) | events, quantities | multiply by standard costs |
| ERP scrap and rework transactions | quantities and standard costs | check valuation method |
| Estimates from interviews | engineering firefighting, sorting | document assumptions |
| Work sampling / time studies | hidden rework, inspection time | statistically defensible |
| Customer and sales records | returns, credits, lost orders | |

**Work sampling example:** observe 6 engineers at random moments over 4 weeks; if 22 % of observations show firefighting quality problems, and their loaded cost is $105,000/yr each, firefighting ≈ 0.22 × 6 × $105,000 ≈ $139,000/yr — the basis of Ellison's $140,000 estimate.

## Event-level data

Wherever possible, collect **events** with cost, driver and detection point, not just account totals — this is what makes driver analysis (Module 09) possible. Ellison's `failure_events.csv` has 700 events for months 1–6; their total ($1,043,700) **reconciles** to the ledger's internal + external failure cost for the same months.

## Validate

- **Reconcile** to known totals (scrap account, warranty account).
- **Sanity check** ratios (CoQ % of sales, cost per unit) against your own history.
- **Review with owners** — the production manager should recognize the rework figure.
- **Document** sources and assumptions for every element.

## Set up ongoing tracking

- Monthly, aligned with the financial close.
- Use the tracker (`templates/coq-tracker.xlsx`) or add CoQ codes to accounting and labor reporting.
- Name an owner per element.
- Keep hidden-cost estimates on a separate sheet, refreshed quarterly.

## Check yourself

1. Why involve finance even if quality owns the CoQ program?
2. Your scrap account shows $400k, but NCR records × standard cost give $580k. What might explain the difference?

<details><summary>Answers</summary>

1. Finance validates numbers, knows where costs are booked, and gives the results credibility with management.
2. Scrap valued at material only in the account; scrap absorbed into variances; rework scrap not booked separately; NCR quantities including items later reworked or used as-is. Reconcile before reporting.

</details>
