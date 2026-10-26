# Exercise and Case Solutions

All numbers come from `data/` (regenerate with `python tools/make_data.py`) and `tools/htest.py`. Last-digit differences are rounding.

## Module 1 — Exercise 1.1

See the answers inside the module.

## Module 3 — Exercise 3.1

δ = 1.4, σ = 1.2 → **13 per group**; δ = 2.0 → **7 per group** (`n_per_group_two_means`, exact noncentral t, α = 0.05, 80% power).

## Module 5 — Exercise 5.1

SE = 0.001347; margin = 2.093 × 0.001347 = 0.00282; CI **25.0043 to 25.0100 mm**.

## Module 10 — Exercise 10.1

t = 0.0012 / (0.0058/√15) = 0.80, df = 14, **p = 0.44**; 95% CI 24.9980 to 25.0044. Fail to reject.

## Module 11 — Exercise 11.1

Pooled t p = 0.091 vs Welch p = 0.092 — nearly identical because the SDs are similar and n₁ = n₂.

## Module 16 — Exercise 16.1

Paired t on discomfort scores: p = 0.002 — agrees with Wilcoxon (0.007) and the sign test (0.012). For ordinal ratings, report the Wilcoxon/sign result as primary.

---

## Capstone

### Case A — The coolant change

- H₀: μ_new = μ_old Hₐ: μ_new ≠ μ_old (two-sided; one-sided μ_new > μ_old is also defensible if fixed in advance), α = 0.05.
- Old: mean 397.8, s 38.7; new: mean 444.3, s 40.7 (n = 10 each). Shapiro–Wilk p = 0.19 and 0.13 — no evidence against normality.
- Welch t = 2.62, df ≈ 18.0, **p = 0.018**; 95% CI for new − old: **+9 to +84 parts**.
- **Verdict:** reject H₀ — the new coolant extends tool life.
- **Practical:** the business threshold is +30. The point estimate (+46.5) beats it, but the CI's lower end (+9) doesn't. Evidence of *an* improvement is solid; evidence that it clears +30 is not. Run more inserts (or a cost model across the CI) before committing.
- **Possible error:** Type I (p = 0.018).

### Case B — The careless carrier?

- H₀: damage rate is the same for all three carriers. α = 0.05.
- Rates: 3.75%, 4.23%, 4.35%.
- Chi-square (3 × 2): **χ² = 0.12, df = 2, p = 0.94**. Expected damaged counts 9.5–10.7 (all ≥ 5).
- **Verdict:** fail to reject. No evidence any carrier is worse.
- **Practical:** don't penalize a carrier based on these data. With ~4% damage rates and ~250 shipments each, only large differences (several percentage points) could be detected — this is a low-power comparison. If a 1-point difference matters, you'd need thousands of shipments per carrier.
- **Possible error:** Type II.

### Case C — Does the training pay off?

- Same inspectors before/after → **paired** design. H₀: μ_d = 0 Hₐ: μ_d < 0 (one-sided, the claim is "cuts time"; two-sided also acceptable), α = 0.05.
- Mean difference (after − before) = **−0.83 min**, s_d = 0.72, n = 10.
- Paired t = −3.64, df = 9, two-sided **p = 0.005** (one-sided 0.003); 95% CI **−1.35 to −0.31 min**.
- If analyzed (wrongly) as independent groups: p = 0.30 — inspector-to-inspector differences (≈ 2.5 min) swamp the effect.
- **Verdict:** reject H₀ — training reduced inspection time by about 0.8 min per part (≈ 6%).
- **Practical:** multiply by annual inspection volume to decide if it's worth the course cost.
- **Possible error:** Type I.

### Case D — Is the CMM biased?

- H₀: μ = 50.000 Hₐ: μ ≠ 50.000, α = 0.05.
- x̄ = 49.99988, s = 0.00124, n = 12.
- One-sample t = −0.35, df = 11, **p = 0.73**; 95% CI **49.99909 to 50.00066 mm**.
- **Verdict:** fail to reject — no evidence of bias.
- **Practical:** the CI (±0.0008 mm around 49.9999) is wider than the master's ±0.0005 mm uncertainty. The study can rule out a bias larger than about 0.0009 mm, not a smaller one. If smaller bias matters, take more readings or use a better reference.
- **Possible error:** Type II.
