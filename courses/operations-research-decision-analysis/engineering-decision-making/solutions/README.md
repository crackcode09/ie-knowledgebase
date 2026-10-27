# Solutions and Facilitator Notes

All values come from `python tools/edmkit.py all` (data seed 2030).

## Key results

| Example | Result |
|---|---|
| AHP (02) | Weights cost 0.351, accuracy 0.189, MTBF 0.351, time 0.109; CR 0.004; scores C 0.336 > B 0.234 > A 0.227 > D 0.203 |
| MAUT, swing weights (02) | Weights accuracy 0.357, cost 0.286, time 0.214, MTBF 0.143; B 0.790 > D 0.713 > A 0.529 > C 0.500 |
| Voting (02) | Plurality C (3); Borda B 16; Condorcet B; Kemeny-Young B>D>A>C (29); majority judgement B (Very good) > A > D > C (Poor) |
| Elicitation (03) | Lognormal σ 0.429; mean 5,481; P(< 4,000) 0.30 |
| Calibration (03) | 9 of 24 hits (37.5 % vs 80 %); p ≈ 0.00001 |
| Dominance (04) | B FSD A and D; A FSD D; B vs C none; C P(loss) 18.6 % |
| Tree and utility (04) | EMV C 2.40, B 2.20; at R = 10: CE C 0.51, B 2.09; switch R ≈ $103 M |
| Zero-sum (05) | No saddle point (maximin −1, minimax 2); Corran 60/40/0; rival 50/50/0; value +1.0 |
| Mixed motive (05) | Nash Low/Low (3,3); dominant strategy Low |
| Search (06) | Reservation $90.95k; 3.65 quotes expected; expected total $90.95k |
| Secretary (06) | n = 20: k = 7, P(best) 0.384 exact (0.379 simulated) |
| Value of information (07) | EVPI $2.40 M; P(fav) 0.44; posteriors 0.727 / 0.143; EVII $1.40 M; net $1.2 M |
| ROC (08) | AUC 0.89; best threshold 2.4 mm/s: 41/50 detected, 147 false alarms, $297.6k; PPV 22 % |
| Sensitivity (09) | Break-even P(strong) 0.381; all five inputs can flip the decision |

## Facilitator notes

- **Module 02:** run the vote live with the class before revealing the methods. Plurality vs Borda usually surprises people.
- **Module 03:** give a 10-question calibration quiz (general-knowledge quantities, 80 % intervals). Most groups hit 40–60 %.
- **Module 04:** ask each participant for their own 50/50 gamble indifference to estimate R.
- **Module 05:** play the pricing game for several rounds with real stakes (points) to show the escape from the dilemma through repetition.
- **Module 08:** have groups pick an alarm threshold before showing the costs, then again after.
- **Module 09:** use a real (anonymized) decision from the participants' organizations for the decision journal exercise.
