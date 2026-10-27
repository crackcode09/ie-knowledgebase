# Module 07 — Value of Information

Outline items: Expected value of perfect information · Expected value of imperfect information

## Objectives

- Compute the expected value of perfect information (EVPI) as an upper bound on what information is worth.
- Compute the expected value of imperfect (sample) information with Bayes' theorem, and decide whether to buy it.

## Expected value of perfect information

If Corran knew the market state **before** choosing:

- strong market → choose C (10.5)
- weak market → choose B (1.0)

EV with perfect information = 0.4 × 10.5 + 0.6 × 1.0 = **4.80**. Without information, EMV = 2.40 (choose C).

**EVPI = 4.80 − 2.40 = $2.40 M.** No study, however good, is worth more than this.

## Expected value of imperfect information

A market study costs **$0.2 M**. Its reliability:

- P(favourable result | strong market) = 0.80
- P(favourable result | weak market) = 0.20

Bayes' theorem:

| Quantity | Value |
|---|---|
| P(favourable) = 0.4 × 0.8 + 0.6 × 0.2 | **0.44** |
| P(strong \| favourable) = 0.32 / 0.44 | **0.727** |
| P(strong \| unfavourable) = 0.08 / 0.56 | **0.143** |

Decisions after the study:

- **Favourable:** EMV(C) = 0.727 × 10.5 + 0.273 × (−3) = 6.82; EMV(B) = 3.18. **Choose C.**
- **Unfavourable:** EMV(C) = 0.143 × 10.5 + 0.857 × (−3) = −1.07; EMV(B) = 1.43. **Choose B.**

EV with the study = 0.44 × 6.82 + 0.56 × 1.43 = **3.80**.

- **EVII = 3.80 − 2.40 = $1.40 M**, against a cost of $0.2 M. **Net value $1.2 M: do the study.**

Information has value **only if it can change the decision**. Here it does: a favourable result points to C, an unfavourable one to B. If the study could never change the choice, its value would be zero, however interesting the result.

## When is more information worthwhile?

1. Compute EVPI. If even perfect information is worth less than the cost, **stop**.
2. Spend on reducing **epistemic** uncertainty in the inputs the decision is **sensitive** to (Module 09's tornado).
3. Compare EVII with the cost **and the delay**. Information that arrives after the decision is worthless.

## Run it

```bash
python tools/edmkit.py voi
```

## Check yourself

1. If the study were less reliable (0.6 / 0.4), would it still change the decision?
2. Why is EVPI always at least as large as EVII?

<details><summary>Answers</summary>

1. P(fav) = 0.4 × 0.6 + 0.6 × 0.4 = 0.48; P(strong | fav) = 0.24 / 0.48 = 0.50 → EMV(C) = 3.75 vs B 2.5: choose C. P(strong | unfav) = 0.16 / 0.52 = 0.308 → EMV(C) = 1.15 vs B 1.92: choose B. So it still changes the decision. EV = 0.48 × 3.75 + 0.52 × 1.92 = 2.80, so **EVII ≈ 0.40**: still worth $0.2 M, but only just.
2. Perfect information always tells you the right choice, while imperfect information sometimes misleads. The value of any information is bounded by the value of perfect information.

</details>
