# Module 11: Capstone and Skill Check

## Part A: plan an experiment (on your own process)

Use `templates/experiment-plan.md`. A complete plan has:

1. A problem statement with a measurable response, and evidence that the measurement system is adequate.
2. Three to six candidate factors with levels and a reason for each range.
3. Nuisance factors, each classed as held constant, blocked or randomized.
4. A design choice: full or fractional, with its resolution and alias structure if fractional.
5. A replicate count justified by a power calculation (Module 06).
6. A randomized run sheet (`templates/run-sheet.csv`).
7. The model you will fit, and how you will choose operating levels (Module 09).

**Review criteria:** could someone else run this experiment from the plan alone, and would the analysis answer the stated question?

## Part B: skill check (answers below)

1. A one-way ANOVA has 5 levels and 4 replicates each. What are the error df, and the F critical value at α = 0.05?
2. In an RCBD with 4 treatments and 6 blocks, how many error df are there?
3. Name two assumptions of the Latin square model.
4. In a 3 × 2 factorial with n = 4, what are the df for A, B, AB and error?
5. Cell means at (A−, B−), (A+, B−), (A−, B+) and (A+, B+) are 20, 30, 22 and 52. Compute the A effect, the B effect and the AB interaction.
6. Write the defining relation and the alias of BD for a 2^(4−1) design with D = ABC. What is its resolution?
7. Unreplicated 2^3 effects are A = 12.1, B = −0.6, C = 8.4, AB = 0.9, AC = 5.2, BC = −0.3 and ABC = 0.4. Which effects look active, and why is Lenth's method shaky here?
8. Centers average 48.0 (n = 4, s = 1.2) and the factorial points average 44.0 (16 runs). Is there curvature?
9. Doubling replicates from 4 to 8: by what factor does the standard error of a cell mean fall?
10. Which SS type should you report for an unbalanced two-factor design with a non-significant interaction?

<details><summary>Answers</summary>

1. df_E = 20 − 5 = 15, and F(4, 15) = 3.06.
2. (4 − 1)(6 − 1) = 15.
3. Any two of: no interactions among rows, columns and treatments; normal, independent errors with constant variance; rows, columns and treatments all have the same number of levels.
4. A: 2, B: 1, AB: 2, error: 3 × 2 × (4 − 1) = 18.
5. A = (30 + 52)/2 − (20 + 22)/2 = 41 − 21 = **20**. B = (22 + 52)/2 − (20 + 30)/2 = 37 − 25 = **12**. AB = [(52 − 22) − (30 − 20)]/2 = (30 − 10)/2 = **10**.
6. I = ABCD. BD × ABCD = AC, so BD is aliased with AC. Resolution IV.
7. A, C and AC. Lenth gives PSE = 0.75 and ME ≈ 2.8, and those three effects exceed it. With only 7 effects, though, Lenth's t has m/3 ≈ 2.3 df, so the PSE itself rests on very few small effects and the method has low power. A half-normal plot plus process knowledge is the practical call, followed by confirmation runs.
8. t = 4.0 / (1.2 × √(1/16 + 1/4)) = 4.0 / 0.671 ≈ 5.96 with 3 df, p ≈ 0.009. Yes, there is curvature; consider axial runs.
9. By √2: SE goes from σ/2 to σ/2.83, about 29 % smaller.
10. Type II (or Type III with sum-to-zero coding). State which one. Avoid Type I unless the term order is meaningful.

</details>
