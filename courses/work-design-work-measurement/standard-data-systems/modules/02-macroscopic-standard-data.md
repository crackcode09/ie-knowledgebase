# Module 02 — Macroscopic Standard Data

## Objectives

- Explain macroscopic standard data and the variables that drive it.
- Use a setup formula and a run formula to set a lot standard.
- Choose the right level of detail for a data system.

## Macroscopic data

**Macroscopic standard data** works at the element, operation or task level: "form one bend", "set up the brake", "weld one inch of fillet". The time units are minutes, and the data is specific to one process, machine type and method.

Macroscopic elements are usually built by **regression on past time studies**. Time is the response, and the job's features are the predictors:

| Element | Typical driving variables |
|---|---|
| Press-brake run | bends, flips, part weight and length |
| Press-brake setup | tool segments changed, new or existing program |
| Shear | cuts, blank weight, sheet size |
| Weld | inches of weld, number of tacks, repositions |
| Pick and pack | lines, items, weight, travel distance |

A good **driving variable** has three properties:

1. It is **known before production**, from the drawing, routing or order.
2. It has a **physical reason** to affect time.
3. It **varies across jobs**. A variable that never changes can't be estimated and isn't needed.

## Harlan's two formulas

Built in Modules 06–08 from `data/brake_run_studies.csv` and `data/brake_setup_studies.csv`:

**Run (normal min/piece)** = 0.1863 + 0.0873 × bends + 0.1184 × flips + 0.0226 × weight_kg + 0.0535 × length_m

**Setup (normal min/lot)** = 6.785 + 2.712 × tool segments + 9.624 × (new program)

**Lot standard (hours)** = (setup + qty × run) × (1 + 0.12) / 60

### Example

A part with 4 bends, 1 flip, 1.2 kg and 400 mm, a 50-piece lot, 3 tool segments and an existing program:

| Step | Value |
|---|---|
| Run | 0.1863 + 0.0873·4 + 0.1184·1 + 0.0226·1.2 + 0.0535·0.4 = **0.702 normal min/piece** |
| Setup | 6.785 + 2.712·3 = **14.92 normal min** |
| Lot | (14.92 + 50 × 0.702) × 1.12 / 60 = **0.934 standard h** |

This took seconds, with no stopwatch and before the part was ever made.

## Choosing the level

| Level | Granularity | Effort to build | Effort to use | Accuracy for one job |
|---|---|---|---|---|
| Motion (micro) | 0.1–3 s | Low per element, high per job | High: every motion listed | Good if the method is described well |
| Element (macro) | 0.05–1 min | Medium | Medium: count elements | Good |
| Operation (macro) | minutes | Medium–high (many studies) | Low: a few variables | Moderate; varies with the family |
| Job / product family | hours | High | Very low: one lookup | Rough, but fine for capacity planning |

The higher the level, the **faster** a standard is to apply and the **narrower** the family it fits. Pick the highest level that still meets your accuracy target (Module 08) for its main use: quoting, planning or incentive pay.

## Run it

```bash
python tools/sdskit.py macro
```

## Check yourself

1. Compute the lot standard for a part with 8 bends, 2 flips, 5.0 kg and 1,200 mm: 30 pieces, 4 tool segments, new program.
2. Why is "operator name" a poor driving variable even if it predicts time well?
3. A planner wants one number per part family ("brackets: 1.1 min"). What do you lose?

<details><summary>Answers</summary>

1. Run = 0.1863 + 0.0873·8 + 0.1184·2 + 0.0226·5 + 0.0535·1.2 = **1.299 min**. Setup = 6.785 + 2.712·4 + 9.624 = **27.26 min**. Lot = (27.26 + 30 × 1.299) × 1.12 / 60 = **1.236 h**.
2. It isn't a feature of the *job*, so it isn't known before production, and the standard should describe the job, not the person. Operator differences belong in performance reporting.
3. You lose accuracy for individual parts. A 2-bend bracket and a 10-bend bracket get the same time. That is fine for rough capacity planning, but poor for quoting and job costing.

</details>
