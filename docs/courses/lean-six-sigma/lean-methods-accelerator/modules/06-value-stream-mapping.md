# Module 6 — Value Stream Mapping, Including the Extended Process

**Time:** 75 min

## Learning objectives

1. Draw a current-state value stream map with data and a timeline.
2. Calculate lead time and PCE.
3. Extend the map beyond the plant to suppliers and customers.
4. Design a future state.

## 1. Current-state map — manifold plant

```
 Distributors ──monthly orders + weekly forecast──► Production control (MRP) ──weekly schedule to every step──►
 Bar-stock supplier ◄── monthly PO ──┘                                                    

 Supplier ═truck weekly═► △900  [Saw]  △640  [CNC ×2]  △300  [Deburr]  △260  [Wash]  △180  [Leak test]  △520 [Assemble & pack] ═► Distributors
                                 C/T 1.2   C/T 6.3          C/T 3.1         C/T 2.0       C/T 3.4             C/T 3.6
                                 C/O 15    C/O 90           C/O 0           C/O 10        C/O 20              C/O 15
                                 Up 98%    Up 77%           Up 100%         Up 95%        Up 92%              Up 97%

 Timeline:   4.09 d  | 1.2 m | 2.91 d | 6.3 m | 1.36 d | 3.1 m | 1.18 d | 2.0 m | 0.82 d | 3.4 m | 2.36 d | 3.6 m
```

(△ = inventory, units; days = units ÷ 220/day; C/T and C/O in minutes.)

```bash
python tools/lean.py vsm
```

| Summary | Value |
|---|---|
| Total inventory | **2,800 units** |
| Lead time (Σ inventory days) | **12.73 days** |
| Processing time (Σ C/T) | **19.6 min** |
| PCE = 19.6 min ÷ (12.73 × 880 min) | **0.18%** |

**Observations:** every step is pushed by its own schedule; the largest inventories are raw material (monthly buying) and finished goods (building ahead); CNC is over takt with 90-minute changeovers; production control schedules everyone, so nobody knows the real priority.

## 2. The extended value stream

Map one level out — supplier and customer:

| Link | Current state | Effect |
|---|---|---|
| Bar-stock supplier → plant | Monthly PO, weekly truck, 3-week lead time | 4 days of raw material; shortages when forecast is wrong |
| Plant → distributors | Distributors order monthly in batches | Demand to the plant swings far more than end-user demand (bullwhip — Module 12) |
| Distributors → equipment builders | Weekly orders, fairly steady | True demand is much smoother than what the plant sees |

The biggest lever may be outside the four walls: sharing end-customer demand data and moving distributors to smaller, frequent replenishment.

## 3. Future state — design questions

1. Takt: 4.0 min.
2. Finished-goods supermarket for families A and B (runners); build family C (low volume) to order.
3. Continuous flow: saw → CNC → deburr → wash → leak test in one cell (Module 14).
4. Pull: assembly pulls from the cell via kanban; the cell's input is controlled by a WIP cap (Module 17).
5. Pacemaker: assembly — the only point scheduled, using a leveled heijunka sequence (Modules 7, 17).
6. Process improvements: CNC changeover 90 → 20 min (Module 15); CNC uptime via TPM (Module 19).
7. Supplier: weekly kanban replenishment of bar stock.

**Target:** inventory ~700 units → lead time ≈ 3.2 days; CNC effective C/T < 3.8 min.

## Check yourself

Why does the VSM timeline count inventory in days rather than units?

<details><summary>Answer</summary>

By Little's law, days of inventory equal the waiting time a unit spends there; summing them gives lead time.
</details>
