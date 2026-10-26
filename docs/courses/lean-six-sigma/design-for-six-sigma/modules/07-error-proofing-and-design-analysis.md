# Module 7 — Error-Proofing and Analyzing Designs

**Time:** 3 h · **Phase:** Design

## Learning objectives

1. Apply error-proofing (poka-yoke) principles to designs and processes.
2. Use Design for Manufacture and Assembly (DFM/DFA) guidelines to analyze a design.

## 1. Error-proofing

Shigeo Shingo developed **poka-yoke** (mistake-proofing) at Toyota: people make mistakes; good design makes mistakes impossible or immediately obvious.

| Level (strongest first) | Example |
|---|---|
| **Eliminate** — the error can't occur | Symmetric part that works either way round |
| **Prevent (control)** — the process stops the error | Asymmetric pin so a part only fits one way; dispenser only accepts the correct lube cartridge |
| **Detect (warning/stop)** — the error is caught immediately | Sensor stops the press if the seal isn't present; torque tool counts fasteners |
| Mitigate | Design so the error causes less harm |

**Common methods:** contact (shape, pins, guides), fixed-value (count of parts, kitting trays with exactly one hole per part), motion-step (sequence interlocks).

Applied to the FMEA in Module 6:

| Failure mode | Error-proofing |
|---|---|
| Wiper seal omitted | Seal acts as the end cap's locating feature — the cap won't seat without it |
| Wrong lubricant | Unique cartridge connector per grease type |
| Preload too high | Selective assembly by measured ball size, plus 100% force check (detect) |

## 2. DFM / DFA

Most product cost is set by part count, part complexity and assembly difficulty.

**DFA guidelines** (after Boothroyd & Dewhurst):

- Minimize part count. For each part ask: does it move relative to others? Must it be a different material? Must it be separate for assembly/service? If all "no," combine it.
- Minimize fasteners (snap fits, integral features).
- Design for top-down, single-axis assembly.
- Make parts self-locating and self-aligning (chamfers, lead-ins).
- Make parts symmetric — or obviously asymmetric.
- Avoid parts that tangle, nest or are hard to grip.

**DFM guidelines:**

- Use standard materials, sizes and components.
- Specify the loosest tolerance that meets function (Module 10).
- Match features to the chosen process (draft angles for molding, uniform wall thickness, standard drill sizes, avoid deep narrow pockets).
- Datum and tolerance schemes that the shop can actually measure.

### Worked example — carriage end-cap assembly

| Before | After |
|---|---|
| End cap, seal, retainer plate, 4 screws, lube nipple = 8 parts | End cap with molded-in seal groove, snap-fit retainer, press-in lube nipple = 3 parts |
| 4 screwing operations, 2 orientations | 3 press/snap operations, single axis |

Fewer parts = fewer failure modes, less inventory, shorter assembly time.

## Check yourself

1. Is a final inspection of every carriage error-proofing?
2. Apply the three DFA questions to a spacer washer between two steel parts.

<details><summary>Answers</summary>

1. No — inspection detects defects after they're made; error-proofing prevents or stops them at the source.
2. It doesn't move, needn't be a different material (if steel), and isn't needed for assembly/service separately → candidate to integrate as a shoulder on one of the parts.
</details>
