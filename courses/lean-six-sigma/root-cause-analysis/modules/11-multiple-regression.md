# Module 11 — Multiple Regression: Finding the Significant Inputs

**Time:** 90 min · **Data:** `data/leak_rate.csv`

## Learning objectives

1. Fit a multiple regression model Y = f(X₁, X₂, …).
2. Identify the significant process inputs.
3. Recognize and handle correlated inputs (multicollinearity).

## 1. The model

  Y = b₀ + b₁X₁ + b₂X₂ + … + ε

Each coefficient is the change in Y per unit change in that X **holding the other Xs constant**. Its p-value tests whether that X adds information once the others are in the model.

## 2. Worked example — what drives leak rate?

60 valves, each with leak rate (cc/min) and five candidate inputs from the fishbone.

```bash
python tools/rca.py multiple
```

**Full model** (R² = 0.805, adjusted R² = 0.787):

| Input | Coefficient | p-value | VIF |
|---|---|---|---|
| Seat Ra (µm) | +3.39 | < 0.001 | 1.08 |
| Clamp torque (N·m) | −0.135 | < 0.001 | 1.05 |
| Ambient temperature (°C) | +0.0001 | 0.996 | 2.14 |
| Humidity (%) | +0.005 | 0.85 | 2.21 |
| Gasket thickness (mm) | −0.78 | 0.51 | 1.09 |

**Reduced model** (drop non-significant inputs one at a time, largest p first):

  **Leak rate = 4.79 + 3.43 × Ra − 0.135 × torque**

R² = 0.804, adjusted R² = 0.797, residual SD = 0.50 cc/min. Both inputs p < 0.0001.

**Reading:**

- **Seat roughness** is the dominant driver: +0.1 µm Ra adds about 0.34 cc/min.
- **Clamp torque** matters too: each extra N·m reduces leak rate by ~0.14 cc/min.
- **Humidity, temperature and gasket thickness** add nothing. The popular humidity theory from the fishbone is ruled out: alone, humidity's correlation with leak rate is r = 0.03 (p = 0.84).
- Dropping three inputs barely changed R² (0.805 → 0.804) and *raised* adjusted R² — a simpler model that predicts just as well.

## 3. Multicollinearity

Ambient temperature and humidity are correlated (r = 0.72) — warm days are humid days. When inputs are correlated, their individual coefficients become unstable and p-values inflate; the model can't separate their effects.

**Variance inflation factor (VIF):** VIF = 1 means no correlation with other inputs; values above ~5–10 are a warning. Here VIFs are ~2.2 — mild. Neither matters anyway.

Remedies when VIF is high: drop one of the correlated inputs, combine them, or collect data where they vary independently (a designed experiment).

## 4. Regression on historical data — limits

Observational data show association, not proof of cause. Lurking variables, narrow ranges and correlated inputs can mislead. Confirm key findings with a designed experiment or a controlled before/after trial — here, run a batch with fresh vs worn inserts at controlled torque.

## Check yourself

1. Why can a factor be significant on its own but not in the multiple regression?
2. What does adjusted R² do that R² doesn't?

<details><summary>Answers</summary>

1. It may be correlated with another input that explains the same variation better.
2. Penalizes adding inputs that don't improve the model, so it can go down when useless terms are added.
</details>
