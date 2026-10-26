# Module 5 — Process Metrics and Takt Time

**Time:** 45 min

## Learning objectives

1. Define and calculate core process metrics.
2. Use takt time to set the pace of work.

## 1. Core metrics

| Metric | Definition |
|---|---|
| **Takt time** | Available working time ÷ customer demand — the pace the customer requires |
| **Cycle time (C/T)** | Time between units completing a step (observed) |
| **Effective cycle time** | C/T ÷ number of parallel machines/operators ÷ uptime |
| **Lead time** | Time for one unit to go through the whole process |
| **WIP** | Units started but not finished |
| **Throughput** | Units completed per unit time |
| **Little's law** | Lead time = WIP ÷ throughput |
| **Process cycle efficiency (PCE)** | Value-added time ÷ lead time |
| **Changeover time (C/O)** | Last good part of one product → first good part of the next |
| **Uptime / availability** | Share of scheduled time the step can run |
| **First-pass yield (FPY)** | Share of units right the first time |

## 2. Takt time — manifold plant

Available time = 2 shifts × 480 min − 2 × 40 min breaks/meetings = **880 min/day**.
Demand = **220 manifolds/day**.

  **Takt = 880 / 220 = 4.0 minutes per manifold**

Every step must be able to complete one manifold every 4.0 minutes, on average, including its losses.

| Step | C/T (min) | Machines / operators | Uptime | Effective C/T (min) | vs takt |
|---|---|---|---|---|---|
| Saw | 1.2 | 1 | 98% | 1.22 | OK |
| **CNC machining** | 6.3 | 2 | 77% | **4.09** | **Over takt** |
| Deburr | 3.1 | 1 | 100% | 3.10 | OK |
| Wash | 2.0 | 1 | 95% | 2.11 | OK |
| Leak test | 3.4 | 1 | 92% | 3.70 | OK, little margin |
| Assemble & pack | 3.6 | 1 | 97% | 3.71 | OK, little margin |

```bash
python tools/lean.py vsm
```

CNC capacity = 880 / 4.09 = **215 per day** — below demand. This is why on-time delivery is 82%.

## 3. Using takt

- **Staffing:** operators needed ≈ total work content ÷ takt (Module 7).
- **Pacing:** an hour-by-hour board shows the target (60 / 4.0 = 15 per hour) vs actual.
- **Design:** equipment must be sized to effective C/T below takt with margin.
- **Takt changes with demand:** recompute when demand or shifts change — and rebalance.

## Check yourself

Demand rises to 250/day with the same hours. New takt? Which steps are now over takt?

<details><summary>Answer</summary>

880 / 250 = 3.52 min. CNC (4.09), leak test (3.70) and assembly (3.71) are over takt.
</details>
