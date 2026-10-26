# Module 13 — Design Procedures · Defining Infrastructure · Scheduling · Material Handling and Containers

Outline items: **Design procedures**, **Defining infrastructure**, **Scheduling**, **Material handling and containers**

## Objectives

- Follow a repeatable cell design procedure.
- Define the infrastructure, scheduling method and material handling a cell needs to run.

## Design procedures

Cell design procedure (course version):

1. Select the family (P–Q, routings, cell formation).
2. Engineer the process (Module 10).
3. Compute takt, machines and operators (Module 11).
4. Balance the work (Module 14).
5. Choose the configuration and lay out the cell (Module 15).
6. Define infrastructure, scheduling and material handling (this module).
7. Define supervision, roles and rewards (Module 14).
8. Mock up, pilot and run in. Measure output, quality and ergonomics, then adjust.

## Defining infrastructure

| Item | Wall-box cell |
|---|---|
| Power | Punch, brake, spot welder and press supplies; drops placed for the chosen configuration |
| Compressed air | Punch and press; quick-connect drops |
| Ventilation | Spot-weld fume extraction |
| Lighting | Task lighting at inspection |
| Floor | Foundation or floor-load check for the punch and brake |
| IT and visual | Production-by-hour board; andon; terminals for kanban and quality data |
| Support | Tool storage at the cell; first-aid and spill kits; nearby break area |

Infrastructure is the most common cause of start-up delays. List it at design time, not at installation.

## Scheduling

The cell makes 12 SKUs that share setups on the punch (20 min) and other machines.

- Punch run time per day = 62 s × 131,730 / 230 = **35,510 s**.
- Punch time available per day = 2 shifts × 27,000 s × 90 % = 48,600 s, so spare time = **13,090 s** a day.
- One changeover of all 12 SKUs on the punch = 12 × 20 min = 14,400 s.
- **EPEI** (every part every interval) = 14,400 / 13,090 = **1.1 days**. Every SKU can be made about every 1.1 days.
- Up to 10 punch changeovers a day are possible.

Schedule the cell with a **daily repeating sequence** (heijunka) instead of weekly batches. Inventory drops to about one day of each SKU. Setup reduction on the punch shortens EPEI further.

## Material handling and containers

- **Container**: 20 boxes per paint rack (one load), at hand height, with a fixed location in and out of the cell.
- **Kanban** between the cell and paint: number of containers = daily demand × lead time × (1 + safety) ÷ container quantity.
  - 572.7 × 1.0 × 1.15 ÷ 20 = 32.93, so **33 kanbans**.
- **Blanks in**: a lift table at the shear, replenished on a fixed route by the material handler.
- **Rules**:
  - Every container has a home address.
  - No floor storage.
  - Containers should be light enough for safe manual handling, or moved on carts.

## Run it

```bash
python tools/fwdkit.py schedule
python tools/fwdkit.py kanban
```

## Check yourself

1. If punch setup fell to 8 minutes, what would EPEI become?
2. How many kanbans would a 0.5-day loop need?

<details><summary>Answers</summary>

1. 12 × 8 × 60 = 5,760 s / 13,090 s = **0.44 days**. Every SKU about twice a day.
2. 572.7 × 0.5 × 1.15 / 20 = 16.5, so **17 kanbans**.

</details>
