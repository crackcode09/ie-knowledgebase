# Module 2 — Operational Definitions, CTQs and QFD

**Time:** 2 h · **Phase:** Define

## Learning objectives

1. Translate customer needs into measurable CTQs with operational definitions.
2. Build a House of Quality (QFD) to prioritize technical requirements.

## 1. From need to CTQ

A customer need is in the customer's words ("slides smoothly"). A **CTQ** is a measurable characteristic with a target and limits. A CTQ tree breaks a need down:

```
Need: Slides smoothly
 ├── Driver: low resistance to motion  → CTQ: Friction force ≤ 15 N
 └── Driver: no stick-slip at low speed → CTQ: Force variation ≤ 2 N p-p at 10 mm/s
```

Each CTQ needs an **operational definition** — a measurement method precise enough that two labs get the same answer:

> **Friction force:** force to move the unloaded carriage at a constant 100 mm/s over 200 mm of a 1 m rail, measured with the load cell on test rig TR-2 after 5 warm-up strokes, 23 ± 2 °C, average of 3 strokes, reported in N.

## 2. Quality Function Deployment (House of Quality)

QFD, developed in Japan by Yoji Akao and others in the late 1960s–70s, links customer needs (rows) to technical requirements (columns).

1. List needs (from the affinity diagram) and their **importance** (1–5, from the survey).
2. List measurable **technical requirements** (CTQ candidates).
3. Rate each relationship: **9 strong, 3 medium, 1 weak**, blank none.
4. Technical importance = Σ (need importance × relationship).
5. Optionally add the "roof" (correlations between technical requirements — e.g., lower friction vs higher stiffness conflict), competitor benchmarks, and target values.

### Worked example — linear guide carriage

| Need (importance) | Friction | Stiffness | Lube interval | Noise | Unit cost |
|---|---|---|---|---|---|
| Slides smoothly (5) | 9 | 1 | 3 | 3 | |
| Holds position under load (4) | 1 | 9 | | | 1 |
| Low maintenance (3) | 3 | | 9 | 1 | |
| Quiet (2) | 3 | 1 | 1 | 9 | |
| Affordable (4) | 1 | 3 | 3 | 1 | 9 |
| **Technical importance** | **68** | 55 | 56 | 40 | 40 |
| **Share** | **26.3%** | 21.2% | 21.6% | 15.4% | 15.4% |

Friction: 5×9 + 4×1 + 3×3 + 2×3 + 4×1 = 68.

```bash
python tools/dfss.py qfd
```

**Reading it:** friction force is the most important technical requirement; stiffness and lube interval follow closely. These become the primary CTQs for the design scorecard (Module 8). The roof would show friction and stiffness pull against each other (more preload = stiffer but more friction) — a trade-off to optimize in Module 9.

## 3. QFD pitfalls

- Too many rows and columns (keep it to the vital needs; cascade to further "houses" for parts and processes).
- Using 9-3-1 everywhere — be honest about weak relationships.
- Treating the output as precise: it's a structured team judgment.

## Check yourself

1. Is "easy to install" a CTQ?
2. What does a technical requirement with no strong relationship to any need suggest?

<details><summary>Answers</summary>

1. No — it's a need. A CTQ would be e.g. "installation time ≤ 10 min by a trained fitter using standard tools."
2. Either it doesn't matter to customers (consider dropping it) or a need is missing from the list.
</details>
