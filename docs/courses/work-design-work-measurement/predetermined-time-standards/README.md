# Predetermined Time Standards (MODAPTS Topics)

A free, open course on body-motion predetermined time systems. It follows the topic outline of a MODAPTS practitioner course item by item. It explains what MODAPTS is and how it is organized, using cited public sources, and teaches the analysis method with an **original teaching code card**.

**Length:** about 3 days (21 short modules plus practice), or self-paced.  
**Prerequisites:** none. [Work Measurement](../work-measurement/README.md) helps for allowances and standards.

> **About MODAPTS.** MODAPTS is a registered trademark of the International MODAPTS Association, Inc. (IMA), which also holds the system's copyright. This course is not affiliated with or endorsed by the IMA, and it **does not reproduce the official MODAPTS code card or manual**. All practice uses the course's own teaching card, whose values are illustrative and not validated for real standards. For official training and the practitioner certification exam, contact the IMA.

## What you will be able to do

- Use the terminology of MODAPTS-style predetermined time systems.
- Apply a body-motion PMTS to set work standards (practised with the teaching card).
- Analyze and improve existing work methods.
- Improve the ergonomics and productivity of work tasks.
- Prepare for official practitioner training and certification.

## Running case

**Kessler Components** (fictional) kits fasteners, assembles pinned housings and packs cartons. The course codes each task, sets a standard for a new job, cuts kitting and packing time by more than half, and removes 600 bends a shift.

## Modules (in outline order)

| # | Module | Outline item |
|---|---|---|
| 01 | [What is MODAPTS?](modules/01-what-is-modapts.md) | What is MODAPTS? |
| 02 | [The MODAPTS acronym](modules/02-modapts-acronym.md) | MODAPTS Acronym |
| 03 | [Predetermined time standards](modules/03-predetermined-time-standards.md) | Predetermined Time Standards |
| 04 | [The MODAPTS symbol (code notation)](modules/04-modapts-symbol.md) | MODAPTS Symbol |
| 05 | [Why apply MODAPTS](modules/05-why-apply-modapts.md) | Why Apply MODAPTS |
| 06 | [History of MODAPTS](modules/06-history-of-modapts.md) | History of MODAPTS |
| 07 | [The modular concept](modules/07-the-modular-concept.md) | The Modular Concept |
| 08 | [MODAPTS codes](modules/08-modapts-codes.md) | MODAPTS Codes |
| 09 | [Classifying movement activities](modules/09-classifying-movement-activities.md) | Classifying Movement Activities |
| 10 | [Commonly found movements](modules/10-commonly-found-movements.md) | Commonly Found Movements |
| 11 | [Movement classifications](modules/11-movement-classifications.md) | Movement Classifications (listed twice in the outline; combined) |
| 12 | [Movements: key rules](modules/12-movements-key-rules.md) | Movements - Key Rules |
| 13 | [Get vs. put](modules/13-get-vs-put.md) | Get vs. Put |
| 14 | [Low vs. high conscious control](modules/14-low-vs-high-conscious-control.md) | Low vs. High Conscious Control |
| 15 | [The element GET](modules/15-the-element-get.md) | The Element GET |
| 16 | [The element PUT](modules/16-the-element-put.md) | The Element PUT |
| 17 | [Terminal activities: key rules](modules/17-terminal-activities-key-rules.md) | Terminal Activities - Key Rules |
| 18 | [The auxiliary class](modules/18-auxiliary-class.md) | Auxiliary Class |
| 19 | [Overview of auxiliary activities](modules/19-overview-of-auxiliary-activities.md) | Overview of Auxiliary Activities |
| 20 | [Practice analysis](modules/20-practice-analysis.md) | Practice MODAPTS Analysis (with the teaching card) |
| 21 | [Review summary and capstone](modules/21-review-summary-and-capstone.md) | Optional Review Summary |

**Suggested schedule:**

- Day 1: modules 01–08
- Day 2: modules 09–17
- Day 3: modules 18–21 and practice

## Related courses

- [Work Measurement](../work-measurement/README.md): time study, allowances and an overview of PMTS
- [Standard Data Systems](../standard-data-systems/README.md): building element data from studies
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md): standard work and line balancing

## Getting started

```bash
pip install -r requirements.txt
python tools/ptskit.py all                     # every worked example
python tools/ptskit.py show B_pin_assembly     # print one coded analysis
python tools/ptskit.py data                    # regenerate data/*.csv
python tools/make_figures.py                   # regenerate figures/
```

## Folder map

```
modules/     lessons, in outline order
tools/       ptskit.py (teaching card, analyses, calculations), make_figures.py
data/        teaching code card, coded practice analyses, exercises and key
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   teaching code card, glossary, sources and further reading
templates/   analysis sheet, method-improvement checklist
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE. This license covers the course's own text, code and teaching card; it grants no rights in MODAPTS.
