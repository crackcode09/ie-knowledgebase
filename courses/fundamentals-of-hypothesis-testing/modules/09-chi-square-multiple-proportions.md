# Module 9 — Comparing Multiple Proportions: Chi-Square

**Time:** 50 min · **Data:** `data/defects_by_machine.csv`

## Learning objectives

1. Test whether two categorical variables are related using a contingency table.
2. Find which cells drive a significant result.
3. Check the expected-count condition.

## 1. The chi-square test of independence

Compare **observed** counts O with the counts **expected** if the two variables were unrelated:

  Eᵢⱼ = (row total × column total) / grand total

  χ² = Σ (O − E)² / E  df = (rows − 1)(columns − 1)

Large χ² → observed pattern far from "independent" → reject H₀.

The same test compares **several proportions** at once (e.g., defective rate across 4 machines is a 4 × 2 table).

## 2. Worked example — defect type by machine

| Machine | Burr | Scratch | Dimension | Other | Total |
|---|---|---|---|---|---|
| M1 | 22 | 15 | 8 | 5 | 50 |
| M2 | 18 | 21 | 9 | 4 | 52 |
| M3 | 12 | 14 | 26 | 6 | 58 |
| **Total** | 52 | 50 | 43 | 15 | 160 |

H₀: defect type is independent of machine. Hₐ: the mix of defect types differs by machine. α = 0.05.

Example expected count: M3 × Dimension = 58 × 43 / 160 = 15.59 (observed 26).

```bash
python tools/htest.py chi-square
```

**χ² = 18.11, df = 6, p = 0.006** → reject H₀ (critical value χ²₀.₉₅,₆ = 12.59).

**Which cells drive it?** Contributions (O − E)²/E:

| | Burr | Scratch | Dimension | Other |
|---|---|---|---|---|
| M1 | 2.03 | 0.02 | 2.20 | 0.02 |
| M2 | 0.07 | 1.39 | 1.77 | 0.16 |
| M3 | 2.49 | 0.94 | **6.96** | 0.06 |

M3 produces far more dimensional defects than expected — that's where to look (fixturing, offsets, thermal growth).

## 3. Expected-count condition

The χ² approximation needs expected counts that aren't too small. Common guidance (Cochran, 1954): no expected count below 1, and no more than 20% of cells below 5.

Here, "Other" has expected counts 4.69 and 4.88 — 2 of 12 cells (17%) are below 5, so the condition is just met. If it weren't, combine sparse categories (e.g., merge "Other" into another column) or use an exact test.

## Check yourself

1. A 2 × 5 table. df?
2. Your table has 6 of 12 expected counts below 5. What do you do?

<details><summary>Answers</summary>

1. (2 − 1)(5 − 1) = 4.
2. Combine categories or use an exact (Fisher–Freeman–Halton or simulated) test.
</details>
