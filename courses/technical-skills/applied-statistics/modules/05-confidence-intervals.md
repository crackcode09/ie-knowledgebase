# Module 5 — Confidence, Risk and Confidence Intervals

**Time:** 75 min

## Learning objectives

1. Explain confidence level and risk (α).
2. Compute confidence intervals for a mean, a proportion and a standard deviation.

## 1. Confidence and risk

A 95% confidence interval comes from a method that captures the true value in 95% of samples. The remaining 5% (α) is the **risk** of an interval that misses. Higher confidence → wider interval; more data → narrower.

## 2. Mean

  x̄ ± t(α/2, n−1) · s/√n

Reflow cycle time (n = 120, x̄ = 61.89, s = 2.35):

  61.89 ± 1.980 × 2.35/√120 = **61.47 to 62.31 s**

## 3. Standard deviation

  √[(n − 1)s² / χ²(upper)] to √[(n − 1)s² / χ²(lower)]

  **2.09 to 2.69 s** (95%) — requires roughly normal data.

## 4. Proportion

118 of 200 boards had at least one solder defect: p̂ = 0.590.

| Method | 95% CI |
|---|---|
| Normal approximation p̂ ± 1.96√[p̂(1 − p̂)/n] | 0.522 to 0.658 |
| Wilson score interval (better for small n or p near 0 or 1) | 0.521 to 0.656 |

```bash
python tools/statkit.py ci
```

## 5. Reading intervals

- The CI is about the **process parameter**, not individual units (95% of boards don't fall between 61.47 and 62.31 s — that would be a much wider prediction or tolerance interval).
- Report effect sizes with CIs, not just "significant / not significant."
- If the interval is too wide for the decision, collect more data: width ∝ 1/√n.

## Check yourself

How many boards would you need to estimate the defect proportion within ±3 points at 95%?

<details><summary>Answer</summary>

n = 1.96² × 0.59 × 0.41 / 0.03² ≈ 1,033 (or 1,068 using p = 0.5 if unknown).
</details>
