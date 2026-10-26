# Module 16 — Capstone

**Time:** 3–4 h

## Option A — Your own problem

Pick a recurring problem at work and produce an A3-style report:

1. Problem statement (5W2H, Is/Is-Not) — Module 1
2. Baseline data and Pareto — Modules 2–3
3. Process map with observations — Module 4
4. Fishbone; top hypotheses marked to-test — Module 5
5. 5-Why for the top hypothesis; root cause tree if causes combine — Modules 6–7
6. Stratification and at least one data analysis (scatter/regression/logistic) that confirms or rules out a cause — Modules 8–12
7. Countermeasures ranked by strength; decision matrix — Modules 13–14
8. Corrective action matrix with verification methods — Module 15

## Option B — Course data challenge

Using the datasets in `data/`:

1. Make a Pareto of **non-leak** scrap by cost, then stratify the top category by machine and shift. Is any stratum different? Test it.
2. Using `leak_rate.csv`, add an interaction term Ra × torque to the reduced model. Does it improve adjusted R²?
3. Using `leak_test.csv`, find the torque needed to keep P(fail) ≤ 5% when Ra = 0.65 µm. Is that torque realistic (≤ 26 N·m)? What does that imply for the solution?
4. Write the corrective action matrix row for whatever you conclude.

## Rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Problem statement | Has cause/solution in it | Measurable but vague scope | Specific, measurable, bounded |
| Root cause logic | Opinion only | Chain without evidence | Chain verified with data in both directions |
| Data analysis | None | Correct method, weak interpretation | Correct method, assumptions checked, practical conclusion |
| Countermeasures | Training/reminders only | Mix, unranked | Ranked by strength, matched to root causes |
| Verification | None | Task completion only | Data-based effectiveness check |

8–10: ready to lead root cause investigations.
