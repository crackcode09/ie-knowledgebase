# Module 7 — Analyzing Data That Don't Follow a Standard Distribution

**Time:** 60 min

## Learning objectives

1. Detect non-normal data.
2. Choose between transforming, fitting another distribution, bootstrapping and nonparametric methods.

## 1. Detecting non-normality

- Histogram and normal probability plot.
- Skewness and kurtosis (Module 1).
- A normality test (Shapiro–Wilk; Anderson–Darling). With large n, tests flag tiny departures that don't matter; with small n they miss big ones — always look at the plot.

Rework time: skewness 1.36, Shapiro–Wilk p < 0.001 → not normal.

## 2. Options

| Approach | How | Use when |
|---|---|---|
| **Transform** | log, square root, Box–Cox | You need normal-theory tools (capability, CIs) and a transform makes data symmetric |
| **Fit another distribution** | Lognormal, Weibull, exponential, gamma | You need tail predictions (percentiles, ppm) |
| **Bootstrap** | Resample the data thousands of times | CIs for medians, percentiles, any statistic |
| **Nonparametric tests** | Sign, Wilcoxon, Mann–Whitney, Kruskal–Wallis | Comparing medians/distributions without distribution assumptions |
| **Rely on the CLT** | Use t methods for **means** | n moderate (~30+) and only the mean matters |

## 3. Rework time

```bash
python tools/statkit.py nonnormal
```

| | Value |
|---|---|
| Log transform: skewness, Shapiro p | −0.30, 0.21 → consistent with normal (lognormal data) |
| Box–Cox λ | 0.20 (close to 0 = log) |
| Mean vs median | 15.2 vs 13.8 min |
| 90th percentile: empirical / normal model / lognormal model | 25.2 / 25.7 / 26.7 min |
| Median 95% CI (bootstrap, 5,000 resamples) | 11.8 to 15.8 min |
| Sign test, median vs 12 min target | p = 0.146 |

**Reading:** the lognormal fits the shape. Here the 90th-percentile forecasts happen to be close, but for more extreme percentiles (99th) or more skewed data, a normal model can understate the tail badly. The median repair is about 14 min, and the data don't show it's above the 12-minute target (p = 0.15) — though the CI (11.8–15.8) says it may be.

## Check yourself

You need a 95% CI for the 90th percentile of repair time. Which approach?

<details><summary>Answer</summary>

Bootstrap the 90th percentile (or fit a lognormal and use its percentile with a parametric CI).
</details>
