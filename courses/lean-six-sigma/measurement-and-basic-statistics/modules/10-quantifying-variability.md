# Module 10 — Quantifying Process Variability

**Time:** 35 min · **Data:** `data/shaft_diameter.csv`, `data/lead_time.csv`

## Learning objectives

1. Compute range, variance, standard deviation, IQR and coefficient of variation.
2. Choose a spread measure that fits the data.
3. Assess whether a process's variation is acceptable relative to its requirements.

## 1. Measures of spread

| Measure | Formula | Notes |
|---|---|---|
| **Range** | max − min | Simple; uses only two values; grows with n |
| **Variance** s² | Σ(x − x̄)² / (n − 1) | Units squared |
| **Standard deviation** s | √variance | Same units as the data; the standard measure |
| **IQR** | Q3 − Q1 | Middle 50%; robust to skew and outliers |
| **Coefficient of variation** | s / x̄ × 100% | Compares spread across different scales; ratio data only |

Why n − 1? Measuring deviations from the sample's own mean makes them slightly too small; dividing by n − 1 corrects that (Bessel's correction).

## 2. Hand calculation — five shaft diameters

x̄ = 12.7024

| x | x − x̄ | (x − x̄)² |
|---|---|---|
| 12.717 | 0.0146 | 0.00021316 |
| 12.704 | 0.0016 | 0.00000256 |
| 12.700 | −0.0024 | 0.00000576 |
| 12.699 | −0.0034 | 0.00001156 |
| 12.692 | −0.0104 | 0.00010816 |
| | **Σ** | **0.00034120** |

- Range = 12.717 − 12.692 = **0.025 mm**
- s² = 0.0003412 / 4 = 0.0000853 mm²
- s = √0.0000853 = **0.0092 mm**

## 3. Full data sets

| | Shaft diameter | Lead time |
|---|---|---|
| n | 100 | 60 |
| Range | 0.062 mm | 13.9 days |
| Standard deviation | 0.0103 mm | 3.27 days |
| IQR | 0.012 mm | 4.0 days |
| CV | 0.08% | 51% |

For skewed lead times, report median and IQR ("half of orders ship in 4.2–8.2 days") alongside mean and SD.

## 4. Is the variation acceptable?

Compare the spread with the requirement. Shaft tolerance 12.70 ± 0.03 mm (width 0.060). The process spread is about 6s = 0.062 mm — almost exactly the tolerance width. Even if perfectly centered, a few parts per thousand will fall outside. This ratio is the idea behind **process capability** (Cp = tolerance width / 6σ ≈ 0.97 here), covered in *Charting Process Behavior*, Module 12.

## Check yourself

1. Two lines produce 5 mm and 500 mm parts with s = 0.01 and 0.5 mm. Which is relatively more variable?
2. Why is the range a poor measure for large samples?

<details><summary>Answers</summary>

1. CV: 0.2% vs 0.1% — the 5 mm line is relatively more variable.
2. It depends only on the two most extreme values and tends to grow as n increases.
</details>
