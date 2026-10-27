# Solutions and Facilitator Notes

All values come from `python tools/qekit.py all`, using data generated with seed 1924 by `python tools/qekit.py data`.

## Key results

| Example | Result |
|---|---|
| Rolled throughput yield (01) | 0.999 per step: 100 steps → 90.5 %, 1,000 steps → 36.8 %. Yield falls below 50 % after 693 steps |
| Descriptive (02) | OD mean 6.36273, SD 0.00709, 95 % CI 6.36210 to 6.36337 |
| Pareto (02) | 40 of 480 defective (8.33 %). Oversize 50 % and thread damage 27.5 % |
| Distribution (02) | Quote turnaround: lognormal is best by AIC (887.3 vs 935.9 for normal). 95th percentile: 43.5 h (lognormal) vs 40.2 h (normal); 43.4 h from the data |
| Cleansing (02) | 41 → 40 rows, 38 usable values. Issues: 1 duplicate, 1 missing, 1 zero, 1 decimal slip, 2 bad labels |
| Gauge R&R (03) | % study variation: repeatability 9.5, reproducibility 13.5, total GRR 16.5. % tolerance 23.7. ndc 8. Ben reads about 0.002 mm high |
| Attribute MSA (03) | Kappa vs standard: Dee 0.71, Eli 0.61, Fay 0.46. All inspectors agree with the standard on 40 % of parts |
| Sample size (03) | 49 inserts (±0.002 mm), 193 (±0.001). Defect rate: 457 (±2 points), 1,825 (±1 point) |
| Baseline (03) | DPU 0.0833, DPMO 16,667, sigma level 3.63, OD Ppk 0.577 |
| I–MR transform (04) | Raw data: LCL −14.7 h and 2 points outside. Log scale: 0 points outside; back-transformed limits 3.2 to 102.9 h |
| Staged p chart (04) | p̄ before 7.92 % (UCL 13.15 %), after 0.33 % (UCL 1.62 %) |
| Capability (04) | M1 Ppk 0.92; M2 Ppk 0.47 (8.1 % expected out of spec). Pp ≈ 1.4 on both machines |
| Stratify (05) | 19 of 20 oversize parts from M2 (χ² p = 0.0001). M2-B is worst at 13.8 % |
| Regression (05) | Tool age 0.0051 mm per 1,000 parts. Multiple-regression R² 0.64 |
| FMEA (05) | Oversize RPN 210, thread damage 192, undersize 135 (S = 9, review) |
| Reliability (05) | Series system R(720 h) 0.657, MTBF 1,714 h. With a redundant chiller, R = 0.797 |
| Pilot (06) | Oversize 7.92 % → 0.33 %. z = 11.5; 95 % CI for the reduction 6.5 to 8.8 points. Tooling $0.010 → $0.015 per insert (+50 %); cost per insert +1.3 %; scrap avoided $0.042 and net saving $0.037 per insert made |

## Exercise answers

**Exercise 0.1** is open-ended. A good answer classifies each activity by the test in module 00 (a decision about a unit or batch is control; confidence held by someone else is assurance; a process that performs better is improvement) and notices that most organisations spend the least on improvement.

**Exercise 1.1.** (1) Problem statement: "In the 20 days to day 20, 12.5 % of inserts sampled from lathe M2 were defective, 19 of its 30 defectives oversize OD, against a customer requirement of under 1 %; M1 ran at 4.2 %." (2) The secondary metrics are cycle time and tooling cost; both appear in module 06's side-effect check. (3) Rolled throughput yield at 99.5 % per step over 12 steps = 0.995¹² = 94.2 %, so about 1 insert in 17 fails at least one step.

**Exercise 2.1.** (1) M1: mean 6.35882, SD 0.00586; M2: mean 6.36664, SD 0.00597. M2 is further from target, by 0.0166 mm against M1's 0.0088 mm. (2) M2 only: oversize OD 19, burr 5, thread damage 4, knurl incomplete 2 (30 of 240 defective, 12.5 %). Oversize dominates even more; thread damage drops to third because M1 has most of it (7 of 11). (3) The 95 % CI for M2's mean, 6.36588 to 6.36740 mm, says where M2's long-run mean most likely is: well above 6.350. It says nothing about individual inserts or about the spread.

