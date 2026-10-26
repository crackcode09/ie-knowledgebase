# Module 0 — Introduction: Design Excellence and the DCDOV Roadmap

**Time:** 60 min · **Prerequisites:** *Measurement & Basic Statistics* recommended

## Learning objectives

1. Explain why quality is cheapest to build in during design.
2. Describe the DCDOV roadmap and how it differs from DMAIC.
3. Write a design project charter.

## 1. Why design for quality?

Most of a product's or process's lifecycle cost — materials, manufacturing method, tolerances, service needs — is locked in by design decisions made before production starts. Changes get dramatically more expensive the later they're made: a tolerance changed on a drawing costs an hour; the same change after tooling is cut costs the tooling; after launch it costs recalls and reputation. (The often-quoted "10× per phase" rule is a rule of thumb, not a measured constant — but the direction is never in doubt.)

DMAIC improves an existing process whose capability is limited by its design. When the design itself is the limit — or there's no process yet — you need **Design for Six Sigma (DFSS)**: build capability in from the start.

## 2. Roadmaps

| DMAIC (improve) | DCDOV (design) | DMADV (design, common alternative) |
|---|---|---|
| Define | **Define** — the opportunity, customers and their needs | Define |
| Measure | **Concept** — generate and select concepts | Measure (CTQs) |
| Analyze | **Design** — develop the chosen concept; model and predict performance | Analyze (concepts) |
| Improve | **Optimize** — make performance robust to variation | Design |
| Control | **Verify** (or Validate) — prove it works and hand it off | Verify |

This course follows DCDOV. The names differ by source; the logic is the same: **understand the customer → choose the best concept → predict and optimize performance before building → verify**.

## 3. Lifecycle cost

Design for the **whole** lifecycle, not just unit cost:

| Cost element | Design levers |
|---|---|
| Development | Reuse proven modules; prototype and simulate early |
| Manufacturing | Fewer parts (DFA), capable tolerances (Module 10), error-proofing (Module 7) |
| Quality | Robustness to variation (Modules 9–10), FMEA (Module 6) |
| Service and warranty | Reliability (Module 15), maintainability |
| End of life | Materials, disassembly |

## 4. The design charter

| Field | Example |
|---|---|
| Opportunity | Customers are switching to competitors' quieter, lower-maintenance linear guides |
| Scope | New compact linear guide carriage for packaging machinery; excludes rails |
| Customers | OEM machine builders (design engineers, purchasing), end-user maintenance staff |
| Goals | Friction ≤ 15 N, 10,000 km lube interval, unit cost ≤ $X, launch in 9 months |
| Deliverables per phase | VOC report; concept selection; design scorecard; pilot results; control plan |
| Team and sponsor | Design, manufacturing, quality, purchasing, sales |
| Risks | New polymer supplier; test-rig availability |

Track the project with phase-gate reviews: at each gate the sponsor sees the deliverables and decides go / revise / stop.

## 5. Course map

| # | Phase | Module |
|---|---|---|
| 1 | Define | Voice of the customer, segmentation, surveys, affinity diagrams |
| 2 | Define | Operational definitions and CTQs; QFD |
| 3 | Concept | DFSS principles, creative process, benchmarking, Pugh selection, key metrics |
| 4 | Design | Measuring variability and capability in design |
| 5 | Design | Statistical process control for new processes |
| 6 | Design | FMEA |
| 7 | Design | Error-proofing and design analysis (DFM/DFA) |
| 8 | Design | Design scorecard and rolled throughput yield |
| 9 | Design | Transfer functions and designed experiments |
| 10 | Optimize | Tolerance design and Monte Carlo |
| 11 | Optimize | Process models and performance (Little's law, utilization, queues) |
| 12 | Optimize | Simulating a process design |
| 13 | Optimize | Continuous flow and design for Lean |
| 14 | Verify | Control plans, piloting and standardized work |
| 15 | Verify | Reliability through testing; project close-out |
| 16 | — | Capstone |

All calculations: `python tools/dfss.py all`.
