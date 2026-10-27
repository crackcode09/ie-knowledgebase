# Formulas

**Central tendency and variation**

- Mean x̄ = Σx / n
- Sample SD s = √(Σ(x − x̄)² / (n − 1))
- IQR = Q3 − Q1; high outlier if x > Q3 + 1.5 × IQR
- CV = s / x̄

**Association rules (A → B)**

- support = P(A ∩ B)
- confidence = support(A ∪ B) / support(A)
- lift = confidence / support(B) (1 means independent)

**Hypothesis tests**

- Two proportions: pooled p̂ = (x₁ + x₂) / (n₁ + n₂); z = (p̂₂ − p̂₁) / √(p̂(1 − p̂)(1/n₁ + 1/n₂))
- 95 % CI for p₂ − p₁ ≈ (p̂₂ − p̂₁) ± 1.96 √(p̂₁(1 − p̂₁)/n₁ + p̂₂(1 − p̂₂)/n₂)
- Welch t = (x̄₁ − x̄₂) / √(s₁²/n₁ + s₂²/n₂)

**Regression**

- ŷ = b₀ + b₁x₁ + … + bₖxₖ (least squares)
- R² = 1 − SSE / SST; adjusted R² = 1 − (1 − R²)(n − 1)/(n − k − 1)
- MAE = mean|e|; RMSE = √mean(e²); MAPE = mean|e / y|

**Classification**

- Accuracy = (TP + TN) / N
- Precision = TP / (TP + FP)
- Recall = TP / (TP + FN)
- F1 = 2TP / (2TP + FP + FN)

**Decision**

- Expected value = Σ pᵢ × valueᵢ − cost
- Call list net = (churners reached × save rate × customer value) − (calls × cost per call)
