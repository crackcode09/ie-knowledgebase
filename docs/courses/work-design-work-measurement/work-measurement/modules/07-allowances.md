# Module 07 — Allowances

## Objectives

- Identify the types of allowances and how they are determined.
- Apply allowances correctly to normal time.
- Avoid common allowance errors.

## Why allowances?

Normal time covers only the work itself. Over a shift, people also need time for personal needs, recovery from fatigue and unavoidable delays. Allowances add this time so the standard can be sustained all day.

## Types of allowance

| Type | Covers | How determined |
|---|---|---|
| **Personal** | rest room, drinks | policy; typical tables suggest about 5 % |
| **Basic fatigue** | general effort of working | policy / tables; often about 4 % |
| **Variable fatigue** | standing, awkward posture, force, lifting, light, noise, heat, mental strain, monotony | allowance tables (e.g. the ILO's work study guide) or ergonomic assessment |
| **Unavoidable delay** | interruptions that are part of the job and not under the worker's control | **work sampling** (Module 11) or production studies |
| **Special** | machine interference, start-up / clean-up, policy allowances | case by case; often handled separately |

(The percentages quoted are typical textbook values, not a standard — your standard practice should state your own values and their source.)

**Marlow pump assembly:** personal 5 % + basic fatigue 4 % + variable fatigue 3 % (standing, light lifts) + unavoidable delay 3 % (from work sampling) = **15 %** (often called PF&D).

## Applying allowances

Two conventions — know which one your organization uses:

| Convention | Formula | 60 s normal time, 15 % |
|---|---|---|
| Allowance as % of **normal time** | ST = NT × (1 + A) | 69.0 s |
| Allowance as % of the **workday** | ST = NT ÷ (1 − A) | 70.6 s |

15 % of the workday equals 17.65 % of normal time. Mixing conventions creates a 2–3 % error in every standard.

## Machine-controlled time

Should allowances apply during machine time? If the operator is idle during the machine cycle, personal and fatigue needs can often be met then, so many practices apply allowances to **manual elements only** (Marlow's practice: standard 117.86 s vs 124.61 s if 15 % were applied to all elements). State the rule in the standard practice.

## Common errors

- Using allowances to cover **method problems** (waiting for parts, searching) — those are wastes to fix, not to allow (Module 11 shows how to separate them).
- **Double counting** — a delay allowance plus off-standard reporting for the same delays.
- Applying the same fatigue allowance to light and heavy work.
- Never reviewing allowances when conditions change.

## Run it

```bash
python tools/wmkit.py allowances
```

## Check yourself

1. Normal time 2.0 min, allowance 12 % of normal time. Standard?
2. Why shouldn't "waiting for parts" be built into the delay allowance?
3. When might machine time need its own allowance?

<details><summary>Answers</summary>

1. 2.0 × 1.12 = 2.24 min.
2. It's a fixable process problem; building it into the standard hides it, inflates cost and removes the incentive to fix it. Report it as off-standard time instead.
3. When the operator must attend the machine continuously (monitoring, adjusting) and can't use the machine time for rest.

</details>
