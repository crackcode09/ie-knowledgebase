# Module 10 — Capstone: An EPM Proposal for Larkfield

## Brief

You are the analytics lead. Prepare a 20-minute proposal for Larkfield's leadership that integrates the course's methods.

## Tasks

1. **Strategy:** improve the strategy map and scorecard. Remove any operational PIs that crept in, and add one key risk indicator.
2. **Profitability:** using `tools/epmkit.py`, summarize channel and customer profitability. Choose three actions and estimate their value.
3. **Retention:** use the churn model to name the five highest-risk accounts and the service drivers behind them. Estimate the value of raising distributor retention by 5 points.
4. **Budget:** rebuild the operational budget for a +12 % growth scenario with no extra web growth. Compare the separate-team and pooled staffing.
5. **Risk:** propose a mitigation for the top risk and show how it changes the P10 of operating profit. (Hint: lower its probability in `data/risk_register.csv`, then re-run `montecarlo`.)
6. **Adoption:** a 4-quarter roadmap with the barriers you expect.

<details><summary>Key values</summary>

**Task 2**

- Distributors carry $2.06 M of the $2.27 M profit.
- Web loses $0.15 M on 83 % cost-to-serve.
- Direct accounts carry $1.28 M of cost-to-serve, driven by visits and specials.
- Actions (one version):
  - minimum web order value: about +$184k
  - price engineering specials at their activity cost of $3,349 each
  - visit planning by account value

**Task 3**

- Highest predicted churn: C22 (0.69), C01 (0.57), C32 (0.44), C28 (0.43), C04 (0.43).
- Drivers: high support calls per order, returns and late deliveries, and few years as a customer.
- +5 points of distributor retention ≈ **+$82k CLV per distributor**.

**Task 4**

- `python -c "import sys; sys.path.insert(0,'tools'); import epmkit as e; print(e.ex_budget(growth=0.12, web_shift=0.0))"`
- Result: 29.71 FTE in total; 32 staff as separate teams; **30 pooled**.

**Task 5**

- Results depend on the mitigation assumed.
- Example: dual-sourcing cuts R1's probability from 0.15 to 0.05. Compare P10 and expected loss before and after, and set that against the mitigation cost.

</details>

## Skill check

1. Name the difference between a strategic KPI and an operational PI.
2. What are the two stages of ABC/M cost assignment?
3. Why does charging overhead by revenue distort customer profitability?
4. Write the CLV formula used in this course.
5. Why is accuracy a poor measure for a churn model with a 15 % base rate?
6. Give two reasons driver-based budgets beat incremental ones.
7. What should a make-or-buy decision compare a supplier's price with?
8. Name the four types of adoption barrier.

<details><summary>Answers</summary>

1. A KPI measures progress on a strategic objective (few, periodic, for executives). A PI monitors a process (many, frequent, for teams).
2. Resources → activities (resource drivers); activities → cost objects (activity drivers).
3. Cost isn't proportional to revenue. Small, service-heavy customers consume more activity per dollar of revenue.
4. CLV = Σₜ profit × retentionᵗ⁻¹ ÷ (1 + r)ᵗ.
5. Predicting "nobody churns" already scores 85 %. Use AUC and top-decile capture instead.
6. They follow the volume drivers and mix, and they make capacity steps and levers visible. (They also cut negotiation and gaming.)
7. The **avoidable** cost of the activity, not its full ABC cost.
8. Technical, perception, model design and cultural.

</details>
