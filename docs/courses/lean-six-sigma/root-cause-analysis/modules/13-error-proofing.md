# Module 13 — Error-Proofing

**Time:** 40 min

## Learning objectives

1. Design countermeasures that prevent a verified root cause from recurring.
2. Rank countermeasures by strength.

## 1. Strength of countermeasures

| Strength | Type | Valve example |
|---|---|---|
| Strongest | **Eliminate** the cause | Finishing process that doesn't wear in the relevant range (e.g., a different seat-finishing method) |
| Strong | **Prevent** — the process can't make the error | Machine controller locks the cycle when the insert passes its tool-life count; torque tool can't release below 22 N·m |
| Medium | **Detect immediately** at the source | In-process Ra probe after finishing; stop on out-of-limit |
| Weak | Detect later | End-of-line leak test (already exists — it let marginal parts through) |
| Weakest | Rely on people | Work instruction: "check finish visually"; training; reminders |

Shigeo Shingo's poka-yoke principle: don't rely on attention or memory for things that matter. Training and procedures are necessary but are not, by themselves, corrective actions for a systemic root cause.

## 2. From root causes to countermeasures

| Root cause (Module 7) | Countermeasure | Strength |
|---|---|---|
| No tool-life limit on finishing | Tool-life counter in the CNC with automatic stop at the limit | Prevent |
| No in-process roughness check | In-process Ra probe, automatic reject | Detect at source |
| "Retest until pass" practice | Leak tester software allows one test per serial number; fails route to quarantine automatically | Prevent |
| Torque not controlled | Torque-controlled clamp with interlock | Prevent |

## Check yourself

Why is "retrain the operators" a weak corrective action for the worn-tool cause?

<details><summary>Answer</summary>

The root cause is the missing tool-life system, not operator knowledge; training fades and doesn't stop the machine from running with a worn insert.
</details>
