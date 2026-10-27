# Formulas and Cheat Sheet

| Item | Formula |
|---|---|
| AHP weights | Principal eigenvector of the pairwise matrix (or normalized row geometric means) |
| AHP consistency | CI = (λmax − n)/(n − 1); CR = CI/RI; CR < 0.10 acceptable (RI from Saaty's tables) |
| Additive value model | V = Σ wᵢ vᵢ(xᵢ), with vᵢ from 0 (worst) to 1 (best) |
| Swing weights | wᵢ = points for swingᵢ ÷ Σ points |
| Borda count | Σ over voters of (number of alternatives − rank position) |
| Kemeny-Young | The ranking that maximizes the total pairwise agreements with voters |
| Majority judgement | Rank by median grade; break ties by removing median grades in turn |
| Lognormal from P10/P50/P90 | μ = ln P50; σ ≈ [ln(P90) − ln(P10)] ÷ (2 × 1.2816) |
| FSD (X over Y) | F_X(t) ≤ F_Y(t) for all t |
| SSD (X over Y) | ∫ F_X ≤ ∫ F_Y up to every t |
| EMV | Σ p × payoff, rolled back through the tree |
| Exponential utility | u(x) = 1 − e^(−x/R) |
| Certainty equivalent | CE = −R ln(1 − E[u]) |
| Risk premium | EMV − CE |
| Zero-sum mixed strategy (LP) | max v s.t. Σᵢ xᵢ aᵢⱼ ≥ v ∀j, Σ xᵢ = 1, x ≥ 0 |
| Nash equilibrium | No player gains by changing strategy alone |
| Search reservation price (uniform a–b, cost c) | r = a + √(2c(b − a)) |
| Secretary rule | Reject the first k ≈ n/e, then take the first better than all seen |
| Bayes | P(S \| F) = P(F \| S) P(S) / P(F) |
| EVPI | EV with perfect information − EMV without information |
| EVII (EVSI) | EV with the information (best decision for each result) − EMV without |
| ROC | TPR = TP/(TP + FN); FPR = FP/(FP + TN); AUC = P(score of a failing unit > score of a healthy one) |
| Expected alarm cost | FP × cost(false alarm) + FN × cost(miss) |
| PPV | TP/(TP + FP) |
| Break-even probability | p where EMV(A) = EMV(B) |
