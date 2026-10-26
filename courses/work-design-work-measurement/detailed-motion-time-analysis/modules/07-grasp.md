# Module 07 — Grasp

## Objectives

- Classify grasps by the control they need.
- Reduce grasp time by presenting parts well.

## Definition

**Grasp** gains enough control of an object with the fingers or hand for the next motion.

## Teaching card (DTC)

| Code | cs | Meaning | High control? |
|---|---|---|---|
| Gc | 0 | Contact: touch, push or slide; no finger closure | no |
| Gp | 3 | Pick-up: easy, isolated object | no |
| Gs | 8 | Small or flat object: precise finger closure | **yes** |
| Gr | 6 | Regrasp: change grip without letting go | no |
| Gt | 6 | Transfer to the other hand | no |
| Gx | 14 | Select from a jumble: search, separate, then grasp | **yes** |

Decision steps:

1. Do the fingers close? **No** → Gc.
2. Is the object mixed with others? **Yes** → Gx.
3. Is it small, thin or flat, needing precise fingers? **Yes** → Gs.
4. Otherwise → Gp.

Regrasp and transfer are coded where they actually happen.

## Presentation decides grasp time

| Presentation | Grasp | Paired reach | Total at 30 cm |
|---|---|---|---|
| Loose in a deep bin with other parts | Gx | R30c | 51 + 14 = **65 cs** |
| One per pocket in a tray | Gp | R30b | 42 + 3 = **45 cs** |
| Fed to a fixed pick point (magazine) | Gp | R30a | 35 + 3 = **38 cs** |

## Check yourself

1. Which grasp applies to picking one sheet of paper from a stack?
2. How much is saved per cycle by moving a part from a mixed bin (R30c Gx) to a fixed pick point (R30a Gp)?

<details><summary>Answers</summary>

1. **Gs**: flat object, precise finger closure.
2. 65 − 38 = **27 cs** (0.27 s) per cycle.

</details>
