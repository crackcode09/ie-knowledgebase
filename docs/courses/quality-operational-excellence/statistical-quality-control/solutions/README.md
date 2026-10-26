# Solutions and Facilitator Notes

All values come from `python tools/sqckit.py all` (data seed 1931).

## Key results

| Example | Result |
|---|---|
| Constants | n = 5: d₂ 2.326, d₃ 0.864, A₂ 0.577, D₃ 0, D₄ 2.114. These match published tables |
| Descriptive (01) | Mean 12.00647, median 12.0066, SD 0.00564, skew 0.027, Shapiro–Wilk p 0.891 |
| X̄–R (03) | Phase I limits: X̄ from 11.99759 to 12.01230; R UCL 0.02695. Signals at subgroups 19, 21, 22 and 25; run rules fire from 21. The shift is about +0.008 mm |
| I–MR (04) | Limits 55.480 to 60.146 HRC; MR UCL 2.866. Day 17 signals. Revised limits: 55.863 to 59.549 |
| p chart (05) | p̄ 3.832%. UCL 8.12% at n = 180 and 7.05% at n = 320. Day 21 (8.64%) is above its UCL of 7.71% |
| c chart (05) | c̄ 4.633, UCL 11.09. Casting 12 signals. Revised c̄ 4.345, UCL 10.60 |
| DNOM (06) | Center +0.00316 mm, limits −0.00757 to +0.01390. Run 20 (P-095) signals |
| Capability (07) | Cp 1.838, Cpk 1.442, Pp 1.772, Ppk 1.389, about 15 ppm. About 0.1 ppm if centered. Cpk would be 0.89 if the +0.009 shift persisted |
| OC (08) | Plan (80, 2): P(accept) 0.953 at 1%, 0.134 at 6%. Producer's risk 4.7%, consumer's risk 13.4% |
| Design (08) | AQL 1% with α 5% and LTPD 6% with β 10% → n = 110, c = 3. Tightening LTPD to 4% → n = 198, c = 4 |
| AOQ (09) | AOQL about 1.64% at about 2.8% incoming. ATI 169, 494 and 1,280 at 1%, 2% and 4% |
| Double (09) | Plan (40, 0, 2; 80, 4): OC close to (80, 2); ASN 45–69 |

## Facilitator notes

- **Day 1:** have learners compute one subgroup mean and range and one set of limits by hand before using the tool.
- **Module 02:** a live tampering demonstration works well. Learners "adjust" a dice-rolling process after each roll and see the spread grow.
- **Module 03:** stress reading the R chart first. Ask what changed at subgroup 19 before revealing the cause.
- **Module 05:** the moving limits on the p chart confuse people at first. Compare day 21 against a fixed limit to show why the adjustment matters.
- **Module 07:** the centering lesson (Cp 1.84 vs Cpk 1.44) is the money shot. A setting change is worth more than a new machine here.
- **Modules 08–09:** let learners change n and c and watch the OC curve move. The "sample 10% of each lot" myth is worth debunking explicitly.
- **ANSI/ASQ Z1.4:** bring a licensed copy if possible. The course does not reproduce the tables.
