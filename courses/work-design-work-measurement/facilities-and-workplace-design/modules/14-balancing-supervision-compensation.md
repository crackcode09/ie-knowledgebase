# Module 14 — Balancing the Work · Supervision · Compensation and Rewards

Outline items: **Balancing the work**, **Supervision**, **Compensation and rewards**

## Objectives

- Balance cell work among operators against takt.
- Set up supervision and reward systems that support cell teamwork.

## Balancing the work

Assign operations to operators so that no one's load (manual time + walking) exceeds takt (94.3 s), and loads are as even as possible.

| Operator | Operations | Manual + walk (s) |
|---|---|---|
| 1 | OP10, OP20, OP30 | 10 + 14 + 34 + 12 = **70** |
| 2 | OP40, OP50, OP60 | 18 + 20 + 24 + 12 = **74** |

- Both are under takt.
- Balance efficiency = (70 + 74) / (2 × 74) = **97.3 %**.
- Cycle time is set by the slower operator: 74 s, below takt, which leaves room to absorb variation.

In a **U-cell**, an operator can take operations from both ends, for example OP10 and OP60 side by side. That makes more balanced assignments possible, and lets the first operator control both input and output.

## Supervision

Cells change the supervisor's job, from directing individuals to supporting a team:

| Role | Responsibilities |
|---|---|
| Cell team (both shifts) | Run the cell to takt; first-piece checks; daily 5S; record hourly output and problems |
| Cell / team leader | Covers absences, solves problems, trains, runs the start-of-shift meeting; usually works in the cell part of the time |
| Supervisor (several cells) | Resources, priorities, escalations, coaching, improvement projects |
| Support (maintenance, quality, IE) | Fast response to andon calls; reliability; standard work |

**Cross-training.** Each operator should be able to run at least two positions, and the leader all of them. Track this on a skills matrix.

## Compensation and rewards

Individual piece-rate incentives pay each person for their own output. They work against cells, where people must help each other, keep to takt rather than over-produce, and do setups and quality checks. Common alternatives:

| Approach | How it works | Strength | Risk |
|---|---|---|---|
| Base pay + skill-based pay | Pay rises with certified skills (positions mastered) | Rewards flexibility | Must be tied to real needs |
| Team gainsharing | Share labor savings vs a baseline with the team | Rewards cooperation and improvement | Baseline disputes; needs clear measures |
| Recognition | Non-cash recognition for improvement ideas and quality | Low cost, immediate | Can feel token if not sincere |

**Gainsharing example (illustrative):**

- Baseline in the functional layout: **0.065 labor h per box**.
- Cell month: 12,000 boxes in 630 labor hours (4 operators × 21 days × 7.5 h) = **0.0525 h per box**.
- Hours saved = (0.065 − 0.0525) × 12,000 = **150 h**. At $32/h, that is **$4,800**.
- 50 % to the team = **$2,400**, which is **$600 per operator** for the month.

Any change to pay needs HR, legal and (where applicable) union involvement. These figures only illustrate the mechanics.

## Run it

```bash
python tools/fwdkit.py balance
```

## Check yourself

1. Demand rises so takt falls to 70 s. Does the 2-operator balance still work?
2. Why can a piece-rate system hurt a cell even if it raises individual output?

<details><summary>Answers</summary>

1. No. Operator 2 at 74 s exceeds 70 s. Rebalance (move OP60's 24 s partly to operator 1), cut the manual content, or add a third operator.
2. It rewards each person for their own count, not for flow. Operators may build ahead of the next station (overproduction), skip setups or quality checks, and won't help a teammate who falls behind.

</details>
