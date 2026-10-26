# Module 10 — Capstone: Plan Reviewers and the Permit Counter

## Objective

Apply the full process to two more Tri-County roles and write a staffing recommendation.

## Brief

The director now wants answers for **plan reviewers** and **permit technicians**:

- Plan reviewers: 6 on staff. Commercial resubmittals (55 % of reviews) are high, and a pre-application meeting program could cut them to 35 %.
- Permit technicians: 4 on staff. A new online permit portal is expected to cut counter arrivals by **30 %**. Back-office processing per permit stays the same.

Use `templates/staffing-model-workbook.xlsx` (sheet `ReviewerModel`), or `tools/stmkit.py`, together with the course data.

## Tasks

1. **Scope and definitions.** List the workload drivers, units and service levels for both roles. Which data types (Module 02) are weakest?
2. **Plan reviewer demand.** Compute required FTE for 2026–2028 (base forecast), with the current resubmittal rates and with commercial resubmittals at 35 %.
3. **Plan reviewer supply.** Project supply with no hiring (quit rate from `separations_history.csv`; retirements from the roster with the course rule). Compute the gap by year.
4. **Counter demand.** Recompute counter positions by hour with arrivals × 0.7, keeping the 80 %/10 min target. What is the new permit technician FTE?
5. **Sensitivity.** Which input most affects the reviewer result? (Hint: look at how the resubmittal rows were measured.)
6. **Recommendation.** In one page, answer first: hires, redeployments, improvement projects and the measures to watch.

## Rubric

| Area | Meets the standard when you… |
|---|---|
| Definitions | Give clear units, service levels and data weaknesses |
| Demand | Get the arithmetic right; use available hours; state indirect shares |
| Supply | Use the quit rate, retirements and new-hire productivity; give year-by-year results |
| Queueing | Recompute positions per hour against the target, rather than scaling linearly |
| Judgment | Recognize that SME-based resubmittal times need validating; combine improvement with hiring |
| Communication | Write one page, answer first, with numbers and a range |

<details><summary>Capstone key (run <code>python tools/stmkit.py capstone</code>)</summary>

- **Reviewer demand (base):** 6.29 / 6.50 / 6.71 FTE in 2026–2028. With commercial resubmittals at 35 %: **6.07 / 6.26 / 6.47**, saving about 0.2 FTE a year.
- **Reviewer supply, no hiring:** effective 5.6 / 5.0 / 4.4. The gap is **−0.7 / −1.5 / −2.3**. The quit rate (6.7 %) is higher than for inspectors, and one reviewer (age 60, 21 years) is retirement-eligible now.
- **Counter:** positions by hour go from 2-3-3-3-4-4-3-2 (24 position-hours) to 2-2-3-3-3-3-2-2 (**20**). Technician FTE falls from **3.99 to 3.41**. Position-hours drop by only 17 % for a 30 % drop in arrivals, because of the minimum of 2 positions and the waiting-time target.
- **Sensitivity:** the commercial review and resubmittal times. Commercial review is ±9 % precise from time records, and resubmittal times are SME estimates. Time-study a sample of resubmittals before acting on small differences.
- **Recommendation (one version):**
  - Hire 1 plan reviewer in 2026 and plan for 1 a year after that, adjusted for actual quits. Hires of 1/1/1 give effective FTE of 6.3 / 6.6 / 7.0 against a need of 6.29 / 6.50 / 6.71.
  - Start the pre-application program to cut resubmittals.
  - After the portal launches, move about 0.5 FTE of technician time to permit pre-screening or inspection scheduling, rather than cutting a position, while the counter's new demand settles.
  - Watch: resubmittal rate, counter wait times, reviewer backlog days.

</details>

## Final skill check

1. Name the seven data types this course uses.
2. Write the workload-driven FTE equation.
3. What is a relief factor, and why is it above 1?
4. Why does a queueing model give more staff than workload alone?
5. Give two reasons why benchmarks are a check and not a model.
6. Why do new hires count as less than one FTE in their first year?
7. What does the back-test in Module 08 show, and why is it persuasive?
8. Name three levers other than hiring that close a staffing gap.

<details><summary>Answers</summary>

1. Workload volume; work content (unit times); activity profile; availability; service and policy requirements; workforce supply; performance and cost.
2. FTE = Σ(volume × unit time) ÷ unit-driven share ÷ available hours per FTE.
3. The FTE needed to keep one post covered: hours to cover ÷ available hours. It is above 1 because people aren't available every paid hour (holidays, leave, training).
4. Random arrivals bunch up. Meeting a waiting-time target needs spare capacity, so servers can't be 100 % busy.
5. Peers differ in methods, travel, mix and service level. A peer group can be under-staffed too. Benchmarks don't explain why a number differs.
6. Hiring lag, training and learning. They aren't productive from day one, and they also take mentors' time.
7. When required FTE exceeds staff on hand, service falls (r = −0.97, about −7 points per 0.1 of ratio). It links the model to an outcome leaders already care about.
8. Any three: retention, method improvement (routing), reducing failure demand (re-inspections, resubmittals), cross-training and redeployment, contract or overtime capacity, changing the service level.

</details>
