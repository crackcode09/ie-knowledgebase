# Module 7 — Line Balancing and Heijunka

**Time:** 50 min

## Learning objectives

1. Balance work to takt across operators.
2. Explain heijunka (level loading) by volume and mix.

## 1. Line balancing

1. List work elements with times (observed, repeatable).
2. Minimum operators = ⌈total work content ÷ takt⌉.
3. Assign elements in sequence to operators without exceeding takt (plan to ~95% of takt for margin).
4. Balance efficiency = work content ÷ (operators × takt).
5. Show it on a yamazumi (stacked bar) chart against the takt line.

### Case — assembly & pack (takt 240 s)

| Element | Plugs | Cartridge valves | Torque | Seals | Functional test | Label | Pack |
|---|---|---|---|---|---|---|---|
| Seconds | 38 | 64 | 41 | 29 | 72 | 18 | 33 |

Total = **295 s** → minimum = ⌈295/240⌉ = **2 operators**.

```bash
python tools/lean.py balance
```

| Operator | Elements | Load |
|---|---|---|
| 1 | Plugs, cartridge valves, torque, seals | 172 s |
| 2 | Functional test, label, pack | 123 s |

Efficiency = 295 / (2 × 240) = **61.5%**. Operator 2 has 117 s of slack each cycle. Options: move "seals" to operator 2 (→ 143 s / 152 s, better balance, same efficiency); or have one operator run assembly at a lower demand with a different takt; or use the spare time for kitting parts for operator 1. Efficiency only rises by removing waste or adding work to the line — balancing redistributes it.

## 2. Heijunka — level loading

Heijunka means leveling the **volume** and the **mix** of production over time, instead of running whatever large batches the orders imply.

| Unleveled | Leveled |
|---|---|
| Mon–Tue all family A, Wed family B, Thu–Fri family C | Every day a repeating pattern: A B A C B A A B … |
| Big swings in material, labor and capacity needs | Steady demand on people, machines and suppliers |
| Long waits for the family not being run | Every family available every day |

Leveling the mix requires **quick changeovers** (Module 15) — otherwise changing often wastes capacity. Module 17 builds the actual heijunka sequence for the plant.

## Check yourself

Why does leveling the schedule reduce inventory?

<details><summary>Answer</summary>

When every product is made every day in small amounts, you only need stock to cover a day's demand instead of the weeks between big batches.
</details>
