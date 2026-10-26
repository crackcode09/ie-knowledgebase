# Solutions and Instructor Notes

Module check and quiz answers are inside the modules. Running-case results (regenerate with `python tools/voc.py data` then `python tools/voc.py all`):

| Item | Result |
|---|---|
| Survey | 300 responses: MRO 150, distributors 90, OEMs 60 |
| Segment attractiveness | MRO 53, distributors 41, OEMs 38 |
| Biggest importance–satisfaction gaps | Status visibility 1.44; fast delivery 1.28 |
| Kano | Order tracking must-be (41%, worse −0.74); same-day shipping one-dimensional (42%); photo part-finder attractive (57%); consignment stock indifferent (66%) |
| NPS | −24 (promoters 22.7%, detractors 46.7%) |
| Status-visibility satisfaction | 16.3% ± 4.2 overall; segment MOEs 5.9–9.4 points |
| Sample sizes | ±5 → 385; ±5 of 1,200 → 292; ±10 → 97 |
| Acceptable delivery | MRO median 3 days (25% satisfied by 5 days; 99% by 2); distributors median 6; OEMs median 9.5 |
| C&E matrix top inputs | Order entry method 120; cross-reference accuracy 105; carrier cut-off 102 |

## Teaching notes

- **Module 3:** have learners classify a few answer pairs by hand before showing the counts.
- **Module 6:** run `python tools/voc.py sim` with different n (edit `ex_sim`) to show MOE shrinking with √n.
- **Module 9:** discuss the cost of a 2-day spec for MRO (VOB) and whether the process can deliver it (VOP) — VOC is necessary but not sufficient.
- **Module 10:** challenge the 0/1/3/9 ratings — which ones should be checked with data first?
