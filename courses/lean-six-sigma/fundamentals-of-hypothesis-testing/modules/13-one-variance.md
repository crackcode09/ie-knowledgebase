# Module 13 — Comparing One Variance to a Standard: Chi-Square Test

**Time:** 35 min · **Data:** `data/torque.csv`

## Learning objectives

1. Test whether a process standard deviation meets a requirement.
2. Compute a confidence interval for σ.
3. Know why this test is sensitive to non-normality.

## 1. Why test variation?

Most quality problems are variation problems. A process can be perfectly centered and still produce defects if σ is too large. Requirements are often written as a maximum σ (e.g., for capability: σ ≤ tolerance/8 for Cp ≥ 1.33).

## 2. Formula

  χ² = (n − 1)s² / σ₀²  df = n − 1

CI for σ: √[(n − 1)s² / χ²₁₋α/₂] to √[(n − 1)s² / χ²α/₂] (upper and lower chi-square percentiles).

**Assumption:** the data are normal. This test is **not robust** — heavy tails or skew can produce badly wrong p-values. Check a normal probability plot, or use a bootstrap CI for σ if in doubt.

## 3. Worked example — fastening torque

Requirement: σ ≤ 0.50 N·m. 25 consecutive fastenings: s = 0.633 N·m.

H₀: σ ≤ 0.50 Hₐ: σ > 0.50 α = 0.05

- χ² = 24 × 0.633² / 0.50² = **38.5**
- Critical χ²₀.₉₅,₂₄ = 36.42 → reject
- p = **0.031**
- 95% CI for σ: **0.49 to 0.88 N·m**

```bash
python tools/htest.py one-var
```

**Conclusion:** the station's variation exceeds the requirement. Note the CI's lower end (0.49) just touches 0.50 — the evidence is real but not overwhelming. Look for sources of variation (tool wear, joint stiffness, operator technique) before buying a new tool.

## Check yourself

1. Why is a sample of 25 still giving such a wide CI for σ?
2. Your data are clearly heavy-tailed. What do you do?

<details><summary>Answers</summary>

1. Standard deviations are estimated much less precisely than means; σ CIs narrow slowly with n.
2. Use a bootstrap CI for σ or a robust method, and investigate the tail values as possible special causes.
</details>
