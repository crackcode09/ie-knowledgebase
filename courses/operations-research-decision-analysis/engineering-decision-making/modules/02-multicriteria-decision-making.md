# Module 02 — Multicriteria Decision Making

Outline items: Analytic Hierarchy Process · Multiattribute utility theory · Swing weighting · Group decision making · Borda count · Kemeny-Young method · Majority judgement

## Objectives

- Weight criteria and score alternatives with AHP and with multiattribute value/utility models.
- Set weights by swing weighting, not by importance in the abstract.
- Combine individual preferences with Borda, Kemeny-Young and majority judgement, and see how the method changes the result.

## Analytic Hierarchy Process

AHP compares criteria **in pairs** on a 1–9 scale (1 = equal, 3 = moderately more important, 5 = strongly, 7 = very strongly, 9 = extremely). Corran's product council:

| | Cost | Accuracy | MTBF | Time to market |
|---|---|---|---|---|
| Cost | 1 | 2 | 1 | 3 |
| Accuracy | 1/2 | 1 | 1/2 | 2 |
| MTBF | 1 | 2 | 1 | 3 |
| Time to market | 1/3 | 1/2 | 1/3 | 1 |

- **Weights** = the principal eigenvector: **cost 0.351, accuracy 0.189, MTBF 0.351, time 0.109**. The geometric mean of each row, normalized, gives the same here.
- **Consistency:** λmax = 4.010, so CI = (λmax − n)/(n − 1) = 0.0035 and CR = CI/RI = **0.004**, where RI = 0.90 for n = 4 (Saaty's random index, from the literature). Below 0.10 is the usual "acceptable" rule.
- **Scoring alternatives**, ratings mode: each attribute is normalized in proportion to performance, inverted where lower is better.
- Result: **C 0.336, B 0.234, A 0.227, D 0.203**.

Why C wins under AHP: proportional normalization gives C's 2 µm accuracy **76.5 %** of the accuracy score, because 1/2 is 25 times 1/50. Whether 2 µm is really worth that much more than 10 µm is a **value question** that this normalization never asks. MAUT asks it explicitly.

## Multiattribute utility theory

MAUT builds a **value (or utility) function for each attribute**, from 0 (worst) to 1 (best), then adds them up with weights:

V(alternative) = Σ wᵢ vᵢ(xᵢ)

- Cost, MTBF and time to market: linear between the worst and best alternative.
- Accuracy: **diminishing returns** (an exponential curve). Going from 50 µm to 10 µm is worth most of the range; 10 µm to 2 µm adds little. v(10 µm) = 0.963, v(30 µm) = 0.738.

## Swing weighting

Weights must reflect **how much the swing from worst to best matters**, not how important the attribute sounds. The council imagines all attributes at their worst and asks which single swing to best it would choose first:

| Swing (worst → best) | Points | Weight |
|---|---|---|
| Accuracy 50 → 2 µm | 100 | 0.357 |
| Unit cost $880 → $410 | 80 | 0.286 |
| Time to market 14 → 6 months | 60 | 0.214 |
| MTBF 15,000 → 30,000 h | 40 | 0.143 |

**MAUT result: B 0.790, D 0.713, A 0.529, C 0.500.** The ball screw wins. The linear motor is best on accuracy and MTBF but worst on cost and time.

If the ranges change (for example, a cheaper linear motor appears), the swings change, and so must the weights. That is the "range sensitivity" that importance-only weights ignore.

## Group decision making

> The source outline lists this item as "SGroup decision making", which appears to be a typo.

Seven council members each ranked the four designs (`data/panel.csv`):

| Voters | Ranking |
|---|---|
| E1, E2, E3 | C > B > D > A |
| E4, E5 | B > D > A > C |
| E6, E7 | A > B > D > C |

**Plurality** (first choices only): C 3, B 2, A 2. C "wins" with a minority (3 of 7).

## Borda count

Points 3, 2, 1, 0 for 1st to 4th place: **B 16**, C 9, D 9, A 8. B wins: it is everyone's 1st or 2nd choice.

## Kemeny-Young method

Find the ranking that agrees with the most voter **pairwise** preferences, by checking all 24 orders:

- Pairwise wins: B beats A (5–2), C (4–3) and D (7–0). B is the **Condorcet winner**.
- Best ranking: **B > D > A > C**, agreeing with 29 pairwise preferences.

Kemeny-Young is the most defensible rank aggregation, but it gets hard to compute for many alternatives.

## Majority judgement

Voters **grade** each design (Reject, Poor, Acceptable, Good, Very good, Excellent) instead of ranking. Each design gets its **median** grade:

| Design | Median grade |
|---|---|
| B | **Very good** |
| A | Good |
| D | Acceptable |
| C | **Poor** (3 Excellent or Very good, but 4 Poor or Reject) |

Ranking B > A > D > C. Ties are broken by removing median grades one at a time.

C is **polarizing**: loved by three, rejected by the rest. Plurality picks it; every method that uses the full preferences does not.

**Lesson:** the voting rule is a decision. Agree it **before** voting, and prefer methods that use full rankings or grades.

## Run it

```bash
python tools/edmkit.py ahp
python tools/edmkit.py maut
python tools/edmkit.py voting
```

## Check yourself

1. With swing points cost 100, MTBF 80, time 60, accuracy 40, which design wins?
2. Why can AHP and MAUT rank the same alternatives differently?
3. Compute B's Borda score from the table above.

<details><summary>Answers</summary>

1. Weights become cost 0.357, MTBF 0.286, time 0.214, accuracy 0.143. Ranking **B 0.705 > A 0.629 > D 0.620 > C 0.429**: B still wins, and A moves up.
2. They score differently. AHP's proportional normalization treats ratios of attribute values as ratios of value. MAUT uses explicit value functions over the range, and swing weights tied to that range.
3. E1–E3 give B 2 each (6). E4 and E5 give 3 each (6). E6 and E7 give 2 each (4). Total **16**.

</details>
