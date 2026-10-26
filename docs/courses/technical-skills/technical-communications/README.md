# Technical Communications

A free, open course for engineers who need to explain projects built on quantitative analysis to managers and non-engineering colleagues, in manufacturing, service or government settings.

**Length:** nine 2-hour sessions (18 contact hours), or self-paced.  
**Prerequisites:** none. The data examples assume you have seen basic charts and averages.

## What you will be able to do

- Explain why communicating effectively with your audience matters.
- Use tools to organize a presentation.
- Treat your audience as a customer and understand their voice.
- Present data analysis effectively.

## Running case

A process engineer at a fictional bearing plant cut scrap on grinding Line 3 from 4.5% to 2.0%. She has 10 minutes at the plant leadership meeting to ask for $38,000 to apply the fix to three more lines. The `examples/` folder holds her **first draft** and **revised** deck and summary, and the course follows the revision step by step. All data and people are fictional.

## Sessions

| # | Session | Body of knowledge |
|---|---|---|
| 00 | [The importance of effective communication](modules/00-importance-of-communication.md) | The engineer–audience gap; four tests: audience, message, evidence, delivery |
| 01 | [Common errors when communicating](modules/01-common-errors.md) | Buried ask, data dumps, jargon, text-heavy slides; diagnosing a draft; readability |
| 02 | [Defining the objectives of the presentation](modules/02-defining-objectives.md) | Audience analysis, the audience as customer, purpose statement, one-sentence message |
| 03 | [Organizing the presentation](modules/03-organizing-the-presentation.md) | Answer first, pyramid structure, situation–complication–resolution, action-title storyboard, timing, appendix |
| 04 | [Listening and feedback from your audience](modules/04-listening-and-feedback.md) | Pre-wiring, reading the room, Q&A and objections, rehearsal feedback |
| 05 | [Data in presentations](modules/05-data-in-presentations.md) | Choosing charts, decluttering, context, uncertainty, tables, accessibility |
| 06 | [Process improvement tools for presentations](modules/06-process-improvement-tools-for-presentations.md) | SIPOC, fishbone, Pareto of feedback, checklists, mistake-proofing, PDCA, standard work |
| 07 | [Quality presentations](modules/07-quality-presentations.md) | Fitness for use, rubric measurement, slide design, delivery, quality in writing |
| 08 | [Final presentations](modules/08-final-presentations.md) | Capstone: plan, build, rehearse, deliver, peer review |

## Related courses

- [Voice of the Customer](../../lean-six-sigma/voice-of-the-customer/README.md): methods for capturing audience needs (Session 02)
- [Charting Process Behavior](../../lean-six-sigma/charting-process-behavior/README.md) and [Measurement & Basic Statistics](../../lean-six-sigma/measurement-and-basic-statistics/README.md): the data behind your charts (Session 05)
- [Process Mapping](../../lean-six-sigma/process-mapping/README.md) and [Root Cause Analysis](../../lean-six-sigma/root-cause-analysis/README.md): SIPOC, fishbone and Pareto (Session 06)

## Getting started

```bash
pip install -r requirements.txt
python tools/commkit.py all                          # every worked example
python tools/commkit.py check examples/deck_draft.md # check any Markdown draft
python tools/make_figures.py                         # regenerate figures/
```

`commkit.py check` works on any Markdown file. Slides are `## ` headings and speaker notes go in `<!-- -->` comments. It reports readability scores, words and bullets per slide, and flags topic-only titles. It is a quick aid and does not replace a human reviewer.

## Folder map

```
modules/     the nine sessions
examples/    draft and revised deck and summary (the running case)
tools/       commkit.py (data, readability, slide checks), make_figures.py
data/        scrap data, defect counts, rehearsal feedback (CSV)
figures/     before/after charts and slides
solutions/   key results and facilitator notes
reference/   glossary, chart chooser, further reading
templates/   planner, storyboard, one-page summary, Q&A prep, rubric, checklist
```

## License

Content: CC BY 4.0. Code: MIT. See the repository root LICENSE.
