# Module 2 — Market Segmentation and Choosing Target Markets

**Time:** 45 min · **Data:** `data/survey.csv`

## Learning objectives

1. Segment customers by needs and characteristics.
2. Use research results to pick target markets.

## 1. Why segment?

Customers differ. Averaging everyone produces a design that fits nobody. A segment is a group whose needs are similar enough to serve with one offer and different enough from other groups to matter.

**Common bases:** industry/application, size, geography, buying behavior (who decides, how they order), and — most useful for design — **needs**.

**Good segments are:** measurable, large enough to matter, reachable, and respond differently.

## 2. Case — needs by segment

Mean importance (1–5) from the survey:

```bash
python tools/voc.py segments
```

| Need | MRO plants (n = 150) | Distributors (n = 90) | OEMs (n = 60) |
|---|---|---|---|
| Fast delivery | **4.63** | 4.16 | 3.55 |
| Right part first time | 4.54 | **4.57** | 4.25 |
| Order status visibility | 4.09 | **4.42** | 3.50 |
| Easy part identification | **4.25** | 3.56 | 3.20 |
| Price | 3.31 | **4.51** | **4.47** |
| Technical support | 3.45 | 2.87 | **4.23** |

Three different customers: **MRO plants** have a machine down and need the right part fast, and struggle to identify it; **distributors** are price- and visibility-driven resellers; **OEMs** plan ahead, care about price and engineering support.

## 3. Choosing target markets

Score each segment on agreed criteria (weights 1–3, scores 1–5) using market data and the survey:

| Criterion (weight) | MRO plants | Distributors | OEMs |
|---|---|---|---|
| Size (3) | 5 | 4 | 2 |
| Growth (2) | 3 | 2 | 4 |
| Fit with our strengths (3) | 3 | 4 | 4 |
| Margin (2) | 4 | 2 | 3 |
| Unmet need — gap we can close (3) | 5 | 3 | 2 |
| **Weighted total** | **53** | 41 | 38 |

**Decision:** design the new ordering service around **MRO plants** first (largest, best margin, biggest unmet need), while making sure distributors' must-haves (status visibility, right part) are met. OEMs are served by the existing engineering-led channel.

## Check yourself

Why segment by needs rather than only by company size?

<details><summary>Answer</summary>

Two companies of the same size can need very different things (e.g., a plant with a machine down vs a distributor restocking); needs-based segments point directly to design choices.
</details>
