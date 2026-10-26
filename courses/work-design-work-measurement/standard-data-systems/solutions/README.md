# Solutions and Facilitator Notes

All values come from `python tools/sdskit.py all` (data seed 1946). The Excel workbook gives the same coefficients; LibreOffice was used to check that it recalculates.

## Key results

| Example | Result |
|---|---|
| Micro build (01) | 4-bend, 1-flip part: 22.7 s manual + 18.0 s ram = 40.7 s (0.678 min) vs macro 0.702 min (−3.4 %) |
| Run model (02, 07) | Normal min/piece = 0.1863 + 0.0873·bends + 0.1184·flips + 0.0226·kg + 0.0535·m. R² 0.993, SE 0.049 min, n = 40 |
| Setup model (02, 07) | Normal min = 6.785 + 2.712·tool segments + 9.624·new program. R² 0.981, SE 1.21 min, n = 24 |
| Example lot (02) | 4 bends, 1 flip, 1.2 kg, 400 mm, 3 segments, 50 pcs: run 0.702, setup 14.92, lot 0.934 std h |
| Consistency (03) | Three analysts differ by 17.6 % on average per job; Analyst 2 lowest on every job |
| Economics (03) | 1,500 → 180 analyst h/yr; $72,600/yr saved; payback 2.9 months; break-even 73 new parts/yr |
| Correlation (06) | r with time: bends 0.879, flips 0.813, length 0.448, weight 0.358, thickness 0.155. Bends only: 0.413 + 0.1305·bends, R² 0.772, SE 0.26 |
| Model ladder (07) | SE 0.260 → 0.195 → 0.056 → 0.049; thickness p = 0.86 and raises LOO error; max VIF 1.75 |
| Transform (07) | Shear handling: 0.1205·kg^0.533 (log-log R² 0.994); linear model 20.9 % mean error on blanks < 2 kg vs 3.8 % |
| Evaluation (08) | S27 studentized residual 8.6 (3 bends keyed, 8 actual); fix takes SE from 0.087 to 0.049. PI for the example part 0.599–0.806 |
| Validation (08) | 12 hold-out jobs: mean abs. error 4.4 %, 11/12 within ±10 %, worst V12 +16.0 %, aggregate +0.7 % |
| Apply (09) | Week: 49.91 std h vs 55.49 actual (89.9 %); load 78.3 % of 63.75 h; setup 26 %; W25 72.7 %, W28 75.3 %; W02, W15, W16 out of range; W01 quote $62.76 ($2.51/pc) |
| Capstone (10) | Exclude T14 (tool jam). 0.6318 + 0.00389·hits + 0.1476·stations + 0.0316·kg, R² 0.979, SE 0.14; hold-out MAE 2.5 %, aggregate +2.2 %; job 2.913 normal min/sheet, 40 sheets = 2.175 std h |

## Facilitator notes

- **Module 01:** stress that the motion table is course-made. If the group has licensed PMTS analysts, have them rebuild the element in their system and compare.
- **Module 03:** let learners time-study the same video clip and compare their standards before showing the analyst-consistency figure.
- **Module 06:** run the regression in Excel live, once with `LINEST` and once with the ToolPak, so learners can map one onto the other.
- **Module 07:** ask the group to predict, before fitting, which variables will matter and the sign of each.
- **Module 08:** give the uncorrected data first (`RunStudies!B28` = 3 in the workbook) and let learners find S27 themselves.
- **Module 09:** discuss the low-efficiency jobs as a problem-finding exercise, not a people-performance one.
- **Capstone:** learners who skip the notes column usually keep T14, so expect some answers with SE around 0.37. Use this to reinforce "read the study file".
