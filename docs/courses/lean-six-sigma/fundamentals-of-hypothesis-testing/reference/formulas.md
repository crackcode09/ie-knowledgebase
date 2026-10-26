# Formulas — One-Page Reference

| Test | Statistic | df / distribution | Key assumption |
|---|---|---|---|
| One-sample t | t = (x̄ − μ₀)/(s/√n) | n − 1 | One stable process; ~normal or n ≥ 30 |
| Paired t | t = d̄/(s_d/√n) | n − 1 | Differences ~normal |
| Welch two-sample t | t = (x̄₁ − x̄₂)/√(s₁²/n₁ + s₂²/n₂) | Welch–Satterthwaite | Independent groups |
| One-way ANOVA | F = MSB/MSW | (k − 1, N − k) | ~Normal, similar variances |
| One proportion (z) | z = (p̂ − p₀)/√[p₀(1 − p₀)/n] | Normal | np₀ ≥ 10, n(1 − p₀) ≥ 10; else exact binomial |
| Two proportions | z = (p̂₁ − p̂₂)/√[p̄(1 − p̄)(1/n₁ + 1/n₂)] | Normal | ≥ 5–10 defectives and good units per group; else Fisher |
| Chi-square independence | χ² = Σ(O − E)²/E, E = row×col/total | (r − 1)(c − 1) | ≤ 20% of E < 5, none < 1 |
| One variance | χ² = (n − 1)s²/σ₀² | n − 1 | **Normal** (not robust) |
| Two variances | F = s₁²/s₂² | (n₁ − 1, n₂ − 1) | **Normal**; else Levene |

## Confidence intervals

- Mean: x̄ ± t₁₋α/₂,n−1 · s/√n
- Difference of proportions: (p̂₁ − p̂₂) ± z₁₋α/₂ √[p̂₁(1 − p̂₁)/n₁ + p̂₂(1 − p̂₂)/n₂]
- σ: √[(n − 1)s²/χ²upper] to √[(n − 1)s²/χ²lower]

## Sample size (mean, two-sided, normal approximation)

n ≈ [(z₁₋α/₂ + z₁₋β) σ/δ]² (one-sample/paired; ×2 per group for two independent groups), then add 1–2 or iterate on the noncentral t.

| α (two-sided) | z₁₋α/₂ | Power | z₁₋β |
|---|---|---|---|
| 0.10 | 1.645 | 0.80 | 0.842 |
| 0.05 | 1.960 | 0.90 | 1.282 |
| 0.01 | 2.576 | 0.95 | 1.645 |

## Decision

p < α → reject H₀. Equivalently (two-sided): the H₀ value lies outside the (1 − α) CI.
