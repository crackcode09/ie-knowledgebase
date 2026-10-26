# Module 14 — Advanced Charts

**Time:** 60 min

## Learning objectives

1. Know when a basic chart is not enough and which advanced chart to use.
2. Understand the principles of X̄–S, EWMA, CUSUM, short-run and three-way charts.

Start with the basic charts. Advanced charts solve specific problems; they are not upgrades.

## 1. Selection guide

| Problem | Chart |
|---|---|
| Subgroups larger than ~10 | **X̄–S** |
| Need to detect small, sustained shifts (≈0.5–1.5σ) quickly | **EWMA** or **CUSUM** |
| Many part numbers, short runs, few points each | **Short-run (deviation-from-nominal or Z–MR)** |
| Subgroups have a real between-subgroup component you must live with (e.g., batch-to-batch) | **Three-way chart** (X̄ / mR of X̄ / R) |
| Data are autocorrelated (each value depends on the last: chemical processes, temperatures) | Chart residuals from a time-series model, or use wider sampling intervals |
| Several correlated characteristics | Multivariate (Hotelling T²) — specialist territory |

## 2. X̄–S chart

Same idea as X̄–R, but uses the subgroup standard deviation s (more efficient for large n).

- S chart: center s̄, limits B₃s̄ and B₄s̄
- X̄ chart: X̿ ± A₃s̄

Constants for n = 5: A₃ = 1.427, B₃ = 0, B₄ = 2.089 (verify in your SPC reference or derive from c₄: A₃ = 3/(c₄√n)).

## 3. EWMA — exponentially weighted moving average

zᵢ = λxᵢ + (1 − λ)zᵢ₋₁, z₀ = target or X̄

- λ between 0.05 and 0.3 (0.2 is common). Small λ = more memory = more sensitive to small shifts.
- Limits: X̄ ± L·σ·√[λ/(2−λ)·(1 − (1−λ)²ⁱ)], with L ≈ 2.7–3 (they widen to a steady state).
- Good for: slow drifts, small shifts, data that are not normal (averaging helps).

## 4. CUSUM — cumulative sum

Accumulate deviations from target beyond a slack value k (typically 0.5σ):

Cᵢ⁺ = max(0, xᵢ − (T + k) + Cᵢ₋₁⁺)
Cᵢ⁻ = max(0, (T − k) − xᵢ + Cᵢ₋₁⁻)

Signal when C⁺ or C⁻ exceeds h (typically 4σ–5σ). Detects small shifts (around 1σ) in far fewer points than a Rule-1-only X chart, and the point where C started climbing marks *when* the shift began. Exercise 14.2 lets you measure the difference by simulation.

## 5. Short-run charts

When a machine makes many parts with different nominals:

- **Deviation from nominal (DNOM):** plot xᵢ − nominal. Works when all parts have similar variation.
- **Z–MR (standardized):** plot (xᵢ − target)/σ_part. Works when variation differs by part.

Lets you put all parts on one chart and see the *machine's* behavior.

## 6. Three-way chart

When there's a true, uncontrollable between-subgroup component (e.g., 5 readings within a batch, batches differ routinely), an X̄–R chart flags every batch. A three-way chart puts the subgroup averages on an XmR chart (between-subgroup) plus an R chart (within-subgroup).

## Exercise 14.1

Implement an EWMA (λ = 0.2) on `data/shaft_diameter.csv` using the hours 1–20 mean and σ̂. At what hour does it first signal? Compare with the XmR detection in Module 7.

## Exercise 14.2

Simulate 2,000 runs of normal data (σ = 1) with a 1σ shift from the first point. Count how many points it takes, on average, for (a) Rule 1 on an X chart and (b) a CUSUM with k = 0.5, h = 5 to signal.

## Check yourself

1. Subgroups of 15 readings. Which chart?
2. Your X̄–R chart flags almost every subgroup, but the R chart is stable and nobody can find causes. What might be going on?

<details><summary>Answers</summary>

1. X̄–S.
2. A real between-subgroup component of variation (batches, setups) — consider a three-way chart, and check the subgrouping.
</details>
