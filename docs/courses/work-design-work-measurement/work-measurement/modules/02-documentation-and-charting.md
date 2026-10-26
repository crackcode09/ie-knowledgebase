# Module 02 — Documentation and Charting

## Objectives

- Use process charts to document how work is done.
- Prepare the documentation that supports a work standard.
- Use a worker–machine chart to reveal idle and interference time.

## Charting tools

| Chart | Shows | Use in work measurement |
|---|---|---|
| Flow process chart (operation, transport, inspection, delay, storage) | sequence of activities for a person or material | identify non-value-added steps before measuring |
| Flow diagram | the process drawn on a layout | walking distance, backtracking |
| Operation process chart | sequence of operations and inspections for a product's parts | scope of what is to be measured |
| Worker–machine (multiple activity) chart | worker and machine activities against time | idle time, machine interference, internal vs external work |
| Two-hand chart | left- and right-hand motions | detailed method study before PMTS or rating |

See the [Process Mapping](../../process-mapping/README.md) course for process-level charts.

## Worker–machine chart: Marlow pump assembly

The present method (Module 05 time study) runs every element in sequence:

| Time (s, normal) | Operator | Leak tester |
|---|---|---|
| 0–50.7 | E1 housing, E2 impeller, E3 seal/cover/screws | idle |
| 50.7–95.7 | **waits** (E4 leak test running) | testing 45.0 s |
| 95.7–108.4 | E5 label/inspect, E6 place in tote | idle |

The operator is idle for **45 s of every 108 s cycle** while the tester runs. Rearranging so the operator assembles the **next** pump (E1–E3, 50.7 s) during the test would shorten the cycle to the larger of the manual work or the machine time per pump — a methods improvement to make **before** the standard is finalized (Module 03). The course uses the present method's standard as the worked example, then shows the effect.

## The study file (standard documentation)

Every standard should have a file containing:

1. Job and part identification; work center; date; analyst.
2. **Method description** — workplace layout sketch, tools, fixtures, sequence.
3. **Element descriptions** with clear **breakpoints** (Module 04).
4. Conditions: material, equipment, speeds and feeds, quality requirements.
5. Raw observations, foreign elements and why they were removed.
6. Ratings and how they were judged (Module 06).
7. Allowances applied and their source (Module 07).
8. Calculations and the resulting standard (Module 08).
9. Approval and communication record.

Template: `templates/time-study-form.csv` and `templates/study-file-checklist.md`.

## Check yourself

1. Why chart the method before timing it?
2. What does the worker–machine chart tell you that a stopwatch total doesn't?

<details><summary>Answers</summary>

1. To document and question the method; measuring an inefficient method produces a standard that bakes in waste.
2. When the worker and machine are each idle, and which work could be done in parallel (internal work) — opportunities that a single total time hides.

</details>
