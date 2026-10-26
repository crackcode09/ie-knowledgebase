# Formulas and Quick Reference

| Tool | Formula / rule |
|---|---|
| Pareto | % = category / total; cumulative % = running sum |
| Pearson correlation | r = Σ(x − x̄)(y − ȳ) / √[Σ(x − x̄)² Σ(y − ȳ)²] |
| Simple regression | b₁ = Σ(x − x̄)(y − ȳ)/Σ(x − x̄)²; b₀ = ȳ − b₁x̄ |
| R² | 1 − SS_residual / SS_total |
| Adjusted R² | 1 − (1 − R²)(n − 1)/(n − p − 1) |
| VIF for input j | 1 / (1 − R²ⱼ), R²ⱼ from regressing Xⱼ on the other inputs; > 5–10 = concern |
| Logistic model | ln[p/(1 − p)] = b₀ + Σ bᵢXᵢ; p = 1/(1 + e^−(…)) |
| Odds ratio | e^(bᵢ × Δx) |
| Input value for target probability | x = [ln(p/(1 − p)) − b₀ − other terms] / bᵢ |
| Weighted decision matrix | Σ weight × score |
| RPN (if using FMEA) | Severity × Occurrence × Detection |

## Which tool when

| Question | Tool |
|---|---|
| What's the biggest problem? | Pareto (by cost and count) |
| Where does the process allow the problem in? | Process map, swim lanes |
| What could cause it? | Fishbone |
| Why did it happen? | 5-Why (single chain), root cause tree (combined causes) |
| Where is it concentrated? | Stratification |
| Is X related to Y? | Scatter + correlation; regression |
| Which of several Xs matter? | Multiple regression (continuous Y), logistic (pass/fail Y) |
| Which fix? | Error-proofing strength ranking, decision matrix |
| Is it fixed? | Corrective action matrix + process behavior chart |
