# Solutions and Instructor Notes

Module checks and the skill-check answers are inside the modules. Running-case results (`python tools/statkit.py all`, seed 1662):

| Item | Result |
|---|---|
| Cycle time | mean 61.89, median 61.75, sd 2.35, skew −0.07, kurtosis −0.17 |
| Rework time | mean 15.22, median 13.75, sd 8.20, skew 1.38, kurtosis 3.24 |
| Hypergeometric | N 500, K 10, n 50, c 1: P(accept) 0.737 |
| Binomial | n 25, p 0.04: P(0) 0.360, P(≥3) 0.077 |
| Poisson | λ 0.82; P(defect-free) 0.44 |
| Normal | P(cycle > 68 s) = 0.0047 (4,677 ppm); 95th pct 65.8 s |
| Exponential | MTBF 63.2 h (CI 47.4–88.5); P(no failure in 8 h) 0.881 |
| CIs | mean 61.47–62.31; sd 2.09–2.69; proportion 0.521–0.656 (Wilson) |
| Tests | mean vs 61: p 0.0001; P2 vs P1 variance F 3.14, p 0.0069; means Welch p 0.019 |
| Non-normal | log Shapiro p 0.21; Box–Cox λ 0.20; median CI 11.8–15.8 |
| Correlation | revenue–orders 0.946; revenue–quote days 0.004 |
| Simple regression | revenue = −2.1 + 2.924 × orders; R² 0.895; PI at 500 orders 1,310–1,610 |
| Multiple regression | quote days −28.9 k$/day (p 0.0004) once orders held constant; R² 0.945 |

## Teaching notes

- **Module 2:** let learners change n and c in the hypergeometric OC curve to design a better sampling plan.
- **Module 4:** rerun the CLT demonstration with n = 10 and n = 50.
- **Modules 8–10:** the key insight is masking — ask learners to predict, from the correlation table alone, which drivers matter, before revealing the multiple regression.
- Data are synthetic; coefficients and p-values are teaching values.
