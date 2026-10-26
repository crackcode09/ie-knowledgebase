# Solutions and Facilitator Notes

All values come from `python tools/qekit.py all`, using data generated with seed 1924.

## Key results

| Example | Result |
|---|---|
| Rolled throughput yield (01) | 0.999 per step: 100 steps → 90.5%, 1,000 steps → 36.8%. Yield falls below 50% after 693 steps |
| Descriptive (02) | OD mean 6.36273, SD 0.00709, 95% CI 6.36210 to 6.36337 |
| Pareto (02) | 40 of 480 defective (8.33%). Oversize 50% and thread damage 27.5% |
| Distribution (02) | Quote turnaround: lognormal is best by AIC (887.3 vs 935.9 for normal). 95th percentile: 43.5 h (lognormal) vs 40.2 h (normal) |
| Cleansing (02) | 41 → 40 rows, 38 usable values. Issues: 1 duplicate, 1 missing, 1 zero, 1 decimal slip, 2 bad labels |
| Gauge R&R (03) | %SV: repeatability 9.5, reproducibility 13.5, total GRR 16.5. %Tolerance 23.7. ndc 8. Ben reads high |
| Attribute MSA (03) | Kappa vs standard: Dee 0.71, Eli 0.61, Fay 0.46. All inspectors agree with the standard on 40% of parts |
| Sample size (03) | 49 parts (±0.002 mm), 193 (±0.001). Defect rate: 457 (±2 pts), 1,825 (±1 pt) |
| Baseline (03) | DPU 0.0833, DPMO 16,667, sigma level 3.63, OD Ppk 0.577 |
| I–MR transform (04) | Raw data: LCL −14.7 h and 2 points outside. Log scale: 0 points outside; back-transformed limits 3.2 to 102.9 h |
| Staged p chart (04) | p̄ before 7.92% (UCL 13.15%), after 0.33% (UCL 1.62%) |
| Capability (04) | M1 Ppk 0.92; M2 Ppk 0.47 (8.1% expected out of spec). Pp ≈ 1.4 on both machines |
| Stratify (05) | 19 of 20 oversize parts from M2 (χ² p = 0.0001). M2-B is worst at 13.8% |
| Regression (05) | Tool age 0.0051 mm per 1,000 parts. Multiple-regression R² 0.64 |
| FMEA (05) | Oversize RPN 210, thread damage 192, undersize 135 (S = 9, review) |
| Reliability (05) | Series system R(720 h) 0.657, MTBF 1,714 h. With a redundant chiller, R = 0.797 |
| Pilot (06) | Oversize 7.92% → 0.33%. z = 11.5; 95% CI for the reduction 6.5 to 8.8 points |

## Facilitator notes

- **Session 01:** let teams write the charter for their own problem. Most first drafts state a solution in the problem statement.
- **Session 02:** the dirty-data exercise works well as a 15-minute competition: find all the issues.
- **Session 03:** run a live gauge R&R with calipers and 10 parts. The ANOVA in `qekit.py` takes any CSV in the same format.
- **Session 04:** contrast the raw and log-scale I-charts of turnaround times. Learners often want to "investigate" the two raw-scale signals.
- **Session 05:** build the fishbone before showing the stratification results. Then mark each cause as verified or not verified.
- **Session 06:** debate "buy a new lathe" against the low-cost actions using the capability numbers (spread is fine; centering isn't).
- **Guideline values** (gauge R&R 10%/30%, kappa bands, the 1.5σ shift) are conventions. Check your customer and industry requirements.
