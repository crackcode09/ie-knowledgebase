# Module 10 — Comparing One Mean to a Standard: One-Sample t-Test

**Time:** 45 min · **Data:** `data/bearing_od.csv`

## Learning objectives

1. Perform a one-sample t-test by hand and with software.
2. Check its assumptions.

## 1. Formula

  t = (x̄ − μ₀) / (s/√n)  df = n − 1

Use t (not z) because σ is estimated from the sample. With n ≥ ~30 the two are nearly identical.

**Assumptions**

1. Data are a random/representative sample from **one stable process** (plot in time order — Module 6).
2. Observations are independent.
3. The population is roughly normal — or n is large enough (≥ ~30) for the averages to be approximately normal. The test is fairly robust to mild non-normality; strong skew with small n → use a nonparametric test (Module 16).

## 2. Worked example — lathe on nominal?

From Module 3, n = 20 was planned to detect a 0.004 mm offset with 80% power.

H₀: μ = 25.000 mm Hₐ: μ ≠ 25.000 mm α = 0.05

| Step | Value |
|---|---|
| x̄ | 25.00715 |
| s | 0.006023 |
| s/√n | 0.001347 |
| t = 0.00715 / 0.001347 | **5.31** |
| df | 19 |
| t critical (two-sided) | 2.093 |
| p | **0.00004** |
| 95% CI | **25.0043 to 25.0100** |

```bash
python tools/htest.py one-mean
```

**Assumption checks:** run chart shows no trend; Shapiro–Wilk normality p = 0.20 (no evidence against normality — which, with n = 20, is weak reassurance, not proof).

**Conclusion:** the lathe is running about 0.007 mm large (CI 0.004 to 0.010). Against a ±0.015 tolerance that matters (Module 4) → adjust the offset by −0.007 mm, then verify with a chart.

## 3. Spreadsheet

`=T.TEST` won't do a one-sample test directly. Compute t from the formula, then p = `T.DIST.2T(ABS(t), n-1)`.

## Exercise 10.1

After the offset adjustment you measure 15 parts: x̄ = 25.0012, s = 0.0058. Test H₀: μ = 25.000 at α = 0.05.

<details><summary>Answer</summary>

SE = 0.0058/√15 = 0.001498; t = 0.0012/0.001498 = 0.80; df = 14; p ≈ 0.44. Fail to reject — no evidence the process is still off nominal. CI ≈ 24.9980 to 25.0044.
</details>

## Check yourself

1. Why t instead of z?
2. n = 8 and the histogram is very skewed. What should you do?

<details><summary>Answers</summary>

1. σ is unknown and estimated by s, which adds uncertainty; the t distribution accounts for it.
2. Use a nonparametric test (Wilcoxon signed-rank or sign test) or collect more data.
</details>
