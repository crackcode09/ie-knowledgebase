# Solutions and Instructor Notes

Module check and skill-check answers are inside the modules. Running-case results (regenerate with `python tools/lean.py all`):

| Item | Result |
|---|---|
| COPQ | $2.46M = 10.2% of sales; failure 76%, prevention 4.1% |
| Takt | 4.0 min (880 min / 220) |
| Constraint | CNC: effective C/T 4.09 min; capacity 215/day |
| VSM | 2,800 units; lead time 12.73 days; processing 19.6 min; PCE 0.18% |
| Downtime Pareto | Tool breakage 30%, changeover overrun 23%, material waits 17%, coolant 12% (83% cum.) |
| Benchmark gaps | Changeover 78%, lead time 70%, inventory turns 56% |
| Assembly balance | 295 s work, 2 operators, 61.5% |
| Bullwhip | Variance ratios 3.9×, 15.3×, 51.1× (retailer, distributor, factory) |
| Cells | Family 1: P1, P3, P5, P7, P9 on Saw, HMC-1, Deburr, Hone; Family 2: P2, P4, P6, P8 on VMC-2, Lathe, Deburr, Anodize; P10 exception |
| SMED | 90 → 50 → 20 min; EPEI 1.16 → 0.26 days |
| CONWIP | Push 204.7/day, WIP 11.6; cap 10: same throughput, WIP 8.1; cap 4: 185.4/day, backlog explodes |
| Heijunka | Pitch 44 min; 20 pitches; ABACBAABABCABAABCABA; 13 kanban cards for family A |
| TPM | MTBF 20.6 h, MTTR 2.25 h, availability 0.902; OEE 61.1% |
| Standard work | 230 s cycle vs 240 s takt |

## Teaching notes

- **Module 12:** change `lead`, `alpha` and `review` in `bullwhip()` to show how lead time and forecasting drive amplification.
- **Module 17:** run `simulate_line` with `interarrival=4.0` (bottleneck ~98% utilized): push floor WIP nearly triples (11.6 → 32.7, flow time 131 min), while a cap of 10 holds floor WIP at 10 (flow time 40 min) — but orders then wait in the backlog (lead time 446 min) and throughput slips slightly (220 → 218/day). A cap moves waiting off the floor; it doesn't create capacity.
- **Module 14:** add a row to `PPM` and re-cluster to show how one new part can break a clean cell design.
- Case figures not produced by the tools (e.g., spaghetti distances, schedule swings, benchmark values) are labeled estimated or illustrative.
