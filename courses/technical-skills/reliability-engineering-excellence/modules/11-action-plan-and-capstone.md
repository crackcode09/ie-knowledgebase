# Module 11 — Applied Exercises, Action Plan and Review

## Objectives

- Combine the course tools into a reliability improvement plan for a real line.
- Report the plan out in business terms.
- Review the course body of knowledge.

## Part A — Line A reliability plan (team exercise)

Using the Lakeshore data, build a 90-day plan. Suggested structure (`templates/action-plan.md`):

1. **Where are the losses?** Downtime and cost Pareto by asset and failure mode (Module 05).
2. **Which assets matter most?** Criticality ranking and risk matrix (Module 01).
3. **What are the failure patterns?** Exponential for the coolant pump, normal for wheels, Weibull for spindle bearings (Modules 05–06).
4. **Strategy by failure mode** (Modules 04, 09, 10).
5. **Root causes** for the top modes (Module 08).
6. **Economics** of each action (Module 07).
7. **Metrics** to track (Module 03).

### A model answer (abbreviated)

| # | Action | Basis | Expected effect | Owner | Due |
|---|---|---|---|---|---|
| 1 | Spindle: online vibration sensor + monthly analysis; planned rebuild window 3,500–5,500 h; lubrication standard | Weibull β 1.81; PM optimum 4,420 h; RCA (contaminated grease) | most of 119 h/yr bearing downtime converted to planned work | Reliability eng. | 30 days |
| 2 | Press: oil analysis monthly; seal installation standard and tooling; RCA on pump wear | 133 h downtime; seal leaks frequent | fewer leaks; early warning on pump | Maint. supervisor | 45 days |
| 3 | Coolant: install standby pump; Δp-based filter changes; level-alarm function test | pump random (β ≈ 1); filters most frequent mode; hidden alarm failure | pump outages ≈ 0 production impact | Maint. eng. | 60 days |
| 4 | Replace coolant pumps at end of life with sealed premium model | LCC: NPV +$65,600, payback 1.1 yr | lower LCC | Purchasing + reliability | on failure |
| 5 | Conveyor: autonomous-maintenance checks for belt tracking; operator training | 11 tracking failures | fewer short stops | Production lead | 30 days |
| 6 | Grinding wheels: change at 4,400 parts (1 % risk) | normal life model | fewer burn scrap events | Process eng. | 14 days |
| 7 | Work-order failure codes and closing review | data quality | better analysis next year | Maint. planner | 30 days |

**Metrics:** Line A unplanned downtime hours (lagging), MTBF for spindle and press (lagging), PdM route compliance and % of faults found before failure (leading), RCA actions closed on time (leading).

## Part B — Report-out

Present the plan to plant leadership in 10 minutes (see the Technical Communications course for structure). Lead with the ask and the value: hours of downtime avoided, dollars, risk reduced. Keep Weibull plots and calculations in the appendix.

## Part C — Review questions

1. Define reliability and name its four elements.
2. What does β < 1 tell you, and what should you avoid doing?
3. A line has three machines in series with R = 0.95, 0.90 and 0.98. System R? What happens if the 0.90 machine gets a parallel twin?
4. MTBF 800 h, MTTR 4 h. Inherent availability?
5. Name the seven RCM questions in short form.
6. Why is the P-F interval the basis for inspection frequency?
7. Option X costs $10,000 more and saves $3,000 a year for 8 years at 10 %. NPV and payback?
8. What makes a failure "hidden," and what task type addresses it?
9. Give the physical, human and latent cause for a motor that failed after a pressure washer was used on it.
10. Name the five PdM technologies covered and one failure each detects.

<details><summary>Answers</summary>

1. The probability that an item performs its intended function, under stated conditions, for a stated time: probability, function, conditions, time.
2. Infant mortality (decreasing hazard). Avoid age-based replacement — it resets units to the riskiest period. Look at installation, quality and start-up practices.
3. 0.95 × 0.90 × 0.98 = 0.838. With a parallel twin: 1 − 0.1² = 0.99 → 0.95 × 0.99 × 0.98 = 0.922.
4. 800 / 804 = 99.50 %.
5. Functions; functional failures; failure modes; failure effects; failure consequences; proactive tasks and intervals; default actions.
6. It is the warning time that the technology provides; inspecting at about half of it ensures detection with time to act.
7. NPV = −10,000 + 3,000 × 5.335 = **+$6,005**; payback 3.33 years.
8. Its failure is not evident to operators under normal conditions (e.g. a standby pump or a protective device). Failure-finding tasks — periodic functional tests.
9. Physical: water ingress → winding insulation failure. Human: motor washed directly with a high-pressure jet. Latent: no cleaning standard identifying protected equipment; motor enclosure not specified for washdown.
10. Vibration (bearing defects), thermography (loose electrical connections), oil analysis (wear metals/contamination), ultrasound (air leaks, lubrication state), motor circuit analysis (winding insulation faults).

</details>
