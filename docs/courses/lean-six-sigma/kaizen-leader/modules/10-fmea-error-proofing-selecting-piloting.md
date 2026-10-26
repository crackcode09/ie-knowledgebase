# Module 10 — FMEA, Error-Proofing, Selecting and Piloting Solutions

**Time:** 2 h

## Learning objectives

1. Use a quick FMEA to check the new process for risks before running it.
2. Error-proof the new process.
3. Select solutions and run a pilot during the event.

Full treatments: *Design for Six Sigma* (FMEA, Module 6; error-proofing, Module 7) and *Root Cause Analysis* (decision matrix, Module 14). This module shows the kaizen-speed versions.

## 1. Quick FMEA on the new cell

Before switching over on Day 4, the team asks of each changed step: what could go wrong now?

| New-process step | Failure mode | S | O | D | RPN | Action |
|---|---|---|---|---|---|---|
| One-piece flow, preload → seal | Unit skips seal step when operator covers two stations | 7 | 4 | 6 | 168 | Fixture nest: test rig won't clamp a carriage without seals |
| Quick clamps on preload fixture | Clamp not fully closed | 8 | 3 | 5 | 120 | Clamp position sensor interlocked to cycle start |
| Kanban from kitting | Wrong part size in container | 6 | 3 | 4 | 72 | Color-coded containers per size |
| Shared operator 1 (kit + pack) | Packing falls behind when kitting has issues | 4 | 4 | 3 | 48 | Visual WIP limit; andon to call relief |

## 2. Error-proofing in the cell

Prefer devices that **prevent** (fixture nests, interlocks, color coding, sequenced kits) over those that only detect, and both over instructions. Shingo: build quality in at the source.

## 3. Prioritizing and selecting

For the kaizen's idea list, a simple impact/effort grid plus "can we do it this week?" is usually enough:

| | Low effort | High effort |
|---|---|---|
| High impact | **Do now:** pre-stage changeover cart, point-of-use parts, move fixture loading | **Do this week if possible / plan:** U-cell move, quick clamps, preset gauge |
| Low impact | Do if convenient: label holders | Park: new automatic packer |

Use a weighted decision matrix when ideas compete for the same resources.

## 4. Piloting during the event

- **Try-storm**: build it rough (cardboard, tape, temporary racks), run real parts, time it, fix it.
- **Pilot on Day 4**: run the new cell for at least a full shift with the regular operators; measure output per hour, quality, safety and ergonomics.
- **Decide on Day 5**: keep, adjust, or roll back — on data.

**Case pilot (Thursday, one shift):** output 290 units in 7 h of run time (41.4/h ≈ 87 s per unit, under takt 90 s), zero friction-test failures, no safety issues. Two problems: label printer too far from operator 4, and grease dispenser runs low mid-shift → both added to the action list.

## Check yourself

Why run an FMEA on the *new* process during a kaizen?

<details><summary>Answer</summary>

Changes create new failure modes (skipped steps, mixed parts). Catching them before switch-over protects the customer and the credibility of the event.
</details>
