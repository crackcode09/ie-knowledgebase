# Module 12 — Simulating a Process Design

**Time:** 3 h · **Phase:** Optimize

## Learning objectives

1. Use discrete-event simulation to stress-test a process design before building it.
2. Compare design alternatives on throughput, WIP and flow time.

## 1. Why simulate?

Formulas (Module 11) handle one station. Real lines have several stations, interacting queues, breakdowns, batching and shift patterns. A **discrete-event simulation** pushes thousands of virtual jobs through the design and records what happens. It's a cheap prototype: you can break it, change it and try "what if" before spending capital.

## 2. A three-station line

`simulate_line()` in `tools/dfss.py` models a serial line: random arrivals (mean every 10 min), single-server stations with unlimited buffers, gamma-distributed service times with a chosen mean and coefficient of variation. It simulates 20,000 jobs and discards the first 10% as warm-up.

| Station | Mean time (min) | cv | Utilization |
|---|---|---|---|
| Cut | 6.0 | 0.5 | 0.60 |
| Drill | 8.0 | 0.5 | 0.80 (bottleneck) |
| Assemble | 7.0 | 0.5 | 0.70 |

## 3. Results — three designs

| Scenario | Throughput (jobs/min) | Mean flow time (min) | 90th percentile flow time | Mean WIP |
|---|---|---|---|---|
| Baseline | 0.099 | **46.2** | 77.7 | 4.6 |
| Drill becomes more variable (cv 1.2) | 0.099 | **74.3** | 143.2 | 7.4 |
| Drill time reduced to 7.0 min | 0.099 | **37.9** | 61.8 | 3.8 |

```bash
python tools/dfss.py sim
```

**Reading it:**

- Throughput is the same in all three: the line has enough capacity, so output equals demand. The differences show up as **waiting, WIP and lead time** — exactly what customers feel.
- More variability at the bottleneck adds 60% to average flow time and nearly doubles the 90th percentile — without changing average capacity.
- Little's law holds: 0.099 × 46.2 ≈ 4.6.

## 4. Good simulation practice

- **Verify** the model (does it do what you intended?) and **validate** it (does it match reality or a similar existing process?).
- Run long enough, discard warm-up, and run multiple replications with different seeds to get confidence intervals.
- Model the things that matter: breakdowns (MTBF/MTTR), setups, batching, shift breaks, rework loops.
- Document assumptions; a simulation is only as good as its input data.

## Exercise 12.1

Modify `ex_sim()` to give the Drill station a 30-minute breakdown every 8 hours on average. What happens to flow time? Then test adding a second drill.

## Check yourself

1. A design change doesn't change throughput in the simulation. Does that mean it doesn't matter?
2. Why look at the 90th percentile, not only the mean?

<details><summary>Answers</summary>

1. No — if the line isn't capacity-limited, the effect appears in WIP and lead time.
2. Customers experience the long waits; percentiles show delivery reliability.
</details>
