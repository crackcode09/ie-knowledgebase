# Formula Sheet

Every symbol is defined where it is used, and a symbol means the same thing throughout the course. Sources are cited by the IDs in `sources.md`.

## Yield and defect metrics (george-2005 for rolled throughput yield, DPU and DPMO; montgomery-8e for the sigma-level convention)

| Formula | Symbols |
|---|---|
| Rolled throughput yield: RTY = Π Yᵢ | Yᵢ = first-pass yield of step i (fraction); Π = product over all steps |
| Defects per unit: DPU = D / U | D = defects counted; U = units inspected |
| DPMO = 10⁶ · D / (U · O) | O = defect opportunities per unit (5 for a Bayline insert: OD, thread, burr, knurl, length) |
| Sigma level (short-term convention) = Φ⁻¹(1 − DPMO / 10⁶) + 1.5 | Φ⁻¹ = inverse of the standard normal distribution; the +1.5 is the conventional long-term to short-term shift, not a law (module 03) |

## Descriptive and inferential statistics (montgomery-8e)

| Formula | Symbols |
|---|---|
| Sample mean: x̄ = Σxᵢ / n | xᵢ = the i-th observation; n = number of observations; x̄ estimates the population mean μ |
| Sample standard deviation: s = √[Σ(xᵢ − x̄)² / (n − 1)] | s estimates the population standard deviation σ |
| Confidence interval for the mean: x̄ ± t₀.₉₇₅,ₙ₋₁ · s / √n | t₀.₉₇₅,ₙ₋₁ = the 97.5th percentile of Student's t with n − 1 degrees of freedom (gives a 95 % interval) |

## Sample size (montgomery-8e)

| Formula | Symbols |
|---|---|
| To estimate a mean within ±E: n = (z · σ / E)² | E = half-width of the interval you want (same units as the data); σ = standard deviation, estimated from prior data (s); z = standard normal quantile for the confidence level, 1.96 for 95 % |
| To estimate a proportion within ±E: n = z² · p(1 − p) / E² | p = the proportion you expect (use 0.5 if unknown; it gives the largest n); E in the same units as p |

## Gauge R&R, crossed design, ANOVA method (aiag-msa-4)

Design: p parts, o operators, r trials of every part by every operator. The two-way ANOVA gives mean squares MS_P (parts), MS_O (operators), MS_PO (part-by-operator interaction) and MS_E (error, within-trial).

| Variance component | Formula |
|---|---|
| Repeatability (equipment variation): σ²_rep = MS_E | |
| Interaction: σ²_int = (MS_PO − MS_E) / r | pooled into repeatability when the interaction is not significant |
| Operator (appraiser variation): σ²_op = (MS_O − MS_PO) / (p · r) | |
| Part: σ²_part = (MS_P − MS_PO) / (o · r) | |
| Gauge R&R: σ²_GRR = σ²_rep + σ²_op + σ²_int | reproducibility = σ²_op + σ²_int |
| Total: σ²_total = σ²_GRR + σ²_part | |

Negative component estimates are set to zero.

| Summary measure | Symbols |
|---|---|
| %Study variation = 100 · σ_component / σ_total | σ = square root of the variance component above |
| %Tolerance = 100 · 6 · σ_GRR / (USL − LSL) | USL, LSL = upper and lower specification limits; 6σ spans 99.73 % of a normal distribution |
| Number of distinct categories: ndc = ⌊1.41 · σ_part / σ_GRR⌋ | ⌊ ⌋ = round down to an integer |

## Attribute agreement (cohen-1960 for the formula; landis-koch-1977 and aiag-msa-4 for the interpretation bands)

| Formula | Symbols |
|---|---|
| Cohen's kappa: κ = (p_o − p_e) / (1 − p_e) | p_o = observed proportion of agreement; p_e = proportion of agreement expected by chance from the marginal totals; κ = 1 is perfect agreement, 0 is chance |

