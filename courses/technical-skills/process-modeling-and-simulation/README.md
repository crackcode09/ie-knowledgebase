# Process Modeling and Simulation — An Open Course

Learn to build process models — discrete-event simulations — to design new processes, improve existing ones and teach Lean concepts. Static process maps assume average conditions; real processes face variation in demand, task times, parts and people. This course shows how to model that variation, explore many designs quickly ("build to think"), test them for resilience, write best-practice operating procedures, quantify risks for FMEAs and build a persuasive case for stakeholders. One running case: a same-day repair service center. All modeling uses a small open Python simulator written for the course; the methods carry over to any simulation tool. No prerequisites.

## What you will be able to do

- Explain why static maps mislead and what a process model adds
- Build a discrete-event model: entities, activities, resources, queues, routing, distributions
- Verify and validate a model and report results with replications and confidence intervals
- Explore a wider design space by building to think
- Test processes for resilience against variation
- Develop best-practice operating procedures (dispatch rules, batching, escalation)
- Identify risks and develop FMEAs using simulated impacts
- Build a persuasive, model-based case for stakeholder buy-in
- Use small models to teach Lean concepts

## Syllabus (≈7 hours)

| # | Module | Time |
|---|---|---|
| 0 | [Why model processes? Static maps vs real variation](modules/00-why-model-processes.md) | 40 min |
| 1 | [How a process model works](modules/01-how-a-process-model-works.md) | 50 min |
| 2 | [Building the model: scope, data, assumptions](modules/02-building-the-model.md) | 50 min |
| 3 | [Verification, validation and replications](modules/03-verification-validation-replications.md) | 50 min |
| 4 | [Exploring the design space ("build to think")](modules/04-exploring-the-design-space.md) | 45 min |
| 5 | [Testing resilience against variation](modules/05-testing-resilience.md) | 45 min |
| 6 | [Developing best-practice operating procedures](modules/06-best-practice-operating-procedures.md) | 50 min |
| 7 | [Identifying risks and building FMEAs](modules/07-risks-and-fmea.md) | 45 min |
| 8 | [Building the case for stakeholders](modules/08-building-the-case.md) | 45 min |
| 9 | [Using models to teach Lean concepts](modules/09-teaching-lean-with-models.md) | 40 min |
| 10 | [Capstone](modules/10-capstone.md) | 2–3 h |

Templates: [`templates/modeling-worksheets.md`](templates/modeling-worksheets.md). Answers and instructor notes: [`solutions/`](solutions/README.md). Reference: [Glossary](reference/glossary.md) · [Further reading](reference/further-reading.md)

## Quick start

```bash
pip install -r requirements.txt
python tools/procsim.py all       # every worked example (about a minute)
python tools/make_figures.py
```

To try your own scenario:

```python
import sys; sys.path.insert(0, "tools")
import procsim as ps
print(ps.run(ps.Design(name="My idea", pooled_techs=True, repair_techs=5, dispatch="PRIORITY")))
```

## Related courses

[Lean Methods Accelerator](../../lean-six-sigma/lean-methods-accelerator/README.md) (pull, CONWIP, variability) · [Design for Six Sigma](../../lean-six-sigma/design-for-six-sigma/README.md) (process models in design, FMEA) · [Process Mapping](../../lean-six-sigma/process-mapping/README.md) (the static maps this course builds on)

## License

Content CC BY 4.0, code MIT — see [LICENSE](../../../LICENSE). Contributions: [CONTRIBUTING.md](../../../CONTRIBUTING.md).
