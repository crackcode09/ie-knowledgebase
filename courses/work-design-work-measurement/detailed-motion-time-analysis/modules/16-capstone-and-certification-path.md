# Module 16 — Capstone and Certification Path

## Capstone: connector assembly

A connector has a housing, two pins and a snap-on cover.

**Current method:**

- housings from a bin and pins from a mixed bin
- the left hand holds the housing while the right hand inserts each pin (close, non-symmetric fit)
- a flat cover is picked from a stack and snapped on
- a visual check, then the assembly is put aside to a tote

**Tasks:**

1. Write the two-handed chart and code it with the teaching card.
2. Total it, and compute the standard (12 %) and the output per hour.
3. Redesign the method (fixture, presentation, part design) and analyse the new method.
4. Report the saving and the design changes needed. Who must approve them (design engineering, quality)?

<details><summary>Capstone key (run <code>python tools/dmtkit.py lab C01_current</code> and <code>... C01_improved</code>)</summary>

**Current: 586.0 cs = 5.86 s** normal, 6.56 s standard, **≈ 549 per hour**.

- The left hand only holds through most of the cycle.
- Each pin costs R35c Gx + M30c PCN RL = 71.5 + 78 = 149.5 cs.

**Improved: 320.5 cs = 3.21 s** normal, 3.59 s standard, **≈ 1,003 per hour** (−45 %).

| Change | Effect |
|---|---|
| Fixture holds the housing | Frees the left hand to insert the second pin |
| Pins on an oriented strip feeder at a fixed point | R20a Gp instead of R35c Gx |
| Chamfered, symmetric pins | PCS instead of PCN |
| Hands alternate | One hand gets while the other inserts, so the high-control positions never coincide |
| Cover magazine and guided nest | R20a Gp and PLS instead of R30b Gs and PLM |
| Push-off into a chute | Gc, RLc |

The pin design change (chamfer, symmetry) needs design-engineering and quality approval.

</details>

## Final skill check

1. What two variables (besides the motion itself) drive reach and move times?
2. Which grasp applies to picking one washer out of a mixed bin?
3. What are the fit and symmetry classes for a position on the teaching card?
4. When can both hands work at the same time under the course rule?
5. Why should process time not be coded as hand motions?
6. What is the difference between allowance conventions A and B?
7. Name three changes that convert a high-control motion into a low-control one.
8. What do you need before setting real MTM-1 standards?

<details><summary>Answers</summary>

1. Distance and case (control needed at the destination). For moves, weight as well.
2. **Gx** (select from a jumble).
3. Fit: loose, close, tight. Symmetry: symmetric, semi-symmetric, non-symmetric. Plus a difficult-handling allowance.
4. Unless both hands have a high-control motion in the same step.
5. It comes from the equipment, isn't paced by the operator, and may be treated differently for allowances.
6. A: allowance on manual time only, process time added unadjusted. B: allowance on the total. State which one you use.
7. Any three: oriented, isolated part presentation; fixed pick points; chamfers and lead-ins; symmetric part design; fixtures and guides; larger targets.
8. Licensed training, the official data card and application rules, and certification through an MTM association (the course this outline follows awards BlueCard certification).

</details>

## Next steps toward certification

To set real standards with MTM-1, you need licensed training, the official data card and certification from an MTM association; the course page this outline comes from issues the BlueCard. The skills practised here (methods analysis, motion classification, simultaneous-motion reasoning and standard development) carry over. The codes and values will be different.
