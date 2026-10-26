# Module 21 — Optional Review Summary and Capstone

## Review summary

| Topic | Key points |
|---|---|
| What MODAPTS is (01–02) | A body-motion PMTS: MODular Arrangement of Predetermined Time Standards; 1 MOD = 0.129 s (public value); no stopwatch, no rating |
| PMTS (03) | Code the method, look up times, add, apply allowances. MTM (1948, TMU 0.036 s), MOST and MODAPTS are major families |
| Code symbol (04) | Letter = type of activity; number = time in units; totals are added |
| Why apply (05) | Standards before production, method improvement, ergonomics, consistency, balancing |
| History (06) | MTM 1948 → MODAPTS 1966 (Heyde, Australia) → copyright assigned to the IMA in 1990 |
| Modular concept (07) | One base unit, whole numbers; time grows with the body member used |
| Codes (08) | Three classes: movement, terminal (get/put), auxiliary |
| Movements (09–12) | Classify by the largest body member; code the limiting hand; pair every movement with a terminal; weight goes in a load factor |
| Get vs put (13–17) | Get = gain control; put = place. Low-control activities overlap between hands, high-control ones don't. Design out G5 and P6 |
| Auxiliary (18–19) | Walk, bend, sit and stand; eyes, read and decide; pressure, transfer, crank, load |
| Practice (20) | Kitting −58 %, packing −52 %, 600 bends a shift removed; new-job standard 14.56 s |

## Capstone — Coil and bag a cable

A new job at Kessler: get a cable from a pile, hook it on a coiling jig, crank 4 turns, tie it with a twist tie, bag it and check the label. A 1:1 cardboard mock-up shows the cable pile 55 cm away, the jig 30 cm away and the tie dispenser 15 cm away.

1. Write the method as steps and code it with the teaching card.
2. Compute normal time, standard (12 % allowance) and units per hour.
3. Identify the two biggest improvement opportunities, and estimate the new time.
4. List the ergonomic exposures per cycle.

<details><summary>Capstone key (run <code>python tools/ptskit.py show D_cable_capstone</code>)</summary>

| Step | Codes | U |
|---|---|---|
| Reach to cable pile, get one cable end (tangled) | A8 G5 | 13 |
| Move to jig, hook on peg | A6 P3 | 9 |
| Crank 4 revolutions | K6x4 | 24 |
| Reach to tie dispenser, get tie | A4 G2 | 6 |
| Move tie around coil, align ends | A4 P6 | 10 |
| Twist ends (3 finger twists) | A2x3 | 6 |
| Get coil off jig | A3 G2 | 5 |
| Move to bag on holder, drop | A6 P0 | 6 |
| Read 2 label groups, decide | R2x2 D3 | 7 |
| **Total** | | **86 U = 8.6 s** |

- **Standard:** 8.6 × 1.12 = **9.63 s**, about **374 an hour**.
- **Improvements:**
  1. A powered coiler or a foot-switch coiler instead of the 4-revolution crank (24 U, replaced by a short process time).
  2. Cables presented separated on a comb rack within 30 cm (A8 G5 → A6 G2, saving 5 U).
  3. Optional: scan the label instead of reading it.
  - With a 1.5 s powered coil started by a pedal (F4 + PT15 = 19 U, replacing 24 U) and the comb rack: 86 − 24 + 19 − 5 = **76 U = 7.6 s**.
- **Ergonomics:** 1 extended reach, 1 selective get, 1 high-control put, and 24 U of repetitive cranking per cycle. The cranking is a wrist and shoulder repetition concern at about 370 cycles an hour.

</details>

## Skill check

1. What does the number in a code symbol represent?
2. Why is no performance rating needed in a PMTS?
3. Which body member governs the coding of a movement?
4. When may two hands perform gets at the same time?
5. What is the difference between G0 and G2 on the teaching card?
6. Name two ways to change a P6 into a P3.
7. Which class do walking and reading belong to?
8. Where must process (tool or machine) time come from?
9. What must you have before setting real MODAPTS standards?

<details><summary>Answers</summary>

1. The time in base units (MODs in MODAPTS; U on the teaching card).
2. The values are already at a defined normal pace.
3. The largest body member that has to move.
4. When both gets are low conscious control. Code the limiting hand.
5. G0 = control by contact, no grasp. G2 = a simple grasp of an easy object.
6. Lead-in chamfers or funnels, self-locating fixtures, more clearance, tool guides.
7. The auxiliary class.
8. From the equipment: measured or specified, not from motion codes.
9. The official code card and rules, training, and normally certification through the International MODAPTS Association.

</details>

## Next steps toward certification

The course page this outline comes from prepares learners for the IMA's practitioner certification test. To become a certified practitioner, contact the **International MODAPTS Association** or an authorized training provider for:

- the official code card
- the manual
- supervised practice
- the certification exam

The method you have practised here transfers directly. The codes and values will differ.
