# Module 05: Balanced and Unbalanced Designs

## Objectives

- Explain why balance makes factorial analysis simple.
- See how losing runs makes the sums of squares depend on the order of terms.
- Choose between sequential (Type I) and adjusted (Type II/III) sums of squares.

## Concept

A design is **balanced** when every cell has the same number of replicates. In a balanced factorial, the factor columns are **orthogonal**. As a result:

- each SS has one value, whatever order the terms are entered;
- the SS add up exactly to the total;
- the hand formulas from Module 04 are correct.

Real experiments lose runs: a short shot, a jammed robot, a mislabeled part. With unequal cell sizes the factors are no longer orthogonal, and the SS for A depends on whether B has already been accounted for. There are three common conventions:

| Type | Each term is adjusted for | Use when |
|---|---|---|
| I (sequential) | terms listed *before* it | there is a natural order (for example, a covariate first) |
| II | all other terms that do not contain it | there is no interaction, or you are testing main effects after dropping a non-significant interaction |
| III (partial) | all other terms, including interactions | the default in most commercial software; needs sum-to-zero (effect) coding |

With balanced data, all three give the same answer.

## Worked example: three shots lost

Start from Module 04's 27-run shrinkage experiment and drop three runs: two from the 290 °C / 60 MPa cell and one from the 260 °C / 90 MPa cell. That leaves 24 runs.

**Type I, temperature entered first:**

| Term | SS |
|---|---|
| Melt temp | 0.0411 |
| Hold pressure | 0.1779 |
| Interaction | 0.0048 |
| Residual | 0.0083 |

**Type I, pressure entered first:**

| Term | SS |
|---|---|
| Hold pressure | 0.1385 |
| Melt temp | 0.0804 |
| Interaction | 0.0048 |
| Residual | 0.0083 |

The melt temperature SS **doubles** depending on the order. That is because the missing runs came from the corners of the table: the cells that remain are no longer orthogonal, and some temperature information is mixed with pressure information.

**Type III (effect coding):**

| Term | SS | F | p |
|---|---|---|---|
| Melt temp | 0.0819 | 73.6 | < 0.001 |
| Hold pressure | 0.1725 | 155.0 | < 0.001 |
| Interaction | 0.0048 | 2.17 | 0.12 |
| Residual | 0.0083 (15 df) | | |

The conclusions do not change: both main effects are strong and the interaction is not significant. But you must say which SS type you report. If you swap software or term order, you may otherwise "lose" an effect.

Also notice that the residual SS (0.0083) is lower than in the full data, partly because the dropped runs happened to be noisy. Removing data never makes an experiment better. Investigate *why* runs were lost, because "missing" is not always random.

## Practical rules

1. **Design for balance**, and protect it by building a few spare parts into the plan.
2. If runs are lost, **report the actual n per cell** and the SS type.
3. If a cell is completely empty, some interaction terms cannot be estimated. Simplify the model, or rerun that cell.
4. Never "fix" imbalance by inventing data. Rerunning a lost treatment (in random order, with a block for "rerun" if timing differs) is fine.

## Run it

```bash
python tools/doekit.py unbalanced
```

The code uses `C(factor, Sum)` coding for the Type III fit. With the default treatment coding, Type III tests in statsmodels answer a different question.

## Check yourself

1. Why does entry order not matter in a balanced 3 × 3 factorial?
2. A colleague's software reports SS_temp = 0.041; yours reports 0.082. Who is wrong?
3. When is Type I the right choice?

<details><summary>Answers</summary>

1. Balance makes the factor contrasts orthogonal, so each term explains its own share of variation regardless of what else is in the model.
2. Possibly neither. 0.041 is Type I with temperature entered first; 0.082 is Type III. Compare like with like.
3. When the order is meaningful, for example a covariate or block entered first and treatments after it, or a polynomial model built up term by term.

</details>
