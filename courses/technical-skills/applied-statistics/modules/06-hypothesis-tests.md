# Module 6 — Hypothesis Tests for Means, Proportions and Standard Deviations

**Time:** 90 min

## Learning objectives

1. Set up and run hypothesis tests for a mean, a proportion and a standard deviation.
2. Compare two groups' means and variances.
3. Interpret p-values, risk and practical significance.

## 1. The logic

| | H₀ true | H₀ false |
|---|---|---|
| Reject H₀ | Type I error (α) | Correct (power) |
| Fail to reject H₀ | Correct | Type II error (β) |

p-value: probability of a result at least this extreme **if H₀ were true**. p < α → reject H₀. Failing to reject is not proof of no effect.

## 2. Tests — PCB case

```bash
python tools/statkit.py tests
```

| Question | Test | Statistic | p | Decision |
|---|---|---|---|---|
| Is mean cycle time different from the 61.0 s standard? | One-sample t | t = 4.15 | 0.0001 | Reject: mean ≈ 61.9 s, about 0.9 s slower than standard |
| Do more than half of boards have a defect? | Exact binomial (one-sided) | 118/200 | 0.0066 | Reject: yes |
| Is printer P1's σ above 5 µm? | Chi-square (one sd) | χ² = 11.3 | 0.987 | No — s = 3.42 |
| Is printer P2's σ above 5 µm? | Chi-square | χ² = 35.3 | 0.064 | Not at α = 0.05 (s = 6.06) — inconclusive |
| Do the printers differ in variability? | F test | F = 3.14 | **0.0069** | Reject: P2 is more variable |
| Same, robust to non-normality | Levene | — | 0.031 | Reject |
| Do the printers differ in mean thickness? | Welch t | t = −2.45 | 0.019 | Reject: P2 ≈ 3.4 µm thicker |

**Reading the printers:** testing P2 alone against a 5 µm requirement is inconclusive with 25 boards, but comparing it with P1 shows clearly that P2 is worse. Comparisons often have more power than tests against a fixed number. Action: investigate P2 (stencil wear, squeegee pressure, support pins).

## 3. Practical significance

The cycle-time difference (0.9 s, 95% CI on the mean 61.47–62.31) is statistically clear. Whether it matters depends on the line: at 0.9 s × 1,000 boards/day ≈ 15 min/day. Always ask both "is it real?" and "does it matter?"

Full treatment of tests, power and nonparametric alternatives: *Fundamentals of Hypothesis Testing* in this repository.

## Check yourself

A test gives p = 0.064 at α = 0.05. Write the conclusion.

<details><summary>Answer</summary>

"Not enough evidence at the 5% level to conclude σ exceeds 5 µm — but the data don't show it's below either; more boards are needed for a confident answer."
</details>
