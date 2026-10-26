# Solutions and Teaching Notes

All values come from `python tools/doekit.py all`, using the data generated with seed 1935.

## Results

| Example | Key result |
|---|---|
| CRD (01) | F(3,20) = 6.57, p = 0.0029. Tukey HSD = 4.90 MPa; only S4 − S3 (7.58) is significant. Levene p = 0.43 |
| RCBD (02) | Agent F(3,12) = 5.70, p = 0.012 with molds blocked. Ignoring blocks: F = 0.46, p = 0.72 |
| Latin square (03) | Program F(3,6) = 20.8, p = 0.0014; machine F = 19.4; day F = 3.60 (p = 0.085). Best program: C, 30.41 s |
| Two-factor (04) | SS: A 0.09203, B 0.21391, AB 0.00391, E 0.01465. F: 56.5, 131.4, 1.20 (p = 0.34) |
| Unbalanced (05) | Type I SS_temp = 0.0411 (temp first) vs 0.0804 (temp second). Type III: 0.0819, 0.1725, 0.0048 |
| Replicates (06) | Power for a 0.05-point cell gap: n = 2: 0.43, 3: 0.64, 4: 0.78, 5: 0.87, 6: 0.92 |
| 2^4 factorial (07) | Active effects: B −27.35, C −21.55, D −17.02, BC +14.35, A +13.05. Lenth ME 3.95. R² 0.987. Curvature p = 0.19 |
| 2^(5−1) (08) | Active effects: C 19.35, E 11.50, CE 7.45, A 5.75, B 2.03. Lenth ME 1.85 |
| Operating levels (09) | 6 of 16 settings meet ≤ 110 µm. Cheapest: A−, B+, C+, D− at 104.1 µm, 27.5 s, $0.33 |

## Teaching notes

- **Module 02** is the strongest "aha" in the course. Show the CRD analysis first and ask the class whether release agents matter. Then add the block.
- **Module 04:** have learners fill the SS table by hand from the cell-mean table before running code. Rounding to 4 decimals reproduces the code to about 3 significant figures.
- **Module 05:** the order dependence surprises people who learned ANOVA only on balanced data. Stress reporting the SS type.
- **Module 07:** AD (3.88) sits just under Lenth's ME (3.95). Use it to discuss borderline effects, and why confirmation runs beat arguing about p-values.
- **Module 09:** the cost model is illustrative. Ask learners to substitute their own machine rate and scrap cost and see whether the decision changes.
- **Simulated data:** the true models are in `make_data()` in `tools/doekit.py`. For example, the true BC interaction coefficient is +7, and the estimate is +7.18. Revealing them after the analysis shows how well each design recovered the truth.
