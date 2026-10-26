# Formula Sheet

## Metrics
- MTBF = total operating time / number of failures
- MTTR = total repair time / number of repairs
- Inherent availability A_i = MTBF / (MTBF + MTTR)
- Operational availability A_o = MTBF / (MTBF + MTTR + mean logistics and administrative delay)
- OEE = availability × performance × quality

## Exponential (constant failure rate λ)
- R(t) = e^(−λt); MTBF = 1/λ
- Number of failures in time t ~ Poisson(λt)
- Confidence interval for MTBF, failure-terminated test with r failures in total time T:
  - lower = 2T / χ²(1 − α/2, 2r)
  - upper = 2T / χ²(α/2, 2r)
  - here χ²(p, df) is the chi-square quantile at probability p
  - for a time-terminated test, use 2r + 2 degrees of freedom for the lower bound

## Normal (wear-out)
- P(fail before t) = Φ((t − μ)/σ)
- Change point for risk p = μ + z_p σ, where z_0.01 = −2.326

## Weibull
- R(t) = exp[−(t/η)^β]
- hazard h(t) = (β/η)(t/η)^(β−1)
- B_p life = η[−ln(1 − p)]^(1/β)
- mean = η Γ(1 + 1/β)
- Benard's median rank ≈ (i − 0.3)/(n + 0.4), with i the adjusted rank when there are suspensions
- Weibull plot axes: x = ln t; y = ln[−ln(1 − F)]

## System reliability
- Series: R = Π R_i
- Parallel (1-out-of-n): R = 1 − Π(1 − R_i)
- k-out-of-n, identical units: R = Σ_{j=k}^{n} C(n, j) R^j (1 − R)^(n−j)

## Reliability growth (Crow-AMSAA, time-terminated at T)
- Expected cumulative failures N(t) = λ t^β
- MLE: β̂ = n / Σ ln(T/t_i); λ̂ = n / T^β̂
- Instantaneous MTBF = 1 / (λ β T^(β−1))

## Age replacement
- C(T) = [C_p R(T) + C_f (1 − R(T))] / ∫₀ᵀ R(t) dt
- Run to failure: C = C_f / mean life

## P-F interval
- Inspection interval ≤ P-F / 2 (common rule)

## Economics
- LCC = PV(acquisition + installation + energy + maintenance + failure costs + disposal) − PV(salvage)
- Simple payback = extra investment / annual saving
- ROI = annual saving / extra investment
- Benefit–cost ratio = PV(savings) / investment
- Net return = NPV = PV(savings) − investment

## FMECA
- RPN = severity × occurrence × detection
