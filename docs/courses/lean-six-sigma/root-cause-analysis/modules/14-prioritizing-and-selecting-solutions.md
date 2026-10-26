# Module 14 — Prioritizing and Selecting a Solution

**Time:** 45 min

## Learning objectives

1. Use a weighted decision matrix to select and prioritize solutions.
2. Complement it with an impact/effort view.

## 1. Weighted decision matrix

1. List candidate solutions.
2. Agree criteria **before** scoring, and weight them (e.g., 1–5).
3. Score each solution on each criterion (1–5, higher = better; for cost, higher = cheaper).
4. Weighted total = Σ (weight × score).
5. Discuss the result — the matrix supports a decision; it doesn't make it.

## 2. Worked example — leak countermeasures

| Criterion (weight) | Change tool every 16 h | In-process Ra gauge + auto tool change | Increase clamp torque to 25 N·m | 100% leak retest |
|---|---|---|---|---|
| Effectiveness (5) | 4 | 5 | 2 | 1 |
| Cost (3) | 3 | 2 | 5 | 3 |
| Time to implement (2) | 5 | 3 | 5 | 4 |
| Risk of side effects (3) | 4 | 4 | 2 | 5 |
| Sustainability (4) | 3 | 5 | 3 | 1 |
| **Weighted total** | 63 | **69** | 53 | 41 |

Example: Ra gauge = 5×5 + 3×2 + 2×3 + 3×4 + 4×5 = **69**.

```bash
python tools/rca.py decision
```

**Decision:** implement the tool-change interval **now** (fast, cheap — it scored second and buys time), and the in-process Ra gauge with automatic tool change as the **permanent** solution. Torque increase is a useful supporting action only after checking it doesn't distort the body (risk score 2). 100% retest is containment, not a solution.

## 3. Impact / effort

| | Low effort | High effort |
|---|---|---|
| **High impact** | Do now (tool-change interval) | Plan (in-process gauge) |
| **Low impact** | Do if convenient | Avoid (100% retest as permanent fix) |

## Check yourself

Why agree on criteria and weights before scoring?

<details><summary>Answer</summary>

Otherwise people adjust weights to favor the solution they already prefer.
</details>
