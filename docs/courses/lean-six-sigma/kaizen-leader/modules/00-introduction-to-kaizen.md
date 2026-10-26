# Module 0 — Introduction: Kaizen, the Lean Blueprint, the 3 Ms and 8 Wastes

**Time:** 90 min

## Learning objectives

1. Explain what a kaizen event is and when it's the right tool.
2. Describe the structure of a kaizen: pre-work, event week, follow-up.
3. Identify the 3 Ms and the 8 wastes in a process.

## 1. What is kaizen?

*Kaizen* (Japanese: "change for the better") means continuous, incremental improvement by the people who do the work. Masaaki Imai's *Kaizen* (1986) brought the term to Western audiences.

A **kaizen event** (also "kaizen blitz" or "rapid improvement event") is a focused, time-boxed burst of improvement: a cross-functional team spends 3–5 days on one process, analyzing it, changing it, and standardizing the result.

| Use a kaizen event when | Use a longer project (e.g., DMAIC) when |
|---|---|
| Scope is one area or value stream segment | The problem spans many processes or sites |
| The cause is likely visible at the gemba (waste, layout, flow, changeover) | The cause is hidden in data and needs weeks of analysis |
| The team can implement most changes during the week | Solutions need capital, IT changes or long tests |
| Leadership can free the team full time for the week | — |

## 2. The kaizen schedule

| Phase | Timing | Key outputs |
|---|---|---|
| **Pre-work** | 3–6 weeks before | Scope, charter, SIPOC, baseline data, team, logistics (Modules 2–3) |
| **Day 1** | Understand the current state | Gemba walk, process maps, spaghetti diagram, VSM, takt, constraint (Modules 4–6) |
| **Day 2** | Root causes and solutions | Fishbone, 5-Why, data, brainstorming (Module 7) |
| **Days 3–4** | Implement | Flow, balance, pull, quick changeover, error-proofing, try-storming and pilots (Modules 8–11) |
| **Day 5** | Standardize and report out | 5S, visual management, standard work, control plan, report-out (Modules 12–13) |
| **Follow-up** | 30/60/90 days | Open actions closed, results sustained (Module 13) |

## 3. The Lean blueprint

The "house" model of the Toyota Production System is a common way to show how Lean fits together:

```
                 ┌────────────────────────────────────────┐
                 │  Goal: highest quality, lowest cost,   │
                 │  shortest lead time, safety, morale    │
                 ├───────────────────┬────────────────────┤
                 │  Just-in-time     │  Jidoka            │
                 │  takt, flow, pull │  stop on problems, │
                 │                   │  error-proofing    │
                 ├───────────────────┴────────────────────┤
                 │  Standard work · Kaizen                │
                 ├────────────────────────────────────────┤
                 │  Stability: 5S, TPM, visual management,│
                 │  heijunka (level loading)              │
                 └────────────────────────────────────────┘
```

Build the foundation (stability) before the pillars: you can't pull or flow through an unreliable machine.

## 4. The 3 Ms

| Term | Meaning | Example |
|---|---|---|
| **Muda** | Waste — activity that adds no value | Walking to fetch parts |
| **Mura** | Unevenness — fluctuation in demand or workload | 800 units Monday, 300 Friday |
| **Muri** | Overburden — unreasonable load on people or machines | Running a machine at 100% with no maintenance time |

Mura causes muri, and muri causes muda (breakdowns, defects). Attacking only muda misses the cause.

## 5. The 8 wastes (DOWNTIME)

| Waste | Example in an assembly cell |
|---|---|
| **D**efects | Carriages failing friction test |
| **O**verproduction | Packing ahead of orders — 1,100 units in finished goods |
| **W**aiting | Operator idle while preload fixture is changed |
| **N**on-utilized talent | Operators' ideas never asked for |
| **T**ransportation | Moving trays between rooms |
| **I**nventory | 5,170 units of WIP for a 560/day demand |
| **M**otion | Walking 100 m per unit, reaching, searching |
| **E**xtra-processing | Re-testing parts that already passed; double paperwork |

Taiichi Ohno described seven wastes; "non-utilized talent" was added later in Western Lean practice. Overproduction is often called the worst, because it hides all the others.

## 6. Running case

A kaizen event on the **carriage assembly and pack cell** for linear guides: demand 560 per day, output around 465, lead time over 9 days. All numbers in this course come from `python tools/kaizen.py all`.

## Check yourself

1. Classify: (a) an operator searches for a torque wrench; (b) monthly orders arrive in the last week; (c) a press runs over rated tonnage to meet output.
2. Why is overproduction considered the worst waste?

<details><summary>Answers</summary>

1. (a) Muda (motion). (b) Mura. (c) Muri.
2. It creates inventory, which hides defects, waiting and imbalance, and consumes material and capacity for things nobody ordered yet.
</details>
