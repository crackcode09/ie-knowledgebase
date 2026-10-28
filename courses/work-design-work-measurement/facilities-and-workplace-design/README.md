# Facilities and Workplace Design

Learn to plan plant layouts, cells and workstations so that flow is short, simple and safe. It follows the topic outline of a two-day facilities and workplace design seminar, in the same order.

**Length:** about 2 days (14 contact hours), or self-paced.  
**Prerequisites:** none. Basic Lean and time study help (see the related courses).

## What you will be able to do

- Arrange a facility for optimum performance.
- Develop techniques to get new cells up and running.
- Identify key issues and their integration with other production elements.
- Plan and design productive layouts.

## Running case

**Corvan Enclosures** (fictional) makes steel electrical enclosures in a 50 m × 40 m plant. The course takes it from products, volumes and flows to a new block layout (−62 % handling with the paint system left in place) and a U-shaped wall-box cell with 2 operators per shift. All data is simulated with a fixed seed.

## Modules and outline

Every outline item appears as a section heading, in the original order.

| # | Module | Outline items |
|---|---|---|
| 01 | [Facilities and strategy · Levels of design](modules/01-facilities-strategy-and-levels-of-design.md) | Facilities and strategy; Levels of design |
| 02 | [Planning the layout · Project model plan](modules/02-planning-the-layout-project-model-plan.md) | Planning the layout; Project model plan |
| 03 | [Information acquisition · Products · Volumes](modules/03-information-acquisition-products-volumes.md) | Information acquisition; Products; Volumes |
| 04 | [Inventory · Usage](modules/04-inventory-usage.md) | Inventory; Usage |
| 05 | [Flow · Processes](modules/05-flow-processes.md) | Flow; Processes |
| 06 | [Planning units · Affinities](modules/06-planning-units-affinities.md) | Planning units; Affinities |
| 07 | [Space constraints · Configuration diagrams](modules/07-space-constraints-configuration-diagrams.md) | Space constraints; Configuration diagrams |
| 08 | [Material flow](modules/08-material-flow.md) | Material flow |
| 09 | [Cellular layouts · Workstation layouts](modules/09-cellular-layouts-workstation-layouts.md) | Cellular layouts; Workstation layouts |
| 10 | [Engineering the process · Process charting · Estimating times](modules/10-engineering-the-process-process-charting-estimating-times.md) | Engineering the process; Process charting; Estimating times |
| 11 | [Calculating cell capacity · How many people and machines?](modules/11-calculating-cell-capacity-how-many-people-and-machines.md) | Calculating cell capacity; How many people and machines? |
| 12 | [Ergonomics · Motion economy](modules/12-ergonomics-motion-economy.md) | Ergonomics; Motion economy |
| 13 | [Design procedures · Infrastructure · Scheduling · Handling](modules/13-design-procedures-infrastructure-scheduling-handling.md) | Design procedures; Defining infrastructure; Scheduling; Material handling and containers |
| 14 | [Balancing · Supervision · Compensation](modules/14-balancing-supervision-compensation.md) | Balancing the work; Supervision; Compensation and rewards |
| 15 | [Layout of the cell · Configurations · Procedures](modules/15-layout-of-the-cell-configurations-procedures.md) | Layout of the cell; Cell configurations; Layout procedures |
| 16 | [Capstone](modules/16-capstone.md) | Junction-box cell; skill check |

**Suggested schedule:**

- Day 1: modules 01–08 (facility layout)
- Day 2: modules 09–16 (cells and workstations)

## Related courses

- [Process Mapping](../../lean-six-sigma/process-mapping/README.md): process charts and spaghetti diagrams
- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md) and [Kaizen Leader](../../lean-six-sigma/kaizen-leader/README.md): takt, balancing, kanban, SMED
- [Work Measurement](../work-measurement/README.md), [Standard Data Systems](../standard-data-systems/README.md), [Predetermined Time Standards](../predetermined-time-standards/README.md): estimating times
- [Process Modeling and Simulation](../../technical-skills/process-modeling-and-simulation/README.md): testing layouts and cells dynamically

## Getting started

```bash
pip install -r requirements.txt
python tools/fwdkit.py all          # every worked example
python tools/fwdkit.py data         # regenerate data/*.csv
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons (outline items as section headings)
tools/       fwdkit.py (P-Q, inventory, flow, space, affinities, layout exchange, ROC, cell capacity, balance, kanban, EPEI), make_figures.py
data/        case datasets (CSV)
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   formulas, glossary, further reading
templates/   layout project plan, relationship chart, space worksheet, cell design checklist
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
