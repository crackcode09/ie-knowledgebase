# Module 1 — Writing Effective Problem Statements

**Time:** 40 min

## Learning objectives

1. Write a problem statement that is specific, measurable and free of causes and solutions.
2. Use 5W2H and Is / Is-Not analysis to bound a problem.

## 1. What makes a good problem statement

| Good | Bad |
|---|---|
| Describes the **gap** between actual and expected | Vague ("quality is poor") |
| Measurable, with a time frame | Contains a cause ("…because of the new tool supplier") |
| States the impact | Contains a solution ("We need a new leak tester") |
| Specific product, process, location | Blames people |

**Template:** *Since [when], [what object] has shown [what defect/gap] at [where], at a level of [how much / how often] versus [expected], costing [impact].*

> **Example:** Since week 1, valve-body leak-test rejects in the machining cell have averaged 10.6 per week versus a goal of 3, costing about $1,500 per week in scrap, and two customers have reported field leaks.

## 2. 5W2H

| Question | Answer (valve case) |
|---|---|
| What? | Valve bodies fail the helium leak test |
| Where? | Machining cell, leak tester LT-1; detected at test, also at two customers |
| When? | Since week 1; no clear time-of-day pattern yet |
| Who? | All shifts (to be verified) |
| Which? | Part family VB-200; all three machines (to be verified) |
| How much? | 85 leak rejects in 8 weeks (42.5% of all scrap) |
| How (detected)? | End-of-line leak test; customer complaints |

## 3. Is / Is-Not analysis

Comparing where the problem **is** with where it **could be but is not** narrows the search fast.

| | Is | Is not | Distinction → clue |
|---|---|---|---|
| What | Leaks at the seal seat | Leaks at threads or castings | Seat finishing operation |
| Where | Mostly MC3 (verify — Module 8) | Mostly not MC1, MC2 | What's different about MC3? |
| When | Spread across weeks | Not a single bad week | Not a one-off material lot |
| Extent | Some parts from each machine | Not every part, not every day | Something that varies part to part over time — tool wear? |

## Check yourself

Rewrite: "The new leak tester is rejecting too many parts because operators aren't loading them right."

<details><summary>Answer</summary>

"Since [date], leak-test rejects on VB-200 have been [x per week] versus [goal], costing [$]." The cause (loading) and the implied blame are removed; the tester's accuracy and loading are hypotheses to test, not facts.
</details>
