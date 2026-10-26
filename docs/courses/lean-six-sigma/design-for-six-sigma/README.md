# Design for Six Sigma — An Open Course

A free, open course on designing new products and processes so quality, capability and flow are built in from the start. It follows the **DCDOV** roadmap — Define, Concept, Design, Optimize, Verify — and runs a single worked case (a linear guide carriage and its production line) through every phase. Every calculation is reproduced by a small Python toolkit.

**Prerequisites:** [Measurement & Basic Statistics](../measurement-and-basic-statistics/README.md). Helpful: [Voice of the Customer](../voice-of-the-customer/README.md) (deeper VOC for Modules 1–2), [Charting Process Behavior](../charting-process-behavior/README.md) and [Fundamentals of Hypothesis Testing](../fundamentals-of-hypothesis-testing/README.md).

## What you will be able to do

- Apply the DCDOV roadmap and write a design charter with lifecycle-cost goals
- Capture the voice of the customer: segmentation, interviews, surveys, affinity diagrams, Kano
- Translate needs into CTQs with operational definitions and a House of Quality
- Generate concepts and select one with a Pugh matrix
- Predict capability, run an FMEA, error-proof the design, and build a design scorecard with RTY
- Build transfer functions from a designed experiment
- Analyze tolerance stack-ups by worst case, RSS and Monte Carlo
- Model and simulate process flow (Little's law, utilization, queues), balance a line to takt
- Verify with control plans, pilots, standard work and reliability testing

## Syllabus (≈45 hours including capstone)

| # | Phase | Module | Time |
|---|---|---|---|
| 0 | — | [Introduction: design excellence and DCDOV](modules/00-introduction.md) | 1 h |
| 1 | Define | [Voice of the customer](modules/01-voice-of-the-customer.md) | 2.5 h |
| 2 | Define | [Operational definitions, CTQs and QFD](modules/02-ctqs-and-qfd.md) | 2 h |
| 3 | Concept | [Principles, creativity, benchmarking, Pugh selection, key metrics](modules/03-concept-generation-and-selection.md) | 3 h |
| 4 | Design | [Measuring variability and capability in design](modules/04-measuring-variability-and-capability.md) | 3 h |
| 5 | Design | [SPC for new processes](modules/05-spc-for-new-processes.md) | 2 h |
| 6 | Design | [FMEA](modules/06-fmea.md) | 4 h |
| 7 | Design | [Error-proofing and analyzing designs](modules/07-error-proofing-and-design-analysis.md) | 3 h |
| 8 | Design | [Design scorecard and rolled throughput yield](modules/08-design-scorecard.md) | 2 h |
| 9 | Design | [Transfer functions and designed experiments](modules/09-transfer-functions-and-doe.md) | 6 h |
| 10 | Optimize | [Tolerance design and Monte Carlo](modules/10-tolerance-design-and-monte-carlo.md) | 4 h |
| 11 | Optimize | [Process models and performance](modules/11-process-models-and-performance.md) | 3 h |
| 12 | Optimize | [Simulating a process design](modules/12-simulating-a-process-design.md) | 3 h |
| 13 | Optimize | [Continuous flow and design for Lean](modules/13-continuous-flow-and-design-for-lean.md) | 3 h |
| 14 | Verify | [Control plans, piloting and standardized work](modules/14-control-plans-piloting-standard-work.md) | 2 h |
| 15 | Verify | [Reliability through testing; project close-out](modules/15-reliability-and-close-out.md) | 3 h |
| 16 | — | [Capstone: design a kitting cell](modules/16-capstone.md) | 4–6 h |

Answers to each module's checks are inside the module; exercise notes are in [`solutions/`](solutions/README.md).

## Reference

[Formulas](reference/formulas.md) · [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/dfss.py all          # every worked example
python tools/make_figures.py      # regenerate figures
```

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
