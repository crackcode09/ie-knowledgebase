# Module 13 — Control Plan, TPM, Standard Work and Project Close-Out

**Time:** 2 h

## Learning objectives

1. Write the control plan and standard work for the new process.
2. Calculate OEE and explain TPM's role in sustaining the gains.
3. Run the report-out and the 30/60/90-day follow-up.

## 1. Control plan

| What | How measured | Frequency | Who | Reaction |
|---|---|---|---|---|
| Output vs hourly target | Hour-by-hour board | Hourly | Team leader | Record reason; call support if 2 hours missed |
| Daily output | XmR chart | Daily | Supervisor | Investigate signals |
| Preload changeover time | Changeover log | Each changeover | Setter | > 20 min → review against standard |
| WIP | Count of WIP squares filled | Each shift | Team leader | Over limit → stop upstream |
| 5S | Audit checklist | Weekly | Rotating | Score < 15 → action |
| Kanban | Card count audit | Weekly | Material handler | Missing cards → find and replace |

## 2. TPM and OEE

Total Productive Maintenance (Seiichi Nakajima, 1980s) makes equipment reliable through operator involvement (autonomous maintenance: clean, inspect, lubricate), planned maintenance, and eliminating losses.

**OEE** = Availability × Performance × Quality

Preload station, one shift:

| Factor | Calculation | Value |
|---|---|---|
| Availability | (420 − 63 min downtime) / 420 | 0.850 |
| Performance | (95 s × 186 units / 60) / 357 min run time | 0.825 |
| Quality | 178 good / 186 | 0.957 |
| **OEE** | 0.850 × 0.825 × 0.957 | **0.671** |

```bash
python tools/kaizen.py oee
```

Availability and performance losses dominate — so the follow-up should target breakdowns, minor stops and speed losses at the constraint (operator daily checks, fixing the shim adjustments at root).

## 3. Standard work

Three elements: **takt time**, **work sequence**, **standard WIP**. For operator 3 (preload + seals):

| # | Step | Key point | Reason | Time (s) |
|---|---|---|---|---|
| 1 | Take carriage from WIP square | One at a time | Flow | 2 |
| 2 | Load into preload fixture, close clamps | Clamp light green before start | Clamp fully closed | 6 |
| 3 | Start preload cycle; read gauge | Within green band | Correct preload | 50 |
| 4 | Fit end seals both sides | Lip faces outward | Sealing direction | 22 |
| | **Total** | | | **80** (takt 90) |

Standard WIP: 1 unit in each fixture, 1 in each WIP square. Post it at the station with photos.

## 4. Report-out (Friday)

Fifteen to thirty minutes, team presents (not the leader), at the gemba where possible: charter goal → before → what we did → after (data) → open actions → what we learned. Sponsor thanks the team.

## 5. Close-out and follow-up

| Day | Check |
|---|---|
| +30 | All "do-now" actions closed; metrics on charts; standard work followed (audit) |
| +60 | Remaining actions closed; second-round improvements (constraint uptime) |
| +90 | Results sustained; hand-off complete; lessons shared with other cells |

Close the kaizen only when results have held — not when the week ends.

## Check yourself

Availability 0.90, performance 0.95, quality 0.99. OEE? Which loss would you attack first?

<details><summary>Answer</summary>

OEE = 0.846. Availability (10% loss) is the largest — attack downtime first.
</details>
