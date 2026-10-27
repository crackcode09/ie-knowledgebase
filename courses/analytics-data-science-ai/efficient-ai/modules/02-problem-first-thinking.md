# Module 02 — Problem First Thinking

Framing AI initiatives around business problems rather than technology adoption.

## Objectives

- Write a problem statement before considering any technology.
- Size the problem and define success measures in business terms.
- Choose the simplest effective countermeasure, which may not be AI.

## Start from the problem

| Technology-first (avoid) | Problem-first (do) |
|---|---|
| "We need an AI strategy" | "Invoice exceptions take 4 minutes each, 42,000 a year, and late payments cost us discounts" |
| "Let's try a chatbot" | "Technicians spend 6 minutes finding the right work instruction, 30,000 times a year" |
| "Which AI tool should we buy?" | "What is the gap, who feels it, what causes it, and how will we know it's fixed?" |

## A problem statement template

> **[Who]** experiences **[problem]** in **[process]**, happening **[how often / how much]**, costing **[time / money / quality / risk]**, because of **[known or suspected causes]**. We will know it is solved when **[measurable result by date]**.

Example (Halvorsen Components, fictional):

> Accounts-payable clerks resolve **42,000 invoice-to-PO matches a year at about 4 minutes each** (2,800 hours), mainly because of unit-of-measure and price differences. Exceptions delay payments and cost **about $15,000 a year in lost early-payment discounts**. Success: 60 % less manual matching time and no lost discounts by Q3.

## Sizing the problem

Annual value (course formula) = volume × minutes per item ÷ 60 × % time saved × loaded rate + avoidable waste ($)

Invoice matching: 42,000 × 4 / 60 × 0.60 × $48 + $15,000 = $80,640 + $15,000 = **≈ $95,600 a year**.

Size the problem **before** the solution, and use the same method for every idea so they can be compared (Module 07).

## Choose the simplest effective countermeasure

Ask in this order:

1. **Can we eliminate the work?** Remove the step, the report, the approval.
2. **Can we simplify or standardize it?** Templates, standard work, error-proofing.
3. **Can rules automate it?** Workflow, scripts, configurators.
4. **Does it need prediction or language understanding?** Then consider ML or GenAI.

At Halvorsen, 4 of 14 "AI ideas" turn out to need a process fix or rules, not AI:

- quoting standard configurations
- chasing approvals
- changeover scheduling
- applicant screening (high bias and legal risk)

## Check yourself

1. Write a problem statement for "We want AI in customer service" using the template.
2. Size: 24,000 tickets a year, 3 minutes each to triage, 50 % saved, $48/h, $10,000 of misrouting cost avoidable.

<details><summary>Answers</summary>

1. For example: "Agents manually read and route 24,000 tickets a year (about 3 minutes each); 1 in 8 goes to the wrong team, adding a day to resolution. Success: routing time down 50 % and misroutes under 3 % by Q2."
2. 24,000 × 3 / 60 × 0.5 × 48 + 10,000 = 28,800 + 10,000 = **$38,800 a year**.

</details>
