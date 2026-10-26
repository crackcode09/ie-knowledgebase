# Module 00 — Staffing Models in Human Capital Management

## Objectives

- Place staffing models within a human capital management (HCM) framework and planning cycle.
- Explain what a staffing model answers, and what it doesn't.
- Describe the course case and the questions executives are asking.

## Human capital management

**Human capital management** is the planning, hiring, development, deployment and evaluation of an organization's people so that it can deliver its mission.

Public agencies in the United States work within a defined framework. The U.S. Office of Personnel Management's **Human Capital Framework** groups HCM into four systems across a plan → implement → evaluate cycle ([OPM, Human Capital Framework overview](https://www.opm.gov/policy-data-oversight/human-capital-framework/tabs/overview/)):

| Phase | System | Staffing-model link |
|---|---|---|
| Plan | **Strategic Planning & Alignment** | How many people, in which roles, to meet mission goals |
| Implement | **Talent Management** | Recruiting, hiring and training plans sized by the model |
| Implement | **Performance Culture** | Workload and productivity measures, and expectations |
| Evaluate | **Evaluation** | Comparing service results with staffing; keeping the model current |

OPM's page cites 5 CFR Part 250, Subpart B as the governing regulation. Private companies use similar cycles under other names, such as strategic workforce planning or headcount planning.

## The workforce planning cycle

```
 1 Set direction ──► 2 Analyze demand ──► 3 Analyze supply ──► 4 Gap analysis
   (mission,          (STAFFING MODEL:     (current staff,       (demand − supply,
    service goals)     workload → FTE)      attrition, hiring)     by role and year)
        ▲                                                               │
        │                                                               ▼
 7 Evaluate & update ◄── 6 Implement ◄──────────── 5 Action plan
   (service vs staffing,   (hire, train, redeploy,   (hiring, overtime, redesign,
    refresh the model)      change methods)           budget request)
```

A **staffing model** sits at step 2. It converts the **work the organization must do** into the **number of people needed**. Its output feeds:

- **Budgeting.** FTE × loaded cost is defensible, because it is tied to workload.
- **Hiring and recruiting.** How many, which roles and when, allowing for lead times.
- **Training.** Training capacity for new hires, and the productivity ramp.
- **Performance measurement.** Workload per FTE and service levels against staffing.
- **Strategic planning.** What-if scenarios for growth, new programs and technology.

## What a staffing model is not

- **It isn't the budget.** It says what the work requires. Leaders still decide what to fund, and what service level to accept if they fund less.
- **It isn't a productivity target for individuals.** It sizes the workforce, not each person's daily quota.
- **It isn't permanent.** Workload, methods and policies change, and so must the model (Module 08).
- **It isn't only arithmetic.** It depends on agreed definitions of work, service levels and available time. Those are management decisions, not data.

## Mission-critical occupations

Staffing models matter most when too few staff in an occupation directly harms the mission: air traffic controllers, nurses, safety inspectors, emergency dispatchers, maintenance technicians on critical equipment. In these occupations:

- **Under-staffing** shows up as delays, backlogs, safety risk and overtime burnout.
- **Over-staffing** is hard to undo and draws budget away from other needs.
- Hiring and training lead times are long, so decisions must be made **ahead** of demand.

A U.S. National Academies report on facilities staffing at the Veterans Health Administration is a public example of this kind of work. It covers workload and infrastructure parameters, non-available time, KPIs and annual review ([NASEM 2020, *Facilities Staffing Requirements for the Veterans Health Administration*](https://www.nationalacademies.org/read/25454/chapter/6)).

## Running case: Tri-County Building Safety

**Tri-County Building Safety** (fictional) is a public agency that reviews construction plans, issues permits and inspects construction for three counties.

| Role | On staff (Jan 2026) | Work |
|---|---|---|
| Inspector | 21 | Residential and commercial inspections, re-inspections, complaints |
| Plan reviewer | 6 | Residential and commercial plan reviews and resubmittals |
| Permit technician | 4 | Permit counter and back-office permit processing |
| Supervisor | 4 | Supervision (policy span of control 1:9) |

The director's questions:

1. Builders complain that inspections take days in summer. **Are we short of inspectors, and by how many?**
2. What will we need in **2026–2028** as construction grows?
3. How many people must we **hire each year**, given retirements, quits and training time?
4. What will it **cost**, and what happens if we don't fund it?

All data is simulated with a fixed seed (2027).

## Run it

```bash
python tools/stmkit.py data     # regenerate the datasets
python tools/stmkit.py all      # every worked example
```

## Check yourself

1. At which step of the cycle does a staffing model sit, and which two steps does it feed directly?
2. Give one reason why a staffing model is not the same as a budget.
3. Why do long hiring and training lead times make staffing models more important?

<details><summary>Answers</summary>

1. Step 2, demand analysis. It feeds gap analysis (step 4) and the action plan and budget (step 5). Through evaluation (step 7) it is also updated by service results.
2. The model states what the workload requires. The budget is a decision about how much to fund, which may accept a lower service level or other trade-offs.
3. Someone hired today may not be fully productive for a year. Decisions must anticipate demand, which needs a forecast-driven model rather than reacting to backlogs.

</details>
