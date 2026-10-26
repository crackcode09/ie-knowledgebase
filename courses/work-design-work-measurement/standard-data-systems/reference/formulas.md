# Formulas and Cheat Sheet

## Standards

| Item | Formula |
|---|---|
| Normal time (time study) | observed time × rating |
| Standard time | normal time × (1 + PF&D), with the allowance as a % of normal time |
| Lot standard (h) | (setup + qty × run) × (1 + PF&D) / 60, with setup and run in normal minutes |
| Standard min/piece for a lot | lot standard × 60 / qty |
| Efficiency | standard hours earned / actual hours |
| Capacity load | standard hours required / available hours × planned utilization |

## Correlation and regression

| Item | Formula / meaning |
|---|---|
| Correlation r | Σ(x−x̄)(y−ȳ) / √[Σ(x−x̄)² Σ(y−ȳ)²]; −1 to +1 |
| Simple regression slope | b₁ = Σ(x−x̄)(y−ȳ) / Σ(x−x̄)²; b₀ = ȳ − b₁x̄ |
| R² | 1 − SS_resid / SS_total; equals r² in simple regression |
| Adjusted R² | 1 − (1 − R²)(n − 1)/(n − k − 1) |
| Std error of estimate | √[SS_resid / (n − k − 1)] |
| t for a coefficient | coefficient / its std error; \|t\| > about 2 is significant at ~5 % for moderate n |
| VIF | 1 / (1 − R²ⱼ); warning above about 5–10 |
| Studentized residual | residual / its own std error (with the point left out); investigate if \|value\| > 3 |
| Cook's distance | influence of one point on all fitted values; compare with the others and look at the largest |
| Prediction interval (one new job) | ŷ ± t × √(SE² + SE_mean²) |
| Confidence interval (mean) | ŷ ± t × SE_mean |
| Leave-one-out RMSE | √[mean of (yᵢ − ŷ₍₋ᵢ₎)²], each point predicted from a fit without it |

## Transformations

| Pattern | Model | Fit as |
|---|---|---|
| Rises then levels off | t = a·xᵇ, 0 < b < 1 | ln t = ln a + b ln x |
| Constant % growth | t = a·e^(bx) | ln t = ln a + b x |
| Step at a threshold | t = b₀ + b₁x + b₂·(x > c) | dummy variable |
| Effect depends on another variable | t = … + b·x₁x₂ | product (interaction) term |

## Excel

| Task | Function / tool |
|---|---|
| Multiple regression, live | `=LINEST(y, X, TRUE, TRUE)` as an array; columns in reverse order of X, intercept last |
| One coefficient | `=INDEX(LINEST(y, X), 1, column)` |
| Correlation | `=CORREL(x, y)` |
| Full report | Data > Data Analysis > Regression (Analysis ToolPak); static output |
| Log transform | `=LN(cell)` |

## Harlan press-brake data (v1.0)

- Run (normal min/piece) = 0.1863 + 0.0873·bends + 0.1184·flips + 0.0226·kg + 0.0535·m. Valid for bends 1–12, flips 0–6, 0.64–29.15 kg, 0.2–2.3 m.
- Setup (normal min) = 6.785 + 2.712·tool segments + 9.624·new program. Valid for 1–10 segments.
- PF&D 12 % on normal time.
