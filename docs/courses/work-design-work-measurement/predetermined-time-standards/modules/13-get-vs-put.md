# Module 13 — Get vs. Put

## Objectives

- Distinguish the two terminal activities and see why each has its own time.

## Two ends of a handling cycle

| | **Get** | **Put** |
|---|---|---|
| Purpose | Gain control of an object | Place an object at its destination |
| Happens at the end of | A reach (empty movement) | A move (loaded movement) |
| Time depends on | How hard the object is to grasp: shape, size, how it is presented | How precisely it must be placed: alignment, fit, corrections |
| Easiest case | Contact or push, no grasp (G0) | Toss or release (P0) |
| Hardest case | Selecting from a jumble, small or tangled parts (G5) | Tight fit or multiple alignments (P6 + corrections) |

```
A6  G5          A6  P6  C2
reach get      move put correction
 └─ get end ─┘  └──── put end ────┘
```

## Design lesson

Both ends can be **designed**:

- **Get time** drops when parts are presented oriented, separated and within easy reach (gravity trays, nests, magazines).
- **Put time** drops when the destination guides the part (chamfers, funnels, locating features), so fine alignment isn't needed.

## Check yourself

1. Which end of the cycle does a chamfer on a bore help?
2. Which end does a parts tray with one part per pocket help?

<details><summary>Answers</summary>

1. The **put**: it guides the pin in, turning a P6 with corrections into something closer to a P3.
2. The **get**: it removes searching and separating, turning a G5 into a G2.

</details>
