# Kaizen Leader — An Open Course

A free, open course on planning, leading and sustaining kaizen events: focused 3–5-day improvement workshops where a cross-functional team analyzes a process, changes it and standardizes the result. The course follows the event itself — pre-work, Day 1 through Day 5, and 30/60/90-day follow-up — using one running case (an assembly and pack cell that misses demand), and includes a **one-day team-member track** for people who take part in events or run a short single-problem kaizen.

**Prerequisites:** none. Helpful: [Root Cause Analysis & Problem Solving](../root-cause-analysis/README.md) and [Charting Process Behavior](../charting-process-behavior/README.md).

## What you will be able to do

- Scope a kaizen, write its charter and SIPOC, and plan pre-work and logistics
- Lead a team through the week and manage change with the four conversations
- Map the current state: gemba walk, value-added flow chart, spaghetti diagram, value stream map, takt, the constraint
- Find root causes and generate solutions at kaizen speed
- Implement continuous flow, line balancing, pull/kanban and quick changeover; error-proof and pilot changes
- Standardize with 5S, visual management, standard work, TPM and a control plan
- Prove and sustain results with process behavior charts and 30/60/90-day follow-up; tell the story on an A3

## Syllabus (≈22 hours; team-member track ≈1 day)

| # | Event phase | Module | Time |
|---|---|---|---|
| 0 | Overview | [Introduction: kaizen, Lean blueprint, 3 Ms, 8 wastes](modules/00-introduction-to-kaizen.md) | 1.5 h |
| 1 | Overview | [Lean and DMAIC; kaizen measurements; baseline](modules/01-lean-dmaic-and-kaizen-measurements.md) | 1.25 h |
| 2 | Pre-work | [Pre-event planning: charter, SIPOC, plan](modules/02-pre-event-planning.md) | 2.5 h |
| 3 | Pre-work | [Leading teams, conversations and change](modules/03-leading-teams-and-change.md) | 2.5 h |
| 4 | Day 1 | [Gemba walk, process maps, spaghetti diagram, takt](modules/04-day1-current-state.md) | 2 h |
| 5 | Day 1 | [Value stream mapping](modules/05-value-stream-mapping.md) | 2 h |
| 6 | Day 1 | [Theory of constraints](modules/06-theory-of-constraints.md) | 45 min |
| 7 | Day 2 | [Root causes and solution ideas](modules/07-day2-root-causes-and-solutions.md) | 2.5 h |
| 8 | Days 3–4 | [Continuous flow, line balancing and pull](modules/08-continuous-flow-balancing-and-pull.md) | 2.5 h |
| 9 | Days 3–4 | [Quick changeover (SMED)](modules/09-quick-changeover.md) | 1.25 h |
| 10 | Days 3–4 | [FMEA, error-proofing, selecting and piloting](modules/10-fmea-error-proofing-selecting-piloting.md) | 2 h |
| 11 | Days 3–4 | [A3 problem solving](modules/11-a3-problem-solving.md) | 45 min |
| 12 | Day 5 | [Control charts revisited, 5S, visual management](modules/12-day5-control-charts-5s-visual-management.md) | 1.5 h |
| 13 | Day 5 + follow-up | [Control plan, TPM, standard work, close-out](modules/13-control-plan-tpm-standard-work-close-out.md) | 2 h |
| 14 | Team member track | [The one-day, ten-step kaizen](modules/14-team-member-one-day-kaizen.md) | 1 day |
| 15 | — | [Capstone: plan and lead a kaizen](modules/15-capstone.md) | 4–6 h |

**Team-member track:** Modules 0, 4, 5 and 14.

## Templates and reference

[Kaizen charter & pre-work checklist](templates/kaizen-charter-template.md) · [A3 template](templates/a3-template.md) · [Formulas](reference/formulas.md) · [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md) · [Solutions](solutions/README.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/kaizen.py all
python tools/make_figures.py
```

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
