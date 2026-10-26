# Solutions and Instructor Notes

Module check and skill-check answers are inside the modules. Results of the running case (`python tools/procsim.py all`, seeds fixed):

| Item | Result |
|---|---|
| Static view | Work content 1.71 h; utilization diag 0.80, repair 0.89, test 0.60 |
| Baseline (A) | 49.8 units/day; mean lead 4.80 h; p90 8.19 h; 88.7% on time (daily CI 88.1–91.1%) |
| Validation | v1 (no parts waits) 95.2% on time vs history 88%; v2 88.7% |
| Designs | B 91.7%; C 92.6%; D 90.3% (lowest mean 3.88 h); E 93.2%; F 94.4% (p90 7.06 h) |
| Resilience | A: 89.1 → 83.4 → 73.4% at +0/10/20% demand; F: 94.5 → 88.3 → 82.8% |
| Dispatch (F) | FIFO 94.4%; SPT 91.1%; PRIORITY 92.1% (contract 99.3%) |
| Test batching | batch 1/3/6: mean lead 4.08/4.23/4.58 h; on time ~94–95% |
| FMEA (F) | Demand +20% −11.7 pts; tech absent −10.6; rework doubles −3.5; parts late −2.2; rig down 2 h −0.9 |
| Business case | E payback 5.3 months; F net $100k/yr; B barely breaks even |

## Teaching notes

- The "history" values in Module 3 are illustrative; in a real project they come from the system of record over the same period.
- Costs in Module 8 are illustrative; replace with real figures before using the case for decisions.
- Results vary slightly with the number of simulated days; differences under ~1 point are within noise.
- Good live exercise: let learners propose a design, edit one `Design(...)` line and run it during class.
- The simulator assumes staff stay until all jobs are done and that a job fails test at most once (assumptions log, Module 2) — ask learners how relaxing each would change results.
