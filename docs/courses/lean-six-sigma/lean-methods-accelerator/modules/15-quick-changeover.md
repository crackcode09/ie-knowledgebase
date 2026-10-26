# Module 15 — Quick Changeover

**Time:** 60 min

## Learning objectives

1. Apply the SMED steps to reduce changeover time.
2. Show how shorter changeovers increase flexibility and reduce inventory (EPEI).

## 1. SMED

Shigeo Shingo, *A Revolution in Manufacturing: The SMED System* (1985). Goal: changeovers in single-digit minutes.

1. **Observe** and record every element (video).
2. **Separate** internal (machine stopped) from external (machine running) work.
3. **Convert** internal to external (preset tools, pre-staged fixtures, duplicate fixtures).
4. **Streamline** the rest (quick clamps, locating pins, no adjustments, parallel work).
5. **Standardize** and train.

## 2. Case — CNC changeover

| Element | Min | Before | After |
|---|---|---|---|
| Find program, tools, fixture | 18 | internal | **external** (pre-staged cart, program called by barcode) |
| Fetch and preset tools at machine | 22 | internal | **external** (offline tool presetter) |
| Remove fixture | 9 | internal | 4 (quick-release clamps) |
| Clean table | 6 | internal | 4 (chip guards) |
| Mount fixture, indicate | 17 | internal | 4 (zero-point locating pins) |
| Touch-off tools | 8 | internal | 2 (preset offsets loaded from presetter) |
| First-part run and inspection | 10 | internal | 6 (in-machine probe) |
| **Machine stopped** | | **90** | **20** |

```bash
python tools/lean.py smed
```

Separating alone: 90 → 50 min. Converting and streamlining: 50 → **20 min**.

## 3. Why it matters: flexibility and inventory

**EPEI (every part every interval)** = how often you can cycle through all products:

  EPEI = (number of changeovers per cycle × changeover time) ÷ time available for changeovers

Both CNCs: available after breakdowns = 2 × 880 × 0.92 = 1,619 min/day; run time needed = 220 × 6.3 = 1,386 min/day → **233 min/day** left for changeovers.

| | Changeover | 3 families per cycle | EPEI |
|---|---|---|---|
| Before | 90 min | 270 min | **1.16 days** — can't even run every family every day; big batches and inventory |
| After | 20 min | 60 min | **0.26 days** — every family ~4 times a day |

Short changeovers make heijunka (Module 17) possible, cut finished-goods and WIP inventory, and free capacity at the constraint.

## Check yourself

After SMED, should the plant change over 4 times a day or bank the freed time as capacity?

<details><summary>Answer</summary>

It depends on the constraint: CNC is the constraint (Module 16), so use part of the freed time to raise capacity above demand and part to change over more often for smaller batches; decide with takt, EPEI and inventory targets.
</details>
