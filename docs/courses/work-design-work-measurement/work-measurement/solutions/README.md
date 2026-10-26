# Solutions and Facilitator Notes

All values come from `python tools/wmkit.py all` (data seed 1911).

## Key results

| Example | Result |
|---|---|
| Time study (05, 08) | Normal time 108.36 s. Standard 117.86 s (15% PF&D on manual elements) = 1.964 min. 30.5 pumps per hour; 229 per shift. 124.61 s if the allowance is applied to all elements |
| Foreign element (05) | Cycle 9, element E3: 48.5 s (dropped bit), excluded |
| Cycles (05) | E3 needs 17–20 cycles and E5 needs 19–22 (14 and 15 were taken); the other elements are sufficient |
| Methods (02–03) | Operator idle 45 of 108 s. Doing manual work during the leak test gives a standard of about 72.9 s (−38%) |
| Rating (06) | Analyst B biased −6 points, C +5, D inconsistent (SD 10.1); A on target |
| Allowances (07) | 15% of normal time vs 15% of workday (= 17.65% of normal time) |
| Labor (09) | Department efficiency 99.5%, utilization 82.0%, productivity 81.6%. OP7 at 89.5% efficiency. About 230 off-standard hours, led by waiting for parts |
| Work sampling (11) | Picking 47.7%, walking 16.5%, searching 7.8%. Picking share needs 1,065 observations for ±3 points. Daily p chart is stable |
| Sampling standard (11) | 2.181 min per kit (current method); 1.524 min with walking and searching removed |
| Standard data (12) | Normal min = 0.516 + 0.087·items + 0.741·heavy. R² 0.993. 24-item heavy crate: 3.35 normal, 3.85 standard |
| Learning (13) | On an 85% curve, a new operator reaches the standard at about unit 26. First 100 units take 209.5 planning minutes |
| Staffing (13) | 3.86 → 4 operators. Takt 64.3 s. Improved method needs about 2.4 operators |

## Facilitator notes

- **Module 03 before Module 05:** ask the group to time the present method first, then reveal the worker–machine chart. Learners see that a precise standard for a poor method is the wrong goal.
- **Module 05:** give the raw cumulative readings and have learners compute element times by hand for two cycles.
- **Module 06:** if possible, show real rating clips (walking, card dealing) and run the calibration exercise live.
- **Module 07:** the two allowance conventions cause frequent real-world errors, so make learners compute both.
- **Module 09:** the "efficiency 99.5% but productivity 81.6%" contrast is the key lesson. The problems are in the system, not with the people.
- **Ethics:** discuss real situations where standards were misused and how to rebuild trust.
