# Module 07 — Capstone and Skill Check

## Part A — Your quality project (or the Bayline case end-to-end)

Produce a short project storyboard (one page per DMAIC phase):

| Phase | Deliverables |
|---|---|
| Define | charter (`templates/project-charter.md`) |
| Measure | data collection plan; MSA (variable or attribute); baseline (% defective, DPMO, capability); Pareto and histogram |
| Analyze | problem statement; fishbone; 5-Why; stratification and graphs; regression or other verification; FMEA |
| Improve | corrective action matrix; error-proofing; pilot with before/after comparison |
| Control | control plan; control chart with stage limits; visual management; standard work |

**Review criteria:** each conclusion is supported by data from a trusted measurement system; root causes are verified, not assumed; the control plan would hold the gain if the team left tomorrow.

## Part B — Skill check

1. Rolled throughput yield for 20 steps at 99 % each?
2. Five ODs: 6.352, 6.358, 6.349, 6.361, 6.355. Mean and standard deviation?
3. A gauge R&R gives 35 % of tolerance. Use the gauge for SPC?
4. Kappa of 0.45 vs standard. What does it mean?
5. How many parts to estimate a mean within ±0.5 units if σ = 2 (95 %)?
6. 12 defects found in 400 units with 3 opportunities each. DPU and DPMO?
7. Spec 10 ± 0.3, mean 10.1, σ 0.08. Cp, Cpk?
8. Which chart for: (a) daily % late shipments, (b) hourly 4-part samples of a length, (c) weekly lab result?
9. Write one "why" chain (3 levels) for "burr on insert."
10. Before 50/1,000 defective, after 15/1,000. Is the improvement significant (two-proportion test)?

<details><summary>Answers</summary>

1. 0.99²⁰ = 81.8 %.
2. Mean 6.3550; s = 0.00474 mm.
3. Not as is — over 30 % is generally unacceptable. Find whether repeatability or reproducibility dominates and fix it first.
4. Agreement is only moderately better than chance; the inspection needs improvement (standards, training, gauge) before its data can be trusted.
5. n = (1.96 × 2 / 0.5)² = 61.5 → 62.
6. DPU = 12/400 = 0.03; DPMO = 12 / (400 × 3) × 10⁶ = 10,000.
7. Cp = 0.6 / 0.48 = 1.25; Cpk = (10.3 − 10.1) / 0.24 = 0.83.
8. (a) p chart; (b) X̄–R; (c) I–MR.
9. Example: Burr → deburr brush worn → brush not changed at interval → no interval defined in PM → **How:** add brush change to PM at a tested interval and a visual wear limit.
10. p₁ = 5 %, p₂ = 1.5 %; pooled p = 3.25 %; z = 0.035 / √(0.0325 × 0.9675 × 2/1,000) ≈ 4.41; p < 0.001 — significant.

</details>
