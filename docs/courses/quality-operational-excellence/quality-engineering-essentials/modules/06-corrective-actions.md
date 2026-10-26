# Module 06 — Corrective Actions and Control

## Objectives

- Select corrective actions with a corrective action matrix.
- Prefer error-proofing over inspection; pilot solutions and verify the effect.
- Lead the change so it sticks.
- Hold the gain with control charts, a process control plan, visual management, 5S and standard work.

## Corrective action matrix

List candidate actions for each verified root cause and score them on impact, cost, effort and risk:

| Root cause | Action | Impact | Cost | Effort | Choose? |
|---|---|---|---|---|---|
| M2 offset ≈ +0.008 mm | Re-zero M2 offset; add first-piece check after any offset change | high | low | low | ✓ |
| Tool wear without compensation | Tool-change interval 1,600 parts + automatic wear-offset increment every 400 parts | high | low | medium | ✓ |
| Coolant temperature rises | Repair/upgrade chiller with temperature alarm; check chiller in PM | medium | medium | medium | ✓ |
| Operator measurement difference | Standard micrometer method, retrain | medium | low | low | ✓ |
| Visual thread inspection unreliable | Go/no-go thread gauge on 1 in 25 | high (detection) | low | low | ✓ |
| — | Buy a new lathe | high | very high | high | ✗ (not needed — spread is fine) |

## Error-proofing

Make errors impossible or immediately obvious, rather than relying on inspection or memory. Strongest to weakest:

1. **Eliminate** the error (design it out).
2. **Prevent** (the machine counts parts and forces a tool change; the controller applies the wear offset automatically).
3. **Detect at the source** (in-process gauge stops the machine before an oversize part is made).
4. **Detect after** (go/no-go gauge at final inspection).

Bayline's tool-life counter that locks the cycle at 1,600 parts is a prevention device; the chiller temperature alarm is detection at the source.

## Piloting a solution

Test the change on a limited scale — one machine, a few shifts — to confirm it works and catch side effects before full rollout. Plan the pilot: what will change, how success is measured, how long, and what would stop it.

**M2 pilot (2 weeks before vs 2 weeks after), oversize OD:**

| | Inspected | Oversize | % |
|---|---|---|---|
| Before | 2,400 | 190 | 7.92 % |
| After | 1,800 | 6 | 0.33 % |

Two-proportion test: z = 11.5, p < 0.001; 95 % CI for the reduction **6.5 to 8.8 percentage points**. The staged p chart in Module 04 shows the new level is stable. Side effects checked: cycle time unchanged; tool cost +6 % (shorter tool life) — far less than the scrap saved.

## Leading change

Technical solutions fail when people aren't brought along. Three ideas:

1. **Leading change** — create a shared need (the customer returns), shape a vision of the better process, involve the people who do the work (the machinists helped set the tool-change interval), and communicate often.
2. **Change is a process** — people move from awareness to understanding to acceptance to commitment; expect resistance and listen to it (it often contains real problems).
3. **Delivering results** — make the new way easy (tools, fixtures, standard work), measure it, recognize contributions, and remove the old way.

## Hold the gains

**Control charts revisited:** keep X̄–R charts on OD for each machine, with a reaction plan — and recalculate limits for the new stage.

**Process control plan** (`templates/control-plan.csv`):

| Step | Characteristic / parameter | Spec / target | Method | Sample size / frequency | Control | Reaction |
|---|---|---|---|---|---|---|
| Turn OD | OD | 6.350 ± 0.025 | micrometer (standard method) | 5 / hour / machine | X̄–R chart | stop, check offset and tool; quarantine since last good subgroup |
| Turn OD | tool life | change at 1,600 parts | counter | every part | cycle lock | change tool |
| Turn OD | coolant temp | 24 ± 2 °C | chiller sensor | continuous | alarm | stop, call maintenance |
| Thread | thread fit | go/no-go | thread gauge | 1 in 25 | p chart | stop, check tap, 100 % sort lot |

**Visual management:** make status obvious at a glance — tool-life countdown on the machine display, coolant temperature with green/red bands, the control chart at the machine, shadow boards for gauges.

**5S** — Sort, Set in order, Shine, Standardize, Sustain. A clean, organized cell makes abnormalities (leaks, chips in the coolant, missing gauges) visible and reduces search time and errors.

**Standard work** — the current best way: sequence, timing, key points and reasons ("dress micrometer anvils before each check — dirt adds 0.002 mm"). Update it when the process improves; leaders check it is followed (leader standard work).

## Run it

```bash
python tools/qekit.py pilot
python tools/qekit.py staged
```

## Check yourself

1. Why is "retrain operators to check more carefully" a weak corrective action on its own?
2. The pilot reduced oversize but tool cost rose 6 %. How do you decide whether to roll it out?
3. Name the control-plan element that tells an operator what to do when a chart signals.

<details><summary>Answers</summary>

1. It relies on attention and memory, fades over time and doesn't remove the cause; pair it with error-proofing and standard work.
2. Compare total cost: scrap, sorting, returns and customer risk saved vs extra tool cost — here the saving is much larger. Also check other side effects (cycle time, safety).
3. The reaction plan.

</details>
