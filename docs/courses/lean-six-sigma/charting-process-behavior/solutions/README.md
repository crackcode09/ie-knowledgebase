# Exercise Solutions

All numbers come from the datasets in `data/` (regenerate with `python tools/make_data.py`) and `tools/spc.py`. Small differences in the last digit are rounding.

## Module 2 — Exercise 2.1 (roughness histogram)

Center ≈ 0.66 µm (median 0.655), spread from ~0.25 to 1.86 µm, strongly right-skewed (skewness 1.45). Roughness is bounded at zero and the process runs near that bound, so a long right tail is expected.

## Module 3 — Exercise 3.1

mR̄ = 0.006426 mm; σ̂ = 0.005697 mm; s = 0.005927 mm. Within and overall agree within ~4% → consistent with a stable baseline.

## Module 4 — Exercise 4.1 (fill weight run chart)

Values alternate above/below the median almost every sample → many more runs than random data would produce. Cause: samples alternate between two filler heads with different averages (Module 11).

## Module 6 — Exercise 6.1 (cycle time XmR)

`python tools/spc.py xmr data/cycle_time.csv days --baseline 25`

Baseline (orders 1–25): X̄ = 3.956 days, mR̄ = 1.1125, natural process limits 0.997–6.915 days, URL 3.636.
After the change: no point beyond the limits, but **Rule 4 fires at order 34** (orders 27–34 all below 3.956). The improvement is real but small relative to routine variation; the run chart with the median (Module 4) found the same shift.

## Module 7 — Exercise 7.1

Hour 22 fires Rule 1 (12.7203 > 12.7163) and Rule 2 (hours 21 and 22 both above 2σ = 12.7106).

## Module 8 — Exercise 8.1

See the answer inside the module.

## Module 9 — Exercise 9.1 (XmR on proportions)

XmR on daily p: center 0.0442, natural process limits −0.010 (→ 0) to 0.0988. Day 14 (0.1115) still signals. Here the XmR limits are close to the average p-chart limits (≈0.08–0.09), so the binomial model is reasonable for this data set.

## Module 11 — Exercise 11.1

| | X̄ | mR̄ | σ̂ = mR̄/1.128 |
|---|---|---|---|
| Combined | 501.42 | 3.64 | 3.23 |
| Head A | 499.57 | 0.71 | 0.63 |
| Head B | 503.27 | 1.35 | 1.19 |

The combined σ̂ is 3–5× the per-head values: the alternation between heads dominates the moving ranges.

## Module 12 — Exercise 12.1 (fill weight capability, spec 495–505 g)

| | Mean | σ_within | Cpk | σ_overall | Ppk |
|---|---|---|---|---|---|
| Combined | 501.42 | 3.23 | 0.37 | 2.14 | 0.56 |
| Head A | 499.57 | 0.63 | 2.44 | 0.94 | 1.62 |
| Head B | 503.27 | 1.19 | 0.48 | 1.16 | 0.50 |

Only the per-head numbers mean anything. The combined result is nonsense — note σ_within > σ_overall, a tell-tale sign of mixed sources. Head B is off-center toward the USL; recentering B is the fix. (Head A's Pp is noticeably below its Cp; with only 20 points, check its chart before trusting either.)

## Module 13 — Exercise 13.1

ln(Ra): mean −0.478, s 0.398, ln(1.6) = 0.470 → Ppk = (0.470 + 0.478) / (3 × 0.398) = 0.79.

## Module 14 — Exercise 14.1 (EWMA)

λ = 0.2, center 12.6992, σ̂ 0.00570, L = 3. First signal at **hour 23** (z = 12.7061 > 12.7049). The XmR chart with Rules 1–2 signaled at hour 22 — for a 2.6σ shift like this one, the Shewhart chart is already fast. EWMA earns its keep on shifts under ~1.5σ.

## Module 14 — Exercise 14.2 (simulation)

2,000 runs, 1σ shift, seed 1: Rule 1 only → average **43.6** points to signal; CUSUM (k = 0.5, h = 5) → **10.3** points.
