# Module 4 — Types of Process Maps, Value-Added Flow Charts and Spaghetti Diagrams

**Time:** 60 min

## Learning objectives

1. Choose the right type of process map.
2. Build a value-added flow chart.
3. Draw and measure a spaghetti diagram.

## 1. Types of process maps

| Map | Shows | Use it to |
|---|---|---|
| SIPOC | Suppliers, inputs, 5–7 steps, outputs, customers | Agree scope |
| Flow chart | Steps and decisions | Understand logic, loops |
| Swim-lane map | Steps by role | See handoffs |
| Value-added flow chart | Steps classified VA / BVA / NVA with times | Find waste |
| Spaghetti diagram | Physical path on a layout | Find transport and motion waste |
| Value stream map | Material + information flow + timeline | See end-to-end flow and lead time (Module 6) |

Map what actually happens (walk it), not what the procedure says.

## 2. Value-added flow chart — manifold, one batch

| Step | Time | Class |
|---|---|---|
| Wait in raw-material store | 4.1 days | NVA |
| Saw blank | 1.2 min/unit | VA |
| Forklift to machining building | 20 min/batch | NVA |
| Wait for CNC | 2.9 days | NVA |
| CNC machining | 6.3 min/unit | VA |
| Wait for deburr | 1.4 days | NVA |
| Deburr | 3.1 min/unit | VA |
| Wash | 2.0 min/unit | BVA (required to remove chips for leak test) |
| Leak test | 3.4 min/unit | BVA (customer requirement) |
| Re-machine leakers (8.5%) | — | NVA (defect) |
| Wait for assembly | 0.8 days | NVA |
| Assemble & pack | 3.6 min/unit | VA |
| Wait in finished goods | 2.4 days | NVA |

VA processing ≈ 14 min per unit; total lead time ≈ 12.7 days (Module 6). Showing the steps colored by class (green VA, yellow BVA, red NVA) tells the story faster than any table.

## 3. Spaghetti diagram

Trace the path of a product (or a person) on the floor plan, measure it, and count backtracks and crossings.

**Manifold plant (before):** saw (building 1) → forklift 140 m to building 2 → CNC → deburr 35 m → wash 20 m → leak test 25 m → re-machine leakers back 60 m → assembly 45 m → pack → forklift 140 m back to shipping in building 1. ≈ **465 m per batch** (estimated from the layout drawing), two building moves.

**Proposed cell (Module 14):** saw, CNC, deburr, wash and leak test in one U-shaped cell in building 1; assembly adjacent → ≈ **60 m** (estimated), no forklift.

## Check yourself

Why is the wash step classified BVA rather than VA?

<details><summary>Answer</summary>

The customer doesn't pay for washing; it's needed only because machining leaves chips that would affect the leak test. Reduce it (e.g., through-spindle coolant, chip control) rather than treat it as value.
</details>
