# Line 3 Grinding DMAIC Project Review

## Agenda
- Background
- Define phase
- Measure phase
- Analyze phase
- Improve phase
- Control phase
- Next steps
- Questions
<!-- Today I'll walk through the whole project phase by phase so you can see everything we did, starting with the background and the define phase and ending with next steps. -->

## Define
- Project charter signed off in week 1 by the champion and process owner
- Problem: Line 3 centerless grinding scrap rate elevated vs. plant average for multiple quarters
- Goal: reduce scrap % by 50% within 6 months of project kickoff
- Scope: Line 3 only, OD grinding of inner-race blanks, all shifts
- SIPOC completed with suppliers, inputs, process, outputs, customers
- VOC from assembly: dimensional issues causing line stoppages
- Team: process engineer, quality engineer, two operators, maintenance tech, coolant vendor
<!-- The charter was signed off in week one. The problem was that Line 3 had elevated scrap compared with the plant average for several quarters, and the goal was a fifty percent reduction within six months. We kept scope to Line 3 only, all shifts. We did a SIPOC and gathered voice of the customer from assembly, who told us that dimensional problems were stopping their line. The team included engineering, quality, operators, maintenance, and the coolant vendor. -->

## Measure
- Gauge R&R on OD air gauge: 11.8% of tolerance (acceptable)
- Baseline scrap 4.46% over 13 weeks (approx. 11,800 parts)
- Defect Pareto: OD oversize 44.6%, burn 25.3%, chatter 16.2%, taper 5.8%, scratches 4.9%, other 3.2%
- Data collection plan: hourly OD checks, coolant concentration twice per shift, wheel dress log, ambient temperature
- Process capability Cpk 0.71 for OD
<!-- In measure we validated the air gauge with a gauge R and R of eleven point eight percent of tolerance, which is acceptable. Baseline scrap was four point four six percent over thirteen weeks, about eleven thousand eight hundred parts. The defect Pareto showed oversize at about forty-five percent and burn at about twenty-five percent. We collected hourly diameter checks, coolant concentration twice per shift, the dressing log and ambient temperature. Capability for diameter was a Cpk of zero point seven one. -->

## Analyze
- Multi-vari: within-shift variation dominant
- Regression OD deviation vs coolant concentration: R-sq 0.62, p < 0.001
- Coolant concentration range observed 3.1% to 7.8% (target 5%)
- Wheel dress interval varied 60 to 150 parts by operator
- Burn incidence higher when dress interval > 90 parts (chi-square p = 0.002)
- Fishbone and 5-Why completed, see appendix
<!-- Multi-vari showed most variation was within shift. Regression of diameter deviation on coolant concentration gave an R-squared of zero point six two with p less than zero point zero zero one. Concentration ranged from three point one to seven point eight percent against a five percent target. The dressing interval varied from sixty to one hundred fifty parts depending on the operator, and burn was more common above ninety parts. The fishbone and five whys are in the appendix. -->

## Improve
- Automatic coolant proportioning pump installed (holds 5.0% +/- 0.3%)
- Dress interval standardized at 40 parts via PLC counter
- In-process gauge with closed-loop compensation
- Pilot 2 weeks, then full implementation week 14
<!-- We installed an automatic proportioning pump that holds concentration at five percent plus or minus zero point three. We set the dressing interval at forty parts using a PLC counter, and added an in-process gauge that compensates the machine automatically. We piloted for two weeks and went live in week fourteen. -->

## Control
- Control plan updated
- Coolant concentration on SPC chart
- Dress counter alarm
- Scrap after: 1.99% over 13 weeks
- Cpk improved to 1.41
<!-- The control plan is updated, coolant concentration is on an SPC chart, and the dress counter alarms if skipped. Scrap after the change averaged one point nine nine percent over thirteen weeks and Cpk improved to one point four one. -->

## Next steps
- Consider rollout to other lines
- Capital required approx. $38k
- Questions?
<!-- As next steps we could consider rolling out to other lines, which would need about thirty-eight thousand dollars. Any questions? -->
