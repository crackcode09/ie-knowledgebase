# Module 10 — Engineering the Process · Process Charting · Estimating Times

Outline items: **Engineering the process**, **Process charting**, **Estimating times**

## Objectives

- Engineer the process for a cell before laying it out.
- Use a process chart to expose non-value-adding steps.
- Estimate operation times with methods matched to the stage of the project.

## Engineering the process

Don't move a bad process into a new layout. For the wall-box family:

1. **Confirm the family and volume**: 12 SKUs, 131,730 units a year (2 shifts, 230 days).
2. **Define operations**: shear blank → turret punch → brake 4 bends → spot weld corners → press hardware → inspect and load to paint rack. Paint, assembly and test stay as shared areas.
3. **Question each step** (eliminate, combine, rearrange, simplify): can punching and shearing combine (punch from a sheet with a part-out)? Can welded corners be replaced with formed corners?
4. **Choose equipment**: dedicate a brake to the cell (removing an exceptional element, Module 09).
5. **Set quality checks** at the source (first-piece check after each setup; in-cell inspection).

## Process charting

A **flow process chart** lists every step using these symbols:

| Symbol | Meaning |
|---|---|
| ○ | Operation |
| ⇨ | Transport |
| D | Delay |
| ▽ | Storage |
| □ | Inspection |

Wall-box, current functional layout (one load of 20, summarized):

| Category | Count | Notes |
|---|---|---|
| Operations | 9 | Shear, punch, brake, weld, paint, assemble, test, pack, plus hardware press |
| Transports | 8 | 345.8 m in the as-is layout |
| Delays (queues) | 7 | Waiting before each department |
| Storages | 2 | Raw material, finished goods |
| Inspections | 2 | Weld check, final test |

Only the operations add value. The cell removes most transports and delays between shear and paint, and the new block layout cuts the route to **115.8 m**. See the [Process Mapping](../../process-mapping/README.md) course for charting in depth.

## Estimating times

| Project stage | Method | Accuracy |
|---|---|---|
| Concept | Historical times, comparison with similar parts | Rough (±25 % or worse) |
| Design | Standard data, predetermined time systems | Good |
| Pilot | Time study of the pilot or mock-up | Good |
| Running | Ongoing measurement; system data | Good, and shows drift |

Wall-box cell operations (`data/cell_operations.csv`), from a mix of standard data and time studies of the current equipment:

| Op | Description | Machine s | Manual s | Setup min |
|---|---|---|---|---|
| OP10 | Shear blank | 14 | 10 | 15 |
| OP20 | Turret punch | 48 | 14 | 20 |
| OP30 | Brake 4 bends | 18 | 34 | 12 |
| OP40 | Spot weld corners | 22 | 18 | 8 |
| OP50 | Press hardware | 6 | 20 | 5 |
| OP60 | Inspect, load to paint rack | 0 | 24 | 0 |

See [Work Measurement](../../work-measurement/README.md) and [Standard Data Systems](../../standard-data-systems/README.md) for these methods.

## Check yourself

1. Which flow-process-chart categories add value?
2. At the concept stage, why not insist on time studies?

<details><summary>Answers</summary>

1. Only **operations** that change the product the way the customer wants. Transports, delays, storages and (usually) inspections don't.
2. The process doesn't exist yet, and rough estimates are enough to compare concepts. Measure more precisely as the design firms up.

</details>
