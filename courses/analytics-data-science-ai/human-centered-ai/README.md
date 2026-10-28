# Human-Centered AI

Learn to ground AI initiatives in real user needs, real work and real constraints. Participants learn to frame AI opportunities through the eyes of the people who will use, trust or reject them, and practise qualitative insight gathering, theme synthesis and opportunity framing. Those framed opportunities then feed design sprints and rapid prototypes. It follows the key topics of a 2-hour livestream session: each topic is a module, with the same title and order.

**Length:** 2 hours as a live session (modules 01–05, with the workshop exercises compressed), or about half a day with the full workshop.  
**Prerequisites:** none. Pairs well with [Efficient AI](../efficient-ai/README.md).

## What you will be able to do

- Define core human-centered design (HCD) principles and explain why they are critical to AI readiness and adoption.
- Understand how user needs, behaviors and constraints shape successful AI solutions.
- Practise qualitative insight techniques by simulating interviews with frontline and operational roles.
- Understand how framed opportunities feed directly into design sprints and rapid prototyping.
- Identify ways to rapidly prototype solutions to learn quickly and de-risk assumptions.

## Running case

**Halvorsen Components** (fictional; the same company as in Efficient AI) interviews eight frontline and operational workers before building anything. The course follows it through:

- 48 notes → 6 themes (word-based clustering of the same notes barely matches them: adjusted Rand index 0.02)
- 6 "How might we" opportunities, of which the technician information opportunity scores highest
- an assumption map with 4 assumptions to test first
- a Wizard-of-Oz prototype: lookups 76 % faster, but only 5 of 12 would use it daily, and all 12 want sources shown

**All interview content is simulated for teaching.**

## Modules (key topics, source titles)

| # | Module |
|---|---|
| 01 | [Human Centered Design Foundations](modules/01-human-centered-design-foundations.md) |
| 02 | [Qualitative Insight Gathering](modules/02-qualitative-insight-gathering.md) |
| 03 | [From Insights to Themes](modules/03-from-insights-to-themes.md) |
| 04 | [Opportunity Framing](modules/04-opportunity-framing.md) |
| 05 | [Bridge to Design Sprints and Prototyping](modules/05-bridge-to-design-sprints-and-prototyping.md) |
| 06 | [Workshop: from people to prototype](modules/06-workshop.md) (added) |

**Suggested 2-hour agenda:**

| Time | Content |
|---|---|
| 0:00–0:15 | 01 |
| 0:15–0:45 | 02, including one round of simulated interviews |
| 0:45–1:10 | 03 |
| 1:10–1:30 | 04 |
| 1:30–2:00 | 05 |

## Related courses

- [Efficient AI](../efficient-ai/README.md): problem-first AI, Lean integration, data readiness, roadmap
- [Voice of the Customer](../../lean-six-sigma/voice-of-the-customer/README.md): interviews, affinity diagrams, CTQs
- [Kaizen Leader](../../lean-six-sigma/kaizen-leader/README.md): running fast, team-based improvement events

## Getting started

```bash
pip install -r requirements.txt
python tools/hcdkit.py all          # every worked example
python tools/hcdkit.py data         # regenerate data/*.csv and the role-play cards
python tools/make_figures.py        # regenerate figures/
```

## Folder map

```
modules/     lessons (source topic titles)
tools/       hcdkit.py (theme synthesis, machine clustering comparison, opportunity scoring, assumption map, prototype analysis), make_figures.py
data/        simulated interview notes, theme key, role-play cards, opportunities, assumptions, Wizard-of-Oz test, survey
figures/     charts used in the lessons
solutions/   key results and facilitator notes
reference/   glossary, cheat sheet, further reading
templates/   interview guide, note sheet, sprint brief, assumption map, prototype test plan
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
