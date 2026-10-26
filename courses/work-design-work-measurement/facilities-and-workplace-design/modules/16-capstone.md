# Module 16 — Capstone: A Junction-Box Cell

## Objective

Use the full course procedure to plan a second cell and fit it into the new block layout.

## Brief

Corvan wants a cell for the **F3 junction box** family (10 SKUs, 80,130 units a year), running **one shift** (230 days × 7.5 h). Proposed operations:

| Op | Description | Machine s | Manual s | Setup min |
|---|---|---|---|---|
| OP10 | Turret punch | 30 | 10 | 20 |
| OP20 | Brake 2 bends | 10 | 16 | 10 |
| OP30 | Press hardware | 5 | 14 | 5 |
| OP40 | Inspect, load to paint rack | 0 | 12 | 0 |

Assume 90 % machine availability, lots of 150, 2 s of walking per operation, 40 boxes per paint rack, a 1-day kanban loop and 15 % safety.

## Tasks

1. Compute takt, the s per piece and the utilization of each machine, and identify the bottleneck.
2. How many operators does the cell need? What would you do with the spare capacity?
3. How many kanbans does the cell–paint loop need?
4. Choose a configuration and sketch the cell (input and output together).
5. Where does the cell go in block layout B? Which relationships change?
6. List the infrastructure, the ergonomic design points and the supervision arrangements.
7. Write a one-page recommendation.

<details><summary>Capstone key (run <code>python tools/fwdkit.py capstone</code>)</summary>

- **Takt** = 6,210,000 / 80,130 = **77.5 s**.
- **Machines**:
  - Punch 30 + 10 + 1,200/150 = **48.0 s**, capacity 116,437, utilization **68.8 %** (bottleneck)
  - Brake 30.0 s, 43.0 %
  - Press 21.0 s, 30.1 %
- **Operators**: (52 + 8) / 77.5 = **0.77**, so **1 operator**. Spare capacity: add the cell's own setups and replenishment; or run the cell 0.77 of the shift and cross-train into the wall-box cell; or plan for growth.
- **Kanbans**: 80,130 / 230 × 1.0 × 1.15 / 40 = 10.02, so **11**.
- **Configuration**: a small U or L with OP10 next to OP40. Four machines fit easily in one grid slot.
- **Block layout**: the cell takes junction-box flow out of the PUN–BRK departments. PUN–BRK flow falls, the remaining shared machines serve F2 and F4, and the cell needs to be near **PNT** (shared paint) and **RCV** (blanks). A second punch is a capital decision. Check whether it can share the wall-box cell's punch instead: the combined load at 2 shifts would be over 100 %, so not without major setup reduction.
- **Recommendation**: build the cell with its own small punch only if the business case covers it. Otherwise first cut setup time on the existing punch, then reassess.

</details>

## Skill check

1. Name the five input-data letters for layout planning.
2. What does an X closeness rating mean, and give one example.
3. Why convert units to loads before flow analysis?
4. What does rank order clustering produce, and what is an exceptional element?
5. Write the formulas for takt time and the number of operators.
6. Why is the U-shape often preferred for cells?
7. Why size storage on target inventory?
8. Name two reward approaches that support cell teamwork.

<details><summary>Answers</summary>

1. P products, Q quantities, R routings, S supporting services, T timing.
2. Not desirable: keep apart. For example, welding next to painting.
3. Handling and space depend on loads (containers or moves). Units of very different sizes would distort flow intensity.
4. A block-diagonal part–machine matrix showing part families and machine groups. An exceptional element is a part that needs a machine outside its cell.
5. Takt = available time ÷ demand. Operators = total manual work (plus walking) ÷ takt, rounded up.
6. Shortest walking; input and output together; flexible operator assignments; good communication.
7. Current inventory may include excess and obsolete stock; target days of cover reflect how the business will run.
8. Any two: skill-based pay, team gainsharing, recognition programs.

</details>
