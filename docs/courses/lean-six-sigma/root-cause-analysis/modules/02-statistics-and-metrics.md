# Module 2 — Solving Problems with Statistics: Measurement and Metrics

**Time:** 30 min

## Learning objectives

1. Choose metrics that show the size and behavior of a problem.
2. Check that the data can be trusted before analyzing them.

## 1. Practical → statistical → practical

1. **Practical problem:** valves leak.
2. **Statistical problem:** which inputs (Xs) explain variation in leak rate (Y)?
3. **Statistical solution:** seat roughness explains most of it; roughness rises with tool hours.
4. **Practical solution:** control tool life and monitor roughness.

## 2. Metrics for RCA

| Purpose | Metric | Example |
|---|---|---|
| Size of the problem | Rate or count per period, cost | Leak rejects per week; $ per week |
| Behavior over time | Run chart / process behavior chart | Is the reject rate stable or did something change? |
| Output (Y) | Continuous if possible | Leak rate in cc/min, not just pass/fail |
| Inputs (Xs) | Measured with each unit | Seat Ra, clamp torque, machine, tool hours, ambient temperature |

**Record the Xs with the Y.** Without the machine, tool hours and torque on each record, the statistical modules (8–12) are impossible.

## 3. Trust the data first

- **Operational definition** of the defect and the measurement.
- **Measurement system:** is the leak tester repeatable? A gauge study on the tester comes before blaming the process. (See *Measurement & Basic Statistics*.)
- **Completeness:** are rejects from all shifts and machines recorded the same way?

## Check yourself

Why prefer leak rate (cc/min) over pass/fail for root cause work?

<details><summary>Answer</summary>

Continuous data show how close each part is to failing and need far fewer samples to detect relationships with inputs.
</details>
