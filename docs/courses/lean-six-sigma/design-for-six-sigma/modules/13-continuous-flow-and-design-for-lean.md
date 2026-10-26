# Module 13 — Continuous Flow and Design for Lean

**Time:** 3 h · **Phase:** Optimize

## Learning objectives

1. Compute takt time and the minimum number of stations.
2. Balance a line with precedence constraints.
3. Apply Lean principles to a new process design.

## 1. Takt time

  **Takt = available working time / customer demand**

450 min available per shift, demand 400 units per shift → takt = **1.125 min** (67.5 s). Every station must complete its work within takt for the line to keep pace with demand.

## 2. Line balancing

Total work content / takt = theoretical minimum number of stations (round up).

### Worked example — carriage assembly

| Task | Time (min) | Must follow |
|---|---|---|
| A Load rail block | 0.6 | — |
| B Insert balls | 0.9 | A |
| C Fit retainer | 0.4 | A |
| D Set preload | 1.1 | B |
| E Fit end seals | 0.5 | C |
| F Lubricate | 0.8 | D, E |
| G Friction test | 0.7 | F |
| H Pack | 0.3 | G |
| **Total** | **5.3** | |

Theoretical minimum: 5.3 / 1.125 = 4.7 → **5 stations**.

Largest-candidate rule (assign the longest eligible task that fits within takt):

| Station | Tasks | Load (min) |
|---|---|---|
| 1 | A, C | 1.0 |
| 2 | B | 0.9 |
| 3 | D | 1.1 |
| 4 | E | 0.5 |
| 5 | F | 0.8 |
| 6 | G, H | 1.0 |

```bash
python tools/dfss.py balance
```

**6 stations, balance efficiency = 5.3 / (6 × 1.125) = 78.5%.**

Why not 5? B (0.9) and D (1.1) are each too long to share a station with anything, and E (0.5) can't join any neighbor without exceeding takt — so 6 is the best possible with these task times. The theoretical minimum ignores precedence and task size.

**Design options:** split D (preload set is at 98% of takt — no room for variation); combine E into a redesigned C ("fit retainer with integral seal" — the DFA change from Module 7); or move some of F into station 4. Redesigning the product often balances the line better than rearranging tasks.

## 3. Design for Lean

| Principle | Design implication |
|---|---|
| Flow | Cells in process sequence; one-piece flow where possible; minimal transport |
| Pull | Kanban-sized buffers; produce to takt, not to forecast |
| Reduce variability | Standard work (Module 14), quick changeover (SMED) built into fixtures |
| Right-sized equipment | Several small machines instead of one large shared one (avoids batching and queues — Module 11) |
| Visual management | Andon, clear WIP limits, visible status |
| Built-in quality | Error-proofing at each station (Module 7) |

## Check yourself

1. Demand rises to 450 per shift. New takt? Does station 3 still work?
2. Why is a station loaded at 98% of takt a risk?

<details><summary>Answers</summary>

1. Takt = 1.0 min. Station 3 (D = 1.1 min) now exceeds takt — D must be split or sped up.
2. Any variation in task time causes the station to miss takt and starve the next station; there's no recovery margin.
</details>
