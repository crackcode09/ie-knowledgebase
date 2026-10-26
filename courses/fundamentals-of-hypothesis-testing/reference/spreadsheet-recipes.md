# Spreadsheet Recipes (Excel / Google Sheets)

| Task | Formula |
|---|---|
| Mean, SD | `=AVERAGE(A2:A21)`, `=STDEV.S(A2:A21)` |
| One-sample t statistic | `=(AVERAGE(A2:A21)-25)/(STDEV.S(A2:A21)/SQRT(COUNT(A2:A21)))` |
| Two-sided p from t | `=T.DIST.2T(ABS(t), df)` |
| t critical (95%, two-sided) | `=T.INV.2T(0.05, df)` |
| CI half-width for a mean | `=CONFIDENCE.T(0.05, STDEV.S(A2:A21), COUNT(A2:A21))` |
| Welch two-sample t p-value | `=T.TEST(A2:A16, B2:B16, 2, 3)` (tails = 2, type 3 = unequal variance) |
| Pooled two-sample t p-value | `=T.TEST(A2:A16, B2:B16, 2, 2)` |
| Paired t p-value | `=T.TEST(B2:B13, C2:C13, 2, 1)` |
| z p-value (one-sided upper) | `=1-NORM.S.DIST(z, TRUE)` |
| Exact binomial upper p, P(X ≥ d) | `=1-BINOM.DIST(d-1, n, p0, TRUE)` |
| Chi-square p from statistic | `=CHISQ.DIST.RT(chi2, df)` |
| Chi-square test on a table | `=CHISQ.TEST(observed_range, expected_range)` |
| F test p (two-sided) | `=F.TEST(A2:A17, B2:B17)` |
| One-variance chi-square p (upper) | `=CHISQ.DIST.RT((n-1)*s^2/sigma0^2, n-1)` |
| ANOVA | Data → Data Analysis → *Anova: Single Factor* (Excel Analysis ToolPak) |

Nonparametric tests (Mann–Whitney, Wilcoxon, Kruskal–Wallis) have no built-in spreadsheet function; use `tools/htest.py` or rank the data with `RANK.AVG` and follow a textbook procedure.
