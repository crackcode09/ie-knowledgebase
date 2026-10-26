# Module 14 — Verify: Control Plans, Piloting and Standardized Work

**Time:** 2 h · **Phase:** Verify

## Learning objectives

1. Write a process control plan.
2. Plan and evaluate a pilot.
3. Create standardized work for a new process.

## 1. Process control plan

A control plan documents how each critical characteristic will be controlled in production. Typical columns (automotive practice uses a defined format; the idea is universal):

| Process step | Characteristic | Spec | Measurement method | Sample size / frequency | Control method | Reaction plan |
|---|---|---|---|---|---|---|
| Set preload | Friction force | ≤ 15 N | Test rig TR-2 | 100% | Automatic reject + XmR chart of hourly average | Stop, check ball size lot, notify engineering |
| Grind raceway | Raceway width | 8.000 ± 0.010 | Air gauge | 5 per 2 h | X̄–R chart | Re-dress wheel, quarantine since last good subgroup |
| Fit end seals | Seal present | Present | Vision sensor | 100% | Error-proofing (Module 7) | Line stops automatically |
| Lubricate | Grease type | Grade X | Unique cartridge connector | Each change | Error-proofing | — |

Sources: QFD and scorecard (which CTQs), FMEA (which risks), DOE (which inputs drive outputs).

## 2. Piloting

A pilot is a small-scale, real-conditions trial — real operators, materials, equipment and customers — before full launch.

**Plan:** objectives and success criteria (from the scorecard), duration and volume, data to collect, roles, rollback plan.

**Evaluate:**

- Did CTQs hit predicted means and capability? (Charts + Cpk with honest caveats about the short run.)
- Did the scorecard's predicted RTY match actual first-pass yield?
- Which failure modes appeared that the FMEA missed? Update the FMEA.
- Compare pilot to baseline (if replacing an old design) with the appropriate hypothesis test — see *Fundamentals of Hypothesis Testing*.

## 3. Standardized work

The current best way to do a job, documented and followed, so results are repeatable and improvement has a baseline. Three elements (Toyota Production System):

1. **Takt time** (Module 13).
2. **Work sequence** — steps in order, with key points (quality, safety, technique) and reasons.
3. **Standard WIP** — the minimum in-process stock needed to work smoothly.

Good standard work is visual (photos, not paragraphs), written with operators, and revised whenever the process improves.

## Check yourself

1. Where should the list of characteristics in a control plan come from?
2. A pilot hits every CTQ but first-pass yield is 90% vs 98% predicted. What next?

<details><summary>Answers</summary>

1. The CTQs (QFD/scorecard), high-risk failure modes (FMEA), and critical inputs found in DOE.
2. Pareto the pilot defects, find the steps the scorecard underestimated, update the FMEA and fix before launch.
</details>
