# Module 03 — Predetermined Time Standards

## Objectives

- Explain how a PMTS works and what "normal time" means in one.
- Compare the main PMTS families and their time units.
- State when a PMTS is the right tool.

## How a PMTS works

1. **Describe the method** in enough detail to see every motion: what is reached for, how it is grasped, where it is placed, and how precisely.
2. **Classify each motion** with the system's rules (body member or distance, type of grasp, precision of placement, body motions).
3. **Look up** each code's time and **add** them. When motions happen at the same time, only the limiting motion counts.
4. **Add allowances** (personal, fatigue, delay) to turn normal time into a standard.

PMTS times represent a **normal pace** by an experienced worker using the specified method. That is why no rating is needed.

## Families and units

| System | Time unit | Source |
|---|---|---|
| MTM (Methods-Time Measurement, first released 1948) and its variants | 1 TMU = 0.00001 h = 0.036 s | [Wikipedia: PMTS](https://en.wikipedia.org/wiki/MODAPTS) |
| MOST family (BasicMOST, MiniMOST, MaxiMOST) | TMU-based index values | Same; Zandin (2003) |
| MODAPTS | 1 MOD = 0.129 s | [Eisbrenner PG](https://eisbrennerpg.com/about-modapts/) |
| **This course's teaching card** | **1 U = 0.1 s** | `data/teaching_code_card.csv` (original, illustrative) |

The International Labour Office reported about 200 different predetermined time systems by 1992 (Kanawaty, *Introduction to Work Study*, as cited on the same Wikipedia page).

Unit conversion for 2.4 s: 24 U = 66.7 TMU = 18.6 MOD.

## Detailed vs higher-level systems

- **Detailed systems** code every basic motion. They give high precision for short, repetitive cycles, but analysis is slow.
- **Higher-level systems** code sequences or larger blocks. They are faster to apply, which suits long, less repetitive work.

Choose by cycle length, repetition and the accuracy you need.

## When to use a PMTS

| Good fit | Poor fit |
|---|---|
| Manual, repetitive, short-cycle work | Machine-paced work (use the machine's time) |
| Jobs not yet built; comparing methods | Thinking, diagnosing or creative work |
| Needing consistent, explainable standards | Highly variable tasks with no defined method |
| Ergonomic redesign (the codes show where the effort goes) | Work where walking or waiting dominates and isn't defined |

## Run it

```bash
python tools/ptskit.py units
```

## Check yourself

1. Convert 3.6 s into TMU, MOD and teaching units.
2. Why must the method be fully defined before a PMTS analysis?

<details><summary>Answers</summary>

1. 3.6 / 0.036 = **100 TMU**; 3.6 / 0.129 = **27.9 MOD**; 3.6 / 0.1 = **36 U**.
2. The codes depend on the exact motions: distances, grasp type and placement precision. An undefined method can't be coded, and a different method gives a different time.

</details>
