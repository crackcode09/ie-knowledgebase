# Module 15 — Layout of the Cell · Cell Configurations · Layout Procedures

Outline items: **Layout of the cell**, **Cell configurations**, **Layout procedures**

## Objectives

- Compare cell configurations by walking distance and control of flow.
- Lay out the wall-box cell and follow a procedure to install it.

## Layout of the cell

Principles:

- Machines in **process sequence**, close together (pitch ≈ 2.5 m here), with the operator's path **inside** the cell.
- **Input and output** next to each other where possible, so one person sees what comes in and goes out.
- **One-piece flow** between machines on gravity chutes or small fixtures. No hidden storage.
- **Visual board** at the exit: hourly output vs plan.
- Clear access for **maintenance and material** from the outside.

## Cell configurations

Walking per cycle for one operator running all 6 stations and returning to the start (pitch 2.5 m; U width 2 m; walking speed 1.2 m/s, a typical assumption):

| Configuration | Walk (m) | Walk (s) | Notes |
|---|---|---|---|
| Straight line | 25.0 | 20.8 | Simple, but the return walk is wasted; input and output at opposite ends |
| L-shape | 21.5 | 17.9 | Fits corners and columns |
| **U-shape** | **14.0** | **11.7** | Shortest walk; input next to output; flexible operator assignments |
| Parallel or two-sided | — | — | Several operators facing each other; for longer lines |

The U-shape suits Corvan's wall-box cell:

- **OP10 shear** next to **OP60 inspect and load**
- punch and brake along one leg
- spot weld and hardware press along the other

Its 1.2 m/s walking speed is a common planning assumption. Measure it on your own floor.

## Layout procedures

1. **Draw** the cell to scale with machine footprints, clearances, utilities and operator paths.
2. **Simulate** a cycle on paper: check every reach, walk and handoff against takt.
3. **Mock up** in cardboard or tape on the floor, and walk through it with the operators.
4. **Review** with maintenance (access), EHS (guards, egress, noise, fumes) and materials (replenishment).
5. **Plan the move**: build banks of parts ahead, move during low demand, set up utilities first, then commission the machines in sequence.
6. **Run in**: start with the experienced operators, track hourly output, fix problems daily, then train the second shift.
7. **Follow up**: after 30 and 90 days, compare lead time, output per labor hour, quality, ergonomics and space with the plan.

## Run it

```bash
python tools/fwdkit.py configs
```

## Check yourself

1. How much walking time per cycle does the U-shape save over a straight line, and what is that per shift at takt 94.3 s?
2. Why put the first and last operations of a U-cell next to each other?

<details><summary>Answers</summary>

1. 20.8 − 11.7 = **9.1 s** per cycle. Cycles per shift = 27,000 / 94.3 ≈ 286, so 286 × 9.1 ≈ **2,600 s ≈ 43 minutes** per shift (if one operator ran the whole loop).
2. One person can control the cell's pace: release a new blank only when a finished box leaves (WIP control). Input and output staging also share one aisle.

</details>
