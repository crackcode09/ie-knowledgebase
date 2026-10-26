# Module 0 — Introduction and the Root Cause Analysis Framework

**Time:** 45 min

## Learning objectives

1. Distinguish symptoms, direct causes and root causes.
2. Distinguish containment, correction, corrective action and preventive action.
3. Follow a structured root cause framework.

## 1. Why root causes?

Fixing symptoms feels productive: sort the bad parts, adjust the machine, retrain the operator. Then the problem comes back. **Root cause analysis (RCA)** finds the cause that, if removed, prevents recurrence — and that the organization can actually control.

| Level | Example (valve leaks) |
|---|---|
| Symptom | Customer reports leaking valves |
| Direct (physical) cause | Seal seat surface too rough to seal |
| Contributing cause | Cutting tool worn |
| **Root cause** (system) | No tool-life limit or roughness check in the process; tools are changed only when they break |

A useful test: *if we fix this, would the problem have been prevented — and would it stay prevented for other parts and machines?*

## 2. Four kinds of action

| Action | Purpose | Example | Timing |
|---|---|---|---|
| **Containment** | Protect the customer now | Quarantine and 100% leak retest of stock | Hours |
| **Correction** | Fix the nonconforming product | Rework or scrap the leaking valves | Days |
| **Corrective action** | Remove the root cause so it doesn't recur | Tool-life limit + in-process roughness check | Weeks |
| **Preventive action** | Stop it happening elsewhere | Apply tool-life limits to every finishing operation plant-wide | Weeks–months |

Containment is necessary but is not a solution.

## 3. The framework used in this course

```
1. Define        Problem statement (Module 1), data and metrics (2), Pareto (3), process map (4)
2. Investigate   Fishbone (5), 5-Why (6), root cause tree (7), stratification (8)
3. Verify        Scatter/correlation (9), regression (10–12) — prove the cause with data
4. Solve         Error-proofing (13), select solutions with a decision matrix (14)
5. Act & sustain Corrective action matrix (15), verify effectiveness
```

It maps onto common formats: **DMAIC** (Define–Measure–Analyze–Improve–Control), **8D** (eight disciplines: team, problem description, containment, root cause, corrective action, implement and verify, prevent recurrence, recognize the team), and **A3** problem solving.

## 4. Running case

Throughout the course: a valve-body machining cell (three CNC machines, MC1–MC3, plus a leak tester). Scrap has risen and two customers have reported leaking valves. All data are synthetic and regenerate with `python tools/make_data.py`.

## Check yourself

1. "Operator error" is given as the root cause. What should you ask next?
2. Sorting all stock with a leak tester — containment or corrective action?

<details><summary>Answers</summary>

1. Why was the error possible and not caught? (Unclear instruction, no error-proofing, no feedback.) "Operator error" is almost never the root cause.
2. Containment.
</details>