**Exercise 3.1.** (1) Part 1: Ana 6.33377, Ben 6.33473, Cai 6.33347; part 10: Ana 6.36797, Ben 6.37157, Cai 6.36960. Ben reads high on both, by about 0.001 mm on part 1 and 0.0036 mm on part 10; across all ten parts his excess over the other two operators runs from 0.001 to 0.004 mm with no clear trend with size (it is 0.0043 on part 6 and 0.0010 on part 8). So the offset is a consistent high reading of roughly 0.002 to 0.003 mm, not a size-dependent one, which points at measuring force or technique rather than a linearity fault or a zero error; the fix is the measuring method, not re-zeroing. (2) Dee's two trials disagree on parts 3, 9, 15, 22 and 23; all five are among the 18 parts where inspectors disagree with each other, the borderline set. (3) n = (1.96 × 0.00709 / 0.0015)² = 85.9, so 86 inserts.

**Exercise 4.1.** (1) M1 Ppk = min(6.375 − 6.35882, 6.35882 − 6.325) / (3 × 0.00586) = 0.01618 / 0.01758 = 0.92 (Ppk, because the overall standard deviation is used; Cpk would use the within-subgroup σ). Centered at 6.350 with the same spread, Ppk would equal Pp = 0.050 / (6 × 0.00586) = 1.42. (2) 0.0033 × 180 = 0.59 oversize inserts per day; with fewer than about 5 expected events the normal approximation behind the p-chart limits breaks down, so a single oversize insert (0.56 %) looks like a third of the way to the limit and two in a day (1.1 %) nearly a signal. (3) A p chart (or np chart, since 1 in 25 gives a constant subgroup size): the fraction of gauged inserts that fail the go/no-go check.

**Exercise 5.1.** (1) Coolant: A 24.0 °C, B 23.9 °C, C 27.1 °C. Tool age: A about 720 parts, B about 1,690, C about 720. Shift B's oversize points at tool wear (oldest tools); shift C's points at coolant temperature (hot coolant, fresh tools); shift A has neither and is lowest on both machines. (2) 12 of M2's 19 oversize inserts (63 %) were made with tools older than 1,600 parts, although only 24 % of M2's inserts were; 17 of 19 were older than 1,200. A 1,600-part interval removes most of the exposure, and the offset step every 400 parts covers the rest. (3) Example: thread damage → the tap is dull or chipped (verifiable: tap age at the time of the defect) → because taps are changed on complaint, not on a count. A second chain: thread damage "found" → the inspector's visual call is wrong (verifiable with the attribute MSA: Fay's kappa 0.46) → because there is no photo standard for borderline threads.

**Exercise 6.1.** (1) Break-even reduction = extra tooling / scrap cost per oversize insert = 0.005 / 0.55 = 0.0091, about 0.9 percentage points. The low end of the confidence interval is 6.5 points, seven times the break-even. (2) At $60 per edge: tooling $0.025 before and $0.0375 after, extra $0.0125 per insert; net saving $0.0417 − $0.0125 = $0.029 per insert. Still worth it; the decision does not change until a tool edge costs about $200. (3) Example: 1. Stop the cycle at the end of the current part. 2. Read the chiller display; if above 26 °C, tag the machine "hold" and call maintenance. 3. Quarantine every insert since the last in-limit X̄ subgroup. 4. Do not restart until the temperature reads 24 ± 2 °C for 15 minutes and a first-piece check passes. 5. Record the event on the chart.

## Facilitator notes

- **Session 01:** let teams write the charter for their own problem. Most first drafts state a solution in the problem statement.
- **Session 02:** the dirty-data exercise works well as a 15-minute competition: find all the issues.
- **Session 03:** run a live gauge R&R with calipers and 10 parts. The ANOVA in `qekit.py` takes any CSV in the same format. Expect debate on the kappa bar: the AIAG baseline puts Dee in its conditional band and the course's stricter bar does not accept her; the point is to make the team decide what miss rate the customer would accept.
- **Session 04:** contrast the raw and log-scale I-charts of turnaround times, then raise the Wheeler position: would you leave the raw chart and live with two signals?
- **Session 05:** build the fishbone before showing the stratification results. Then mark each cause as verified or not verified.
- **Session 06:** debate "buy a new lathe" against the low-cost actions using the capability numbers (spread is fine; centering isn't). Then run the tooling-cost break-even as a group.
- **Guideline values** (gauge R&R 10 %/30 %, kappa bands, the 1.5σ shift) are conventions; the course states the industry baseline and its own bar separately. Check your customer and industry requirements.
