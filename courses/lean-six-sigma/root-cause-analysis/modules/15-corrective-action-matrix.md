# Module 15 — Corrective Action Matrix and Verifying Effectiveness

**Time:** 45 min

## Learning objectives

1. Track improvement actions with a corrective action matrix.
2. Verify that actions worked and are sustained.

## 1. The matrix

One row per action; reviewed weekly until closed.

| # | Root cause | Action | Type | Owner | Due | Status | Verification method | Verified? |
|---|---|---|---|---|---|---|---|---|
| 1 | Leakers shipped | Quarantine and retest stock; notify customers | Containment | Quality lead | Week 9 | Done | Customer complaint count | ✓ |
| 2 | No tool-life limit | 16 h finishing-insert change interval in CNC tool-life counter | Corrective | Mfg engineer | Week 10 | Done | Ra chart; leak rejects per week | In progress |
| 3 | No in-process Ra check | Install in-process Ra probe with auto-reject | Corrective | Mfg engineer | Week 16 | Open | Probe gauge study; leak rejects | — |
| 4 | Retest-until-pass | Tester software: one test per serial; auto quarantine | Corrective | Test engineer | Week 11 | Done | Audit of tester logs | ✓ |
| 5 | Torque not controlled | Torque-controlled clamp, 22–24 N·m window | Corrective | Maintenance | Week 13 | Open | Torque log | — |
| 6 | Seat Ra limit doesn't protect function | Engineering review of 0.80 µm drawing limit (data suggest ≤ 0.5) | Corrective | Design engineer | Week 14 | Open | Drawing change | — |
| 7 | Same gap may exist elsewhere | Audit all finishing operations for tool-life limits | Preventive | CI engineer | Week 20 | Open | Audit report | — |

## 2. Verify effectiveness

An action is closed when **data** show the problem is reduced and stays reduced — not when the task is done.

- Plot leak rejects per week on a process behavior chart with limits from the baseline; look for a sustained shift (see *Charting Process Behavior*).
- Quantify the change with a confidence interval or test (see *Fundamentals of Hypothesis Testing*).
- Confirm the mechanism: Ra values after the change should sit near the predicted 0.63 µm.
- Check for side effects (tool cost, cycle time).

## 3. Sustain

Update the control plan, standard work, FMEA and training; hand ownership to the process owner; share the lessons (preventive action across similar processes).

## Check yourself

An action is marked "done" but leak rejects haven't changed after four weeks. What now?

<details><summary>Answer</summary>

Reopen it. Either the action isn't working as intended (check it's actually in place) or the root cause was wrong or incomplete — go back to the tree and the data.
</details>
