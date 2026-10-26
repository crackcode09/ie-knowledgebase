# Module 3 — Concept: Principles, Creativity, Benchmarking and Pugh Selection

**Time:** 3 h · **Phase:** Concept

## Learning objectives

1. State the core principles of DFSS.
2. Generate concepts using brainstorming, benchmarking and structured creativity.
3. Select a concept with a Pugh matrix.
4. Define key metrics for the chosen concept.

## 1. Core principles of DFSS

1. **Start from the customer** — every requirement traces to a need (Modules 1–2).
2. **Generate many concepts before choosing** — the first idea is rarely the best.
3. **Predict before you build** — use transfer functions, models and simulation (Modules 9–12).
4. **Design for variation** — performance must be robust to manufacturing, environment and use (Modules 4, 9, 10).
5. **Manage risk early** — FMEA and error-proofing during design (Modules 6–7).
6. **Verify with data** — pilots and tests prove the prediction (Modules 14–15).

## 2. Generating concepts

| Method | How | Watch out for |
|---|---|---|
| **Brainstorming** | Quantity first, no criticism, build on others' ideas; then cluster | Loud voices dominate — use silent idea writing first (brainwriting) |
| **Benchmarking** | Study competitors' products and best-in-class solutions in other industries | Copying instead of understanding *why* it works |
| **Functional decomposition** | Break the product into functions ("guide," "carry load," "retain lubricant"), generate options per function, combine (morphological matrix) | Combinatorial explosion — prune obviously bad combinations |
| **TRIZ** (Altshuller) | Resolve contradictions (e.g., stiffer *and* lower friction) using inventive principles | Steep learning curve |
| **Biomimicry, analogy** | How does nature or another field solve this? | — |

**The creative process** alternates **divergence** (many options, defer judgment) and **convergence** (evaluate, select). Mixing them in one meeting kills ideas early.

## 3. Pugh concept selection

Stuart Pugh's method compares concepts against a **datum** (reference — often the current design or the best competitor) criterion by criterion: **+** better, **0** same, **−** worse.

### Worked example — carriage concepts vs datum A (current ball-bushing design)

Criteria weights from QFD importance.

| Criterion (weight) | B: polymer bushing | C: recirculating ball | D: roller + wiper seal |
|---|---|---|---|
| Friction (5) | + | + | + |
| Stiffness (4) | − | + | + |
| Maintenance (3) | + | 0 | + |
| Noise (2) | + | − | 0 |
| Cost (4) | + | − | − |
| Ease of assembly (2) | + | − | 0 |
| **Σ +** | 5 | 2 | 3 |
| **Σ −** | 1 | 3 | 1 |
| **Net** | **+4** | −1 | +2 |
| **Weighted** | **+12** | +1 | +8 |

```bash
python tools/dfss.py pugh
```

**Don't just pick the winner.** Pugh is iterative:

1. B wins overall but loses on stiffness, the #2 technical requirement.
2. D is strong on stiffness and maintenance but loses on cost.
3. Ask: can we **hybridize** — B's polymer bushing with D's wiper seal and a stiffer housing? Make that concept E, use B as the new datum, and run another round.

Weighted scores are convenient but can hide a fatal weakness; check every "−" against must-be requirements.

## 4. Key metrics

For the selected concept, define the few metrics that will track design progress through to launch — usually the top CTQs from QFD, each with target, limits, measurement method and current predicted value. These feed the design scorecard (Module 8).

| Metric | Target | Limit | Predicted now |
|---|---|---|---|
| Friction force | 12 N | ≤ 15 N | 13 N (from supplier data) |
| Static stiffness | 150 N/µm | ≥ 120 | unknown → DOE (Module 9) |
| Lube interval | 10,000 km | ≥ 8,000 | unknown → reliability test (Module 15) |

## Check yourself

1. Why compare to a datum rather than score each concept 1–10?
2. In round 1, concept C has many "−". Should it be discarded?

<details><summary>Answers</summary>

1. Relative comparisons are easier and more consistent than absolute scores, and force discussion of specific trade-offs.
2. Not automatically — look at its "+" features (stiffness, friction) and whether they can be borrowed into a hybrid.
</details>
