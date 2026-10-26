# Module 06 — Planning Units · Affinities

Outline items: **Planning units**, **Affinities**

## Objectives

- Define the planning units (areas) the layout will arrange, and size them.
- Rate the closeness needed between every pair of planning units, with reasons.

## Planning units

A **planning unit** is an area the layout treats as one block: a department, a cell, a storage area, an office. Choose units at the right level. Too few and the layout hides problems. Too many and the analysis becomes unmanageable.

**Space** for each unit (course convention): machine footprints × 2.5 (operator, material and maintenance space) × 1.25 (aisles), or a standard for non-machine areas:

| Unit | m² | Basis |
|---|---|---|
| RCV Receiving | 110 | standard |
| SHR Shear | 70.3 | 22.5 m² of machines |
| PUN Punch | 187.5 | 60.0 m² |
| BRK Press brake | 112.5 | 36.0 m² |
| WLD Weld | 126.6 | 40.5 m² |
| PNT Paint | 168.8 | 54.0 m² (booth + oven) |
| ASM Assembly | 108.0 | 34.6 m² (12 benches) |
| TST Test | 30.0 | 9.6 m² |
| PKG Pack & ship | 140 | standard |
| WHS Warehouse | 93.1 | target pallets, 3-high racks, × 2 for aisles |
| TLR Tool room | 75.0 | 24.0 m² |
| OFF Offices | 120 | standard |
| **Total** | **1,341.8** | of 2,000 m² available |

The remaining ≈ 660 m² covers main aisles, cells, staging and expansion. The multipliers are rules of thumb. Check them against your own areas.

## Affinities

**Closeness ratings** state how important it is for two units to be near each other. The widely used letter scale:

| Rating | Meaning | Weight (this course) |
|---|---|---|
| **A** | Absolutely necessary | 4 |
| **E** | Especially important | 3 |
| **I** | Important | 2 |
| **O** | Ordinary closeness OK | 1 |
| **U** | Unimportant | 0 |
| **X** | Not desirable (keep apart) | −4 |

Ratings come from **flow** and from **other reasons**:

- **Flow-based** (course convention: relative to the largest flow): A ≥ 90 %, E ≥ 75 %, I ≥ 40 %, otherwise O.
- **Non-flow reasons:**
  - tooling: TLR–PUN I, TLR–BRK I
  - component kitting: WHS–ASM I
  - engineering support: OFF–TST O
  - paperwork: OFF–RCV O
  - safety: **WLD–PNT X** (sparks and fumes)

Result:

- **A** (2): PNT–ASM, PUN–BRK
- **E** (4): RCV–SHR, BRK–WLD, ASM–TST, SHR–PUN
- **I** (6), **O** (6), **X** (1)
- U: the other 47 pairs

Always record the **reason** with each rating. Reasons are what you discuss when people disagree.

## Run it

```bash
python tools/fwdkit.py space
python tools/fwdkit.py affinities
```

## Check yourself

1. The punch department has two turret punches of 6.0 m × 5.0 m. Check its 187.5 m².
2. Why is WLD–PNT rated X even though its flow would make it E?

<details><summary>Answers</summary>

1. 2 × 30 = 60 m² × 2.5 × 1.25 = **187.5 m²**.
2. Safety and quality override flow: sparks and fumes near powder coating are a fire and contamination risk. The flow is served by a short path *across* a separation instead.

</details>
