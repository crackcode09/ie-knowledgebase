# Efficient AI

Learn to apply AI across operations, from back-office functions to frontline work, to drive measurable efficiency and better decisions. It starts with the problems organizations are trying to solve, not with tools or trends. It examines where AI is appropriate and where it isn't, and uses Lean and Six Sigma thinking to make sure AI work delivers real outcomes. It follows the key topics of a half-day livestream session: each topic is a module, with the same title, in the same order.

**Length:** about 4 hours as a live session (modules 01–07 plus the workshop), or self-paced with the exercises.  
**Prerequisites:** none.

## What you will be able to do

- Clearly explain what AI is and isn't, and when it makes sense to apply it.
- Identify business and operational pain points where AI can deliver real value: improving efficiency, reducing waste and supporting better decisions across functions.
- Recognize common misconceptions and risks that derail AI initiatives, and how Lean principles help de-risk them.
- Assess data readiness and organizational constraints before pursuing AI solutions.
- Define practical next steps toward an AI roadmap aligned with business goals.

## Running case

**Halvorsen Components** (fictional), a 600-person manufacturer, has 14 "AI ideas" from every department. The course:

- sizes the ideas and finds that 4 of them need a process fix rather than AI
- prioritizes the rest with a PICK chart
- shows that a simple rule captures most of the value of a late-delivery model
- audits ticket data (only 61 % labelled)
- tests a document assistant against acceptance criteria (73 % correct, not ready)
- builds a phased roadmap with a sensitivity-tested business case

All data is simulated with a fixed seed. No AI service is needed: every example runs locally.

## Modules (key topics, source titles)

| # | Module |
|---|---|
| 01 | [AI Foundations](modules/01-ai-foundations.md) |
| 02 | [Problem First Thinking](modules/02-problem-first-thinking.md) |
| 03 | [Cross Functional Use Cases](modules/03-cross-functional-use-cases.md) |
| 04 | [AI and Lean Six Sigma Integration](modules/04-ai-and-lean-six-sigma-integration.md) |
| 05 | [Risks, Limitations, and Misconceptions](modules/05-risks-limitations-and-misconceptions.md) |
| 06 | [Data Readiness](modules/06-data-readiness.md) |
| 07 | [From Ideas to Roadmap](modules/07-from-ideas-to-roadmap.md) |
| 08 | [Workshop: your AI roadmap](modules/08-workshop.md) (added) |

**Suggested 4-hour agenda:**

| Time | Modules |
|---|---|
| 0:00–0:30 | 01 |
| 0:30–1:00 | 02 |
| 1:00–1:30 | 03 |
| 1:30–2:00 | 04 |
| 2:00–2:15 | Break |
| 2:15–2:45 | 05 |
| 2:45–3:00 | 06 |
| 3:00–3:15 | 07 |
| 3:15–4:00 | 08 (workshop) |

## Related courses

- [Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md) and [Kaizen Leader](../../lean-six-sigma/kaizen-leader/README.md): Lean tools
- [Introduction to Engineering Analytics](../engineering-analytics/README.md) and [Advanced Engineering Analytics](../advanced-engineering-analytics/README.md): building and validating models
- [Engineering Decision Making & Risk Management](../../operations-research-decision-analysis/engineering-decision-making/README.md): ROC curves, value of information, risk
- [Analytics-Based Enterprise Performance Management](../analytics-based-epm/README.md): predictive accounting and roadmaps

## Getting started

```bash
pip install -r requirements.txt
python tools/aikit.py all          # every worked example
python tools/aikit.py data         # regenerate data/*.csv
python tools/make_figures.py       # regenerate figures/
```

## Folder map

```
modules/     lessons (source topic titles)
tools/       aikit.py (portfolio scoring, data readiness audit, prediction vs rule, GenAI pilot evaluation, ROI and sensitivity, roadmap), make_figures.py
data/        use-case list, ticket extract, shipments, assistant evaluation
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   cheat sheet, glossary, further reading
templates/   problem statement, use-case scoring, data readiness checklist, pilot charter, AI roadmap
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
