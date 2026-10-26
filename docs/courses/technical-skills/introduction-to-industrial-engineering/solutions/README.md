# Solutions and Instructor Notes

Module checks and the skill-check answers are inside the modules. Running-case results (regenerate with `python tools/ie.py all`):

| Item | Result |
|---|---|
| Time study | Normal 53.47 s; standard 61.49 s (1.025 min) with 15% PF&D; 58.5 kits/h |
| Cycles needed (±5%, 95%) | 2–3 per element (10 taken) |
| Work sampling (n = 400) | Productive 71%; waiting 11.5% (CI 8.4–14.6%); walking 7.5%; 879 obs for ±3 pts |
| Learning curve (85%, 4.0 min) | Unit 8: 2.46 min; unit 128: 1.28 min; first 100 kits 175 min |
| Staffing | 2,600 kits/shift × 61.49 s / (27,000 s × 0.90) = 6.58 → 7 per shift |
| NIOSH | Before RWL 5.71 kg, LI 2.45; after RWL 15.24 kg, LI 0.92 |
| Anthropometry | Adjustable bench ≈ 84–112 cm (illustrative data) |
| Layout | 13,890 → 7,170 trip-m/day (−48%) |
| Job evaluation | Points 220 (packer) to 415 (maintenance tech) |
| Wage line | Pay = 4.23 + 0.0626 × points, R² 0.94; team leader −7.6% |
| Incentives (680 kits, 0.81 std min) | 9.18 std h (115%): day $148.00; standard hour $169.83; Halsey $158.92; Rowan $167.02 |

## Teaching notes

- **Module 4:** have learners time a simple task (e.g., assembling a pen) in pairs and compare ratings — the rating spread is the lesson.
- **Module 6:** use the official NIOSH frequency and coupling tables with learners' own lifts; the FM and CM values in the case are assumed.
- **Module 7:** change one from–to value (e.g., QC ↔ Packing to 200) and rerun `best_layout()` to show how the optimum moves.
- **Module 10:** discuss why incentive plans are now less common in many industries and what replaced them (gainsharing, skill-based pay, team bonuses).
- Values labeled illustrative or assumed (anthropometric data, NIOSH FM/CM, the post-improvement standard of 0.81 min) are teaching values, not reference data.
