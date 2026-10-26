# Module 10 — Simple Regression Analysis

**Time:** 50 min · **Data:** `data/tool_wear.csv`

## Learning objectives

1. Fit and interpret a straight-line model Y = b₀ + b₁X.
2. Use the model to set a process limit.
3. Check residuals.

## 1. The model

Least squares chooses b₀ and b₁ to minimize Σ(observed − predicted)².

  b₁ = Σ(x − x̄)(y − ȳ) / Σ(x − x̄)²  b₀ = ȳ − b₁x̄

## 2. Worked example — roughness vs tool hours

```bash
python tools/rca.py simple
```

  **Seat Ra = 0.307 + 0.0199 × hours**

| Output | Value | Meaning |
|---|---|---|
| Slope b₁ | 0.0199 µm/h (95% CI 0.0177 to 0.0221) | Ra rises ~0.02 µm per spindle hour |
| Intercept b₀ | 0.307 µm | Expected Ra with a fresh insert |
| R² | 0.91 | Tool hours explain 91% of Ra variation |
| p (slope) | < 0.0001 | Relationship is real |
| Residual SD s | 0.073 µm | Typical scatter around the line |

## 3. Using the model — set a tool-life limit

Seat Ra must stay ≤ 0.80 µm.

- The **mean** reaches 0.80 at (0.80 − 0.307)/0.0199 = **24.7 h**. Changing at 24.7 h means about half the parts at that point would be over the limit.
- Individual parts scatter by s ≈ 0.073. To keep individual parts below 0.80 with margin, aim for a predicted mean of about 0.80 − 2 × 0.073 ≈ 0.65 µm → (0.65 − 0.307)/0.0199 ≈ **17 h**.
- **Decision:** change the finishing insert every **16 h** (predicted mean 0.63 µm). Verify with the in-process Ra check.

(A formal prediction interval would add a little more width for uncertainty in the line itself; with n = 35 that's small.)

## 4. Check the residuals

Plot residuals (observed − predicted) against X and in time order. Look for curvature (the model's shape is wrong), funnel shapes (variation changes with X), or patterns over time. Here the residuals scatter evenly — the straight line is adequate over 3–40 h.

**Don't extrapolate:** the data cover 3–40 h; predictions beyond that are guesses.

## Check yourself

What does R² = 0.91 not tell you?

<details><summary>Answer</summary>

It doesn't prove causation, doesn't confirm the model's form is right (check residuals), and doesn't say whether predictions are precise enough for the decision (look at s).
</details>
