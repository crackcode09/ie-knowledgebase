# Solutions and Exercise Notes

Answers to each module's "Check yourself" questions are inside the modules. This file covers the open exercises and lists every worked result for instructors. All values come from `python tools/dfss.py all`.

## Module 12 — Exercise 12.1 (breakdowns at the drill)

Approach: inside `simulate_line`, track the drill's cumulative busy time; when it passes a randomly drawn time-between-failures (exponential, mean 480 min), add a repair delay (mean 30 min) before the next job starts. Expect average flow time to rise well above the 46 min baseline — drill utilization effectively rises from 0.80 to about 0.85 (0.80 / availability of 480/510 ≈ 0.94), and repairs add a large burst of variability. Adding a second drill drops drill utilization to ~0.43 and removes most of the queue at that station. Run several seeds and compare means and 90th percentiles.

## Worked results (instructor reference)

| Module | Result |
|---|---|
| 1 Survey | n = 385 (±5%, 95%); 260 with population 800; 1,068 (±3%) |
| 2 QFD | Friction 68 (26.3%), Lube interval 56 (21.6%), Stiffness 55 (21.2%), Noise 40, Cost 40 |
| 3 Pugh | B net +4, weighted +12; D +2 / +8; C −1 / +1 |
| 4 Capability | μ 20.004: Cp 1.25, Cpk 0.92, 2,981 DPMO; recentered: Cpk 1.25, 177 DPMO |
| 6 FMEA | RPN: preload 175, wiper seal 168, lubricant 112, holes 96, scratches 72 |
| 8 Scorecard | Total DPU 0.0182, RTY 0.982 |
| 9 DOE | Effects A 6.10, C 2.10, B −0.75, AC 0.30; model y = 15.70 + 3.05A − 0.375B + 1.05C |
| 10 Stack-up | Worst case 0.05–0.55; RSS 0.167–0.433; MC σ 0.0443 |
| 11 Kingman | 20 min (u 0.8, cₑ 0.5); 51 (u 0.9); 52 (cₑ 1.5) |
| 12 Simulation | Flow time 46.2 / 74.3 / 37.9 min; WIP 4.6 / 7.4 / 3.8 |
| 13 Balance | Takt 1.125 min; 6 stations; efficiency 78.5% |
| 15 Reliability | Weibull β 2.68, η 6,459 km, B10 2,789 km; success-run n 22 / 45 / 299 |
