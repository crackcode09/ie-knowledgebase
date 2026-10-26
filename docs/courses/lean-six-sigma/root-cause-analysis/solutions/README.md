# Solutions

Module check answers are inside each module. Below: capstone Option B and an instructor summary. All values regenerate with `python tools/make_data.py` and `python tools/rca.py all`.

## Capstone Option B

1. **Non-leak scrap by cost:** Bore oversize $3,800 (47.6%), Thread damage $1,710 (21.4%) … Bore oversize by machine: MC1 11, MC2 13, MC3 16; by shift: Day 21, Night 19. No stratum stands out — a chi-square goodness-of-fit test against equal machines gives a large p-value (try it). Unlike leaks, bore oversize looks like a common-cause problem across the cell: look at the process design (offset method, gauging) rather than one machine.
2. **Ra × torque interaction:** p = 0.67; adjusted R² falls from 0.797 to 0.794. No interaction — keep the additive model.
3. **Torque for P(fail) ≤ 5% at Ra = 0.65 µm:** solve b₀ + b₁(0.65) + b₂·T = ln(0.05/0.95) → **T ≈ 24.7 N·m**. Within the 26 N·m ceiling, but near it, and the decision matrix flagged distortion risk at high torque. Torque alone is a weak lever; controlling roughness (tool life / in-process Ra) remains the primary fix.
4. Example matrix row: "Bore oversize — common-cause across cell — review offset/gauging method; owner: process engineer; verify with X̄–R chart of bore after change."

## Instructor summary

| Module | Key result |
|---|---|
| 3 Pareto | Leaks 42.5% of count, 59.8% of cost |
| 8 Stratification | Leaks MC1 16, MC2 19, MC3 50; χ² = 15.4, p = 0.0004; shift no difference |
| 9 Correlation | r = 0.955 (tool hours vs Ra) |
| 10 Regression | Ra = 0.307 + 0.0199·h; R² 0.91; s 0.073; mean hits 0.80 µm at 24.7 h |
| 11 Multiple regression | Leak = 4.79 + 3.43·Ra − 0.135·torque; R² 0.804; humidity, temperature, gasket not significant |
| 12 Logistic | OR 2.05 per +0.1 µm Ra, 0.69 per +1 N·m; Ra ≤ 0.51 µm for P(fail) ≤ 5% at 22 N·m |
| 14 Decision matrix | Ra gauge 69, tool interval 63, torque 53, retest 41 |
