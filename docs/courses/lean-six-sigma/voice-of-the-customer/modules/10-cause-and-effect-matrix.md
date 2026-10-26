# Module 10 — Cause-and-Effect Matrix

**Time:** 45 min

## Learning objectives

1. Use a cause-and-effect (C&E) matrix to prioritize the process inputs that most affect the customer's CTQs.

## 1. Method

1. List the key outputs (CTQs) across the top; weight each by customer importance (from VOC; e.g., 1–10).
2. List process inputs (Xs) down the side — from the process map and fishbone.
3. Rate how strongly each input affects each output: **0, 1, 3, 9** (none, weak, moderate, strong) — the spread makes strong relationships stand out.
4. Score each input: Σ (output weight × rating).
5. Sort and Pareto: the top inputs go forward to FMEA, data collection, control plans.

## 2. Case — spare-parts ordering

| Input ↓ / Output → (weight) | Delivered within promise (9) | Right part first time (9) | Status visible (7) | Order in < 5 min (5) | **Score** | Cum % |
|---|---|---|---|---|---|---|
| Order entry method (web vs email) | 3 | 3 | 3 | 9 | **120** | 18.9 |
| Part-number cross-reference accuracy | 1 | 9 | 0 | 3 | **105** | 35.4 |
| Carrier selection and cut-off time | 9 | 0 | 3 | 0 | **102** | 51.5 |
| Picker training / pick verification | 1 | 9 | 0 | 0 | 90 | 65.7 |
| Stock availability (fill rate) | 9 | 0 | 1 | 0 | 88 | 79.5 |
| ERP-to-customer status integration | 1 | 0 | 9 | 1 | 77 | 91.7 |
| Credit hold process | 3 | 0 | 3 | 1 | 53 | 100.0 |

Example: order entry = 9×3 + 9×3 + 7×3 + 5×9 = **120**.

```bash
python tools/voc.py cematrix
```

**Reading:** the order-entry method touches every CTQ (emailed orders are re-keyed, delayed, and invisible to the customer) — it tops the list even though it's not the strongest driver of any single output. Cross-reference data and carrier cut-off follow. Five inputs cover ~80% of the weighted impact.

**Watch out:** an input with a single strong (9) relationship to a must-be CTQ can matter more than its total suggests — e.g., ERP status integration is the only strong driver of status visibility, the need with the biggest satisfaction gap (Module 5). Read the matrix, don't just sort it.

## 3. What happens next

- Top inputs → FMEA (how can each fail?) and data collection (verify the ratings).
- Ratings are team judgment; confirm the important ones with data (see *Root Cause Analysis*, Modules 9–12).
- The matrix connects VOC (weights) to process control (the Xs you will monitor).

## Check yourself

Why use 0/1/3/9 instead of 1–5?

<details><summary>Answer</summary>

The nonlinear scale separates strong relationships from weak ones, so the inputs that really matter rise clearly to the top instead of everything scoring in the middle.
</details>
