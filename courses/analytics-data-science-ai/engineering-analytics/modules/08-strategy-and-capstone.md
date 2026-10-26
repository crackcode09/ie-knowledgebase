# Module 08 — Strategic Implications of Analytics and Capstone

## Objectives

- Identify the strategic implications of analytics for an engineering organization.
- Plan an analytics initiative from use case to deployment.
- Complete a capstone analysis on Ridgeway (or your own) data.

## Strategic implications

| Implication | What it means |
|---|---|
| **Data as an asset** | clean, shared, governed data compounds in value; treat it like equipment — maintained, owned, invested in |
| **Decision rights shift** | insight reaches the floor in real time; front-line people need authority and skills to act |
| **New capabilities** | analytics translators (people who speak both engineering and data), data engineers, citizen analysts |
| **Competitive differentiation** | better forecasts, uptime and service levels; data-based services to customers |
| **Build vs buy** | off-the-shelf analytics in ERP/MES/BI tools vs custom models; open-source tools lower the entry cost |
| **Risk and ethics** | privacy, security, model errors, over-automation; humans accountable for decisions |

## A roadmap that works

1. **Pick use cases by value and feasibility.** Score candidates on decision value, data readiness and effort; start where both value and readiness are high.
2. **Fix the data foundations** for those use cases — definitions, quality, access.
3. **Deliver a small working result fast** (weeks, not years), then scale.
4. **Embed in the process** — a model nobody uses is worth zero; change the standard work, meeting or system.
5. **Measure value** — downtime avoided, inventory reduced, forecast error cut.
6. **Build skills** — basic data literacy for many, deeper skills for a few.

Use `templates/use-case-canvas.md` to score and plan a use case.

## Capstone

Choose **one** question (Ridgeway or your own data) and produce a 2-page summary plus a short presentation:

| Option | Question | Techniques |
|---|---|---|
| A | How should Ridgeway serve its customer segments? | SQL summaries, k-means, profiles, recommendations |
| B | Which machines should maintenance inspect this week, and what threshold minimizes cost? | classification, confusion matrix, cost-based threshold |
| C | What will sales be next quarter, and how confident are we? | Holt-Winters, holdout MAPE, range |
| D | How many of each kit should we build next week if CNC capacity rises 10 %? | LP, shadow prices |
| E | Which inventory items deserve tight control? | ABC (+ criticality), policy by class |

**Deliverable checklist:**

- [ ] The decision and its owner, stated first
- [ ] Data source, grain, quality checks and limitations
- [ ] Method and why it fits
- [ ] Results with honest uncertainty (holdout tests, intervals)
- [ ] Recommendation, expected value, and how it will be embedded and monitored
- [ ] One or two clear visualizations (Module 01)

## Review questions

1. Name the four types of analytics with an example each.
2. Why can 95 % accuracy be a bad result?
3. What is a star schema, and why is it used?
4. How do you choose k in k-means?
5. What does a shadow price tell a manager?
6. Why compare forecasts with a naive benchmark on a holdout?
7. Give two technologies that make Big Data processing possible.

<details><summary>Answers</summary>

1. Descriptive (sales by family), diagnostic (why energy rose), predictive (failure in 30 days), prescriptive (optimal product mix).
2. When the event is rare: a model that never predicts it can be 95 % accurate and useless. Look at recall, precision and costs.
3. A fact table of events with measures, linked to dimension tables of attributes; it makes analytical queries simple and fast.
4. Compare silhouette (or within-cluster error) across k, then pick the k that also gives interpretable, actionable segments.
5. How much the objective would improve with one more unit of a constrained resource — the most it is worth paying for that unit.
6. To prove the model adds value on data it hasn't seen; in-sample fit always looks better.
7. Distributed storage and parallel processing (e.g. Spark-style engines), columnar storage, stream processing, cloud elastic compute.

</details>
