# Solutions and Facilitator Notes

All values come from `python tools/aikit.py all` (data seed 2031).

## Key results

| Example | Result |
|---|---|
| Sizing (02) | Invoice matching ≈ $95,600/yr; ticket triage $38,800/yr |
| Portfolio (04) | Median value $62,900. Implement: #9 forecasting $128k, #1 invoices $96k, #10 late deliveries $80k, #11 doc search $72k. Challenge: #6 predictive maintenance $187k (feasibility 2.33), #7 vision. 4 ideas → fix the process first |
| Late-delivery model (03) | Test late rate 24.7 %; AUC 0.715. Best threshold 0.15: 128 of 148 caught, precision 0.30, $13,840 vs simple rule $11,440 (+21 %) |
| Data readiness (06) | 618 rows; 18 duplicates; 9 invalid dates; 11 label variants for 5 categories; 68 missing customer IDs; 31 missing and 4 negative resolution times; **labels 60.8 %** |
| GenAI pilot (05) | 73.3 % correct (CI 61–83 %), fabricated sources 3.3 % (0.9–11 %): fails both criteria. 80.8 % correct when the answer is in the documents vs 25 % when it isn't |
| Business case (07) | Cash flows −60,000 / 11,820 / 45,294 / 50,076; NPV $25,801; payback year 3; every factor in the tornado can turn the NPV negative |

## Facilitator notes

- **Module 01:** ask participants to classify their own "AI" examples. Many turn out to be rules or analytics.
- **Module 02:** insist on a number in every problem statement.
- **Module 03:** the "accuracy is useless" point lands best when groups first guess the model's accuracy.
- **Module 04:** build the PICK chart on a wall with sticky notes; move ideas as data readiness is discussed.
- **Module 05:** use real anonymized examples of fluent but wrong GenAI output from participants' experience.
- **Module 06:** the label-availability finding is the key lesson: the fix is a process change at ticket closure.
- **Throughout:** avoid recommending specific vendors or products. Focus on problem, data, risk and measures.
