# Module 10 — Using CoQ to Select and Manage Improvement Projects

## Objectives

- Turn cost drivers into a ranked portfolio of improvement projects.
- Estimate savings, payback and ROI.
- Manage projects so that CoQ savings are real and verified.

## From drivers to projects

For each major driver: annual cost × expected reduction = expected annual saving. Compare with one-time cost.

Ellison's candidate portfolio (annual failure cost = 2 × months 1–6 driver cost):

| Project | One-time cost | Annual driver cost | Expected reduction | Annual saving | Payback (months) | First-year ROI |
|---|---|---|---|---|---|---|
| Port orientation: error-proof fixture | $9,000 | $113,200 | 90 % | $101,880 | 1.1 | 1,032 % |
| Rod seal leak: install tool + seal supplier change | $38,000 | $450,500 | 65 % | $292,825 | 1.6 | 671 % |
| Weld porosity: gas-flow monitoring + welder certification | $62,000 | $490,460 | 70 % | $343,322 | 2.2 | 454 % |
| Bore tolerance: in-process gauging on hone | $85,000 | $600,540 | 60 % | $360,324 | 2.8 | 324 % |
| Paint line: pretreatment control | $24,000 | $62,640 | 50 % | $31,320 | 9.2 | 30 % |
| **Portfolio** | **$218,000** | | | **$1,129,671** | | |

These returns look extraordinary — and quality projects often do pay back fast — but they rest on **estimated reductions**. Treat them as a ranking tool, then prove them with pilots.

## Selection criteria beyond payback

- **Size of prize** (annual saving) — bore tolerance has the largest.
- **Speed and certainty** — error-proofing (port orientation) is fast and almost certain.
- **Customer impact** — rod seal leaks escape to customers most; that also affects hidden costs.
- **Resources and capability** — how many projects can the team run well at once?
- **Strategic fit** — a key customer's complaint may override the ranking.

A reasonable plan: start the port-orientation fixture immediately (quick win), and run rod seal and weld porosity as the first two full projects, with bore tolerance next.

## Managing CoQ projects

1. **Charter** each project with the CoQ baseline for its driver (see Quality Engineering Essentials).
2. **Define how savings will be measured** — which ledger elements and event codes, which months, how volume changes are normalized.
3. **Agree with finance** what counts as a saving: **hard** (cost leaves the books — scrap, warranty) vs **soft** (capacity freed, time saved — real only if redeployed or used).
4. **Account for added costs** — the prevention spending the project adds.
5. **Track monthly** and verify after 3–6 months; close the project only when the driver cost is down and controls are in place.
6. **Avoid double counting** — two projects can't both claim the same scrap reduction.

## Run it

```bash
python tools/coqkit.py projects
```

## Check yourself

1. Why normalize savings for volume?
2. A project frees 300 hours of inspector time a year but nobody leaves or moves. Hard or soft saving?
3. Which project would you start first, and why?

<details><summary>Answers</summary>

1. If production rises 20 %, scrap dollars may rise even as the scrap rate falls; compare cost per unit or % of sales.
2. Soft — it becomes hard only if the time is redeployed to work that would otherwise cost money, or headcount/overtime falls.
3. The port-orientation fixture: lowest cost, fastest payback and near-certain effect — it builds credibility while the larger projects run. (Answers emphasizing the largest prize — bore tolerance — or customer impact — rod seal — are defensible if argued.)

</details>