## Control charts (montgomery-8e)

| Chart | Limits | Symbols |
|---|---|---|
| I (individuals) | x̄ ± 2.66 · MR̄ | x̄ = mean of the individual values; MR̄ = mean of the moving ranges \|xᵢ − xᵢ₋₁\|; 2.66 = 3 / d₂ for n = 2 |
| MR (moving range) | UCL = 3.267 · MR̄, LCL = 0 | 3.267 = D₄ for n = 2 |
| X̄ (subgroup means) | X̿ ± A₂ · R̄ | X̿ = grand mean of the subgroup means; R̄ = mean subgroup range; A₂ = 0.577 for subgroups of n = 5 |
| R (subgroup ranges) | UCL = D₄ · R̄, LCL = D₃ · R̄ | D₃ = 0 and D₄ = 2.114 for n = 5 |
| p (fraction defective) | p̄ ± 3 · √[p̄ (1 − p̄) / n] | p̄ = overall fraction defective; n = subgroup size; a negative LCL is set to 0 |

A₂, D₃, D₄ and d₂ are tabulated constants that depend only on the subgroup size n; the course gives the n = 5 and n = 2 values it uses.

## Capability (montgomery-8e)

| Formula | Symbols |
|---|---|
| Cp = (USL − LSL) / (6 · σ_within) | σ_within = short-term standard deviation estimated from within-subgroup variation (R̄ / d₂ or MR̄ / 1.128); Cp is potential capability, ignoring centering |
| Cpk = min(USL − μ, μ − LSL) / (3 · σ_within) | μ = process mean (estimated by X̿); Cpk is actual capability, penalised for off-centre running |
| Pp and Ppk | the same two formulas with the overall standard deviation s of all the data in place of σ_within; they describe performance over the whole period, including shifts and drift |

Both indices assume a stable process and approximately normal data; transform or use a distribution-specific method otherwise (module 04).

## Regression (montgomery-8e)

| Formula | Symbols |
|---|---|
| ŷ = b₀ + b₁x₁ + b₂x₂ + … | ŷ = predicted response; b₀ = intercept; bₖ = estimated coefficient of predictor xₖ (change in ŷ per unit of xₖ, other predictors held fixed) |
| R² = 1 − SS_residual / SS_total | share of the variation in y explained by the model; SS = sum of squares |

## FMEA (aiag-vda-fmea)

| Formula | Symbols |
|---|---|
| RPN = S × O × D | S = severity of the effect, O = likelihood of occurrence, D = likelihood that current controls fail to detect it; each rated 1 (best) to 10 (worst) on the team's agreed scales |

The AIAG-VDA handbook replaces RPN with an Action Priority table that ranks S, O and D in that order; module 05 explains both.

## Reliability, exponential model (montgomery-8e; see Reliability Engineering Excellence for depth)

| Formula | Symbols |
|---|---|
| R(t) = e^(−λt) = e^(−t / MTBF) | R(t) = probability of surviving to time t; λ = constant failure rate; MTBF = mean time between failures = 1 / λ. Valid only when the failure rate is constant over time |
| Series system: R_sys = Π Rᵢ; λ_sys = Σ λᵢ | Rᵢ, λᵢ = reliability and failure rate of component i; the system fails if any component fails |
| Two identical units in parallel (1-of-2): R_sys = 1 − (1 − R_unit)² | R_unit = reliability of one unit; the system fails only if both fail |

## Two-proportion test (montgomery-8e)

| Formula | Symbols |
|---|---|
| z = (p̂₁ − p̂₂) / √[p̄ (1 − p̄)(1/n₁ + 1/n₂)] | p̂₁ = x₁/n₁ and p̂₂ = x₂/n₂ = observed proportions in the two samples; xᵢ = defectives, nᵢ = inspected; p̄ = (x₁ + x₂) / (n₁ + n₂) = pooled proportion under the hypothesis that the two are equal |
