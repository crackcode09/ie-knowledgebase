# Module 04 — The MODAPTS Symbol (Code Notation)

## Objectives

- Read and write the letter-plus-number code notation.
- Write an analysis line that anyone can re-add.

> **Note.** The outline lists "MODAPTS Symbol" but no public source explains what that lesson covers. It may describe the system's logo. This module covers the **code symbol**, meaning how a MODAPTS-style code is written, which is the part an analyst uses. The logo is the Association's trademark material and isn't reproduced.

## The code symbol

Public sources describe MODAPTS codes as **a letter for the type of activity, followed by an integer that is the time in MODs** ([Eisbrenner PG](https://eisbrennerpg.com/about-modapts/)). The number *is* the time, so an analysis can be totalled by adding the numbers.

This course's teaching card uses the same notation with its own letters and values:

```
A6   G5   A6   P0         ← code symbols: letter = what kind of activity, number = time in U
6  + 5  + 6  + 0 = 17 U = 1.7 s
```

| Letter (teaching card) | Activity class |
|---|---|
| A | Movement of a body member (arm, hand, finger) |
| G | Get: gaining control of an object |
| P | Put: placing an object at its destination |
| C | Correction during a precise put |
| W, F, B, S, U, E, R, D, X, T, K, L | Auxiliary activities (walk, foot, bend, sit, stand, eye, read, decide, pressure, transfer, crank, load) |
| PT | Process (tool or machine) time; not a motion |

## Writing conventions

- One **step per line**: a meaningful piece of work ("get housing, place in fixture").
- Codes in the order they happen: **movement, then terminal** (get or put).
- Repetitions as `W6x3` (three steps of walking), never as a pre-multiplied "W18".
- Note in the description which hand works and what the other hand does at the same time.
- Total each line, then the task.

## Check yourself

1. What is the total for `A4 G5 A4 P6 C2`?
2. Why write `W6x4` rather than `W24`?

<details><summary>Answers</summary>

1. 4 + 5 + 4 + 6 + 2 = **21 U = 2.1 s**.
2. It keeps the meaning (four steps) visible for checking and method improvement. W24 hides how many steps there are, and might be read as a code that doesn't exist.

</details>
