# Module 8 — Building a Persuasive Case for Stakeholders

**Time:** 45 min

## Learning objectives

1. Turn model results into a cost–benefit comparison.
2. Present a model-based recommendation that earns buy-in.

## 1. Cost–benefit

Late jobs cost about $180 each (courier upgrade, customer credit — illustrative). The center handles ~12,500 jobs a year.

```bash
python tools/procsim.py business
```

Current: **1,412 late jobs/year**.

| Option | Late/yr | Saving/yr | Annual cost | One-time cost | Net/yr | Payback |
|---|---|---|---|---|---|---|
| B +1 repair tech | 1,037 | $67,500 | $65,000 | — | $2,500 | — |
| C Cross-trained pool | 925 | $87,750 | $18,000 | $51,000 | $69,750 | 8.8 months |
| E Stock fast-moving parts | 850 | $101,250 | $10,000 | $40,000 | $91,250 | **5.3 months** |
| F Pool + stock parts | **700** | **$128,250** | $28,000 | $91,000 | **$100,250** | 10.9 months |

(Annual costs: tech salary; cross-training skill premium; 25% carrying cost on $40k of parts. One-time: training, tooling, initial parts stock. All illustrative.)

**Recommendation:** start with **E** (fastest payback, no hiring), then add cross-training (**F**) — the best net benefit and the most resilient design (Module 5). Hiring alone (B) barely pays.

## 2. Telling the story

1. **The problem in the customer's terms:** 1 job in 9 misses same-day; 1,400 late jobs a year.
2. **Why intuition fails:** static map says 1.7 h; reality 4.8 h average, long tail. Show the histogram.
3. **Validation:** the model reproduces the last three months.
4. **Options tested:** six designs; the obvious one (hire) is not the best.
5. **Robustness:** F holds up under +10% demand; current design doesn't.
6. **Risks:** what the model says matters (absence, surges) and what doesn't (the rig).
7. **Money and plan:** payback, phased plan, triggers, and how results will be tracked.

## 3. Earning trust

- Involve the technicians in building and validating the model.
- Show the assumptions log; invite challenges.
- Let stakeholders propose a scenario and run it live — "build to think" in the meeting.
- After implementation, compare actual results with the prediction and publish them.

## Check yourself

Why show the validation step to managers who only want the answer?

<details><summary>Answer</summary>

Without evidence that the model reproduces reality, its predictions are just another opinion; validation is what makes the recommendation credible.
</details>
