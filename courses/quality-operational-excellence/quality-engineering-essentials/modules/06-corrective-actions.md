# Module 06 — Corrective Actions and Control

**Time:** 6 h (about half of it with the data)

## Objectives

- Select corrective actions with a corrective action matrix.
- Prefer error-proofing over inspection; pilot solutions and verify the effect.
- Lead the change so it sticks.
- Hold the gain with control charts, a process control plan, visual management, 5S and standard work.

## Corrective action matrix

List candidate actions for each verified root cause and score them on impact, cost, effort and risk (`templates/corrective-action-matrix.csv`):

| Root cause (Module 05) | Action | Impact | Cost | Effort | Choose? |
|---|---|---|---|---|---|
| M2 offset ≈ +0.008 mm | Re-zero M2 offset; add first-piece check after any offset change | high | low | low | ✓ |
| Tool wear without compensation | Tool-change interval 1,600 parts + automatic wear-offset increment every 400 parts | high | low | medium | ✓ |
| Coolant temperature rises on shift C | Repair or upgrade the chiller with a temperature alarm; check the chiller in PM | medium | medium | medium | ✓ |
| Operator measurement difference | Standard micrometer method, retrain, repeat the gauge study | medium | low | low | ✓ |
| Visual thread inspection unreliable | Go/no-go thread gauge on 1 in 25 | high (detection) | low | low | ✓ |
| — | Buy a new lathe | high | very high | high | ✗ (not needed: spread is fine, Module 04) |

Why 1,600 parts: in the production sample 12 of M2's 19 oversize inserts came from tools older than 1,600 parts, and the regression gives 0.0145 mm of growth over a 2,400-part life; changing at 1,600 with an offset step every 400 keeps the growth between steps to about 0.0025 mm (0.0145 mm × 400 / 2,400).

## Error-proofing

Make errors impossible or immediately obvious, rather than relying on inspection or memory (shingo-1986). Strongest to weakest:

1. **Eliminate** the error (design it out).
2. **Prevent** (the machine counts parts and forces a tool change; the controller applies the wear offset automatically).
3. **Detect at the source** (an in-process gauge stops the machine before an oversize part is made).
4. **Detect after** (a go/no-go gauge at final inspection).

Bayline's tool-life counter that locks the cycle at 1,600 parts is a prevention device; the chiller temperature alarm is detection at the source.

## Worked example: piloting the solution, before and after

Test the change on a limited scale, one machine for a few weeks, to confirm it works and to catch side effects before full rollout. Plan the pilot: what will change, how success is measured, how long, and what would stop it.

**The situation before.** Module 04 found M2 running 0.017 mm above target with a Ppk of 0.47 and 8 % of its inserts expected out of specification; Module 05 traced that to the offset, uncompensated tool wear and coolant temperature. The before figures below are the two weeks of normal M2 production immediately before the change, counted at final inspection.

**What changed.** On M2 only: the offset was re-zeroed with a first-piece check, the tool-change interval was set to 1,600 parts with an automatic wear-offset increment every 400 parts, and the chiller was serviced and fitted with a temperature alarm. Nothing else changed; M1 ran as before.

**Data:** `data/pilot_results.csv`, two rows: phase (before, after), inserts inspected, inserts oversize. And `data/pilot_daily.csv`, the same inspection broken down by day, used for the staged chart in Module 04. `data/tooling_cost.csv` holds the cost inputs for the side-effect check: the price of a tool edge, the tool-change intervals before and after, the conversion cost per insert excluding tooling, and the cost of scrapping an oversize insert.

**Steps:**

1. Compute the fraction oversize before and after.
2. Test whether the difference is bigger than chance would produce with a two-proportion z-test, and give a 95 % confidence interval for the reduction (formulas and symbols in `reference/formulas.md`).
3. Check the side effects: cycle time (unchanged, from the machine log) and tooling cost, computed from the cost inputs.

Command: `python tools/qekit.py pilot`.

**Result:**

| | Inspected | Oversize | % |
|---|---|---|---|
| Before | 2,400 | 190 | 7.92 % |
| After | 1,800 | 6 | 0.33 % |

Two-proportion test: z = 11.5, p < 0.001; 95 % CI for the reduction **6.5 to 8.8 percentage points**.

