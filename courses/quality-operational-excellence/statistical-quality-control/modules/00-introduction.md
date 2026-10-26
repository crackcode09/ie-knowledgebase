# Module 00 — Introduction to Statistical Quality Control

## Objectives

- Distinguish statistical process control (SPC) from acceptance sampling.
- Explain what SQC can and cannot do for quality.
- Meet the running case and the course map.

## Two complementary tools

| | Statistical process control (SPC) | Acceptance sampling |
|---|---|---|
| Looks at | the **process**, over time | a **lot** (batch) of product |
| Question | Is the process stable and on target? Has something changed? | Should this lot be accepted or rejected? |
| Timing | during production | at receiving, between operations, before shipment |
| Main tools | control charts, capability indices | sampling plans, OC curves |
| Effect on quality | prevents defects by detecting changes early | sorts lots; does not improve the process |

SPC keeps a process running the way it was designed to run. It **cannot fix a poor design**: a stable process with specifications it can't meet will make defects consistently. Capability analysis (Module 07) tells you which situation you're in.

Acceptance sampling is a **decision rule** with known risks. It is useful when 100 % inspection is impractical, destructive or too costly, or when you have no information about a supplier's process. As process control improves, sampling should give way to supplier certification and process data.

## Running case

**Harbor Precision** (fictional) turns steel pins (diameter spec 12.000 ± 0.030 mm) and assembles small valve bodies. Data in `data/`:

| File | Used in |
|---|---|
| `capability_study.csv` — 100 consecutive pins | 01, 07 |
| `pin_diameter_subgroups.csv` — 25 subgroups of 5 pins | 03 |
| `daily_hardness.csv` — one heat-treat hardness result per day | 04 |
| `valve_final_inspection.csv` — daily defectives with varying sample size | 05 |
| `casting_defects.csv` — surface defects per casting | 05 |
| `short_run_lathe.csv` — three part numbers on one lathe | 06 |

Acceptance-sampling examples (Modules 08–09) use a lot of 2,000 purchased valve seats.

All data is simulated with a fixed seed. Control-chart constants (d₂, d₃, A₂, D₃, D₄) are **computed** by the toolkit from the normal distribution rather than copied from a table:

```bash
pip install -r requirements.txt
python tools/sqckit.py constants
python tools/sqckit.py all
```

## Related course

This course covers the same SPC body of knowledge as [Charting Process Behavior](../../charting-process-behavior/README.md), more briefly, and adds acceptance sampling. Take either; the other is a useful companion.

## Check yourself

1. A supplier's lots pass sampling inspection every time, but your line still finds defects. Is that a contradiction?
2. Why can't SPC alone fix a process that makes 5 % out-of-spec parts?

<details><summary>Answers</summary>

1. No. Sampling accepts lots with some defect level with a known probability (the OC curve). It also says nothing about features not inspected or defects that appear later.
2. If the process is stable (only common-cause variation), the 5 % comes from the process itself — its spread or centering relative to the spec. Fixing it needs process change, not monitoring.

</details>
