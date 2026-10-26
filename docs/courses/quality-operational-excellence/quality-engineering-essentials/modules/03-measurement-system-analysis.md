# Module 03 — Measurement System Analysis

## Objectives

- Treat measurement as a process with its own variation.
- Use a cause-and-effect matrix to focus data collection.
- Run and interpret a variable gauge R&R and an attribute agreement analysis.
- Plan data collection and sampling, and establish baseline performance.

## Measurement is a process

Observed variation = true part-to-part variation + measurement variation. If the gauge varies too much, you can't see the process, can't trust SPC, and may scrap good parts or ship bad ones.

**Properties of a measurement system:**

| Property | Meaning | How assessed |
|---|---|---|
| Resolution | smallest readable increment (aim for ≤ 1/10 of tolerance or process spread) | gauge spec |
| Accuracy / bias | average reading vs a reference value | calibration, bias study |
| Linearity | bias across the range | linearity study |
| Stability | bias over time | control chart of a reference part |
| Repeatability | same operator, same part, repeated | gauge R&R |
| Reproducibility | different operators (or setups) | gauge R&R |

**Calibration** ensures accuracy against traceable standards at set intervals; it does **not** prove the gauge is precise enough for the job — that's what gauge R&R does.

## Cause-and-effect matrix: what should we measure?

Score each input (X) by how strongly it affects each output (Y), weighted by the Y's importance (e.g. 0 / 1 / 3 / 9). The top-scoring X's get measured. At Bayline, the team rated tool wear, coolant temperature, machine offset and insert bar stock hardness against OD, thread quality and burr. Tool wear, coolant temperature and machine scored highest — so those were recorded with every sample. (`templates/ce-matrix.csv`)

## Variable gauge R&R (crossed ANOVA method)

Design: **10 parts** spanning the process range × **3 operators** × **3 trials**, randomized, blind (`data/gauge_rr.csv`). The ANOVA separates variance components:

| Source | % study variation |
|---|---|
| Repeatability (equipment) | 9.5 % |
| Reproducibility (operators + operator × part) | 13.5 % |
| **Total gauge R&R** | **16.5 %** |
| Part-to-part | 98.6 % |

- % tolerance (6σ_GRR / 0.050 mm): **23.7 %**
- Number of distinct categories (ndc): **8**
- Operator means: Ana 6.35046, **Ben 6.35260**, Cai 6.34988 mm

![Gauge R&R](../figures/03_gauge_rr.png)

**Commonly used guidelines** (e.g. the automotive MSA reference manual — check your customer's requirements): < 10 % acceptable; 10–30 % may be acceptable depending on the application and cost; > 30 % unacceptable; ndc ≥ 5.

**Interpretation:** marginal — acceptable for SPC (ndc 8) but using almost a quarter of the tolerance. **Reproducibility dominates**, and the operator-by-part plot shows Ben reads about 0.002 mm high on every part. Likely cause: measuring force or micrometer technique. Action: standard method (ratchet stop, measuring position), retrain, repeat the study. Fixing reproducibility is cheaper than a better gauge.

(The interaction term was significant here, p = 0.003, so it stays in the model.)

## Attribute agreement analysis

Thread damage is judged visually (pass/fail). 30 inserts (12 deliberately borderline) × 3 inspectors × 2 trials, against an expert standard (`data/attribute_msa.csv`):

| Inspector | Within-inspector agreement | Agrees with standard (both trials) | Kappa vs standard |
|---|---|---|---|
| Dee | 83.3 % | 80.0 % | 0.71 |
| Eli | 73.3 % | 70.0 % | 0.61 |
| Fay | 66.7 % | 60.0 % | 0.46 |

All three inspectors agreed with the standard on only **40 %** of parts.

Kappa (agreement beyond chance): a common guideline treats ≥ 0.9 as excellent, 0.7–0.9 acceptable, < 0.7 needing improvement. **This inspection is not reliable**: thread-damage defect counts from it can't be trusted, and customers may be receiving damaged threads that "passed." Actions: boundary samples (limit samples) at each station, better lighting/magnification, training — or replace visual judgement with a go/no-go thread gauge.

## Data collection and sampling plan

Before collecting baseline data, write a plan (`templates/data-collection-plan.md`): what to measure, operational definition, gauge, who, when, how many, how recorded, and which stratification factors (machine, shift, tool age, coolant temp) to capture alongside.

**How many?**

| Goal | Formula | Bayline result |
|---|---|---|
| Estimate mean OD within ±0.002 mm (95 %) | n = (1.96 σ / E)² | 49 inserts (σ = 0.00709) |
| … within ±0.001 mm | | 193 |
| Estimate a ~5 % defect rate within ±2 points | n = 1.96² p(1 − p) / E² | 457 |
| … within ±1 point | | 1,825 |

Attribute data need far larger samples — another reason to measure OD.

## Baseline performance

From the 480-insert sample (after the MSA fixes were in place for OD):

| Metric | Baseline |
|---|---|
| % defective | 8.33 % |
| Defects per unit (DPU) | 0.0833 |
| DPMO (5 opportunities per insert) | 16,667 |
| First-pass yield | 91.67 % |
| Sigma level (short-term convention, adding a 1.5σ shift) | 3.63 |
| OD Ppk (overall) | 0.577 |

The "1.5 sigma shift" in sigma-level tables is a convention, not a law; report DPMO and Ppk directly as well.

## Run it

```bash
python tools/qekit.py grr
python tools/qekit.py attribute
python tools/qekit.py sample_size
python tools/qekit.py baseline
```

## Check yourself

1. A gauge is calibrated monthly. Does that mean it's adequate for SPC?
2. Gauge R&R is 45 % of tolerance, with repeatability 42 %. Where do you look?
3. Why choose parts spanning the process range for a gauge study?

<details><summary>Answers</summary>

1. No. Calibration addresses accuracy (bias); gauge R&R addresses precision (repeatability and reproducibility) relative to the tolerance and process variation.
2. The gauge itself or the fixture/part setup: equipment variation (wear, resolution, clamping, part form error at the measuring point, temperature).
3. To assess whether the system can distinguish parts across the range it will see; a narrow set of parts makes %study variation look worse and ndc lower, and hides linearity problems.

</details>
