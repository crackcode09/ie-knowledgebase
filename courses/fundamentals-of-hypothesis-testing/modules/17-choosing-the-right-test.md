# Module 17 — Choosing the Right Test

**Time:** 30 min

## Learning objectives

1. Given a situation, select the appropriate hypothesis test.

## 1. Three questions

1. **What kind of data?** Continuous (measured) or attribute (counts / categories)?
2. **What are you comparing?** Center (mean/median), proportion, or variation (σ)?
3. **How many groups, and are they paired?** One vs a standard, two independent, two paired, or three+?

## 2. Decision tree

```
Continuous data
├── Center
│   ├── 1 group vs standard ─────── one-sample t      | Wilcoxon signed-rank / sign
│   ├── 2 groups, paired ───────── paired t          | Wilcoxon signed-rank / sign
│   ├── 2 groups, independent ──── Welch two-sample t | Mann–Whitney
│   └── 3+ groups ──────────────── one-way ANOVA     | Kruskal–Wallis / Mood's median
│        (then Tukey)                                   (then pairwise + correction)
└── Variation
    ├── 1 group vs standard ─────── chi-square (σ)    | bootstrap CI for σ
    └── 2+ groups ──────────────── F (2 groups)       | Levene / Brown–Forsythe
                     parametric ──┘                     └── nonparametric / robust

Attribute data
├── Defectives (pass/fail)
│   ├── 1 group vs standard ─────── one-proportion (exact binomial)
│   ├── 2 groups ───────────────── two-proportion z  | Fisher's exact (small counts)
│   └── 3+ groups ──────────────── chi-square (k × 2 table)
└── Two categorical variables ───── chi-square test of independence

Data over time, before/after a change ── process behavior chart first (Module 6)
```

## 3. Quick reference

| Situation | Test | `htest.py` example |
|---|---|---|
| Mean vs target | One-sample t | `one-mean` |
| Two suppliers, separate units | Welch t | `two-means` |
| Same units, two conditions | Paired t | `paired` |
| 3+ machines/lines | ANOVA + Tukey | `anova` |
| Defect rate vs claim | Exact binomial | `one-prop` |
| Defect rate, 2 groups | Two-proportion z / Fisher | `two-prop` |
| Category × category | Chi-square | `chi-square` |
| σ vs requirement | Chi-square (σ) | `one-var` |
| σ, 2 groups | F / Levene | `two-var` |
| Skewed or ordinal, 2 groups | Mann–Whitney | `mann-whitney` |
| Skewed or ordinal, paired | Wilcoxon / sign | `wilcoxon`, `sign` |
| Skewed or ordinal, 3+ groups | Kruskal–Wallis | `kruskal` |

## Practice — name the test

1. Is the mean fill weight from a new nozzle different from 500 g? (20 bottles)
2. Do three suppliers have different on-time delivery rates?
3. Same 15 welds measured by two inspectors — do they differ?
4. Does a new oven reduce the variation of case depth vs the old oven?
5. 1–5 customer ratings for two product versions.
6. Do four molds produce different average part weight? (Similar spread, roughly normal.)

<details><summary>Answers</summary>

1. One-sample t. 2. Chi-square on a 3 × 2 table. 3. Paired t (or Wilcoxon). 4. Levene (or F if normal) — and plan a large sample. 5. Mann–Whitney. 6. One-way ANOVA, then Tukey.
</details>
