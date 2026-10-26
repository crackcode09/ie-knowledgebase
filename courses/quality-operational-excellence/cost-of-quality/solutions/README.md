# Solutions and Facilitator Notes

All values come from `python tools/coqkit.py all` (data seed 1951). A full generated report is in [coq-summary-report.md](coq-summary-report.md).

## Key results

| Example | Result |
|---|---|
| Summary (02) | CoQ $2,852,930 = 7.08% of $40.29M sales. P 10.5%, A 22.9%, IF 42.5%, EF 24.1% |
| Before/after (11) | $249,230 → $209,790 per month (7.53% → 6.07% of sales). Net saving $39,440/month, about $473,280/yr |
| Ratios (11) | Failure share of CoQ 69.8% (Jan) → 55.0% (Dec). Prevention share 7.2% → 19.8% |
| Failure elements (05) | Scrap $581,880, rework $421,300, warranty $320,030 |
| Drivers (09) | 700 events, $1,043,700 (reconciles to the ledger). Bore 28.8%, weld 23.5%, seal 21.6% |
| Internal vs external (06) | $970 vs $5,472 per event. 12% of events cause 42% of cost |
| Hidden (07) | $1,049,000/yr, 0.5× booked failure cost. True failure cost about $3.14M/yr |
| Loss function (07) | k = $288,000/mm². Expected loss per cylinder: $47.23 (offset), $18.43 (centred), $4.61 (centred, tight) |
| Projects (10) | Portfolio $218,000 one-time cost, about $1.13M/yr estimated saving. Fastest payback: port-orientation fixture, 1.1 months |
| Models (01) | Classic optimum at 97.1% conformance (illustrative); modern view: minimum at the 99.99% edge |

## Facilitator notes

- **Day 1 opener:** ask participants to guess their organization's CoQ as a % of sales. Revisit the guess at the end of Day 2.
- **Module 02:** the gray-area table is a good group exercise. Have tables categorize 10 items, then compare answers.
- **Module 07:** expect pushback on the hidden-cost estimates. Use it to teach separating booked costs from estimated ones.
- **Module 09:** show the count Pareto first, then the cost Pareto. The re-ranking is the key lesson.
- **Module 10:** discuss hard vs soft savings with a finance colleague present if possible.
- **Tracker:** have participants clear the sample data and enter three months of their own estimates during Day 2.
