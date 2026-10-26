# Design of Experiments

A free, open course on planning, running and analyzing designed experiments, so you can find the factor settings that improve quality and productivity at the lowest cost.

**Length:** about 2 days (14 contact hours) of self-study or classroom time.  
**Prerequisites:** basic statistics (means, standard deviation, hypothesis tests). See the [Applied Statistics](../applied-statistics/README.md) and [Fundamentals of Hypothesis Testing](../../lean-six-sigma/fundamentals-of-hypothesis-testing/README.md) courses in this repo.

For DOE inside a full product-design roadmap, see [Design for Six Sigma](../../lean-six-sigma/design-for-six-sigma/README.md).

## What you will be able to do

- Analyze and interpret data from designed experiments.
- Design experiments that find the best combination of factor levels to cut cost and raise quality and productivity.
- Determine operating levels for key process factors.
- Identify the critical process characteristics, the few factors that really move the response.

## Running case

Injection molding of a glass-filled nylon bearing cage. Six simulated experiments, all with fixed seeds, cover tensile strength, ejection force, cycle time, shrinkage, warpage and flash. Your numbers will match the text.

## Modules

| # | Module | Body of knowledge |
|---|---|---|
| 00 | [Why designed experiments](modules/00-why-designed-experiments.md) | OFAT pitfalls; randomization, replication, blocking; planning |
| 01 | [Single-factor design (CRD)](modules/01-single-factor-crd.md) | completely randomized design, one-way ANOVA, Tukey HSD, assumptions |
| 02 | [Randomized block design](modules/02-randomized-block-design.md) | two-factor design without interaction, blocking a nuisance factor |
| 03 | [Latin square designs](modules/03-latin-square.md) | blocking two nuisance factors in p² runs |
| 04 | [Two-factor factorial with interaction](modules/04-two-factor-factorial.md) | two-factor ANOVA, hand calculations for two-factor tables, interaction plots |
| 05 | [Balanced and unbalanced designs](modules/05-balanced-unbalanced.md) | orthogonality, Type I/II/III sums of squares |
| 06 | [Replications and sample size](modules/06-replications-and-power.md) | error df, power, choosing n |
| 07 | [Full-factorial 2^k designs](modules/07-full-factorial-2k.md) | effects, interactions, Lenth's method, center points, curvature |
| 08 | [Fractional-factorial designs](modules/08-fractional-factorial.md) | generators, aliasing, resolution, fold-over |
| 09 | [Operating levels: quality, cost, productivity](modules/09-operating-levels-and-cost.md) | prediction, cost trade-off, margin, confirmation runs |
| 10 | [Computer applications](modules/10-computer-applications.md) | Python, spreadsheet, reading DOE software output |
| 11 | [Capstone and skill check](modules/11-capstone.md) | plan your own experiment; 10-question check |

A suggested two-day schedule: day 1 covers modules 00 to 06, day 2 covers modules 07 to 11.

## Getting started

```bash
pip install -r requirements.txt
python tools/doekit.py data      # regenerate data/*.csv (already included)
python tools/doekit.py all       # every worked example
python tools/make_figures.py     # regenerate figures/
```

## Folder map

```
modules/     lessons (Markdown)
tools/       doekit.py (data + analysis), make_figures.py
data/        simulated datasets (CSV)
figures/     charts used in the lessons
solutions/   results of every worked example + teaching notes
reference/   formulas, glossary, further reading
templates/   experiment plan, run sheet
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
