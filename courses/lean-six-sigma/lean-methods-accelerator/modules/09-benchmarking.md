# Module 9 — Benchmarking

**Time:** 35 min

## Learning objectives

1. Choose the type of benchmarking for a purpose.
2. Quantify performance gaps and use them to set goals.

## 1. Types

| Type | Compare with | Example |
|---|---|---|
| **Internal** | Another site, line or shift in your company | Plant B's CNC changeover is 35 min |
| **Competitive** | Direct competitors | Competitor quotes 5-day delivery |
| **Functional** | Best-in-class in the same function, any industry | Automotive supplier's machining cell, 98.5% FPY |
| **Generic / process** | Any organization with an excellent similar process | E-commerce order-to-ship speed |

Robert Camp's *Benchmarking* (1989), based on Xerox's program, framed benchmarking as learning **practices**, not just copying numbers.

## 2. Process

1. Decide what to benchmark (from COPQ, VSM, customer gaps).
2. Measure your own performance with clear definitions.
3. Find partners and data sources (associations, site visits, published studies, internal sites).
4. Compare: gap = benchmark − current.
5. Understand **how** they achieve it (practices, enablers).
6. Set goals and adapt practices — don't transplant blindly.

## 3. Case — gaps

```bash
python tools/lean.py benchmark
```

| Metric | Us | Benchmark | Gap | Gap % |
|---|---|---|---|---|
| On-time delivery | 82% | 97% | 15 pts | 15% |
| Lead time | 13.4 days | 4.0 days | 9.4 days | 70% |
| First-pass yield | 91.5% | 98.5% | 7 pts | 7% |
| Inventory turns | 6.1 | 14.0 | 7.9 | 56% |
| CNC changeover | 90 min | 20 min | 70 min | 78% |

(Benchmark values are illustrative of what published Lean case studies report; use real partner data in practice.)

**Reading:** the largest relative gaps — changeover, lead time and inventory — are linked: long changeovers force big batches, which create inventory and long lead times. One practice (SMED) moves all three.

## Check yourself

Why is copying a competitor's numbers as goals not enough?

<details><summary>Answer</summary>

Without understanding the practices that produce those numbers, you can set targets but not reach them; benchmarking is about learning how.
</details>
