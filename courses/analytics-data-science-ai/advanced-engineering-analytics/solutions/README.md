# Solutions and Facilitator Notes

All values come from `python tools/aeakit.py all` (data seed 2028).

## Key results

| Example | Result |
|---|---|
| Merge (02) | 1,002 run rows; 3,000 lab tests. The naive join gives 3,006 rows (fan-out). The clean analysis table has 1,000 runs, one per row |
| Prepare (03) | 2 duplicates, 3 temperatures in °F, 2 missing pressures, 1 bad label, 4 missing lab tests. Seal temperature after cleaning: 150.5–177.0 °C |
| Describe (04) | L4: availability 82.7%, seal strength 20.94 N, 79 min downtime per run, on-time 58.6%. 5.9% of runs have a seal test below 18 N |
| ANOVA (05) | F 192.1, η² 0.367. All Tukey pairs differ. Supplier −0.99 N; interaction p 0.20 |
| Regression (06) | R² 0.760. Optimum temperature 174.9 °C. L4 still 2.45 N below L1 after adjusting for settings. Residual SD 0.94 N |
| Nonparametric (07) | Kruskal-Wallis p 0.0045. L4 median 164 min (bootstrap CI 111–273). Mann-Whitney scrap p 0.016 (negligible difference). Spearman ρ 0.54 |
| DOE (08) | Effects: temperature +2.16 N, pressure +2.21 N, dwell +1.41 N; AB +0.54 (p 0.08). Best cell 26.91 N |
| Seal-strength prediction (09) | CV RMSE: baseline 1.918 → settings 1.612 → + line and supplier 0.982 → + quadratic terms 0.956. Gradient boosting 1.025. Noise floor 0.924 |
| Failure prediction (09) | CV AUC: logistic raw 0.841, + trend features 0.856, random forest 0.848, gradient boosting 0.843 |
| Delivery (04) | 78.8% on time overall. By line: L1 84.5%, L2 78.1%, L3 91.8%, L4 58.6% |

## Facilitator notes

- **Module 02:** have learners do the naive join first and total the units. The tripled total makes the fan-out lesson stick.
- **Module 03:** give learners `production_workbook.xlsx` and ask them to find all five data problems before revealing the list.
- **Module 05:** discuss why η² matters more than p with 1,000 runs.
- **Module 09:** the punchline is that the best accuracy gain came from better information (line and supplier), not a fancier model. The noise floor ends the modeling debate.
- **Module 10:** if learners have a BI tool, have them rebuild the dashboard from the cleaned analysis table. The point is that grain mistakes from Module 02 reappear there too.
- **Delivery format:** the course works for classroom or livestream sessions. Run the Python demonstrations live, or share the figures.
