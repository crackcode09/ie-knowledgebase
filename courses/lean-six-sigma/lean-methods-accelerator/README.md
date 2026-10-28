# Lean Methods Accelerator — An Open Course

Learn the Lean enterprise toolkit end to end, as a **standalone** course — from cost of poor quality and the Lean blueprint, through value stream mapping, takt, line balancing and benchmarking, to continuous flow and cells, quick changeover, theory of constraints, pull systems (kanban, CONWIP, heijunka), 5S, visual management, TPM and standard work. It can be taken on its own or alongside a Six Sigma curriculum. One running case throughout: a hydraulic-manifold plant that misses demand, with simulations of the bullwhip effect and WIP-capped pull. No prerequisites.

Want more depth on a topic? See [Process Mapping](../process-mapping/README.md), [Kaizen Leader](../kaizen-leader/README.md), [Root Cause Analysis](../root-cause-analysis/README.md) and [Design for Six Sigma](../design-for-six-sigma/README.md) in this repository.

## What you will be able to do

- Discuss processes using Lean terminology and quantify the cost of poor quality
- Map a value stream, including the extended process with suppliers and customers
- Use takt time to set the pace of work, and balance work to it
- Find bottlenecks and non-value-added activities
- Move a process toward continuous flow and cells while removing waste
- Shorten setup times to gain flexibility and cut inventory
- Design pull systems: kanban, CONWIP, heijunka
- Improve workplace organization and visual management
- Apply TPM and standard work to make processes reliable and sustain the gains

## Syllabus (≈18 hours)

| # | Session | Module | Time |
|---|---|---|---|
| 0 | 1 Introduction | [Lean and Lean Six Sigma](modules/00-introduction.md) | 30 min |
| 1 | 1 | [Cost of poor quality](modules/01-cost-of-poor-quality.md) | 35 min |
| 2 | 1 | [Lean blueprint, Y = f(X), DMAIC, thought process maps](modules/02-blueprint-yfx-dmaic-thought-maps.md) | 60 min |
| 3 | 2 Define & Measure | [Source of value, gemba walks, 3 Ms and 8 wastes](modules/03-value-gemba-wastes.md) | 60 min |
| 4 | 2 | [Process maps, value-added flow charts, spaghetti diagrams](modules/04-process-maps-va-spaghetti.md) | 60 min |
| 5 | 2 | [Process metrics and takt time](modules/05-process-metrics-and-takt.md) | 45 min |
| 6 | 2 | [Value stream mapping (incl. extended value stream)](modules/06-value-stream-mapping.md) | 75 min |
| 7 | 2 | [Line balancing and heijunka](modules/07-line-balancing-and-heijunka.md) | 50 min |
| 8 | 2 | [Measurement and data types; Pareto charts](modules/08-data-types-and-pareto.md) | 45 min |
| 9 | 2 | [Benchmarking](modules/09-benchmarking.md) | 35 min |
| 10 | 2 | [Kaizen](modules/10-kaizen.md) | 40 min |
| 11 | 3 Analyze, Improve, Control | [A3 and 5-Why, 1-How](modules/11-a3-and-5why.md) | 50 min |
| 12 | 3 | [DFSS and design for Lean: supply chain dynamics](modules/12-dfss-and-design-for-lean.md) | 60 min |
| 13 | 3 | [Error-proofing](modules/13-error-proofing.md) | 35 min |
| 14 | 3 | [Continuous flow and cellular processing](modules/14-continuous-flow-and-cells.md) | 60 min |
| 15 | 3 | [Quick changeover](modules/15-quick-changeover.md) | 60 min |
| 16 | 3 | [Theory of constraints](modules/16-theory-of-constraints.md) | 45 min |
| 17 | 3 | [Pull systems: types, CONWIP, pull scheduling](modules/17-pull-systems.md) | 90 min |
| 18 | 3 | [Visual management and 5S](modules/18-visual-management-and-5s.md) | 50 min |
| 19 | 3 | [Total productive maintenance](modules/19-total-productive-maintenance.md) | 75 min |
| 20 | 3 | [Standard work and leader standard work](modules/20-standard-work-and-leader-standard-work.md) | 60 min |
| 21 | — | [The Lean journey, skill check and capstone](modules/21-lean-journey-and-capstone.md) | 60 min + capstone |

Templates: [A3](templates/a3-template.md) · [Lean worksheets](templates/lean-worksheets.md). Answers and instructor notes: [`solutions/`](solutions/README.md). Reference: [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/lean.py all          # every worked example and simulation
python tools/make_figures.py
```

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
