# Statistical Quality Control

Learn the two classic tools of statistical quality control. **Statistical process control** keeps a process stable and on target. **Acceptance sampling** decides whether to accept a lot from a sample.

**Length:** about 3 days (21 contact hours), or self-paced.  
**Prerequisites:** basic algebra. A spreadsheet or Python is needed for the exercises.

## What you will be able to do

- Calculate basic statistical measures.
- Construct control charts: X̄–R, I–MR, p, c and short-run.
- Develop acceptance sampling plans and evaluate their risks.
- Explain process capability.

## Running case

**Harbor Precision** (fictional) turns steel pins (12.000 ± 0.030 mm) and assembles valve bodies. Datasets cover pin diameter subgroups, daily hardness, final-inspection defectives, casting defects, a short-run lathe, and a 100-pin capability study. The sampling examples use incoming lots of 2,000 valve seats. All data is simulated with a fixed seed.

Control-chart constants (d₂, d₃, A₂, D₃, D₄) are **computed** by the toolkit from the normal distribution, not copied from a table. `python tools/sqckit.py constants` prints them.

## Modules

| # | Module | Body of knowledge |
|---|---|---|
| 00 | [Introduction](modules/00-introduction.md) | SPC vs acceptance sampling; what SQC can and can't do |
| 01 | [Descriptive statistics](modules/01-descriptive-statistics.md) | Location, spread, shape, histograms |
| 02 | [Variation](modules/02-variation.md) | Common and special causes, tampering, rational subgroups, run rules, control vs spec limits |
| 03 | [Average and range charts](modules/03-xbar-r-charts.md) | X̄–R construction, where the constants come from, Phase I/II, interpretation |
| 04 | [Individuals and moving range](modules/04-individuals-moving-range.md) | I–MR construction, revising limits, cautions |
| 05 | [P chart and C chart](modules/05-attribute-charts-p-and-c.md) | Defectives vs defects, variable-n p chart, c and u charts, sample-size limits |
| 06 | [Short-run charts](modules/06-short-run-charts.md) | Deviation-from-nominal (DNOM) and standardized (Z) charts |
| 07 | [Process capability](modules/07-process-capability.md) | Proportion nonconforming, Cp, Cpk, Pp, Ppk, prerequisites, pitfalls |
| 08 | [Acceptance sampling: risks and OC curves](modules/08-acceptance-sampling-risks-oc.md) | Single plans, AQL/LTPD, producer's and consumer's risk, OC curves, plan design |
| 09 | [AOQ, AOQL, ATI, ASN and the ANSI standard](modules/09-aoq-asn-ati-standards.md) | Rectifying inspection, double sampling, how ANSI/ASQ Z1.4 is used |
| 10 | [Capstone and skill check](modules/10-capstone.md) | Quality plan exercise, 10-question check |

**Suggested schedule:**

| Day | Modules | Topics |
|---|---|---|
| 1 | 00–03 | Statistics, variation, X̄–R |
| 2 | 04–07 | I–MR, attribute charts, short-run charts, capability |
| 3 | 08–10 | Acceptance sampling, capstone |

## Related courses

- [Charting Process Behavior](../../lean-six-sigma/charting-process-behavior/README.md): a deeper SPC course in this repo
- [Measurement & Basic Statistics](../../lean-six-sigma/measurement-and-basic-statistics/README.md): measurement systems and basic statistics
- [Applied Statistics](../../technical-skills/applied-statistics/README.md): distributions and inference

## Getting started

```bash
pip install -r requirements.txt
python tools/sqckit.py all        # every worked example (constants take a few seconds to integrate)
python tools/sqckit.py data       # regenerate data/*.csv
python tools/make_figures.py      # regenerate figures/
```

## Folder map

```
modules/     lessons
tools/       sqckit.py (constants, charts, run rules, capability, sampling plans), make_figures.py
data/        process and inspection datasets (CSV)
figures/     control charts, capability, OC/AOQ/ASN curves
solutions/   key results + facilitator notes
reference/   formulas, glossary, further reading
templates/   control-chart worksheet, reaction plan, capability report, sampling-plan worksheet
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
