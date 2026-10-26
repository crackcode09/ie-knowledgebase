# Module 07 — The Modular Concept

## Objectives

- Explain how a single base unit and whole-number values make an analysis additive.
- Apply the body-member principle: bigger body members take longer to move.

## One unit, whole numbers

In a modular system every code's value is a **whole-number multiple of one base unit**. MODAPTS's unit is the MOD (0.129 s, public value). This course's teaching unit is U = 0.1 s.

Benefits of whole numbers:

- **Mental arithmetic.** Analysts total a line at a glance.
- **Code = time.** `A6` *is* 6 U, so there is no table lookup once you know the classification.
- **Fewer errors.** No decimals to misread, and totals are easy to re-check.
- **Easy conversion.** Seconds = units × unit size.

## The body-member principle

Public descriptions of MODAPTS stress that it classifies motions by **the body part that moves**, not by measured distance ([6sigma.us](https://www.6sigma.us/work-measurement/modapts-modular-arrangement-of-predetermined-time-standards/)). The idea: a larger body member takes longer to accelerate and decelerate, so it takes longer whatever the exact distance.

The teaching card applies the same principle with its own values:

![Movement classes](../figures/11_movement_classes.png)

| Body member | Teaching code | U | s |
|---|---|---|---|
| Finger | A2 | 2 | 0.2 |
| Hand / wrist | A3 | 3 | 0.3 |
| Forearm | A4 | 4 | 0.4 |
| Whole arm | A6 | 6 | 0.6 |
| Extended arm with shoulder | A8 | 8 | 0.8 |
| Arm plus trunk lean | A12 | 12 | 1.2 |

The distance ranges on the card are only a guide to which body member is used. Watch the body, not the ruler.

## Building blocks

A task time is assembled from the blocks:

```
get pencil, put in cup  =  A6  +  G2  +  A6  +  P3   =  17 U = 1.7 s
                           reach   get    move   put
```

## Check yourself

1. Why does the teaching card value a forearm move (A4) less than a whole-arm move (A6) even if the distances are similar?
2. Total `A8 G2 A8 P3` and convert to seconds.

<details><summary>Answers</summary>

1. The body-member principle: moving the whole arm involves the shoulder and more mass, so it takes longer than a forearm move pivoting at the elbow.
2. 8 + 2 + 8 + 3 = **21 U = 2.1 s**.

</details>
