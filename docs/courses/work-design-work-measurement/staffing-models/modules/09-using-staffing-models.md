# Module 09 — Using Staffing Models: Budget, Hiring and Performance

## Objectives

- Turn model results into a budget request and a hiring plan.
- Compare overtime, hiring and contracting as ways to close a gap.
- Use the model for performance measurement and present it to executives.

## The 2026 staffing picture

| Role | On staff | Required 2026 (base) | Gap | Loaded cost/FTE | Gap × cost |
|---|---|---|---|---|---|
| Inspector | 21 | 25.12 | **−4.12** | $112,000 | −$461,600 |
| Plan reviewer | 6 | 6.29 | −0.29 | $125,000 | −$36,300 |
| Permit technician | 4 | 3.99 | 0.01 | $78,000 | +$900 |
| Supervisor | 4 | 3.93 | 0.07 | $140,000 | +$9,300 |

Loaded costs are illustrative. Use your agency's salary, benefits and overhead rates.

The model says the problem is **inspectors**. The other roles are about right, which helps credibility: the model isn't simply asking for more of everything.

## Options for the inspector gap

| Option | 2026 cost | Pros | Cons |
|---|---|---|---|
| **Overtime only** (no hiring) | 8,380 h × $54.92 = **$460,300** | Fast, no training | 8.3 h overtime per inspector per week (over 48 weeks): unsustainable; burnout raises quits, which widens the gap |
| **Hire 4/4/3 + bridge** | New hires $291,200 + bridge overtime 3,861 h ≈ **$212,100** | Closes the gap by 2027–28; sustainable | Training load; 2026 still partly short |
| **Contract inspectors for the peak** | Market rate × peak hours | Seasonal flexibility | Availability and quality vary; procurement time |
| **Accept a lower service level** | $0 | No spending | Builder delays, economic cost, safety risk |

Overtime **per hour** costs about the same as straight-time staff here: 1.5 × the wage (68 % of loaded cost) ≈ 1.02 × the loaded hourly rate. Its real cost is **fatigue, quality and quits**, which the model can show (Module 07).

**Recommendation in the course case:**

- Hire 4, 4 and 3 inspectors in 2026–2028.
- Bridge the 2026 summer peak with overtime plus contract inspectors.
- Start route optimization (−1.6 FTE potential, Module 05) and re-inspection reduction (−0.8 FTE) projects.
- If they deliver, reduce 2028 hiring.

The three-year payroll for the new hires is about $2.14 M. Much of it replaces leavers rather than adding to total payroll.

## Budget justification

A defensible staffing request links each FTE to:

1. **Workload**: volumes and forecast, from data the finance office can check.
2. **Work content**: measured unit times, with methods and precision.
3. **Availability**: actual leave and training data.
4. **Service level**: the promise being kept, and what happens without the staff (the Module 08 back-test).
5. **Alternatives considered**: overtime, contract, method improvement.

## Performance measurement

The model also supplies performance measures:

| Measure | Formula | Use |
|---|---|---|
| Workload per FTE | Unit-driven hours ÷ FTE on staff | Trend in demand per person |
| Staffing ratio | Required FTE ÷ FTE on staff | Leading indicator of service problems |
| Service level | e.g. next-day inspection % | Outcome |
| Overtime % | Overtime hours ÷ straight hours | Hidden shortage |
| Vacancy rate and time to hire | Vacant positions ÷ authorized; days from requisition to start | Supply risk |
| Unit-time drift | Audit sample vs model unit time | Model maintenance |

Report the **staffing ratio** monthly next to the service level. When it rises above 1.0, service drops about 7 points for every 0.1 (Module 08). That gives leaders warning before builders complain.

## Presenting to executives

Use one page, answer first:

> **We need 4 more inspectors in 2026, and 11 hires over three years, to restore next-day inspections.** Inspection demand has grown 2–6 % a year while inspector headcount fell from 23 to 21. In 2025, summer service fell to about 60–70 % next-day. Hiring 4/4/3, with a 2026 overtime/contract bridge (~$212k), closes the gap by 2027. Route optimization and fewer re-inspections could save 2–3 FTE. Plan reviewers, permit technicians and supervisors are right-sized.

Then supporting charts: required vs on staff with service, the supply and demand projection, and the sensitivity range. The [Technical Communications](../../technical-communications/README.md) course covers answer-first structure in detail.

## Run it

```bash
python tools/stmkit.py budget
```

## Check yourself

1. Why does the model's finding that three roles are right-sized make the inspector request stronger?
2. The council offers funding for 2 inspectors instead of 4. What do you tell them the model predicts?
3. Which performance measure would warn you earliest that the model is drifting out of date?

<details><summary>Answers</summary>

1. It shows the model isn't biased toward "more staff". It finds surpluses and balances too, so its shortage finding is more credible.
2. Two hires in 2026 give about 21.6 effective FTE against 25.1 required: a ratio of about 1.16. In the back-test, months with ratios between 1.10 and 1.22 averaged next-day service of about 76 %. Summer months would be worse. State the service level the council is choosing, rather than arguing for the number.
3. Unit-time drift from audit samples, and the gap between modelled and actual service. If the staffing ratio and the service level stop moving together, the model needs refreshing.

</details>
