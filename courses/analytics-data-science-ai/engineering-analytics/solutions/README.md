# Solutions and Facilitator Notes

All values come from `python tools/anlkit.py all`, using data generated with seed 2027.

## Key results

| Example | Result |
|---|---|
| SQL (02) | 4,000 lines, $6.84M. Valves $5.06M (74%), tees $0.98M, elbows $0.80M. Discount 8.8–9.2% in every region |
| Describe (02) | 21,688 kWh/day mean, 4.20 kWh per unit. Customer revenue mean $103k vs median $67k (skew 2.38). Top 20% of customers bring 65.2% of revenue |
| Segmentation (03) | Silhouette is best at k = 3 (0.584). Segments: 38 key accounts (52.7% of revenue), 142 regular OEMs (43.6%), 120 occasional buyers (3.6%). Adjusted Rand index vs the true segments: 0.983 |
| ABC (03) | A: 100 SKUs, 79.9% of value. B: 156 SKUs, 15.1%. C: 244 SKUs, 5.0% |
| Classification (03) | Base rate 20.1%. Logistic AUC 0.843. At threshold 0.5, recall is 41.7%; at 0.25, 69.4%. Tree AUC 0.812. Expected cost at the two thresholds: $348,300 vs $203,900 |
| Regression (04) | kWh = 8,908 + 2.12·units + 2,362·third shift + 89.05·\|T − 15\|. R² 0.873, residual SD 702. Prediction 25,769 kWh (24,381 to 27,157) |
| PCA (05) | PC1 to PC3 explain 90.4% of variance. CV R² by number of PCs: 1 → 0.035, 3 → 0.827, 10 → 0.824 |
| Forecast (05) | Holdout MAPE: naive 12.93%, seasonal naive 7.69%, moving average 7.33%, SES 12.93%, Holt-Winters 2.21% |
| Optimization (07) | 700 / 600 / 60 kits, $28,260. CNC binding at $136.67/h. At 170 CNC h: $29,300 with assembly binding |

## Facilitator notes

- **Format:** the course is written for Python, with spreadsheet equivalents. In a 2-day class, demo the Python and let participants work in whichever tool they know. `data/ridgeway.xlsx` has the main tables.
- **Module 02:** a 20-minute SQL exercise. Give the star-schema diagram and ask for revenue by region and family. Any free SQLite browser works.
- **Module 03:** the most common learner error is judging the classifier by accuracy. Show the "never fails" baseline at 80% before showing the model.
- **Module 05:** let learners guess which PC predicts yield before revealing that PC1 doesn't.
- **Module 06:** keep vendor-neutral. Discuss each technology category, not product choices.
- **Module 07:** have learners re-solve the LP after changing one input. The sensitivity-range lesson (shadow prices hold only within a range) comes up naturally.
- **Capstone:** groups of 2–3 pick option A–E. Score with the Technical Communications rubric.
