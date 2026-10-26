# Formulas and Cheat Sheet

| Item | Formula |
|---|---|
| Available hours per FTE | paid hours − holidays − leave − training − other non-available time |
| Unit-driven hours | Σ volumeᵢ × (unit timeᵢ + travel per unitᵢ) / 60 |
| Unit-driven share | unit-driven ÷ (unit-driven + allowed indirect), from work sampling |
| Required FTE (workload) | unit-driven hours ÷ unit-driven share ÷ available hours |
| Required FTE (fixed indirect %) | unit hours ÷ (1 − indirect share) ÷ available hours |
| Relief factor | hours a post must be covered ÷ available hours per FTE |
| Coverage FTE | posts × relief factor |
| Ratio FTE | supported FTE ÷ span of control |
| Offered load (Erlangs) | a = λ × mean service time (same time unit) |
| Erlang C (probability of waiting) | C(c,a) = [aᶜ/c! · c/(c−a)] ÷ [Σₖ₌₀ᶜ⁻¹ aᵏ/k! + aᶜ/c! · c/(c−a)] |
| Service level | P(wait ≤ t) = 1 − C(c,a) · e^−(cμ − λ)t |
| Server utilization | a ÷ c |
| Unit-time precision (95 %) | ± 1.96 · SD / (mean · √n) |
| Sample size for ±e precision | n = (1.96 · SD / (e · mean))² |
| Work sampling CI for a share p | ± 1.96 · √(p(1 − p)/n) |
| Log-trend growth per year | e^(12·b₁) − 1 (b₁ = monthly slope of ln volume) |
| Effective FTE in a year | average headcount + new hires × first-year productivity |
| Gap | effective supply − required demand (negative = shortage) |
| Overtime hourly cost | wage × premium (1.5) |
| Staffing ratio | required FTE ÷ FTE on staff |

## Rules of thumb used in this course (not universal)

- Measure unit times to about ±5–10 % for activities that drive most of the hours.
- Plan permanent staff to the annual average and cover peaks with flexible capacity, unless the service policy says otherwise.
- Present a range (scenarios or Monte Carlo percentiles), not a single number.
