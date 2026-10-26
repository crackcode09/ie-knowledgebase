# Module 06 — Turn and Apply Pressure

## Objectives

- Code turning motions of the hand and forearm.
- Recognize when force is applied without significant movement.

## Turn

**Turn** rotates the hand, empty or loaded, about the long axis of the forearm, as when turning a knob, a lever handle or a screwdriver.

DTC code: `T<degrees><L|M|H>`. Time (cs) = (3 + 0.05 × degrees) × factor, with factor 1.0 for light, 1.5 for medium and 2.5 for heavy resistance.

| Code | cs |
|---|---|
| T90L | 7.5 |
| T90M | 11.2 (11.25 before rounding) |
| T90H | 18.8 |
| T180L | 12.0 |

A turn of more than about 180° needs a **regrasp** (Gr) between turns.

## Apply pressure

**Apply pressure** exerts force with little or no movement: seating a part, pressing a stamp, snapping a cover, pushing a palm button.

| Code | cs | Use |
|---|---|---|
| AP | 30 | Apply pressure |
| APR | 45 | Apply pressure with a regrasp to get a better hold first |

## Check yourself

1. Turn a light knob 60°.
2. Turn a stiff valve handle 120° (heavy).
3. Seat a snap-fit cover with the thumb.

<details><summary>Answers</summary>

1. **T60L** = 3 + 3 = **6 cs**.
2. **T120H** = (3 + 6) × 2.5 = **22.5 cs**.
3. **AP** = **30 cs**.

</details>
