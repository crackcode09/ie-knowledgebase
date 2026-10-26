# Module 11 — A3 Problem Solving and 5-Why, 1-How

**Time:** 50 min · **Session 3: Analyze, Improve & Control**

## Learning objectives

1. Tell a problem-solving story on one A3 page.
2. Use 5-Why, 1-How to reach a root cause and countermeasure.

## 1. A3

One sheet (A3 paper ≈ 11 × 17 in), read left to right:

| Left | Right |
|---|---|
| 1. Background | 5. Countermeasures |
| 2. Current condition (data, map) | 6. Implementation plan |
| 3. Goal | 7. Results / check |
| 4. Root cause analysis | 8. Follow-up |

**Manifold A3 (outline):** Background — on-time delivery 82%, customers threatening to dual-source. Current condition — CNC effective C/T 4.09 min > takt 4.0; 90-min changeovers; downtime Pareto. Goal — 97% on time in 6 months. Root cause — see 5-Why below. Countermeasures — SMED, TPM, cell, WIP cap, leveled schedule. Plan — who/what/when. Results — tracked weekly.

Template: `templates/a3-template.md`.

## 2. 5-Why, 1-How

| Why? | Answer | Evidence |
|---|---|---|
| Why are orders late? | Work waits at the CNC | VSM: 2.9 days queue before CNC |
| Why does work wait at the CNC? | CNC capacity (215/day) is below demand (220/day) | Effective C/T 4.09 vs takt 4.0 |
| Why is CNC capacity too low? | Uptime is 77% | Downtime log |
| Why is uptime 77%? | 90-min changeovers and tool breakage dominate downtime | Pareto: 53% from tool breakage + changeover overrun |
| Why are changeovers 90 min? | Tools, fixtures and programs are found after the machine stops; fixtures are dialed in by hand | SMED study (Module 15) |

**1-How:** SMED (separate external work, quick-locating fixtures, preset tools) and tool-life management (Module 19).

**Check the logic backwards** with "therefore": manual fixture setup → therefore 90-min changeovers → therefore low uptime → therefore capacity below demand → therefore queues → therefore late orders.

## Check yourself

Why put the root-cause box before countermeasures on the A3?

<details><summary>Answer</summary>

Countermeasures must address verified causes; the layout forces the team (and reviewers) to show the causes first.
</details>
