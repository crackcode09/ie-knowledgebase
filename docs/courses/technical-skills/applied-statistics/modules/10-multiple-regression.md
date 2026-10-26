# Module 10 — Multiple Regression: Building Models to Predict Business Results

**Time:** 75 min

## Learning objectives

1. Build a multiple regression model and identify significant drivers.
2. Use the model to predict and to inform decisions.

## 1. Full model

```bash
python tools/statkit.py multiple
```

| Term | Coefficient | p |
|---|---|---|
| Orders | 3.10 k$ per order | < 0.001 |
| **Quoting lead time** | **−29.6 k$ per day** | **0.0002** |
| On-time delivery | +11.9 k$ per point | 0.0025 |
| Marketing spend | +2.7 k$ per k$ | 0.13 |

R² = 0.950, adjusted R² = 0.942.

**The masked driver appears.** Quoting lead time had r ≈ 0 with revenue alone (Module 8), but once orders are held constant, each extra day to quote costs about $30k per month. Marketing spend isn't significant here.

## 2. Reduced model

Drop marketing (p = 0.13):

  **Revenue = −871 + 3.01 × orders − 28.9 × quote days + 10.0 × on-time %**

R² = 0.945, adjusted R² = 0.938 — almost no loss from removing marketing.

## 3. Predicting business results

Plan: 480 orders, 2-day quotes, 95% on time →

  **1,468 k$**, 95% prediction interval **1,353 to 1,584 k$**

**What-if:** cutting quoting time from 4 to 2 days (within the observed 1.2–6 days) (holding the rest) → +2 × 28.9 ≈ **+58 k$/month** — a case for a faster quoting process.

## 4. Cautions

- Observational data: coefficients show association holding the other variables constant, not proof of cause. Confirm with a trial where possible.
- Correlated predictors make coefficients unstable — check variance inflation factors.
- Keep the model simple; validate it on new months before trusting it.
- Check residuals.

More depth (multicollinearity, logistic regression for pass/fail outcomes): *Root Cause Analysis*, Modules 9–12.

## Check yourself

Why might marketing spend show a negative correlation with revenue but a positive (non-significant) coefficient in the multiple regression?

<details><summary>Answer</summary>

Its simple correlation is confounded with other variables (e.g., spend happened to be higher in low-order months); holding orders, quoting and on-time constant changes the picture — and with p = 0.13 the data can't pin down its effect.
</details>
