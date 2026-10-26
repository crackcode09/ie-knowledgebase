# Module 14 — Comparing Two Variances: F-Test and Levene's Test

**Time:** 40 min · **Data:** `data/saw_length.csv`

## Learning objectives

1. Compare the variation of two processes.
2. Choose between the F-test and Levene's test.
3. Recognize a low-power variance comparison.

## 1. The tests

**F-test:** F = s₁² / s₂², df = (n₁ − 1, n₂ − 1). Requires normal data — like the one-variance test, it is very sensitive to non-normality.

**Levene's test (Brown–Forsythe variant, median-centered):** an ANOVA on the absolute deviations from each group's median. Much more robust; a good default. Also works for 3+ groups.

## 2. Worked example — does the new saw cut more consistently?

16 cuts per saw, target length 150 mm.

| Saw | n | s (mm) |
|---|---|---|
| Old | 16 | 0.312 |
| New | 16 | 0.300 |

H₀: σ_old = σ_new Hₐ: σ_old ≠ σ_new α = 0.05

| Test | Statistic | p |
|---|---|---|
| F-test | F = 0.312²/0.300² = 1.08, df (15, 15) | 0.88 |
| Levene (median) | W = 0.10 | 0.75 |

```bash
python tools/htest.py two-var
```

**Conclusion:** no evidence the saws differ in variation.

## 3. A cautionary note on power

These data were generated with true σ_old = 0.40 and σ_new = 0.22 — the new saw really is almost twice as consistent. This sample happened to understate the difference badly. Even with the true ratio, the power of the F-test with 16 cuts each is only about **61%**.

Variance tests need **much more data than mean tests**. Before declaring "no difference in variation," compute the power, or report a CI for the ratio σ₁/σ₂ and see how wide it is. Plan around 30–50+ per group for variance comparisons that matter.

## Check yourself

1. Why prefer Levene over the F-test in practice?
2. The F-test p = 0.40 with n = 10 per group. What can you conclude?

<details><summary>Answers</summary>

1. The F-test can give misleading p-values when data aren't normal; Levene is robust.
2. Very little — with 10 per group the test has low power for anything but a huge difference.
</details>
