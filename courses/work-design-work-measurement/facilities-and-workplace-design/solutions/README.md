# Solutions and Facilitator Notes

All values come from `python tools/fwdkit.py all` (data seed 2028).

## Key results

| Example | Result |
|---|---|
| P–Q (03) | 230,580 units/yr; 13 of 40 SKUs = 80 %; F1 57.1 %, F3 34.8 %, F2 6.3 %, F4 1.8 % of units |
| Loads (03, 05) | F1 6,586; F2 7,235; F3 2,003; F4 1,062 loads/yr |
| Inventory (04) | Median 37.1 days on hand; 296.3 → 86.8 m³ at 10 days; 330 → 97 pallet positions; warehouse 93.1 m² with 3-high racks |
| Usage (04) | A = 2 items (60.3 % of picks), B = 4 (27.3 %), C = 24 (12.4 %) |
| Space (06) | 12 planning units total 1,341.8 m² of 2,000 m² |
| Affinities (06) | A: PNT–ASM, PUN–BRK; E: RCV–SHR, BRK–WLD, ASM–TST, SHR–PUN; X: WLD–PNT |
| Layout (08) | As-is 5.67 M load-m ($68,035), 10 backtracks → A 2.10 M ($25,187, −63.0 %, 3 backtracks, 7 exchanges) → **B (paint stays) 2.15 M ($25,788, −62.1 %, 4 backtracks)**; wall-box route 345.8 → 115.8 m |
| Cells (09) | ROC → 3 cells; 6 exceptional elements (P01/P07/P10:BRK, P03/P09:SHR, P05:PUN) |
| Cell capacity (11) | Takt 94.3 s; punch 70.0 s/pc, 82.5 % (bottleneck); 1 of each machine |
| People (11) | 120 s manual + 12 s walk = 132 s → 1.40 → 2 operators per shift |
| Balance (14) | Op 1: OP10–30 = 70 s; Op 2: OP40–60 = 74 s; 97.3 % |
| Configurations (15) | Straight 25.0 m / 20.8 s; L 21.5 m / 17.9 s; U 14.0 m / 11.7 s |
| Scheduling (13) | Punch spare 13,090 s/day; EPEI 1.1 days; 33 kanbans |
| Capstone (16) | Takt 77.5 s (1 shift); punch 48 s, 68.8 %; 0.77 → 1 operator; 11 kanbans |

## Facilitator notes

- **Module 03:** make learners compute loads before they look at flows. The F2 (floor cabinet) surprise is the point.
- **Module 06:** argue the ratings in groups. The reasons column matters more than the letters.
- **Module 07:** have teams draw the relationship diagram by hand before showing the figure.
- **Module 08:** let teams build their own grid layouts and score them with `flow_cost()`. Then discuss why B beats A in practice.
- **Module 11:** emphasise the setup term. Ask what happens to the punch at a lot size of 50.
- **Module 14:** the compensation discussion depends on local labor relations. Keep it about principles.
- **Module 15:** run a tape-on-the-floor mock-up of the U-cell if space allows.
