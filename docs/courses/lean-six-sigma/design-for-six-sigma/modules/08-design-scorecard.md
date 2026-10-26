# Module 8 — The Design Scorecard and Rolled Throughput Yield

**Time:** 2 h · **Phase:** Design

## Learning objectives

1. Build a design scorecard that predicts quality before production.
2. Compute rolled throughput yield (RTY) from step-level DPMO.

## 1. What a scorecard is

A design scorecard tracks predicted performance of every CTQ and every process step against targets, updated as the design matures. It answers: *if we launched today, what quality would we get, and where would the defects come from?*

Typical sections:

| Scorecard | Contents |
|---|---|
| Performance | Each CTQ: target, limits, predicted μ and σ, Cpk, DPMO |
| Process | Each step: opportunities per unit, DPMO, yield |
| Parts / suppliers | Incoming quality of each purchased part |
| Software / documentation (if relevant) | Defect predictions |

## 2. Rolled throughput yield

First-time yield of a step, assuming defects occur randomly (Poisson):

  Y = e^(−DPU), DPU = opportunities × DPMO / 10⁶

**RTY** = product of step yields = probability a unit passes **every** step with no defects or rework.

### Worked example — linear guide production

| Step | Opportunities | DPMO | DPU | Yield |
|---|---|---|---|---|
| Machine rail | 12 | 300 | 0.0036 | 0.9964 |
| Grind raceway | 4 | 1,500 | 0.0060 | 0.9940 |
| Assemble carriage | 20 | 150 | 0.0030 | 0.9970 |
| Lubricate & seal | 6 | 800 | 0.0048 | 0.9952 |
| Final inspect & pack | 8 | 100 | 0.0008 | 0.9992 |
| **Total** | | | **0.0182** | **RTY = 0.982** |

```bash
python tools/dfss.py scorecard
```

About 1.8% of units will need some rework or scrap somewhere. The biggest contributors are **grinding** (highest DPMO) and **lubricate & seal**. Those are where design and process effort should go — and they match the FMEA priorities.

## 3. Why RTY, not final yield?

Final yield counts what ships good after rework. RTY exposes the **hidden factory** — the rework loops, re-tests and scrap that final yield hides. In design, RTY is the right target because it drives cost and lead time.

## Check yourself

1. A 10-step process with 99% first-time yield per step. RTY?
2. Why does adding steps to a design hurt RTY even if each step is good?

<details><summary>Answers</summary>

1. 0.99¹⁰ ≈ 0.904.
2. Yields multiply; every added step adds defect opportunities.
</details>
