# Solutions

Module check answers are inside each module. Below: the capstone paper case (Option B) and an instructor summary.

## Capstone Option B — order-entry kaizen

1. **Takt** = 450 min / 120 orders = **3.75 min per order**.
2. **Effective time per order per staff member** (C/T × share of orders ÷ staff):

| Step | Effective (min) | Daily capacity | vs takt |
|---|---|---|---|
| Receive | 1.5 | 300 | OK |
| Check configuration | 3.0 | 150 | OK — but 18% of orders loop back to the customer, adding rework and waiting |
| Credit check | 2.0 | 225 | OK |
| Enter in ERP | 2.0 | 225 | OK |
| **Engineering review** | 20 × 0.25 / 1 = **5.0** | **90** | **Constraint** (over takt) |
| Confirm | 1.5 | 300 | OK |

Engineering can review only ~90 orders' worth of specials per day against 120 orders' demand → queues grow; this matches the 70-order queue.

3. Total queue = 40 + 95 + 30 + 60 + 70 + 25 = **320 orders** → lead time = 320 / 120 = **2.7 days**. Average processing time per order = 1.5 + 6 + 2 + 4 + 0.25 × 20 + 1.5 = **20 min** → PCE = 20 / (2.67 × 450) ≈ **1.7%**.
4. Biggest wastes: **Waiting/Inventory** (320 orders queued), **Defects** (18% of configurations wrong → customer clarification loop), **Non-utilized talent / Extra-processing** (engineers reviewing standard-able specials).
5. Future state ideas: configurator with rules at order receipt (eliminates most configuration errors and the check step's rework); "standard specials" catalog so most specials skip engineering; dedicate engineering capacity to the constraint (exploit: no interruptions, triage by complexity); FIFO lanes with WIP caps; level release of orders through the day. If queues fall to ~60 orders total, lead time ≈ 0.5 day.
6. A3 and 30/60/90 plan: student work; use `templates/a3-template.md`.

## Instructor summary (main case)

| Item | Value |
|---|---|
| Takt | 90 s (840 min / 560) |
| Current WIP, lead time, PCE | 5,170 units; 9.23 days; 0.08% |
| Constraint | Preload set, effective C/T 111.8 s, capacity 451/day |
| Spaghetti | 100 → 11.5 m/unit; 56 → 6.4 km/day |
| Line balance | Straight 5 stations, 63.6%; U-cell 4 operators, 79.4% |
| Kanban | 9 cards × 40 = 360 units max |
| SMED | 50 min experienced → 34 min internal → 17 min after |
| OEE (preload) | A 0.850 × P 0.825 × Q 0.957 = 0.671 |
| Output before/after | Mean 464.6 → 545.5; mR̄ 29.3 → 16.4; 9 of 15 after-days above old UNPL |
| 5S audit | 7 → 17 of 25 |
