# Solutions and Instructor Notes

Module check answers and the Module 11 quiz answers are inside the modules. Worked results for the running case (regenerate with `python tools/pmap.py all`):

| Item | Value |
|---|---|
| Steps VA / BVA / NVA | 3 / 5 / 6 |
| Work time VA / BVA / NVA | 117 / 65 / 43 min (225 min total) |
| Waiting | 274 h |
| Lead time | 277.8 h ≈ 11.6 calendar days |
| VA ÷ lead time | 0.70% |
| Handoffs | 9 |
| Spaghetti | 478 m → 232 m (−51%); 9 → 7 moves |
| Rolled %C&A | 35.3% |
| VOC turnaround (n = 120) | median 9 days; 25th pct 7; 10th pct 6; 5th pct 5 |
| Customers satisfied | 17% at 11.6 days; 86% at 7 days; 100% at 5 days |

## Teaching notes

- **Module 3:** learners often classify "write failure report" as VA. Ask: would the customer pay for the report format, or for the knowledge of why it failed? The diagnosis is VA; the report is BVA.
- **Module 4:** the after-layout keeps two trips between lab and bench; ask learners to propose a layout that removes them (e.g., diagnosis and repair at the same bench).
- **Module 10:** discuss who decides the share of customers to satisfy — it's a business decision, informed by VOC data and competitor offers, not a statistical one.
