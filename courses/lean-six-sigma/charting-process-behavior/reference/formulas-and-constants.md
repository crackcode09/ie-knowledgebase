# Formulas & Constants — One-Page Reference

## Variables charts

| Chart | Center | Lower limit | Upper limit |
|---|---|---|---|
| X (individuals) | X̄ | X̄ − 2.66 mR̄ | X̄ + 2.66 mR̄ |
| mR | mR̄ | — | 3.268 mR̄ |
| X̄ (with R) | X̿ | X̿ − A₂R̄ | X̿ + A₂R̄ |
| R | R̄ | D₃R̄ | D₄R̄ |
| X̄ (with S) | X̿ | X̿ − A₃s̄ | X̿ + A₃s̄ |
| S | s̄ | B₃s̄ | B₄s̄ |

σ̂_within = mR̄/1.128 = R̄/d₂ = s̄/c₄

## Attribute charts

| Chart | Center | Limits |
|---|---|---|
| p | p̄ = Σd/Σn | p̄ ± 3√[p̄(1−p̄)/nᵢ] |
| np | np̄ | np̄ ± 3√[np̄(1−p̄)] |
| c | c̄ | c̄ ± 3√c̄ |
| u | ū = Σc/Σa | ū ± 3√(ū/aᵢ) |

Negative lower limits → 0.

## Capability

Cp = (USL−LSL)/6σ_within  Cpk = min(USL−μ, μ−LSL)/3σ_within
Pp = (USL−LSL)/6s     Ppk = min(USL−μ, μ−LSL)/3s

## Constants (subgroup size n)

| n | d₂ | d₃ | A₂ | D₃ | D₄ |
|---|---|---|---|---|---|
| 2 | 1.128 | 0.853 | 1.880 | 0 | 3.267 |
| 3 | 1.693 | 0.888 | 1.023 | 0 | 2.574 |
| 4 | 2.059 | 0.880 | 0.729 | 0 | 2.282 |
| 5 | 2.326 | 0.864 | 0.577 | 0 | 2.114 |
| 6 | 2.534 | 0.848 | 0.483 | 0 | 2.004 |
| 7 | 2.704 | 0.833 | 0.419 | 0.076 | 1.924 |
| 8 | 2.847 | 0.820 | 0.373 | 0.136 | 1.864 |
| 9 | 2.970 | 0.808 | 0.337 | 0.184 | 1.816 |
| 10 | 3.078 | 0.797 | 0.308 | 0.223 | 1.777 |

A₂ = 3/(d₂√n); D₄ = 1 + 3d₃/d₂; D₃ = max(0, 1 − 3d₃/d₂). Every value is recomputed by numerical integration in `tools/check_constants.py`.

For X̄–S, n = 5: c₄ = 0.9400, A₃ = 1.427, B₃ = 0, B₄ = 2.089 (c₄ = √[2/(n−1)]·Γ(n/2)/Γ((n−1)/2); A₃ = 3/(c₄√n); B₄ = 1 + 3√(1−c₄²)/c₄).

## Detection rules (Western Electric zone tests)

1. One point beyond 3σ
2. 2 of 3 successive beyond 2σ, same side
3. 4 of 5 successive beyond 1σ, same side
4. 8 successive on one side of the center line
