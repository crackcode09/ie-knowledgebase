# Module 00: Why Designed Experiments

## Objectives

By the end of this module you can:

- explain why changing one factor at a time (OFAT) misses interactions and wastes runs;
- name the three principles of a sound experiment: randomization, replication and blocking;
- write a one-page experiment plan before a single part is molded.

## The running case

Every module uses one fictional process: **injection molding of a glass-filled nylon bearing cage**. The plant sees four kinds of problems, and each one becomes an experiment:

| Problem | Response (y) | Module |
|---|---|---|
| Strength varies by resin lot | tensile strength, MPa | 01 |
| Parts stick in the mold | ejection force, N | 02 |
| Cycle time is too long | cycle time, s | 03 |
| Parts shrink out of tolerance | shrinkage, % | 04-06 |
| Parts warp | warpage, µm | 07, 09 |
| Flash on the parting line | flash defects per 1000 | 08 |

All data is simulated with a fixed seed (`python tools/doekit.py data`), so your numbers match the text exactly.

## Vocabulary

- **Factor**: an input you deliberately change (melt temperature, hold pressure).
- **Level**: a setting of a factor (270 °C and 290 °C).
- **Treatment**: one combination of levels (270 °C with 60 MPa).
- **Response**: the output you measure (warpage).
- **Experimental unit**: the thing a treatment is applied to (one shot, one cage).
- **Run**: one trial at one treatment.
- **Effect**: how much the average response changes when a factor moves from its low level to its high level.
- **Interaction**: the effect of one factor depends on the level of another.

## Why not one factor at a time?

Suppose an engineer tunes warpage by OFAT. She holds everything at a baseline, varies hold pressure, keeps the best value, then varies mold temperature. Two things go wrong:

1. **Interactions are invisible.** In Module 07 we find that raising hold pressure cuts warpage by about 36 µm when the mold is cool but only about 7 µm when it is hot. OFAT measures one of those numbers and reports it as "the" effect.
2. **Runs buy less information.** In a 2^4 factorial, all 16 runs help estimate *every* main effect: each effect is a comparison of 8 runs against 8 runs. With OFAT, each comparison uses only the few runs where that one factor moved.

## The three principles

**Randomization.** Run treatments in a random order. Drift you did not plan for (tool wear, resin moisture, operator fatigue) then spreads evenly across treatments instead of piling onto one. Randomization is what lets you say the factor *caused* the difference.

**Replication.** Repeat each treatment on independent experimental units. Replicates give you an estimate of pure error, and the error estimate is what every F-test and confidence interval divides by. Measuring the same part twice is *not* replication; that is repeated measurement.

**Blocking.** When a known nuisance source (mold cavity, shift, raw-material lot) cannot be held constant, make it a block: run every treatment inside every block and remove the block-to-block variation in the analysis. Module 02 shows blocking turning a "no effect" result into a clear one.

Rule of thumb: **block what you can, randomize what you cannot.**

## A planning checklist

Before running anything, write down:

1. **Objective.** Screening (which factors matter?), characterization (how big are the effects and interactions?) or optimization (what settings are best?).
2. **Response and measurement.** How is y measured, and is the gauge capable? Run an MSA first if you are unsure.
3. **Factors and levels.** Levels far enough apart to show an effect, but still safe and producible.
4. **Nuisance factors.** Which to hold constant, which to block, which to leave to randomization.
5. **Design and run count.** Choose the design, then check replicates and power (Module 06).
6. **Run sheet.** Randomized order, data columns, and a notes column for anything odd.
7. **Analysis plan.** Write the model you will fit *before* you see data.

A fill-in version of this checklist is in `templates/experiment-plan.md`.

## Check yourself

1. An engineer measures each molded cage three times on a CMM and calls this "three replicates". What is wrong?
2. Why does randomizing run order protect against tool wear?
3. Your molds differ a lot and only four cages fit in a shift. What principle applies?

<details><summary>Answers</summary>

1. Those are repeated measurements of one experimental unit. They estimate gauge variation, not part-to-part variation. Real replicates are separate shots or cages made under the same treatment.
2. Wear drifts with time. Under a random order, early and late runs mix across treatments, so wear adds noise but does not bias any one treatment.
3. Blocking. Make mold (or shift) a block, run every treatment within it, and remove its variation in the ANOVA (Module 02).

</details>
