# Module 1 — Basic Statistical and Lean Six Sigma Terms

**Time:** 30 min

## Learning objectives

1. Use core statistical vocabulary correctly.
2. Communicate using common Lean Six Sigma terminology.

## 1. Statistical terms

| Term | Meaning | Example |
|---|---|---|
| **Population** | Every item you want to draw conclusions about | All shafts this lathe will make this year |
| **Sample** | The subset you actually measure | 100 shafts measured this week |
| **Parameter** | A number describing the population (usually unknown) | True process mean μ |
| **Statistic** | A number computed from the sample | Sample mean x̄ = 12.7001 mm |
| **Variable** | A characteristic that varies | Diameter, defect type, cycle time |
| **Observation** | One recorded value | Part 17: 12.704 mm |
| **Distribution** | The pattern of how values are spread | Mound-shaped, skewed, bimodal |
| **Central tendency** | Where values cluster | Mean, median, mode |
| **Variation / dispersion** | How spread out values are | Range, standard deviation |

Convention: Greek letters (μ, σ) for population parameters; Latin letters (x̄, s) for sample statistics.

## 2. Lean Six Sigma terms

| Term | Meaning |
|---|---|
| **VOC** (voice of the customer) | What the customer needs, in their words |
| **CTQ** (critical to quality) | A measurable characteristic that the customer cares about, with a target and limits |
| **Specification limits** (LSL, USL) | The acceptable range for a CTQ |
| **Defect** | Any failure to meet a CTQ requirement |
| **Defective** | A unit with one or more defects |
| **Opportunity** | A chance for a defect to occur on a unit |
| **DPU** | Defects per unit = defects / units |
| **DPMO** | Defects per million opportunities = defects / (units × opportunities) × 1,000,000 |
| **Yield** | Share of units that pass; *first-pass yield* counts only those passing without rework |
| **Y = f(X)** | The output (Y) is a function of the inputs (Xs); improvement means finding and controlling the critical Xs |
| **DMAIC** | Define, Measure, Analyze, Improve, Control |
| **VOP** (voice of the process) | What the process actually delivers, shown by data and process behavior charts |

### Worked example — DPU and DPMO

500 invoices are checked; each has 6 fields that can be wrong (opportunities). 18 errors are found on 15 invoices.

- Defectives: 15 → defective rate 3.0%, yield 97.0%
- DPU = 18 / 500 = 0.036
- DPMO = 18 / (500 × 6) × 1,000,000 = **6,000**

DPMO depends heavily on how you count opportunities; only compare DPMO between processes that count them the same way.

## Check yourself

1. "Average diameter of the 30 parts measured today" — parameter or statistic?
2. A circuit board has 200 solder joints. 1,000 boards have 50 bad joints in total. DPMO?
3. What's the difference between a defect and a defective?

<details><summary>Answers</summary>

1. Statistic (it's from a sample).
2. 50 / (1,000 × 200) × 1,000,000 = 250 DPMO.
3. A defect is a single nonconformance; a defective is a unit containing one or more defects.
</details>
