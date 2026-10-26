# Module 05 — Move

## Objectives

- Define the move motion and the effect of weight.
- Code moves with the teaching card.

## Definition

**Move** transports an object with the hand to a destination. It starts when the loaded hand begins to move and ends when the object arrives.

## What drives the time

1. **Distance**, as for reach.
2. **Case**: what is at the destination.
3. **Weight or resistance**: a heavier object takes longer to start and stop.

## Teaching card (DTC)

Code: `M<distance><case>[m][/<kg>]`.

| Case | Meaning | Formula (cs) | 30 cm |
|---|---|---|---|
| a | To the other hand or against a stop | 7 + 0.8 d | 31 |
| b | To an approximate location | 8 + 1.0 d | 38 |
| c | To an exact location | 10 + 1.2 d | 46 |

**Weight** (per hand, above 1 kg):

- multiply by (1 + 0.015 × (kg − 1))
- then add 1.5 × (kg − 1) cs

So **M30b/5** = 38 × 1.06 + 6 = **46.3 cs**. If both hands carry one object, use the weight per hand.

Case c is a **high-control** move. It usually ends in a position (Module 08).

## Check yourself

1. Move a part 35 cm to an exact location.
2. Move a 4 kg casting 30 cm to an approximate location, one hand.
3. Move a part 50 cm against a stop.

<details><summary>Answers</summary>

1. **M35c** = 10 + 1.2 × 35 = **52 cs**.
2. **M30b/4** = 38 × 1.045 + 4.5 = **44.2 cs**.
3. **M50a** = 7 + 0.8 × 50 = **47 cs**.

</details>
