# Module 4 — Day 1: Gemba Walk, Process Maps, Spaghetti Diagram, Takt

**Time:** 2 h

## Learning objectives

1. Run a gemba walk that produces facts, not opinions.
2. Map value-added and non-value-added steps.
3. Draw a spaghetti diagram and quantify motion.
4. Calculate takt time and compare it with cycle times.

## 1. Day 1 schedule (typical)

| Time | Activity |
|---|---|
| 08:00 | Kickoff: sponsor explains why; charter; ground rules; Lean basics refresher |
| 09:30 | Gemba walk — follow a unit from start to finish |
| 11:00 | Time observations; process map; spaghetti diagram |
| 13:30 | Value stream map of current state (Module 5) |
| 15:30 | Takt vs cycle times; identify the constraint (Module 6) |
| 16:30 | Daily review with sponsor (15 min) |

## 2. Gemba walk

*Gemba* = "the actual place." Go and see; don't map from the conference room.

- Follow the product, not the people; walk the path it takes.
- Ask operators: "What gets in your way?" "Where do you wait?"
- Record facts: times, distances, inventory counts, defects seen. Photos.
- Respect: you're there to learn the process, not to judge people.

## 3. The source of value; value-added flow chart

A step is **value-added (VA)** if the customer would pay for it, it changes the product's form, fit or function, and it's done right the first time. Otherwise it's **non-value-added (NVA)** — either pure waste or **necessary NVA** (required today by regulation or current technology, e.g., a test).

Mark each step on the process map VA / NVA / necessary NVA. In the carriage cell: inserting balls and setting preload are VA; walking to fetch seals, waiting for the fixture, moving trays to packing are NVA; the friction test is necessary NVA.

## 4. Spaghetti diagram

Draw the floor plan; trace every movement of the product (or the operator) with a line. Measure the distance.

```bash
python tools/kaizen.py spaghetti
```

| Movement | Before (m/unit) | After re-layout (m/unit) |
|---|---|---|
| Kitting → ball insert | 18 | 2 |
| Ball insert → preload | 12 | 1.5 |
| Preload → seal | 22 | 1.5 |
| Seal → test | 9 | 1.5 |
| Test → pack | 25 | 2 |
| Fetching parts (average per unit) | 14 | 3 |
| **Total** | **100 m** | **11.5 m** |

At 560 units/day: **56 km/day** of walking and carrying before → **6.4 km/day** after (−89%). The "after" comes from the U-cell layout in Module 8 and point-of-use parts presentation in Module 12.

## 5. Process metrics and takt

| Metric | Definition |
|---|---|
| **Takt time** | Available time ÷ customer demand — the pace the customer requires |
| **Cycle time (C/T)** | Time for one unit to complete a step (observed) |
| Changeover (C/O) | Time from last good part of one product to first good part of the next |
| Uptime | Share of scheduled time the step is able to run |
| Lead time | Time for one unit to pass through the whole process |

Takt = 840 min × 60 / 560 = **90 s**. Any step whose effective cycle time is above 90 s can't keep up — Module 6.

**Time observation tips:** time at least 10 cycles per step with a stopwatch or video; record the lowest repeatable time and note what causes the longer ones.

## Check yourself

A test step is required by the customer's contract. VA, NVA or necessary NVA?

<details><summary>Answer</summary>

Necessary NVA: it doesn't change the product, but it can't be removed today. Aim to reduce it or make it unnecessary (by making the process capable).
</details>
