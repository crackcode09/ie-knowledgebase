# Formula Sheet

## Descriptive statistics

- Mean: x̄ = Σx / n
- Sample variance: s² = Σ(x − x̄)² / (n − 1)
- Range: R = max − min
- IQR = Q3 − Q1

## Control-chart constants (computed by `sqckit.py`)

- d₂(n) = E[range of n standard normals]
- d₃(n) = SD of that range
- A₂ = 3 / (d₂√n)
- D₃ = max(0, 1 − 3d₃/d₂)
- D₄ = 1 + 3d₃/d₂

| n | d₂ | d₃ | A₂ | D₃ | D₄ |
|---|---|---|---|---|---|
| 2 | 1.128 | 0.853 | 1.880 | 0 | 3.267 |
| 3 | 1.693 | 0.888 | 1.023 | 0 | 2.575 |
| 4 | 2.059 | 0.880 | 0.729 | 0 | 2.282 |
| 5 | 2.326 | 0.864 | 0.577 | 0 | 2.114 |
| 6 | 2.534 | 0.848 | 0.483 | 0 | 2.004 |
| 7 | 2.704 | 0.833 | 0.419 | 0.076 | 1.924 |
| 8 | 2.847 | 0.820 | 0.373 | 0.136 | 1.864 |
| 9 | 2.970 | 0.808 | 0.337 | 0.184 | 1.816 |
| 10 | 3.078 | 0.797 | 0.308 | 0.223 | 1.777 |

## Charts

| Chart | Center | Limits |
|---|---|---|
| X̄ | X̿ | X̿ ± A₂R̄ |
| R | R̄ | D₃R̄, D₄R̄ |
| Individuals | x̄ | x̄ ± 2.66 MR̄ |
| Moving range | MR̄ | 0, 3.267 MR̄ |
| p | p̄ | p̄ ± 3√(p̄(1 − p̄)/nᵢ) |
| np | n p̄ | n p̄ ± 3√(n p̄ (1 − p̄)) |
| c | c̄ | c̄ ± 3√c̄ |
| u | ū | ū ± 3√(ū/nᵢ) |
| DNOM X̄ | mean deviation | ± A₂R̄ on the deviations |
| Z (standardized) | 0 | ±3 |

Any negative lower limit is set to 0.

## Capability

- Cp = (USL − LSL) / 6σ_within
- Cpk = min(USL − μ, μ − LSL) / 3σ_within
- Pp and Ppk: the same formulas with σ_overall
- σ_within = R̄/d₂ or MR̄/1.128
- ppm = 10⁶ [P(Z > (USL − μ)/σ) + P(Z < (LSL − μ)/σ)]

## Acceptance sampling

- Single plan: P(accept) = Σ_{d=0}^{c} C(n, d) pᵈ(1 − p)ⁿ⁻ᵈ (binomial). Use the hypergeometric distribution when the lot is small relative to the sample.
- Producer's risk = 1 − P(accept at AQL)
- Consumer's risk = P(accept at LTPD)
- AOQ = P(accept) · p · (N − n)/N; AOQL = max AOQ
- ATI = n + (1 − P(accept))(N − n)
- Double plan:
  - P(accept) = P(d₁ ≤ c₁) + Σ_{d₁=c₁+1}^{r₁−1} P(d₁) · P(d₂ ≤ c₂ − d₁)
  - ASN = n₁ + n₂ · P(c₁ < d₁ < r₁)
