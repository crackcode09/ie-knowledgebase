# Module 12 — Writing an Analysis (Applying Motion Times)

## Objectives

- Lay out a complete two-handed analysis.
- Total it correctly, applying simultaneous-motion rules and frequencies.

## Format

Each row is one **step**. Columns:

| Column | Content |
|---|---|
| Description | What happens, in plain words |
| LH codes | Left-hand motions in order; `H` = holding; blank = idle |
| RH codes | Right-hand motions in order |
| Body / eye / process | Body motions, eye time and machine or tool time (`PT<cs>`) |
| Time | Hands (simultaneous → max; otherwise sum) + body / eye / process |
| Frequency | How often per cycle, if not every cycle (e.g. 1/20 for a box change every 20 parts) |

Template: `templates/analysis-sheet.csv`. Tool: `python tools/dmtkit.py lab L01`.

## Worked example: Lab 1 (bolt into fixture, right hand only)

| Step | RH | cs |
|---|---|---|
| Reach to bin, select bolt | R40c Gx | 64 + 14 = 78 |
| Move bolt to fixture, place, release | M35c PLS RL | 52 + 9 + 2 = 63 |
| Return hand toward bin | R10a | 17 |
| **Total** | | **158 cs = 1.58 s** |

The last reach "toward the bin" is a part of the next cycle's reach. Make sure each motion is counted once per cycle.

## Rules of good practice

1. Code from the **method description**, and verify on the floor or on video.
2. Measure **distances**. Don't guess.
3. Analyse each hand fully before deciding what is simultaneous.
4. Put process times in the body/process column. Never code them as hand motions.
5. Record **frequencies** for occasional elements (container changes, tool changes, inspections every *n*) and prorate them.
6. Keep the analysis **traceable**: anyone should be able to recompute it from the sheet.

## Occasional elements

Example: every 50 parts, the operator walks 2 steps, swaps a tote and returns, which is `WK2 R30a Gp M40b/3 RL WK2`. Compute its total, then add total ÷ 50 per cycle.

## Check yourself

Compute the tote-change element above and its per-cycle share.

<details><summary>Answers</summary>

WK2 = 90; R30a Gp = 35 + 3 = 38; M40b/3 = 48 × 1.03 + 3 = 52.4; RL = 2; WK2 = 90. Total = **272.4 cs**. Per cycle = 272.4 / 50 ≈ **5.4 cs**.

</details>
