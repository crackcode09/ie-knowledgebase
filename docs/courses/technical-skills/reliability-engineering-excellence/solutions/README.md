# Solutions and Facilitator Notes

All values come from `python tools/relkit.py all`, using data generated with seed 4242.

## Key results

| Example | Result |
|---|---|
| Pareto (05) | 88 work orders, 363.7 h of downtime, $121,740. Spindle (37.7%) and press (36.7%) together make 74.3% of downtime. Top 5 modes make 76.2% |
| Metrics (03) | Coolant pump MTBF 1,949 h, MTTR 3.29 h, A_i 99.83%, A_o 99.53% (6 h delay), 28.6 h downtime per 6,000 h |
| Exponential (05) | 90% CI for MTBF 1,320 to 3,225 h. R(500 h) = 0.774. P(0/1/2+ failures per month) = 0.774 / 0.198 / 0.028 |
| Normal (05) | Wheel life 5,261 ± 361 parts. Change at 4,421 for 1% risk |
| Weibull (06) | β 1.81, η 8,778 h (MLE, 12 failures and 12 suspensions). B10 2,532 h. Rank regression gives 2.06 and 7,785 |
| RBD (02) | Series line 0.7172. With a standby pump 0.7889. 2-of-3 sensors 0.972 |
| Criticality (01) | A class: hydraulic press, grinder spindle. Air compressor flagged for individual review (worst consequence 5) |
| PM (09) | Optimum age 4,420 h at $2.127/h vs $2.819/h run-to-failure (−24.5%). About $4,200 per spindle per year |
| P-F (10) | P-F 1,200 h → inspect every 600 h, about 10 readings per year |
| LCC (07) | A $174,199 vs B $108,587. Incremental payback 1.10 yr, B/C 5.86, NPV +$65,612 |
| Optimum (07) | R ≈ 0.975 minimizes total cost in the illustrative model |
| Growth (02) | Crow-AMSAA β 0.595. Cumulative MTBF 90.9 h, instantaneous 152.8 h at 2,000 h |

## Independent checks

- The Weibull MLE was confirmed with SciPy's censored-data fit (`stats.weibull_min.fit` on `stats.CensoredData`, SciPy 1.18): β 1.81, η 8,778.
- The PM optimum was confirmed by a 10-hour grid search (4,420 h, $2.127/h).

## Facilitator notes

- **Day 1:** start with the work-order data in a spreadsheet. Ask "where would you start?" before showing the Pareto. Many groups pick the coolant system because it fails most often, but the spindle and press dominate downtime.
- **Module 04:** run the mini-RCM as a table exercise on a machine the learners know.
- **Module 06:** have learners fit the Weibull with the suspensions removed, or treated as failures, and compare. The bias is the lesson.
- **Module 07:** get a real cost-of-downtime figure from finance before the course if possible.
- **Module 09:** stress that the cost curve is flat near the optimum. Precision in the interval matters less than having the right strategy.
- **Module 11:** teams of 3–4. Score report-outs with the Technical Communications rubric.
- **Illustrative inputs** (costs, P-F interval, one-month reliabilities, the optimum-cost model) should be replaced with plant data where available.
