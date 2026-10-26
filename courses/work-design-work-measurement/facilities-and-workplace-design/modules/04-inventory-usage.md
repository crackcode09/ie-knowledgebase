# Module 04 — Inventory · Usage

Outline items: **Inventory**, **Usage**

## Objectives

- Size storage from target inventory, not current inventory.
- Locate items by how often they are used.

## Inventory

`data/inventory.csv`: 30 purchased and raw-material items, with on-hand quantity, daily usage and unit volume.

| Measure | Now | At a 10-day target |
|---|---|---|
| Median days on hand | 37.1 | 10 |
| Items over 30 days | 18 of 30 | 0 |
| Volume | 296.3 m³ | 86.8 m³ |
| Pallet positions (1.2 m³ pallets, 75 % fill) | 330 | 97 |
| Floor area, single stack | 475 m² | 140 m² |
| Floor area, 3-high racking × 2 for aisles | — | **93 m²** (warehouse planning unit) |

Sizing storage for **today's** inventory builds in today's excess. Agree the **target** days of cover with materials management (by item class, lead time and variability) before sizing. Cutting inventory is often the cheapest space you will ever find.

## Usage

Locate items by **how often they are picked**, not by how much there is:

| Class | Items | Share of picks | Location rule |
|---|---|---|---|
| A | 2 | 60.3 % | At point of use, or the nearest, waist-height ("golden zone") positions |
| B | 4 | 27.3 % | Near the point of use |
| C | 24 | 12.4 % | Further away, higher or lower levels |

Two items (M02, M04) make up 60 % of picks. Moving just those two to point-of-use flow racks cuts most of the walking.

## Run it

```bash
python tools/fwdkit.py inventory
python tools/fwdkit.py usage
```

## Check yourself

1. An item uses 40 units a day and has 1,600 on hand. How many days of cover is that, and what is the excess at a 10-day target?
2. Why locate by picks rather than by volume?

<details><summary>Answers</summary>

1. 1,600 / 40 = **40 days**. Excess = 1,600 − 400 = **1,200 units**.
2. Travel time is driven by how often you go to a location. A bulky item picked once a month can be far away; a small item picked hundreds of times a day must be close.

</details>
