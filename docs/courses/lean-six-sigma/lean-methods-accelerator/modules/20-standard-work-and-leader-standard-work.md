# Module 20 — Standard Work and Leader Standard Work

**Time:** 60 min

## Learning objectives

1. Create standard work for an operator.
2. Design leader standard work that sustains the system.

## 1. Standard work

The current best way to do a job, so results are repeatable and improvements have a baseline. Three elements:

1. **Takt time** — the required pace.
2. **Work sequence** — steps in order, with key points and reasons.
3. **Standard WIP** — the minimum in-process stock to run smoothly.

### Case — cell operator loop (takt 240 s)

| Step | Manual (s) | Walk (s) |
|---|---|---|
| Unload/load CNC | 35 | |
| Walk to deburr | | 6 |
| Deburr ports | 110 | |
| Walk to wash | | 5 |
| Load wash | 20 | |
| Walk to leak test | | 6 |
| Leak test load/unload | 40 | |
| Walk back to CNC | | 8 |
| **Total** | **205** | **25** |

```bash
python tools/lean.py standardwork
```

Operator cycle = **230 s**, takt 240 s → only **10 s** of margin. Deburring (110 s) is the next improvement target. Standard WIP: one block in the CNC, one at each station.

**Documents:** standard work chart (layout + walk path), combination table (manual, machine and walk times vs takt), job instruction sheets with photos and key points.

Standard work is not fixed forever: it's the baseline for kaizen. When someone finds a better way, test it and update the standard.

## 2. Leader standard work

Lean systems decay without daily leadership routines. Leader standard work (David Mann, *Creating a Lean Culture*) defines what each leader checks, how often:

| Leader | Daily | Weekly |
|---|---|---|
| Team leader | Hour-by-hour board each hour; start-of-shift checks done; standard work observed for one operator; andon response | 5S audit |
| Supervisor | Gemba walk of each cell; review misses and actions at the team board; check kanban and WIP caps | Standard work audit; TPM checklist review |
| Plant manager | Tiered daily meeting (15 min); gemba walk to one area | Review KPI trends; coach one A3 |

**Tiered meetings:** team (start of shift) → supervisors → plant leadership, each short and standing, escalating problems that can't be solved at the level below.

The leader's job: check that the standards are followed, help when they aren't, and drive improvement — not to fight fires all day.

## Check yourself

Why does standard work make improvement easier, not harder?

<details><summary>Answer</summary>

Without a standard, you can't tell whether a change helped — variation between people hides it. A standard is the baseline that kaizen improves.
</details>
