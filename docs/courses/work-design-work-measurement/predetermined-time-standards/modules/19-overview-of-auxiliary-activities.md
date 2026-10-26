# Module 19 — Overview of Auxiliary Activities

## Objectives

- Use each auxiliary code on the teaching card correctly.

## The teaching card's auxiliary codes

| Code | U | Activity | Notes |
|---|---|---|---|
| W6 | 6 | Walk, per step | Count steps on the floor plan or video; write W6x*n* |
| F4 | 4 | Foot or leg action | Pedal, foot switch; per action |
| B22 | 22 | Bend and arise | Stoop to below knee height and return; an ergonomic flag every time |
| S20 | 20 | Sit down | |
| U22 | 22 | Stand up from sitting | |
| E3 | 3 | Eye focus or eye travel | Only when the eyes must move or refocus **separately** from a hand motion |
| R2 | 2 | Read, per word or number group | A part number such as "HF-71861" is one group |
| D3 | 3 | Decide or judge (simple) | Yes/no checks: right label? defect present? |
| X5 | 5 | Apply pressure without movement | Seat, snap, press a seal |
| T2 | 2 | Transfer or regrasp | Pass between hands; reposition in the fingers |
| K6 | 6 | Crank or turn, per full revolution | Handwheels, cranks |
| L1 | 1 | Load factor per loaded movement | 1 per 2 kg above 2 kg per hand (8 kg in two hands = 4 kg per hand → L1) |

All values are **teaching values**. The official MODAPTS auxiliary codes and values are in the IMA manual.

## Notes on use

- **Reading and deciding** are often hidden inside inspection steps. Code them explicitly, because they are frequent targets for scanners, colour coding and poka-yoke.
- **Load factor** only applies to movements that carry the load, not to the reach to it.
- **Walking** is best removed by layout, not sped up.

## Run it

```bash
python tools/ptskit.py practice     # includes auxiliary exercises P5-P10
```

## Check yourself

1. Code: walk 4 steps to a shelf, read a 3-group label, decide if it is the right bin.
2. Code the load factor for a 6 kg casting carried in one hand.
3. Code: turn a crank handle 5 full revolutions.

<details><summary>Answers</summary>

1. W6x4 R2x3 D3 = 24 + 6 + 3 = **33 U**.
2. 6 − 2 = 4 kg above the 2 kg threshold, at 1 per 2 kg, so 2 load units. Write it as **L1x2** on that loaded movement (2 U).
3. **K6x5** = 30 U.

</details>
