# Module 11 — Capstone and Skill Check

## Part A — End-to-end analysis

Using the Corbin data (or your own, with at least two sources to merge), produce:

1. **Data inventory and dictionary** for the sources used (Module 01).
2. **Merged analysis table** with documented joins and validation (Module 02).
3. **Preparation log** — each issue found and how it was handled (Module 03).
4. **Descriptive summary** by the relevant groups (Module 04).
5. **One inferential analysis** — ANOVA, regression or a nonparametric test — with assumptions checked and effect size reported (Modules 05–07).
6. **One predictive model** with cross-validated accuracy against a baseline and a chosen threshold or prediction interval (Module 09).
7. **A dashboard** answering 3–4 operational questions (Module 10).
8. **A one-page recommendation** for a decision maker.

**Review criteria:** correct grain and no fan-out; preparation reproducible; claims match the evidence (association vs cause); accuracy measured on unseen data; dashboard answers specific questions; recommendation states value and uncertainty.

## Part B — Skill check

1. A table of orders (1 row per order) is joined to shipments (several per order). Total order value triples. Why, and how do you fix it?
2. Three seal temperatures read 329, 331 and 334. What happened, and what is the fix?
3. One-way ANOVA: F = 4.2, p = 0.02, η² = 0.01, n = 2,000. What do you report?
4. Regression coefficient for pressure is 1.42 N/bar. Interpret it.
5. Downtime data is heavily skewed with 12 observations per group. Which test compares three groups?
6. Bootstrap: what is resampled, and why?
7. In a 2³ factorial, how is the main effect of A computed?
8. A model's CV RMSE is 0.95 and the measurement noise floor is 0.92. Next step?
9. Why must trend features use only past data?
10. Name three design rules for an operations dashboard.

<details><summary>Answers</summary>

1. Fan-out from a one-to-many join. Aggregate shipments to one row per order (or keep values only at the order level) before joining; use a uniqueness check.
2. Values logged in °F; convert with (°F − 32) × 5/9 → about 165–168 °C, after confirming the cause.
3. The difference is statistically significant but explains only 1 % of the variation — likely of little practical importance.
4. Holding temperature, dwell, supplier and line constant, each extra bar of pressure adds about 1.42 N on average (within the range studied).
5. Kruskal-Wallis.
6. The observed data, with replacement, many times; to see how much a statistic (e.g. the median) varies from sample to sample, giving a confidence interval without a formula.
7. Mean response at A high minus mean response at A low (each averaged over all levels of B and C).
8. Stop tuning the model; improve measurement (more or better tests) or accept the current accuracy.
9. To avoid leakage — at prediction time future data don't exist, so using them inflates accuracy falsely.
10. Any three: start from questions; KPIs top-left; consistent colors; show targets/limits; trends over snapshots; useful interactivity; state data freshness and definitions.

</details>
