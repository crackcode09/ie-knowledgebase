# Module 8 — Comparing Two Proportions

**Time:** 40 min · **Data:** `data/shift_defectives.csv`

## Learning objectives

1. Test whether two groups have different defective rates.
2. Report the difference with a confidence interval.

## 1. Formulas

p̂₁ = d₁/n₁, p̂₂ = d₂/n₂, pooled p̄ = (d₁ + d₂)/(n₁ + n₂)

**z = (p̂₁ − p̂₂) / √[p̄(1 − p̄)(1/n₁ + 1/n₂)]**

CI for the difference (unpooled): (p̂₁ − p̂₂) ± 1.96 √[p̂₁(1 − p̂₁)/n₁ + p̂₂(1 − p̂₂)/n₂]

Conditions: at least ~5–10 defectives *and* non-defectives in each group. Otherwise use **Fisher's exact test**.

## 2. Worked example — day vs night shift

| Shift | Inspected | Defective | Rate |
|---|---|---|---|
| Day | 500 | 17 | 3.40% |
| Night | 520 | 35 | 6.73% |

H₀: p_day = p_night Hₐ: p_day ≠ p_night α = 0.05

- p̄ = 52/1020 = 0.0510
- SE = √[0.0510 × 0.9490 × (1/500 + 1/520)] = 0.01378
- z = (0.0340 − 0.0673)/0.01378 = **−2.42**, p = **0.016**
- Fisher's exact test: p = 0.022 (agrees)
- 95% CI for p_day − p_night: **−6.0 to −0.7 percentage points**

```bash
python tools/htest.py two-prop
```

**Conclusion:** night shift's defective rate is higher, by somewhere between 0.7 and 6 points. Next question for the Analyze phase: *why?* (lighting, staffing, material lot, machine warm-up). A significant test identifies *where* to look, not the cause.

## 3. Pitfall — confounding

If night shift runs a different product mix, the comparison mixes shift with product. Stratify (compare within product) or use a chi-square table (Module 9) with product as a factor.

## Check yourself

1. Day: 2/60 defective; night: 5/58. Which test?
2. The CI for p₁ − p₂ is (−0.02, 0.04). Conclusion at α = 0.05?

<details><summary>Answers</summary>

1. Fisher's exact test — too few defectives for the normal approximation.
2. Fail to reject; 0 is inside the interval.
</details>
