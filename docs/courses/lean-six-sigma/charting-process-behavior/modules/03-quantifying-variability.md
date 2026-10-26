# Module 3 — Quantifying Variability

**Time:** 45 min · **Data:** `data/shaft_diameter.csv`

## Learning objectives

1. Compute range and standard deviation by hand.
2. Explain the difference between **within** (short-term) and **overall** (long-term) variation.
3. Estimate sigma from ranges using the bias-correction constant d₂.

## 1. Measures of spread

Using the first five shaft diameters (mm): 12.6937, 12.7019, 12.6848, 12.7112, 12.7051.

**Mean:** x̄ = 63.4967 / 5 = **12.69934**

**Range:** R = max − min = 12.7112 − 12.6848 = **0.0264**

**Sample standard deviation:**

s = √[ Σ(xᵢ − x̄)² / (n − 1) ]

| xᵢ | xᵢ − x̄ | (xᵢ − x̄)² |
|---|---|---|
| 12.6937 | −0.00564 | 0.00003181 |
| 12.7019 | 0.00256 | 0.00000655 |
| 12.6848 | −0.01454 | 0.00021141 |
| 12.7112 | 0.01186 | 0.00014066 |
| 12.7051 | 0.00576 | 0.00003318 |
| | **Σ** | **0.00042361** |

s = √(0.00042361 / 4) = √0.00010590 = **0.01029 mm**

The divisor n − 1 (not n) corrects the bias from estimating the mean from the same data.

## 2. Estimating sigma from ranges

The average range of samples from a normal process is proportional to σ:

  E[R] = d₂ · σ  →  σ̂ = R̄ / d₂

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
|---|---|---|---|---|---|---|---|---|---|
| d₂ | 1.128 | 1.693 | 2.059 | 2.326 | 2.534 | 2.704 | 2.847 | 2.970 | 3.078 |

These values are recomputed by numerical integration in `tools/check_constants.py`.

For individual values we use **moving ranges** — the absolute difference between consecutive points, a "subgroup" of size 2 — so σ̂ = mR̄ / 1.128.

## 3. Within vs overall variation

This is the most important idea in the module.

| | Within (short-term) | Overall (long-term) |
|---|---|---|
| Estimated from | Point-to-point differences (mR̄/d₂ or R̄/d₂) | Standard deviation of all data, s |
| Captures | Routine noise only | Routine noise **plus** any shifts, drifts, cycles |
| Used for | Control limits, Cp/Cpk | Pp/Ppk |

If the process is stable, the two are about equal. If the process shifted during the data, overall sigma is inflated but within sigma is not — and that is exactly why chart limits use within sigma: limits built from overall sigma would widen to swallow the very shift you want to detect.

**Shaft diameter, all 30 hours** (a shift occurs at hour 21 — see Module 6):

| Estimate | Value (mm) |
|---|---|
| Overall s | 0.0104 |
| Within, mR̄ / 1.128 | 0.0075 |
| Within, hours 1–20 only | 0.0057 |

Overall is ~40% larger than within: a hint the process was not stable across all 30 hours. (The within estimate on all 30 hours is also inflated, by the large moving range at the shift; that's why we compute limits from a stable baseline.)

## Exercise 3.1

Using hours 1–20 of `data/shaft_diameter.csv`, compute (a) the 19 moving ranges, (b) mR̄, (c) σ̂ = mR̄/1.128, (d) s. Compare (c) and (d).

<details><summary>Answer</summary>

mR̄ = 0.006426, σ̂ = 0.005697, s = 0.005927. They agree within ~4%, consistent with a stable baseline.
</details>

## Check yourself

1. Why do control limits use within-subgroup sigma instead of the overall standard deviation?
2. For subgroups of 4, the average range is 0.020. Estimate σ.

<details><summary>Answers</summary>

1. Overall sigma includes the effect of any shifts, which widens the limits and hides those shifts.
2. 0.020 / 2.059 = 0.0097.
</details>
