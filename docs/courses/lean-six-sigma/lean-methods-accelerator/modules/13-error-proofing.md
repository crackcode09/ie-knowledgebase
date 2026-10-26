# Module 13 — Error-Proofing

**Time:** 35 min

## Learning objectives

1. Apply error-proofing (poka-yoke) at the source.
2. Rank countermeasures by strength.

## 1. Principles

Shigeo Shingo (*Zero Quality Control*, 1986): mistakes are inevitable; defects are not. Catch the mistake before it becomes a defect, at the source, every time — without relying on attention or memory.

| Strength | Type | Manifold example |
|---|---|---|
| Strongest | **Eliminate** the possibility | Symmetric port pattern so the block can't be loaded wrong |
| Strong | **Prevent** (control) | Fixture with offset locating pins — block only fits one way |
| Medium | **Detect** immediately and stop | Probe checks a feature before the cycle continues; torque tool counts plugs |
| Weak | Detect later | End-of-line leak test |
| Weakest | Rely on people | Instruction "check orientation" |

**Methods:** contact (shape, pins), fixed-value (count parts, kit trays), motion-step (sequence interlocks).

## 2. Case — leak-test failures

| Cause | Error-proofing |
|---|---|
| Missing plug | Kit tray with exactly one cavity per plug; torque tool counts 7 tightenings before release |
| Wrong cartridge valve (look-alike families) | Color-coded valves and fixture nests per family |
| Chip left in port | Through-spindle coolant + vision check after wash |
| Block loaded rotated 180° | Offset locating pins |

Each moves detection from the leak test (end of line) to the point where the error could occur.

## Check yourself

Is the end-of-line leak test error-proofing?

<details><summary>Answer</summary>

It's detection, but late and after value has been added; true error-proofing prevents or catches the error where it happens.
</details>
