# Module 5 — Introduction to Process Behavior Charts & Limits

**Time:** 45 min

## Learning objectives

1. Distinguish common-cause (routine) from special-cause (assignable) variation.
2. Explain where control limits come from and why they are three sigma.
3. Explain why control limits and specification limits must never be confused.

## 1. Two kinds of variation

| | Common cause (routine) | Special cause (assignable / exceptional) |
|---|---|---|
| Source | Many small, ever-present factors built into the system | A specific, identifiable event or change |
| Pattern | Random scatter within predictable limits | Points outside limits or non-random patterns |
| Who fixes it | Management — requires changing the system | Usually local — find it, remove it (or keep it, if it helps) |
| Wrong response | Investigating individual points | Ignoring it |

A process showing only common-cause variation is **predictable** (in statistical control). Predictable does not mean good — it means you can say what it will do tomorrow.

## 2. Anatomy of a chart

```
  UCL / UNPL  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   center + 3σ̂(within)
                 •     •
  Center line ─────•─────•───•──•─────   average (or median)
              •       •          •
  LCL / LNPL  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─   center − 3σ̂(within)
```

- Limits are **computed from the data**, not chosen.
- σ̂ is the **within** estimate (moving ranges or subgroup ranges — Module 3).
- Wheeler calls the limits on an individuals chart **natural process limits** (UNPL/LNPL) because they describe where individual values naturally fall.

## 3. Why three sigma?

Shewhart chose three-sigma limits on economic and empirical grounds, not from a probability table:

- Wide enough that a predictable process will rarely produce a false alarm (for many distribution shapes, well under 1% of points).
- Narrow enough to catch shifts that matter in practice.
- Robust: the result holds well for non-normal data, so no distributional assumption is needed for the chart to be useful.

## 4. Limits are the voice of the process; specs are the voice of the customer

| | Control (natural process) limits | Specification limits |
|---|---|---|
| Comes from | The process data | Engineering / customer |
| Answers | "Is the process behaving consistently?" | "Is this part acceptable?" |
| Applies to | The plotted statistic (individuals, averages, ranges…) | Individual parts |
| Changes when | The process changes and you recompute | The design changes |

Four possible states (after Wheeler):

| | Predictable | Unpredictable |
|---|---|---|
| **All product in spec** | Ideal state — keep it there | Brink of chaos — it's in spec by luck |
| **Some product out of spec** | Threshold state — must change the system (reduce variation or recenter) | Chaos — first remove special causes |

**Never draw spec limits on an X̄ chart.** Averages vary less than individuals, so an average can sit inside spec while individual parts are out.

## 5. Baseline, freeze, extend

1. Collect a baseline: ideally 20–30 points (limits from as few as ~6–10 are usable but softer; treat them as provisional).
2. Compute limits. If there are special causes, investigate; remove points only if you found and fixed the cause.
3. **Freeze** the limits and **extend** them forward. Plot new data against them.
4. Recompute only when there is evidence the process has changed (a sustained signal following a deliberate change), not on a calendar.

## Check yourself

1. A process is stable but 4% of parts are out of spec. Which state is it in, and what action is required?
2. Why must spec limits never appear on an X̄ chart?
3. True or false: control limits should be recalculated every month.

<details><summary>Answers</summary>

1. Threshold state. The system must change — reduce common-cause variation or recenter. Hunting for special causes won't help.
2. X̄ limits describe averages; specs apply to individual parts. Mixing them is misleading.
3. False. Recompute only after a documented process change.
</details>
