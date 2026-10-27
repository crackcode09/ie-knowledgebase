# Module 10 — Capstone: Corran's Drive-Technology Decision

## Brief

Prepare a decision memo and a 15-minute briefing for Corran's product council that integrates the course.

## Tasks

1. **Frame:** fundamental and means objectives; at least one new alternative generated from the means objectives.
2. **Evaluate:** MAUT with swing weights (and AHP for comparison); explain any difference in rank.
3. **Group:** propose the voting rule for the council and justify it.
4. **Uncertainty:** check the demand assessment for overconfidence (Module 03), then widen the P10–P90 by 30 % and re-run the dominance analysis.
5. **Decide:** decision tree with the market study; choose with expected utility at R = $10 M.
6. **Value of information:** EVPI and EVII; decide on the study.
7. **Risk plan:** potential problem analysis for the chosen design; the warning threshold and how you will communicate it.
8. **Learning:** what the decision journal records, and which assumption the post-launch review checks first.

<details><summary>Key values</summary>

- **MAUT:** B 0.790 > D 0.713 > A 0.529 > C 0.500. AHP (ratings mode) puts C first because of proportional normalization of accuracy.
- **Voting:** plurality gives C (3 of 7); Borda, Kemeny-Young and majority judgement all give **B**. B is the Condorcet winner.
- **Calibration:** past 80 % intervals hit only 37.5 % of the time, so widen the ranges.
- **Dominance:** B first-order dominates A and D; B vs C is not dominated either way.
- **Tree:** EMV(C) 2.40 vs B 2.20; CE at R = $10 M: B 2.09 vs C 0.51, so **choose B** unless R > ~$103 M.
- **Information:** EVPI $2.40 M; study EVII $1.40 M vs cost $0.2 M, so **do the study**: launch C if favourable, B if unfavourable. With a risk-averse utility, recheck the post-study choice (CE of C given a favourable result).
- **Risk:** alarm threshold 2.4 mm/s (41 of 50 detected, 147 false alarms, expected cost $297.6k).
- **Sensitivity:** break-even P(strong) 0.381. Check the market assumption first.

</details>

## Skill check

1. Fundamental vs means objective: give one of each for a decision of your own.
2. Why is plurality voting risky with several alternatives?
3. What does first-order stochastic dominance let you conclude?
4. Define the certainty equivalent and the risk premium.
5. What is the value of a mixed strategy in a zero-sum game?
6. State the secretary-problem stopping rule.
7. When is the value of information zero?
8. Why might the cost-optimal alarm threshold produce more false alarms than detections?
9. Why judge decisions by process rather than outcome?

<details><summary>Answers</summary>

1. Answers vary. For example: fundamental = minimize total cost of ownership; means = use standard parts.
2. A candidate can win with a minority of first choices even when most voters rank it last (a polarizing option).
3. Everyone who prefers more to less prefers the dominant alternative, regardless of risk attitude.
4. CE = the sure amount equal in utility to the gamble. Risk premium = EMV − CE.
5. The expected payoff a player can guarantee by randomizing optimally, whatever the opponent does.
6. Observe and reject about n/e candidates, then accept the first that beats all seen so far.
7. When no possible result would change the decision.
8. Because misses cost far more than false alarms, and failures are rare.
9. Outcomes include luck. A good process with good information can still meet a bad outcome, and vice versa.

</details>
