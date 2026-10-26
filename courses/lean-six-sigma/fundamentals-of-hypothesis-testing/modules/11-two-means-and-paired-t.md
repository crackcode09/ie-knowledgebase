# Module 11 — Comparing Two Means: Two-Sample and Paired t-Tests

**Time:** 60 min · **Data:** `data/supplier_hardness.csv`, `data/gauge_paired.csv`

## Learning objectives

1. Choose between an independent two-sample t-test and a paired t-test.
2. Perform both and interpret the results.
3. Explain why pairing increases power.

## 1. Independent or paired?

| Design | Example | Test |
|---|---|---|
| Two separate groups of units | Bars from supplier A vs bars from supplier B | **Two-sample t** |
| Same units measured twice | The same 12 parts on the old gauge and the new gauge; operators before/after training | **Paired t** |

Using the wrong one is a serious error — see Section 4.

## 2. Two-sample t (Welch)

  t = (x̄₁ − x̄₂) / √(s₁²/n₁ + s₂²/n₂)

Welch's version doesn't assume equal variances and is the safer default (it's what most modern software uses by default for "two-sample t"). The degrees of freedom come from the Welch–Satterthwaite formula; software handles it.

### Worked example — supplier hardness

| | Supplier A | Supplier B |
|---|---|---|
| n | 15 | 15 |
| Mean (HRC) | 58.41 | 59.26 |
| s | 1.28 | 1.39 |

H₀: μ_A = μ_B Hₐ: μ_A ≠ μ_B α = 0.05

- SE = √(1.277²/15 + 1.394²/15) = 0.488
- t = (58.41 − 59.26)/0.488 = **−1.75**, df = 27.8, p = **0.092**
- 95% CI for μ_A − μ_B: **−1.85 to +0.15 HRC**

```bash
python tools/htest.py two-means
```

**Conclusion:** fail to reject. But the CI includes differences up to 1.85 HRC — **inconclusive**, not "the suppliers are the same." (These data were generated with a true difference of 1.4 HRC; this is the Type II error discussed in Module 2.) Action: test more bars before switching suppliers.

## 3. Paired t

Compute the difference for each unit, dᵢ = after − before (or new − old), then do a one-sample t-test on the d's against 0:

  t = d̄ / (s_d/√n)  df = n − 1

### Worked example — new vs old height gauge

12 parts measured on both gauges. Differences new − old (mm):

0.0095, 0.0026, −0.0016, 0.0044, 0.0032, 0.0116, 0.0140, 0.0058, 0.0007, 0.0078, −0.0019, 0.0024

- d̄ = **0.00488 mm**, s_d = 0.00504
- t = 0.00488/(0.00504/√12) = **3.35**, df = 11, p = **0.0064**
- 95% CI: **0.0017 to 0.0081 mm**

```bash
python tools/htest.py paired
```

**Conclusion:** the new gauge reads about 0.005 mm higher than the old one (bias). Correct it or re-zero before release.

## 4. Why pairing matters

Run the gauge data through an **independent** two-sample t-test by mistake: p = **0.66**. The real bias (≈ 0.005 mm) is buried under the part-to-part variation (s ≈ 0.025 mm). Pairing removes part-to-part variation from the comparison — the same effect would need hundreds of parts in an unpaired design.

## Exercise 11.1

Using `data/supplier_hardness.csv`, run the equal-variance (pooled) t-test and compare its p-value with Welch's. Why are they so close here?

<details><summary>Answer</summary>

Pooled p = 0.091 vs Welch 0.092. The two sample SDs are similar and n₁ = n₂, so the methods nearly coincide. They diverge when variances and sample sizes both differ.
</details>

## Check yourself

1. Ten operators measure a part with and without a new fixture. Which test?
2. Why is Welch's t a better default than the pooled t?

<details><summary>Answers</summary>

1. Paired t (each operator is measured under both conditions).
2. It stays valid when variances differ and loses little when they're equal.
</details>
