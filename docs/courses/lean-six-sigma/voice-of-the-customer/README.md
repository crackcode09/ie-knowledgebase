# Voice of the Customer — An Open Course

A free, open course on finding out what customers need — stated and unstated — and turning it into measurable requirements, specifications and targets that drive product and process design. One running case throughout: a manufacturer's spare-parts ordering service for maintenance plants, distributors and OEMs, with a 300-response survey dataset. No prerequisites.

This is the in-depth VOC course in the repository. [Process Mapping](../process-mapping/README.md) (Modules 6–10) and [Design for Six Sigma](../design-for-six-sigma/README.md) (Modules 1–2) include shorter VOC sections that link here.

## What you will be able to do

- Identify who the customer is, and view the organization as processes where inputs determine outputs (Y = f(X))
- Organize and manage VOC research, listening to customer, business, employee and process voices
- Segment customers and use research results to pick target markets
- Distinguish output from service requirements and classify needs with the Kano model
- Explain how customer expectations change over time and drive the process
- Design and run a basic survey; calculate margin of error and sample size
- Use affinity and tree diagrams to identify CTQs, and write effective operational definitions
- Turn VOC into specifications and targets
- Use a cause-and-effect matrix to find the inputs that most affect customer outputs

## Syllabus (≈7 hours)

| # | Module | Time |
|---|---|---|
| 0 | [Introduction: who is the customer; Y = f(X)](modules/00-introduction.md) | 40 min |
| 1 | [Obtaining VOC; listening to all the voices](modules/01-obtaining-voc-and-all-the-voices.md) | 45 min |
| 2 | [Market segmentation and target markets](modules/02-market-segmentation.md) | 45 min |
| 3 | [Understanding customer requirements: two types, Kano, changing expectations](modules/03-understanding-customer-requirements.md) | 60 min |
| 4 | [Where to go for customer requirements](modules/04-where-to-go-for-requirements.md) | 30 min |
| 5 | [Surveys: design and execution](modules/05-surveys.md) | 60 min |
| 6 | [Sampling uncertainty and margin of error](modules/06-sampling-and-margin-of-error.md) | 50 min |
| 7 | [Affinity diagram](modules/07-affinity-diagram.md) | 35 min |
| 8 | [CTQ tree and operational definitions](modules/08-ctq-tree-and-operational-definitions.md) | 50 min |
| 9 | [VOC as specifications and targets](modules/09-voc-as-specifications.md) | 45 min |
| 10 | [Cause-and-effect matrix](modules/10-cause-and-effect-matrix.md) | 45 min |
| 11 | [Skill check and capstone](modules/11-skill-check-and-capstone.md) | 45 min + capstone |

Templates: [`templates/voc-templates.md`](templates/voc-templates.md). Answers: [`solutions/`](solutions/README.md). Reference: [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/voc.py data      # generate data/survey.csv (fixed seed)
python tools/voc.py all       # every worked example
python tools/make_figures.py
```

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
