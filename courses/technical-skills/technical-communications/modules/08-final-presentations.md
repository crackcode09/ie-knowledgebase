# Module 08 — Final Presentations

## Objectives

- Prepare and deliver a complete technical presentation on your own project.
- Apply every tool from the course: audience analysis, answer-first structure, clear data, Q&A preparation, feedback.
- Receive and give structured feedback.

## The assignment

Present a real project (or the running case) to a decision-making audience.

| Element | Requirement |
|---|---|
| Length | 10 minutes including questions (about 5 minutes of content) |
| Audience | named, with a decision maker and their likely concerns |
| Purpose | one written sentence: what should happen by the end |
| Deck | 4–6 content slides with action titles; labeled appendix |
| Data | at least one chart redesigned using Module 05 |
| Written summary | one paragraph (≤ 150 words) with the finding, impact and ask |
| Q&A prep | top ten questions with two-sentence answers |

## Steps

1. **Plan** — complete `templates/presentation-planner.md` (audience, purpose, one-sentence message, voice of the audience).
2. **Storyboard** — write action titles only (`templates/storyboard.md`). Have a peer read the titles alone and tell you the story back.
3. **Build** — slides, speaker notes, appendix, one-paragraph summary (`templates/one-page-summary.md`).
4. **Check** — run `python tools/commkit.py check your_deck.md`; work through `templates/presentation-checklist.md`.
5. **Rehearse** — timed, aloud, with at least two reviewers using `templates/feedback-rubric.md`.
6. **Improve** — Pareto the comments, fix the vital few, rehearse again.
7. **Deliver** — to the real audience if possible.
8. **Follow up** — within 24 hours send the decision, actions, owners and dates.

## Assessment rubric

Reviewers score 1–5 on each criterion (the same rubric used in Module 07):

| Criterion | 5 looks like |
|---|---|
| Clear objective | the ask is stated in the first 30 seconds and again at the end |
| Audience fit | no unexplained jargon; content matches what this audience cares about |
| Structure | action titles alone tell the story; supporting points don't overlap |
| Data clarity | each chart makes one point, stated in its title; numbers have context and uncertainty |
| Delivery | on time; speaks to the audience; steady pace |
| Q&A handling | direct, brief, honest answers; "I'll find out" when needed |

A presentation **passes** if the average is ≥ 3.5 and no criterion is below 3 — and, if delivered for real, the purpose was achieved or the reason it wasn't is understood.

## Example: the Line 3 rollout, revised

Compare `examples/deck_draft.md` and `examples/deck_revised.md` side by side:

| | Draft | Revised |
|---|---|---|
| Ask | last slide, "consider rollout", no savings | slide 1 and the last slide: "Approve $38,000", ~$250k/yr, ~2-month payback |
| Titles | DMAIC phase names | full-sentence takeaways |
| Words per content slide | 10–76 | 0–26 |
| Statistics | on the main slides | in Appendix A |
| Savings math | absent | Appendix B, checkable by finance |
| Risk | not mentioned | Line 4 difference named, pilot planned, owner and timeline |

The outcome in the case: the plant manager approved the $38,000 with the condition that Line 4 be piloted first — which the deck had already proposed.

## Peer review etiquette

- Score against the rubric, not personal style.
- Give one thing to keep and one thing to change, each specific.
- Presenters: say "thank you" and write it down; decide later what to act on.

## After the course

- Keep your planner, storyboard and checklist as templates.
- Volunteer to present more often — skill grows with repetitions and feedback.
- Help your team adopt the checklist and action-title habit; it's the cheapest improvement most technical teams can make.
