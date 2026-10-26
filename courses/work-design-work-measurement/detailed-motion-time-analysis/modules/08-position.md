# Module 08 — Position

## Objectives

- Classify positioning by fit, symmetry and ease of handling.
- Design parts and fixtures to reduce positioning time.

## Definition

**Position** aligns, orients and engages one object with another, as when inserting a pin in a hole, a key in a slot or a part on locating pins. It starts when the object reaches the destination area and ends when it is engaged.

## Teaching card (DTC)

Code: `P<fit><symmetry>[h]`. Time = fit + symmetry (+ 6 if difficult to handle).

| Fit | cs | | Symmetry | cs |
|---|---|---|---|---|
| L: loose (no pressure, visible clearance) | 9 | | S: symmetric (any orientation fits) | 0 |
| C: close (light pressure, small clearance) | 20 | | M: semi-symmetric (a few orientations fit) | 4 |
| T: tight (heavy pressure or interference) | 45 | | N: non-symmetric (one orientation fits) | 10 |
| h: difficult to handle (flexible, slippery, tiny) | +6 | | | |

| Code | cs | | Code | cs |
|---|---|---|---|---|
| PLS | 9 | | PCN | 30 |
| PLM | 13 | | PTS | 45 |
| PLN | 19 | | PTN | 55 |
| PCS | 20 | | PTNh | 61 |

Only **PLS** is low-control. Every other position needs the eyes and can't be overlapped with another high-control motion (Module 11).

## Designing for positioning

| Change | Effect |
|---|---|
| Chamfer or lead-in on the pin or hole | Close behaves more like loose |
| Make the part symmetric, or add a clear orientation feature | N → M or S |
| Fixtures with guides | Fewer corrections; position by touch |
| Increase clearance where function allows | Tight → close |

## Check yourself

1. Code and time: a close-fit pin with a key that fits two ways.
2. A tight, non-symmetric, slippery insertion is redesigned to a close, symmetric fit. What is saved?

<details><summary>Answers</summary>

1. **PCM** = 20 + 4 = **24 cs**.
2. PTNh 61 → PCS 20: **41 cs** saved per insertion.

</details>
