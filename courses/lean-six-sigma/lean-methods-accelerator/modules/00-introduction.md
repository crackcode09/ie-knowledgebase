# Module 0 — Introduction to Lean and Lean Six Sigma

**Time:** 30 min · **Session 1: Introduction to Lean Methods**

## Learning objectives

1. Describe Lean, Six Sigma and how they combine.
2. Use basic Lean terminology.
3. Navigate this course and its running case.

## 1. Lean and Six Sigma

| | Lean | Six Sigma |
|---|---|---|
| Roots | Toyota Production System (Ohno, Shingo, 1950s–70s); "lean" coined by Krafcik (1988) and popularized by Womack, Jones & Roos, *The Machine That Changed the World* (1990) | Motorola (1980s), GE (1990s) |
| Focus | Flow, speed, waste | Variation, defects |
| Core question | Where does time and effort go that the customer doesn't value? | What causes variation in the output? |
| Typical tools | VSM, takt, flow, pull, SMED, 5S, standard work | DMAIC, statistics, DOE, SPC |

They fit together: waste and slow flow hide defects; variation destroys flow. **Lean Six Sigma** uses both, usually inside the DMAIC structure (Module 2).

## 2. Five Lean principles

Womack and Jones (*Lean Thinking*, 1996):

1. **Value** — defined by the customer.
2. **Value stream** — all the steps that deliver it; remove those that don't add value.
3. **Flow** — make the remaining steps flow without interruption.
4. **Pull** — produce only what the downstream customer needs, when needed.
5. **Perfection** — improve continuously.

## 3. Course map

| Session | Modules |
|---|---|
| **1. Introduction** | 0 Lean & LSS · 1 Cost of poor quality · 2 Lean blueprint, Y = f(X), DMAIC, thought process maps |
| **2. Define & Measure** | 3 Value, gemba, wastes · 4 Process maps, VA flow charts, spaghetti · 5 Process metrics & takt · 6 Value stream mapping · 7 Line balancing & heijunka · 8 Data types & Pareto · 9 Benchmarking · 10 Kaizen |
| **3. Analyze, Improve, Control** | 11 A3 & 5-Why · 12 DFSS & design for Lean (supply chain dynamics) · 13 Error-proofing · 14 Continuous flow & cells · 15 Quick changeover · 16 Theory of constraints · 17 Pull systems · 18 Visual management & 5S · 19 TPM · 20 Standard work & leader standard work · 21 The Lean journey & capstone |

## 4. Running case

A **hydraulic-manifold plant**: blanks are sawn, machined on two CNC machining centers, deburred, washed, leak-tested, assembled and packed. Three product families go to equipment builders, mostly through distributors. Demand is 220 manifolds/day; on-time delivery is 82%; lead time is almost 13 days. All numbers come from `python tools/lean.py all`.

This course is self-contained. Related in-depth courses in this repository: *Process Mapping*, *Kaizen Leader*, *Root Cause Analysis*, *Measurement & Basic Statistics*, *Design for Six Sigma*.

## Check yourself

Which Lean principle does a large finished-goods warehouse built to forecast most obviously violate?

<details><summary>Answer</summary>

Pull (and flow): production is pushed to a forecast rather than triggered by customer demand.
</details>
