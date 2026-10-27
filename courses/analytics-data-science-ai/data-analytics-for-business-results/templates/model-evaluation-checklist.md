# Model evaluation checklist

- [ ] The decision the model supports is written down
- [ ] Every input is known at prediction time (no leakage)
- [ ] Tested on data not used for training (time-based split for anything over time)
- [ ] Compared with a naive baseline and with today's practice
- [ ] Metrics chosen for the decision (for rare outcomes: recall, precision, AUC — not accuracy alone)
- [ ] Threshold chosen by cost / value, not left at 0.5
- [ ] Residuals or errors checked by group (branch, segment, period)
- [ ] Inputs and outcomes checked for unfair treatment of groups
- [ ] Owner, monitoring measure and retraining trigger agreed
