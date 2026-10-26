# Module 01 — Facilities and Strategy · Levels of Design

Outline items: **Facilities and strategy**, **Levels of design**

## Objectives

- Link layout decisions to business strategy.
- Distinguish the levels at which facilities are designed, and what each decides.

## Facilities and strategy

Layout largely determines workflow. A convoluted layout creates long moves, backtracking, queues and hidden inventory. Whatever product you make, the facility should be designed to support how the business **competes**:

| Competitive priority | What the facility must do | Layout implication |
|---|---|---|
| Low cost | Short flow, little handling, high utilization | Product-oriented lines and cells for high-volume families |
| Speed and short lead time | Small queues, quick changeovers, visible flow | Cells; point-of-use storage; no central queues |
| Variety and customization | Flexibility in routing and mix | Functional (process) areas for low-volume variety, plus cells for repeaters |
| Quality | Clear ownership, fast feedback | Cells where operators see the next process; inspection at the source |
| Growth | Room to expand without rework | Expansion directions planned; fixed "monuments" placed so they don't block growth |

## Levels of design

Facilities are planned from the outside in. Each level sets limits for the next.

| Level | Decides | Typical output |
|---|---|---|
| 1 Site / location | Where the facility is; site, access, utilities | Site plan |
| 2 Overall (block) layout | Where each department or planning unit goes | Block layout with flows |
| 3 Detailed layout | Where every machine, bench, aisle and rack goes within each area | Detailed drawings |
| 4 Workstation | Heights, reaches, tools and parts presentation at each workplace | Workstation drawings, standard work |
| 5 Installation and start-up | Moves, utilities hook-up, debugging, ramp-up | Move plan, start-up plan |

Levels 2 and 3 are often planned with some overlap, so that a cell design (level 3) can shape the block layout (level 2). This sequence is the classic approach in systematic layout planning texts. The table above is the course's version.

## Running case: Corvan Enclosures

**Corvan Enclosures** (fictional) makes steel electrical enclosures in a **50 m × 40 m** plant (2,000 m²). The plant has grown department by department. Products now criss-cross the floor, and wall boxes (the highest-volume family) take days to get through.

| Family | SKUs | Units/yr | Units per load |
|---|---|---|---|
| F1 wall box | 12 | 131,730 | 20 |
| F2 floor cabinet | 8 | 14,470 | 2 |
| F3 junction box | 10 | 80,130 | 40 |
| F4 custom | 10 | 4,250 | 4 |

The IE team will:

- re-plan the **block layout** (levels 2–3)
- design a **wall-box cell** (levels 3–4)

All data is simulated with a fixed seed (2028).

## Run it

```bash
python tools/fwdkit.py data
python tools/fwdkit.py all
```

## Check yourself

1. Corvan wants to cut wall-box lead time from days to hours. Which layout type does that priority point to?
2. Why decide the block layout before detailed machine positions?

<details><summary>Answers</summary>

1. A product-focused **cell** for the wall-box family, with short flow and small queues.
2. The block layout sets which areas are next to each other and how big they are. Detailed layouts made first may not fit, or may lock in poor flow between areas.

</details>
