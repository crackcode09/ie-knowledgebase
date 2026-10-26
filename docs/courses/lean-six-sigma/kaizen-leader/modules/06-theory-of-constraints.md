# Module 6 — Theory of Constraints

**Time:** 45 min

## Learning objectives

1. Identify a system's constraint.
2. Apply the five focusing steps.

## 1. The idea

Eliyahu Goldratt's Theory of Constraints (*The Goal*, 1984): every system has at least one constraint that limits its output. An hour lost at the constraint is an hour lost for the whole system; an hour saved at a non-constraint is a mirage.

## 2. Find the constraint — case

Compare each step's **effective** cycle time (cycle time ÷ uptime) with takt:

```bash
python tools/kaizen.py toc
```

| Step | C/T (s) | Uptime | Effective C/T (s) | vs takt 90 s |
|---|---|---|---|---|
| **Preload set** | 95 | 85% | **111.8** | **Over takt** |
| Ball insert | 75 | 92% | 81.5 | |
| Friction test | 70 | 90% | 77.8 | |
| Seal & lube | 60 | 95% | 63.2 | |
| Pack | 45 | 100% | 45.0 | |
| Kitting | 40 | 100% | 40.0 | |

Capacity of the constraint: 840 × 60 / 111.8 = **451 units/day** — matching the observed output (~465, with some overtime) and well short of 560. The preload station explains the shortfall.

## 3. Five focusing steps

| Step | Carriage cell |
|---|---|
| 1. **Identify** the constraint | Preload set |
| 2. **Exploit** it — get the most from it as it is | Never let it wait for parts or operators; run through breaks with a relief operator; move the "load fixture" element off it; inspect before it, not after (don't waste constraint time on bad parts) |
| 3. **Subordinate** everything else | Ball insert paced to preload; WIP buffer of a few units in front of preload only |
| 4. **Elevate** it — add capacity if still needed | Quick changeover (Module 9), TPM to lift uptime from 85% (Module 13), second fixture |
| 5. **Repeat** — don't let inertia become the constraint | After the event the constraint may move (e.g., to friction test) |

## Check yourself

Why is adding a faster packing machine a poor use of money right now?

<details><summary>Answer</summary>

Pack isn't the constraint; extra pack capacity can't increase output beyond the preload station's 451/day.
</details>
