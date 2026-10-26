# Module 18 — Capstone: Four Case Files

**Time:** 2–3 hours

Each case puts a process "on trial." For each one, write a one-page case report:

1. **The charge:** the practical question, H₀ and Hₐ, one- or two-sided, α.
2. **The evidence:** plot the data; check the assumptions.
3. **The test:** which test and why (Module 17).
4. **The verdict:** reject / fail to reject, p-value, confidence interval.
5. **The sentence:** the practical decision — and whether the result is practically significant.
6. **Possible errors:** which error type could you have made, and how likely is it given the power?

Solutions are in `solutions/README.md` — try first.

---

### Case A — The coolant change

Production wants to switch to a more expensive coolant if it extends tool life by at least 30 parts per edge. Ten inserts were run with each coolant on the same machine, same material lot.

Data: `data/case_a_tool_life.csv` (parts per edge).

---

### Case B — The careless carrier?

Logistics suspects one of three carriers damages more shipments. Last quarter:

| Carrier | Shipments | Damaged |
|---|---|---|
| Carrier 1 | 240 | 9 |
| Carrier 2 | 260 | 11 |
| Carrier 3 | 230 | 10 |

Data: `data/case_b_carrier_damage.csv`

---

### Case C — Does the training pay off?

Ten inspectors' average time to inspect a standard part was recorded before and after a measurement-technique course. The training manager claims it cuts inspection time.

Data: `data/case_c_inspection_time.csv` (minutes)

---

### Case D — Is the CMM biased?

A 50.000 mm certified master block was measured 12 times on the CMM. The lab wants to know whether the CMM has a bias. The master's calibration uncertainty is ±0.0005 mm.

Data: `data/case_d_master_block.csv`

---

## Rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Hypotheses | Missing or reversed | Correct but sidedness unjustified | Correct, sidedness justified before data |
| Test choice | Wrong test | Right test, no reasoning | Right test with assumption checks |
| Calculation | Wrong | Minor error | Correct, with CI |
| Interpretation | "Accept H₀" / p as probability H₀ is true | Statistically correct | Statistical **and** practical conclusion |
| Error analysis | Missing | Error type named | Error type + power or CI reasoning |

8–10 points per case: ready to run tests on a project team.
