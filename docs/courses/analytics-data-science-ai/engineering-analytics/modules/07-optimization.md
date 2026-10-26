# Module 07 — Optimization

## Objectives

- Formulate a decision as an optimization model: decision variables, objective, constraints.
- Solve a linear program and read the solution, binding constraints and shadow prices.
- Know the main families of optimization techniques and when to use them.

## Formulating a model

Every optimization model has three parts:

1. **Decision variables** — what you control (kits to make each week).
2. **Objective** — what to maximize or minimize (contribution margin).
3. **Constraints** — limits (machine hours, materials, demand).

## Worked example: weekly product mix

Ridgeway assembles three kits:

| | Elbow kit | Tee kit | Valve kit | Available per week |
|---|---|---|---|---|
| Contribution ($/kit) | 18 | 22 | 41 | |
| CNC hours per kit | 0.10 | 0.12 | 0.30 | 160 |
| Assembly hours per kit | 0.05 | 0.08 | 0.10 | 90 |
| Brass (kg per kit) | 1.2 | 1.5 | 2.6 | 2,200 |
| Maximum demand | 700 | 600 | 300 | |

**Model:** maximize 18E + 22T + 41V subject to the three resource constraints, the demand limits and E, T, V ≥ 0.

**Solution** (linear programming, `scipy.optimize.linprog` with the HiGHS solver):

| Result | Value |
|---|---|
| Elbow / Tee / Valve kits | **700 / 600 / 60** |
| Weekly contribution | **$28,260** |
| CNC hours used | 160 of 160 (**binding**) |
| Assembly hours used | 89 of 90 |
| Brass used | 1,896 of 2,200 kg |

**Why so few valve kits when they have the highest margin per kit?** Because CNC time is the constraint. Contribution per CNC hour: elbow 18/0.10 = $180, tee 22/0.12 = $183, valve 41/0.30 = $137. The model fills elbow and tee demand first, then spends the remaining CNC hours on valves.

**Shadow prices** (value of one more unit of a resource):

- CNC hour: **$136.67** — another CNC hour would make 3.33 more valve kits worth $41 each. Overtime or outsourcing CNC work is worth up to that much per hour.
- Assembly hours and brass: $0 — they have slack; more of them adds nothing.
- Demand limits: an extra elbow-kit order is worth $4.33 and a tee kit $5.60 (their CNC-hour advantage over valves).

This is **prescriptive analytics**: it doesn't just describe; it tells you what to do and what a constraint is worth — e.g., a CNC capacity investment paying more than ~$137 per hour of added capacity per week fails the test.

In a spreadsheet, the same model is built with the **Solver** add-in: decision cells, an objective cell with `SUMPRODUCT`, and constraint rows. The sensitivity report gives the shadow prices.

## Families of optimization

| Technique | Use when | Examples |
|---|---|---|
| Linear programming (LP) | linear objective and constraints, continuous variables | product mix, blending, transportation |
| Integer / mixed-integer (MIP) | yes/no or whole-number decisions | facility location, scheduling, machine assignment |
| Network models | flows on networks | distribution, shortest path |
| Nonlinear programming | curved relationships | process set-points, inventory with nonlinear costs |
| Heuristics and metaheuristics | huge or messy problems | sequencing, routing (genetic algorithms, simulated annealing) |
| Simulation-optimization | uncertain, complex systems | buffer sizing with variable demand |

Combine with predictive analytics: forecasts (Module 05) feed demand limits; regression (Module 04) supplies cost coefficients.

## Run it

```bash
python tools/anlkit.py optimize
```

## Check yourself

1. CNC capacity rises to 170 hours. Estimate the change in contribution from the shadow price, then check by re-solving.
2. Why is the assembly-hours shadow price zero?
3. Valve demand jumps to 500 but CNC stays at 160 h. Does the plan change?

<details><summary>Answers</summary>

1. The shadow price suggests +10 × $136.67 ≈ +$1,367 — but it is valid only while the same constraints stay binding. Each extra CNC hour makes 3.33 valve kits, which use 0.33 assembly hours, so assembly's 1 hour of slack runs out after about 3 extra CNC hours. Re-solving at 170 h gives 700 / 541.7 / 116.7 kits and **$29,300 (+$1,040)**, with assembly now binding. Lesson: shadow prices hold only over a range — re-solve for bigger changes.
2. It has slack (89 of 90 hours used) — an extra hour can't increase output.
3. No — valve output is limited by CNC hours (only 60 kits fit), not by demand. Higher valve demand matters only if CNC capacity rises.

</details>
