# Module 15 — Laboratory Problems

## Objectives

- Analyse industrial and office operations from start to finish with the teaching card.
- Check your analyses against the keys and explain any differences.

## How to work the labs

1. Open `data/lab_worksheets.csv`. Each lab has its steps described, with the codes left blank.
2. If possible, set up the task on a bench (or watch someone do it) and measure the distances.
3. Code the left hand, the right hand and the body/eye/process column for each step.
4. Apply the simultaneous-motion rule and total the analysis.
5. Compare with the key: `python tools/dmtkit.py lab L04` (or `data/lab_keys.csv`).
6. Where you differ, decide whether the difference is in **classification** (case, grasp, fit) or in the **method assumed**. Both are worth discussing.

## Keys (totals)

Standard = normal time × 1.12. Per-hour figures use that standard.

| Lab | Task | cs | Normal s | Standard s | Per hour |
|---|---|---|---|---|---|
| L01 | Pick a bolt from a bin and place it in a fixture hole | 158.0 | 1.58 | 1.77 | 2,034 |
| L02 | Insert a dowel pin into a close-fit hole | 110.5 | 1.10 | 1.24 | 2,909 |
| L03 | Washer on bolt: current | 235.0 | 2.35 | 2.63 | 1,368 |
| L03 | Washer on bolt: improved | 106.5 | 1.06 | 1.19 | 3,018 |
| L04 | Fold a letter and insert it in an envelope (office) | 260.5 | 2.60 | 2.92 | 1,234 |
| L05 | Stamp a document (office) | 156.5 | 1.56 | 1.75 | 2,054 |
| L06 | Load press, two-hand buttons, unload (incl. 180 cs press) | 512.5 | 5.12 | 5.74 | 627 |
| L07 | Pack six bottles, two at a time | 261.0 | 2.61 | 2.92 | 1,232 |
| L08 | Lever, then handwheel one turn | 112.2 | 1.12 | 1.26 | 2,865 |
| L09 | Inspect three features | 202.5 | 2.02 | 2.27 | 1,587 |
| L10 | Box from the floor to a bench 3 steps away | 520.9 | 5.21 | 5.83 | 617 |

## Discussion points

- **L04:** office work can be analysed the same way. The flexible letter makes the envelope insertion a "difficult" position (PCMh).
- **L06:** the right hand does all the manual work, while the press cycle (180 cs) is idle time for the operator. How could the left hand load the next blank during the press cycle?
- **L07:** two-handed packing works because PLS is low control in both hands.
- **L09:** eye time limits the work. Better lighting and a gauge could replace three eye focuses.
- **L10:** body motions are 87 % of the time. Fix the layout before anything else.

## Check yourself

In L06, if a second nest let the left hand load the next blank during the 180 cs press cycle, which right-hand steps could overlap with the press? Roughly what cycle time would result?

<details><summary>Answers</summary>

The blank get and load (steps 1–2: 66.5 + 85 = 151.5 cs) could be done during the press cycle, at the second nest with the left hand. The cycle becomes about: buttons 65 + press 180 + unload 66 + aside 50 = **361 cs**, down from 512.5. That is about 30 % faster, if guarding and safety rules allow loading during the press cycle (with a two-nest shuttle, for example).

</details>
