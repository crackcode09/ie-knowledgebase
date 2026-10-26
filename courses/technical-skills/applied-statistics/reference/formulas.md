# Formulas — One-Page Reference

## Descriptive

Mean x̄ = Σx/n · s = √[Σ(x − x̄)²/(n − 1)] · IQR = Q3 − Q1 · CV = s/x̄

## Distributions

| Distribution | P(X = x) or P(X > x) | Mean | Variance |
|---|---|---|---|
| Hypergeometric | C(K,x)C(N−K,n−x)/C(N,n) | nK/N | n(K/N)(1−K/N)(N−n)/(N−1) |
| Binomial | C(n,x)p^x(1−p)^(n−x) | np | np(1−p) |
| Poisson | e^(−λ)λ^x/x! | λ | λ |
| Normal | z = (x − μ)/σ | μ | σ² |
| Exponential | P(T > t) = e^(−t/MTBF) | MTBF | MTBF² |

## Intervals (95%)

| Parameter | Interval |
|---|---|
| Mean | x̄ ± t(0.025, n−1) s/√n |
| Proportion | p̂ ± 1.96√[p̂(1−p̂)/n] (Wilson for small n) |
| SD | √[(n−1)s²/χ²(0.975)] to √[(n−1)s²/χ²(0.025)] |
| MTBF (exponential, failure-terminated) | 2T/χ²(0.975, 2r) to 2T/χ²(0.025, 2r) |

## Test statistics

t = (x̄ − μ₀)/(s/√n) · z = (p̂ − p₀)/√[p₀(1−p₀)/n] · χ² = (n−1)s²/σ₀² · F = s₁²/s₂²

## Sample size

Mean: n = (z s / E)² · Proportion: n = z² p(1−p)/E²

## Regression

b₁ = Σ(x − x̄)(y − ȳ)/Σ(x − x̄)² · b₀ = ȳ − b₁x̄ · R² = 1 − SSE/SST · prediction interval: ŷ ± t s√[1 + 1/n + (x₀ − x̄)²/Σ(x − x̄)²]
