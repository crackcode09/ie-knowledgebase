# Module 12 — Wrap-Up and Skill Check

**Time:** 30 min + optional mini-project

## Part A — Quiz (answers below)

1. 300 parts are inspected for 4 characteristics each; 9 defects are found on 7 parts. Compute DPU, DPMO and first-pass yield.
2. Classify: (a) number of late orders per week; (b) customer region; (c) shaft runout in µm; (d) satisfaction 1–5.
3. A gauge reads a 10.000 mm block as 10.012, 10.011, 10.013, 10.012. Accurate? Precise?
4. Downtime by cause: Jams 120 min, Changeover 340 min, Waiting for material 90 min, Breakdowns 410 min, Other 40 min. Build the Pareto table (%, cumulative %). Which causes make up about three-quarters of the downtime?
5. Data: 4, 5, 5, 6, 30. Mean, median, mode. Which describes a typical value?
6. For the data in Q5, compute the range and the standard deviation.
7. A histogram of fill weight has two peaks. What's the most likely explanation and next step?
8. μ = 200 g, σ = 4 g, LSL = 190 g. What fraction is below the LSL, assuming normality?
9. Two suppliers both average 25.00 mm; s = 0.02 vs 0.08. Tolerance ± 0.15. Which do you choose and why?
10. Give one reason a plant-wide average can be misleading.

<details><summary>Answers</summary>

1. DPU = 9/300 = 0.03. DPMO = 9/(300 × 4) × 10⁶ = 7,500. First-pass yield = 293/300 = 97.7%.
2. (a) discrete, ratio; (b) discrete, nominal; (c) continuous, ratio; (d) discrete, ordinal.
3. Precise (readings within 0.002) but not accurate (bias ≈ +0.012).
4. Total 1,000 min. Breakdowns 41.0% (41.0), Changeover 34.0% (75.0), Jams 12.0% (87.0), Waiting 9.0% (96.0), Other 4.0% (100.0). Breakdowns + changeover = 75% — the top two causes.
5. Mean 10, median 5, mode 5. The median (or mode) — 30 is an outlier pulling the mean.
6. Range 26. s = √[(36 + 25 + 25 + 16 + 400)/4] = √125.5 ≈ 11.2.
7. Two sources mixed (e.g., two filling heads). Stratify by head and look at each.
8. z = (190 − 200)/4 = −2.5 → about 0.62%.
9. The s = 0.02 supplier: ±0.15 is 7.5 s away vs 1.9 s for the other (about 6% out of spec, if normal).
10. It can hide a poorly performing shift/line, or describe a value that no actual unit has (bimodal data).
</details>

## Part B — Mini-project (optional)

Pick one process you work with and:

1. Write an operational definition for one CTQ measurement.
2. Collect 30–50 values in time order, with at least one grouping variable (machine, shift, supplier).
3. Make a Pareto chart of defects or complaints by category — by count and by cost.
4. Make a histogram; describe shape, center (mean, median) and spread (SD, IQR).
5. Compare groups: does any group differ in center or spread?
6. Estimate the fraction out of spec with the normal model, and say whether you trust it.

Then continue with *Charting Process Behavior* to check whether the process is stable over time.
