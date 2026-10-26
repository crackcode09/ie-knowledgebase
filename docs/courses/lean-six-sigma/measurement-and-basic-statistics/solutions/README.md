# Solutions and Exercise Notes

Answers to each module's "Check yourself" questions and the Module 12 quiz are inside the modules (collapsed). This file covers the open exercises.

## Module 7 — Exercise 7.1 (lead time bin widths)

- **1-day bins:** right skew is clear; peak around 4–5 days, long tail to 15 days.
- **2-day bins:** same shape, smoother.
- **4-day bins:** only four bars; the skew is still visible but the peak location is lost.

Lesson: with 60 points, bin width changes the picture. Use √n ≈ 8 bins as a start and check that your conclusion doesn't depend on the choice.

## Key worked numbers (for instructors)

All regenerate from `python tools/make_data.py` (seed 1924).

| Item | Value |
|---|---|
| Complaints | 155; top category by count: Late delivery 41.3%; by cost: Dimension out of tolerance 41.7% |
| Shaft diameter (n = 100) | mean 12.7001, median 12.699, s 0.0103, range 0.062, IQR 0.012 |
| Lead time (n = 60) | mean 6.39, median 5.35, s 3.27, IQR 4.0 (Q1 4.15, Q3 8.15), skewness 1.09 |
| Supplier thickness | A: mean 10.000, s 0.054; B: mean 10.000, s 0.123 |
| Gauges (bias, s) | G1 +0.0007/0.0016; G2 −0.0021/0.0115; G3 +0.0147/0.0018; G4 +0.0089/0.0047 |
| Fill weight | overall 500.4; head A 497.9; head B 502.9 |
| Shift output means | 407.2, 406.2, 329.4 (plant 380.9) |
