# Module 10 — Commonly Found Movements

## Objectives

- Recognize the movements that make up most assembly, kitting and packing work.
- Code common sequences quickly.

## Frequently seen sequences

Public descriptions note that a small number of basic movements make up most manufacturing work ([Eisbrenner PG](https://eisbrennerpg.com/about-modapts/)). On the teaching card:

| Everyday activity | Typical teaching coding | U |
|---|---|---|
| Get a part from a nearby tray and drop it in a bin | A4 G2 A4 P0 | 10 |
| Get a part from a mixed bin and place it loosely | A6 G5 A6 P3 | 20 |
| Get a part and insert it with a tight fit | A6 G2 A6 P6 | 20 |
| Press a button | A3 G0 | 3 |
| Get a hand tool, use it, put it aside | A4 G2 A4 P6 … A4 P0 | 4+2+4+6+…+4 |
| Turn a part over in the hand | T2 (regrasp) | 2 |
| Slide a part along a surface | A6 G0 A6 P0 | 12 |

## Patterns

- **Get–put pairs:** almost every handling step is *movement–get–movement–put*.
- **Tool cycles:** get tool → (move–put to the work) → process time → aside tool.
- **Sliding and pushing** use contact gets (G0) and zero puts (P0). They are faster and kinder to the body than lifting.

## Check yourself

1. Code "reach 20 cm to a parts tray, pick up an easy part, move it 20 cm and place it loosely in a nest". Total?
2. What is faster for moving a box on a bench: lifting it (G2…P3) or sliding it (G0…P0)? By how much on the teaching card?

<details><summary>Answers</summary>

1. A4 G2 A4 P3 = 4 + 2 + 4 + 3 = **13 U = 1.3 s**.
2. Sliding. G0 + P0 = 0 vs G2 + P3 = 5, so 5 U (0.5 s) less with the same movements, and with less load on the body.

</details>
