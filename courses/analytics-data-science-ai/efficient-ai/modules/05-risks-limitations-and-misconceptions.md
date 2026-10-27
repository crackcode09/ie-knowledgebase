# Module 05 — Risks, Limitations, and Misconceptions

Why AI initiatives fail, including data issues, trust, bias, and adoption challenges, and how to overcome these risks with Lean principles.

## Objectives

- Recognize the common misconceptions and failure modes of AI initiatives.
- Evaluate a GenAI pilot against explicit acceptance criteria.
- Apply Lean countermeasures to de-risk adoption.

## Misconceptions

| Misconception | Reality |
|---|---|
| "AI is objective" | It learns the patterns, and biases, in historical data |
| "More data fixes everything" | Bad or unlabelled data at scale is still bad data |
| "It works in the demo, so it works" | Demos use clean, chosen examples. Test on your own messy cases |
| "Once it's built, it's done" | Processes and data change; models drift and need monitoring |
| "AI will replace the process expert" | Experts are needed to define, label, review and improve |
| "Accuracy is the measure" | Business value and the cost of errors are the measures (Module 03) |
| "GenAI knows our business" | It only knows what it is given (documents, context) plus general training. It can fill gaps with fluent fabrication |

## Why initiatives fail

| Failure mode | Typical sign | Lean countermeasure |
|---|---|---|
| **Wrong problem** | No baseline; "AI strategy" with no customer | Problem statement, value-stream map (Module 02, 04) |
| **Data issues** | Months of cleaning; missing labels | Data readiness check before committing (Module 06) |
| **Trust** | Users double-check everything, or ignore the tool | Pilot with users; show evidence; transparent confidence and sources |
| **Over-trust (automation bias)** | Users accept wrong outputs without checking | Standard work for review; error-proofing; spot audits |
| **Bias and fairness** | Different error rates across groups (customers, applicants, sites) | Test outcomes by group; keep high-stakes decisions (hiring, credit) with people |
| **Security and privacy** | Sensitive data in uncontrolled tools | Approved tools, data classification, access control |
| **Adoption** | Tool built, nobody uses it | Co-design with frontline users; fit the tool into the existing workflow; measure usage |
| **No owner after the pilot** | Model decays; nobody retrains it | Control plan: owner, monitoring, retraining trigger |

## Evaluating a GenAI pilot: the knowledge assistant

Halvorsen piloted a document-search assistant (idea #11). Two reviewers graded 60 test questions (`data/assistant_pilot_eval.csv`):

| Grade | Count |
|---|---|
| Correct | 44 |
| Partly correct | 7 |
| Incorrect | 4 |
| Said it did not know | 3 |
| **Fabricated a source** | **2** |

The acceptance criteria, agreed **before** testing, were at least 85 % correct and at most 2 % fabricated sources:

| Measure | Result | 95 % interval | Target | Pass? |
|---|---|---|---|---|
| Correct | 73.3 % | 61–83 % | ≥ 85 % | **No** |
| Fabricated source | 3.3 % | 0.9–11 % | ≤ 2 % | **No** |

Breaking the results down shows where the problem is:

- When the answer **was** in the documents: **80.8 %** correct (52 questions).
- When it **wasn't** (8 questions): only **25 %** correct. Both fabrications happened here.

**Decision:** not ready for unsupervised use. Countermeasures:

- Make "I don't know" the expected response when no source is found.
- Show the source passage with every answer.
- Clean up and fill gaps in the document library.
- Keep a human check for safety-critical instructions.
- Re-test on a new set of questions.

With 60 questions the intervals are wide. Size the test set to the precision you need.

## Run it

```bash
python tools/aikit.py genai_eval
```

## Check yourself

1. Why agree acceptance criteria before testing?
2. Which Lean tool addresses automation bias?

<details><summary>Answers</summary>

1. To avoid moving the goalposts after seeing results, and to force a conversation about what error rate is acceptable for this use.
2. Error-proofing (poka-yoke) and standard work for review: for example, requiring the reviewer to confirm the source passage before an answer is used for a safety-critical step.

</details>
