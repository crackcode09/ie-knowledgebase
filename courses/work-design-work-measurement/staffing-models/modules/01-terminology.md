# Module 01 — Terminology of Work Measurement and Staffing Models

## Objectives

- Use the core terms of work measurement and staffing models consistently.
- Convert between workload, hours and FTE.
- Spot the terminology mistakes that most often distort staffing numbers.

## Why terminology matters

Most staffing-model disputes are really about **definitions**. Does "FTE" mean paid hours or available hours? Does "inspection time" include travel? Is "workload" this year's actual volume or demand including backlog? Agree the definitions in writing before you collect any data.

## Core terms

| Term | Definition | Tri-County example |
|---|---|---|
| **Workload driver** | A countable event that creates work | A residential inspection |
| **Workload unit** | The unit the driver is counted in | One inspection stop |
| **Volume** | Number of workload units in a period | 19,711 residential inspections in 2025 |
| **Unit time** | Time to complete one workload unit by the defined method | 33.1 min on site + report |
| **Standard time** | Unit time at normal pace with allowances, from formal work measurement | Used when a time study and allowances are applied |
| **Direct (unit-driven) time** | Time spent on workload units, including travel tied to each unit | Inspecting, writing reports, driving to the stop |
| **Indirect time** | Necessary work not tied to individual units | Customer calls, meetings, administration |
| **Allowance** | Time added for personal needs, fatigue and unavoidable delay | Personal time from work sampling |
| **Non-available time** | Paid time when the person isn't at work | Holidays, leave, training |
| **Paid hours** | Hours paid per FTE per year | 2,080 (40 h × 52 weeks) |
| **Available hours** | Paid hours minus non-available time | 1,738 h per FTE |
| **FTE** | Full-time equivalent: one full-time position's paid hours | 2 half-time staff = 1 FTE |
| **Productive FTE** | FTE needed if each person is available its available hours | Required hours ÷ available hours |
| **Relief factor** | FTE needed to cover one post for its required hours | 1.15 for a counter post open 2,000 h a year |
| **Coverage (post) requirement** | Posts that must be staffed regardless of workload | Counter open 08:00–16:00 |
| **Service level** | A measurable promise to customers | 80 % of counter customers served within 10 min |
| **Span of control** | Staff per supervisor | 1:9 policy |
| **Demand** | Staff required to do the expected work at the target service level | From the staffing model |
| **Supply** | Staff available, after attrition and hiring | From the workforce projection |
| **Gap** | Supply − demand | Negative means a shortage |
| **Attrition** | Separations (quits, retirements, transfers) as a share of headcount | Inspector quits about 4.6 % a year |

## The basic equation

```
Required FTE = Σ (volume × unit time)  ÷  unit-driven share  ÷  available hours per FTE
               └── unit-driven hours ─┘   └─ adds indirect ─┘   └─ converts to people ─┘
```

Each part comes from a different data type (Module 02):

- **volume** from operational systems
- **unit time** from work measurement
- **unit-driven share** from work sampling or activity analysis
- **available hours** from leave records

## Common errors

| Error | Effect |
|---|---|
| Dividing by **paid** hours (2,080) instead of available hours (≈1,738) | Understates FTE by about 16 % |
| Counting travel in the unit time **and** as indirect time | Double-counts |
| Using **completed** work as volume while there is a backlog | Understates demand; a short-staffed unit looks right-sized |
| Treating SME estimates as standards without checking | Bias of unknown size |
| Mixing headcount and FTE | Part-timers inflate supply |
| Leaving out new-hire productivity | Overstates supply in hiring years |

## Run it

```bash
python tools/stmkit.py workload_model
```

## Check yourself

1. 41,260 hours of total work and 1,738 available hours per FTE. How many FTE? How many if you wrongly divide by 2,080?
2. Is a 10-minute coffee break indirect time, non-available time or an allowance?
3. A unit has no backlog because it stopped accepting complaint calls. Why is its completed volume a poor measure of demand?

<details><summary>Answers</summary>

1. 41,260 / 1,738 = **23.7 FTE**. With 2,080: 41,260 / 2,080 = 19.8, an understatement of about 4 FTE (16 %).
2. An **allowance** (personal time during the working day). Non-available time is time not at work at all. Indirect time is work not tied to a unit.
3. Demand that is refused or diverted never shows up in the counts. Use requests received (or estimated latent demand), not work completed.

</details>
