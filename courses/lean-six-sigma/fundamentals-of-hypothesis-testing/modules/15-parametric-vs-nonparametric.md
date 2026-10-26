# Module 15 — Parametric vs Nonparametric Tests

**Time:** 35 min

## Learning objectives

1. Explain the difference between parametric and nonparametric tests.
2. Decide when a nonparametric test is the better choice.

## 1. Definitions

- **Parametric tests** (t, ANOVA, F, chi-square for variance) assume the data come from a distribution family with known form — usually normal — and test its *parameters* (μ, σ).
- **Nonparametric (distribution-free) tests** make weaker assumptions, usually working with **ranks** or **signs** instead of the raw values. They typically test medians or "one group tends to have larger values."

## 2. Pairs of tests

| Situation | Parametric | Nonparametric |
|---|---|---|
| One group vs a standard | One-sample t | Wilcoxon signed-rank (symmetric data) / sign test |
| Paired data | Paired t | Wilcoxon signed-rank / sign test |
| Two independent groups | Two-sample t | Mann–Whitney (Wilcoxon rank-sum) |
| Several groups | One-way ANOVA | Kruskal–Wallis; Mood's median test |
| Variances | F, Bartlett | Levene (median), Brown–Forsythe |

## 3. Trade-offs

| | Parametric | Nonparametric |
|---|---|---|
| Power when assumptions hold | Highest | Slightly lower (Mann–Whitney is ~95% as efficient as t for normal data — asymptotic relative efficiency 3/π) |
| Power with heavy tails / outliers | Can drop sharply | Often higher |
| Ordinal data (ratings, scores) | Not appropriate | Appropriate |
| Output | Mean difference with CI | Median-based conclusion; CIs available but less familiar |
| Small samples, unknown shape | Risky | Safer |

## 4. Decision guide

Use a nonparametric test when:

- The data are **ordinal** (1–10 scores, rankings, Likert scales).
- The sample is **small** (< ~15–20 per group) **and** clearly skewed or has outliers.
- There are **censored values** ("> 100 hours", below detection limit).

Stay parametric when:

- Samples are moderate or large (central limit theorem helps means).
- Data are roughly symmetric without wild outliers.
- You need a CI for a mean difference in engineering units.

A transformation (e.g., log of skewed times) followed by a t-test is a third option; Module 16 shows it agrees here.

## Check yourself

1. Customer satisfaction ratings 1–5 from two plants. Which kind of test?
2. Why don't nonparametric tests need normality?

<details><summary>Answers</summary>

1. Nonparametric (Mann–Whitney) — the data are ordinal.
2. They use ranks or signs, whose distribution under H₀ doesn't depend on the shape of the original data.
</details>
