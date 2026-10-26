# Module 03: Latin Square Designs

## Objectives

- Use a Latin square to block two nuisance sources at once.
- Lay out and randomize a square.
- Analyze it and know its limits.

## Concept

A **Latin square** of order *p* arranges *p* treatments in a p × p grid. Each treatment appears **exactly once in every row and every column**. Rows block one nuisance source and columns block another. The design needs only p² runs, compared with p³ for a full three-way layout.

Model: y_ijk = μ + α_i (row) + τ_j (treatment) + β_k (column) + ε_ijk

ANOVA degrees of freedom for a p × p square:

| Source | df |
|---|---|
| Rows | p − 1 |
| Columns | p − 1 |
| Treatments | p − 1 |
| Error | (p − 1)(p − 2) |
| Total | p² − 1 |

**Limitations:**

- The square assumes **no interactions** among rows, columns and treatments.
- Small squares leave little error: a 3 × 3 square has 2 error df, which is usually too few. Replicate the square if you can.
- The numbers of rows, columns and treatments must all be equal.

**Randomizing a square:** start from a standard square (the first row and column in order), then randomly permute the rows, then the columns, then the assignment of treatment letters.

## Worked example: cooling programs

Four mold-cooling programs (A to D) aim to shorten cycle time. Cycle time also depends on the **machine** (four presses of different ages) and the **day** (ambient temperature and chiller load). A 4 × 4 Latin square tests every program once on every machine and once on every day: 16 runs instead of 64 (`data/latin_cooling.csv`).

| | Day 1 | Day 2 | Day 3 | Day 4 |
|---|---|---|---|---|
| Mc1 | A 32.54 | B 30.84 | C 30.00 | D 32.59 |
| Mc2 | B 31.39 | C 31.05 | D 33.32 | A 34.05 |
| Mc3 | C 28.38 | D 31.92 | A 30.69 | B 30.71 |
| Mc4 | D 32.89 | A 35.05 | B 32.45 | C 32.22 |

The square in the data file is the cyclic standard form, kept that way so it is easy to read. In practice, randomize it as described above.

| Source | SS | df | MS | F | p |
|---|---|---|---|---|---|
| Program | 18.09 | 3 | 6.03 | 20.8 | 0.0014 |
| Machine | 16.86 | 3 | 5.62 | 19.4 | 0.0017 |
| Day | 3.13 | 3 | 1.04 | 3.60 | 0.085 |
| Error | 1.74 | 6 | 0.29 | | |
| Total | 39.81 | 15 | | | |

Program means (s): A 33.08, B 31.35, **C 30.41**, D 32.68. Program C is about 2.7 s faster than A. On a high-volume part, that matters.

Machines differed nearly as much as programs did. Had machine been left in the error term, the program test would have been far weaker. The day effect was smaller (p = 0.085); blocking on it cost 3 df for little gain, but that could not be known in advance.

## Run it

```bash
python tools/doekit.py latin
```

## Check yourself

1. How many error df does a 5 × 5 Latin square have?
2. If program C works especially well on the newest machine, what assumption is broken, and what happens?
3. You have 3 programs, 3 machines and 4 days. Can you use a Latin square?

<details><summary>Answers</summary>

1. (5 − 1)(5 − 2) = 12.
2. The no-interaction assumption. The program × machine interaction lands in the error and in the program estimates, which biases the comparison and inflates error.
3. Not a standard Latin square, because the dimensions must match. Use three of the days, or a Youden square or another incomplete design.

</details>
