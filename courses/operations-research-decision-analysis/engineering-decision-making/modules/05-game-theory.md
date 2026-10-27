# Module 05 — Sequential Decision Making — Game Theory

Outline items: Two-player zero-sum games · Mixed strategies for a zero-sum game · Mixed motive games

## Objectives

- Analyse two-player zero-sum games: saddle points and mixed strategies.
- Recognize mixed-motive games, including the prisoner's dilemma, and how to escape it.

## Two-player zero-sum games

Corran and a rival compete for one large OEM contract. Each chooses a tactic. The payoff is Corran's gain in contract **points** (the rival loses the same), so the game is zero-sum.

| Corran \ Rival | Price cut | New model | Hold |
|---|---|---|---|
| Price cut | 3 | −1 | 2 |
| Feature push | −2 | 4 | 1 |
| Service bundle | 1 | 0 | −1 |

- **Maximin** (Corran's guaranteed minimum with a single tactic) = −1.
- **Minimax** (the rival's guaranteed limit) = 2.
- They differ, so there is **no saddle point**: any fixed (pure) tactic can be exploited by the other side.

## Mixed strategies for a zero-sum game

Choose tactics **at random** with set probabilities, to make yourself unpredictable. Solve by linear programming: maximize v, subject to Σᵢ xᵢ aᵢⱼ ≥ v for every rival column, with Σ xᵢ = 1.

- **Corran:** price cut 60 %, feature push 40 %, service bundle 0 %.
- **Rival:** price cut 50 %, new model 50 %, hold 0 %.
- **Value of the game = +1.0 points to Corran.**

Check: against the rival's price cut, 0.6 × 3 + 0.4 × (−2) = 1.0. Against the new model, 0.6 × (−1) + 0.4 × 4 = 1.0. Against hold, 0.6 × 2 + 0.4 × 1 = 1.6 ≥ 1.

The service bundle is never optimal here: it is weak against every rival tactic.

## Mixed motive games

Most business games are **not** zero-sum: both sides can win or both can lose. Pricing for the next year, in $M profit (Corran, Rival):

| Corran \ Rival | High price | Low price |
|---|---|---|
| High price | (6, 6) | (1, 8) |
| Low price | (8, 1) | **(3, 3)** |

- "Low" is a **dominant strategy** for each firm (8 > 6 and 3 > 1), so the only Nash equilibrium is **Low/Low (3, 3)**.
- Both would be better off at High/High (6, 6). This is the **prisoner's dilemma**.

Escape routes (where legal; explicit price fixing is illegal in most countries):

- **Repetition:** in repeated play, reciprocating strategies such as tit-for-tat can sustain cooperation.
- **Changing the game:**
  - Differentiate the product, so customers stop comparing on price alone.
  - Lock in long-term contracts.
  - Compete on value (cost-to-serve, service) instead of price.

"Sequential" means one player moves first and the other responds. Analyse by **backward induction**, as in decision trees. Commitment (for example, publicly announced capacity) can change what the other side will do.

## Run it

```bash
python tools/edmkit.py zerosum
python tools/edmkit.py mixedmotive
```

## Check yourself

1. If the rival always plays "new model", what should Corran do, and what does it get?
2. Why is (High, High) not stable in the pricing game?

<details><summary>Answers</summary>

1. Feature push, for **4 points**. That is why the rival should mix, not play one tactic.
2. Each firm gains by switching to Low (8 > 6) if the other stays High. Without a way to commit or repeat the game, both drift to Low/Low.

</details>
