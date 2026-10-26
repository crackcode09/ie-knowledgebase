# Module 10 — Capstone and Skill Check

## Part A — Harbor Precision quality plan (team exercise)

Using the course data, prepare a one-page quality plan for the pin line and incoming valve seats:

1. **Characteristic and spec** — pin diameter 12.000 ± 0.030 mm.
2. **Chart choice and subgrouping** — which chart, subgroup size, frequency, and why (Modules 02–06).
3. **Reaction plan** — what the operator does on each signal (Module 03; `templates/reaction-plan.md`).
4. **Capability** — current Cp/Cpk, the centering opportunity and its value (Module 07).
5. **Incoming inspection** — a sampling plan for valve seats that meets AQL 1 % (α 5 %) and LTPD 6 % (β 10 %), with its OC curve, AOQL and expected inspection load; and the path to reducing inspection through supplier process data (Modules 08–09).

Or apply the same steps to a process you know.

## Part B — Skill check

1. Five values: 4.2, 4.8, 5.1, 4.6, 4.3. Mean, median, range, s?
2. Give one example each of common-cause and special-cause variation on a lathe.
3. Subgroups of 5: X̿ = 2.500, R̄ = 0.020. X̄ and R limits?
4. Individuals data: x̄ = 100, MR̄ = 4. Limits for the I and MR charts?
5. p̄ = 0.05, n = 200. p-chart limits?
6. c̄ = 9. c-chart limits?
7. When would you use a DNOM chart instead of separate charts per part?
8. Spec 10.00 ± 0.06, mean 10.02, σ_within 0.012. Cp, Cpk, and expected ppm (normal)?
9. Plan n = 125, c = 3. P(accept) at p = 1 %? (binomial)
10. For a plan with P(accept) = 0.90 at p = 2 %, N = 5,000, n = 125, what is the AOQ?

<details><summary>Answers</summary>

1. Mean 4.60; median 4.6; range 0.9; s = 0.367.
2. Common: small fluctuations in material hardness, ambient temperature. Special: a chipped insert, a wrong offset entered.
3. X̄: 2.500 ± 0.577 × 0.020 → 2.4885 to 2.5115. R: UCL 2.114 × 0.020 = 0.0423; LCL 0.
4. I: 100 ± 2.66 × 4 → 89.36 to 110.64. MR: UCL 3.267 × 4 = 13.07.
5. 0.05 ± 3√(0.05 × 0.95 / 200) = 0.05 ± 0.0462 → 0.38 % to 9.62 %.
6. 9 ± 3 × 3 → 0 to 18.
7. Many part numbers in short runs on the same process, with similar variation.
8. Cp = 0.12 / 0.072 = 1.67; Cpk = (10.06 − 10.02) / 0.036 = 1.11; ppm ≈ 1e6 × [P(Z > 3.33) + P(Z < −6.67)] ≈ 429 ppm.
9. ≈ 0.962.
10. 0.90 × 0.02 × (5,000 − 125) / 5,000 = 1.755 %.

</details>
