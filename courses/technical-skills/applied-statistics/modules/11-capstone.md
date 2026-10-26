# Module 11 — Capstone and Skill Check

**Time:** 2 h

## Part A — Skill check

1. Data: mean 50, median 42. Skewness sign?
2. A lot of 200 contains 6 defectives; sample 20, accept if 0 defective. Which distribution? (Compute with software.)
3. p = 0.02 defective, sample 50. P(0 defective) by binomial?
4. Mean 3 defects per panel (Poisson). P(defect-free panel)?
5. Mean 10.0, sd 0.2, LSL 9.5. Percentage below LSL?
6. MTBF 200 h (exponential). P(no failure in 24 h)?
7. n = 16, x̄ = 48.0, s = 4.0. 95% CI for the mean (t = 2.131)?
8. 45 of 300 orders late. 95% CI for the late rate (normal approximation)?
9. Two printers: s₁ = 3, s₂ = 6, n = 25 each. F statistic?
10. Revenue = 100 + 2.5 × orders − 20 × quote days. Effect of cutting quote time by 1.5 days?

<details><summary>Answers</summary>

1. Positive (right-skewed).
2. Hypergeometric (N = 200, K = 6, n = 20); P(accept) ≈ 0.53.
3. 0.98⁵⁰ = 0.364.
4. e⁻³ = 0.050.
5. z = −2.5 → 0.62%.
6. e^(−24/200) = 0.887.
7. 48.0 ± 2.131 × 4/4 = 45.9 to 50.1.
8. 0.15 ± 1.96 × √(0.15 × 0.85/300) = 0.15 ± 0.040 → 11.0% to 19.0%.
9. 36/9 = 4.0.
10. +30.
</details>

## Part B — Project

Using your own process data (or the course datasets):

1. Write a data collection plan (purpose, operational definition, sampling, stratification).
2. Summarize one continuous and one count variable (graphs, center, spread, shape).
3. Fit an appropriate distribution to each and forecast one performance figure (ppm beyond a limit, P(no failure), P(defect-free)).
4. Give 95% CIs for a mean, a proportion and a standard deviation.
5. Run one test for a mean, one for a proportion and one comparing two variances; state practical significance.
6. Handle one non-normal variable (transform or bootstrap).
7. Build a multiple regression predicting a business outcome; report a prediction interval and one what-if.

Score each 0/1/2 (missing / done / done with sound interpretation). 11+ of 14: ready to apply these methods at work.
