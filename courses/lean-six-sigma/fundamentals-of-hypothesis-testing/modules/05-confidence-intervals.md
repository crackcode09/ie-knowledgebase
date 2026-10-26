# Module 5 — Confidence Intervals

**Time:** 45 min

## Learning objectives

1. Compute and interpret a confidence interval for a mean.
2. Use a confidence interval to judge statistical significance.
3. Explain why an interval says more than a p-value.

## 1. What a confidence interval is

A 95% confidence interval (CI) is a range computed from the sample, by a method that captures the true parameter in 95% of repeated samples.

General form: **estimate ± (critical value) × standard error**

For a mean: x̄ ± t₁₋α/₂, n−1 · s/√n

**Correct reading:** "We're 95% confident the process mean is between 25.0043 and 25.0100 mm." **Not:** "95% of parts fall in this range" — that's a tolerance or prediction interval, a different thing.

## 2. CIs and tests are two views of the same thing

For a two-sided test at α, **reject H₀ exactly when the hypothesized value lies outside the (1 − α) CI.**

| Example (module) | 95% CI | H₀ value | Inside? | Decision |
|---|---|---|---|---|
| Bearing OD (10) | 25.0043 to 25.0100 mm | 25.000 | No | Reject |
| Hardness A − B (11) | −1.85 to +0.15 HRC | 0 | Yes | Fail to reject |
| Gauge new − old (11) | +0.0017 to +0.0081 mm | 0 | No | Reject |
| Day − night defect rate (8) | −6.0 to −0.7 points | 0 | No | Reject |

## 3. Why the interval is more useful

Look at the hardness result. The p-value (0.092) only says "not significant." The CI says the difference is somewhere between B being **1.85 HRC harder** and A being **0.15 HRC harder**. If 1 HRC matters for your heat treatment, the data are **inconclusive**, not reassuring — you need more bars.

| CI relative to "what matters" (±δ) | Conclusion |
|---|---|
| Excludes 0, entirely beyond δ | Real and important |
| Excludes 0, entirely within ±δ | Real but unimportant |
| Includes 0, entirely within ±δ | Equivalent for practical purposes |
| Includes 0, extends beyond δ | **Inconclusive** — get more data |

## 4. Width

Width ∝ σ/√n. To halve the width, quadruple n.

## Exercise 5.1

Compute by hand the 95% CI for the bearing OD: n = 20, x̄ = 25.00715, s = 0.006023, t₀.₉₇₅,₁₉ = 2.093.

<details><summary>Answer</summary>

SE = 0.006023/√20 = 0.001347. Margin = 2.093 × 0.001347 = 0.00282. CI = 25.0043 to 25.0100 mm.
</details>

## Check yourself

1. A 95% CI for a mean difference is (0.2, 3.1). What's the two-sided test result at α = 0.05?
2. True or false: a 99% CI is narrower than a 95% CI from the same data.

<details><summary>Answers</summary>

1. Reject H₀ (0 is outside the interval).
2. False — more confidence requires a wider interval.
</details>
