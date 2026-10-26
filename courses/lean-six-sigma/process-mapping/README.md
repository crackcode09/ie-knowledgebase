# Process Mapping — An Open Course

A free, open course on drawing process pictures that a team can act on — SIPOC, flow charts, swim lanes, value-added flow charts, spaghetti diagrams and value stream maps — and on letting the voice of the customer define what the process must deliver: affinity diagrams, CTQ trees, and turning VOC into specifications. One running case throughout: a returns-and-repair (RMA) process that takes 11.6 days when customers want 6. No prerequisites.

## What you will be able to do

- Choose the right type of process map for a purpose
- Build a SIPOC, flow chart and swim-lane map
- Identify non-value-added operations and create a value-added flow chart to communicate findings
- Use a spaghetti diagram to illustrate and measure the path of material or information
- Draw a value stream map with a timeline and percent complete-and-accurate
- Explain how customer expectations drive a process and how they change over time
- Use an affinity diagram and a CTQ tree to identify critical-to-quality characteristics
- Turn customer data into a specification

## Syllabus (≈6 hours)

| # | Module | Time |
|---|---|---|
| 0 | [Drawing a process picture: why map, which map](modules/00-drawing-a-process-picture.md) | 40 min |
| 1 | [SIPOC](modules/01-sipoc.md) | 30 min |
| 2 | [Process flow charts and swim lanes](modules/02-flow-charts-and-swim-lanes.md) | 45 min |
| 3 | [Value-added flow charts](modules/03-value-added-flow-charts.md) | 45 min |
| 4 | [Spaghetti diagrams](modules/04-spaghetti-diagrams.md) | 35 min |
| 5 | [Value stream mapping](modules/05-value-stream-mapping.md) | 50 min |
| 6 | [Introduction to the voice of the customer](modules/06-voice-of-the-customer-introduction.md) | 30 min |
| 7 | [Capturing VOC: methods and sources](modules/07-capturing-voc-and-sources.md) | 35 min |
| 8 | [Affinity diagram](modules/08-affinity-diagram.md) | 30 min |
| 9 | [CTQ tree diagram](modules/09-ctq-tree.md) | 35 min |
| 10 | [VOC as specifications](modules/10-voc-as-specifications.md) | 35 min |
| 11 | [Skill check and capstone](modules/11-skill-check-and-capstone.md) | 45 min + capstone |

Diagrams are written in [Mermaid](https://mermaid.js.org/) and render on GitHub. Templates: [`templates/mapping-templates.md`](templates/mapping-templates.md). Answers and instructor notes: [`solutions/`](solutions/README.md).

## Reference

[Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/pmap.py all
python tools/make_figures.py
```

## Related courses

[Voice of the Customer](../voice-of-the-customer/README.md) (VOC in depth: segmentation, Kano, surveys, margin of error, C&E matrix) · [Kaizen Leader](../kaizen-leader/README.md) (uses these maps during an event) · [Root Cause Analysis](../root-cause-analysis/README.md) · [Design for Six Sigma](../design-for-six-sigma/README.md) (VOC and QFD in depth)

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
