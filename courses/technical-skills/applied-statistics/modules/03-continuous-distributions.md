# Module 3 — Continuous Distributions: Normal and Exponential

**Time:** 75 min

## Learning objectives

1. Use the normal distribution to forecast the share of output beyond a limit.
2. Use the exponential distribution for time between failures.

## 1. Normal — forecasting process performance

Reflow cycle time: mean 61.89 s, sd 2.35 s; histogram symmetric; Shapiro–Wilk normality test p = 0.36 (no evidence against normality).

The line is balanced to 68 s per board. What share of boards will exceed 68 s?

  z = (68 − 61.89) / 2.35 = **2.60** → P(Z > 2.60) = **0.0047 ≈ 4,700 ppm**

```bash
python tools/statkit.py normal
```

None of the 120 sampled boards exceeded 68 s — and that's consistent: at 0.47% you'd expect about 0.6 in 120. The model forecasts what the sample is too small to show: roughly **5 boards per 1,000** will hold up the line.

95th percentile: 61.89 + 1.645 × 2.35 = **65.8 s**.

**Normal-model rule:** only for roughly symmetric, single-peaked, stable data. For skewed data the tail forecast can be badly wrong (Module 7).

## 2. Exponential — time between failures

If failures occur randomly at a constant rate λ, the time between them is exponential:

  P(T > t) = e^(−λt), mean = MTBF = 1/λ, sd = mean

40 times between failures of the pick-and-place machine:

```bash
python tools/statkit.py exponential
```

| | Value |
|---|---|
| MTBF | **63.2 h** (λ = 0.0158 per hour) |
| P(no failure in an 8-h shift) | e^(−8/63.2) = **0.881** |
| P(no failure in a 40-h week) | **0.531** |
| MTBF 95% CI (chi-square method) | 47.4 to 88.5 h |
| sd / mean | 1.32 (exponential predicts ~1) |

**Planning:** about 1 shift in 8 has a breakdown; half of weeks see at least one. The wide CI on MTBF (40 failures!) is a reminder that reliability estimates need lots of data.

The exponential is "memoryless": a machine that's run 50 h since its last failure is no more likely to fail in the next hour than a freshly repaired one. If failures cluster after long run times (wear-out), use a Weibull model instead.

## Check yourself

Mean 100, sd 5, upper limit 112. Forecast the percentage above the limit.

<details><summary>Answer</summary>

z = 2.4 → about 0.82%.
</details>
