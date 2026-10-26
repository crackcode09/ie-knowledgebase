# Module 6 — Workplace Design and Ergonomics

**Time:** 90 min

## Learning objectives

1. Design workstations using anthropometric data.
2. Evaluate a manual lift with the revised NIOSH lifting equation.
3. Apply basic ergonomic principles to reduce injury risk.

## 1. Fit the job to the person

Ergonomics designs work around human capabilities and limits. Benefits: fewer musculoskeletal disorders (back, shoulder, wrist), better quality, higher productivity, easier recruiting.

**Risk factors:** force, awkward posture, repetition, duration, contact stress, vibration, and the environment (heat, cold, light, noise).

## 2. Anthropometry

Design for a **range** of people, not the "average person":

| Design case | Use | Example |
|---|---|---|
| Design for the extreme | Reach → 5th percentile (small); clearance → 95th percentile (large) | Bin reach; door height |
| Design for adjustability | Range from small female to large male | Work-surface height, chair |
| Design for the average | Only when adjustability and extremes don't apply | Counter height in a public space |

### Case — packing bench height

Light assembly work is usually best a little below elbow height (often cited as about 5–10 cm below). Using illustrative standing elbow heights for the workforce:

```bash
python tools/ie.py anthropometry
```

| Group | 5th pct | 50th | 95th |
|---|---|---|---|
| Female | 93.6 cm | 101.0 | 108.4 |
| Male | 100.8 cm | 109.0 | 117.2 |

Adjustable range ≈ **84–112 cm** covers 5th-percentile female to 95th-percentile male. A fixed 95 cm bench would be too high for many smaller packers and too low for taller ones. (Use your own population's data or a published survey; the numbers here are illustrative.)

## 3. Revised NIOSH lifting equation

The U.S. National Institute for Occupational Safety and Health (NIOSH) equation (Waters et al., 1993; *Applications Manual*, 1994) gives a **recommended weight limit (RWL)** for a two-handed lift:

  RWL = LC × HM × VM × DM × AM × FM × CM

| Term | Metric formula |
|---|---|
| Load constant LC | 23 kg |
| Horizontal multiplier HM | 25 / H (H = hand distance from ankles, cm) |
| Vertical multiplier VM | 1 − 0.003 × \|V − 75\| (V = hand height at origin, cm) |
| Distance multiplier DM | 0.82 + 4.5 / D (D = vertical travel, cm) |
| Asymmetry multiplier AM | 1 − 0.0032 × A (A = twist angle, degrees) |
| Frequency FM, coupling CM | From NIOSH tables |

**Lifting index (LI)** = load ÷ RWL. LI > 1 indicates increased risk for some workers; LI > 3 is high risk for many.

### Case — lifting a 14 kg box of kits

```bash
python tools/ie.py niosh
```

| | Before: box from floor pallet to conveyor | After: pallet on a leveler, box pulled close |
|---|---|---|
| H, V, D, A | 50 cm, 15 cm, 80 cm, 45° | 30 cm, 70 cm, 25 cm, 0° |
| HM, VM, DM, AM | 0.50, 0.82, 0.876, 0.856 | 0.833, 0.985, 1.0, 1.0 |
| FM, CM (from tables, assumed) | 0.85, 0.95 | 0.85, 0.95 |
| **RWL** | **5.71 kg** | **15.24 kg** |
| **Lifting index** | **2.45** | **0.92** |

The redesign (spring-loaded pallet leveler, box slides to the operator, no twist) brings the lift below LI 1 without changing the box weight. Always check the multipliers against the official NIOSH tables for your frequency and duration.

## 4. Other principles

- Neutral postures: elbows close, wrists straight, no reaching above shoulder or below knee for frequent tasks.
- Reduce force: lighter tools, mechanical assists, good handles.
- Reduce repetition: job rotation, automation of the most repetitive motions.
- Environment: task lighting for inspection, anti-fatigue mats, temperature.

## Check yourself

What happens to RWL if the box is held 60 cm from the ankles instead of 30 cm, all else equal?

<details><summary>Answer</summary>

HM drops from 25/30 = 0.833 to 25/60 = 0.417, so RWL halves.
</details>
