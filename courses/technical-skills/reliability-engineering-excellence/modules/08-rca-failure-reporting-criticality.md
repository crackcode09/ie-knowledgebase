# Module 08 — Root Cause Analysis, Failure Reporting and Criticality Analysis

## Objectives

- Set up a failure reporting, analysis and corrective action system (FRACAS).
- Run a root cause analysis on an equipment failure, down to physical, human and latent causes.
- Use FMECA to rank failure modes and target actions.

## Failure reporting (FRACAS)

Reliability improvement runs on data. A closed-loop system:

1. **Report** every failure with a structured work order: asset, **failure mode** (from a standard code list), symptom, cause (if known), action, downtime, parts, labor.
2. **Analyze** — Pareto (Module 05), Weibull (Module 06), trends; trigger RCA by rule.
3. **Correct** — assign actions with owners and dates.
4. **Verify** — did the failure rate drop? Close the loop.

**RCA triggers** (example policy for Line A): any failure on a class-A asset; any failure with a safety consequence; downtime > 4 h; the same failure mode three times in 90 days; repair cost > $5,000.

Data quality is the weak point in most plants. "Fixed" or "replaced part" as the only text makes analysis impossible. Fix it with standard failure-mode codes, a required "cause" field, and supervisors reviewing work orders before closing them.

## Root cause analysis for equipment

Work down three levels:

| Level | Question | Spindle bearing example |
|---|---|---|
| **Physical root** | What physically happened to the part? | rolling-contact fatigue spalling, accelerated by contaminated grease |
| **Human root** | What did people do (or not do) that allowed it? | regreasing done with an unclean grease gun; wrong grease used after a stores substitution |
| **Latent root** | Which system, procedure or culture let the human error happen? | no lubrication standard or color-coded tools; MOC not applied to the grease substitution; no oil/grease analysis |

Tools: **5-Why** for simple chains, **cause-and-effect (fishbone)** for brainstorming, **fault tree** for complex or safety-critical failures, and **failure analysis of the part itself** (bearing inspection, metallurgy) — always keep failed parts, labeled.

Corrective actions should target latent causes (they prevent many future failures), not only the physical cause (which fixes one).

## FMECA: failure modes, effects and criticality analysis

For each failure mode, rate (1–10 scales typical):

- **Severity** of the effect,
- **Occurrence** (likelihood),
- **Detection** (how likely we catch it before it reaches function — 10 = can't detect).

Risk priority number **RPN = S × O × D**, or use a criticality matrix of severity vs occurrence.

Grinder spindle, illustrative:

| Failure mode | Effect | S | O | D | RPN | Action |
|---|---|---|---|---|---|---|
| Bearing spall (contaminated grease) | spindle seizure, scrap, 22 h down | 8 | 6 | 6 | 288 | lubrication standard + monthly vibration route |
| Drawbar spring fatigue | tool pull-out, crash | 9 | 3 | 7 | 189 | drawbar force check every 500 h |
| Encoder cable wear | stop, alarm | 5 | 4 | 3 | 60 | cable routing fix |
| Coolant ingress at seal | bearing corrosion | 7 | 4 | 6 | 168 | seal upgrade, air purge |

RPN has known weaknesses — the same RPN can hide very different risks (S = 10 with O = 1 vs S = 2 with O = 10), and the scales are ordinal. **Always look at high-severity items individually**, regardless of RPN. Some standards now favor action-priority tables over RPN — check what your industry uses.

## Exercise: RCA on Line A

Using `data/work_orders.csv`, pick the failure mode that meets the most RCA triggers (hint: spindle bearing failure — class A, long downtime, high cost). Complete `templates/rca-report.md`: problem statement, timeline, physical/human/latent causes, evidence, actions, verification plan.

## Check yourself

1. Why keep and label failed parts?
2. A press seal leaks 9 times in 12 months. Which trigger(s) apply, and what would your first question be?
3. Give a latent-cause action for "wrong grease used."

<details><summary>Answers</summary>

1. The part is the primary evidence of the physical root cause (fatigue, overload, corrosion, contamination all look different). Without it, RCA becomes guesswork.
2. Repeat failure (3+ in 90 days, depending on timing) and class-A asset. First question: "What do the failed seals look like?" — nicks (installation), hardening (heat/chemistry), extrusion (pressure/clearance).
3. Lubrication standard with a single approved grease per point, color-coded grease guns and fittings, stores substitutions routed through MOC.

</details>
