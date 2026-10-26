# Module 8 — Correlation Analysis

**Time:** 50 min

## Learning objectives

1. Measure the strength and direction of a linear relationship.
2. Avoid misreading correlations.

## 1. Pearson's r

  r = Σ(x − x̄)(y − ȳ) / √[Σ(x − x̄)² Σ(y − ȳ)²], −1 ≤ r ≤ 1

r² = share of variation in y explained by a straight line in x.

## 2. Case — what drives monthly revenue? (30 months)

```bash
python tools/statkit.py correlation
```

| Revenue vs | r | p |
|---|---|---|
| Orders per month | **0.946** | < 0.001 |
| Quoting lead time (days) | 0.004 | 0.98 |
| On-time delivery % | 0.177 | 0.35 |
| Marketing spend (k$) | −0.325 | 0.08 |

At face value only orders matter; quoting time has **no** correlation with revenue. Module 10 shows that conclusion is wrong.

## 3. Traps

| Trap | Here |
|---|---|
| **Masking** — a strong driver hides weaker ones | Orders swing revenue so much that quoting time's effect is invisible in a one-to-one correlation |
| **Spurious correlation** | Marketing spend's negative r (−0.33) is chance or confounding, not "marketing loses money" (Module 10: not significant once other drivers are included) |
| Correlation ≠ causation | Revenue and orders both rise in good months for many reasons |
| Nonlinearity, outliers, restricted range | Always plot |

## Check yourself

r = 0.004 between quoting time and revenue. Can you conclude quoting speed doesn't affect revenue?

<details><summary>Answer</summary>

No — a near-zero simple correlation can hide a real effect masked by other variables; check with multiple regression or an experiment.
</details>
