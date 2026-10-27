# Solutions and Facilitator Notes

All values come from `python tools/dalkit.py all` (data seed 2033).

## Key results

| Example | Result |
|---|---|
| Data quality (01) | 412 records. Completeness 91.0; validity 96.6; conformity 95.4; consistency 94.7; uniqueness 97.1 (12 duplicates); integrity 97.8; accuracy proxy 98.8; reasonableness 98.3; **timeliness 28.9** (all %) |
| EDA (02) | 4,000 orders, $1,328,506. Mean $332.13, median $295.06, SD $208.46, skew 1.12, 107 high outliers. East mean $371.26 vs South $305.06 (×1.217) |
| Apriori (02) | 60 frequent itemsets (12/40/8). 25 rules at confidence ≥ 0.5. Top rule: glasses + gloves → hearing protection (support 0.156, confidence 0.828, lift 2.52) |
| A/B test (02) | 8.50 % vs 10.92 %, +2.42 points, *z* = 2.00, *p* = 0.046, 95 % CI [0.05, 4.78] points |
| East vs South (02) | Welch *t* = 6.21, *p* = 6.9 × 10⁻¹⁰ |
| Regression (03) | SLR: 409.68 + 4.169 × marketing, R² 0.317. MLR: 120.97 + 3.91 × marketing + 22.559 × reps + 0.558 × accounts, R² 0.754 (adjusted 0.748) |
| Evaluation (03) | Holdout months 19–24: RMSE 24.8, MAE 20.4, MAPE 4.3 %; naive 54.8; 5-fold CV RMSE 26.2 |
| Churn (03) | Rate 11.5 %; test *n* 450. AUC: logistic 0.811, tree 0.787. At 0.5: TP 5, FP 1, recall 0.096. At 0.15: TP 31, FP 77, precision 0.287, recall 0.596. All-stay baseline accuracy 0.884 |
| Segments (03) | 139 / 173 / 42 / 46 customers; revenue share 48.6 / 38.3 / 7.4 / 5.7 % |
| Expected value (04) | Threshold 0.5 nets $2,010; 0.15 nets $9,630 (save rate 30 %). Break-even save rate 9.3 % |
| Bias (04) | Tenure: all 7.63 vs survivors 7.82. Tickets: survivors 1.42 vs churned 1.82 |

## Capstone model answer (outline)

1. **Frame.** Decision: where the account team and marketing spend their time next year. Measure: revenue from existing customers vs this year. Types: descriptive, predictive and prescriptive.
2. **Data.** Fix duplicates before RFM; flag that 71 % of contacts are unverified, a risk for any outreach plan.
3. **Describe.** Core accounts plus steady buyers make up 87 % of revenue. East's larger orders are worth investigating. The PPE kit and cutting-tool cross-sell rules give the offers.
4. **Test.** The reminder e-mail works (+2.4 points); roll it out to all segments.
5. **Predict.** A churn list at threshold 0.15, focused on the "slipping" segment.
6. **Decide.** Compare (a) the churn call list, (b) a PPE-kit cross-sell to steady buyers, (c) the reminder e-mail, by expected value. State the key assumption for each (save rate, attach rate, conversion lift).
7. **Tell.** One page: "Most growth is in customers we already have: three actions worth about $X." Include one chart and an owner for each action.

## Facilitator notes

- **Module 01:** have groups map one of their own processes and mark one NVA step that data could remove. Then score a real table on the 12 dimensions.
- **Module 02:** before showing the Apriori output, ask the group to guess which products go together. Experts usually get the PPE trio, but rarely the strength of the batteries–flashlights rule.
- **Module 03:** reveal the all-stay baseline only after someone praises the 89 % accuracy.
- **Module 04:** run the expected-value table live, changing the save rate. Participants should see the decision flip.
