# Formulas — One-Page Reference

| Topic | Formula |
|---|---|
| Survey sample size (proportion) | n = z²p(1 − p)/E²; finite population: n / [1 + (n − 1)/N] |
| QFD technical importance | Σ (need importance × relationship 9/3/1) |
| Cp, Cpk | (USL − LSL)/6σ; min(USL − μ, μ − LSL)/3σ |
| DPMO | P(out of spec) × 10⁶ = defects / (units × opportunities) × 10⁶ |
| Sigma level (convention) | Z_bench + 1.5 |
| RPN | S × O × D |
| Step yield (Poisson) | Y = e^(−DPU) |
| RTY | Π step yields |
| 2^k factorial effect | mean(y at +) − mean(y at −); coded coefficient = effect / 2 |
| Worst-case stack | nominal ± Σ tolᵢ |
| RSS stack | nominal ± √(Σ tolᵢ²) |
| Little's law | WIP = TH × FT |
| Utilization | u = arrival rate × mean service time = tₑ/tₐ |
| Kingman wait | Wq ≈ [(cₐ² + cₑ²)/2] · [u/(1 − u)] · tₑ |
| Takt time | available time / demand |
| Minimum stations | ⌈total work content / takt⌉ |
| Balance efficiency | total work content / (stations × takt) |
| Weibull reliability | R(t) = exp[−(t/η)^β] |
| B10 life | η(−ln 0.9)^(1/β) |
| Success-run sample size | n = ln(1 − C) / ln(R) |

## Sigma level ↔ DPMO (1.5σ shift convention)

| Sigma level | 3 | 4 | 5 | 6 |
|---|---|---|---|---|
| DPMO | 66,807 | 6,210 | 233 | 3.4 |
