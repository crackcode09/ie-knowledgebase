# Module 7 — Comparing One Proportion to a Standard

**Time:** 40 min · **Data:** `data/incoming_inspection.csv`

## Learning objectives

1. Test a proportion against a claimed or target value.
2. Choose between the normal approximation and the exact binomial test.

## 1. When to use it

Data are **pass/fail** (defective/good, on-time/late, yes/no), and you want to compare the observed rate with a standard: a supplier's claim, a contract limit, a historical rate.

## 2. Formulas

p̂ = d/n

**Normal approximation (z-test):** z = (p̂ − p₀) / √[p₀(1 − p₀)/n]. Reasonable when n·p₀ ≥ 10 and n·(1 − p₀) ≥ 10 (a common rule of thumb; some texts use 5).

**Exact binomial test:** p-value = P(X ≥ d) for X ~ Binomial(n, p₀) (upper-tailed). Always valid; preferred whenever software is available, and essential when n·p₀ is small.

## 3. Worked example — is the supplier meeting 3%?

The supplier claims ≤ 3% defective. You inspect 400 parts and find 21 defective.

- H₀: p ≤ 0.03 Hₐ: p > 0.03 (one-sided — the contract only cares about "worse than claimed") α = 0.05
- p̂ = 21/400 = **0.0525** (5.25%)
- n·p₀ = 12 → normal approximation borderline

| Method | Statistic | p-value |
|---|---|---|
| Normal approx. | z = (0.0525 − 0.03)/√(0.03 × 0.97/400) = 0.0225/0.00853 = **2.64** | 0.004 |
| Exact binomial | P(X ≥ 21 \| n = 400, p = 0.03) | **0.010** |

```bash
python tools/htest.py one-prop
```

Both reject H₀, but notice the normal approximation overstates the evidence by about 2.5× here. Report the exact result.

**95% CI for the true rate** (exact Clopper–Pearson, two-sided): **3.3% to 7.9%**. The supplier's 3% claim sits below the whole interval.

**Practical conclusion:** the evidence says the supplier is running above 3%, probably 3–8%. Open a supplier corrective action and tighten incoming inspection until fixed.

## 4. Sample size note

Low defect rates need large samples. To distinguish 3% from 5% with 80% power at α = 0.05 (one-sided), you need several hundred parts. For very low rates (ppm), proportion tests become impractical — measure a continuous characteristic instead.

## Check yourself

1. 2 defective in 50 parts; standard 1%. Is the normal approximation OK?
2. Why one-sided here?

<details><summary>Answers</summary>

1. No: n·p₀ = 0.5. Use the exact binomial test.
2. The decision (supplier action) only triggers if the rate is worse than claimed; the direction was set before seeing data.
</details>
