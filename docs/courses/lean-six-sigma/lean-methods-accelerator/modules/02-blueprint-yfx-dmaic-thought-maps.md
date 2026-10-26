# Module 2 — The Lean Blueprint, Input Determines Output, DMAIC and Thought Process Maps

**Time:** 60 min

## Learning objectives

1. Explain the Lean "house" and why stability comes first.
2. Use Y = f(X) to focus on the inputs that drive results.
3. Describe the DMAIC phases and where Lean tools fit.
4. Plan a project's reasoning with a thought process map.

## 1. The Lean blueprint

```
          ┌─────────────────────────────────────────────────┐
          │ Customer: best quality, lowest cost, shortest   │
          │ lead time, safety, engaged people               │
          ├─────────────────────────┬───────────────────────┤
          │ JUST-IN-TIME            │ JIDOKA (built-in      │
          │ takt · flow · pull      │ quality): stop on     │
          │ quick changeover        │ abnormality, error-   │
          │                         │ proofing, andon       │
          ├─────────────────────────┴───────────────────────┤
          │ STANDARD WORK · KAIZEN · PEOPLE                 │
          ├─────────────────────────────────────────────────┤
          │ STABILITY: 5S · TPM · visual management ·       │
          │ heijunka (level loading) · capable processes    │
          └─────────────────────────────────────────────────┘
```

You can't flow or pull through machines that break down, processes that make defects, or a schedule that swings wildly. Build the foundation first.

## 2. Input determines output: Y = f(X)

The results the customer sees (Y: on-time delivery, defects, lead time) are produced by process inputs (X: machine uptime, changeover time, batch sizes, release rules, training). You can't manage Ys directly — only through the Xs.

| Y (result) | Xs that drive it in the manifold plant |
|---|---|
| On-time delivery 82% | CNC uptime (77%), changeover time (90 min), release of work ahead of the constraint, schedule swings |
| Lead time 12.7 days | Inventory between steps, batch sizes, waiting for the constraint |
| First-pass yield 91.5% | Tool wear, coolant concentration, deburr method |

## 3. DMAIC and Lean tools

| Phase | Purpose | Lean tools used here | Module |
|---|---|---|---|
| **Define** | Problem, customer, scope | Charter, SIPOC, COPQ, benchmarking | 1, 9 |
| **Measure** | Current performance | Gemba, process maps, VSM, takt, metrics, Pareto | 3–8 |
| **Analyze** | Root causes | 5-Why, TOC, A3, waste analysis | 11, 16 |
| **Improve** | Implement solutions | Flow, cells, SMED, pull, error-proofing, kaizen | 10, 13–15, 17 |
| **Control** | Sustain | 5S, visual management, TPM, standard work, leader standard work | 18–20 |

## 4. Thought process maps

A thought process map lays out the **questions** a project must answer and the tools and data that will answer them — before collecting data. It keeps a team from jumping to tools or solutions.

```
Goal: on-time delivery 82% → 97%
 ├─ Q: Where are orders late?            → Tool: VSM, lead-time data by step     → Answer: waiting before CNC
 │   └─ Q: Why does work wait at CNC?    → Tool: takt vs effective C/T (TOC)     → CNC 4.09 min > takt 4.0
 │        ├─ Q: What eats CNC time?      → Tool: downtime Pareto                 → tool breakage, changeovers
 │        └─ Q: How long are changeovers?→ Tool: SMED study                      → 90 min
 └─ Q: Does releasing more work help?    → Tool: CONWIP analysis                 → no — more WIP, same output
```

Update the map as answers come in; it becomes the project's storyline for reviews.

## Check yourself

A manager wants to set a target for "on-time delivery" and post it on the wall. What's missing from the Y = f(X) view?

<details><summary>Answer</summary>

Knowing and managing the Xs that drive on-time delivery; a target on Y alone tells people what, not how.
</details>
