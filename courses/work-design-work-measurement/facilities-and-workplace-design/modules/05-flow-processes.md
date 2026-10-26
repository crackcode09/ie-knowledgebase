# Module 05 — Flow · Processes

Outline items: **Flow**, **Processes**

## Objectives

- Build a from–to chart of material flow in common handling units.
- Analyse the process steps that create the flow.

## Flow

Convert every product's volume to **loads** (units ÷ units per load), then add up the loads between consecutive routing steps:

**Flow (loads/yr) between department pairs** (both directions combined):

| Pair | Loads/yr | Pair | Loads/yr |
|---|---|---|---|
| PNT–ASM | 16,887 | TST–PKG | 7,649 |
| PUN–BRK | 15,825 | TST–WHS | 7,235 |
| RCV–SHR | 14,884 | PKG–WHS | 7,235 |
| BRK–WLD | 14,884 | RCV–PUN | 2,003 |
| WLD–PNT | 14,884 | BRK–PNT | 2,003 |
| ASM–TST | 14,884 | ASM–PKG | 2,003 |
| SHR–PUN | 13,822 | SHR–BRK | 1,062 |

The **intensity** of flow, not just whether a flow exists, should decide which departments sit together.

**Backtracking.** In the current layout, **10** routing steps move *back toward* receiving instead of toward shipping. Backtracks add distance, cross other flows and congest aisles.

## Processes

For each process (department), record:

- what it does to the product, and which families use it
- equipment, capacity and changeover time
- environment: noise, fumes, heat, cleanliness, floor loading
- its relationships with other processes beyond flow (shared people, tools, services)

| Process | Corvan notes |
|---|---|
| Shear, punch, brake | Heavy machines; tooling from the tool room; punch is noisy |
| Weld | Sparks and fumes: must be separated from paint (fire and finish risk) |
| Paint (powder booth + oven) | A large **monument**: expensive to move, sets the layout around it |
| Assembly, test | Clean, quiet; engineering support |
| Warehouse | Floor cabinets go to stock before shipping |

## Run it

```bash
python tools/fwdkit.py flow
```

## Check yourself

1. WLD–PNT has one of the highest flows (14,884 loads), but weld and paint must not be adjacent. How can both needs be met?
2. Why count backtracks as well as total distance?

<details><summary>Answers</summary>

1. Place them **near but not adjacent**: separated by an aisle, a wall or another low-risk area, with a short, direct conveyor or handling path between them.
2. Backtracking flows cross other flows, create congestion and confusion, and usually mean a department is out of sequence, even when total distance looks acceptable.

</details>
