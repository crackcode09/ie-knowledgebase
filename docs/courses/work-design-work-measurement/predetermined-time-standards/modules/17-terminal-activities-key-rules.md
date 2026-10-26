# Module 17 — Terminal Activities: Key Rules

## Objectives

- Apply the key rules for gets and puts consistently.

## Rules on the teaching card

1. **Every movement ends with exactly one terminal activity**, a get or a put, which may be G0 or P0.
2. **A reach ends in a get; a move ends in a put.** Code the movement first, then the terminal.
3. **Classify by the hardest requirement.** If any part of the grasp needs the eyes, it is G5. If the fit is tight or has two alignments, it is P6.
4. **High-control terminals block the other hand.** Two G5s or P6s can't overlap (Module 14).
5. **Corrections only when the method normally needs them.** Don't code the occasional fumble; it belongs in the allowance.
6. **A put can be followed straight away by another movement** without a new get when the hand keeps control (for example a tool moved from screw 1 to screw 2).
7. **Process time isn't a terminal.** Waiting for a driver or a press is PT from the equipment.
8. **Releasing is free.** Opening the fingers at the end of a put has no separate code.

## Common coding errors

| Error | Correction |
|---|---|
| Coding a get after every put of a tool still in hand | Rule 6: no new get while control is kept |
| Coding G2 for picking from a mixed bin | Rule 3: G5 |
| Adding corrections for every cycle because "it happened once" | Rule 5 |
| Coding both hands' high-control gets as simultaneous | Rule 4 |

## Check yourself

The pin assembly codes "Move driver to screw 1, engage `A4 P6`", "Drive `PT18`", "Move driver to screw 2, engage `A3 P6`". Why is there no G code before screw 2?

<details><summary>Answers</summary>

Rule 6: the operator keeps control of the driver between screws, so there is no new get. A G2 there would overstate the time.

</details>
