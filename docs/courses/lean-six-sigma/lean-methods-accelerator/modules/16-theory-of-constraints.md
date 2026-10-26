# Module 16 — The Theory of Constraints

**Time:** 45 min

## Learning objectives

1. Identify the constraint and apply the five focusing steps.
2. Explain drum-buffer-rope scheduling.

## 1. Find the constraint

Eliyahu Goldratt, *The Goal* (1984): a system's output is limited by its constraint; improving anything else doesn't increase output.

```bash
python tools/lean.py toc
```

| Step | Effective C/T (min) |
|---|---|
| **CNC machining** | **4.09** (> takt 4.0) |
| Assemble & pack | 3.71 |
| Leak test | 3.70 |
| Deburr | 3.10 |
| Wash | 2.11 |
| Saw | 1.22 |

Constraint capacity: 880 / 4.09 = **215/day** vs demand 220.

## 2. Five focusing steps

| Step | Manifold plant |
|---|---|
| 1. Identify | CNC machining |
| 2. Exploit | Never idle: run through breaks, pre-stage material, inspect before CNC, no defective blanks, stagger lunch |
| 3. Subordinate | Release work at the CNC's pace; other steps serve the CNC |
| 4. Elevate | SMED (Module 15), TPM (Module 19), and only then consider a third machine |
| 5. Repeat | After improvement, leak test or assembly (3.7 min) may become the constraint — watch for it |

## 3. Drum-buffer-rope (DBR)

- **Drum:** the constraint sets the pace of the whole plant.
- **Buffer:** a time buffer of work just before the constraint (e.g., ~4 hours) so it never starves.
- **Rope:** release raw material into the system only at the drum's pace — tied to the constraint, not to MRP's schedule.

DBR is a form of pull: it caps WIP between release and the constraint. Compare CONWIP in Module 17.

## Check yourself

The saw is idle 70% of the time. Should the team improve its utilization?

<details><summary>Answer</summary>

No — the saw isn't the constraint. Keeping it busy would just build inventory; it should run only at the CNC's pace.
</details>
