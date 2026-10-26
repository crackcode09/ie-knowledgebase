# Formula Sheet

## Yield and defect metrics

- Rolled throughput yield: RTY = Π (yield of each step)
- DPU = defects / units
- DPMO = 10⁶ × defects / (units × opportunities per unit)
- Sigma level (short-term convention) = Φ⁻¹(1 − DPMO/10⁶) + 1.5

## Descriptive and inferential statistics

- Mean: x̄ = Σx / n
- Sample standard deviation: s = √[Σ(x − x̄)² / (n − 1)]
- Confidence interval for the mean: x̄ ± t(0.975, n − 1) · s/√n

## Sample size

- To estimate a mean within ±E: n = (z σ / E)²
- To estimate a proportion within ±E: n = z² p(1 − p) / E²
- z = 1.96 for 95% confidence

## Gauge R&R (crossed design: p parts, o operators, r trials; ANOVA mean squares)

Variance components:

- Repeatability: σ²_rep = MS_E
- Interaction: σ²_int = (MS_PO − MS_E) / r
- Operator: σ²_op = (MS_O − MS_PO) / (p r)
- Part: σ²_part = (MS_P − MS_PO) / (o r)
- Gauge R&R: σ²_GRR = σ²_rep + σ²_op + σ²_int

Summary measures:

- %Study variation = 100 · σ_component / σ_total
- %Tolerance = 100 · 6σ_GRR / (USL − LSL)
- ndc = ⌊1.41 · σ_part / σ_GRR⌋

## Attribute agreement

- Cohen's kappa: κ = (p_o − p_e) / (1 − p_e)
  - p_o = observed agreement
  - p_e = agreement expected by chance

## Control charts

| Chart | Limits |
|---|---|
| I | x̄ ± 2.66 MR̄ |
| MR | UCL = 3.267 MR̄ |
| X̄ | X̿ ± A₂R̄ (n = 5: A₂ = 0.577) |
| R | D₃R̄, D₄R̄ (n = 5: D₃ = 0, D₄ = 2.114) |
| p | p̄ ± 3√(p̄(1 − p̄)/n) |

## Capability

- Cp = (USL − LSL) / 6σ
- Cpk = min(USL − μ, μ − LSL) / 3σ
- Pp and Ppk: the same formulas using the overall standard deviation

## Regression

- ŷ = b₀ + b₁x₁ + …
- R² = share of variation in y that the model explains

## FMEA

- RPN = S × O × D

## Reliability (exponential model)

- R(t) = e^(−t/MTBF)
- Series system: R_sys = Π R_i; λ_sys = Σ λ_i
- Two units in parallel (1-of-2): R = 1 − (1 − R)²

## Two-proportion test

- z = (p₁ − p₂) / √[p̄(1 − p̄)(1/n₁ + 1/n₂)]
- p̄ = pooled proportion
