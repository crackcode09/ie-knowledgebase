# Detailed Motion Time Analysis (MTM-1 Topics)

A free, open course on detailed, distance- and condition-based predetermined motion time analysis, the style of work measurement that Methods-Time Measurement (MTM-1) made standard. It covers the four objectives of an MTM-1 practitioner course:

- perform methods analysis
- define the motions
- apply the times
- develop standards

It includes laboratory problems from industrial and office operations.

**Length:** self-paced; about 10 days if every lab is worked in a classroom, as in the original course format.  
**Prerequisites:** none. [Predetermined Time Standards](../predetermined-time-standards/README.md) is a gentler introduction.

> **About MTM.** MTM-1's data card, rules and manuals are copyrighted by the MTM associations, and certification (such as BlueCard) is issued through licensed training. This course is not affiliated with or endorsed by any MTM association and **does not reproduce MTM data**. All practice uses the course's original **Detailed Teaching Card**, whose classes and values are illustrative and not valid for real standards.

## What you will be able to do

- Perform methods analysis with two-handed charts.
- Define the basic motions and the conditions that drive their times.
- Apply motion times, including the simultaneous-motion reasoning.
- Develop, document and audit standards.

## Modules

| # | Module | Objective |
|---|---|---|
| 01 | [What is Methods-Time Measurement?](modules/01-what-is-mtm.md) | Background |
| 02 | [Time units and system levels](modules/02-time-units-and-system-levels.md) | Background |
| 03 | [Methods analysis](modules/03-methods-analysis.md) | Perform methods analysis |
| 04 | [Reach](modules/04-reach.md) | Define motions |
| 05 | [Move](modules/05-move.md) | Define motions |
| 06 | [Turn and apply pressure](modules/06-turn-and-apply-pressure.md) | Define motions |
| 07 | [Grasp](modules/07-grasp.md) | Define motions |
| 08 | [Position](modules/08-position.md) | Define motions |
| 09 | [Release and disengage](modules/09-release-and-disengage.md) | Define motions |
| 10 | [Eye, body, leg and foot motions](modules/10-eye-body-leg-and-foot-motions.md) | Define motions |
| 11 | [Simultaneous motions](modules/11-simultaneous-motions.md) | Define motions / apply times |
| 12 | [Writing an analysis](modules/12-writing-an-analysis.md) | Apply times |
| 13 | [Methods improvement with motion analysis](modules/13-methods-improvement.md) | Perform methods analysis |
| 14 | [Developing standards](modules/14-developing-standards.md) | Develop standards |
| 15 | [Laboratory problems](modules/15-laboratory-problems.md) | All (11 labs) |
| 16 | [Capstone and certification path](modules/16-capstone-and-certification-path.md) | All |

The source course page lists objectives but no topic outline, so the module structure is this course's own.

## Getting started

```bash
pip install -r requirements.txt
python tools/dmtkit.py all            # worked examples
python tools/dmtkit.py lab L03_current
python tools/dmtkit.py code R30c      # value of one code
python tools/dmtkit.py data           # regenerate card tables and lab files
python tools/make_figures.py
```

## Folder map

```
modules/     lessons
tools/       dmtkit.py (teaching card, analysis engine, labs), make_figures.py
data/        teaching card tables, lab worksheets (blank) and keys
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   teaching card summary, glossary, sources
templates/   two-handed analysis sheet, method description sheet
```

## Related courses

- [Predetermined Time Standards](../predetermined-time-standards/README.md): body-member, modular PMTS (different teaching card)
- [Work Measurement](../work-measurement/README.md): time study, allowances, standards
- [Standard Data Systems](../standard-data-systems/README.md): from element analyses to standard data
- [Facilities and Workplace Design](../facilities-and-workplace-design/README.md): workstation layout and motion economy

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE. This license covers the course's own text, code and teaching card; it grants no rights in MTM.
