# Module 04 — Disadvantages and Limits

## Objectives

- List the disadvantages and risks of standard data systems.
- Recognize the conditions that make a standard-data standard wrong.
- Plan controls for each risk.

## The disadvantages

| Disadvantage | Why it happens | Control |
|---|---|---|
| **High start-up cost** | Many good studies are needed (rule of thumb: at least 5–10 per predictor, spread across the range), plus analysis and documentation | Start with the bottleneck or the highest-volume family; reuse existing studies if they are good |
| **Only valid inside the data** | A formula fitted to 1–12 bends says nothing reliable about 20 | Record the range of every variable; the calculator flags jobs outside it (Module 09) |
| **Method drift** | New tooling, a new machine or a layout change alters the method, but the data stays the same | Change control: any method change triggers a review of the affected elements |
| **Hides job-specific factors** | Tight tolerances, awkward shapes or difficult materials aren't in the formula | Add a variable if it recurs; otherwise allow a documented special adjustment |
| **Lower accuracy for one job** | A formula predicts the average; one job can differ by 10–15 % | Use it where errors cancel (planning, mixes of jobs); spot-check high-value jobs |
| **Requires skill** | Regression, validation and maintenance need trained people | Train two people, document the model, keep the study data |
| **Maintenance burden** | Data ages as methods improve | Budget the hours (Harlan: 60 h a year) and audit on a schedule |
| **False precision** | "1.2986 min" looks exact | Round sensibly; publish the accuracy with the data |
| **Can fossilize waste** | Elements built from current methods include current waste | Improve the method first; standard data should describe the method you *want* |

## When the formula is wrong

Most failures fall into one of four patterns:

1. **Extrapolation.** The job's variables are outside the studied range, either one at a time or in combination (Module 08).
2. **Different method.** The job uses a step the data never saw, such as a hemming tool or a second operator for a long part.
3. **Bad source data.** One mis-keyed study distorts every coefficient. Module 08 finds a study with 3 bends keyed instead of 8.
4. **Wrong family.** Using brake data for a different machine model with a different ram speed.

## Accuracy: per job vs in aggregate

In the hold-out test (Module 08), individual job errors range from −4 % to +16 %, but the **total** for all 12 jobs is off by only **0.7 %**. Errors of different signs cancel.

This affects how to use the data:

| Use | Errors cancel? | Is standard data suitable? |
|---|---|---|
| Weekly capacity load for a department | Yes, many jobs | Very suitable |
| Product-family cost | Mostly | Suitable |
| Quote for one job | No | Suitable, with the accuracy stated and spot-checks on large quotes |
| Individual incentive pay per job | No | Use with care; validate tightly and publish the accuracy |

## Run it

```bash
python tools/sdskit.py evaluate     # range of each variable
python tools/sdskit.py validate     # per-job vs aggregate error
```

## Check yourself

1. The brake shop buys a new electric brake whose ram is 30 % faster. Which elements are affected, and what must you do?
2. A 2.6 m part comes in. The studied lengths run up to 2.3 m. What do you do?
3. Why can a formula with ±10 % job error still give a good weekly capacity plan?

<details><summary>Answers</summary>

1. Only the machine-time part of each bend (the ram cycle). The manual elements don't change. Study a sample of jobs on the new brake, then either add a machine variable to the model or keep separate per-bend values for each machine.
2. It is outside the data range. Long parts may need two people or different support, which is a different method. Set a provisional standard from the formula, mark it provisional, and time-study the first lot.
3. A weekly plan adds up many jobs. Random errors of both signs partly cancel, so the percentage error of the total shrinks roughly with the square root of the number of jobs. A systematic bias would *not* cancel, which is why validation also checks the aggregate error (Module 08).

</details>
