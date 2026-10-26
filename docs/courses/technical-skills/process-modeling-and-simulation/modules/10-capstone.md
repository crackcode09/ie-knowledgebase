# Module 10 — Capstone

**Time:** 2–3 h

## Part A — Skill check

1. Name five building blocks of a discrete-event model.
2. What's the difference between verification and validation?
3. Why use common random numbers when comparing designs?
4. Give one reason a design with the lowest average lead time can be the wrong choice.
5. A failure mode drops on-time by 0.5 points in the model; the team rated it severity 9. What do you do?
6. Utilization rises from 0.75 to 0.90. By what factor does u/(1 − u) grow?

<details><summary>Answers</summary>

1. Entities, activities, resources, queues, routing, arrivals, rules, KPIs (any five).
2. Verification: the model works as intended (built right). Validation: the model represents reality well enough for the question (right model).
3. So differences come from the design rather than random luck, giving sharper comparisons.
4. The promise applies to each job; averages can hide long tails (e.g., SPT).
5. Discuss the evidence with the team, check the model's assumptions about that failure, and revise the severity if the model holds up.
6. From 3 to 9 — three times as much waiting.
</details>

## Part B — Project

Model a process you know (or extend the repair center):

1. Write the question, scope and KPIs.
2. Draw the conceptual model; list data needed and an assumptions log.
3. Build the model (adapt `procsim.py`, or use SimPy or another tool).
4. Verify (no-variation run vs hand calculation) and validate against at least one real measure.
5. Compare at least four designs, including one "unusual" idea.
6. Stress-test the best two designs (demand, variability, absence).
7. Compare at least two operating rules; write the SOP.
8. Quantify at least three failure modes and update an FMEA.
9. Build the cost–benefit table and a 7-slide story for stakeholders.

Score each item 0 (missing) / 1 (done) / 2 (done with data and clear reasoning). 14+ of 18: ready to use process modeling on real projects.