| Side effect | Before | After | Change |
|---|---|---|---|
| Tooling cost per insert | $0.010 | $0.015 | +50 % |
| Cost per insert (conversion + tooling) | $0.390 | $0.395 | +1.3 % |
| Scrap avoided per insert made | | | $0.042 |
| Net saving per insert made | | | $0.037 |

**What it means.** The reduction is real: a z of 11.5 means a difference this large would essentially never arise by chance, and even the low end of the confidence interval (6.5 points) is a large improvement. The staged p chart in Module 04 is the picture of the new level holding day by day. The side effect is real too: changing tools every 1,600 parts instead of 2,400 uses 50 % more tool edges. But tooling is a small part of the cost of an insert, so the cost per insert rises by about 1.3 %, while the scrap avoided is worth about eight times the extra tooling. The pilot passes on both counts and goes to rollout.

## Leading change

Technical solutions fail when people aren't brought along. Three ideas. They are the course's own summary, not a published model; Kotter's eight steps (kotter-1996) are the standard reference for leading change and cover the same ground in more detail:

1. **Leading change**: create a shared need (the customer returns), shape a vision of the better process, involve the people who do the work (the machinists helped set the tool-change interval), and communicate often.
2. **Change is a process**: people move from awareness to understanding to acceptance to commitment; expect resistance and listen to it, because it often contains real problems.
3. **Delivering results**: make the new way easy (tools, fixtures, standard work), measure it, recognize contributions, and remove the old way.

## Hold the gains

**Control charts revisited:** keep X̄–R charts on OD for each machine, with a reaction plan, and recalculate limits for the new stage.

**Process control plan** (`templates/control-plan.csv`):

| Step | Characteristic / parameter | Spec / target | Method | Sample size / frequency | Control | Reaction |
|---|---|---|---|---|---|---|
| Turn OD | OD | 6.350 ± 0.025 | micrometer (standard method) | 5 / hour / machine | X̄–R chart | stop, check offset and tool; quarantine since last good subgroup |
| Turn OD | tool life | change at 1,600 parts | counter | every part | cycle lock | change tool |
| Turn OD | coolant temp | 24 ± 2 °C | chiller sensor | continuous | alarm | stop, call maintenance |
| Thread | thread fit | go/no-go | thread gauge | 1 in 25 | p chart | stop, check tap, 100 % sort lot |
| Measurement | micrometer gauge R&R | < 10 % of tolerance | repeat the Module 03 study | after the method change, then yearly | study record | retrain, repair or replace the gauge |

**Visual management:** make status obvious at a glance: a tool-life countdown on the machine display, coolant temperature with green and red bands, the control chart at the machine, shadow boards for gauges.

**5S**: Sort, Set in order, Shine, Standardize, Sustain. A clean, organized cell makes abnormalities (leaks, chips in the coolant, missing gauges) visible and reduces search time and errors.

**Standard work**: the current best way: sequence, timing, key points and reasons ("dress micrometer anvils before each check; dirt adds 0.002 mm"). Update it when the process improves; leaders check that it is followed (leader standard work).

## Run it

```bash
python tools/qekit.py pilot
python tools/qekit.py staged
```

## Exercise 6.1

Using `data/tooling_cost.csv` and the pilot results:

1. The extra tooling cost is $0.005 per insert. What reduction in the oversize rate, in percentage points, would exactly pay for it? Compare with the 6.5-point low end of the confidence interval.
2. Suppose a tool edge cost $60 instead of $24. Recompute the extra tooling cost per insert and the net saving. Does the decision change?
3. Write the reaction-plan entry for the coolant alarm in the control plan as a short numbered procedure an operator could follow at 2 a.m.

Answers in `solutions/README.md`.

## Check yourself

1. Why is "retrain operators to check more carefully" a weak corrective action on its own?
2. The pilot reduced oversize but tooling cost per insert rose 50 %. How do you decide whether to roll it out?
3. Name the control-plan element that tells an operator what to do when a chart signals.

<details><summary>Answers</summary>

1. It relies on attention and memory, fades over time and doesn't remove the cause; pair it with error-proofing and standard work.
2. Compare total cost per insert: scrap, sorting, returns and customer risk saved against the extra tooling; here the saving is about eight times the extra cost. Also check other side effects (cycle time, safety).
3. The reaction plan.

</details>
