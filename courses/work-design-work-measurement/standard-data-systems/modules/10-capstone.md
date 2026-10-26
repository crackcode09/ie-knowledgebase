# Module 10 — Capstone: Build a Standard Data Model

## Objective

Build, evaluate and apply a standard data model on your own, from raw studies to a standard for a new job.

## Brief

Harlan wants standard data for the **turret punch run** (normal minutes per sheet). The IE team has collected:

- `data/capstone_punch_studies.csv`: 30 past studies with hits (holes and nibbles per sheet), tool stations used, sheet weight (kg), normal minutes and a notes column
- `data/capstone_punch_holdout.csv`: 6 newer studies for validation

Work in Excel (copy the `RunStudies` / `RunModel` layout from `templates/standard-data-workbook.xlsx`) or in Python.

## Tasks

1. **Define the element.** Write the start point, end point and method in two or three lines. What does "per sheet" include?
2. **Screen the data.** Plot normal minutes against each variable and compute r. Read the notes column.
3. **Fit a first model** with hits, tool stations and sheet weight. Look at the studentized residuals (ToolPak: standardized residuals).
4. **Deal with any outliers** using the Module 08 rules. Document what you did and why.
5. **Refit and evaluate.** Check coefficients (sign, size, t), R², SE, VIF and residual plots.
6. **Validate** on the 6 hold-out studies: error per study, mean absolute error, aggregate error. Note any study outside the data range.
7. **Write the data sheet** (codes, constant and variable elements, frequencies, ranges, allowance, version).
8. **Apply it.** Set the standard for a 40-sheet lot of a part with 180 hits, 6 tool stations and 22 kg sheets (12 % PF&D; ignore setup).
9. **Recommend.** In half a page: is the model ready to use, for which uses, and with what controls?

## Rubric

| Area | Meets the standard when you… |
|---|---|
| Element definition | State clear boundaries and the method, and say what is excluded (setup, sheet loading by crane, etc.) |
| Data handling | Find the problem study and give a documented reason for the action taken |
| Model | Keep only variables that are significant and physically sensible; report SE and range |
| Evaluation | Check residuals, VIF and hold-out errors; flag extrapolation |
| Application | Get the arithmetic right, apply the allowance once and state the units |
| Recommendation | Match the model's accuracy to its uses and give maintenance controls |

## Skill check

1. What makes a variable a good driver for standard data?
2. Name two situations where microscopic (motion-level) data is the better choice.
3. Why can a formula with 10 % per-job error still give an accurate weekly plan?
4. In `LINEST` output, where is the intercept?
5. What does a VIF of 12 tell you, and what can you do about it?
6. Why use a log-log transform for an element that rises steeply and then levels off?
7. What is the difference between a confidence interval and a prediction interval for a standard?
8. When may you delete a study from the data set?
9. Where should allowances be applied in a data system?
10. Name three events that should trigger a review of standard data.

<details><summary>Capstone key (run <code>python tools/sdskit.py capstone</code>)</summary>

- **Problem study:** T14 has a studentized residual of **12.6**, and its note reads "tool jam cleared during study". That is a foreign element, so exclude T14 and record the reason. (The first fit gives R² 0.887 and SE 0.372.)
- **Model (29 studies):** normal min/sheet = **0.6318 + 0.00389 × hits + 0.1476 × stations + 0.0316 × kg**. R² **0.979**, SE **0.14 min**, all p < 0.001. VIFs 1.16 / 1.55 / 1.74.
  - Ranges: hits 40–372, stations 1–12, weight 4.6–37.8 kg.
- **Hold-out:** errors −0.1 % to +7.2 %; mean absolute **2.5 %**; aggregate **+2.2 %**. T35 (375 hits) and T36 (29 hits) are slightly outside the hits range but still within ±3 %.
  - The aggregate bias is positive on 5 of 6 studies. Watch it in audits.
- **Job:** 0.6318 + 0.00389·180 + 0.1476·6 + 0.0316·22 = **2.913 normal min/sheet**; 40 × 2.913 × 1.12 / 60 = **2.175 standard h**.
- **Recommendation:** ready for quoting and capacity planning, with range flags in the calculator, an audit of a few jobs a quarter (watching the slight positive bias), change control on tooling and machines, and a refit once the hold-out studies are added.

</details>

<details><summary>Skill check answers</summary>

1. It is known before production, has a physical reason to affect time, and varies across jobs.
2. When the job doesn't exist yet, or you are comparing methods on paper. Also very short cycles, and building or checking new elements.
3. Random errors of different signs cancel when many jobs are added; bias does not.
4. In the last column of the first row, because coefficients run in reverse order of X.
5. That predictor is strongly explained by the others, so its coefficient is unstable. Drop or combine variables, or collect studies that break the link.
6. Because time ∝ weightᵇ becomes a straight line in logs, so linear regression fits it, and the relative errors on light items shrink.
7. A confidence interval is for the average of many such jobs. A prediction interval is for one new job; it is wider and is the honest uncertainty of a standard.
8. Only for a documented reason (foreign element, different method, proven error), never just because it doesn't fit.
9. Once, at the job level, on normal time, and never inside the elements as well.
10. Any three of: new machine or tooling; a method or layout change; audit errors drifting or biased in one direction; persistent efficiency outliers; new part features outside the range.

</details>
