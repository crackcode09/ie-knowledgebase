# Module 0 — Introduction and Building an Effective Data Collection System

**Time:** 75 min · **Day 1**

## Learning objectives

1. Explain what statistics can and can't do for business and process decisions.
2. Design a data collection system that delivers useful, trustworthy data.

## 1. Why statistics?

Every process varies. Statistics lets you **describe** that variation (Modules 1), **model** it with probability distributions to forecast performance (Modules 2–4), **infer** from samples to the whole process with stated confidence and risk (Modules 5–7), and **predict** outcomes from the factors that drive them (Modules 8–10).

## 2. Running case

A **contract electronics assembler** builds printed circuit board assemblies. Its data: reflow oven cycle times, solder-joint defects per board, rework repair times, time between pick-and-place machine failures, solder-paste thickness from two printers, and 30 months of business data (orders, quoting speed, on-time delivery, marketing spend, revenue). All datasets are synthetic and regenerate with `python tools/statkit.py data`.

## 3. A data collection system that delivers insight

Most analysis problems start with poor data. Design collection **before** you collect.

| Step | Question | PCB example |
|---|---|---|
| 1. Purpose | Which decision or question will the data answer? | "Is printer P2 more variable than P1?" |
| 2. What to measure | Which characteristic, in which units, with what resolution? | Paste thickness in µm, 0.1 µm resolution |
| 3. Operational definition | Exactly how and where? | Laser height at 5 fixed pads per board, average reported |
| 4. Stratification | What context to record? | Printer, stencil, paste lot, shift, time |
| 5. Sampling plan | How many, how often, how selected? | 25 boards per printer, every 30 min, consecutive boards |
| 6. Measurement system | Is the gauge good enough? | Repeatability study on the laser gauge |
| 7. Recording | Form or system, who, when? | Auto-logged from the inspection machine |
| 8. Analysis plan | Which chart or test? | Variance test (Module 6) |

### Data types

| | Discrete (attribute) | Continuous (variable) |
|---|---|---|
| Examples | Defects per board; pass/fail; machine ID | Cycle time; thickness; repair minutes |
| Distributions | Binomial, Poisson, hypergeometric | Normal, exponential, lognormal |
| Information per point | Low — need larger samples | High |

**Prefer continuous measurements.** Recording "paste OK / not OK" throws away the information needed to see a drift before it causes defects.

### Sampling

| Method | Use when |
|---|---|
| Simple random | Every unit equally likely; e.g., auditing a lot |
| Systematic (every kth) | Production in time order; beware cycles that match k |
| Stratified | Known groups (printers, shifts) — sample each |
| Rational subgroups | Process monitoring: small samples of consecutive units at intervals |

## Check yourself

Why record printer ID with every paste measurement?

<details><summary>Answer</summary>

So the data can be stratified by printer; without it you can't tell whether variation comes from one printer, and later analysis (Module 6) is impossible.
</details>
