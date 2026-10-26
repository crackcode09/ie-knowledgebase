# Module 21 — The Lean Journey, Skill Check and Capstone

**Time:** 60 min + capstone

## 1. The Lean journey

Lean is a long-term system, not a toolkit. Typical stages:

| Stage | Focus | Risk |
|---|---|---|
| 1. Awareness & pilots | Training, kaizen events in a model area | "Program of the month" |
| 2. Model value stream | VSM, flow, pull, standard work in one value stream end-to-end | Isolated success |
| 3. Expansion | More value streams; supporting functions (planning, maintenance, purchasing) | Tools without thinking |
| 4. Management system | Leader standard work, tiered meetings, A3 thinking, strategy deployment (hoshin kanri) | Leaders delegate Lean to a department |
| 5. Culture | Everyone improves every day; problems surfaced, not hidden | Complacency |

**Manifold plant roadmap:** COPQ and VSM (month 1) → CNC SMED + TPM kaizen (months 2–3) → machining cell + WIP cap + kanban (months 3–6) → heijunka at assembly, supplier kanban (months 6–9) → distributor demand sharing to dampen bullwhip (months 9–12) → leader standard work and tiered meetings throughout.

Respect for people is the other pillar of the Toyota Way (Liker, *The Toyota Way*, 2004): Lean that removes people's jobs stops getting their ideas.

## 2. Skill check

1. Classify COPQ: (a) calibration of gauges; (b) customer penalty for late delivery.
2. Available time 450 min, demand 150. Takt?
3. A step has C/T 5 min, 2 machines, 80% uptime. Effective C/T? Over a 3-min takt?
4. Inventory 600 units, demand 100/day. Lead time?
5. Why does a 90-min changeover lead to large inventory?
6. Name two causes of the bullwhip effect and one remedy each.
7. A CONWIP cap is reduced and throughput falls. What happened?
8. Demand 200/day, replenishment 0.5 day, safety 20%, container 20. Kanban cards?
9. MTBF 40 h, MTTR 2 h. Availability?
10. What three elements make up standard work?

<details><summary>Answers</summary>

1. (a) Appraisal; (b) external failure.
2. 3.0 min.
3. 5 / 2 / 0.8 = 3.125 min — over a 3-min takt.
4. 6 days.
5. Long changeovers make frequent switching uneconomic, so large batches are run; each product's stock must cover the long interval between runs.
6. E.g., forecast updating → share end-customer data; order batching → frequent small orders; price promotions → stable pricing; shortage gaming → allocate by past sales.
7. The cap is too low — the bottleneck is starved.
8. 200 × 0.5 × 1.2 / 20 = 6.
9. 40 / 42 = 0.952.
10. Takt time, work sequence, standard WIP.
</details>

## 3. Capstone

Apply the course to a value stream you know (or use the manifold plant data in `tools/lean.py`):

1. COPQ estimate by category.
2. Gemba walk notes; waste list (DOWNTIME).
3. Takt; current-state VSM with timeline, lead time and PCE; extended map (supplier and customer).
4. Constraint analysis and five focusing steps.
5. Pareto of losses at the constraint.
6. Future-state VSM: flow, pull type and WIP cap or kanban sizes, pacemaker and heijunka sequence.
7. One SMED study with EPEI before and after.
8. TPM: MTBF, MTTR, OEE and loss analysis for one machine; autonomous maintenance checklist.
9. Standard work for one operator; leader standard work for one supervisor.
10. A3 telling the story, and a 12-month roadmap.

Score each item 0 (missing) / 1 (present) / 2 (quantified and linked to the customer and the constraint). 15+ of 20: ready to lead Lean projects.
